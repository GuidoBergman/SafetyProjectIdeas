# Story 3.1: Idea Generation Skill & Pipeline Stage Infrastructure

## Story Info

- **Epic:** Epic 3 - Idea Generation
- **Story ID:** story-3.1
- **Status:** done
- **Created:** 2026-03-19
- **FRs Covered:** FR18, FR20, FR21, FR22, FR25, FR26, FR27, FR67, FR68

## User Story

As a coordinator,
I want to auto-generate a batch of research idea sketches covering all my specified subfields heavily,
So that I get thorough coverage of candidate project ideas across every area I care about.

## Acceptance Criteria

### AC1: Pipeline Run Directory & Metadata

**Given** the project config exists (team profiles, scoring criteria)
**When** the coordinator invokes `/generate-ideas`
**Then** the system creates a pipeline run directory at `data/runs/<timestamp>/` with `run_meta.json` capturing:
- `run_id` (timestamp-based, format `YYYY-MM-DDTHH-MM-SS`)
- `timestamp` (ISO 8601)
- `git_commit` (current HEAD short hash)
- `parameters` (team_profile used, subfields targeted, stages run)
- Config snapshot (criteria weights, pipeline settings used)

### AC2: Independent Stage Invocation

**Given** pipeline infrastructure exists
**When** the coordinator invokes `/generate-ideas`
**Then** the generation stage can be invoked independently (FR18)
**And** each other pipeline stage (`/score-ideas`, `/refine-ideas`, `/rank-ideas`) can also be invoked independently when they exist
**And** stages read from previous stage output directories and write to their own

### AC3: Idea Sketch Generation

**Given** the coordinator specifies subfields to target (or all subfields from research-landscape.md are used)
**When** idea generation runs
**Then** it generates idea sketches as brief descriptions: problem + direction + why it matters (FR25)
**And** covers all specified subfields heavily
**And** uses generation strategies: novel directions, variations of existing experiments (FR67), follow-up experiments to explain observed effects (FR68)
**And** feeds only relevant context (abstracts, limitations) to generation — never full papers (FR26)
**And** each idea sketch is written as a markdown file in `data/runs/<timestamp>/generate/`
**And** confidence is reported on each generated idea

### AC4: Model Tiering

**Given** pipeline settings define model assignments per stage
**When** idea generation runs
**Then** the system uses cheaper models for simple generation tasks and more capable models for deeper analysis (FR27)
**And** model assignments are read from `config/pipeline.yaml`

### AC5: Structured Logging

**Given** a generation run is executing
**When** each stage processes ideas
**Then** the system logs inputs, decisions, and outputs in structured JSON format (FR22)
**And** logs are written to `data/runs/<timestamp>/pipeline.log.json`
**And** each log entry includes `timestamp`, `run_id`, `stage`, `level`, `message`, `data`

### AC6: Output Inspection & Intervention

**Given** a generation run has completed
**When** the coordinator inspects the output
**Then** they can review individual idea sketches before proceeding to scoring (FR20)
**And** they can intervene to add, remove, or redirect ideas (FR21)

### AC7: Graceful KB Degradation

**Given** the KB is not yet populated
**When** idea generation runs
**Then** the system functions using Claude's native AI Safety knowledge + active web search

**Given** the KB has been populated (Epic 7)
**When** idea generation runs
**Then** the system queries the KB via the query module for relevant context to enrich generation

## Technical Notes

### Architecture References

- **Skill location:** `.claude/commands/generate-ideas.md` [Source: docs/architecture.md#Project Structure]
- **Python modules:** `src/saim/pipeline/orchestrator.py`, `src/saim/pipeline/generate.py`, `src/saim/pipeline/memory.py` [Source: docs/architecture.md#Project Structure]
- **Skills invoke Python via:** `uv run python -m saim.pipeline.<module>` [Source: docs/architecture.md#Skill Patterns]
- **Run directory:** `data/runs/<timestamp>/` with per-stage subdirectories [Source: docs/architecture.md#Pipeline Run State]
- **Track A, step 3:** After research-landscape, before score-ideas [Source: docs/architecture.md#Decision Impact Analysis]

### Key Design Decisions

1. **Hybrid skill + Python architecture:**
   - `.claude/commands/generate-ideas.md` — Claude Code skill that orchestrates generation conversationally, uses web search, generates ideas via LLM prompting
   - `src/saim/pipeline/orchestrator.py` — Python module for run directory setup, metadata writing, log management
   - `src/saim/pipeline/generate.py` — Python module for idea file I/O, structured output
   - `src/saim/pipeline/memory.py` — Loads past idea titles from `data/ideas/` to avoid repetition

2. **Idea sketch format (markdown with YAML frontmatter):**
   ```markdown
   ---
   idea_id: "gen-001"
   run_id: "2026-03-19T14-30-00"
   stage: "generate"
   timestamp: "2026-03-19T14:30:00Z"
   subfield: "mechanistic_interpretability"
   generation_strategy: "novel_direction"  # novel_direction | experiment_variation | follow_up_experiment
   confidence: 0.7
   ---

   # [Idea Title]

   **Problem:** [What problem this addresses]

   **Direction:** [Proposed approach/direction]

   **Why it matters:** [Theory of impact for AI Safety]

   **Relevant context:** [Brief pointers to relevant work — abstracts/limitations only, never full papers]
   ```

3. **Run directory structure:**
   ```
   data/runs/2026-03-19T14-30-00/
   ├── run_meta.json
   ├── generate/
   │   ├── gen-001.md
   │   ├── gen-002.md
   │   └── ...
   └── pipeline.log.json
   ```

4. **Integration with research-landscape.md:**
   - Skill parses `data/output/research-landscape.md` `## Coordinator Selection` section
   - Subfields marked `[x]` are targeted; if none marked, all subfields used ordered by priority
   - Open problems, generation strategy hints, and recent surprising results from landscape file feed generation
   - If no landscape file exists, skill asks coordinator for subfields or uses all default categories

5. **Pipeline memory (dedup):**
   - `pipeline/memory.py` loads idea titles/summaries from `data/ideas/` directory
   - Passes them to generation as "already generated — explore different directions"
   - Simple title matching, no semantic similarity

### Existing Code to Use (DO NOT Reinvent)

- `saim.config.loader.load_config()` — Load all config (teams, criteria, pipeline settings)
- `saim.config.participants.get_default_participant()` — Get participant profile
- `saim.constants` — All path constants (`RUNS_DIR`, `IDEAS_DIR`, `OUTPUT_DIR`, `STAGE_NAMES`)
- `saim.utils.load_yaml()` — YAML loading

### Implementation Approach

**Python modules to create:**

1. **`src/saim/pipeline/orchestrator.py`** — Pipeline infrastructure:
   - `create_run_dir(stages: list[str]) -> Path` — Creates `data/runs/<timestamp>/` with subdirs
   - `write_run_meta(run_dir: Path, params: dict) -> None` — Writes `run_meta.json`
   - `PipelineLogger` class — Appends structured JSON entries to `pipeline.log.json`
   - Gets git commit via `subprocess.run(["git", "rev-parse", "--short", "HEAD"])`

2. **`src/saim/pipeline/generate.py`** — Generation I/O:
   - `write_idea_sketch(run_dir: Path, idea: dict) -> Path` — Writes idea markdown file
   - `read_idea_sketches(run_dir: Path) -> list[dict]` — Reads all idea files from generate/
   - `list_idea_files(run_dir: Path) -> list[Path]` — Lists idea files for inspection

3. **`src/saim/pipeline/memory.py`** — Dedup memory:
   - `load_previous_ideas(ideas_dir: Path) -> list[str]` — Returns titles of previously generated ideas

**Claude Code skill to create:**

4. **`.claude/commands/generate-ideas.md`** — Orchestration skill that:
   - Runs `uv run python -m saim.pipeline.orchestrator init` to create run dir
   - Loads research landscape and participant profile for context
   - Uses Claude's AI Safety knowledge + web search to generate idea sketches
   - Writes each idea via `uv run python -m saim.pipeline.generate write`
   - Logs all decisions via the pipeline logger
   - Presents results for coordinator review

### File Structure

```
src/saim/pipeline/
  orchestrator.py     # NEW — run dir setup, metadata, logging
  generate.py         # NEW — idea sketch I/O
  memory.py           # NEW — load previous idea titles for dedup
.claude/commands/
  generate-ideas.md   # NEW — Claude Code skill
tests/pipeline/
  test_orchestrator.py  # NEW — test run dir creation, metadata, logging
  test_generate.py      # NEW — test idea file I/O
  test_memory.py        # NEW — test previous idea loading
```

### What NOT to Build

- No scoring/filtering — that is Epic 4 (`/score-ideas`)
- No refinement — that is Epic 5 (`/refine-ideas`)
- No ranking — that is Epic 5 (`/rank-ideas`)
- No KB connectors or querying — that is Epic 7 (but leave hook for future KB integration)
- No multi-LLM generation — post-MVP (FR23-24 deferred)
- No LiteLLM integration — post-MVP
- Do not create new Pydantic schemas for ideas — use plain dicts + markdown frontmatter for now

### NFRs Addressed

- **NFR1-NFR3 (Cost Efficiency):** Brief sketches (not full proposals), model tiering, relevant-context-only feeding
- **NFR7 (Auditability):** Structured JSON logging of all stage inputs/decisions/outputs
- **NFR11-NFR13 (Maintainability):** Modular pipeline stages, externalized config, file-based inter-stage communication

## Dependencies

- **Story 1.1:** Config schemas, loader, project structure, `data/runs/` and `data/ideas/` directories
- **Story 1.2:** Participant profiles for tailored generation (optional — works without)
- **Story 2.1:** Research landscape output for subfield targeting (optional — works without, uses defaults)

## Tasks / Subtasks

- [x] Create `src/saim/pipeline/orchestrator.py` (AC: #1, #5)
  - [x] `create_run_dir()` function
  - [x] `write_run_meta()` function
  - [x] `PipelineLogger` class with structured JSON logging
  - [x] CLI entry point for skill invocation (`__main__` or argparse)
- [x] Create `src/saim/pipeline/generate.py` (AC: #3)
  - [x] `write_idea_sketch()` — writes idea markdown with frontmatter
  - [x] `read_idea_sketches()` — reads all ideas from a run dir
  - [x] `list_idea_files()` — lists idea files
  - [x] CLI entry point for skill invocation
- [x] Create `src/saim/pipeline/memory.py` (AC: #3)
  - [x] `load_previous_ideas()` — reads titles from `data/ideas/`
- [x] Create `.claude/commands/generate-ideas.md` skill (AC: #2, #3, #4, #6, #7)
  - [x] Parse research-landscape.md for selected subfields
  - [x] Load participant profile and config context
  - [x] Generate ideas across subfields using all three strategies
  - [x] Write ideas via Python module
  - [x] Log all decisions
  - [x] Present results for coordinator review and intervention
- [x] Create `tests/pipeline/test_orchestrator.py` (AC: #1, #5)
- [x] Create `tests/pipeline/test_generate.py` (AC: #3)
- [x] Create `tests/pipeline/test_memory.py`

## Test Strategy

- **Unit tests** for Python modules:
  - `test_orchestrator.py`: run dir creation, metadata writing, logger append
  - `test_generate.py`: idea sketch write/read round-trip, frontmatter parsing
  - `test_memory.py`: loading previous ideas, empty dir handling
- **Manual test** for Claude Code skill:
  - Invoke `/generate-ideas` and verify it produces idea sketches in `data/runs/<timestamp>/generate/`
  - Verify `run_meta.json` contains git commit and config snapshot
  - Verify `pipeline.log.json` has structured entries
  - Verify ideas cover specified subfields
- Run all tests with: `uv run pytest tests/pipeline/ -v`

## Dev Agent Record

### Context Reference

### Agent Model Used
Claude Opus 4.6 (1M context)

### Debug Log References
N/A

### Completion Notes List
- Created `src/saim/pipeline/orchestrator.py` with `create_run_dir()`, `write_run_meta()`, `PipelineLogger`, and CLI entry point
- Created `src/saim/pipeline/generate.py` with `write_idea_sketch()`, `read_idea_sketches()`, `list_idea_files()`, and CLI entry point
- Created `src/saim/pipeline/memory.py` with `load_previous_ideas()` and CLI entry point
- Created `src/saim/pipeline/__main__.py` for module invocation
- Created `.claude/commands/generate-ideas.md` skill with 5-phase workflow: Setup, Load Context, Generate Ideas (parallelized via subagents), Write Ideas, Coordinator Review
- Created 16 unit tests across 3 test files — all passing
- Fixed pre-existing test assertion in `tests/config/test_loader.py` (criteria count 4→5 for novelty criterion)
- Fixed 4 ruff lint issues (timezone.utc → datetime.UTC)
- Code review fixes: added input validation to write_idea_sketch(), updated skill to use write_run_meta() with config snapshot, added CLI entry point tests
- Full test suite: 60 passed, 0 failed

### File List
- `src/saim/pipeline/orchestrator.py` (NEW)
- `src/saim/pipeline/generate.py` (NEW)
- `src/saim/pipeline/memory.py` (NEW)
- `src/saim/pipeline/__main__.py` (NEW)
- `.claude/commands/generate-ideas.md` (NEW)
- `tests/pipeline/__init__.py` (NEW)
- `tests/pipeline/test_orchestrator.py` (NEW)
- `tests/pipeline/test_generate.py` (NEW)
- `tests/pipeline/test_memory.py` (NEW)
- `tests/config/test_loader.py` (MODIFIED — fixed pre-existing criteria count assertion)
- `docs/stories/story-3.1.md` (NEW — story file)
- `docs/sprint_status.yaml` (MODIFIED — added Epic 3)
