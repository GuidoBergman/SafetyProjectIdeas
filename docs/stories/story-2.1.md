# Story 2.1: Research Landscape Skill

## Story Info

- **Epic:** Epic 2 - Research Landscape Discovery
- **Story ID:** story-2.1
- **Status:** review_complete
- **Created:** 2026-03-19
- **FRs Covered:** Supports FR25-FR27 context; `/research-landscape` skill

## User Story

As a coordinator,
I want to discover and map the AI Safety research landscape before generating ideas,
So that I know which subfields and open problems exist and can decide which areas to target for idea generation.

## Acceptance Criteria

### AC1: Research Landscape Skill Discovery

**Given** the project foundation from Epic 1 exists (config schemas, loader, default config)
**When** the coordinator invokes `/research-landscape`
**Then** the skill searches for open problems lists, research agendas, and key sources across AI Safety using Claude's knowledge + active web search
**And** identifies active AI Safety subfields and maps what open problems and research directions exist in each
**And** identifies key organizations, authors, and important source documents (open problems lists, research agendas)
**And** outputs a structured markdown summary to `data/output/research-landscape.md`

### AC2: Structured Output Format

**Given** the landscape discovery has completed
**When** the output is generated
**Then** the markdown summary contains:
- List of active AI Safety subfields with descriptions
- Open problems per subfield (sourced from open problems lists, research agendas, and Claude's knowledge)
- Key organizations and their focus areas
- Key authors per subfield
- Important source documents (open problems lists, research agendas, survey papers)
- Suggested priority ordering for idea generation coverage
**And** the output is structured for both human review and programmatic consumption by `/generate-ideas`

### AC3: Coordinator Review and Selection

**Given** a landscape summary has been generated
**When** the coordinator reviews the output
**Then** they can select which subfields to target for subsequent idea generation
**And** selections are saved to `data/output/research-landscape.md` (or a companion file) so `/generate-ideas` can reference them

### AC4: Integration with Idea Generation

**Given** a landscape summary with coordinator selections exists
**When** the coordinator runs `/generate-ideas` (Epic 3)
**Then** the generation skill can reference the landscape summary to generate ideas covering all coordinator-specified subfields heavily

## Technical Notes

### Architecture References

- **Skill location:** `.claude/commands/research-landscape.md` [Source: docs/architecture.md#Project Structure]
- **Skills invoke Python via:** `uv run python -m saim.<module>` [Source: docs/architecture.md#Skill Patterns]
- **Output location:** `data/output/` directory [Source: docs/architecture.md#Project Structure]
- **No KB dependency:** This skill runs before KB exists. Uses Claude's native AI Safety knowledge + active web search (graceful KB degradation pattern) [Source: docs/architecture.md#Boundary 3]
- **Track A, step 2:** This is the second implementation step in Track A, after project initialization [Source: docs/architecture.md#Decision Impact Analysis]

### Key Design Decisions

- **Claude Code skill (markdown), not Python module:** The research landscape skill is a Claude Code skill that orchestrates discovery conversationally. It uses web search (WebSearch/WebFetch tools) and Claude's training knowledge to discover the landscape. No Python programmatic component is needed for this skill -- it produces a markdown output directly.
- **No external API calls needed:** Unlike KB build (Epic 7), this skill does not need Semantic Scholar or ArXiv API connectors. It uses Claude's built-in web search to find open problems lists, research agendas, and key sources. The connectors are for Track B (KB construction).
- **Output consumed by `/generate-ideas`:** The landscape summary serves as input context for the generation skill (Epic 3). The output format must be parseable -- use clear markdown sections with consistent heading structure so the generation skill can extract subfields and open problems programmatically.
- **Existing taxonomy as starting point:** The 800-paper shallow review from arb-consulting/shallow-review-2025 includes a `taxonomy.yaml` with 7 AI Safety categories (Black-box Safety, Interpretability, Safety by Construction, Make AI Solve It, Theory, Multi-agent & Evals, Labs). The landscape skill should discover whether these categories are comprehensive or if additional subfields should be added. [Source: docs/architecture.md#KB Bootstrap]
- **Source priority awareness:** The skill should identify Priority 1 sources (open problems lists) as the most actionable for idea generation. [Source: docs/architecture.md#Source Priority System]

### Implementation Approach

1. Create `.claude/commands/research-landscape.md` skill file
2. The skill should:
   - Start by loading any existing config (team profiles, criteria) for context on what the coordinator cares about
   - Use web search to find current AI Safety open problems lists (e.g., from ARC, MIRI, Anthropic, DeepMind, OpenAI safety teams, CAIS, Redwood Research, etc.)
   - Use web search to find recent AI Safety research agendas and survey papers
   - Synthesize findings with Claude's training knowledge of the field
   - Produce a structured markdown output covering all subfields, open problems, key sources
   - Present the landscape to the coordinator for review and subfield selection
   - Save the output to `data/output/research-landscape.md`
3. Ensure `data/output/` directory exists (should already exist from Story 1.1)

### File Structure

```
.claude/commands/
  research-landscape.md     # Claude Code skill (NEW - this story)
data/output/
  research-landscape.md     # Skill output (generated at runtime)
```

### What NOT to Build

- No Python module needed -- this is a pure Claude Code skill
- No KB connectors (Semantic Scholar, ArXiv API) -- those are Epic 7 / Track B
- No PDF parsing or document ingestion -- that is Epic 7
- No scoring or evaluation -- that is Epic 4
- Do not create any new Pydantic schemas -- config schemas from Epic 1 are sufficient

### NFRs Addressed

- **NFR1-NFR3 (Cost Efficiency):** Skill uses Claude's native knowledge + web search only -- no external LLM API costs
- **NFR11 (Maintainability):** Skill is a standalone markdown file, independently modifiable
- **NFR12 (Externalized Config):** Skill reads config from YAML files via the existing config loader pattern

## Dependencies

- **Story 1.1:** Requires project structure, `data/output/` directory, config schemas and loader
- **Story 1.2:** Benefits from team profiles and criteria config (to understand what the coordinator cares about), but not strictly required

## Tasks / Subtasks

- [ ] Create `.claude/commands/research-landscape.md` skill (AC: #1, #2, #3)
  - [ ] Implement web search discovery for open problems lists and research agendas
  - [ ] Implement subfield mapping with open problems per subfield
  - [ ] Implement key organizations and authors identification
  - [ ] Implement structured markdown output to `data/output/`
  - [ ] Implement coordinator review and subfield selection flow
- [ ] Verify `data/output/` directory exists from Story 1.1 setup
- [ ] Test skill produces valid, structured markdown output (AC: #2)
- [ ] Test output is consumable by future `/generate-ideas` skill (AC: #4)

## Test Strategy

- Manual test: invoke `/research-landscape` and verify it produces structured output in `data/output/research-landscape.md`
- Verify output contains all required sections (subfields, open problems, organizations, authors, sources)
- Verify output format is consistent and parseable for downstream consumption
- Verify skill handles web search failures gracefully (falls back to Claude's training knowledge)
- No unit tests needed -- this is a pure Claude Code skill with no Python components

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used
Claude Opus 4.6 (1M context)

### Debug Log References
N/A - pure Claude Code skill, no Python components to debug

### Completion Notes List
- Created `.claude/commands/research-landscape.md` skill file
- Skill implements 4-phase workflow: Discover, Synthesize, Generate Output, Coordinator Review
- Uses WebSearch/WebFetch tools with graceful fallback to Claude knowledge
- Output format uses parseable markdown with consistent heading structure for `/generate-ideas` consumption
- Coordinator Selection section uses checkboxes for subfield targeting
- Open problems include source traceability via HTML comments
- Starts from 7-category shallow review taxonomy, expandable based on discoveries

### File List
- `.claude/commands/research-landscape.md` (NEW) - Claude Code skill for landscape discovery
- `docs/sprint_status.yaml` (MODIFIED) - story-2.1 status updated to dev_complete
- `docs/stories/story-2.1.md` (MODIFIED) - status updated to dev_complete
