# Story 4.1: Scoring, Novelty & Citation Verification Skill

## Story Info

- **Epic:** Epic 4 - Idea Scoring & Hybrid Novelty Assessment
- **Story ID:** story-4.1
- **Status:** done
- **Created:** 2026-03-19
- **FRs Covered:** FR28, FR29, FR30, FR31, FR32, FR33, FR34, FR35

## User Story

As a coordinator,
I want generated ideas scored against my configured criteria with novelty assessment and verified citations,
So that I can trust the evaluations and focus review time on the most promising ideas.

## Acceptance Criteria

### AC1: Per-Criterion Scoring with Explicit Reasoning

**Given** idea sketches exist from a generation run (Epic 3) in `data/runs/<timestamp>/generate/`
**When** the coordinator invokes `/score-ideas`
**Then** the system evaluates each idea against all configured scoring criteria from `config/criteria.yaml` (FR28)
**And** scores each idea per criterion against the criterion's rubric with explicit reasoning for each score (FR30)
**And** configurable weights from criteria config and team-specific weight overrides are applied (FR28)
**And** outputs scored ideas as JSON files in `data/runs/<timestamp>/filter_score/`

### AC2: Staged Filtering with Progressive Evaluation

**Given** multiple ideas need scoring
**When** the filter/score stage runs
**Then** it applies staged filtering — progressively more expensive evaluation, killing bad ideas early (FR29)
**And** stage 1 (cheap): quick relevance/scope check eliminates obviously unfit ideas
**And** stage 2 (medium): full criterion scoring on survivors
**And** stage 3 (expensive): hybrid novelty assessment only on ideas that pass scoring threshold
**And** applies threshold settings per filter stage from `config/pipeline.yaml` to control which ideas advance (FR31)

### AC3: Hybrid Novelty Assessment

**Given** an idea is being scored and passes the initial filter stages
**When** the hybrid novelty assessment runs
**Then** the system checks the KB first if available (fast, cheap), then always searches the web — ArXiv, Semantic Scholar, Google Scholar (FR34)
**And** classifies each idea as: novel / partially addressed / already solved
**And** includes evidence for the assessment (NFR6)
**And** if classified as "already solved", the idea is eliminated immediately (hard gate) — no further scoring or refinement regardless of other criteria scores
**And** if classified as "novel" or "partially addressed", the classification is converted to a derived "novelty" score that feeds into the configurable scoring criteria
**And** the novelty score is weighted per team type (e.g., low for novice teams doing replication studies per FR67, high for experienced groups)
**And** reports confidence in the novelty assessment

### AC4: Citation Verification

**Given** an idea references papers
**When** citation verification runs
**Then** every cited paper has a verifiable link or DOI (FR32)
**And** the system actively verifies that cited papers exist and links/DOIs resolve (FR35) — using the cheapest possible method (API lookups via Semantic Scholar/CrossRef, not LLM calls) and only falling back to cheap models when programmatic verification is insufficient
**And** papers that cannot be verified are excluded from the output entirely (NFR4)
**And** factual claims trace back to specific source passages (FR33)

### AC5: Auditable Scoring Output

**Given** scoring is complete
**When** the coordinator reviews results
**Then** all scoring reasoning is explicit and auditable — no opaque scores (NFR7)
**And** confidence is reported but never used for automated filtering — human decides what to act on
**And** each scored idea JSON includes: all criterion scores with reasoning, novelty classification with evidence, citation verification results, overall weighted score, confidence

## Tasks / Subtasks

- [x] Create `src/safety_ideas/pipeline/filter_score.py` (AC: #1, #2, #5)
  - [x] `score_idea(idea: dict, criteria: list, team_profile: TeamProfile) -> dict` — scores one idea against all criteria with reasoning
  - [x] `apply_weights(scores: dict, criteria: list, team_profile: TeamProfile) -> float` — compute weighted score with team overrides
  - [x] `staged_filter(ideas: list[dict], criteria: list, thresholds: StageThreshold, team_profile: TeamProfile) -> list[dict]` — progressive filtering
  - [x] `write_scored_idea(run_dir: Path, scored: dict) -> Path` — writes scored idea JSON to filter_score/
  - [x] `read_scored_ideas(run_dir: Path) -> list[dict]` — reads all scored ideas from filter_score/
  - [x] CLI entry point for skill invocation (`main()`)
- [x] Create `src/safety_ideas/pipeline/novelty.py` (AC: #3)
  - [x] `assess_novelty(idea: dict, kb_available: bool) -> dict` — returns classification, evidence, confidence, derived score
  - [x] `classify_novelty(evidence: list[dict]) -> str` — returns "novel" / "partially_addressed" / "already_solved"
  - [x] `novelty_to_score(classification: str) -> int` — converts classification to 1-5 score
  - [x] CLI entry point
- [x] Create `src/safety_ideas/verification/citation.py` (AC: #4)
  - [x] `verify_citations(idea: dict) -> dict` — verifies all citations in an idea, returns verification results
  - [x] `verify_doi(doi: str) -> bool` — check DOI via CrossRef API
  - [x] `verify_semantic_scholar(title: str) -> dict | None` — look up paper via Semantic Scholar API
  - [x] `filter_unverified(idea: dict, verification: dict) -> dict` — removes unverified citations
  - [x] CLI entry point
- [x] Create `.claude/commands/score-ideas.md` skill (AC: #1, #2, #3, #4, #5)
  - [x] Accept run directory path (or find latest)
  - [x] Load ideas from generate/ stage
  - [x] Orchestrate staged filtering with LLM scoring
  - [x] Run hybrid novelty assessment (web search mandatory)
  - [x] Run citation verification
  - [x] Write scored ideas to filter_score/
  - [x] Log all decisions via PipelineLogger
  - [x] Present results summary for coordinator review
- [x] Create `tests/pipeline/test_filter_score.py` (AC: #1, #2, #5)
- [x] Create `tests/pipeline/test_novelty.py` (AC: #3)
- [x] Create `tests/verification/test_citation.py` (AC: #4)
- [x] Add `filter_score` thresholds to pipeline.yaml schema validation if needed

## Dev Notes

### Architecture References

- **Skill location:** `.claude/commands/score-ideas.md` [Source: docs/architecture.md#Project Structure]
- **Python modules:** `src/safety_ideas/pipeline/filter_score.py`, `src/safety_ideas/pipeline/novelty.py`, `src/safety_ideas/verification/citation.py` [Source: docs/architecture.md#Project Structure]
- **Skills invoke Python via:** `uv run python -m safety_ideas.pipeline.<module>` [Source: docs/architecture.md#Skill Patterns]
- **Filter/Score output:** JSON files in `data/runs/<timestamp>/filter_score/` [Source: docs/architecture.md#Data Architecture]
- **Track A, step 4:** After generate-ideas, before refine-ideas [Source: docs/architecture.md#Decision Impact Analysis]

### Key Design Decisions

1. **Hybrid skill + Python architecture (same pattern as story 3.1):**
   - `.claude/commands/score-ideas.md` — Claude Code skill that orchestrates scoring conversationally, uses web search for novelty assessment, applies LLM judgment for per-criterion scoring
   - `src/safety_ideas/pipeline/filter_score.py` — Python module for scoring I/O, weight computation, staged filtering logic, scored idea file management
   - `src/safety_ideas/pipeline/novelty.py` — Python module for novelty assessment data structures and classification logic
   - `src/safety_ideas/verification/citation.py` — Python module for programmatic citation verification (API calls, DOI resolution)

2. **Scored idea JSON format (output of filter_score stage):**
   ```json
   {
     "idea_id": "gen-001",
     "run_id": "2026-03-19T14-30-00",
     "stage": "filter_score",
     "timestamp": "2026-03-19T15:00:00Z",
     "title": "Idea Title",
     "original_idea": { "...": "full idea dict from generate stage" },
     "filter_stage_passed": 3,
     "scores": {
       "theory_of_impact": { "score": 4, "reasoning": "...", "confidence": 0.8 },
       "low_compute": { "score": 5, "reasoning": "...", "confidence": 0.9 },
       "accessible_complexity": { "score": 3, "reasoning": "...", "confidence": 0.7 },
       "narrow_scope": { "score": 4, "reasoning": "...", "confidence": 0.85 },
       "novelty": { "score": 4, "reasoning": "Derived from hybrid assessment", "confidence": 0.6 }
     },
     "novelty_assessment": {
       "classification": "mostly_novel",
       "evidence": [
         { "source": "semantic_scholar", "title": "Related Paper", "url": "...", "relevance": "..." }
       ],
       "confidence": 0.6,
       "derived_score": 4
     },
     "citation_verification": {
       "verified": ["doi:10.xxxx/xxxxx"],
       "failed": [],
       "removed": []
     },
     "weighted_score": 3.85,
     "confidence": 0.75,
     "eliminated": false,
     "elimination_reason": null
   }
   ```

3. **Staged filtering implementation:**
   - Stage 1 (cheap, LLM quick check): Read idea title + problem + direction. Score on basic relevance and scope. Threshold: ideas scoring < 2.0 on quick check are eliminated. This is done by the skill via a quick LLM prompt.
   - Stage 2 (medium, full LLM scoring): Full per-criterion rubric scoring. Threshold: `min_score` from `config/pipeline.yaml` thresholds.filter_score (default 2.5). Max ideas: `max_ideas` from config (default 500).
   - Stage 3 (expensive, web search): Hybrid novelty assessment with web search. "Already solved" is hard gate. Citation verification on survivors.

4. **Hybrid novelty assessment flow (implemented in the skill, with Python helpers):**
   - The skill does the web searching (ArXiv, Semantic Scholar, Google Scholar) since it has access to web search tools
   - Python `novelty.py` handles classification logic and score derivation
   - KB check happens first if `data/kb/` has content (query via `kb/query.py` when it exists)
   - Web search is ALWAYS mandatory — never KB-only

5. **Citation verification (programmatic, not LLM):**
   - `verification/citation.py` uses HTTP requests to Semantic Scholar API and CrossRef API
   - DOI verification: `https://api.crossref.org/works/{doi}` — checks for 200 response
   - Title verification: Semantic Scholar search API — matches title fuzzy
   - Unverified citations are removed from output (NFR4)
   - Falls back to LLM (cheap model) only when APIs are insufficient

6. **Per-team novelty weighting:**
   - `criteria_weights` in `TeamProfile` can override `novelty` weight
   - Experienced groups: high novelty weight (default or higher)
   - Novice teams: low novelty weight (replication studies are valuable per FR67)
   - Weight overrides are already supported by `TeamProfile.criteria_weights` in schemas.py

### Existing Code to Use (DO NOT Reinvent)

- `safety_ideas.config.loader.load_config()` — Load all config (teams, criteria, pipeline settings)
- `safety_ideas.config.schemas` — `TeamProfile`, `ScoringCriteria`, `StageThreshold`, `PipelineSettings`
- `safety_ideas.constants` — All path constants (`RUNS_DIR`, `SCORING_CRITERIA`, `STAGE_NAMES`)
- `safety_ideas.pipeline.generate.read_idea_sketches(run_dir)` — Read ideas from generate stage
- `safety_ideas.pipeline.orchestrator.PipelineLogger` — Structured JSON logging
- `safety_ideas.utils.load_yaml()` — YAML loading

### Implementation Approach

**Python modules to create:**

1. **`src/safety_ideas/pipeline/filter_score.py`** — Scoring computation and I/O:
   - `score_idea()` — Takes idea dict, criteria list, team profile; returns scored dict
   - `apply_weights()` — Computes weighted average using criteria weights + team overrides
   - `staged_filter()` — Applies progressive filtering with thresholds
   - `write_scored_idea()` / `read_scored_ideas()` — JSON I/O for scored ideas
   - CLI for skill invocation

2. **`src/safety_ideas/pipeline/novelty.py`** — Novelty assessment helpers:
   - `classify_novelty()` — Maps evidence to classification enum
   - `novelty_to_score()` — Maps classification string to 1-5 integer score
   - `format_novelty_assessment()` — Structures novelty data for scored idea JSON

3. **`src/safety_ideas/verification/citation.py`** — Citation verification:
   - `verify_doi()` — CrossRef API check
   - `verify_semantic_scholar()` — Semantic Scholar title search
   - `verify_citations()` — Orchestrates verification for all citations in an idea
   - `filter_unverified()` — Removes unverified citations

**Claude Code skill to create:**

4. **`.claude/commands/score-ideas.md`** — Orchestration skill that:
   - Accepts run directory or finds latest
   - Loads ideas via `uv run python -m safety_ideas.pipeline.generate read <run_dir>`
   - Stage 1: Quick LLM relevance check, eliminates low scorers
   - Stage 2: Full per-criterion LLM scoring against rubrics
   - Stage 3: Web search for novelty assessment (always mandatory), citation verification
   - Writes scored ideas via `uv run python -m safety_ideas.pipeline.filter_score write`
   - Logs via PipelineLogger
   - Presents scored results summary

### File Structure

```
src/safety_ideas/pipeline/
  filter_score.py      # NEW — scoring I/O, weight computation, staged filtering
  novelty.py           # NEW — novelty classification helpers
src/safety_ideas/verification/
  citation.py          # NEW — programmatic citation verification
.claude/commands/
  score-ideas.md       # NEW — Claude Code skill
tests/pipeline/
  test_filter_score.py # NEW — scoring tests
  test_novelty.py      # NEW — novelty classification tests
tests/verification/
  __init__.py          # NEW
  test_citation.py     # NEW — citation verification tests
```

### What NOT to Build

- No refinement or proposal assembly — that is Epic 5 (`/refine-ideas`)
- No ranking — that is Epic 5 (`/rank-ideas`)
- No KB query module — that is Epic 7 (but leave hook for future KB integration in novelty assessment)
- No actual web searching in Python — the skill handles web search via Claude's tools
- No semantic similarity for novelty — use keyword-based evidence matching
- Do not create new Pydantic schemas for scored ideas — use plain dicts + JSON for now

### NFRs Addressed

- **NFR1-NFR3 (Cost Efficiency):** Staged filtering kills bad ideas before expensive novelty assessment; citation verification uses cheap API calls not LLM; model tiering (Sonnet for scoring per pipeline.yaml)
- **NFR4 (Accuracy):** Unverified citations removed from output entirely
- **NFR6 (Evidence):** Novelty assessment includes evidence (papers found, search queries used)
- **NFR7 (Auditability):** Every score has explicit reasoning; all filtering decisions logged

## Dependencies

- **Story 1.1:** Config schemas, loader, project structure (DONE)
- **Story 1.2:** Participant profiles for team-specific novelty weighting (DONE)
- **Story 3.1:** Pipeline orchestrator, generate stage output format, PipelineLogger (DONE)

## Test Strategy

- **Unit tests** for Python modules:
  - `test_filter_score.py`: weight computation, staged filtering logic, scored idea JSON write/read round-trip, threshold application
  - `test_novelty.py`: classification logic, score derivation, edge cases (empty evidence, mixed signals)
  - `test_citation.py`: DOI verification (mocked HTTP), Semantic Scholar lookup (mocked), citation filtering
- **Manual test** for Claude Code skill:
  - Invoke `/score-ideas` on existing generation run
  - Verify scored ideas appear in `data/runs/<timestamp>/filter_score/`
  - Verify ideas with "already solved" novelty are eliminated
  - Verify citation verification removes unverifiable papers
  - Verify `pipeline.log.json` has scoring stage entries
- Run all tests with: `uv run pytest tests/pipeline/test_filter_score.py tests/pipeline/test_novelty.py tests/verification/ -v`

## Dev Agent Record

### Context Reference

### Agent Model Used
Claude Opus 4.6 (1M context)

### Debug Log References
N/A

### Completion Notes List
- Review fixed 6 issues: unused pytest imports (test_filter_score.py, test_citation.py), line-too-long in test_citation.py, hardcoded Stage 1 threshold replaced with STAGE1_RELEVANCE_THRESHOLD constant, misleading "Stage 2" elimination reason for max_ideas overflow corrected, and missing assess_novelty() function added to novelty.py with 5 new tests
- All 116 tests pass, ruff clean on story files
- filter_score thresholds already validated via existing PipelineSettings/StageThreshold Pydantic schema in pipeline.yaml

### File List
- `src/safety_ideas/pipeline/filter_score.py` — scoring computation, staged filtering, scored idea I/O, CLI
- `src/safety_ideas/pipeline/novelty.py` — novelty classification, assess_novelty, score derivation, CLI
- `src/safety_ideas/verification/citation.py` — DOI/Semantic Scholar API verification, citation filtering, CLI
- `src/safety_ideas/verification/__init__.py` — package init
- `src/safety_ideas/constants.py` — added STAGE1_RELEVANCE_THRESHOLD constant
- `.claude/commands/score-ideas.md` — Claude Code skill for scoring orchestration
- `tests/pipeline/test_filter_score.py` — 11 tests for scoring, weights, staged filtering, I/O
- `tests/pipeline/test_novelty.py` — 19 tests for classification, scoring, formatting, assess_novelty
- `tests/verification/__init__.py` — package init
- `tests/verification/test_citation.py` — 15 tests for DOI, Semantic Scholar, citation filtering
