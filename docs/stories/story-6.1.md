# Story 6.1: Brainstorming & Idea Evaluation Skills

## Story Info

- **Epic:** Epic 6 - Collaborative Brainstorming & Idea Evaluation
- **Story ID:** story-6.1
- **Status:** done
- **Created:** 2026-03-25
- **FRs Covered:** FR43, FR44, FR45, FR46, FR47, FR48, FR49, FR50, FR51, FR66

## User Story

As a coordinator or external researcher,
I want to interactively brainstorm AI Safety research directions and evaluate existing ideas against the pipeline's criteria,
So that I can explore specific areas in depth and assess ideas I bring from outside the pipeline.

## Acceptance Criteria

### AC1: Collaborative Brainstorm Chat Mode

**Given** the project config and optionally the KB exist
**When** the coordinator invokes `/brainstorm`
**Then** the system enters collaborative chat mode for idea exploration (FR43)
**And** the coordinator can direct brainstorming by specifying topics, research areas, or specific problems (FR44)
**And** the coordinator can combine topic direction with team constraints (e.g., "interpretability ideas for a novice with one A100") (FR45)
**And** the coordinator can refine, iterate, and push back on ideas interactively (FR46)
**And** the chat has access to the KB and pipeline memory when available (FR47)
**And** the coordinator can pose open research questions and the system assesses whether they have been addressed in the literature (FR48)

### AC2: Participant Profile Integration

**Given** a participant profile exists in `config/participants/`
**When** the brainstorming or evaluation skill is invoked
**Then** the system loads the profile automatically and tailors generation to the participant's constraints (FR66)

**Given** no participant profile exists
**When** brainstorming is invoked
**Then** the system guides the user through describing their constraints conversationally

### AC3: Idea Evaluation with Novelty Assessment

**Given** the coordinator has an existing idea
**When** they invoke `/evaluate-idea`
**Then** the system evaluates the submitted idea against the configured scoring criteria (FR49)
**And** assesses novelty against published work using the same hybrid novelty assessment flow — evidence-based search, hard gate on "already solved", derived novelty score (FR50)
**And** can refine and strengthen the idea using auto-strengthen and alternative framing (FR51)

## Tasks / Subtasks

- [x] Create `.claude/commands/brainstorm-ideas.md` skill (AC: #1, #2)
  - [x] Load project config via existing CLI (`show-scoring`, `show`, `show-participant`)
  - [x] Detect and load participant profile from config/participants/ if available
  - [x] If no profile, guide user through describing constraints conversationally
  - [x] Load pipeline memory via existing `pipeline.memory` module
  - [x] Enter interactive brainstorming loop: user proposes topics/questions, system generates tailored ideas
  - [x] Support research question assessment against literature using existing citation lookup tools
  - [x] Allow iterative refinement, pushback, and deepening

- [x] Create `.claude/commands/evaluate-idea.md` skill (AC: #3)
  - [x] Accept idea submission (free-text or structured, parsed by LLM)
  - [x] Load scoring criteria and team profile via existing CLI
  - [x] Score idea against each criterion using rubrics (LLM judgment)
  - [x] Run hybrid novelty assessment using existing `pipeline.novelty` and `verification.citation` modules
  - [x] Present evaluation results with per-criterion scores and overall assessment
  - [x] Offer to auto-strengthen weak dimensions and generate alternative framings

## Dev Notes

### Architecture Patterns

- **Skills are markdown files** in `.claude/commands/` — they are executable documentation that orchestrate LLM calls, NOT Python code. They load configs, invoke Python CLI helpers via `uv run`, and present results interactively.
- **Python modules** provide mechanical helpers (data loading, formatting, parsing) — the LLM in the skill makes all judgment calls (scoring, assessment, refinement).
- **Novelty assessment** reuses existing `pipeline/novelty.py` (validate_classification, novelty_to_score, format_novelty_assessment) and `verification/citation.py` (search_crossref, search_semantic_scholar) — do NOT reinvent these.
- **Pipeline memory** reuses `pipeline/memory.py` (load_previous_ideas) — returns list of previous idea titles for divergence.
- **Config loading** uses `config/loader.py` to load YAML configs — follow existing patterns.
- **Participant profiles** are YAML files in `config/participants/` loaded via `config/loader.py` into `ParticipantProfile` Pydantic models.

### Existing Modules to Reuse (DO NOT DUPLICATE)

- `src/saim/pipeline/novelty.py` — novelty classification, scoring, formatting
- `src/saim/pipeline/memory.py` — previous idea loading
- `src/saim/verification/citation.py` — CrossRef and Semantic Scholar lookup
- `src/saim/config/loader.py` — config file loading
- `src/saim/config/schemas.py` — all Pydantic models (TeamProfile, ScoringCriteria, ParticipantProfile, etc.)
- `src/saim/constants.py` — paths (CONFIG_DIR, KB_DIR, IDEAS_DIR, etc.)

### Project Structure Notes

- New Python modules go in `src/saim/pipeline/`
- New skill files go in `.claude/commands/`
- New tests go in `tests/pipeline/`
- All Python helpers must have CLI entry points callable via `uv run python -m saim.pipeline.<module>`
- Every new function MUST have a test (CLAUDE.md mandate)

### Key Constraints

- Brainstorming is inherently interactive — the skill file must support a conversational loop, not a batch pipeline
- The evaluate-idea skill reuses the SAME novelty assessment flow as score-ideas (FR50) — evidence-based search, hard gate on "already_solved", derived score
- KB access is optional — brainstorming must work without KB (just with less context)
- When no participant profile exists, the skill must conversationally elicit constraints

### References

- [Source: docs/epics.md#Epic 6] — Epic definition and acceptance criteria
- [Source: src/saim/pipeline/novelty.py] — Novelty assessment helpers
- [Source: src/saim/pipeline/memory.py] — Previous idea loading
- [Source: src/saim/verification/citation.py] — Citation lookup tools
- [Source: src/saim/config/schemas.py] — Pydantic models
- [Source: .claude/commands/score-ideas.md] — Reference for novelty assessment flow in skills

## Dev Agent Record

### Agent Model Used

Claude Opus 4.6

### Completion Notes List

- No new Python modules needed — skills reuse existing CLI commands and modules
- Code review identified over-engineering; simplified to skill-only approach

### File List

- .claude/commands/brainstorm-ideas.md (new)
- .claude/commands/evaluate-idea.md (new)
