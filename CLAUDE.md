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
- `data/output/idea_tracker.md` — Master tracker for all ranked ideas. Each idea has a status column tracking its review state: "Not reviewed" (default), "Not promising", "Removed", "Evaluating", "Added and needs manual review", "Added". The evaluate-idea skill updates this status as ideas move through the evaluation workflow.
- `.claude/commands/` — Claude Code skills: generate-ideas, score-ideas, configure-teams, research-landscape

## Conventions

- Python 3.11+, managed with `uv` (never use `pip`)
- Pydantic v2 for all schemas
- Ruff for linting and formatting (line-length 100)
- Tests mirror `src/` structure under `tests/`
- Config is YAML-based, loaded via `config/loader.py`
- Team types and scoring criteria are configured in `config/teams.yaml` and `config/criteria.yaml`
- Every new function MUST have a test
- **Idea IDs** come from one place only: `saim.ids.new_idea_id()` (CLI: `uv run python -m saim.ids [count]`), which returns a short UUID like `gen-3f9a1c04`. Never mint an ID by hand, from a title slug, or from a per-run counter — sequential IDs collide when ideas are generated in separate batches or runs and overwrite each other in `data/ideas/`. Legacy IDs (`gen-001`, `gen-0017`) stay valid on disk but must not be created again.
- Whenever an LLM is asked to produce a numeric score, there must be a rubric defining what each number means
- Estimated novelty (`novelty_method: "novelty_estimated"`) is unreliable — it is an LLM guess without literature search. Ideas must not be saved/persisted with only estimated novelty; a real novelty check (web search + citation verification) must run first.
- **Source credibility:** When a paper or post is proposed as a basis for an idea, assess its credibility before building on it. Three dimensions matter:
  1. **Publication venue** — Peer-reviewed venues (NeurIPS, ICML, AAAI, JAIR, etc.) are most credible. Preprints (arXiv) are acceptable when backed by credible authors. Blog posts and informal publications (e.g., Alignment Forum) are not sufficient as a primary basis for a project idea, though they may be useful as supplementary context.
  2. **Author credibility** — Is the author affiliated with a known research institution or lab? Do they have a meaningful publication track record? Indicators: h-index, total citation count, number of publications in relevant venues. An arXiv paper from an established researcher (e.g., h-index > 10, affiliated with a recognized lab) is trustworthy; one from an unknown author with no track record is not.
  3. **Citation signals** — How many citations does the paper have, and by whom? Well-cited papers (especially by established researchers) are more credible. Recent papers may lack citations, so weigh venue and author more heavily in that case.
  LessWrong and Alignment Forum posts from credible authors (established researchers, known AI safety contributors) are sufficient as a primary basis, especially when highly upvoted. Posts from unknown authors on these platforms are not.
  An idea should not be built primarily on sources that lack credibility across these dimensions. Flag low-credibility sources and prefer ideas grounded in peer-reviewed or well-established work.

## Branch: tais_04_2026 — Facilitator mode

On this branch the repo is used to **track the progress of a cohort of participant research projects**, evaluate participant ideas, and suggest next steps. It is not used to run the main SAIM idea generation pipeline on this branch — the pipeline skills are still available but out-of-scope for day-to-day work here.

The facilitator-mode workflow has three pieces:

- **Participant profiles** — `config/participants/*.yaml`. Background, skills, compute budget, hours/week, goals, deliverables. The `<key>` (filename without extension) is the stable identifier used everywhere else.
- **Research log allowlist** — `.participant-logs-allowlist` at the repo root. One `<participant_key>  <google-doc-url>` per line, mapping each participant to their Google Doc research log. This file is committed so the cohort is shared.
- **Shared idea list** — `.gdoc-allowlist` points at a Google Doc that contains the numbered catalogue of ideas participants draw from. When a research log references an idea by number (e.g. "working on idea #17", "idea 23 looks promising"), resolve the number against that doc before interpreting the entry — the participant is pointing at a specific proposal, not a line in `data/output/idea_tracker.md`.
- **Tracker outputs** under `data/output/participant_updates/`:
  - `log.md` — cumulative per-participant update log, newest first. Never rewritten, only appended to.
  - `review_queue.md` — ephemeral list of items the facilitator still needs to look at. **The facilitator deletes items from this file as they are handled** — the skill never removes anything.

To refresh both files, run the project-local skill `/refresh-participant-logs` (`.claude/commands/refresh-participant-logs.md`). It reads the allowlist, calls the `gdoc` CLI in read-only mode (relying on gdoc's built-in awareness system for change detection — do not roll your own snapshotting), and merges new entries into the two tracker files.

Participant ideas that graduate to formal evaluation still flow through `data/output/idea_tracker.md` and the existing status vocabulary (`Not reviewed`, `Evaluating`, `Added and needs manual review`, `Added`, `Not promising`, `Removed`) via the `/evaluate-idea` skill — that side of the workflow is unchanged on this branch.
