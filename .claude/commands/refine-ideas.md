# Refine AI Safety Research Ideas into Full Proposals

Refine scored ideas by strengthening weak dimensions, generating alternative framings with score-based comparison, and assembling full research proposals.

## Setup

Determine the run directory. If the user provided a path, use it. Otherwise, find the latest run:

```bash
ls -1t data/runs/ | head -1
```

Use that as the run directory: `data/runs/<timestamp>`.

Verify scored ideas exist from the filter_score stage:

```bash
uv run python -m saim.pipeline.filter_score read <run_dir>
```

If no scored ideas exist, tell the coordinator and stop.

Load scoring configuration (criteria, weights):

```bash
uv run python -m saim.config.cli show-scoring
```

Load team profile:

```bash
uv run python -m saim.config.cli show-team
```

Load participant profile:

```bash
uv run python -m saim.config.cli show-participant
```

Save all configuration outputs — they will be used in LLM prompts throughout refinement.

Before proceeding, echo the active configuration:
> **Refining with:** team=[default_team], participant=[profile_name], scored_ideas=[count], criteria=[list each criterion name=active_weight (threshold=N)]

## Phase 1: Load Scored Ideas

Read all scored (non-eliminated) ideas:

```bash
uv run python -m saim.pipeline.filter_score read <run_dir>
```

Parse the output into a list of scored idea objects. Sort by `weighted_score` descending. Record the total count.

Log the start:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine info 'Refine stage started' '{"scored_ideas": <COUNT>}'
```

## Phase 2: Auto-Strengthen Weak Ideas (FR36)

For EACH scored idea, identify weak dimensions and strengthen them.

### Step 2.1: Analyze weaknesses

```bash
uv run python -m saim.pipeline.refine analyze-weaknesses '<scored_idea_json>' '<criteria_json>' '<active_weights_json>'
```

Where `<criteria_json>` is the JSON array of scoring criteria objects from `show-scoring` output, and `<active_weights_json>` is the team's criteria weight overrides (or `null` if none). This returns a context dict with weak dimensions (all criteria scoring below their per-criterion `refinement_threshold` where the active weight is non-zero), strong dimensions, and idea metadata.

### Step 2.2: LLM refinement

If the idea has weak dimensions, use the LLM to suggest improvements. Provide the following in the prompt:

> You are brainstorming improvements to an AI Safety research idea. Your goal is to maximize scores on the weak dimensions according to the rubric.
>
> **Idea:** [title, problem, direction, approach from scored_idea]
>
> **Weak Dimensions:**
> [FOR EACH weak dimension: criterion name, current score, threshold, scoring reasoning, full rubric for that criterion]
>
> **Strong Dimensions:**
> [FOR EACH strong dimension: criterion name, score]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** For each weak dimension, propose a concrete change to the idea that would raise its score above the threshold on the rubric. The improvement must be:
> - Specific and actionable (not vague advice)
> - Compatible with the team's skill level
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "refinements": [
>     {
>       "criterion": "<name>",
>       "original_score": <int>,
>       "change": "<2-4 sentences describing the concrete change to the idea>",
>       "expected_score": <int>,
>       "rationale": "<1-2 sentences why this raises the score per the rubric>"
>     }
>   ],
>   "confidence": <0.0-1.0>,
>   "overall_notes": "<any cross-cutting observations>"
> }
> ```

If the LLM refinement fails for an idea, keep the original idea unchanged and log a warning:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine warning 'LLM refinement failed, keeping original' '{"idea_id": "<id>", "title": "<title>"}'
```

### Step 2.3: Re-score refined idea on weak dimensions

After refinement, have the LLM re-score the refined idea on ONLY the weak dimensions using the same rubric:

> You are scoring a refined AI Safety research idea on specific dimensions.
>
> **Original Idea:** [title, problem, direction, approach]
>
> **Refinements Applied:** [list of changes from Step 2.2]
>
> **Task:** Re-score the idea as modified by the refinements on each of these criteria. Use the exact same rubric. If the refinement changed how the idea relates to novelty, mark the novelty score as "estimated" (lightweight re-assessment without web search).
>
> **Criteria to score:**
> [FOR EACH weak dimension: criterion name, full rubric]
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "rescored_dimensions": [
>     {
>       "criterion": "<name>",
>       "original_score": <int>,
>       "new_score": <int>,
>       "reasoning": "<1-2 sentences>",
>       "is_estimated_novelty": <true|false>
>     }
>   ]
> }
> ```

**Decision rule:** Only accept refinements where `new_score > original_score`. If a refinement does not improve the score, discard it and keep the original for that dimension.

### Step 2.4: Record strengthening results

Report per-idea confidence that refinement improved the idea. Track the count of ideas that had weak dimensions, were strengthened, and how many refinements were accepted vs discarded.

Log results:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine info 'Phase 2 complete: auto-strengthen' '{"total_ideas": <TOTAL>, "ideas_with_weak_dims": <COUNT>, "ideas_strengthened": <COUNT>, "refinements_accepted": <COUNT>, "refinements_discarded": <COUNT>}'
```

## Phase 3: Generate and Score Alternative Framings (FR37)

Select promising ideas: top 50% by `weighted_score` from the scored ideas list.

For EACH promising idea, use the LLM to generate 2-3 alternative framings:

> You are generating alternative framings for a promising AI Safety research idea. You have creative freedom to reimagine the idea.
>
> **Original Idea:** [title, problem, direction, approach, scores summary]
>
> **Refinements Applied:** [if any accepted from Phase 2]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** Generate 2-3 alternative framings of this idea. Each framing should:
> - Approach the problem from a different angle (different methodology, different subfield lens, different scope)
> - Be feasible for the described team
> - Aim to maximize scores across all criteria
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "original_title": "<title>",
>   "alternative_framings": [
>     {
>       "framing_id": "<idea_id>_alt_<N>",
>       "title": "<new title>",
>       "problem_reframe": "<1-2 sentences>",
>       "approach": "<2-3 sentences>",
>       "key_difference": "<1 sentence explaining how this differs from original>"
>     }
>   ]
> }
> ```

### Score alternative framings

After generating framings, have the LLM score EACH alternative framing on ALL criteria using the same rubrics:

> You are scoring alternative framings of an AI Safety research idea.
>
> **Original Idea Scores:** [all criterion scores]
>
> **Alternative Framing:** [framing details]
>
> **Task:** Score this framing on every criterion using the same rubric used for the original. For novelty, provide an "estimated novelty" score — a lightweight re-assessment without web search where you estimate whether the novelty has likely changed given the new framing.
>
> **Criteria:**
> [FOR EACH criterion: name, full rubric]
>
> **Output format (JSON):**
> ```json
> {
>   "framing_id": "<id>",
>   "scores": {
>     "<criterion_name>": {
>       "score": <int>,
>       "reasoning": "<1-2 sentences>",
>       "is_estimated_novelty": <true|false>
>     }
>   },
>   "weighted_score": <float>
> }
> ```

**Decision rule:** Framings that improve `weighted_score` over the original become the primary version. Framings that do not improve the score are kept as "alternative framings" in the proposal for reference.

If the LLM fails for an idea, skip alternative framings for that idea and log a warning:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine warning 'Alternative framing generation failed' '{"idea_id": "<id>", "title": "<title>"}'
```

Log results:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine info 'Phase 3 complete: alternative framings' '{"promising_ideas": <COUNT>, "framings_generated": <TOTAL_FRAMINGS>, "framings_promoted": <COUNT>, "framings_kept_as_alternatives": <COUNT>}'
```

## Phase 4: Assemble Full Proposals (FR38, FR40)

For EACH scored idea (including those without refinements), use the LLM to produce a full proposal and write it:

> You are assembling a full research proposal for an AI Safety idea.
>
> **Idea:** [title, problem, direction, approach — use the promoted framing if one was selected in Phase 3, otherwise the refined version from Phase 2, otherwise the original]
>
> **Scores:** [all criterion scores — use re-scored values where available, marking estimated novelty scores]
>
> **Refinements:** [accepted refinements from Phase 2, if any]
>
> **Alternative Framings:** [non-promoted framings from Phase 3, if any]
>
> **Verified Citations:** [all citations from filter_score stage citation_verification that were verified or corrected]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** Produce a structured research proposal. Follow the proposal writing rules in `writing-guidelines.md` (self-contained, plain, brief, no em dashes; simple intuitive title).
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "title": "<simple, intuitive title — short; let the research question carry the fuller framing>",
>   "research_question": "<1-2 clear sentences framing the core question>",
>   "approach_outline": "<3-5 sentences describing methodology and key steps>",
>   "proposed_first_experiments": [
>     "<concrete experiment 1 — what to do, what to measure, expected outcome>",
>     "<concrete experiment 2>",
>     "<concrete experiment 3>"
>   ],
>   "theory_of_impact_chain": "<2-4 sentences: if this works, then X, which leads to Y, which improves safety because Z>",
>   "strength_rationale": "<2-3 sentences summarizing why this idea is strong, referencing top-scoring criteria>",
>   "cited_sources": [
>     {"title": "<paper title>", "authors": "<authors>", "url": "<url>", "relevance": "<1 sentence>"}
>   ],
>   "refinements_applied": [<list of accepted refinement changes incorporated>],
>   "alternative_framings": [<non-promoted framings from Phase 3>],
>   "metadata": {
>     "weighted_score": <float>,
>     "confidence": <float>,
>     "novelty_classification": "<classification>",
>     "has_estimated_novelty": <true|false>,
>     "weak_dimensions_addressed": <count>
>   }
> }
> ```

Build the proposal skeleton and write:

```bash
uv run python -m saim.pipeline.refine build-skeleton '<scored_idea_json>' '<refinement_json>'
uv run python -m saim.pipeline.refine write <run_dir> '<proposal_json>'
```

If the LLM fails for an idea, build a minimal proposal from the scored idea data and log a warning:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine warning 'Proposal generation failed, using minimal proposal' '{"idea_id": "<id>", "title": "<title>"}'
```

Repeat for every scored idea.

Log results:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> refine info 'Phase 4 complete: proposals assembled' '{"proposals_written": <COUNT>, "minimal_fallbacks": <COUNT>}'
```

## Phase 5: Results Summary

Present the coordinator with:

1. **Refinement summary**: Total scored ideas processed, ideas with weak dimensions strengthened, alternative framings generated, full proposals assembled
2. **Score improvements**: List ideas where refinement or reframing improved weighted_score, showing before/after
3. **Estimated novelty flags**: List any ideas where novelty was re-estimated (not re-verified via web search)
4. **Proposals written**: List with idea_id, title, weighted_score, confidence, novelty classification

Tell the coordinator:
> Your refined proposals are in `data/runs/<timestamp>/refine/`. Use `/rank-ideas` next to produce the final ranking.

## Error Handling

- **LLM refinement failure** (Phase 2): Keep the original idea unchanged, log warning, continue with remaining ideas
- **LLM framing failure** (Phase 3): Skip alternative framings for that idea, log warning, continue
- **LLM proposal failure** (Phase 4): Build a minimal proposal from scored idea data (title, scores, cited sources), log warning, continue
- **Pipeline command failure**: Log the error and continue with remaining ideas where possible
- Always produce output even with degraded quality — partial refinement is better than none
