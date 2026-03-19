# Score and Filter AI Safety Research Ideas

Score generated ideas against configured criteria, assess novelty, and verify citations.

**IMPORTANT — Source reading policy:** Throughout this entire skill, NEVER read full papers or full system cards. Only read **abstracts, summaries, and introductions**. WebFetch should target summary pages, not full documents.

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

Load all generated ideas:

```bash
uv run python -m safety_ideas.pipeline.generate read <run_dir>
```

Parse the JSON output and store the list of ideas for processing.

Load participant profile for context on the team's skill level:

```bash
uv run python -c "
from safety_ideas.config.participants import get_default_participant
p = get_default_participant()
if p:
    print(f'name: {p.name}')
    print(f'background: {p.background}')
    print(f'technical_skills: {p.technical_skills}')
    print(f'compute_resources: {p.compute_resources}')
else:
    print('NO_PARTICIPANT')
"
```

## Phase 1: Quick Relevance Filter (Stage 1)

For each idea, do a quick relevance and scope check. Read just the title, problem, and direction fields.

Evaluate each idea on basic relevance to AI Safety and scope appropriateness. Assign a quick score (1-5). Ideas scoring below 2.0 are eliminated immediately.

For each idea that passes, note it as a Stage 1 survivor.

For each idea that fails, record it with elimination reason "Stage 1: quick relevance score below 2.0".

Log the Stage 1 results:

```bash
uv run python -c "
from pathlib import Path
from safety_ideas.pipeline.orchestrator import PipelineLogger
logger = PipelineLogger(Path('<run_dir>'))
logger.log('filter_score', 'info', 'Stage 1 complete: quick relevance filter', {
    'total_ideas': <TOTAL>,
    'survivors': <SURVIVORS>,
    'eliminated': <ELIMINATED>
})
"
```

## Phase 2: Full Per-Criterion Scoring (Stage 2)

For each surviving idea, score it against ALL criteria and active weights loaded from `show-scoring` in Setup. Do NOT hardcode criteria names or weights — use exactly what `show-scoring` returned.

Before scoring, echo the active configuration you are using:
> **Scoring with:** team=[default_team], criteria=[list each criterion name=active_weight], thresholds=[filter_score min_score, rank min_score]

For each criterion, use the rubric from the config to assign a score 1-5 with explicit reasoning.

**Scoring format for each criterion:**
- **Score** (1-5): Based on the rubric levels
- **Reasoning**: 1-3 sentences explaining why this score, referencing the rubric level
- **Confidence** (0.0-1.0): How confident you are in this score

After scoring all criteria, compute the weighted score. Then write each scored idea:

```bash
uv run python -m safety_ideas.pipeline.filter_score write <run_dir> '<scored_idea_json>'
```

Where `<scored_idea_json>` includes all the fields from the scored idea format (see story-4.1.md for the full JSON schema).

Ideas with weighted score below the `min_score` threshold from `config/pipeline.yaml` (default 2.5) are eliminated at Stage 2.

## Phase 3: Novelty Assessment & Citation Verification (Stage 3)

For each idea that passed Stage 2:

### 3a: Hybrid Novelty Assessment

Search for existing work that addresses this idea. Use WebSearch to check:
- ArXiv for related papers
- Semantic Scholar for published work
- Google Scholar for broader coverage

Collect evidence as a list of relevant papers/results found. For each piece of evidence, note:
- `source`: where it was found (arxiv, semantic_scholar, google_scholar)
- `title`: paper/result title
- `url`: link if available
- `summary`: brief description of what this paper does and how it relates to the idea

After collecting all evidence, **YOU (the LLM) classify the novelty** by reading all evidence and reasoning about it. Produce:
- `classification`: one of "already_solved", "largely_addressed", "partially_addressed", "mostly_novel", "novel"
- `confidence`: 0.0-1.0 reflecting how thorough the search was and how clear the evidence is
- `reasoning`: 2-4 sentences explaining why you chose this classification, referencing specific papers

Use the rubric from `config/criteria.yaml` novelty criterion to guide your classification:
- **already_solved** (score 1): Existing published work FULLY addresses this idea — the proposed research would not produce new knowledge. You must cite the specific paper(s).
- **largely_addressed** (score 2): Multiple published works cover most of the proposed contribution; remaining gaps are minor.
- **partially_addressed** (score 3): Published work exists on the topic but the specific angle/method/combination proposed has not been explored.
- **mostly_novel** (score 4): No direct published work on this specific proposal; related work exists in adjacent areas.
- **novel** (score 5): No published work found addressing this question or approach.

Then validate and format the assessment:

```bash
uv run python -m safety_ideas.pipeline.novelty format '{"classification": "<classification>", "evidence": <evidence_json>, "confidence": <confidence>, "reasoning": "<reasoning>"}'
```

**HARD GATE:** If classification is "already_solved", the idea is eliminated immediately regardless of other scores.

### 3b: Citation Verification

For each idea that references papers (in its `relevant_context` or explicit citations), verify them:

```bash
uv run python -m safety_ideas.verification.citation verify-idea '<idea_json_with_citations>'
```

Remove unverified citations from the idea output (NFR4).

### 3c: Update Scored Ideas

Update each scored idea's JSON with:
- `novelty_assessment`: classification, evidence, confidence, derived_score
- `citation_verification`: verified, failed, removed lists
- Update the `novelty` criterion score to the derived novelty score
- Recompute `weighted_score` with novelty included
- Set `filter_stage_passed` to 3 for survivors

Write the updated scored ideas:

```bash
uv run python -m safety_ideas.pipeline.filter_score write <run_dir> '<updated_scored_idea_json>'
```

## Phase 4: Results Summary

Present the coordinator with:

1. **Pipeline summary**: Total ideas → Stage 1 survivors → Stage 2 survivors → Stage 3 survivors
2. **Eliminated ideas**: List with idea_id, title, elimination reason, stage eliminated
3. **Surviving ideas** (sorted by weighted_score, highest first):
   - idea_id, title, weighted_score, confidence
   - Per-criterion scores summary
   - Novelty classification
   - Citation verification status
4. **Team weight overrides** applied (if any)

Tell the coordinator:
> Your scored ideas are in `data/runs/<timestamp>/filter_score/`. Surviving ideas are ready for refinement with `/refine-ideas`. You can review individual scored ideas in the JSON files for full reasoning.

## Error Handling

- If web search fails during novelty assessment: note degraded assessment, classify as "mostly_novel" by default (conservative — do not eliminate)
- If citation verification APIs are down: note unverified status, do not remove citations
- If scoring fails for an individual idea: log the error and continue with remaining ideas
- Always produce output even with degraded sources — partial scoring is better than none
