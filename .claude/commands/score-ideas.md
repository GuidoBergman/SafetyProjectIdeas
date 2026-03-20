# Score and Filter AI Safety Research Ideas

Score generated ideas against configured criteria, assess novelty, and verify citations using **parallel subagents** organized in 3 waves.

**IMPORTANT — Source reading policy:** For Waves 1-2, only read **abstracts, summaries, and introductions** — never full papers. For Wave 3 (novelty assessment), targeted deep reading of specific sections (discussion, limitations, future work) is permitted via the paper_fetcher module when the LLM judges that abstract-level evidence is insufficient to classify novelty.

## Setup

Determine the run directory. If the user provided a path, use it. Otherwise, find the latest run:

```bash
ls -1t data/runs/ | head -1
```

Use that as the run directory: `data/runs/<timestamp>`.

Verify ideas exist from the generate stage:

```bash
uv run python -m safety_ideas.pipeline.generate list <run_dir>
```

If no ideas exist, tell the coordinator and stop.

Load scoring configuration (criteria, weights, thresholds):

```bash
uv run python -m safety_ideas.config.cli show-scoring
```

Load the quick filter rubric and threshold:

```bash
uv run python -m safety_ideas.config.cli show-quick-filter
```

Load batch sizes for parallel processing:

```bash
uv run python -m safety_ideas.config.cli show-batch-sizes
```

Load participant profile for context on the team's skill level:

```bash
uv run python -m safety_ideas.config.cli show-participant
```

Load the citation relevance rubric:

```bash
uv run python -m safety_ideas.config.cli show-citation-relevance
```

Save all the configuration outputs — they will be embedded in subagent prompts so subagents don't need to call config commands themselves.

Before proceeding, echo the active configuration:
> **Scoring with:** team=[default_team], criteria=[list each criterion name=active_weight], thresholds=[filter_score min_score], batch_sizes=[stage1=N, stage2=N, stage3=N]

## Wave 1: Quick Relevance Filter (Stage 1)

### Step 1.1: Create batches

```bash
uv run python -m safety_ideas.pipeline.filter_score create-batches <run_dir> 1 <stage1_batch_size>
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
> uv run python -m safety_ideas.pipeline.filter_score read-batch [BATCH_PATH]
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
> uv run python -m safety_ideas.pipeline.filter_score write-batch-results [RESULT_PATH] '<json_array>'
> ```
>
> Where [RESULT_PATH] is: `[RUN_DIR]/filter_score/results/stage1/batch_[NNN]_results.json`

### Step 1.3: Collect and filter

After all Wave 1 subagents complete:

```bash
uv run python -m safety_ideas.pipeline.filter_score filter-survivors <run_dir> 1
```

This merges all batch results, filters out eliminated ideas, and writes the survivors file. It prints survivor and eliminated counts.

Log the results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> filter_score info 'Stage 1 complete: quick relevance filter' '{"total_ideas": <TOTAL>, "survivors": <SURVIVORS>, "eliminated": <ELIMINATED>}'
```

## Wave 2: Full Per-Criterion Scoring (Stage 2)

### Step 2.1: Create batches from Stage 1 survivors

```bash
uv run python -m safety_ideas.pipeline.filter_score create-batches <run_dir> 2 <stage2_batch_size>
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
> **Skip the `novelty` criterion** — it is derived from evidence in Wave 3, not scored here.
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
> uv run python -m safety_ideas.pipeline.filter_score read-batch [BATCH_PATH]
> ```
>
> **Step 2:** For EACH idea, score it against every criterion (except novelty). Match the idea against the rubric level descriptions and pick the level that best fits — do NOT score based on gut feeling. Compute the weighted score. Compute overall confidence as the average of per-criterion confidences.
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
>     }
>   },
>   "weighted_score": <computed weighted average>,
>   "confidence": <average of per-criterion confidences>,
>   "eliminated": <true if weighted_score below [MIN_SCORE]>,
>   "elimination_reason": <null or "Stage 2: weighted score [X] below threshold [Y]">
> }
> ```
>
> Do NOT skip any ideas.
>
> **Step 4:** Write results:
> ```bash
> uv run python -m safety_ideas.pipeline.filter_score write-batch-results [RESULT_PATH] '<json_array>'
> ```
>
> Where [RESULT_PATH] is: `[RUN_DIR]/filter_score/results/stage2/batch_[NNN]_results.json`

### Step 2.3: Collect and filter

```bash
uv run python -m safety_ideas.pipeline.filter_score filter-survivors <run_dir> 2
```

Log the results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> filter_score info 'Stage 2 complete: full scoring' '{"survivors": <SURVIVORS>, "eliminated": <ELIMINATED>}'
```

## Wave 3: Novelty Assessment & Citation Verification (Stage 3)

### Step 3.1: Create batches from Stage 2 survivors

```bash
uv run python -m safety_ideas.pipeline.filter_score create-batches <run_dir> 3 <stage3_batch_size>
```

### Step 3.2: Launch parallel subagents

Launch **one Agent subagent per batch**, all in a single message. These subagents use tools (WebSearch, Bash) — keep batches small.

**Subagent prompt template:**

> You are assessing novelty and verifying citations for AI Safety research ideas.
>
> **IMPORTANT — Source reading policy:** Only read abstracts, summaries, and introductions — never full papers. For novelty assessment, targeted deep reading of specific sections (discussion, limitations, future work) is permitted via the paper_fetcher module when abstract-level evidence is insufficient.
>
> **Novelty Classification Rubric:**
> - **already_solved** (score 1): Existing published work FULLY addresses this idea — the proposed research would not produce new knowledge. You must cite the specific paper(s).
> - **largely_addressed** (score 2): Multiple published works cover most of the proposed contribution; remaining gaps are minor.
> - **partially_addressed** (score 3): Published work exists on the topic but the specific angle/method/combination proposed has not been explored.
> - **mostly_novel** (score 4): No direct published work on this specific proposal; related work exists in adjacent areas.
> - **novel** (score 5): No published work found addressing this question or approach.
>
> **HARD GATE:** If classification is "already_solved", the idea is eliminated immediately.
>
> **Citation Relevance Rubric (verification threshold: [THRESHOLD]):**
> [FULL CITATION RELEVANCE RUBRIC from show-citation-relevance]
>
> **Citation removal consequences:**
> - Relevance 3 (Substantive): Flag with warning, idea survives
> - Relevance 4 (Load-bearing): Confidence penalty, re-score affected criterion, attempt rewrite
> - Relevance 5 (Foundational): Attempt rewrite; eliminate if idea cannot stand without it
>
> **Confidence Rubric:**
> [FULL CONFIDENCE RUBRIC]
>
> **Step 1:** Read your batch:
> ```bash
> uv run python -m safety_ideas.pipeline.filter_score read-batch [BATCH_PATH]
> ```
>
> **Step 2:** For EACH idea in the batch, perform:
>
> **2a — Novelty Assessment:**
> - Use WebSearch to search for existing work on ArXiv, Semantic Scholar, and Google Scholar
> - Collect evidence: for each relevant paper, note source, title, url, summary
> - If any evidence papers warrant deeper reading (abstract suggests overlap but degree is ambiguous), fetch sections:
>   ```bash
>   uv run python -m safety_ideas.connectors.paper_fetcher fetch-batch '<json_array_of_urls>'
>   ```
> - Classify novelty using the rubric above
> - Validate and format:
>   ```bash
>   uv run python -m safety_ideas.pipeline.novelty format '<novelty_json>'
>   ```
>
> **2b — Citation Relevance & Verification:**
> - Score each citation's relevance (1-5) using the rubric
> - For citations at or above the threshold, verify via:
>   ```bash
>   uv run python -m safety_ideas.verification.citation lookup-idea '<idea_json>'
>   ```
> - Judge each verified citation: verified, corrected, or removed
> - For citations about to be removed, try WebSearch with paper title + authors first
> - Apply consequences for removed citations based on relevance level
>
> **Step 3:** Build a JSON array of results. For each idea:
> ```json
> {
>   "idea_id": "<id>",
>   "title": "<title>",
>   "run_id": "<run_id>",
>   "novelty_assessment": {
>     "classification": "<one of the 5 levels>",
>     "evidence": [{"source": "<src>", "title": "<paper>", "url": "<url>", "summary": "<relevance>"}],
>     "confidence": <0.0-1.0>,
>     "derived_score": <1-5>,
>     "reasoning": "<2-4 sentences>"
>   },
>   "citation_verification": {
>     "relevance_scores": [{"citation": {...}, "relevance_score": <1-5>, "relevance_label": "<label>", "relevance_reasoning": "<1 sentence>"}],
>     "verified": [{"citation": {...}, "reason": "<1 sentence>"}],
>     "corrected": [{"original": {...}, "corrected": {...}, "reason": "<1 sentence>"}],
>     "removed": [{"citation": {...}, "reason": "<1 sentence>", "relevance_score": <int>}]
>   },
>   "scores_updates": {<criterion_name>: {"score": <new>, "reasoning": "<updated>", "confidence": <new>}},
>   "eliminated": <true if already_solved or foundational citation removed and unrewritable>,
>   "elimination_reason": <null or reason string>
> }
> ```
>
> If web search fails for an idea: classify as "mostly_novel" (conservative — do not eliminate).
> If citation lookup APIs fail: keep all citations as-is, record "api_unavailable".
>
> Do NOT skip any ideas.
>
> **Step 4:** Write results:
> ```bash
> uv run python -m safety_ideas.pipeline.filter_score write-batch-results [RESULT_PATH] '<json_array>'
> ```
>
> Where [RESULT_PATH] is: `[RUN_DIR]/filter_score/results/stage3/batch_[NNN]_results.json`

### Step 3.3: Collect and filter

```bash
uv run python -m safety_ideas.pipeline.filter_score filter-survivors <run_dir> 3
```

Log the results:

```bash
uv run python -m safety_ideas.pipeline.orchestrator log <run_dir> filter_score info 'Stage 3 complete: novelty + citations' '{"survivors": <SURVIVORS>, "eliminated": <ELIMINATED>}'
```

## Phase 4: Assemble Final Scored Ideas

After all 3 waves complete, assemble the final scored idea JSON files.

Read the results from all 3 stages:

```bash
uv run python -m safety_ideas.pipeline.filter_score merge-results <run_dir> 1
uv run python -m safety_ideas.pipeline.filter_score merge-results <run_dir> 2
uv run python -m safety_ideas.pipeline.filter_score merge-results <run_dir> 3
```

For each idea that appears in the Stage 2 results (all ideas that were scored, both survivors and eliminated):

1. Start with the Stage 2 result (contains `original_idea`, `scores`, `weighted_score`, `eliminated`)
2. If the idea has Stage 3 results, splice in:
   - `novelty_assessment` from Stage 3
   - `citation_verification` from Stage 3
   - Update the `novelty` score in `scores` to `novelty_assessment.derived_score`
   - Apply any `scores_updates` from citation consequences
   - Recompute `weighted_score` with novelty now included
   - Set `filter_stage_passed` to 3 for Stage 3 survivors
   - Apply elimination from Stage 3 if applicable
3. If the idea was eliminated at Stage 1, build a minimal scored idea with the Stage 1 result data
4. Add metadata: `stage: "filter_score"`, `timestamp`, `filter_stage_passed`

Write each final scored idea:

```bash
uv run python -m safety_ideas.pipeline.filter_score write <run_dir> '<scored_idea_json>'
```

## Phase 5: Results Summary

Present the coordinator with:

1. **Pipeline summary**: Total ideas → Stage 1 survivors → Stage 2 survivors → Stage 3 survivors
2. **Eliminated ideas**: List with idea_id, title, elimination reason, stage eliminated
3. **Surviving ideas** (sorted by weighted_score, highest first):
   - idea_id, title, weighted_score, confidence
   - Per-criterion scores summary
   - Novelty classification
   - Citation verification status (verified/corrected/removed counts, any warnings from removed load-bearing or foundational citations)
4. **Team weight overrides** applied (if any)

Tell the coordinator:
> Your scored ideas are in `data/runs/<timestamp>/filter_score/`. Surviving ideas are ready for refinement with `/refine-ideas`. You can review individual scored ideas in the JSON files for full reasoning.

## Error Handling

- **Subagent failure**: After each wave, check if any batch result files are missing. Re-launch failed batches once. If retry also fails, mark those ideas as eliminated with "Scoring failed: subagent error" and add a warning to the pipeline log.
- **Web search failure** (Wave 3): classify as "mostly_novel" by default (conservative — do not eliminate)
- **Citation lookup API failure** (Wave 3): note unverified status, keep all citations as-is, record "api_unavailable"
- **Scoring failure** for individual ideas within a subagent: log the error within the batch results and continue with remaining ideas
- Always produce output even with degraded sources — partial scoring is better than none
