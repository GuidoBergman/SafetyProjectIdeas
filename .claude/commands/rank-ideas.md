# Rank Refined AI Safety Research Proposals

Re-score refined proposals against full criteria using richer proposal content, compute weighted rankings, and produce human-scannable output (FR41).

## Setup

Determine the run directory. If the user provided a path, use it. Otherwise, find the latest run:

```bash
ls -1t data/runs/ | head -1
```

Use that as the run directory: `data/runs/<timestamp>`.

Verify refined proposals exist from the refine stage:

```bash
uv run python -m saim.pipeline.refine read <run_dir>
```

If no refined proposals exist, tell the coordinator and stop.

Load scoring configuration (criteria, weights, thresholds):

```bash
uv run python -m saim.config.cli show-scoring
```

Load team profile for weight context:

```bash
uv run python -m saim.config.cli show-participant
```

Save all configuration outputs for use in scoring prompts.

Before proceeding, echo the active configuration:
> **Ranking with:** team=[default_team], criteria=[list each criterion name=active_weight], participant=[profile summary]

## Phase 1: Load Proposals

Read all refined proposals from the run's refine/ directory:

```bash
uv run python -m saim.pipeline.refine read <run_dir>
```

Parse the output into a list of proposal objects. Each proposal contains the full refined content: research question, approach, experimental plan, impact chain, and the original scores (including novelty) from filter_score.

Log the load:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> rank info 'Loaded refined proposals for ranking' '{"proposal_count": <COUNT>}'
```

## Phase 2: Re-Score Full Proposals (FR39)

For each refined proposal, re-score against all criteria **except novelty** using the full proposal content (research question, approach, experiments, impact chain). The richer content from refinement provides better signal than the initial idea-level scoring.

**Novelty handling:** Keep the novelty score from the original filter_score assessment. Novelty was assessed via evidence-based search in Wave 3 and should not be re-evaluated without new evidence.

For each proposal, use the LLM to produce re-scored criteria:

**Scoring instructions:**

> For each criterion (excluding novelty), evaluate using the full proposal content:
> - Research question clarity and specificity
> - Approach feasibility and detail
> - Experimental plan concreteness
> - Impact chain plausibility
>
> **Scoring Rubric:** Use the rubric from show-scoring for each criterion. Match the proposal against the rubric level descriptions — do NOT score based on gut feeling.
>
> **Output per criterion:**
> ```json
> {
>   "score": <1-5>,
>   "reasoning": "<2-3 sentences referencing rubric level and specific proposal content>",
>   "confidence": <0.0-1.0>
> }
> ```

Build the full scores dict for each proposal in the format:

```json
{
  "<criterion_name>": {
    "score": <1-5>,
    "reasoning": "<reasoning>",
    "confidence": <0.0-1.0>
  }
}
```

Include the original novelty score entry unchanged. The complete scores dict should cover all criteria.

Log scoring progress:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> rank info 'Re-scoring complete' '{"proposals_scored": <COUNT>}'
```

## Phase 3: Rank and Output

### Step 3.1: Compute rankings

Build a JSON array of proposals with their full re-scored criteria, then rank:

```bash
uv run python -m saim.pipeline.rank rank <run_dir> '<proposals_json>'
```

This computes weighted scores using active criterion weights and sorts proposals highest-first. It returns the ranked proposals as JSON.

### Step 3.2: Write output to run directory

**IMPORTANT:** Only pass the ranked JSON — do NOT pass a separate markdown argument. The `write` command auto-generates the full markdown from the JSON using the `format_ranked_output` function, which includes ALL proposal fields (research question, full approach, experiments, impact chain, strength rationale, alternative framings, cited sources, scores, provenance) without any truncation. Do NOT attempt to generate or pass markdown yourself.

```bash
uv run python -m saim.pipeline.rank write <run_dir> '<ranked_json>'
```

This writes `rank/ranked_proposals.json` and `rank/ranked_proposals.md` to the run directory.

### Step 3.3: Persist to data/ideas/

```bash
uv run python -m saim.pipeline.rank persist '<ranked_json>'
```

This copies ranked proposals to `data/ideas/` for cross-run accumulation.

**Note:** `persist` only writes ideas whose novelty has been **calculated**
(`novelty_method: "novelty_assessed"`). If this is the first ranking (rank #1) and ideas
still carry **estimated** novelty, nothing is persisted — that is intentional. Run the
`novelty-rerank` workflow (calculated novelty on the top-ranked ideas + re-rank) first; it
persists the assessed top ideas itself. This enforces the project rule that ideas must not
be persisted with only estimated novelty.

Log the output:

```bash
uv run python -m saim.pipeline.orchestrator log <run_dir> rank info 'Ranking complete, output written' '{"ranked_count": <COUNT>, "top_score": <TOP_WEIGHTED_SCORE>}'
```

## Phase 4: Summary

Present the coordinator with the **top 10 proposals** in a concise table:

| Rank | Title | Weighted Score | Confidence | Top Criterion | Novelty |
|------|-------|---------------|------------|---------------|---------|
| 1 | ... | ... | ... | ... | ... |

For each entry, show only: rank, title (truncated if needed), weighted score, overall confidence, highest-scoring criterion name, and novelty classification.

Tell the coordinator:

> Ranking complete. **[N] proposals ranked.**
>
> - Full ranked output: `data/runs/<timestamp>/rank/ranked_proposals.md`
> - Machine-readable: `data/runs/<timestamp>/rank/ranked_proposals.json`
> - Persistent copy: `data/output/ranked_proposals.md`
> - Ideas accumulated in: `data/ideas/`
>
> Review the markdown file for detailed per-criterion reasoning. Proposals are sorted by weighted score (highest first) with re-scored criteria reflecting the full refined proposal content.

## Error Handling

- **No refined proposals found**: Stop early, tell coordinator to run `/refine-ideas` first
- **Re-scoring failure for individual proposal**: Log the error, fall back to original filter_score scores for that proposal, add warning to output
- **Rank CLI failure**: Retry once. If retry fails, log error and present partial results with warning
- **Persist failure**: Log warning but do not block — run-local output is the primary artifact
- Always produce output even with degraded scoring — partial ranking is better than none
