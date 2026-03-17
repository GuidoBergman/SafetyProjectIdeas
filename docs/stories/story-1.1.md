# Story 1.1: Project Initialization, Config Schemas & Default Configuration

## Story Info

- **Epic:** Epic 1 - Project Foundation & Team Configuration
- **Story ID:** story-1.1
- **Status:** review_complete
- **Created:** 2026-03-16
- **FRs Covered:** FR52, FR53, FR55, FR56, FR57, FR66 (partial)

## User Story

As a coordinator,
I want the project set up with proper structure, validated configuration schemas, and sensible defaults for BAISH's teams,
So that the system is ready for idea generation from day one.

## Acceptance Criteria

### AC1: Project Structure Initialization

**Given** no project structure exists
**When** the developer initializes the project
**Then** the following structure is created:
- `src/safety_ideas/` Python package with subpackages: `config/`, `kb/`, `connectors/`, `pipeline/`, `verification/`
- `data/kb/`, `data/output/`, `data/runs/`, `data/ideas/` directories
- `config/` directory with `participants/` subdirectory
- `tests/` directory mirroring `src/` structure
- `.claude/commands/` directory for Claude Code skills

**And** `pyproject.toml` is configured with dependencies (`pytest`, `ruff`, `pyyaml`, `pydantic`, `python-dotenv`), ruff config, and project metadata
**And** `.env.example` documents required environment variables
**And** `.gitignore` excludes `.env`, `__pycache__/`, `.venv/`, `data/runs/`
**And** `src/safety_ideas/constants.py` and `src/safety_ideas/utils.py` exist
**And** `README.md` exists with project overview and setup instructions
**And** `LICENSE` exists with MIT license
**And** `uv sync` succeeds without errors

### AC2: Pydantic Config Schemas

**Given** the project structure exists
**When** Pydantic models are defined in `src/safety_ideas/config/schemas.py`
**Then** the following models exist: `TeamProfile`, `ScoringCriteria`, `KBCriteria`, `PipelineSettings`, `ParticipantProfile`
**And** `TeamProfile` includes: team name, type (mentor_novice / solo_novice / experienced_group), compute_budget, technical_skills, custom criteria weights
**And** `ScoringCriteria` includes: criteria name, description, default weight, per-team-type weight overrides
**And** `PipelineSettings` includes: model assignments per stage, threshold settings per filter stage
**And** `ParticipantProfile` includes: name, experience_level, technical_background, compute_resources, time_availability
**And** `KBCriteria` includes: subfields_in_scope, organizations, authors, exclusions

### AC3: Config Loader with Validation

**Given** Pydantic models are defined
**When** `load_config()` is called from `src/safety_ideas/config/loader.py`
**Then** it loads and validates all YAML files from `config/` directory
**And** returns validated Pydantic model instances
**And** raises clear error messages if YAML is malformed or missing required fields
**And** loads `.env` via python-dotenv for API keys

### AC4: Default Configuration Files

**Given** no config files exist yet
**When** the developer creates default config files
**Then** `config/teams.yaml` contains BAISH's three team profiles (mentor_novice, solo_novice, experienced_group)
**And** `config/criteria.yaml` contains the five default scoring criteria (soundness, relevance, theory_of_impact, low_compute, accessible_complexity) with default weights and per-team-type overrides
**And** `config/pipeline.yaml` contains default model assignments and threshold settings
**And** `config/kb-criteria.yaml` contains default inclusion criteria for AI Safety subfields
**And** all config files are human-readable and editable YAML

## Technical Notes

### Architecture References

- Python 3.11+ with `uv init`, dependencies: pytest, ruff, pyyaml, pydantic, python-dotenv
- Claude Code skills (markdown) for pipeline orchestration; Python for programmatic components
- Skills invoke Python via `uv run python -m safety_ideas.<module>`
- All config access through Pydantic models -- never raw YAML parsing in pipeline code
- `.env` + python-dotenv for API keys (Semantic Scholar, etc.)
- `.env` added to `.gitignore`
- No secrets in YAML config or pipeline output
- Local-only for MVP -- runs entirely on local machine via Claude Code
- Git + GitHub for backup and version control
- No cloud compute, no CI/CD, no containers

### Key Design Decisions

- **Config validation via Pydantic:** All configuration is accessed through Pydantic models. No raw YAML dict access in pipeline code. This ensures type safety and clear error messages.
- **YAML as source of truth:** Config files are human-editable YAML (FR56). Pydantic validates on load, but the YAML files are the canonical source.
- **Three team types:** mentor_novice, solo_novice, experienced_group -- these map to BAISH's actual team configurations.
- **Five default scoring criteria:** soundness, relevance, theory_of_impact, low_compute, accessible_complexity -- with per-team-type weight overrides (e.g., experienced_group removes low_compute, doubles theory_of_impact).

### File Structure

```
project-root/
  src/safety_ideas/
    __init__.py
    constants.py
    utils.py
    config/
      __init__.py
      schemas.py        # Pydantic models
      loader.py          # load_config() function
    kb/
      __init__.py
    connectors/
      __init__.py
    pipeline/
      __init__.py
    verification/
      __init__.py
  config/
    teams.yaml
    criteria.yaml
    pipeline.yaml
    kb-criteria.yaml
    participants/
  data/
    kb/
    output/
    runs/
    ideas/
  tests/
    config/
    kb/
    connectors/
    pipeline/
    verification/
  .claude/commands/
  .env.example
  .gitignore
  pyproject.toml
  README.md
  LICENSE
```

### NFRs Addressed

- **NFR11:** Modular package structure supports independent stage development
- **NFR12:** All configurable parameters externalized in YAML
- **NFR13:** Config schemas define the interfaces for pipeline stage communication
- **NFR14:** .env for secrets, .gitignore excludes .env

## Dependencies

- None (this is the first story -- prerequisite for all others)

## Test Strategy

- Unit tests for each Pydantic schema (valid data, invalid data, edge cases)
- Unit tests for `load_config()` with valid YAML, malformed YAML, missing required fields
- Integration test: `uv sync` succeeds
- Integration test: load default config files and validate against schemas
- Verify `.env.example` documents all required environment variables
- Verify `.gitignore` contains required exclusions

## Story Validation Checklist

- [ ] All acceptance criteria have clear Given/When/Then format
- [ ] Each AC is independently testable
- [ ] Technical notes reference architecture decisions
- [ ] Dependencies are identified (none for this story)
- [ ] NFRs addressed are listed
- [ ] Story is implementable in a single sprint
- [ ] No ambiguous requirements -- all file paths, model fields, and config structures are specified
