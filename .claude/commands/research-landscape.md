# Research Landscape Discovery

Discover and map the AI Safety research landscape to guide idea generation.

**IMPORTANT — Source reading policy:** Throughout this entire skill, NEVER read full papers or full system cards. Only read **abstracts, executive summaries, introductions, and conclusion sections**. For system cards specifically, read only the executive summary / safety evaluations summary. The goal is landscape mapping, not deep paper analysis. WebFetch should target summary pages, abstract pages, and landing pages — not full PDFs or full documents.

## Setup

First, ensure the output directory exists:

```bash
mkdir -p data/output
```

## Phase 1: Discover the Landscape (Parallelized)

This phase launches **parallel subagents** to search different categories simultaneously. Each subagent performs web searches in its assigned category and returns structured findings.

**Orchestration instructions:**
1. Launch all category subagents in parallel using the Agent tool (one Agent call per category, all in a single message)
2. Each subagent should be given a clear, self-contained prompt specifying: the category to search, the exact searches to perform, the output format to return, and the source reading policy (abstracts/summaries only)
3. Each subagent returns its findings as structured text (not files) — the orchestrator synthesizes all results in Phase 2
4. If a subagent fails or returns empty results, proceed with the remaining categories — partial coverage is acceptable
5. After all subagents complete, collect their results and proceed to Phase 2

**Subagent prompt template** (adapt per category):
> You are researching the AI Safety landscape for category: [CATEGORY NAME].
> Perform the following web searches using WebSearch. For promising results, use WebFetch to read ONLY abstracts, executive summaries, or landing pages — NEVER full papers or full documents.
> Searches: [LIST OF SEARCHES]
> For each relevant result found, extract: title, URL, type (open-problems-list / research-agenda / survey / report / system-card / project-list / incident-report), organization, key authors, and a 1-2 sentence summary of what it contributes to the landscape.
> Also extract any specific open problems, research directions, or research questions mentioned.
> Return your findings as a structured list.

### Category 1: Open Problems Lists (Priority 1 — most actionable)
- Search: "AI safety open problems list" (include current and previous year)
- Search: "alignment research agenda open questions"
- Search: "concrete problems in AI safety"
- Look for lists from: ARC, MIRI, Anthropic, DeepMind, OpenAI safety, CAIS, Redwood Research, Apollo Research, FAR AI, AISI, Conjecture, METR, EleutherAI, Epoch AI, CHAI Berkeley, Apart Research

### Category 2: Research Agendas and Surveys
- Search: "AI safety research agenda" (include current and previous year)
- Search: "AI alignment survey paper"
- Search: "technical AI safety roadmap"

### Category 3: Key Organizations and Their Focus Areas
- Search: "AI safety research organizations labs"
- Search: "AI alignment research groups"
- Cover at minimum: ARC, MIRI, Anthropic, DeepMind, OpenAI safety, CAIS, Redwood Research, Apollo Research, FAR AI, AISI (UK AI Safety Institute), Conjecture, EleutherAI, Epoch AI, GovAI, CHAI (Berkeley), NYU alignment group (Sam Bowman), Apart Research, METR (formerly ARC Evals), CSET Georgetown, Harvard Kempner Institute, Stanford HAI safety work

### Category 4: Recent Breakthrough Papers and Open Threads
- Search: "AI safety breakthrough paper [current year]"
- Search: "most cited AI alignment paper [current year]"
- Search: "AI safety best paper NeurIPS ICML ICLR [current year]" (main conference papers only, NOT workshop papers)
- For each breakthrough found, note: what open questions it raises, limitations acknowledged by authors, obvious extensions
- **Only include papers from main conferences or by highly respected authors. No workshop papers, no preprints from unknown authors.**

### Category 5: System Cards and Model Safety Evaluations
- Search: "AI model system card safety evaluations [current year]"
- Search for system cards from: Anthropic (Claude), OpenAI (GPT), Google (Gemini), Meta (Llama)
- **Read ONLY the executive summary / safety evaluation summary sections — never the full system card**
- Extract: novel evaluation methods used, safety-relevant findings, gaps identified in current evaluation approaches

### Category 6: Alignment Forum and LessWrong Active Discussions
- Search: "site:alignmentforum.org open problem [current year]"
- Search: "site:lesswrong.com AI safety research direction [current year]"
- Focus on highly-upvoted posts proposing new research directions
- Read only the post summary/introduction — not full posts

### Category 7: Funding and Grant Priorities
- Search: "AI safety research grants open philanthropy [current year]"
- Search: "LTFF long-term future fund AI safety grants"
- Search: "survival and flourishing fund AI safety"
- Search: "AI safety RFP request for proposals"
- What funders prioritize reveals community consensus on neglected areas

### Category 8: Government and Regulatory Safety Research Priorities
- Search: "AISI UK AI Safety Institute research priorities"
- Search: "NIST AI safety framework research"
- Search: "EU AI Act safety research requirements"
- Search: "US AI Safety Institute priorities"

### Category 9: Available Tools, Benchmarks, and Datasets
- Search: "AI safety benchmark dataset [current year]"
- Search: "alignment evaluation tool open source"
- Identify existing infrastructure and gaps — this informs feasible project ideas

### Category 10: Failure Modes and Incident Databases
- Search: "AI incident database safety failures"
- Search: "AI system failure case study"
- Real-world failures are an excellent source of grounded research questions

### Category 11: Curated Project Idea Lists
- Search: "AI safety project ideas for beginners"
- Search: "AI alignment research project suggestions"
- Search: "MATS mentorship project list"
- Search: "SERI MATS research directions"
- Search: "AI safety camp project proposals"
- Search: "BlueDot Impact AI safety projects"
- Search: "Apart Research hackathon projects"
- These are pre-curated and feasibility-assessed — high value as input

For each web search, use the WebSearch tool. For promising results, use WebFetch to get more detail from specific pages — but **only abstracts, executive summaries, and landing pages**.

**IMPORTANT:** If web search is unavailable or returns limited results, fall back to Claude's training knowledge of the AI Safety field. The skill must produce useful output regardless of web search availability.

## Phase 2: Synthesize and Map

Starting from the 7 categories in the 800-paper shallow review taxonomy, synthesize all findings from the parallel subagents:

**Starting categories (expand/modify based on discoveries):**
1. Black-box Safety (adversarial robustness, red-teaming, jailbreak defenses)
2. Interpretability (mechanistic interpretability, probing, feature visualization)
3. Safety by Construction (RLHF, constitutional AI, safe-by-design architectures)
4. Make AI Solve It (AI-assisted alignment, scalable oversight, debate)
5. Theory (agent foundations, decision theory, formal verification)
6. Multi-agent & Evals (multi-agent safety, evaluation benchmarks, capability elicitation)
7. Labs (governance, policy, deployment practices)

For each subfield discovered, compile:
- A short description of the subfield
- Open problems or research directions (sourced from open problems lists where possible)
- Key organizations working in this area
- Key authors (up to 25 per subfield — only include well-known, established researchers to ensure reliability)
- Important source documents (open problems lists, research agendas, survey papers)
- Source code availability signal: for key papers, note which have open-source code
- Key datasets and benchmarks used in this subfield
- Methodological approaches commonly used (e.g., probing, activation patching, formal proofs, red-teaming)
- Recent surprising results that demand follow-up experiments

If discoveries suggest additional subfields beyond the initial 7, add them.

**Deduplication:** Multiple searches will return overlapping results. When synthesizing, deduplicate organizations, authors, and source documents across subfields. An author or org may appear under multiple subfields -- that is fine -- but each source document should be listed once in the "Key Source Documents (All)" table even if it covers multiple subfields.

## Phase 3: Landscape Gaps Analysis

After mapping what exists, explicitly analyze what is **missing** or under-served:

- **Under-researched subfields**: Subfields mentioned in open problems lists but with few recent papers or active researchers
- **Methodology gaps**: Areas where the community has identified problems but no good methodology exists to attack them
- **Scale gaps**: Research done on small models that hasn't been replicated or tested on larger ones
- **Infrastructure gaps**: Needed benchmarks, datasets, or tools that don't exist yet
- **Replication gaps**: Important results that haven't been independently verified

This analysis is critical for idea generation — gaps are where the most impactful new projects live. Include the gaps analysis as a dedicated section in the output file.

## Phase 4: Generate Structured Output

Write the landscape summary to `data/output/research-landscape.md` using EXACTLY the following format. This format is designed to be parseable by the `/generate-ideas` skill.

**Use the following structure as a guide (do NOT copy-paste -- fill in real content):**

```markdown
# AI Safety Research Landscape

> Generated: [DATE]
> Sources: [list of key sources consulted]

## Metadata

- **Total subfields:** [N]
- **Total open problems identified:** [N]
- **Source priority:** Open problems lists > Research agendas > Survey papers > Claude knowledge

---

## Quick Reference

**Top 5 most actionable sources** (the ones to read first for idea generation):
1. [Source name](URL) — why it's actionable
2. ...

**Top 5 most promising subfields for idea generation:**
1. [Subfield] — why
2. ...

---

## Subfields

### [subfield_id_in_snake_case]: [Subfield Name]

**Description:** [1-2 sentence description]

**Status:** [active | emerging | mature]

**Open Problems:**
- [ ] [Problem 1] <!-- source: [source name or "claude-knowledge"] -->
- [ ] [Problem 2] <!-- source: [source name or "claude-knowledge"] -->
- [ ] [Problem 3] <!-- source: [source name or "claude-knowledge"] -->

**Key Organizations:** [Org1], [Org2], [Org3]

**Key Authors:** [Author1], [Author2], [Author3] (up to 10 — established researchers only)

**Source Documents:**
- [Document title](URL) - [type: open-problems-list | research-agenda | survey | report | system-card | project-list | incident-report]
- [Document title](URL) - [type]

**Source Code Availability:** [Note which key papers in this subfield have open-source implementations]

**Key Datasets & Benchmarks:** [List commonly used evaluation resources]

**Common Methodologies:** [e.g., activation patching, probing, red-teaming, formal verification]

**Recent Surprising Results:**
- [Result description] — from [paper/source] <!-- suggests follow-up: [brief idea] -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: [novel direction | experiment variation | follow-up experiment]
- Specific papers whose experiments could be varied (FR67): [paper names]
- Specific surprising results that need follow-up (FR68): [result descriptions]

**Priority for idea generation:** [high | medium | low]
**Rationale:** [Why this priority]

---

[Repeat for each subfield]

---

## Subfield Cross-Reference Matrix

| Subfield | Connects To | Via |
|----------|------------|-----|
| [subfield_id] | [other_subfield_id] | [brief explanation of connection] |

---

## Landscape Gaps

### Under-Researched Subfields
- [Gap description] <!-- evidence: [what suggests this is under-researched] -->

### Methodology Gaps
- [Gap description] <!-- evidence: [what problem exists without a good method] -->

### Scale Gaps
- [Gap description] <!-- evidence: [what small-model result needs large-model replication] -->

### Infrastructure Gaps
- [Gap description] <!-- evidence: [what benchmark/dataset/tool is missing] -->

### Replication Gaps
- [Gap description] <!-- evidence: [what important result lacks independent verification] -->

---

## Key Source Documents (All)

| Document | Type | Organization | URL | Subfields Covered |
|----------|------|-------------|-----|-------------------|
| [title] | [type] | [org] | [url] | [subfield_ids] |

---

## Coordinator Selection

> **Instructions:** Mark subfields for idea generation by changing `[ ]` to `[x]`.
> The `/generate-ideas` skill will target selected subfields.

- [ ] [subfield_id]: [Subfield Name] (priority: [high|medium|low], problems: [N])
- [ ] [subfield_id]: [Subfield Name] (priority: [high|medium|low], problems: [N])

```

Write the actual file with real discovered content using a bash heredoc or by composing the content directly. The above is a structural template only.

## Phase 5: Coordinator Review

After writing the output file, present the coordinator with:

1. A summary of what was discovered (number of subfields, total open problems, key sources found)
2. The suggested priority ordering
3. The most important landscape gaps identified
4. Ask the coordinator to review `data/output/research-landscape.md` and:
   - Confirm or adjust subfield priorities
   - Select which subfields to target for idea generation (mark with `[x]` in the Coordinator Selection section)
   - Add any subfields or open problems that were missed

If the coordinator provides selections, update the file accordingly.

## Output Contract

The output file `data/output/research-landscape.md` MUST:
- Use `###` headings for each subfield with format `### [ID]: [Name]` where ID is `snake_case` (e.g., `black_box_safety`, `mechanistic_interpretability`)
- Use `- [ ]` checkbox format for open problems (allows coordinator marking)
- Include `<!-- source: ... -->` comments on each open problem for traceability
- Include the `## Coordinator Selection` section with checkboxes for subfield selection
- Include the `## Landscape Gaps` section with gap categories
- Include the `## Subfield Cross-Reference Matrix` section
- Include the `## Quick Reference` section at the top
- Include per-subfield: Source Code Availability, Key Datasets & Benchmarks, Common Methodologies, Recent Surprising Results, Generation Strategy Hints
- Use consistent heading hierarchy: `#` title, `##` sections, `###` subfields
- Be valid markdown parseable by the `/generate-ideas` skill

**Integration contract for `/generate-ideas`:**
- The `/generate-ideas` skill parses the `## Coordinator Selection` section to find selected subfields
- A subfield is selected when its checkbox is `[x]` (e.g., `- [x] black_box_safety: ...`)
- If no subfields are marked `[x]`, `/generate-ideas` should use all subfields ordered by priority
- Subfield IDs in the Coordinator Selection section MUST match the `### [ID]: [Name]` heading IDs exactly
- The `## Landscape Gaps` section feeds directly into idea generation — gaps are high-priority targets for novel project ideas
- The "Generation Strategy Hints" per subfield guide which generation strategies to prioritize
- The "Recent Surprising Results" per subfield feed FR68 (follow-up experiments)
- The "Source Code Availability" signal feeds FR69 (papers with code are preferred bases for extension work)

## Error Handling

- If web search fails: fall back entirely to Claude's training knowledge, note this in the output metadata
- If config loading fails: proceed without config context (config is informational, not required)
- If individual subagents fail: proceed with results from successful subagents, note gaps in metadata
- Always produce output even with degraded sources -- partial landscape is better than none
