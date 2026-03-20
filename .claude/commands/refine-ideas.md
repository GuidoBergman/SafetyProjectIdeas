# Refine AI Safety Research Ideas into Full Proposals

Refine scored ideas by strengthening weak dimensions, generating alternative framings, and assembling full research proposals.

## Setup

Determine the run directory. If the user provided a path, use it. Otherwise, find the latest run:

```bash
ls -1t data/runs/ | head -1
```

Use that as the run directory: `data/runs/<timestamp>`.

Verify scored ideas exist from the filter_score stage:

```bash
uv run python -m safety_ideas.pipeline.filter_score read <run_dir>
```

If no scored ideas exist, tell the coordinator and stop.

Load scoring configuration (criteria, weights):

```bash
uv run python -m safety_ideas.config.cli show-scoring
```

Load team profile:

```bash
uv run python -m safety_ideas.config.cli show-team
```

Load participant profile:

```bash
uv run python -m safety_ideas.config.cli show-participant
```

Save all configuration outputs — they will be used in LLM prompts throughout refinement.

Before proceeding, echo the active configuration:
> **Refining with:** team=[default_team], participant=[profile_name], scored_ideas=[count], criteria=[list each criterion name=active_weight]

## Phase 1: Load Scored Ideas

Read all scored (non-eliminated) ideas:

```bash
uv run python -m safety_ideas.pipeline.filter_score read <run_dir>
```

Parse the output into a list of scored idea objects. Sort by `weighted_score` descending. Record the total count.

Log the start:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine info 'Refine stage started' '{"scored_ideas": <COUNT>}'
```

## Phase 2: Auto-Strengthen Weak Ideas (FR36)

For EACH scored idea, identify and strengthen weak dimensions.

### Step 2.1: Identify weak dimensions

```bash
uv run python -m safety_ideas.pipeline.refine identify-weak '<scored_idea_json>' '<criteria_json>'
```

Where `<criteria_json>` is the JSON array of scoring criteria objects from `show-scoring` output. This returns the weakest criterion names for the idea.

### Step 2.2: Build refinement context

If the idea has weak dimensions:

```bash
uv run python -m safety_ideas.pipeline.refine build-context '<scored_idea_json>' '<weak_dims_json>'
```

This returns context for LLM refinement — weak and strong dimensions with scores, and improvement suggestions.

### Step 2.3: LLM refinement

Use the LLM to suggest improvements for each weak dimension. Provide the following in the prompt:

> You are refining an AI Safety research idea to strengthen its weak dimensions.
>
> **Idea:** [title, problem, direction, approach from scored_idea]
>
> **Weak Dimensions:**
> [FOR EACH weak dimension: criterion name, current score, scoring reasoning, rubric for that criterion]
>
> **Refinement Context:**
> [Context from build-context output]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** For each weak dimension, suggest a concrete improvement that would raise its score by at least 1 point on the rubric. The improvement must be:
> - Specific and actionable (not vague advice)
> - Compatible with the team's skill level
> - Preserving the core idea while strengthening the weak area
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "refinements": [
>     {
>       "criterion": "<name>",
>       "original_score": <int>,
>       "suggestion": "<2-4 sentences describing the improvement>",
>       "expected_score": <int>,
>       "rationale": "<1-2 sentences why this raises the score>"
>     }
>   ],
>   "confidence": <0.0-1.0>,
>   "overall_notes": "<any cross-cutting observations>"
> }
> ```

If the LLM refinement fails for an idea, keep the original idea unchanged and log a warning:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine warning 'LLM refinement failed, keeping original' '{"idea_id": "<id>", "title": "<title>"}'
```

### Step 2.4: Record strengthening results

Report per-idea confidence that refinement improved the idea. Track the count of ideas that had weak dimensions and were strengthened.

Log results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine info 'Phase 2 complete: auto-strengthen' '{"total_ideas": <TOTAL>, "ideas_with_weak_dims": <COUNT>, "ideas_strengthened": <COUNT>}'
```

## Phase 3: Generate Alternative Framings (FR37)

Select promising ideas: top 50% by `weighted_score` from the scored ideas list.

For EACH promising idea, use the LLM to generate 2-3 alternative framings:

> You are generating alternative framings for a promising AI Safety research idea.
>
> **Original Idea:** [title, problem, direction, approach, scores summary]
>
> **Refinements Applied:** [if any from Phase 2]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** Generate 2-3 alternative framings of this idea. Each framing should:
> - Preserve the core safety-relevant insight
> - Approach the problem from a substantially different angle (different methodology, different subfield lens, different scope)
> - Be feasible for the described team
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
>       "key_difference": "<1 sentence explaining how this differs from original>",
>       "estimated_feasibility": <1-5>
>     }
>   ]
> }
> ```

If the LLM fails for an idea, skip alternative framings for that idea and log a warning:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine warning 'Alternative framing generation failed' '{"idea_id": "<id>", "title": "<title>"}'
```

Log results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine info 'Phase 3 complete: alternative framings' '{"promising_ideas": <COUNT>, "framings_generated": <TOTAL_FRAMINGS>}'
```

## Phase 4: Assemble Full Proposals (FR38, FR40)

For EACH scored idea (including those without refinements), assemble a full research proposal.

### Step 4.1: LLM proposal generation

Use the LLM to produce a full proposal for each idea:

> You are assembling a full research proposal for an AI Safety idea.
>
> **Idea:** [title, problem, direction, approach from scored_idea]
>
> **Scores:** [all criterion scores with reasoning]
>
> **Refinements:** [suggestions from Phase 2, if any]
>
> **Alternative Framings:** [from Phase 3, if any]
>
> **Verified Citations:** [all citations from filter_score stage citation_verification that were verified or corrected]
>
> **Participant Profile:**
> [PARTICIPANT SUMMARY]
>
> **Task:** Produce a structured research proposal with these sections:
>
> **Output format (JSON):**
> ```json
> {
>   "idea_id": "<id>",
>   "title": "<title>",
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
>   "refinements_applied": [<list of refinement suggestions incorporated>],
>   "alternative_framings": [<list from Phase 3 if available>],
>   "metadata": {
>     "weighted_score": <float>,
>     "confidence": <float>,
>     "novelty_classification": "<classification>",
>     "weak_dimensions_addressed": <count>
>   }
> }
> ```

If the LLM fails for an idea, build a minimal proposal from the scored idea data and log a warning:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine warning 'Proposal generation failed, using minimal proposal' '{"idea_id": "<id>", "title": "<title>"}'
```

### Step 4.2: Build proposal skeleton

```bash
uv run python -m safety_ideas.pipeline.refine build-skeleton '<scored_idea_json>' '<refinement_json>'
```

### Step 4.3: Write proposal

```bash
uv run python -m safety_ideas.pipeline.refine write <run_dir> '<proposal_json>'
```

Repeat Steps 4.1-4.3 for every scored idea.

Log results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> refine info 'Phase 4 complete: proposals assembled' '{"proposals_written": <COUNT>, "minimal_fallbacks": <COUNT>}'
```

## Phase 5: Results Summary

Present the coordinator with:

1. **Refinement summary**: Total scored ideas processed, ideas with weak dimensions strengthened, alternative framings generated, full proposals assembled
2. **Strengthened ideas**: List with idea_id, title, weak dimensions addressed, refinement confidence
3. **Alternative framings**: Count per idea, total framings generated
4. **Proposals written**: List with idea_id, title, weighted_score, confidence, novelty classification

Tell the coordinator:
> Your refined proposals are in `data/runs/<timestamp>/refine/`. Use `/rank-ideas` next to produce the final ranking.

## Error Handling

- **LLM refinement failure** (Phase 2): Keep the original idea unchanged, log warning, continue with remaining ideas
- **LLM framing failure** (Phase 3): Skip alternative framings for that idea, log warning, continue
- **LLM proposal failure** (Phase 4): Build a minimal proposal from scored idea data (title, scores, cited sources), log warning, continue
- **Pipeline command failure**: Log the error and continue with remaining ideas where possible
- Always produce output even with degraded quality — partial refinement is better than none
