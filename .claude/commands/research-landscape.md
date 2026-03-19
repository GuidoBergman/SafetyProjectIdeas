# Research Landscape Discovery

Discover and map the AI Safety research landscape to guide idea generation.

## Setup

First, ensure the output directory exists:

```bash
mkdir -p data/output
```

Read the current project configuration for context on team profiles and criteria:

```bash
uv run python -m safety_ideas.config.cli show
```

## Phase 1: Discover the Landscape

Use web search to find current AI Safety research sources. Search for each of these categories:

1. **Open problems lists** (Priority 1 - most actionable for idea generation):
   - Search: "AI safety open problems list" (include current and previous year)
   - Search: "alignment research agenda open questions"
   - Search: "concrete problems in AI safety"
   - Look for lists from: ARC, MIRI, Anthropic, DeepMind, OpenAI safety, CAIS, Redwood Research, Apollo Research, FAR AI

2. **Research agendas and surveys**:
   - Search: "AI safety research agenda" (include current and previous year)
   - Search: "AI alignment survey paper"
   - Search: "technical AI safety roadmap"

3. **Key organizations and their focus areas**:
   - Search: "AI safety research organizations labs"
   - Search: "AI alignment research groups"

For each web search, use the WebSearch tool. For promising results, use WebFetch to get more detail from specific pages.

**IMPORTANT:** If web search is unavailable or returns limited results, fall back to Claude's training knowledge of the AI Safety field. The skill must produce useful output regardless of web search availability.

## Phase 2: Synthesize and Map

Starting from the 7 categories in the 800-paper shallow review taxonomy, synthesize all findings:

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
- 3-8 open problems or research directions (sourced from open problems lists where possible)
- Key organizations working in this area
- Key authors (2-5 per subfield)
- Important source documents (open problems lists, research agendas, survey papers)

If discoveries suggest additional subfields beyond the initial 7, add them.

**Deduplication:** Multiple searches will return overlapping results. When synthesizing, deduplicate organizations, authors, and source documents across subfields. An author or org may appear under multiple subfields -- that is fine -- but each source document should be listed once in the "Key Source Documents (All)" table even if it covers multiple subfields.

## Phase 3: Generate Structured Output

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

## Subfields

### [subfield_id_in_snake_case]: [Subfield Name]

**Description:** [1-2 sentence description]

**Status:** [active | emerging | mature]

**Open Problems:**
- [ ] [Problem 1] <!-- source: [source name or "claude-knowledge"] -->
- [ ] [Problem 2] <!-- source: [source name or "claude-knowledge"] -->
- [ ] [Problem 3] <!-- source: [source name or "claude-knowledge"] -->

**Key Organizations:** [Org1], [Org2], [Org3]

**Key Authors:** [Author1], [Author2], [Author3]

**Source Documents:**
- [Document title](URL) - [type: open-problems-list | research-agenda | survey | report]
- [Document title](URL) - [type]

**Priority for idea generation:** [high | medium | low]
**Rationale:** [Why this priority]

---

[Repeat for each subfield]

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

## Phase 4: Coordinator Review

After writing the output file, present the coordinator with:

1. A summary of what was discovered (number of subfields, total open problems, key sources found)
2. The suggested priority ordering
3. Ask the coordinator to review `data/output/research-landscape.md` and:
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
- Use consistent heading hierarchy: `#` title, `##` sections, `###` subfields
- Be valid markdown parseable by the `/generate-ideas` skill

**Integration contract for `/generate-ideas`:**
- The `/generate-ideas` skill parses the `## Coordinator Selection` section to find selected subfields
- A subfield is selected when its checkbox is `[x]` (e.g., `- [x] black_box_safety: ...`)
- If no subfields are marked `[x]`, `/generate-ideas` should use all subfields ordered by priority
- Subfield IDs in the Coordinator Selection section MUST match the `### [ID]: [Name]` heading IDs exactly

## Error Handling

- If web search fails: fall back entirely to Claude's training knowledge, note this in the output metadata
- If config loading fails: proceed without config context (config is informational, not required)
- Always produce output even with degraded sources -- partial landscape is better than none
