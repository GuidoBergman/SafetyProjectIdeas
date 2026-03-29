# Story 5.1: Refinement, Proposal Assembly, Ranking & Persistent Idea Storage

## Story Info

- **Epic:** Epic 5 - Idea Refinement, Proposal Assembly & Ranked Output
- **Story ID:** story-5.1
- **Status:** done
- **Created:** 2026-03-20
- **FRs Covered:** FR36, FR37, FR38, FR39, FR40, FR41, FR42, FR64

## User Story

As a coordinator,
I want promising ideas auto-strengthened and assembled into full proposals, then re-scored and ranked so I can scan them efficiently and they accumulate across runs,
So that I get actionable research project proposals ranked on complete information and build a growing library of ideas over time.

## Acceptance Criteria

### AC1: Auto-Strengthen Ideas with Weak Scores

**Given** scored ideas exist from Epic 4 in `data/runs/<timestamp>/filter_score/`
**When** the coordinator invokes `/refine-ideas`
**Then** the system identifies ideas with weak scores (lowest-scoring dimensions)
**And** auto-strengthens them by improving the weakest dimensions (FR36)
**And** reports confidence that refinement improved each idea

### AC2: Alternative Framings for Promising Ideas

**Given** scored ideas are being refined
**When** the refine stage processes promising ideas
**Then** it generates 2-3 alternative framings for each promising idea (FR37)
**And** each framing represents a different angle on the same core insight

### AC3: Full Proposal Assembly

**Given** ideas have been refined
**When** the refine stage assembles proposals
**Then** each surviving idea becomes a full proposal including: research question, approach outline, proposed first experiments, theory of impact chain, strength rationale, and cited sources with verifiable links/DOIs (FR38, FR40)
**And** outputs full proposals as markdown files in `data/runs/<timestamp>/refine/`

### AC4: Re-Score and Rank Full Proposals

**Given** full proposals exist from the Refine stage
**When** the coordinator invokes `/rank-ideas`
**Then** the system re-scores full proposals against criteria — now with richer signal from complete proposals (first experiments, impact chain) — and produces a ranked list sorted by overall score as a markdown file (FR39)
**And** proposals are concise enough for a human to scan 20+ in a sitting (FR41)
**And** the provenance of each idea is preserved — which KB sources contributed, which generation method produced it (FR42)
**And** ranked output is written to `data/runs/<timestamp>/rank/` and copied to `data/output/`

### AC5: Persistent Idea Storage

**Given** a ranking run completes
**When** final proposals are produced
**Then** they are also copied to `data/ideas/` for persistent accumulation across pipeline runs (FR64)
**And** subsequent generation runs can reference `data/ideas/` to avoid repeating previously generated ideas

## Tasks / Subtasks

- [x] Create `src/saim/pipeline/refine.py` (AC: #1, #2, #3)
  - [x] `identify_weak_dimensions(scored_idea: dict, criteria: list) -> list[str]` — find lowest-scoring criteria
  - [x] `build_refinement_context(scored_idea: dict, weak_dims: list[str]) -> dict` — prepare context for LLM refinement
  - [x] `build_proposal_skeleton(scored_idea: dict, refinement: dict) -> dict` — structure the full proposal
  - [x] `write_refined_proposal(run_dir: Path, proposal: dict) -> Path` — write proposal as markdown file to refine/
  - [x] `read_refined_proposals(run_dir: Path) -> list[dict]` — read all proposals from refine/
  - [x] CLI entry point for skill invocation (`main()`)
- [x] Create `src/saim/pipeline/rank.py` (AC: #4, #5)
  - [x] `rank_proposals(proposals: list[dict], criteria: list, team_profile: TeamProfile) -> list[dict]` — re-score and sort by overall weighted score
  - [x] `format_ranked_output(ranked: list[dict]) -> str` — generate concise markdown for 20+ proposals
  - [x] `persist_ideas(ranked: list[dict], ideas_dir: Path) -> list[Path]` — copy final proposals to data/ideas/
  - [x] `write_ranked_output(run_dir: Path, ranked: list[dict], markdown: str) -> Path` — write ranked output to rank/
  - [x] CLI entry point for skill invocation (`main()`)
- [x] Create `.claude/commands/refine-ideas.md` skill (AC: #1, #2, #3)
  - [x] Accept run directory path (or find latest)
  - [x] Load scored ideas from filter_score/ stage
  - [x] Identify weak dimensions and auto-strengthen via LLM
  - [x] Generate alternative framings for promising ideas
  - [x] Assemble full proposals (research question, approach, experiments, impact chain, citations)
  - [x] Write proposals to refine/
  - [x] Log all decisions via PipelineLogger
  - [x] Present refinement summary for coordinator review
- [x] Create `.claude/commands/rank-ideas.md` skill (AC: #4, #5)
  - [x] Accept run directory path (or find latest)
  - [x] Load proposals from refine/ stage
  - [x] Re-score full proposals against criteria with LLM
  - [x] Produce ranked markdown sorted by overall score
  - [x] Copy output to data/output/ and data/ideas/
  - [x] Log via PipelineLogger
  - [x] Present ranked results summary
- [x] Create `tests/pipeline/test_refine.py` (AC: #1, #2, #3)
- [x] Create `tests/pipeline/test_rank.py` (AC: #4, #5)

## Dev Notes

### Architecture References

- **Skill locations:** `.claude/commands/refine-ideas.md`, `.claude/commands/rank-ideas.md` [Source: docs/architecture.md#Project Structure]
- **Python modules:** `src/saim/pipeline/refine.py`, `src/saim/pipeline/rank.py` [Source: docs/architecture.md#Project Structure]
- **Skills invoke Python via:** `uv run python -m saim.pipeline.<module>` [Source: docs/architecture.md#Skill Patterns]
- **Refine output:** Markdown files in `data/runs/<timestamp>/refine/` [Source: docs/architecture.md#Data Architecture]
- **Rank output:** Markdown + JSON in `data/runs/<timestamp>/rank/`, copied to `data/output/` and `data/ideas/`
- **Track A, steps 5-6:** After filter_score, final pipeline stages

### Key Design Decisions

1. **Hybrid skill + Python architecture (same pattern as stories 3.1, 4.1):**
   - `.claude/commands/refine-ideas.md` — Claude Code skill that orchestrates refinement conversationally, uses LLM for auto-strengthening, alternative framings, and proposal assembly
   - `.claude/commands/rank-ideas.md` — Claude Code skill that re-scores full proposals via LLM, produces ranked markdown output
   - `src/saim/pipeline/refine.py` — Python module for refine I/O, weak dimension identification, proposal skeleton building
   - `src/saim/pipeline/rank.py` — Python module for ranking, persistence, output formatting

2. **Refined proposal markdown format (output of refine stage):**
   Each file in `refine/<idea_id>.md` with YAML frontmatter:
   ```yaml
   ---
   idea_id: gen-001
   run_id: "2026-03-19T14-30-00"
   stage: refine
   timestamp: "2026-03-20T10:00:00Z"
   original_scores:
     theory_of_impact: 4
     low_compute: 3
     accessible_complexity: 4
     narrow_scope: 5
   novelty_classification: mostly_novel
   novelty_score: 4
   pre_refine_weighted_score: 3.85
   weak_dimensions_addressed: ["low_compute"]
   num_alternative_framings: 2
   generation_strategy: novel_directions
   subfield: interpretability
   provenance:
     generation_method: novel_directions
     kb_sources: []
     web_sources: ["arxiv:2401.xxxxx"]
   refinement_confidence: 0.8
   ---
   # Research Question
   ...
   # Approach Outline
   ...
   # Proposed First Experiments
   ...
   # Theory of Impact Chain
   ...
   # Strength Rationale
   ...
   # Alternative Framings
   ## Framing 1: ...
   ## Framing 2: ...
   # Cited Sources
   - [Paper Title](doi/url) — relevance note
   ```

3. **Ranked output format:**
   - `rank/ranked_proposals.md` — Human-scannable ranked list with one section per proposal
   - `rank/ranked_proposals.json` — Machine-readable ranked list with re-scored data
   - Each proposal in the ranked list is concise: title, research question, approach summary, scores, rank position
   - Provenance preserved: generation method, KB sources, web sources per idea

4. **Persistent idea storage:**
   - Each final ranked proposal copied to `data/ideas/<idea_id>.md`
   - Uses the same markdown format as refine/ output (full proposal)
   - `memory.py:load_previous_ideas()` reads H1 titles from these files for dedup in future generation runs

### Existing Code to Use (DO NOT Reinvent)

- `saim.pipeline.filter_score.read_scored_ideas(run_dir)` — Load scored ideas from Epic 4
- `saim.pipeline.filter_score.apply_weights(scores, criteria, team_profile)` — Recompute weighted scores
- `saim.config.loader.load_config()` — Load all config (teams, criteria, pipeline settings)
- `saim.config.schemas` — `TeamProfile`, `ScoringCriteria`, `StageThreshold`, `PipelineSettings`
- `saim.constants` — All path constants (`RUNS_DIR`, `IDEAS_DIR`, `OUTPUT_DIR`, `SCORING_CRITERIA`)
- `saim.pipeline.orchestrator.PipelineLogger` — Structured JSON logging
- `saim.pipeline.orchestrator.write_run_meta(run_dir, params)` — Update run metadata
- `saim.pipeline.memory.load_previous_ideas()` — Load previous idea titles (for dedup verification)
- `saim.pipeline.novelty` — Novelty classification constants, score derivation
- `saim.utils.load_yaml()` — YAML loading

### What NOT to Build

- No KB query module — that is Epic 7 (but preserve provenance field for future KB integration)
- No actual LLM calls in Python — the skills handle LLM interactions via Claude's tools
- No new Pydantic schemas for proposals — use plain dicts + markdown/JSON for now
- No re-running novelty assessment — preserve novelty from filter_score stage, don't re-assess
- No web searching in rank stage — re-scoring uses the richer signal from the assembled proposal text, not new web searches

### NFRs Addressed

- **NFR1-NFR3 (Cost Efficiency):** Re-scoring in rank uses existing novelty data, no redundant web search; proposal assembly happens only for survivors
- **NFR7 (Auditability):** Every re-score has explicit reasoning; all refinement decisions logged
- **NFR11 (Modularity):** Refine and rank are independent stages, invokable separately
- **NFR12 (Configuration):** Weights, thresholds externalized in YAML

## Dependencies

- **Story 1.1:** Config schemas, loader, project structure (DONE)
- **Story 1.2:** Participant profiles for team-specific scoring (DONE)
- **Story 3.1:** Pipeline orchestrator, generate stage, PipelineLogger (DONE)
- **Story 4.1:** filter_score module — `read_scored_ideas()`, `apply_weights()`, novelty module (DONE)

## Test Strategy

- **Unit tests** for Python modules:
  - `test_refine.py`: weak dimension identification, proposal skeleton building, markdown write/read round-trip, build_refinement_context
  - `test_rank.py`: ranking by score, format_ranked_output, persist_ideas, write_ranked_output
- **Manual test** for Claude Code skills:
  - Invoke `/refine-ideas` on existing scored run
  - Verify proposals appear in `data/runs/<timestamp>/refine/`
  - Invoke `/rank-ideas` on refined run
  - Verify ranked output in `data/runs/<timestamp>/rank/`, `data/output/`, `data/ideas/`
- Run all tests with: `uv run pytest tests/pipeline/test_refine.py tests/pipeline/test_rank.py -v`

## Dev Agent Record

### Context Reference

### Agent Model Used
Claude Opus 4.6 (1M context)

### Debug Log References
N/A

### Completion Notes List
- All 273 tests pass (16 refine + 17 rank + 240 existing)
- Ruff lint clean on all new files
- Removed unused pytest import from test_refine.py
- Review fixed 5 issues: rank CLI reading *.json instead of *.md (H1), format_ranked_output showing original_scores instead of re-scored scores (H2), refine skill CLI arg mismatch for identify-weak/build-context (M1), rank_proposals mutating input (M2), persist_ideas heading level inconsistency (M3)
- Added 2 new tests: test_does_not_mutate_input, test_displays_rescored_scores_when_available

### File List
- `src/saim/pipeline/refine.py` — refinement logic: weak dimension identification, context building, proposal skeleton, markdown I/O, CLI
- `src/saim/pipeline/rank.py` — ranking logic: proposal scoring, output formatting, idea persistence, CLI
- `.claude/commands/refine-ideas.md` — Claude Code skill for refine stage orchestration
- `.claude/commands/rank-ideas.md` — Claude Code skill for rank stage orchestration
- `tests/pipeline/test_refine.py` — 16 tests for refine module
- `tests/pipeline/test_rank.py` — 15 tests for rank module
