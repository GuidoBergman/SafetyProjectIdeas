# Evaluate and Refine an AI Safety Research Idea

Collaboratively evaluate, refine, and strengthen a research idea — whether it comes from the pipeline or is submitted fresh by the user.

## Idea Tracker

The idea tracker (`IDEA_TRACKER_FILE` from `src/saim/constants.py`, default: `data/output/idea_tracker.md`) tracks the review status of every ranked idea. **You must update the tracker at each status transition during this skill.**

Status values:
- **Not reviewed** — default, idea has not been reviewed by the human
- **Not promising** — the collaborator manually marked this idea as not promising
- **Removed** — the idea was eliminated
- **Evaluating** — the idea is currently being evaluated with this skill
- **Added and needs manual review** — the idea was added to the selected ideas file and needs the human to manually review the content added
- **Added** — the idea was added to the selected ideas file and the content was reviewed by the human

To update the tracker, find the row matching the idea's ID in `data/output/idea_tracker.md` and replace the Status cell value.

## Setup

Load scoring configuration (criteria with rubrics and active weights):

```bash
uv run python -m saim.config.cli show-scoring
```

Load team profile:

```bash
uv run python -m saim.config.cli show
```

Load participant profile:

```bash
uv run python -m saim.config.cli show-participant
```

Save all configuration for use throughout the session.

## Step 1: Load or Accept the Idea

Ask the coordinator how they want to provide the idea:

> How would you like to provide the idea?
> 1. **Existing idea** — provide an idea ID (e.g., "gen-3f9a1c04") and I'll load it from `data/ideas/`
> 2. **New idea** — describe it and we'll build it up together

### If existing idea (option 1):

**Immediately update the idea tracker** status to **"Evaluating"** for this idea.

First check if the idea exists in the **selected ideas file** (`SELECTED_IDEAS_FILE`). If it does, treat that version as the most up-to-date — it may have been edited directly by the coordinator. Also read `data/ideas/<idea_id>.md` for the full YAML frontmatter. If the two versions differ, prefer the selected ideas file content and note the discrepancy.

Parse the full YAML frontmatter and markdown body. The idea has these structured fields:

**Frontmatter:**
- `idea_id`, `run_id`, `stage`, `rank`, `weighted_score`
- `title`, `subfield`, `generation_strategy`
- `research_field`: list of one or more AI safety research fields (e.g., Mechanistic Interpretability, AI Control, Adversarial Robustness, Alignment Science, Governance, Evaluations). **Required** — every idea must have at least one research field.
- `novelty_classification`, `novelty_score`, `novelty_method`
- `original_scores`: dict with `theory_of_impact`, `impact_pathway`, `accessible_complexity`, `narrow_scope`, `novelty` (each 1-5)
- `provenance`: dict with `generation_method`, `kb_sources` (list), `web_sources` (list)
- `timestamp`

**Body sections (H1 headings):**
- Research Question
- Approach Outline
- Proposed First Experiments
- Impact Pathway
- Theory Of Impact Chain
- Strength Rationale
- Alternative Framings
- Cited Sources

Present the full idea with all its contents — display every field and every body section in full, without truncating or summarizing. **Present them in a top-down reading order that leads with what the idea is about and defers the metadata**, so the coordinator reads the substance before the grades. Use this order:

1. **Title** (the headline)
2. **Research Question**
3. **Research field** and **subfield**
4. **Approach Outline**
5. **Proposed First Experiments**
6. **Impact Pathway**
7. **Theory Of Impact Chain**
8. **Strength Rationale**
9. **Alternative Framings**
10. **Cited Sources**
11. **Scores** — `original_scores` (theory_of_impact, impact_pathway, accessible_complexity, narrow_scope, novelty) and `weighted_score`
12. **Novelty** — `novelty_classification`, `novelty_score`, `novelty_method`
13. **Provenance & metadata** — `generation_strategy`, `provenance` (generation_method, kb_sources, web_sources), `idea_id`, `run_id`, `stage`, `rank`, `timestamp`

The point is that the reader should see the headline and research question first — never the scores before the substance.

Since this idea is **already scored**, do NOT re-score it. Go directly to **Step 4: Readiness Assessment**, then **Step 5: Collaborative Refinement**. Offer novelty re-assessment as an option (see Step 3).

**IMPORTANT — Live sync rule:** Throughout the session, whenever you edit the idea (any section — research question, approach, impact chain, scores, citations, etc.), apply the change to **both** `data/ideas/<idea_id>.md` **and** the idea's section in the selected ideas file (if it exists there). Do not wait for the "Save" action — keep both files in sync as you go. The selected ideas file uses a condensed format (see the "If save" section for details), so adapt the content accordingly when writing there.

### If new idea (option 2):

Guide the coordinator to describe their idea. Explain what a complete idea looks like in this system:

> To evaluate your idea thoroughly, I'll need:
> - **Title**: A simple, intuitive title (keep it short; let the research question carry the fuller framing)
> - **Research field**: Which AI safety research field(s) does this fall under? (e.g., Mechanistic Interpretability, AI Control, Adversarial Robustness, Alignment Science, Governance, Evaluations)
> - **Research question**: What specific question does this address?
> - **Problem**: What gap or issue motivates this?
> - **Approach outline**: High-level methodology — what would you actually do?
> - **Why it matters**: Theory of impact — how does this connect to AI safety?
>
> Optional but helpful:
> - **Proposed first experiments**: What would the first concrete steps look like?
> - **Relevant prior work**: Any papers or resources you're aware of?
>
> You can provide as much or as little as you have — we'll build it up together.

**Mint an `idea_id` for the new idea** with the shared generator — never write one by hand and never reuse a sequential ID:

```bash
uv run python -m saim.ids
```

It prints a short-UUID ID such as `gen-3f9a1c04`. Use it as the idea's `idea_id` and as its filename in `data/ideas/`. Set `run_id` to `"unknown"` since the idea did not come from a pipeline run.

Accept whatever the coordinator provides and fill in what's missing conversationally. This is collaborative — suggest improvements, ask clarifying questions, help sharpen the framing. Every idea **must** have a `research_field` before proceeding — if the coordinator doesn't provide one, ask which AI safety research field(s) it falls under or suggest the best fit.

Once the idea is sufficiently described, proceed to **Step 2: Score Against Criteria**.

## Step 2: Score Against Criteria (new ideas only)

**Skip this step for existing ideas that already have scores.**

For EACH scoring criterion (except novelty — that comes from Step 3):
- Read the criterion's rubric levels from the scoring config
- Assess the idea against the rubric
- Assign a score (1-5) with confidence (0.0-1.0) and reasoning
- Consider team/participant constraints when scoring

Present scores:
> **Criteria Scores:**
> - theory_of_impact: X/5 (confidence: Y) — reasoning
> - impact_pathway: X/5 (confidence: Y) — reasoning
> - accessible_complexity: X/5 — reasoning
> - narrow_scope: X/5 — reasoning
> - (etc.)

## Step 3: Novelty Assessment & Citation Verification (optional)

For **new ideas**, run novelty assessment automatically.

For **existing ideas**, offer it as a choice:
> Your idea already has a novelty classification of "[classification]" (score: [score]).
> Would you like me to re-assess novelty against current literature? This includes full literature search, deep reading when needed, and citation verification. (y/n)

If running novelty assessment:

Read and follow the full protocol in `.claude/commands/novelty-check.md`. This includes:
- **Novelty Assessment Protocol** (steps N1-N5): multi-source literature search (WebSearch + CrossRef + Semantic Scholar), evidence collection, deep reading of paper sections when abstract-level evidence is insufficient, novelty classification against the 5-level rubric, and validation
- **Citation Verification Protocol** (steps C1-C3): relevance scoring, verification via lookup APIs, and consequence application for removed citations

Present the results to the coordinator using the Standalone Summary format from `novelty-check.md`.

## Step 4: Readiness Assessment (Operationalizable & Contextualized)

Before entering open-ended refinement, judge the **written idea** against two readiness criteria. These are the gate that decides whether the idea is ready to be executed by a participant. Run this pass for every idea (new or existing), and report the verdict on each criterion to the coordinator.

### Criterion A — Operationalizable

The idea is operationalizable when **all the important decisions needed to execute it are already stated in the idea**, so a researcher can read it and go straight to executing — without having to invent choices themselves. Important decisions typically include:

- The **evaluation metric(s)** and how they're computed
- The **dataset(s) / benchmark(s)** to use
- The **task setup** (what the model is asked to do, how inputs are constructed)
- **Baselines / comparisons** the results are measured against
- The **concrete method or intervention** (not just a direction — the actual procedure)
- **Success criteria / thresholds** (what result would confirm or refute the hypothesis)
- The **analysis approach** (how raw results become the answer)

**Model choice is explicitly NOT one of these decisions** — do not flag an unspecified model as a gap, and do not force a model decision. The only exception is when the choice of model is itself central to the project (e.g., the idea is specifically about a capability that only appears in a particular model class); flag it only in that case.

Go through the relevant dimensions and classify each as **specified** or **missing/underspecified**. Then:

- If everything important is specified → the idea passes this criterion. Say so and move on.
- For each **missing or underspecified** dimension, do **NOT** silently fill it in. Instead, discuss it with the coordinator one dimension at a time:
  1. Present a **ranking of all the viable options** for that dimension, best first.
  2. Give your **reasoning** for the ranking — tradeoffs, fit to the research question, fit to the participant's compute/skill constraints.
  3. Let the coordinator choose (they may pick a lower-ranked option or something off-list).
  4. Once decided, **write the choice into the idea** (Approach Outline / Proposed First Experiments as appropriate) and keep both files in sync per the live-sync rule.

Only consider the idea operationalizable once every important dimension has a decision recorded in the text.

### Criterion B — Contextualized

The idea is contextualized when its **novelty relative to prior work is clear and direct**: a reader can see exactly what has already been done and what this idea adds on top.

**Do not trust the existing novelty fields.** Earlier pipeline phases sometimes get the novelty check wrong, so the stored `novelty_classification` / `novelty_score` / `novelty_method` are not sufficient evidence here. Redo the novelty check properly:

1. **Validate the plan with the coordinator first.** Before running anything, describe *how* you intend to conduct the novelty check — the search queries you'll run, the sources you'll consult (WebSearch + CrossRef + Semantic Scholar), and specifically which novelty claims you'll try to verify or refute. Ask the coordinator to confirm nothing is missing (a key paper, an obvious related line of work, a competing method). Incorporate their additions.
2. **Run the full protocol** in `.claude/commands/novelty-check.md` (Steps N1–N5 and Citation Verification C1–C3), exactly as in Step 3.
3. **Make the contrast explicit in the idea.** The result of the check is not just a score — update the idea's text (Strength Rationale / Cited Sources) so the delta against the closest prior work is stated directly: "X did Y; this idea differs by Z."

Only consider the idea contextualized once the novelty check has actually been rerun with a coordinator-validated plan and the prior-work contrast is written into the idea.

After both criteria are assessed, proceed to **Step 5: Collaborative Refinement** (the coordinator can also revisit either criterion from the refinement menu at any time).

## Step 5: Collaborative Refinement

This is the core of the skill. Present the current state of the idea and enter a collaborative loop.

**Writing style:** Whenever you write or rewrite any reader-facing part of the proposal (title, research question, approach, impact chain, cited sources), follow the proposal writing rules in [`writing-guidelines.md`](../../writing-guidelines.md).

> **What would you like to work on?**
> 1. **Discuss** — talk through concerns, questions, or specific aspects of the idea
> 2. **Strengthen weak dimensions** — improve the lowest-scoring criteria
> 3. **Reframe** — explore 2-3 alternative angles on the core insight
> 4. **Sharpen the approach** — make the methodology more concrete
> 5. **Refine experiments** — design or improve first experiments
> 6. **Improve impact chain** — strengthen the theory of why this matters
> 7. **Check novelty** — search literature for related work
> 8. **Operationalize** — fill in missing execution decisions (metrics, dataset, setup) via ranked options (Step 4, Criterion A)
> 9. **Contextualize** — re-run the novelty check on a coordinator-validated plan and write the prior-work contrast into the idea (Step 4, Criterion B)
> 10. **Not promising** — mark the idea as not promising (no file changes, just tracker update)
> 11. **Remove** — eliminate the idea (mark as eliminated with reason; does not delete files)
> 12. **Save** — write the idea (with improvements) everywhere it exists
> 13. **Done** — end session
>
> Or just tell me what's on your mind — you don't have to pick from the list.

### If discuss (or any free-form input):
Engage naturally with whatever the coordinator wants to talk about. This could be:
- Concerns about feasibility ("I'm worried the compute requirements are too high")
- Questions about framing ("Is this really an alignment problem or more of an evaluation problem?")
- Comparisons ("How does this compare to the approach in paper X?")
- Scope decisions ("Should I focus on just GPT-2 or try multiple models?")
- Any other aspect of the idea

Respond thoughtfully, drawing on the loaded config, scoring criteria, and participant constraints. Suggest concrete changes when appropriate. This is a conversation — follow the coordinator's lead.

### If strengthen:
Identify the weakest scoring dimensions. For each:
- Explain why the score was low (referencing the rubric)
- Suggest specific, concrete improvements
- Rewrite the relevant sections with improvements applied
- Re-score to show the improvement

### If reframe:
Generate 2-3 alternative framings of the core insight:
- Each takes a different methodological or conceptual angle
- Each is tailored to the participant's constraints
- Include estimated scores for each framing so the coordinator can compare tradeoffs

### If sharpen approach:
Work with the coordinator to make the methodology more concrete:
- What specific tools, datasets, or models would be used?
- What are the key assumptions and how would you test them?
- What's the minimum viable experiment?

### If refine experiments:
Help design concrete first experiments:
- Break down into time-boxed steps
- Consider the participant's compute and skill constraints
- Identify what each experiment would prove or disprove

### If improve impact chain:
Strengthen the connection to AI safety:
- Why does this specific question matter?
- What decisions or actions would change based on the results?
- How does this connect to broader safety research agendas?

### If check novelty:
Run the full novelty assessment and citation verification protocol from Step 3 (i.e., follow `.claude/commands/novelty-check.md`).

### If operationalize:
Run Criterion A from **Step 4**. Walk the important execution decisions (metric, dataset, task setup, baselines, method, success criteria, analysis), classify each as specified or missing, and for every missing one present a ranked list of options with reasoning and let the coordinator choose before writing the decision into the idea. Do not force a model choice unless the model is central to the project.

### If contextualize:
Run Criterion B from **Step 4**. First validate the novelty-check plan with the coordinator (queries, sources, which novelty claims you'll verify — confirm nothing is missing), then run the full protocol in `.claude/commands/novelty-check.md`, and finally write the explicit prior-work contrast into the idea's text. Do not rely on the stored novelty fields.

### If remove (eliminate):
"Removing" an idea means marking it as **eliminated** — not deleting files. Pipeline history is preserved for auditability.

0. **Idea tracker** — update the idea's status to **"Removed"** in `data/output/idea_tracker.md`.

1. **`data/ideas/<idea_id>.md`** — add `eliminated: true` and `elimination_reason: '<reason>'` to the YAML frontmatter. Update `novelty_classification`, `novelty_score`, and `novelty_method` if the elimination was driven by a novelty assessment.

2. **Ranked proposals** — in both `data/output/ranked_proposals.md` and `data/runs/<run_id>/rank/ranked_proposals.md` (if they exist), remove the idea's content but keep the heading. Add an **[ELIMINATED]** badge right after the heading and an `Elimination reason: <reason>` line below it. The section should contain only the heading, badge, and reason — no other content. In the corresponding `.json` file, add `eliminated: true` and `elimination_reason` fields to the idea's entry.

3. **Selected ideas file** — if the idea appears in the selected ideas file (`SELECTED_IDEAS_FILE`), remove its section entirely (eliminated ideas should not remain in the curated selection).

4. Do NOT delete any pipeline stage files (generate/, filter_score/, refine/ batches). These are historical artifacts.

Report which files were updated.

### If not promising:
The collaborator has marked this idea as not promising. Update the idea tracker status to **"Not promising"** in `data/output/idea_tracker.md`. Do not modify any other files. Return to the refinement menu.

### If save:

**Idea tracker — update status to "Added and needs manual review"** in `data/output/idea_tracker.md`. The status will change to "Added" only when the human confirms they have reviewed the content in the selected ideas file.

**Novelty gate — MANDATORY before saving:**
Before writing any files, check the idea's `novelty_method` field. If it is `"novelty_estimated"`, `null`, or missing, the idea has only estimated novelty — which is unreliable and must not be saved:
1. Inform the coordinator: *"This idea has only estimated novelty (novelty_method: [value]) — estimated novelty is unreliable and ideas must have a verified novelty assessment before being saved. Running novelty check now."*
2. Run the full novelty assessment protocol (Step 3 / `.claude/commands/novelty-check.md`) before proceeding with the save.
3. After the assessment, update `novelty_method` to reflect the actual method used (e.g., `"evidence_based"`, `"novelty_web_search"`, `"novelty_verified"`). Only continue with the save once this is done.

Save the idea with all improvements to **every location where it exists**:

1. **`data/ideas/<idea_id>.md`** — the primary idea file. Use the existing filename if updating an existing idea. For a new idea, use the `idea_id` minted in Step 1 (`uv run python -m saim.ids`) as the filename — never a title slug and never a hand-written or sequential ID. Include full YAML frontmatter and all body sections.

2. **Pipeline run stages** — if the idea came from a pipeline run (`run_id` is set and not "unknown"), check for the idea in `data/runs/<run_id>/` stage directories (generate/, filter_score/, refine/, rank/). For individual `.md` files, update them. For batch `.json` files, load the batch, find the matching idea by `idea_id`, update its fields, and write back.

3. **Selected ideas file** — check if a selected ideas file exists at the path configured by `SELECTED_IDEAS_FILE` in `src/saim/constants.py` (default: `data/output/selected_ideas.md`). If the file exists and contains this idea (match by idea_id or title), update the idea's section in that file. If the idea isn't in the file yet, **always add it** — every saved idea should be in the selected ideas file. **Numbering: scan ALL sections of the file (including "Lower Confidence" and any other secondary sections) to find the highest existing number, then use the next integer.** For example, if the file has #1, #2, #3 in the main section and #4 in "Lower Confidence", the next idea gets #5 regardless of which section it's added to. Never use fractional numbers (e.g., #3.5). Never reuse or skip numbers.

```bash
uv run python -c "from saim.constants import SELECTED_IDEAS_FILE; print(SELECTED_IDEAS_FILE)"
```

For `data/ideas/` and pipeline run files, preserve the full structure:
- YAML frontmatter: idea_id, run_id, stage, rank, weighted_score, title, research_field (list), subfield, generation_strategy, novelty_classification, novelty_score, novelty_method, original_scores, provenance, timestamp
- Body sections: Research Question, Approach Outline, Proposed First Experiments, Impact Pathway, Theory Of Impact Chain, Strength Rationale, Alternative Framings, Cited Sources

For the **selected ideas file**, write a condensed version: include all sections EXCEPT the detailed per-experiment breakdowns in Proposed First Experiments. Only include follow-up experiments or experiments that go beyond the core methodology described in the Approach Outline. The full experiment details remain in `data/ideas/` — the selected ideas file is a reference summary, not a duplicate.

Report which files were updated.

Return to the refinement menu until the user chooses "Done".

## Session Summary

When done, provide:
- Summary of changes made to the idea
- Current scores (if scored)
- Whether the idea was saved
- Suggestions for next steps (e.g., run full pipeline, try `/brainstorm` for related directions)
