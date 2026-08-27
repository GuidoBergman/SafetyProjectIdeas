# Run Light Paper-Driven SAIM Pipeline (Autonomous)

A **lighter, paper-driven** alternative to `/run-pipeline`. Instead of mapping the whole landscape and fanning out ~10×N idea-generation subagents over thousands of sketches, this skill:

1. **Harvests every AI Safety paper from a fixed set of curated sources for the period** — the **ML Safety Newsletter**, the **AI Safety at the Frontier** newsletter, and **all publications by the top safety orgs** — plus any papers the coordinator names in the prompt.
2. **Generates ideas grounded in those papers** (extensions, follow-ups, replications-with-a-twist).
2b. **Generates ideas from the harvest as a whole** — cross-paper gaps, contradictions, method transfers, measurement gaps — via four synthesis lenses that each see every paper at once.
3. **Scores them** in bounded batches (no per-strategy fan-out, no per-idea scoring waves).
4. **Refines the survivors into full proposals** (batched — a few subagents, not one per idea).
5. **Ranks** the proposals, then runs **calculated novelty on the top 100**.

Everything is written into **one isolated run directory** under `data/runs/`. This skill does **not** persist into the shared `data/ideas/` catalogue and does **not** overwrite the shared `data/output/ranked_proposals.md` — the run is kept separate so the coordinator can merge it later by hand.

> **Why it's still lighter than `/run-pipeline`:** ideas are anchored to a finite harvested paper list (~2 ideas/paper) instead of fanning out ~10×N strategy×subfield subagents over thousands of speculative sketches; discovery/generation/score/refine all run as **batched** subagents (per batch, never per paper or per idea); and estimated novelty runs inline (free) before a single calculated-novelty pass. Note: an exhaustive harvest can still surface many papers — the cost scales with the curated source volume, not with brute-force ideation.

**Optional topic (`/run-pipeline-light <topic>`):** with no argument the run behaves exactly as described above — scoped by time window and source. Give it a topic and the run scopes to that topic instead: retrieval switches to two topic searches (**latest work**, and **top work of any age**) with the curated sweep demoted to a topic-filtered supplement, and the topic becomes a hard constraint in every generation prompt. See Phase 0.

**Source reading policy (entire skill):** NEVER read full papers or full posts. Abstracts, summaries, introductions, and (for novelty) the specific sections that could change a verdict only. WebFetch targets summary/abstract/landing pages, or `arxiv.org/html/<id>` for a specific section.

---

## Phase 0: Resolve Parameters (no dialog — use defaults)

**Do not ask the coordinator anything.** Run on the fixed defaults below. They are overridden by exactly two things: the optional **topic argument** (below), and what the coordinator writes in the prompt (e.g. "also include paper X", "use a 3-month window", "skip novelty").

### Topic argument (optional)

The coordinator may scope the whole run to a single research topic:

```
TOPIC_ARG: $ARGUMENTS
```

Read `TOPIC_ARG` above and resolve it:

- **Empty, absent, or the literal unexpanded token** → **no topic**. Run the untopiced path: every block below marked *"If a topic is set"* is skipped entirely and the run behaves exactly as it always has.
- **Otherwise** → that text is the topic.

If `TOPIC_ARG` did not expand but the coordinator's prompt plainly names a research area, use that instead.

**Do not mistake the existing prose overrides for a topic.** Strip these first: `must_include` paper names and URLs, window directives ("use a 3-month window"), and "skip novelty". A topic is what remains, and it names a **research area, question, technique, or failure mode** (e.g. "interpretability of reward models", "sandbagging in evals", "chain-of-thought faithfulness").

**If a topic is set,** derive these three artifacts **once, here**, and reuse them verbatim everywhere downstream. Deriving them once is the point: if twenty harvest and generation subagents each re-interpret the topic, each draws the boundary somewhere different and the scoping stops meaning anything. This mirrors how `participant_constraints` is translated once in Phase 1 and embedded unchanged in every prompt.

| Artifact | Content |
|---|---|
| `TOPIC` | The coordinator's text, verbatim. |
| `TOPIC_TERMS` | 5-8 query expansions: synonyms, acronyms, the canonical subfield name, common alternative phrasings, **plus at least one adjacent-but-distinct term to exclude** (so searches do not drift into a neighbouring field). |
| `TOPIC_SCOPE` | 2-3 sentences drawing an explicit **in-scope / out-of-scope boundary**. Say what a paper or idea must be *about* to count, and name the nearest thing that does *not* count. |

**Fixed defaults:**

| Parameter | Default |
|---|---|
| Time window | **Last 2 months** from today — compute the cutoff date (today minus ~2 months) and state it explicitly. *If a topic is set,* this window still governs the curated sweep, but the topic searches use their own windows (see Phase 2). |
| Sources | **Exhaustive** over the curated set (see Phase 2): ML Safety Newsletter, AI Safety at the Frontier, all top-safety-org publications, plus Alignment Forum / LessWrong (credibility-filtered). *If a topic is set,* topic search becomes the primary source and the curated sweep is demoted to a topic-filtered supplement. |
| Coverage | **Include every paper** found in those sources within the window — no top-N cap. |
| Ideas per paper | **~2** (1 for thin/narrow papers, up to 3 for rich ones). Idea count is driven by the paper count, not a fixed cap. |
| Calculated novelty (`topN`) | **100** (all proposals at this scale). |
| Persistence | **None** — run-local, isolated run dir. |

**Coordinator-named papers:** if the prompt mentions specific papers/URLs to include, collect them into a `must_include` list and **force-add them** in Phase 2 (they bypass any filtering — **including the topic filter**; never silently drop a paper the coordinator named, even if it sits outside the topic).

Load the active profiles (for embedding into prompts — not for asking questions):

```bash
uv run python -m saim.config.cli show-participant
uv run python -m saim.config.cli show           # default team
uv run python -m saim.config.cli show-scoring   # criteria + active weights + thresholds
```

Echo the resolved parameters in one line, then proceed without pausing:
> **Running light pipeline with:** topic=[TOPIC | none], harvest_mode=[sweep | topic_hybrid], window=[since DATE], sources=[…], coverage=exhaustive, ideas_per_paper≈2, topN_novelty=100, must_include=[…], participant=[name], team=[name] — isolated run dir, no catalogue persist.

If a topic is set, print `TOPIC_SCOPE` underneath the echo line so the coordinator can see the boundary the run is actually using.

---

## Phase 1: Init Run + Load Context

Create an isolated run directory and capture its path as `<RUN_DIR>` (thread it through every later phase):

```bash
uv run python -m saim.pipeline.orchestrator init source generate filter_score refine rank
```

Load the context that gets embedded into subagent prompts (so subagents never call config themselves):

```bash
uv run python -m saim.config.cli show-participant      # → participant_constraints
uv run python -m saim.config.cli show-scoring          # → criteria names + weights + thresholds
```

**Participant constraints:** translate the profile into a concrete bullet list (hours → scope, technical_skills → allowed methods, deliverables, goals). If no profile, `participant_constraints = "none specified"`.

**Counterfactual-value steering (always include in generation prompts):** prioritise ideas that are valuable to pursue **outside major labs** — no privileged access to frontier models, massive compute, or internal data required. Favour **direct extensions of the recent papers** discovered below over blue-sky proposals.

**If a topic is set:** write the resolved scope to `<RUN_DIR>/source/topic.md` before going further — `TOPIC`, `TOPIC_TERMS`, and `TOPIC_SCOPE`, exactly as derived in Phase 0. This is the run's record of how the topic was interpreted, and every downstream prompt quotes `TOPIC_SCOPE` from it verbatim rather than paraphrasing it.

---

## Phase 2: Exhaustive Paper Harvest (parallel subagents → `source/`)

The goal here is **completeness**: not a curated top-N, but **every** paper that qualifies. What "qualifies" means depends on the mode.

**This phase has two modes. Pick one and follow only its branch.**

| Mode | When | What runs |
|---|---|---|
| `sweep` | **No topic set** | Only the **Curated sweep** below (Subagents 1-4), exactly as always. Completeness means *every paper in the window*. Skip the Tier A block entirely. |
| `topic_hybrid` | **A topic is set** | **Tier A (topic search) is the primary source**, and the **Curated sweep runs as a topic-filtered supplement**. Completeness means *every paper on the topic*, whatever its date. |

---

### Tier A: Topic search — PRIMARY (only when a topic is set)

Skip this whole section if there is no topic.

The curated sweep is scoped by **time and publisher**, not by subject. For a specific topic it has near-zero recall on its own: two months of newsletters and org blogs may contain two relevant papers, and it structurally misses the topic's actual literature (academic work from labs outside the thirteen-org list). So when a topic is set, targeted search is the load-bearing mechanism and the sweep is the supplement, not the reverse.

Launch these three subagents **in a single message**, alongside the sweep subagents.

**Subagent A1 — Latest work on the topic.**

> You are finding the **most recent research** on this topic: **[TOPIC]**.
>
> **Scope boundary (obey it exactly):**
> [TOPIC_SCOPE]
>
> **Search terms to use and vary:** [TOPIC_TERMS]
>
> 1. Run WebSearch with at least **4 different phrasings** of the topic, including the canonical subfield name and one alternative terminology. Search arXiv listings as well as the open web.
> 2. Cover roughly the **last 12 months**. This is deliberately wider than the pipeline's usual 2-month window: a narrow topic does not produce enough recent work in 2 months to fill a funnel.
> 3. Abstracts and landing pages only — never read full papers.
> 4. Keep a paper only if it is genuinely **within the scope boundary** above. A paper that merely *uses* the topic's tools, or cites it as motivation while studying something else, is out of scope.
>
> Return a JSON array per the schema below. Set `"discovered_via": "topic_search_latest"`.

**Subagent A2 — Top / canonical work on the topic (NO time window).**

> You are finding the **most important papers of all time** on this topic: **[TOPIC]** — the work anyone entering this topic must know. **There is no date cutoff.** An old paper is exactly what is wanted if it is still the best or most recent trustworthy work on the question.
>
> **Scope boundary (obey it exactly):**
> [TOPIC_SCOPE]
>
> **Search terms to use and vary:** [TOPIC_TERMS]
>
> 1. Start with WebSearch to identify candidate titles (surveys, "seminal", "foundational", highly-cited work, and the papers that later work repeatedly builds on).
> 2. For each candidate, get the **citation signal** using the project's lookup tools:
>    ```bash
>    uv run python -m saim.verification.citation search-crossref "<title>"
>    uv run python -m saim.verification.citation search-s2 "<title>"
>    ```
>    Use the returned metadata (venue, authors, citation count) to judge standing. Do not invent citation counts.
> 3. Return the **10-20 strongest** by citation signal and centrality to the topic. Abstracts only.
> 4. Apply the project credibility standard: peer-reviewed venues first, preprints acceptable when the authors are established, unknown-author preprints excluded.
>
> Return a JSON array per the schema below. Set `"discovered_via": "topic_search_foundational"`. In `open_threads`, prioritise **what the paper left unresolved that later work still has not settled** — these papers feed the synthesis pass, so the gaps matter more than the results.

**Subagent A3 — Alignment Forum / LessWrong on the topic.**

> Find substantive AI-safety posts on **[TOPIC]** on Alignment Forum / LessWrong. WebSearch with `allowed_domains: ["alignmentforum.org","lesswrong.com"]`, varying the phrasing across [TOPIC_TERMS]. No date cutoff, but prefer recent.
>
> **Scope boundary (obey it exactly):**
> [TOPIC_SCOPE]
>
> **Apply the project credibility gate:** include a post only if its author is an established/credible AI-safety researcher (and preferably it is highly upvoted); discard posts from unknown authors. Set `"discovered_via": "topic_search_af_lw"`.

---

### Curated sweep (always runs; topic-filtered when a topic is set)

Launch the following subagents **in a single message**. The first two (newsletters) are the priority — they are human-curated lists of the period's notable safety papers, so every paper they cite goes in.

**If a topic is set,** add this instruction to **each** of the four sweep subagent prompts below, and treat the sweep as a supplement to Tier A rather than the main event:

> **Topic filter.** This run is scoped to **[TOPIC]**.
> **Scope boundary:** [TOPIC_SCOPE]
> Enumerate the window exhaustively as instructed, but **return only papers inside that boundary**. Additionally return `"dropped_count": <how many in-window papers you excluded as off-topic>` and `"near_misses": [<up to 5 titles you judged borderline>]`, so the coordinator can see what the filter removed.

**Subagent 1 — ML Safety Newsletter.**

> You are extracting **every research paper** referenced in the **ML Safety Newsletter** (the Center for AI Safety / Dan Hendrycks newsletter, `newsletter.mlsafety.org`, also on Substack) for issues published since [CUTOFF_DATE].
>
> 1. Find the newsletter's issue index (WebSearch "ML Safety Newsletter", then its archive page). Identify **all issues dated on/after [CUTOFF_DATE]**.
> 2. For each such issue, WebFetch the issue page and extract **every paper/work it links or summarises**, across all of its sections (e.g. robustness, monitoring, alignment, systemic safety).
> 3. Read only the newsletter's summary of each paper plus the paper's abstract/landing page — never full papers.
>
> Return a JSON array (one object per paper) using the schema in the orchestrator note below. Set `"discovered_via": "ml_safety_newsletter"` and `"issue_url"` to the issue it came from. **Do not drop papers for being minor** — include all of them.

**Subagent 2 — AI Safety at the Frontier.**

> You are extracting **every research paper** referenced in the **"AI Safety at the Frontier"** newsletter (Substack — search "AI Safety at the Frontier newsletter") for issues/posts published since [CUTOFF_DATE].
>
> 1. Find its archive; identify **all issues on/after [CUTOFF_DATE]** (including the monthly "paper of the month" and the "shorter reads" / other-papers sections).
> 2. WebFetch each issue and extract **every paper it discusses or links**.
> 3. Newsletter summary + paper abstract only — no full reads.
>
> Return a JSON array per the schema below. Set `"discovered_via": "ai_safety_frontier"` and `"issue_url"`. Include all papers, not just the headline one.

**Subagent 3 (split into one subagent per ~3 orgs) — Top safety org publications.**

> You are listing **all AI-safety research publications released since [CUTOFF_DATE]** by these organisations: **[ORG SUBSET]**. Go to each org's publications/research/blog index and enumerate everything in the window — this is an **exhaustive** sweep, not a highlight reel.
>
> Cover the full org set across subagents: **Anthropic, Google DeepMind (safety/alignment), OpenAI (safety/preparedness), Redwood Research, Apollo Research, METR, UK AISI, US AISI (CAISI), FAR AI, Center for AI Safety (CAIS), MIRI, EleutherAI, GovAI**.
> Use each org's own publications page (WebFetch the index) plus WebSearch as backup. Abstracts/landing pages only.
>
> Return a JSON array per the schema below. Set `"discovered_via": "org:<org name>"`. Include every publication in the window.

**Subagent 4 — Alignment Forum / LessWrong (credibility-filtered).**

> Find substantive AI-safety research posts on Alignment Forum / LessWrong published since [CUTOFF_DATE]. WebSearch with `allowed_domains: ["alignmentforum.org","lesswrong.com"]`. **Apply the project credibility gate:** include a post only if its author is an established/credible AI-safety researcher (and preferably it is highly upvoted); discard posts from unknown authors. Set `"discovered_via": "alignment_forum_lesswrong"`.

**Per-paper JSON schema (all subagents):**
```json
{
  "title": "...", "authors": "...", "org_or_venue": "...", "url": "...",
  "date": "YYYY-MM", "summary": "2-3 sentences: what it found/claims",
  "key_result": "the single most important result/claim",
  "open_threads": "limitations / explicitly-stated open questions / obvious extensions",
  "code_available": true|false|"unknown",
  "discovered_via": "...", "issue_url": "<if from a newsletter, else null>",
  "credibility": "1 sentence: venue + author standing + citation signal"
}
```

**Orchestrator merges:**
1. Concatenate all arrays **plus the `must_include` papers** from Phase 0 (fetch each named paper's abstract to fill the schema; mark `"discovered_via": "coordinator"`).
2. **Dedupe by normalised title / arXiv id / URL.** When the same paper appears in multiple sources, keep one record but record all `discovered_via` values.
3. **Do NOT apply a top-N cap.** Two filters exist, and no others:
   - **The credibility gate.** It applies to the AF/LW cluster **and to both `topic_search_*` clusters** — open academic and web search return unvetted preprints, whereas newsletter and org papers are pre-curated. Newsletter and org papers are still kept wholesale.
   - **The topic filter, only when a topic is set.** The sweep subagents have already applied it at source; apply it here to anything they missed. In a run with **no topic this filter does not exist**, and the merge behaves exactly as it always has.

   `must_include` papers bypass **both** filters.
4. Assign a stable `paper_id` (`p001`, `p002`, …).
5. **Mark the foundational set.** Papers whose `discovered_via` is `topic_search_foundational` are flagged `"role": "context"`. Every other paper is `"role": "extend"`. Phase 3 treats the two differently: only `extend` papers get per-paper idea generation, while `context` papers feed the synthesis pass and the shared background digest. This is deliberate — proposing an extension to a heavily-cited five-year-old paper usually reproposes work that the last five years already did.

**Thin-harvest escalation (only when a topic is set).** A narrow topic returning almost nothing is the most likely way a topic run fails, so handle it explicitly instead of quietly producing a four-idea run. Let `P` = the number of `role: extend` papers after merge:

| `P` | Action |
|---|---|
| `P >= 12` | Proceed. |
| `5 <= P < 12` | **Widen A1 once:** re-run Subagent A1 over the last **24 months** with 2 extra query phrasings (alternative terminology, and the field's canonical acronym). **Do not re-run the sweep** — it is bound to publication cadence, so it costs the most for the least. Re-merge and proceed regardless of the new count. Record `topic_window_widened: true`. |
| `P < 5` after widening | Proceed, but raise **ideas per paper from ~2 to ~4-5** so the funnel is not starved, and warn in the final report that the topic may be too narrow or mis-specified. List the sweep's `near_misses` so the coordinator can judge whether the boundary was drawn too tightly. |
| `P == 0` | Stop and report (see below). Suggest running `/research-topic [TOPIC]` first to check the topic has a literature at all. |

Never pad the harvest with off-topic papers to reach a threshold.

Write the digest to `source/papers.md` (a readable table: paper_id, title, org/venue, date, url, discovered_via, key_result, open_threads, code) and keep the JSON list in memory for Phase 3. Log:

```bash
uv run python -m saim.pipeline.orchestrator log <RUN_DIR> source info 'Paper harvest complete' '{"papers_total": <N>, "topic": "<TOPIC or null>", "harvest_mode": "<sweep|topic_hybrid>", "from_topic_latest": <N>, "from_topic_foundational": <N>, "from_topic_af_lw": <N>, "from_ml_safety_newsletter": <N>, "from_ai_safety_frontier": <N>, "from_orgs": <N>, "from_af_lw": <N>, "must_include": <N>, "dropped_off_topic": <N>, "window_widened": <true|false>, "since": "<CUTOFF_DATE>"}'
```

If the harvest yields zero papers, stop and report — do not fabricate sources.

---

## Phase 3: Paper-Grounded Idea Generation (batched → `generate/`)

Partition the **`role: extend`** papers into batches of **~5 papers** and launch **one subagent per batch**, in waves of ~10 subagents at a time (the paper count is now driven by the exhaustive harvest, so there may be many batches — process them in waves rather than all at once). One subagent per *batch* (not per paper) is the key token saving vs. `/run-pipeline`.

**`role: context` papers are not batched here.** They are the foundational papers from Subagent A2, and they exist to inform rather than to be extended. They appear in every batch prompt as shared background (so ideas do not re-propose settled work) and they feed the synthesis pass in Phase 3b. In a run with no topic there are no `context` papers, so this partition is a no-op and every harvested paper is batched exactly as before.

**Subagent prompt template** (per batch):

> You are generating AI-Safety research idea sketches **grounded in specific recent papers**.
>
> **Your papers (with paper_id, summary, key_result, open_threads, code):**
> [JSON DIGEST OF THIS BATCH'S PAPERS]
>
> For **each** paper, propose **~2** concrete idea sketches that *extend* it (1 for a thin/narrow paper, up to 3 for a rich one) — using these strategies, picking whichever fit best:
> - **follow_up_experiment** — explain or pin down a surprising result the paper reports.
> - **experiment_variation** — vary model family / dataset / modality / scale.
> - **replication_with_twist** — replicate a key result under a changed condition (beginner-friendly).
> - **tool_or_benchmark_gap** — turn an open thread into a measurement, eval, or small benchmark.
> - **failure_mode_investigation** — characterise a limitation the authors acknowledge.
>
> **Counterfactual-value constraint (hard):** every idea must be feasible **outside a major lab** — no privileged frontier-model access, no massive compute, no internal datasets. Prefer open models, public datasets, inference-only or lightweight-finetune methods.
>
> **Topic constraint (hard — include this block ONLY when a topic is set):** every idea must be **about [TOPIC]**.
> **Scope boundary:** [TOPIC_SCOPE]
> An idea is in scope when **the research question itself sits inside the topic**. It is *not* in scope merely because it *uses* the topic's tools, or mentions the topic in its motivation. For the topic "interpretability of reward models": training a probe to detect jailbreaks is *using* interpretability, not *studying* reward-model interpretability — out of scope.
> If a paper's natural extensions all fall outside the boundary, return **fewer ideas, or none, for that paper**, and say which paper you skipped and why. Do not stretch an off-topic extension to fill a quota.
>
> **Background — foundational work on this topic (do NOT generate ideas from these; use them to avoid re-proposing settled work):**
> [COMPACT DIGEST OF THE `role: context` PAPERS: title, year, key_result — one line each. Omit this block entirely when there are none.]
>
> **Participant constraints (all ideas MUST satisfy):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> Ground each idea in its source paper. You MAY run 1 quick WebSearch (abstracts only) if needed to avoid duplicating obvious prior work, but do not deep-read.
>
> Return a JSON array; each object:
> ```json
> {
>   "title": "...",
>   "problem": "what gap/question (1-2 sentences)",
>   "direction": "the proposed approach (2-4 sentences)",
>   "why_it_matters": "safety relevance + theory of impact (1-3 sentences)",
>   "relevant_context": "grounding: cite the source paper title + the specific result being extended",
>   "source_paper_id": "pNN",
>   "source_paper": "Title — url",
>   "subfield": "best-fit subfield — but if a topic is set, use [TOPIC] verbatim here",
>   "generation_strategy": "one of the strategies above",
>   "confidence": 0.0-1.0
> }
> ```

**Orchestrator collects** all idea objects and dedupes near-identical titles (no max-ideas cap — every `role: extend` paper should be represented, **unless the topic constraint ruled out all of its extensions**, in which case record it as skipped and report it in Phase 8). Mint one ID per idea with the shared generator — never invent IDs by hand, and never use sequential IDs (they collide across runs and batches):

```bash
uv run python -m saim.ids <number_of_ideas>
```

Assign the printed IDs (e.g. `gen-3f9a1c04`) to the ideas in order, add `run_id` (the run dir name), then write each as a compatible sketch file:

```bash
uv run python -m saim.pipeline.generate write <RUN_DIR> '<idea_json_with_idea_id_and_run_id>'
```

(`write` requires keys: `idea_id, run_id, title, problem, direction, why_it_matters, relevant_context, subfield, generation_strategy, confidence`.)

Log the count. If zero ideas, stop and report.

---

## Phase 3b: Whole-Harvest Synthesis (parallel lenses → `generate/`)

**This phase runs on every run, with or without a topic.**

Everything in Phase 3 is generated by a subagent that sees only its own ~5 papers, so no idea can ever come from looking *across* the harvest. That rules out an entire class of the best ideas: the assumption every paper on a question quietly shares but none tests, the two results that cannot both be right, the thing the whole literature measures badly. This phase recovers them. It is the light-pipeline counterpart to the cross-subfield synthesis in `/generate-ideas` (Phase 2b).

Build a **compact digest of the entire harvest** — one line per paper: `paper_id`, title, year, `key_result`, `open_threads`. One line each, not the full summaries: on a 60-paper sweep the full digest is too large to reason over, and the compact form is what makes cross-paper comparison possible at all. Include **both** `role: extend` and `role: context` papers; the foundational papers matter most here.

Launch **four subagents in a single message**, one per lens. They share the same prompt skeleton and differ only in the lens block.

**Shared skeleton (all four):**

> You are generating AI-Safety research idea sketches by looking **across an entire body of work at once**, not by extending any single paper.
>
> **The full harvest (one line per paper):**
> [COMPACT DIGEST — ALL PAPERS]
>
> [TOPIC BLOCK — include only when a topic is set:]
> **Topic constraint (hard):** every idea must be **about [TOPIC]**.
> **Scope boundary:** [TOPIC_SCOPE]
>
> **Your lens:** [ONE OF THE FOUR BELOW]
>
> **Counterfactual-value constraint (hard):** every idea must be feasible **outside a major lab** — no privileged frontier-model access, no massive compute, no internal datasets. Prefer open models, public datasets, inference-only or lightweight-finetune methods.
>
> **Participant constraints (all ideas MUST satisfy):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> Propose **4-6** idea sketches through your lens. Every idea must **name the specific papers it draws on** (by `paper_id` and title) and explain what about *the relationship between them* produces the idea. An idea that could have been written from one paper alone does not belong in this phase — discard it and find a real cross-paper one. Prefer 4 genuine ones over 6 padded ones.
>
> You MAY run 1 quick WebSearch (abstracts only) to avoid duplicating obvious prior work. Do not deep-read.
>
> Return a JSON array; each object:
> ```json
> {
>   "title": "...",
>   "problem": "what gap/question (1-2 sentences)",
>   "direction": "the proposed approach (2-4 sentences)",
>   "why_it_matters": "safety relevance + theory of impact (1-3 sentences)",
>   "relevant_context": "which papers this draws on and what about their relationship produces the idea",
>   "source_paper_id": "synthesis",
>   "source_paper": "pNN Title; pNN Title; … (every paper this idea rests on)",
>   "subfield": "best-fit subfield — but if a topic is set, use [TOPIC] verbatim here",
>   "generation_strategy": "<your lens name>",
>   "confidence": 0.0-1.0
> }
> ```

**The four lenses:**

1. **`cross_paper_gap`** — Find assumptions that **many papers share but none tests**: the setup everyone inherits, the metric everyone reuses without validating, the condition every experiment holds fixed. Propose work that tests the assumption itself. Name which papers share it.
2. **`contradiction_resolution`** — Find papers whose results, framings, or implicit predictions **cannot all be right**: incompatible findings, a result that fails to replicate under another paper's conditions, two papers whose recommendations conflict. Propose the experiment that would settle it. Name both sides. If you find no genuine contradiction, say so and return fewer ideas rather than manufacturing one.
3. **`methodology_bridging`** — Find a method that is **proven in one paper** and an **open problem in another** where it has not been tried, and propose the transfer. Name the source paper (where the method works) and the target paper (whose problem it would attack), and say why the transfer is plausible rather than merely novel.
4. **`measurement_gap`** — Ask what this body of work **measures badly or not at all**: results that are not comparable because everyone uses a different setup, a claim everyone makes that no benchmark checks, an effect reported anecdotally across papers but never quantified. Propose the eval, benchmark, or measurement that would fix it.

**Orchestrator collects** the four arrays, dedupes near-identical titles **against each other and against the Phase 3 ideas**, mints IDs with `uv run python -m saim.ids <count>`, adds `run_id`, and writes each with `saim.pipeline.generate write` exactly as in Phase 3. These ideas then flow through scoring, refinement, and ranking identically to the per-paper ones — nothing downstream treats them specially.

Log the count separately (`synthesis_ideas`). If a lens subagent fails or genuinely finds nothing, record a warning and continue: this phase is additive, and an empty lens is not a reason to stop the run.

---

## Phase 4: Score Inline (batched → in-memory)

Batch the generated ideas into a few groups (~25 ideas each → ~2–4 subagents). Launch **one scoring subagent per batch** in a single message.

**Subagent prompt template:**

> You are scoring AI-Safety research ideas against the team's criteria.
>
> **Criteria, weights, and rubrics (excluding novelty):**
> [FOR EACH CRITERION from show-scoring: name, active_weight, full 5-level rubric]
>
> **Ideas to score:**
> [JSON ARRAY OF THIS BATCH'S IDEAS — full objects]
>
> For each idea: score every non-novelty criterion 1-5 by matching the rubric level (not gut feeling), with a 1-sentence reason and a 0.0-1.0 confidence. Then produce an **estimated** novelty (1-5) from your own knowledge only — NO web search (calculated novelty runs later on the top ideas).
>
> Compute `weighted_score` = Σ(score×weight)/Σ(weight) over the **non-novelty** criteria. Compute `confidence` = mean of per-criterion confidences.
>
> Return a JSON array; each object:
> ```json
> {
>   "idea_id": "...", "title": "...", "run_id": "...",
>   "scores": {
>     "<criterion>": {"score": 1-5, "reasoning": "...", "confidence": 0.0-1.0},
>     "novelty": {"score": 1-5, "reasoning": "estimate, no search", "confidence": 0.0-1.0}
>   },
>   "novelty_classification": "already_solved|largely_addressed|partially_addressed|mostly_novel|novel",
>   "novelty_score": 1-5,
>   "novelty_method": "novelty_estimated",
>   "weighted_score": <float, excl. novelty>,
>   "confidence": <float>
> }
> ```
> Estimated-novelty rubric: already_solved=1, largely_addressed=2, partially_addressed=3 (default when unsure), mostly_novel=4, novel=5.

**Orchestrator** merges results, joins them back to the full idea objects (keep `problem/direction/why_it_matters/source_paper/subfield/generation_strategy`), and applies the **Stage-2 weighted-score threshold** from `show-scoring` to drop weak ideas. Keep the survivors (the full scored objects) for refinement.

---

## Phase 5: Refine into Full Proposals (batched → `refine/`)

Refine the surviving scored ideas into full proposals. Keep this **batched** (group survivors into ~15-idea batches → a few subagents) rather than the per-idea weakness-analysis loop of `/refine-ideas` — that is the token saving while still producing genuine full proposals.

**Subagent prompt template** (per batch):

> You are turning scored AI-Safety research ideas into full, fundable research proposals.
>
> **Criteria + rubrics (for strengthening weak dimensions):**
> [CRITERIA NAMES + WEIGHTS + RUBRICS from show-scoring]
>
> **Participant constraints (proposals MUST satisfy):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> **Counterfactual-value constraint (hard):** the proposal must be executable outside a major lab — open models, public data, modest compute.
>
> **Scored ideas (each with its scores, weak dimensions, and source paper):**
> [JSON ARRAY OF THIS BATCH'S SCORED IDEAS]
>
> For each idea: first identify its weakest-scoring criteria and concretely strengthen the idea on those dimensions; then assemble the full proposal grounded in its source paper. Follow the proposal writing rules in `writing-guidelines.md` (self-contained, plain, brief, no em dashes; simple intuitive title). Return a JSON array; each object:
> **Rules that decide whether the proposal is usable:**
> 1. `tldr` is capped at 45 words and is the line that represents this idea in a ranked list of hundreds.
> 2. `day1_check` names an artifact to obtain and a number to measure, doable in under four hours with no training. "Read the literature" is not one. Return `""` if none exists.
> 3. Every risk names the experiment that detects it, and its response is stop / retry with a named change / mitigate with a named change. A risk you cannot detect or respond to is a worry, not a risk. Leave it out.
> 4. A result that falsifies the hypothesis is a finding, not a risk.
> 5. `why_this_matters` names a mechanism, not a category. For pathways B/C/D/E, `where_the_chain_ends` names the concrete decision the chain terminates in.
> 6. `who_this_is_for` names an org or team, never "researchers" or "the community".
> 7. No score numbers or criterion names outside `scores_rationale`.
>
> ```json
> {
>   "idea_id": "...", "title": "<simple, intuitive title — short; let the research question carry the fuller framing>",
>   "tldr": "<max 45 words>",
>   "pathway": "<exactly one of A, B, C, D, E>",
>   "named_party": "<the org or team that would act>",
>   "research_question": "1-2 sentence core question",
>   "why_this_matters": {
>     "failure_this_targets": "<specific mechanism>",
>     "why_the_work_reduces_it": "<2-3 sentences>",
>     "where_the_chain_ends": "<concrete decision for B/C/D/E, \"\" for A>"
>   },
>   "day1_check": "<under 4h, names an artifact and a number, or \"\">",
>   "approach_outline": "3-5 sentences: methodology + key steps",
>   "scope_and_deliverables": "<hours and weeks in 2-3 stages, each able to stop the next, then the concrete artifact>",
>   "proposed_first_experiments": ["concrete experiment 1 (what to do, what to measure, expected outcome)", "experiment 2", "experiment 3"],
>   "risks": [{"name": "...", "consequence": "...", "detected_by": "...", "response": "..."}],
>   "prerequisites": ["<compute, access, data or skill needed to start>"],
>   "who_this_is_for": "<org or team, what they do today, what they would do differently>",
>   "open_questions": ["<genuinely unresolved>"],
>   "scores_rationale": "2-3 sentences referencing top-scoring criteria",
>   "weak_dimensions_strengthened": ["criterion", "..."],
>   "cited_sources": ["<source paper title — url>", "<any other grounding source>"]
> }
> ```

**Orchestrator** assembles a full proposal dict per idea and writes it to `refine/` (compatible with the refine data model, so the run is mergeable/persistable later). For each idea build:

```json
{
  "idea_id": "...", "run_id": "<run dir name>", "stage": "refine",
  "title": "...",
  "original_scores": { "<criterion>": <int>, ... },
  "novelty_classification": "<from scoring>", "novelty_score": <1-5>, "novelty_method": "novelty_estimated",
  "pre_refine_weighted_score": <float>,
  "weak_dimensions_addressed": ["..."],
  "generation_strategy": "<strategy>", "subfield": "<subfield>",
  "provenance": {"generation_method": "paper_driven_light", "kb_sources": [], "web_sources": ["<source paper url>"]},
  "scores": { ...full per-criterion scores incl. novelty from Phase 4... },
  "confidence": <float>,
  "tldr": "...", "pathway": "<A-E>", "named_party": "...",
  "sections": {
    "research_question": "...",
    "why_this_matters": "**The failure this targets:** ...\n\n**Why the work reduces it:** ...\n\n**Where the chain ends:** ...",
    "day1_check": "...",
    "approach_outline": "...",
    "scope_and_deliverables": "...",
    "proposed_first_experiments": ["...", "...", "..."],
    "risks": [{"name": "...", "consequence": "...", "detected_by": "...", "response": "..."}],
    "prerequisites": ["..."],
    "who_this_is_for": "...",
    "open_questions": ["..."],
    "scores_rationale": "...",
    "alternative_framings": [],
    "cited_sources": ["..."]
  }
}
```

The three parts of `why_this_matters` are joined into one prose section with their labels, as shown. `risks` stays structured: `refine write` renders it and reads it back.

Then write it:

```bash
uv run python -m saim.pipeline.refine write <RUN_DIR> '<proposal_json>'
```

Log the count of proposals written. If a refine subagent fails, fall back to a minimal proposal (map `problem→research_question`, `direction→approach_outline`, `why_it_matters→why_this_matters`, leaving `tldr`, `day1_check`, `risks` and `who_this_is_for` empty) for its ideas and record a warning.

---

## Phase 6: Rank (isolated — run dir only)

Load the refined proposals back and rank them:

```bash
uv run python -m saim.pipeline.refine read <RUN_DIR>
```

Each proposal returned by `refine read` already carries `scores`, `sections`, novelty, and provenance — exactly the fields `format_ranked_output` and `persist_ideas` expect. Compute `weighted_score` from the per-criterion `scores` (excluding novelty) using the active weights from `show-scoring`, sort the proposals descending, and add a 1-based `rank` to each. **Write the ranked output directly into the run dir only** (do NOT call `rank write` or `rank persist` — those overwrite the shared `data/output/ranked_proposals.md` and the `data/ideas/` catalogue, which breaks run isolation):

1. Write the ranked JSON list to `<RUN_DIR>/rank/ranked_proposals.json` (use the Write tool).
2. Render the markdown with the shared formatter, writing it **only** inside the run dir:

```bash
uv run python -c "
import json
from pathlib import Path
from saim.pipeline.rank import format_ranked_output
rd = Path('<RUN_DIR>')
ranked = json.loads((rd/'rank'/'ranked_proposals.json').read_text())
(rd/'rank'/'ranked_proposals.md').write_text(format_ranked_output(ranked))
print('wrote', rd/'rank'/'ranked_proposals.md')
"
```

---

## Phase 7: Calculated Novelty on Top-100 (run-local)

For each of the top-`topN` ranked proposals (default **100** — effectively all of them at this scale), run the **`/novelty-check`** protocol (the 2-subagent academic + LW/AF search, two-tier problem-then-method strategy, abstracts/targeted-sections only). To keep fan-out bounded, process them in **waves** (e.g. ~10 proposals' novelty checks in flight at a time) rather than launching 100 simultaneously.

For each assessed proposal, update its object in `ranked_proposals.json`: set `novelty_classification`, `novelty_score`, `novelty_method: "novelty_assessed"`, and fold the evidence into `scores.novelty.reasoning` and `sections.cited_sources`. **Apply the hard gate:** drop any proposal classified `already_solved`. Then re-sort by `weighted_score`, re-number `rank`, and re-write `ranked_proposals.json` + `ranked_proposals.md` (same run-dir-only commands as Phase 6).

Because every persisted-eligible proposal now carries `novelty_method: "novelty_assessed"`, the run is later mergeable into `data/ideas/` via `rank persist` with no estimated-only exclusions. If `topN = 0`, skip this phase (estimated novelty only — fine since nothing is auto-persisted here).

Write run metadata:

```bash
uv run python -c "
from pathlib import Path
from saim.pipeline.orchestrator import write_run_meta
write_run_meta(Path('<RUN_DIR>'), {
  'pipeline': 'run-pipeline-light',
  'topic': '<TOPIC>' or None,          # None when no topic was given — always emit the key
  'topic_terms': [<TOPIC_TERMS>],      # [] when no topic
  'topic_scope': '<TOPIC_SCOPE>',      # '' when no topic
  'harvest_mode': '<sweep|topic_hybrid>',
  'window_since': '<CUTOFF_DATE>',
  'sources': ['ml_safety_newsletter', 'ai_safety_frontier', 'top_org_pubs', 'alignment_forum_lesswrong'],
  'must_include_count': <N>,
  'papers_kept': <N>,
  'papers_topic_latest': <N>,          # 0 in a no-topic run
  'papers_topic_foundational': <N>,    # 0 in a no-topic run
  'papers_from_sweep': <N>,
  'papers_dropped_off_topic': <N>,
  'topic_window_widened': <True|False>,
  'ideas_generated': <N>,
  'synthesis_ideas': <N>,              # from Phase 3b — present in every run
  'ideas_after_score': <N>,
  'proposals_refined': <N>,
  'topN_novelty': <N>,
  'already_solved_dropped': <N>,
  'persisted_to_catalogue': False,
})
"
```

---

## Phase 7b: Publish the Idea Dashboard

Build this run's dashboard and publish it as an Artifact. The dashboard is how anyone other than the coordinator reads the run: ideas in rank order, full-text search and facet filters, and a **review status per idea that every viewer shares**.

**1. Build the page** (deterministic script, no subagent):

```bash
uv run python scripts/build_idea_dashboard.py <RUN_DIR> --title "SAIM Ideas <RUN_DATE>" --seed-status data/output/idea_tracker.md
```

It writes `<RUN_DIR>/dashboard.html`. Notes:
- `--title` must name the run (e.g. `SAIM Ideas 2026-08-27`) so two runs never publish under the same name.
- `--seed-status` pre-fills the status of ideas that are already in the tracker. Drop the flag if that file does not exist.
- The output is an **HTML fragment**, not a full document — the Artifact tool adds the document wrapper at publish time. Add `--standalone` only when you need a file that opens in a plain browser (shared status saving does not work there).

**2. Publish it with the Artifact tool:**
- `file_path`: `<RUN_DIR>/dashboard.html`
- `capabilities`: `{"artifact": {}}` — **required**. Without it the page loads read-only and nobody can save a status change.
- `favicon`: 💡
- `description`: one sentence naming the run and how many ideas it holds.

**3. Report the artifact URL** in the final report. The coordinator shares it from the artifact's share menu; anyone with an edit link can change a status and everyone else sees it on their next load.

Run this **after** calculated novelty, never before: the dashboard should carry assessed novelty, not estimated guesses.

**If the Artifact tool is unavailable:** say so plainly, re-run the build with `--standalone`, and leave the file in the run directory. The run is not a failure — the dashboard can be published later from another session.

---

## Phase 8: Final Report

Present:
1. **Run directory:** `<RUN_DIR>` (everything is here; nothing was written to `data/ideas/` or the shared `data/output/ranked_proposals.md`).
2. **Topic** (only if one was set): the topic as given, and the `TOPIC_SCOPE` boundary the run actually used, so the coordinator can tell whether it was interpreted as intended. Say if the window was widened, and if the harvest was thin.
3. **Harvest coverage:** papers per source (topic-latest / topic-foundational / topic-AF-LW / ML Safety Newsletter / AI Safety at the Frontier / each org / AF-LW / coordinator), which newsletter issues were read, and **any source that failed or had no issue in the window** (so the coordinator knows the harvest's true completeness). If a topic was set, also give **how many in-window papers the sweep dropped as off-topic** and its `near_misses` list — if the sweep kept 61 of 74, the topic barely filtered anything and the coordinator should know that.
4. **Funnel:** papers harvested → ideas generated (per-paper + synthesis, counted separately) → survived scoring → refined into proposals → ranked → top-N novelty-assessed → final (after the `already_solved` gate). Name any `role: extend` paper that produced zero ideas because the topic constraint ruled out all its extensions.
5. **Topic drift check** (only if a topic was set): this pipeline applies the topic as a prompt constraint, **not** as a scoring gate, so off-topic ideas are possible. Report **how many surviving ideas have a `subfield` that does not match the topic**, and list up to 5 of them. This is visibility, not a filter — the coordinator decides whether drift is a problem.
6. **Top 10** from `<RUN_DIR>/rank/ranked_proposals.md`: rank, title, weighted score, novelty classification + method, source paper (or `synthesis` plus the papers it drew on).
7. **Outputs:**
   - Papers digest: `<RUN_DIR>/source/papers.md`
   - Resolved topic scope: `<RUN_DIR>/source/topic.md` (topic runs only)
   - Idea sketches: `<RUN_DIR>/generate/`
   - Full proposals: `<RUN_DIR>/refine/`
   - Ranking: `<RUN_DIR>/rank/ranked_proposals.{md,json}`
   - Shared dashboard: the Artifact URL from Phase 7b
8. **To merge later:** the coordinator can copy chosen sketches into `data/ideas/`, or run `rank persist` on `ranked_proposals.json` (note: `persist` only writes ideas whose novelty is `novelty_assessed`).

---

## Autonomous Mode Rules

- **No interactive checkpoints.** Run on the Phase 0 defaults end-to-end; never call AskUserQuestion. The only coordinator input is the optional topic argument plus what was already in the prompt (e.g. `must_include` papers, a different window). **This holds even when the topic is vague or ambiguous** — do not ask what it means. Resolve it yourself, write the assumed `TOPIC_SCOPE` to `source/topic.md`, and report it in Phase 8 so the coordinator can correct it on the next run.
- Thread the **same `<RUN_DIR>`** through every phase.
- Keep fan-out bounded: a handful of harvest subagents (2 newsletters + org-subset sweeps + AF/LW, plus 3 topic-search subagents when a topic is set), one generation subagent per ~5-paper batch, 4 synthesis subagents in Phase 3b, one scoring subagent per ~25-idea batch, one refine subagent per ~15-idea batch, and novelty in waves of ~10. Run large batch sets in waves of ~10 subagents. Do not balloon into per-paper or per-idea subagents.
- **Never write outside `<RUN_DIR>`** in this skill (no `data/ideas/` persist, no shared `data/output/` overwrite) — the run is intentionally isolated.
- If a phase produces zero items, stop and report which phase emptied the funnel.

## Error Handling

- **A harvest subagent fails** (a newsletter archive is unreachable, an org index won't load): proceed with the other sources, but **record which source was missed** in run_meta and call it out in the final report — exhaustiveness is the goal, so a missed source is a real gap, not a silent omission. Zero papers total → stop.
- **A newsletter has no issue in the window:** note it (e.g. "AI Safety at the Frontier published no issue since [CUTOFF_DATE]") and continue.
- **A generation/scoring subagent fails:** proceed with successful batches; record a warning in run_meta.
- **WebSearch unavailable:** generation still runs from the paper digests; for novelty, fall back to `mostly_novel` (conservative, do not eliminate) and note it.
- **A `must_include` paper can't be found/fetched:** still include it with whatever metadata is available and flag that its abstract was unavailable — never silently drop a coordinator-named paper.
- **A topic-search subagent fails:** proceed with the remaining sources, but say plainly in the final report that on-topic recall is degraded — the sweep alone is a poor substitute for topic search.
- **The topic harvest is thin:** follow the escalation ladder in Phase 2 (widen A1 once, then raise ideas-per-paper, then warn). Never pad with off-topic papers to hit a count.
- **The topic yields zero papers:** stop and report. Suggest running `/research-topic [TOPIC]` first to check the topic has a literature at all, or that the topic was phrased in terms the field actually uses.
- **A Phase 3b synthesis lens finds nothing genuine:** record a warning and continue with the other lenses. A fabricated contradiction is worse than four ideas instead of six.
- Never silently skip a phase — if one is skipped, say so and why.
