# Research Topic Deep Dive

Pull the most relevant papers from a research topic and produce a structured report with analysis across coordinator-selected dimensions.

**IMPORTANT — Source reading policy:** Start with abstracts and summaries. When a paper seems highly relevant, read deeper into specific sections (discussion, limitations, future work, methodology) to extract dimension-specific insights. Do NOT read full papers end-to-end.

## Step 1: Define the Topic

Ask the coordinator:

> What research topic would you like me to investigate?
>
> This can be:
> - A specific research question (e.g., "How do attention heads encode factual associations?")
> - A broad area (e.g., "scalable oversight")
> - A technique or method (e.g., "activation patching for circuit discovery")
> - A problem framing (e.g., "detecting deceptive alignment in frontier models")

Accept the topic and identify 3-5 key search terms/phrases to use across sources.

## Step 2: Negotiate Dimensions

Before searching, collaborate with the coordinator on which dimensions to track across papers. Present a default set and invite customization:

> I'll analyze papers across several dimensions. Here's what I'd suggest for "[TOPIC]" — but these should reflect what **you** need from this report.
>
> **Suggested dimensions:**
>
> | # | Dimension | What it captures | Why it matters |
> |---|-----------|-----------------|----------------|
> | 1 | **Methodology** | What methods/techniques are used (empirical, theoretical, hybrid) | Reveals the toolkit available and methodological gaps |
> | 2 | **Scale** | Model sizes, dataset sizes, compute requirements | Shows what's been tested at what scale — and what hasn't |
> | 3 | **Key findings** | Core results and claims | The substance of what's been discovered |
> | 4 | **Open questions** | What the authors flag as unresolved | Direct input for research idea generation |
> | 5 | **Reproducibility** | Code availability, dataset access, clarity of method | Whether you could build on this work |
>
> **Alternative dimensions you might consider:**
> - **Threat model** — what failure mode or risk each paper addresses (useful for safety-specific topics)
> - **Assumptions** — what each paper takes for granted (useful for finding weak foundations to challenge)
> - **Evaluation approach** — how results are validated (useful for benchmarking/evals topics)
> - **Practical applicability** — how close to deployment-ready the work is (useful for applied research)
> - **Theoretical grounding** — what formal frameworks underpin the work (useful for theory-heavy topics)
> - **Stakeholder relevance** — who would act on these findings (useful for governance/policy topics)
> - **Temporal trajectory** — how the topic has evolved over time (useful for mature fields)
> - **Cross-domain connections** — links to other research areas (useful for interdisciplinary work)
>
> **Which dimensions would you like to track?** You can:
> 1. Use the suggested set as-is
> 2. Add, remove, or replace dimensions
> 3. Define your own from scratch
>
> For each dimension you pick, it helps to know **why** — what decision or understanding will it support?

Wait for the coordinator's response. If they pick the defaults, proceed. If they customize, confirm the final dimension set before searching.

Store the final agreed dimensions — they structure the entire report.

---

## Step 3: Literature Search (Parallelized)

Launch **3 parallel sub-agents** to search different source categories simultaneously:

**Sub-agent 1: Academic Literature (CrossRef + Semantic Scholar)**

> You are searching academic databases for papers on a research topic.
>
> **Topic:** [TOPIC]
> **Search terms:** [KEY TERMS]
>
> 1. Run structured database searches with at least 3 different query phrasings:
>    ```bash
>    uv run python -m saim.verification.citation search-crossref '<query>'
>    uv run python -m saim.verification.citation search-s2 '<query>'
>    ```
> 2. For each result, record: `{"source": "<crossref|semantic_scholar>", "title": "<title>", "authors": "<authors>", "url": "<url>", "doi": "<doi if available>", "year": "<year if available>"}`.
>
> Run at least 3 query variations: one broad, one narrow, one using alternative terminology.
> Return your findings as a JSON array. Aim for 15-30 unique results.

**Sub-agent 2: Web Search (ArXiv, Google Scholar, broader web)**

> You are searching the web for papers, preprints, and technical reports on a research topic.
>
> **Topic:** [TOPIC]
> **Search terms:** [KEY TERMS]
>
> 1. Use WebSearch with at least 4-5 queries:
>    - `"[topic] survey"` or `"[topic] review paper"`
>    - `"[topic] [current year]"` (recent work)
>    - `"[topic] arxiv"` (preprints)
>    - `"[topic] open problems"` or `"[topic] challenges"`
>    - Alternative terminology variations
> 2. For each relevant result, record: `{"source": "<arxiv|google_scholar|web>", "title": "<title>", "url": "<url>", "snippet": "<1-2 sentence summary from search results>"}`.
>
> Return your findings as a JSON array. Aim for 15-25 unique results.

**Sub-agent 3: LessWrong & Alignment Forum**

> You are searching LessWrong and the Alignment Forum for posts and discussions on a research topic.
>
> **Topic:** [TOPIC]
> **Search terms:** [KEY TERMS]
>
> 1. Use WebSearch with `allowed_domains: ["lesswrong.com", "alignmentforum.org"]` for at least 3 queries:
>    - `[topic] AI safety`
>    - `[topic] alignment`
>    - `[specific technical terms from topic]`
> 2. For promising results, use WebFetch to read the post introduction and key sections.
> 3. For each relevant result, record: `{"source": "<lesswrong|alignment_forum>", "title": "<post title>", "url": "<url>", "summary": "<1-2 sentences>"}`.
>
> Return your findings as a JSON array.

After all sub-agents complete, merge results and deduplicate by URL/title. If a sub-agent fails, proceed with results from the others.

---

## Step 4: Relevance Ranking and Selection

From the merged results, select the **top 15-25 most relevant papers** based on:
1. Direct relevance to the stated topic
2. Citation count / influence signals (when available)
3. Recency (prefer recent work, but include foundational older papers)
4. Source diversity (mix of academic papers, preprints, blog posts)
5. Coverage across the coordinator's chosen dimensions

Present the ranked list to the coordinator:

> I found **[N] unique sources**. Here are the top [15-25] ranked by relevance:
>
> | # | Title | Source | Year | Why relevant |
> |---|-------|--------|------|-------------|
> | 1 | ... | ArXiv | 2025 | ... |
> | 2 | ... | Semantic Scholar | 2024 | ... |
>
> Would you like me to:
> 1. Proceed with these papers for the full report
> 2. Add/remove specific papers
> 3. Adjust the focus or search for more in a specific sub-area

Wait for confirmation before deep reading.

---

## Step 5: Deep Reading and Dimension Extraction

For each selected paper, fetch deeper content when needed:

**ArXiv papers:**
```bash
uv run python -m saim.connectors.paper_fetcher fetch '<arxiv_url>'
```

**LessWrong/AF posts:**
```bash
uv run python -m saim.connectors.paper_fetcher fetch '<lw_or_af_url>'
```

**Other URLs:**
```bash
uv run python -m saim.connectors.paper_fetcher fetch '<url>'
```

For each paper, extract values for every agreed dimension. Not every paper will have data for every dimension — that's fine, mark as "N/A" or "Not discussed".

**Citation verification:** For papers that were found via search but lack strong metadata, verify they exist:
```bash
uv run python -m saim.verification.citation search-crossref '<paper title>'
uv run python -m saim.verification.citation search-s2 '<paper title>'
```

This ensures the report only includes real, verifiable papers.

---

## Step 6: Synthesis and Gap Analysis

After extracting dimension data from all papers, synthesize:

1. **Per-dimension synthesis:** For each dimension, what patterns emerge across the literature? What's the consensus, what's contested?
2. **Coverage gaps:** Which dimensions have sparse coverage? What questions remain unanswered?
3. **Research frontier:** Where is the field heading? What are the most promising open directions?
4. **Contradictions:** Where do papers disagree? What explains the disagreement?

---

## Step 7: Write Report

Write the report to `data/output/research-topic-[SANITIZED_TOPIC].md`:

```markdown
# Research Topic Report: [TOPIC]

> Generated: [DATE]
> Requested by: coordinator
> Papers analyzed: [N]

## Topic Definition

[1-2 paragraph description of the topic as scoped during Step 1]

## Dimensions Tracked

| Dimension | Description | Coordinator rationale |
|-----------|------------|----------------------|
| [dim1] | [what it captures] | [why the coordinator chose it] |

---

## Paper Catalog

### [Paper #1 Title]

- **Authors:** [authors]
- **Source:** [journal/venue/platform]
- **Year:** [year]
- **URL:** [url]
- **DOI:** [doi if available]

| Dimension | Finding |
|-----------|---------|
| [dim1] | [extracted value] |
| [dim2] | [extracted value] |

**Relevance to topic:** [1-2 sentences]

---

[Repeat for each paper]

---

## Dimension Synthesis

### [Dimension 1 Name]

**Pattern:** [What the literature collectively shows for this dimension]

**Key findings:**
- [Finding 1] — from [Paper X], [Paper Y]
- [Finding 2] — from [Paper Z]

**Gaps:** [What's missing or underexplored]

---

[Repeat for each dimension]

---

## Coverage Gap Analysis

### Under-Researched Areas
- [Gap 1] — evidence: [why this is a gap]

### Methodological Gaps
- [Gap 1] — evidence: [what approach is missing]

### Contradictions and Open Debates
- [Debate 1] — [Paper X] argues ..., while [Paper Y] argues ...

---

## Research Frontier

**Most promising open directions:**
1. [Direction 1] — supported by [evidence]
2. [Direction 2] — supported by [evidence]

**Suggested follow-up questions:**
1. [Question that emerged from the analysis]
2. [Question that emerged from gaps]

---

## Full Source List

| # | Title | Authors | Year | Source | URL | DOI |
|---|-------|---------|------|--------|-----|-----|
| 1 | ... | ... | ... | ... | ... | ... |
```

---

## Step 8: Coordinator Review

Present the coordinator with:

1. A summary of the report (paper count, key patterns, most surprising findings)
2. The most important gaps identified
3. The top 3 research directions that emerged
4. Ask if they want to:
   - Dive deeper into any specific paper or dimension
   - Adjust dimensions and re-analyze
   - Use findings as input to `/brainstorm-ideas` or `/generate-ideas`
   - Export the report as-is

If the coordinator wants changes, update the report file accordingly.

---

## Error Handling

- **Web search failure:** Fall back to CrossRef + Semantic Scholar database searches only. Note degraded coverage in the report metadata.
- **Sub-agent failure:** Proceed with results from successful sub-agents. Note which source categories are missing.
- **Paper fetcher failure:** Use abstract/snippet-level information only for that paper. Mark affected dimension extractions as "abstract-only" in the report.
- **Citation verification failure:** Keep the paper but mark as "unverified" in the source list.
- **Too few results:** If fewer than 5 papers are found, inform the coordinator and suggest broadening the topic or trying alternative search terms before producing a thin report.
- Always produce output even with degraded sources — partial analysis is better than none.

---

## Integration with Other Skills

This report can feed into:
- `/brainstorm-ideas` — use the research frontier and gaps as brainstorming seeds
- `/generate-ideas` — gaps and open questions feed directly into idea generation strategies
- `/evaluate-idea` — use the paper catalog as context when evaluating related ideas
- `/novelty-check` — the paper catalog provides a head start for novelty assessment of ideas in this area
