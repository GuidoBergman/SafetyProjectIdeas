# Run Light Paper-Driven SAIM Pipeline (Autonomous)

A **lighter, paper-driven** alternative to `/run-pipeline`. Instead of mapping the whole landscape and fanning out ~10×N idea-generation subagents over thousands of sketches, this skill:

1. **Harvests every AI Safety paper from a fixed set of curated sources for the period** — the **ML Safety Newsletter**, the **AI Safety at the Frontier** newsletter, and **all publications by the top safety orgs** — plus any papers the coordinator names in the prompt.
2. **Generates ideas grounded in those papers** (extensions, follow-ups, replications-with-a-twist).
3. **Scores them** in bounded batches (no per-strategy fan-out, no per-idea scoring waves).
4. **Refines the survivors into full proposals** (batched — a few subagents, not one per idea).
5. **Ranks** the proposals, then runs **calculated novelty on the top 100**.

Everything is written into **one isolated run directory** under `data/runs/`. This skill does **not** persist into the shared `data/ideas/` catalogue and does **not** overwrite the shared `data/output/ranked_proposals.md` — the run is kept separate so the coordinator can merge it later by hand.

> **Why it's still lighter than `/run-pipeline`:** ideas are anchored to a finite harvested paper list (~2 ideas/paper) instead of fanning out ~10×N strategy×subfield subagents over thousands of speculative sketches; discovery/generation/score/refine all run as **batched** subagents (per batch, never per paper or per idea); and estimated novelty runs inline (free) before a single calculated-novelty pass. Note: an exhaustive harvest can still surface many papers — the cost scales with the curated source volume, not with brute-force ideation.

**Source reading policy (entire skill):** NEVER read full papers or full posts. Abstracts, summaries, introductions, and (for novelty) the specific sections that could change a verdict only. WebFetch targets summary/abstract/landing pages, or `arxiv.org/html/<id>` for a specific section.

---

## Phase 0: Resolve Parameters (no dialog — use defaults)

**Do not ask the coordinator anything.** Run on the fixed defaults below. The only input that ever overrides them is what the coordinator writes in the prompt (e.g. "also include paper X", "use a 3-month window", "skip novelty").

**Fixed defaults:**

| Parameter | Default |
|---|---|
| Time window | **Last 2 months** from today — compute the cutoff date (today minus ~2 months) and state it explicitly. |
| Sources | **Exhaustive** over the curated set (see Phase 2): ML Safety Newsletter, AI Safety at the Frontier, all top-safety-org publications, plus Alignment Forum / LessWrong (credibility-filtered). |
| Coverage | **Include every paper** found in those sources within the window — no top-N cap. |
| Ideas per paper | **~2** (1 for thin/narrow papers, up to 3 for rich ones). Idea count is driven by the paper count, not a fixed cap. |
| Calculated novelty (`topN`) | **100** (all proposals at this scale). |
| Persistence | **None** — run-local, isolated run dir. |

**Coordinator-named papers:** if the prompt mentions specific papers/URLs to include, collect them into a `must_include` list and **force-add them** in Phase 2 (they bypass any filtering).

Load the active profiles (for embedding into prompts — not for asking questions):

```bash
uv run python -m saim.config.cli show-participant
uv run python -m saim.config.cli show           # default team
uv run python -m saim.config.cli show-scoring   # criteria + active weights + thresholds
```

Echo the resolved parameters in one line, then proceed without pausing:
> **Running light pipeline with:** window=[since DATE], sources=[ML Safety Newsletter, AI Safety at the Frontier, top-org pubs, AF/LW], coverage=exhaustive, ideas_per_paper≈2, topN_novelty=100, must_include=[…], participant=[name], team=[name] — isolated run dir, no catalogue persist.

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

---

## Phase 2: Exhaustive Paper Harvest (parallel subagents → `source/`)

The goal here is **completeness**, not a curated top-N: harvest **every** paper from the curated sources published within the window. Launch the following subagents **in a single message**. The first two (newsletters) are the priority — they are human-curated lists of the period's notable safety papers, so every paper they cite goes in.

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
3. **Do NOT apply a top-N cap.** Keep every paper from the newsletters, org sweeps, and `must_include`. The **only** filter is the credibility gate, and it applies **only** to the AF/LW cluster — newsletter and org papers are pre-curated and kept wholesale.
4. Assign a stable `paper_id` (`p001`, `p002`, …).

Write the digest to `source/papers.md` (a readable table: paper_id, title, org/venue, date, url, discovered_via, key_result, open_threads, code) and keep the JSON list in memory for Phase 3. Log:

```bash
uv run python -m saim.pipeline.orchestrator log <RUN_DIR> source info 'Paper harvest complete' '{"papers_total": <N>, "from_ml_safety_newsletter": <N>, "from_ai_safety_frontier": <N>, "from_orgs": <N>, "from_af_lw": <N>, "must_include": <N>, "since": "<CUTOFF_DATE>"}'
```

If the harvest yields zero papers, stop and report — do not fabricate sources.

---

## Phase 3: Paper-Grounded Idea Generation (batched → `generate/`)

Partition **all** harvested papers into batches of **~5 papers** and launch **one subagent per batch**, in waves of ~10 subagents at a time (the paper count is now driven by the exhaustive harvest, so there may be many batches — process them in waves rather than all at once). One subagent per *batch* (not per paper) is the key token saving vs. `/run-pipeline`.

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
>   "subfield": "best-fit subfield",
>   "generation_strategy": "one of the strategies above",
>   "confidence": 0.0-1.0
> }
> ```

**Orchestrator collects** all idea objects and dedupes near-identical titles (no max-ideas cap — every harvested paper should be represented). Assign sequential IDs `gen-001`, `gen-002`, …, add `run_id` (the run dir name), then write each as a compatible sketch file:

```bash
uv run python -m saim.pipeline.generate write <RUN_DIR> '<idea_json_with_idea_id_and_run_id>'
```

(`write` requires keys: `idea_id, run_id, title, problem, direction, why_it_matters, relevant_context, subfield, generation_strategy, confidence`.)

Log the count. If zero ideas, stop and report.

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
> ```json
> {
>   "idea_id": "...", "title": "<simple, intuitive title — short; let the research question carry the fuller framing>",
>   "research_question": "1-2 sentence core question",
>   "approach_outline": "3-5 sentences: methodology + key steps",
>   "proposed_first_experiments": ["concrete experiment 1 (what to do, what to measure, expected outcome)", "experiment 2", "experiment 3"],
>   "theory_of_impact_chain": "2-4 sentences: if this works → X → Y → improves safety because Z",
>   "strength_rationale": "2-3 sentences referencing top-scoring criteria",
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
  "sections": {
    "research_question": "...",
    "approach_outline": "...",
    "proposed_first_experiments": ["...", "...", "..."],
    "theory_of_impact_chain": "...",
    "strength_rationale": "...",
    "alternative_framings": [],
    "cited_sources": ["..."]
  }
}
```

Then write it:

```bash
uv run python -m saim.pipeline.refine write <RUN_DIR> '<proposal_json>'
```

Log the count of proposals written. If a refine subagent fails, fall back to a minimal proposal (map `problem→research_question`, `direction→approach_outline`, `why_it_matters→theory_of_impact_chain`) for its ideas and record a warning.

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
  'window_since': '<CUTOFF_DATE>',
  'sources': ['ml_safety_newsletter', 'ai_safety_frontier', 'top_org_pubs', 'alignment_forum_lesswrong'],
  'must_include_count': <N>,
  'papers_kept': <N>,
  'ideas_generated': <N>,
  'ideas_after_score': <N>,
  'proposals_refined': <N>,
  'topN_novelty': <N>,
  'already_solved_dropped': <N>,
  'persisted_to_catalogue': False,
})
"
```

---

## Phase 8: Final Report

Present:
1. **Run directory:** `<RUN_DIR>` (everything is here; nothing was written to `data/ideas/` or the shared `data/output/ranked_proposals.md`).
2. **Harvest coverage:** papers per source (ML Safety Newsletter / AI Safety at the Frontier / each org / AF-LW / coordinator), which newsletter issues were read, and **any source that failed or had no issue in the window** (so the coordinator knows the harvest's true completeness).
3. **Funnel:** papers harvested → ideas generated → survived scoring → refined into proposals → ranked → top-N novelty-assessed → final (after the `already_solved` gate).
4. **Top 10** from `<RUN_DIR>/rank/ranked_proposals.md`: rank, title, weighted score, novelty classification + method, source paper.
5. **Outputs:**
   - Papers digest: `<RUN_DIR>/source/papers.md`
   - Idea sketches: `<RUN_DIR>/generate/`
   - Full proposals: `<RUN_DIR>/refine/`
   - Ranking: `<RUN_DIR>/rank/ranked_proposals.{md,json}`
6. **To merge later:** the coordinator can copy chosen sketches into `data/ideas/`, or run `rank persist` on `ranked_proposals.json` (note: `persist` only writes ideas whose novelty is `novelty_assessed`).

---

## Autonomous Mode Rules

- **No interactive checkpoints.** Run on the Phase 0 defaults end-to-end; never call AskUserQuestion. The only coordinator input is what was already in the prompt (e.g. `must_include` papers, a different window).
- Thread the **same `<RUN_DIR>`** through every phase.
- Keep fan-out bounded: a handful of harvest subagents (2 newsletters + org-subset sweeps + AF/LW), one generation subagent per ~5-paper batch, one scoring subagent per ~25-idea batch, one refine subagent per ~15-idea batch, and novelty in waves of ~10. Run large batch sets in waves of ~10 subagents. Do not balloon into per-paper or per-idea subagents.
- **Never write outside `<RUN_DIR>`** in this skill (no `data/ideas/` persist, no shared `data/output/` overwrite) — the run is intentionally isolated.
- If a phase produces zero items, stop and report which phase emptied the funnel.

## Error Handling

- **A harvest subagent fails** (a newsletter archive is unreachable, an org index won't load): proceed with the other sources, but **record which source was missed** in run_meta and call it out in the final report — exhaustiveness is the goal, so a missed source is a real gap, not a silent omission. Zero papers total → stop.
- **A newsletter has no issue in the window:** note it (e.g. "AI Safety at the Frontier published no issue since [CUTOFF_DATE]") and continue.
- **A generation/scoring subagent fails:** proceed with successful batches; record a warning in run_meta.
- **WebSearch unavailable:** generation still runs from the paper digests; for novelty, fall back to `mostly_novel` (conservative, do not eliminate) and note it.
- **A `must_include` paper can't be found/fetched:** still include it with whatever metadata is available and flag that its abstract was unavailable — never silently drop a coordinator-named paper.
- Never silently skip a phase — if one is skipped, say so and why.
