# Novelty Assessment & Citation Verification

Perform a full novelty assessment and citation verification for one or more AI Safety research ideas. This skill is used standalone or referenced by other skills (`/score-ideas` Wave 3, `/evaluate-idea` Step 3).

## Setup

Load the citation relevance rubric and threshold:

```bash
uv run python -m saim.config.cli show-citation-relevance
```

Load the confidence rubric:

```bash
uv run python -m saim.config.cli show-scoring
```

Save both outputs — they are used throughout the protocol below.

## Input

Ask the coordinator how they want to provide the idea(s):

> How would you like to provide the idea(s)?
> 1. **By ID** — provide an idea ID (e.g., "gen-0017") and I'll load it from `data/ideas/`
> 2. **Describe it** — paste or describe the idea inline
> 3. **From a batch file** — provide a batch file path (used by pipeline subagents)

### If by ID (option 1):
Read the idea file from `data/ideas/<idea_id>.md`. Parse the YAML frontmatter and markdown body.

### If described inline (option 2):
Accept the idea description. At minimum, you need a title, research question, and approach outline to assess novelty.

### If from a batch file (option 3):
```bash
uv run python -m saim.pipeline.filter_score read-batch <BATCH_PATH>
```
Process each idea in the batch sequentially through the protocol below.

---

## Novelty Assessment Protocol

**IMPORTANT — Source reading policy:** The goal is to not miss important information that could change the novelty classification. Start with abstracts and summaries. When a paper seems relevant, use judgment about what sections to read deeper — if reading the discussion, limitations, future work, or appendix could reveal information that would change your assessment, read them. Do not read full papers end-to-end just because they seem related; read the specific sections where the answer is likely to be.

### Step N1: Literature Search

Search for existing work using multiple sources. Construct search queries from the idea's title, research question, and key concepts.

**Web search** (broad coverage — ArXiv, Semantic Scholar, Google Scholar):
Use WebSearch to find existing papers, blog posts, and research on the idea's core question and approach.

**Structured database search** (precise metadata):
```bash
uv run python -m saim.verification.citation search-crossref '<key_terms>'
```

```bash
uv run python -m saim.verification.citation search-s2 '<key_terms>'
```

Run at least 2-3 search queries with different phrasings to maximize coverage (e.g., one broad, one narrow, one using alternative terminology).

### Step N2: Evidence Collection

For each relevant paper or work found, record:
- **source**: where it was found (arxiv, semantic_scholar, crossref, google_scholar, blog)
- **title**: paper/post title
- **url**: link to the work
- **summary**: 1-2 sentences on how it relates to the idea being assessed

### Step N3: Deep Reading

For relevant papers, consider whether reading specific sections could change your assessment. If a paper's abstract suggests it might address the idea but you're unsure of the degree, or if the answer likely lives in the discussion/limitations/future work/appendix — fetch those sections:

```bash
uv run python -m saim.connectors.paper_fetcher fetch-batch '<json_array_of_urls>'
```

The goal is to not miss information that would change the novelty classification. Don't read every related paper end-to-end, but don't skip deeper reading when it could matter.

### Step N4: Classify Novelty

Using all collected evidence, classify the idea against this rubric:

| Classification | Score | Definition |
|---|---|---|
| **already_solved** | 1 | Existing published work FULLY addresses this idea — the proposed research would not produce new knowledge. You must cite the specific paper(s). |
| **largely_addressed** | 2 | Multiple published works cover most of the proposed contribution; remaining gaps are minor. |
| **partially_addressed** | 3 | Published work exists on the topic but the specific angle/method/combination proposed has not been explored. |
| **mostly_novel** | 4 | No direct published work on this specific proposal; related work exists in adjacent areas. |
| **novel** | 5 | No published work found addressing this question or approach. |

Match the evidence against the rubric level descriptions — do NOT classify based on gut feeling. Write 2-4 sentences of reasoning referencing specific evidence.

Assign a confidence score (0.0-1.0) using the confidence rubric from setup.

### Step N5: Validate and Format

```bash
uv run python -m saim.pipeline.novelty format '<novelty_json>'
```

Where `<novelty_json>` is:
```json
{
  "classification": "<one of the 5 levels>",
  "evidence": [{"source": "...", "title": "...", "url": "...", "summary": "..."}],
  "confidence": 0.0-1.0,
  "reasoning": "2-4 sentences"
}
```

### HARD GATE

If classification is **"already_solved"**, the idea is eliminated immediately.

In standalone mode, flag prominently:
> **WARNING: This idea appears to be already solved.** [list existing works]. Consider pivoting to a related open question — I can help with that.

---

## Citation Verification Protocol

For ideas that have cited sources (in their "Cited Sources" or equivalent section), verify them.

### Step C1: Score Citation Relevance

For each citation in the idea, score its relevance to the idea's argument using the citation relevance rubric loaded in setup. This determines how much damage removing it would cause.

### Step C2: Verify Citations

For citations at or above the verification threshold (from the rubric config), verify via:

```bash
uv run python -m saim.verification.citation lookup-idea '<idea_json>'
```

This searches CrossRef (by DOI if available, then by title) and Semantic Scholar (by title) for each citation. It returns metadata for you to judge.

For each citation, judge one of:
- **verified** — metadata confirms the citation exists and is accurately represented
- **corrected** — the citation exists but details (title, authors, year) need correction
- **removed** — the citation cannot be found or does not support the claim made

Before removing a citation, try one more WebSearch with the paper title + authors to rule out API gaps.

### Step C3: Apply Consequences for Removed Citations

Based on the relevance score of each removed citation:

| Relevance | Label | Consequence |
|---|---|---|
| 3 | Substantive | Flag with warning. Idea survives. |
| 4 | Load-bearing | Apply confidence penalty to the idea. Re-score the affected criterion. Attempt to rewrite the claim without the citation. |
| 5 | Foundational | Attempt to rewrite the claim. If the idea cannot stand without this citation, eliminate the idea. |

Citations with relevance 1-2 (Peripheral/Supporting) can be removed without consequence.

---

## Output Format

For each idea processed, produce:

```json
{
  "idea_id": "<id>",
  "title": "<title>",
  "novelty_assessment": {
    "classification": "<one of the 5 levels>",
    "evidence": [{"source": "<src>", "title": "<paper>", "url": "<url>", "summary": "<relevance>"}],
    "confidence": 0.0-1.0,
    "derived_score": 1-5,
    "reasoning": "2-4 sentences"
  },
  "citation_verification": {
    "relevance_scores": [{"citation": {}, "relevance_score": 1-5, "relevance_label": "<label>", "relevance_reasoning": "<1 sentence>"}],
    "verified": [{"citation": {}, "reason": "<1 sentence>"}],
    "corrected": [{"original": {}, "corrected": {}, "reason": "<1 sentence>"}],
    "removed": [{"citation": {}, "reason": "<1 sentence>", "relevance_score": 0}]
  },
  "scores_updates": {},
  "eliminated": false,
  "elimination_reason": null
}
```

The `scores_updates` dict contains any criterion scores that changed due to citation removal consequences. Keys are criterion names, values are `{"score": <new>, "reasoning": "<updated>", "confidence": <new>}`.

---

## Error Handling

- **Web search failure**: Classify as "mostly_novel" (conservative — do not eliminate). Note the failure in reasoning.
- **Citation lookup API failure**: Keep all citations as-is, record "api_unavailable" in the verification results.
- **Paper fetcher failure**: Proceed with abstract-level evidence only. Do not block on deep reading.
- Always produce output even with degraded sources — partial assessment is better than none.

---

## Standalone Summary

When running standalone (not as part of another skill), present results to the coordinator:

1. **Novelty classification** with score, confidence, and reasoning
2. **Key existing works** found (top 3-5 most relevant)
3. **Citation verification summary**: verified/corrected/removed counts, any warnings
4. **Recommendation**: whether the idea should proceed, pivot, or be reconsidered
