# SAIM (Safety Idea Machine)

AI Safety Research Idea Generation Pipeline for BAISH (Beginner AI Safety Heuristics).

## Overview

SAIM (Safety Idea Machine) is a Claude Code skills-based pipeline that generates, evaluates, refines, and ranks AI Safety research project ideas tailored to different team configurations. It uses a knowledge base of AI Safety research papers and configurable scoring criteria to produce actionable research proposals.

## Setup

1. Install [uv](https://docs.astral.sh/uv/):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Clone and install dependencies:
   ```bash
   uv sync
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. Run tests:
   ```bash
   uv run python -m pytest
   ```

## Project Structure

- `src/saim/` - Python package with pipeline stages
- `config/` - YAML configuration files (teams, criteria, pipeline settings)
- `data/` - Knowledge base, pipeline outputs, and run history
- `.claude/commands/` - Claude Code skills for pipeline orchestration
- `tests/` - Test suite mirroring src/ structure

## Configuration

All configuration is managed through YAML files in `config/`:

- `teams.yaml` - Team profiles (mentor_novice, solo_novice, experienced_group)
- `criteria.yaml` - Scoring criteria with per-team-type weight overrides
- `pipeline.yaml` - Model assignments and threshold settings per stage
- `kb-criteria.yaml` - Knowledge base inclusion criteria

## License

MIT
