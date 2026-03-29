# CLAUDE.md

## Project Overview

SAIM (Safety Idea Machine) is an AI Safety Research Idea Generation Pipeline for BAISH (Buenos Aires AI Safety Hub). It uses Claude Code skills to generate, score, and filter AI safety research project ideas tailored to different team configurations and participant profiles.

## Commands

- **Install dependencies:** `uv sync`
- **Run tests:** `uv run python -m pytest`
- **Lint:** `uv run ruff check src/ tests/ scripts/`
- **Format:** `uv run ruff format src/ tests/ scripts/`

## Architecture

- `src/saim/pipeline/` — Pipeline stages are defined in `constants.py:STAGE_NAMES`. Stage modules: `generate.py`, `filter_score.py`. Helpers: `novelty.py` (novelty scoring), `memory.py` (previous idea dedup). `orchestrator.py` handles run directory creation and metadata.
- `src/saim/config/` — Config loading, CLI, Pydantic schemas, participant profiles
- `src/saim/verification/` — Citation lookup tools (CrossRef DOI/title search, Semantic Scholar title search) that return metadata for LLM-driven verification decisions
- `src/saim/connectors/` — Source connectors for KB ingestion (placeholder)
- `src/saim/kb/` — Knowledge base management (placeholder)
- `config/` — YAML config files (teams, criteria, pipeline settings, KB criteria, participants/)
- `data/` — Pipeline outputs: `ideas/`, `kb/`, `output/`, `runs/`
- `.claude/commands/` — Claude Code skills: generate-ideas, score-ideas, configure-teams, research-landscape

## Conventions

- Python 3.11+, managed with `uv` (never use `pip`)
- Pydantic v2 for all schemas
- Ruff for linting and formatting (line-length 100)
- Tests mirror `src/` structure under `tests/`
- Config is YAML-based, loaded via `config/loader.py`
- Team types and scoring criteria are configured in `config/teams.yaml` and `config/criteria.yaml`
- Every new function MUST have a test
- Whenever an LLM is asked to produce a numeric score, there must be a rubric defining what each number means
