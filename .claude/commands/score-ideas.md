# Score and Filter AI Safety Research Ideas

Score generated ideas against configured criteria using **parallel subagents** organized in 2 waves.

**IMPORTANT — Source reading policy:** Only read **abstracts, summaries, and introductions** — never full papers.

## Setup

Determine the run directory. If the user provided a path, use it. Otherwise, find the latest run:

```bash
ls -1t data/runs/ | head -1
```

Use that as the run directory: `data/runs/<timestamp>`.

Verify ideas exist from the generate stage:

```bash
uv run python -m saim.pipeline.generate list <run_dir>
```

If no ideas exist, tell the coordinator and stop.

Load scoring configuration (criteria, weights, thresholds):

```bash
uv run python -m saim.config.cli show-scoring
```

Load the quick filter rubric and threshold:

```bash
uv run python -m saim.config.cli show-quick-filter
```

Load batch sizes for parallel processing:

```bash
uv run python -m saim.config.cli show-batch-sizes
```

Load participant profile for context on the team's skill level:

```bash
uv run python -m saim.config.cli show-participant
```

Load the citation relevance rubric:

```bash
uv run python -m saim.config.cli show-citation-relevance
```

Save all the configuration outputs — they will be embedded in subagent prompts so subagents don't need to call config commands themselves.

Before proceeding, echo the active configuration:
> **Scoring with:** team=[default_team], criteria=[list each criterion name=active_weight], thresholds=[filter_score min_score], batch_sizes=[stage1=N, stage2=N, stage3=N]

## Wave 1: Quick Relevance Filter (Stage 1)

### Step 1.1: Create batches

```bash
uv run python -m saim.pipeline.filter_score create-batches <run_dir> 1 <stage1_batch_size>
```

This reads all generated ideas, partitions them into batches, and writes batch files. It prints the batch count and file paths as JSON.

### Step 1.2: Launch parallel subagents

Launch **one Agent subagent per batch**, all in a single message for maximum parallelism. Each subagent receives a self-contained prompt with all config needed.

**Subagent prompt template** (substitute values for each batch):

> You are a quick relevance filter for AI Safety research ideas.
>
> **Your task:** Read each idea's title, problem, and direction. Score it 1-5 against the rubric below. Write results when done.
>
> **Quick Filter Rubric (threshold: [THRESHOLD]):**
> [FULL RUBRIC FROM show-quick-filter — all 5 levels with descriptions]
>
> **Confidence Rubric:**
> [FULL CONFIDENCE RUBRIC FROM show-scoring]
>
> **Step 1:** Read your batch:
> ```bash
> uv run python -m saim.pipeline.filter_score read-batch [BATCH_PATH]
> ```
>
> **Step 2:** For EACH idea in the batch, score it against the rubric. Match the idea against the rubric level descriptions and pick the level that best fits — do NOT score based on gut feeling.
>
> **Step 3:** Build a JSON array of results. For each idea:
> ```json
> {
>   "idea_id": "<id>",
>   "title": "<title>",
>   "run_id": "<run_id>",
>   "quick_score": <1-5>,
>   "quick_reasoning": "<1 sentence matching rubric level>",
>   "quick_confidence": <0.0-1.0>,
>   "eliminated": <true if quick_score below [THRESHOLD], else false>,
>   "elimination_reason": <null or "Stage 1: quick relevance score [X] below threshold [Y]">
> }
> ```
>
> Do NOT skip any ideas. Include every idea from the batch.
>
> **Step 4:** Write results:
> ```bash
> uv run python -m saim.pipeline.filter_score write-batch-results [RESULT_PATH] '<json_array>'
> ```
>
> Where [RESULT_PATH] is: `[RUN_DIR]/filter_score/results/stage1/batch_[NNN]_results.json`

### Step 1.3: Collect and filter

After all Wave 1 subagents complete:

```bash
uv run python -m saim.pipeline.filter_score filter-survivors <run_dir> 1
```

This merges all batch results, filters out eliminated ideas, and writes the survivors file. It prints survivor and eliminated counts.

Log the results:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> filter_score info 'Stage 1 complete: quick relevance filter' '{"total_ideas": <TOTAL>, "survivors": <SURVIVORS>, "eliminated": <ELIMINATED>}'
```

## Wave 2: Full Per-Criterion Scoring (Stage 2)

### Step 2.1: Create batches from Stage 1 survivors

```bash
uv run python -m saim.pipeline.filter_score create-batches <run_dir> 2 <stage2_batch_size>
```

### Step 2.2: Launch parallel subagents

Launch **one Agent subagent per batch**, all in a single message.

**Subagent prompt template:**

> You are scoring AI Safety research ideas against multiple criteria.
>
> **Your task:** Score each idea against ALL criteria listed below using the rubrics. Write results when done.
>
> **Scoring Criteria and Rubrics:**
> [FOR EACH CRITERION from show-scoring (EXCLUDING novelty): name, description, active_weight, and full 5-level rubric]
>
> **Estimated novelty (provisional — NO web search):** Produce a quick LLM *estimate* of novelty from your own knowledge only. Do NOT search the web or call any citation tools — this is the cheap early signal. Classify against the rubric below; the calculated (evidence-based) novelty is run later, only on the top-ranked ideas, by the `novelty-rerank` workflow, which overwrites this estimate.
>
> | Classification | Score | Definition |
> |---|---|---|
> | already_solved | 1 | You are confident existing published work fully addresses this idea. |
> | largely_addressed | 2 | Most of the proposed contribution is likely already covered. |
> | partially_addressed | 3 | Work likely exists on the topic but this specific angle/combination may be open. |
> | mostly_novel | 4 | You are not aware of direct published work on this specific proposal. |
> | novel | 5 | You are not aware of any published work on this question or approach. |
>
> When unsure, default to `partially_addressed` (3). This is an estimate — keep confidence modest.
>
> **Confidence Rubric:**
> [FULL CONFIDENCE RUBRIC]
>
> **Participant profile:**
> [PARTICIPANT SUMMARY or "none specified"]
>
> **Weighted score threshold:** [MIN_SCORE from show-scoring thresholds]
>
> **Weighted score formula:** For each scored criterion, multiply score by its active weight. Sum all (score × weight), divide by sum of weights. Active weights: [LIST criterion=weight pairs, excluding novelty].
>
> **Step 1:** Read your batch:
> ```bash
> uv run python -m saim.pipeline.filter_score read-batch [BATCH_PATH]
> ```
>
> **Step 2:** For EACH idea, score it against every criterion (except novelty). Match the idea against the rubric level descriptions and pick the level that best fits — do NOT score based on gut feeling. Compute the weighted score **over the non-novelty criteria only** (this drives the Stage 2 cutoff). Compute overall confidence as the average of per-criterion confidences. Then assign the **estimated** novelty classification + score (1-5) from the rubric above, with NO web search.
>
> **Step 3:** Build a JSON array of results. For each idea:
> ```json
> {
>   "idea_id": "<id>",
>   "title": "<title>",
>   "run_id": "<run_id>",
>   "original_idea": <full idea object from batch>,
>   "scores": {
>     "<criterion_name>": {
>       "score": <1-5>,
>       "reasoning": "<1-3 sentences referencing rubric level>",
>       "confidence": <0.0-1.0>
>     },
>     "novelty": {
>       "score": <1-5 estimated>,
>       "reasoning": "<1 sentence — estimate, no search>",
>       "confidence": <0.0-1.0>
>     }
>   },
>   "novelty_assessment": {
>     "classification": "<one of the 5 levels>",
>     "evidence": [],
>     "confidence": <0.0-1.0>,
>     "derived_score": <1-5, matching the classification>,
>     "reasoning": "<1 sentence estimate>"
>   },
>   "novelty_method": "novelty_estimated",
>   "weighted_score": <computed weighted average, EXCLUDING novelty>,
>   "confidence": <average of per-criterion confidences>,
>   "eliminated": <true if weighted_score below [MIN_SCORE]>,
>   "elimination_reason": <null or "Stage 2: weighted score [X] below threshold [Y]">
> }
> ```
>
> The `novelty` entry here is an **estimate** (`novelty_method: "novelty_estimated"`). It carries through refine into the first ranking, then the `novelty-rerank` workflow replaces it with a calculated, evidence-based assessment on the top-ranked ideas.
>
> Do NOT skip any ideas.
>
> **Step 4:** Write results:
> ```bash
> uv run python -m saim.pipeline.filter_score write-batch-results [RESULT_PATH] '<json_array>'
> ```
>
> Where [RESULT_PATH] is: `[RUN_DIR]/filter_score/results/stage2/batch_[NNN]_results.json`

### Step 2.3: Collect and filter

```bash
uv run python -m saim.pipeline.filter_score filter-survivors <run_dir> 2
```

Log the results:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> filter_score info 'Stage 2 complete: full scoring' '{"survivors": <SURVIVORS>, "eliminated": <ELIMINATED>}'
```

## Phase 3: Assemble Final Scored Ideas

After both waves complete, assemble the final scored idea JSON files.

Read the results from both stages:

```bash
uv run python -m saim.pipeline.filter_score merge-results <run_dir> 1
uv run python -m saim.pipeline.filter_score merge-results <run_dir> 2
```

For each idea that appears in the Stage 2 results (all ideas that were scored, both survivors and eliminated):

1. Start with the Stage 2 result (contains `original_idea`, `scores`, `weighted_score`, `eliminated`)
2. If the idea was eliminated at Stage 1, build a minimal scored idea with the Stage 1 result data
3. Add metadata: `stage: "filter_score"`, `timestamp`, `filter_stage_passed`

Write each final scored idea:

```bash
uv run python -m saim.pipeline.filter_score write <run_dir> '<scored_idea_json>'
```

## Phase 4: Results Summary

Present the coordinator with:

1. **Pipeline summary**: Total ideas → Stage 1 survivors → Stage 2 survivors
2. **Eliminated ideas**: List with idea_id, title, elimination reason, stage eliminated
3. **Surviving ideas** (sorted by weighted_score, highest first):
   - idea_id, title, weighted_score, confidence
   - Per-criterion scores summary
4. **Team weight overrides** applied (if any)

Tell the coordinator:
> Your scored ideas are in `data/runs/<timestamp>/filter_score/`. Surviving ideas are ready for refinement with `/refine-ideas`. You can review individual scored ideas in the JSON files for full reasoning.

## Error Handling

- **Subagent failure**: After each wave, check if any batch result files are missing. Re-launch failed batches once. If retry also fails, mark those ideas as eliminated with "Scoring failed: subagent error" and add a warning to the pipeline log.
- **Scoring failure** for individual ideas within a subagent: log the error within the batch results and continue with remaining ideas
- Always produce output even with degraded sources — partial scoring is better than none
