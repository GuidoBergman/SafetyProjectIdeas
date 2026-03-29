---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
inputDocuments:
  - 'docs/prd.md'
workflowType: 'architecture'
lastStep: 8
status: 'complete'
completedAt: '2026-03-16'
project_name: 'SafetyProjectIdeas'
user_name: 'guido'
date: '2026-03-12'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

## Project Context Analysis

### Requirements Overview

**Functional Requirements (65 total, 14 categories):**

| Category | FRs | Architectural Significance |
|---|---|---|
| Knowledge Base Management | FR1-FR10, FR69 | Core subsystem — autonomous discovery, inclusion criteria, structured storage with selective retrieval. Tracks source code availability per paper (FR69) for filtering |
| KB Update Mechanisms | FR11-FR15 | Push/pull update patterns, subscription management, approval workflows |
| KB Suggestions | FR16-FR17 | Persistent suggestions list, review workflow |
| Pipeline Execution | FR18-FR22 | Stage independence, end-to-end composition, human intervention points, structured logging |
| Idea Generation | FR23-FR27, FR67-FR68 | V1: Single-provider generation via Claude Code with capable models. Multi-LLM parallel generation deferred to post-MVP. Generation strategies include experiment variations (FR67) and follow-up experiments (FR68) |
| Idea Evaluation & Scoring | FR28-FR35 | Configurable criteria/weights, staged filtering, citation verification, hybrid novelty assessment (evidence-based search → classification → hard gate on "already solved" → derived novelty score feeds into configurable criteria with per-team weighting). Ideas extending papers without source code are downranked (uses FR69 KB attribute) |
| Idea Refinement & Proposal Assembly | FR36-FR38, FR40 | Auto-strengthen, alternative framing, assemble full proposals (research question, approach, experiments, impact chain, citations) so Rank has complete signal |
| Ranking & Output | FR39, FR41-FR42 | Re-score full proposals, sort, filter, format markdown output, provenance tracking, concise human-scannable format |
| Collaborative Brainstorming | FR43-FR48 | Conversational mode with full KB access, directed exploration, open question assessment |
| Evaluate Existing Ideas | FR49-FR51 | External idea ingestion through same scoring/refinement pipeline |
| Configuration Management | FR52-FR57 | YAML-based, human-editable, persistent across sessions |
| Priority Areas | FR58-FR59 | Organizational priorities influencing pipeline behavior |
| Pipeline Memory & Learning | FR60-FR63 | Cross-session persistence, accumulated knowledge, unexplored direction tracking |
| Idea Repository | FR64-FR65 | Persistent searchable store, retrospective feedback loop |

**Non-Functional Requirements (14 total, 4 areas):**

| Area | NFRs | Architectural Impact |
|---|---|---|
| Cost Efficiency | NFR1-NFR3 | Model tiering within Claude family — capable models (Sonnet/Opus) for creative/analytical work (generation, scoring, refinement, proposal assembly), cheaper models (Haiku) for mechanical subtasks (citation verification, format validation, dedup checks, ranking/sorting). Token minimization via progressive elaboration |
| Accuracy & Reliability | NFR4-NFR7 | Citation verification pipeline, source traceability, explicit scoring reasoning |
| Integration | NFR8-NFR10 | V1: Modular source connectors for KB (ArXiv, forums, etc.) only. LLM provider abstraction deferred to post-MVP |
| Maintainability & Modularity | NFR11-NFR13 | Stage independence, externalized config, well-defined inter-stage interfaces |
| Security | NFR14 | V1: Simplified — no external LLM API keys to manage, just source connector credentials |

**V1 Scope Adjustment — Multi-LLM Generation Deferred:**
- All LLM work (generation, scoring, refinement, brainstorming) runs through Claude Code natively
- LiteLLM integration, multi-provider orchestration, and cross-provider deduplication move to post-MVP
- Model tiering stays in scope within the Claude family: capable models for creative/analytical work, cheaper models for mechanical verification subtasks
- This removes ~3 architectural components and significantly reduces integration complexity

**Scale & Complexity:**

- Primary domain: CLI/Agent tooling (Claude Code skills)
- Complexity level: Medium
- Estimated architectural components: ~6-7 (KB subsystem, pipeline orchestrator, 5 pipeline stages, configuration manager, persistent state/memory)

### Technical Constraints & Dependencies

- **Execution environment:** Claude Code skills — all operations must fit within skill invocation patterns
- **LLM provider:** Claude Code only (v1) — no external LLM dependencies. Model tiering by task complexity within Claude family
- **Storage:** Knowledge base format TBD — must support efficient querying, incremental updates, and selective context retrieval
- **Configuration:** YAML files for all configurable parameters. `teams.yaml` stores `default_team` and `default_participant` settings alongside team profiles
- **Output:** Markdown (ideas/proposals), JSON (pipeline logs), YAML (config)
- **Solo developer:** Architecture must be maintainable by one person
- **Quality over reliability:** System can require manual intervention; output quality is non-negotiable

### Cross-Cutting Concerns Identified

- **Citation integrity:** Verification must happen at multiple pipeline stages — generation, scoring, and final output
- **Auditability:** Every stage must log inputs, decisions, and outputs in structured format
- **Persistent state:** Knowledge base, pipeline memory, idea repository, configuration, and suggestions list all require cross-session persistence
- **Configuration propagation:** Team profiles and scoring criteria must flow through multiple pipeline stages consistently
- **Selective context retrieval:** Both pipeline stages and brainstorming need filtered KB access to avoid context bloat
- **Token efficiency:** Progressive elaboration pattern (cheap sketches → expand only winners) and model tiering (cheap models for mechanical subtasks) to minimize cost
- **Confidence reporting:** Every pipeline stage reports confidence scores on its outputs. Confidence is always reported, never used for automated filtering — the human decides what to act on
- **Graceful KB degradation:** All pipeline stages must function without KB. When KB is unavailable or thin, stages actively search the web (ArXiv, Semantic Scholar, Google Scholar) rather than relying solely on Claude's training knowledge

## Starter Template Evaluation

### Primary Technology Domain

CLI/Agent tooling (Claude Code skills with Python programmatic components) — no traditional starter template applies. Foundation is project structure + config schema + tooling choices.

### Starter Options Considered

This project doesn't fit traditional starter template patterns. It's built as Claude Code skills (prompt-based markdown) with Python for programmatic components. The "starter" is a well-defined project structure and tooling configuration.

**Evaluated approaches:**
- **Traditional CLI framework (Click/Typer):** Unnecessary — Claude Code skills handle the CLI interface
- **Cookiecutter Python template:** Too opinionated for a skills-based project
- **Manual project structure:** Best fit — custom structure matching the skill-based architecture

### Selected Approach: Custom Project Structure

**Rationale:** Claude Code skills are the primary interface, with Python modules for programmatic tasks. No existing starter template matches this hybrid pattern.

**Initialization:**

```bash
uv init saim
uv add pytest ruff pyyaml
```

### Architectural Decisions

**Language & Runtime:**
- Python 3.11+ for all programmatic components
- Claude Code skills (markdown) for pipeline orchestration and user interaction
- Skills invoke Python via Bash tool: `uv run python -m saim.<module>`

**Package Management:**
- uv (replaces pip + venv + pip-tools)
- `uv.lock` for reproducible installs
- External users set up with `uv sync`

**Storage:**
- Knowledge base: Markdown files with YAML frontmatter (human-readable source of truth)
- No SQLite — in-memory filtering via Python at 2000-3000 doc scale is fast and sufficient
- KB query module loads frontmatter, caches in memory, filters by subfield/org/venue/recency/tags
- SQLite can be added later as caching layer if KB grows beyond expectations

**Testing:** pytest
**Linting & Formatting:** ruff

**Project Structure:**

```
SafetyProjectIdeas/
├── .claude/
│   └── commands/         # Claude Code skills (markdown)
├── src/
│   └── saim/     # Python package
│       ├── kb/           # KB build + query
│       ├── pipeline/     # Pipeline stages
│       ├── connectors/   # Source connectors (arxiv, forums)
│       └── verification/ # Citation verification
├── data/
│   ├── kb/               # KB content (markdown w/ frontmatter)
│   ├── output/           # Pipeline output (ranked ideas)
│   └── logs/             # Pipeline logs (JSON)
├── config/               # YAML config files
├── tests/
├── pyproject.toml
└── uv.lock
```

**Backup & Durability:**
- Git + GitHub (free private repo) for all project data including KB contents
- No cloud compute costs — everything runs locally via Claude Code

### MVP Scope Adjustments

**New Requirement:**
- **FR66:** System can load pre-defined participant profiles (experience level, technical background, compute resources, time availability) and use them to tailor idea generation and brainstorming without requiring the user to re-enter their constraints. Profiles stored as YAML in config directory. Falls back to conversational discovery if no profile exists.

**Clarified for MVP:**
- FR43-48 (Collaborative Brainstorming) and auto-generation are the first user-facing capabilities. They work immediately using Claude's native AI Safety knowledge + active web search, plus participant profiles. KB integration enriches them as Track B progresses. External users use the same Claude Code interface. Brainstorming skill must be self-explanatory and guide users through describing constraints conversationally.

**Primary Interaction Mode:** Auto-generation (batch) is the primary mode, not interactive brainstorming. Guido's time is the bottleneck — the system auto-generates, scores, refines, and ranks. Guido reviews ranked output, then optionally brainstorms to refine specific directions.

**Moved to post-MVP:**
- FR11-FR15 (KB Update Mechanisms) — push/pull updates, subscriptions, newsletter processing
- FR16-FR17 (KB Suggestions) — suggestions list and review workflow
- FR5 (KB update command with approval workflow) — manual file drops replace this for MVP
- FR7 (change detection during updates) — no automated updates means no change detection

**MVP KB scope reduced from 17 requirements to ~8:**
- FR1 (inclusion criteria), FR2 (initial build), FR3-FR4 (approval workflow), FR6 (edit criteria), FR8-FR10 (selective retrieval, filtering, browsing)

**User model for MVP:**
- **Guido:** Configures pipeline, builds KB, runs full pipeline, brainstorms — power user
- **External users with profile:** Brainstorming skill loads their participant profile automatically, generates tailored ideas immediately. A default participant can be configured so the profile is used without specifying a name
- **External users without profile:** Skill guides them through describing constraints conversationally (existing FR43-48 flow)

**Note:** Project initialization is the first implementation story.

## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
- Inter-stage data format (hybrid markdown/JSON)
- KB frontmatter schema and document structure
- KB build pipeline (parse-first with existing libraries, LLM-extract from sections only)
- Configuration validation (Pydantic)
- Source priority system for KB ingestion and context feeding

**Important Decisions (Shape Architecture):**
- Pipeline run state organization
- Credential management
- Document parsing strategy per source type (using existing libraries)

**Deferred Decisions (Post-MVP):**
- SQLite caching layer (if KB exceeds 3000 docs)
- LiteLLM multi-provider integration
- KB update automation (push/pull mechanisms)
- Web interface for external users
- CI/CD pipeline
- In-memory caching for KB queries (add only if profiling shows bottleneck)

### Data Architecture

**Inter-Stage Data Format: Hybrid (Markdown + JSON)**
- **Generate stage** outputs idea sketches as markdown files (natural document format for creative content)
- **Filter/Score stage** outputs JSON (structured scores, reasoning per criterion, numeric thresholds)
- **Refine stage** outputs full proposals as markdown (research question, approach, first experiments, theory of impact chain, cited sources)
- **Rank stage** re-scores full proposals, sorts, filters, and outputs final ranked markdown with embedded score metadata
- Each stage writes to its run directory; next stage reads from previous

**KB Document Structure (JSON with section-level access):**

```json
{
  "meta": {
    "title": "Paper title",
    "source_type": "paper | forum_post | agenda | report | open_problems_list",
    "source_venue": "arxiv | alignment_forum | lesswrong | conference | org_report",
    "organization": "Anthropic",
    "authors": ["Author Name"],
    "date": "2026-01-15",
    "subfields": ["mechanistic_interpretability", "scalable_oversight"],
    "tags": ["deceptive_alignment", "tool_use"],
    "priority": 1,
    "url": "https://...",
    "doi": "10.xxxx/xxxxx",
    "key_findings": "LLM-extracted from parsed sections",
    "limitations": "LLM-extracted from parsed sections",
    "relevance_notes": "LLM-extracted: why this matters for AI Safety research",
    "source_code_available": "available | partially_available | not_available | unknown"
  },
  "sections": {
    "abstract": "...",
    "introduction": "...",
    "conclusion": "...",
    "discussion": "...",
    "limitations": "..."
  }
}
```
Query module never returns all sections — caller always specifies which sections they need.

**Source Code Availability (FR69):**
- Tracked per KB document as a meta field. Populated during KB build (check for GitHub/GitLab links in paper, associated repos on PapersWithCode, or code links in blog posts).
- Pipeline stages that generate ideas by extending existing work use this field to downrank or filter out ideas building on papers without available source code — extending work without code is substantially harder and riskier.
- Query module supports filtering by `source_code_available` so pipeline stages can preferentially draw on papers with code.

**Source Priority System:**
- Priority 1: Open problems lists — most actionable, direct idea input. Ingested and consumed first.
- Priority 2: Key papers, org reports — specific findings, concrete results.
- Priority 3: Research agendas, regular papers, forum posts — broad context. Research agendas are intentionally priority 3 as they tend to be too broad for direct idea generation.
- Source stage uses priority to determine ingestion order and context allocation — high-priority sources get processed and fed to Generate first.

**KB Bootstrap: 800-Paper Shallow Review Ingestion**
- Source: CSV from github.com/arb-consulting/shallow-review-2025 (`data-dump-classify.csv`)
- Contains: ~800 papers with title, authors, organizations, date, venue, summary, categories, `ai_safety_relevance` score (0-1), `shallow_review_inclusion` score (0-1), kind (paper/blog/forum), and nested JSON metadata
- Also includes: `taxonomy.yaml` (7 AI Safety categories: Black-box Safety, Interpretability, Safety by Construction, Make AI Solve It, Theory, Multi-agent & Evals, Labs), scraped HTML (`.html.zst`), curated source link lists
- Ingestion maps CSV fields to KB JSON schema: title→title, authors→authors, kind→source_type, categories→subfields/tags, summary→key_findings, ai_safety_relevance→priority
- The existing taxonomy provides initial subfield classification — but which categories to prioritize for idea generation needs further research (via `/research-landscape`)
- No manual curation needed — the CSV's relevance scores provide ready-made priority ranking

**KB Build Pipeline (Token-Efficient):**
1. **Discovery** — Semantic Scholar API for paper search and metadata (title, abstract, authors, venue, DOI, citation count). ArXiv API (arxiv.py) for ArXiv-specific searches. Many papers can be evaluated from abstract + metadata alone without downloading PDFs.
2. **Automated parsing** (Python, zero LLM cost) — for papers that need deeper extraction: Docling (IBM) for PDF section extraction (abstract, introduction, conclusion, discussion, limitations). LessWrong/Alignment Forum content retrieved via their public GraphQL API (returns HTML or Markdown directly — no scraping needed). Trafilatura for HTML content from research org blog posts (MIRI, Anthropic, etc.). Strip references, figures, formatting noise.
3. **LLM extraction** (reads parsed sections only, not full paper) — generates frontmatter: key_findings, limitations summary, relevance_notes, subfield/tag classification.
4. **Full storage** — original content stored in markdown body for future deep-dive access.

**Document Parsers (Existing Libraries):**

| Source Type | Discovery | Parsing | Libraries |
|---|---|---|---|
| ArXiv papers | arxiv.py + Semantic Scholar API | PDF section extraction | Docling (IBM) |
| Alignment Forum / LessWrong | GraphQL API | Structured content (HTML/Markdown) | Direct API (requests/httpx) — no scraping needed |
| Org reports / agendas | Manual or Semantic Scholar | PDF section extraction | Docling |
| Research org blogs | Manual curation | HTML → clean text | Trafilatura |
| Open problems lists | Manual curation | HTML or PDF as appropriate | Trafilatura or Docling |

**KB Querying:**
- Python module loads and filters JSON meta from KB files on each query
- No in-memory caching for MVP — direct load-and-filter at 2000-3000 docs is fast enough
- Filters by any meta dimension: subfield, organization, venue, recency, tags, priority
- Returns metadata by default; specific sections only when caller explicitly requests them
- Never returns all sections at once — caller always specifies which sections they need via `sections=[]` parameter

### Configuration Validation

**Pydantic Models**
- Config schemas defined as Pydantic models in `src/saim/config/`
- YAML files validated on load with clear error messages
- Models serve as both validation layer and typed data access
- Schemas: `TeamProfile`, `ScoringCriteria`, `KBCriteria`, `PipelineSettings`, `ParticipantProfile`
- `AppConfig` includes `default_participant: str | None` — the name of the participant profile loaded by default when none is specified

### Credential Management

**.env + python-dotenv**
- API keys for source connectors stored in `.env`
- `.env` added to `.gitignore`
- Loaded via python-dotenv on application startup
- No secrets in YAML config or pipeline output

### Pipeline Run State & Logging

**Run Directory + Consolidated Log**
- Each pipeline run creates: `data/runs/<timestamp>/`
- Run directory contains per-stage outputs (markdown and JSON as appropriate)
- Single consolidated JSON log per run capturing full pipeline trace
- Final ranked output also copied to `data/output/` for easy access

### Infrastructure & Deployment

**Local-Only (MVP)**
- Runs entirely on local machine via Claude Code
- Git + GitHub (free private repo) for backup and version control
- No cloud compute, no CI/CD, no containers
- External users clone repo, run `uv sync`, use Claude Code skills

### Project Dependencies

```bash
# Track A (day 1 — idea generation)
uv add pytest ruff pyyaml pydantic python-dotenv

# Track B (KB infrastructure — parallel)
uv add semanticscholar arxiv docling trafilatura
```

**Note:** Semantic Scholar API requires a free API key for reliable rate limits (1 req/sec dedicated). Register at semanticscholar.org and add the key to `.env`.

### Decision Impact Analysis

**Implementation: Two Parallel Tracks**

*Track A — Ideas (from day 1, parallel with Track B):*
1. Project initialization (uv, package structure, config schemas for teams/criteria/participants)
2. `/research-landscape` skill — discover open problems lists, research agendas, key sources, and which categories to cover
3. `/generate-ideas` skill — auto-batch idea generation, balanced across researched categories. Uses KB when available, Claude knowledge + web search otherwise
4. `/score-ideas` with hybrid novelty assessment — evidence-based search (KB first pass if available, then always web search), hard gate on "already solved", derived novelty score feeds into configurable criteria with per-team weighting. Confidence reported on every assessment
5. `/refine-ideas` — auto-strengthen, alternative framings, assemble full proposals, with confidence reported
6. `/rank-ideas` — re-score full proposals, sort, filter, with confidence reported throughout
7. `/brainstorm` skill — interactive collaborative mode (secondary to auto-generation)
8. `/evaluate-idea` skill — score existing ideas against criteria

*Track B — Knowledge Base (parallel with Track A):*
1. Ingest 800-paper shallow review CSV (from github.com/arb-consulting/shallow-review-2025) — auto-map to KB schema using existing taxonomy
2. KB query module (filtering by subfield, org, venue, recency, tags)
3. Discover key AI Safety authors' recent work via Semantic Scholar API
4. `/research-sources` skill — find additional open problems lists, agendas, sources
5. Source connectors (ArXiv, Semantic Scholar, LessWrong/AF GraphQL API, blog scraper) and document parsers
6. Full KB build pipeline with approval workflow

*Convergence:* As Track B populates the KB, Track A stages automatically get richer context. Full end-to-end pipeline run once both tracks are validated.

**Cross-Component Dependencies:**
- Pipeline stages use KB query module for context retrieval **when KB is available**; degrade gracefully to Claude's native knowledge + active web search when KB is empty or thin
- Filter/Score depends on Pydantic config models for criteria/weights
- KB build depends on document parsers (Docling, Trafilatura, LessWrong/AF GraphQL API) and LLM extraction
- Brainstorming skill depends on participant profiles and config; KB access is **additive enrichment**, not a prerequisite
- Hybrid novelty assessment ALWAYS includes web search — KB is first pass (fast, cheap), web is mandatory second pass. Never KB-only. "Already solved" is a hard gate; "novel"/"partially addressed" feed a derived novelty score into configurable criteria
- All pipeline stages report confidence scores but do NOT filter by confidence — human decides what to act on
- Pipeline orchestrator depends on all stages and logging infrastructure

## Implementation Patterns & Consistency Rules

### Naming Patterns

**Python Code:**
- Functions/variables: `snake_case` — `load_frontmatter()`, `query_kb()`
- Classes: `PascalCase` — `TeamProfile`, `PipelineRun`
- Constants: `UPPER_SNAKE` — `DEFAULT_PRIORITY`, `STAGE_NAMES`
- Modules/files: `snake_case` — `kb_query.py`, `citation_verifier.py`
- Private: `_leading_underscore` for internal functions

**YAML frontmatter fields:** `snake_case` consistently — `source_type`, `key_findings`, `relevance_notes`

**KB document file naming:** `{source_venue}_{sanitized_title}_{date}.json` — e.g., `arxiv_deceptive_alignment_in_tool_use_2026-01-15.json`

### Structure Patterns

**Project Organization:**
- Tests in `tests/` mirroring `src/` structure — `tests/kb/test_query.py` for `src/saim/kb/query.py`
- `src/saim/utils.py` — flat file for helper functions used across modules
- `src/saim/constants.py` — flat file for all project constants (default priorities, stage names, file patterns, etc.)
- Config schemas in `src/saim/config/schemas.py` — all Pydantic models in one place until complexity warrants splitting

### Data Format Patterns

**JSON log format:**
```json
{
  "timestamp": "2026-03-16T14:30:00Z",
  "run_id": "2026-03-16T14-30-00",
  "stage": "filter_score",
  "level": "info",
  "message": "Scored idea against 5 criteria",
  "data": {}
}
```

**Pipeline run metadata:** Each run directory includes `run_meta.json`:
```json
{
  "run_id": "2026-03-16T14-30-00",
  "timestamp": "2026-03-16T14:30:00Z",
  "git_commit": "a8b971e",
  "parameters": {
    "team_profile": "mentor_novice",
    "criteria_weights": {},
    "stages": ["source", "generate", "filter_score", "refine", "rank"]
  }
}
```
This makes every run reproducible — you know exactly what code and config produced the output.

**Inter-stage data:**
- Markdown files use frontmatter for metadata, body for content
- JSON files use `snake_case` keys consistently
- Every inter-stage file includes `run_id`, `stage`, and `timestamp` in metadata

**KB documents:** JSON format with `meta` and `sections` keys. All meta fields are always present (empty string or empty list if not applicable, never omitted). Sections stored individually for section-level access. Query module never returns all sections at once — caller always specifies which sections they need.

### Error Handling

Keep it simple:
- Use Python's built-in exceptions (`ValueError`, `FileNotFoundError`, etc.) — no custom exception hierarchy
- Use Python `logging` module for diagnostics
- Skills read Python stdout/stderr and present results to user — no silent failures

### Config Access Pattern

```python
from saim.config import load_config
config = load_config()  # Returns validated Pydantic models
config.teams["mentor_novice"].compute_budget
```

Never read YAML files directly in pipeline code — always go through Pydantic models.

### Hybrid Novelty Assessment Flow

**Mandatory for all ideas (generation, scoring, evaluation). Uses a hybrid approach — separate evidence-based assessment that feeds a derived score into configurable criteria:**

1. If KB available: query KB for related work in same subfield/tags (fast, cheap)
2. Always: search web — ArXiv, Semantic Scholar, Google Scholar for related/identical work
3. Synthesize assessment: classify as novel / partially addressed / already solved, with supporting evidence (NFR6)
4. **Hard gate:** "Already solved" classification eliminates the idea immediately — no further scoring or refinement, regardless of other criteria scores
5. **Derived score:** The classification (novel/partially addressed) is converted to a novelty score that feeds into the configurable scoring criteria alongside theory_of_impact, low_compute, accessible_complexity, narrow_scope, etc.
6. **Per-team weighting:** Novelty weight is configurable per team type — experienced groups weight it high (these projects should break new ground), novice teams can weight it low (replication studies and variations of existing experiments are valuable learning exercises, per FR67)
7. Report confidence in the assessment
8. Never rely entirely on KB — web search is always mandatory

**Why hybrid?** Novelty requires a fundamentally different methodology from other criteria (evidence-based search vs. LLM judgment), and "already solved" must be a hard gate. But "partially addressed" is a spectrum that teams should be able to weight — a novice replication study has different novelty needs than an experienced group's flagship project. The hybrid approach preserves the gate, the evidence, and the configurability.

### Confidence Reporting (Cross-Cutting)

Every pipeline stage reports a confidence score on its outputs:
- **Generation:** confidence in idea quality
- **Scoring:** confidence in each criterion score
- **Novelty:** confidence in the novelty assessment (how thorough was the search)
- **Refinement:** confidence that refinement improved the idea
- **Ranking:** overall confidence

Confidence is ALWAYS reported, NEVER used for automated filtering — the human decides what to act on. Confidence is included in all output formats (markdown frontmatter for ideas, JSON for logs).

### Skill Patterns

- **Python invocation:** Always `uv run python -m saim.<module> <args>`
- **Output:** Skills read Python stdout/stderr and present results to user
- **Error recovery:** If a Python command fails, skill reads error output and explains what went wrong

### Enforcement Guidelines

**All AI agents MUST:**
- Follow Python naming conventions (enforced by ruff)
- Use Pydantic models for all config access (never raw YAML parsing in pipeline code)
- Include `run_id`, `stage`, `timestamp` in all inter-stage data
- Write tests in `tests/` mirroring `src/` structure
- Name KB documents using the `{venue}_{title}_{date}.json` pattern
- Store run parameters and git commit in `run_meta.json`

**Pattern Enforcement:**
- ruff catches naming and style violations automatically
- Pydantic validates config correctness at runtime
- pytest structure conventions enforced by code review

## Project Structure & Boundaries

### Complete Project Directory Structure

```
SafetyProjectIdeas/
├── .claude/
│   └── commands/                    # Claude Code skills
│       │   # Track A — Ideas (day 1)
│       ├── research-landscape.md    # Discover open problems lists, agendas, categories
│       ├── generate-ideas.md        # Auto-batch idea generation
│       ├── score-ideas.md           # Score + hybrid novelty (KB → web always → hard gate → derived score)
│       ├── refine-ideas.md          # Auto-strengthen, alternative framings, assemble full proposals
│       ├── rank-ideas.md            # Re-score full proposals, sort, filter
│       ├── brainstorm.md            # Collaborative brainstorming (secondary mode)
│       ├── evaluate-idea.md         # Score an existing idea
│       ├── configure-teams.md       # Team profile management
│       │   # Track B — KB (parallel)
│       ├── research-sources.md      # Find additional sources, agendas
│       ├── build-kb.md              # KB construction with ingestion
│       └── run-pipeline.md          # Full pipeline (once tracks converge)
├── src/
│   └── saim/
│       ├── __init__.py
│       ├── constants.py             # All project constants
│       ├── utils.py                 # Shared helper functions
│       ├── config/
│       │   ├── __init__.py
│       │   ├── schemas.py           # Pydantic models (TeamProfile, ScoringCriteria, etc.)
│       │   └── loader.py            # load_config(), .env loading
│       ├── kb/
│       │   ├── __init__.py
│       │   ├── builder.py           # KB build orchestration (discovery → parse → extract → store)
│       │   ├── query.py             # Load meta, filter, return requested sections
│       │   └── document.py          # KB document read/write, JSON handling
│       ├── connectors/
│       │   ├── __init__.py
│       │   ├── arxiv.py             # ArXiv API via arxiv.py
│       │   ├── semantic_scholar.py  # Semantic Scholar API
│       │   ├── web_scraper.py       # Research org blogs via Trafilatura
│       │   ├── lesswrong.py         # LessWrong/Alignment Forum via GraphQL API
│       │   └── parsers/
│       │       ├── __init__.py
│       │       ├── pdf_parser.py    # PDF section extraction via Docling
│       │       └── html_parser.py   # HTML content extraction via Trafilatura
│       ├── pipeline/
│       │   ├── __init__.py
│       │   ├── orchestrator.py      # Run directory setup, stage sequencing, logging
│       │   ├── memory.py            # Load past idea titles from data/ideas/ to avoid repetition
│       │   ├── source.py            # Source stage: select KB context by priority
│       │   ├── generate.py          # Generate stage: idea sketches from source material
│       │   ├── filter_score.py      # Filter/Score stage: evaluate against criteria + hybrid novelty assessment (FR34: evidence search → hard gate → derived score)
│       │   ├── refine.py            # Refine stage: strengthen, reframe, assemble full proposals
│       │   └── rank.py              # Rank stage: re-score full proposals, sort, filter, format output
│       └── verification/
│           ├── __init__.py
│           └── citation.py          # Citation/DOI verification
├── data/
│   ├── kb/                          # Knowledge base content (JSON files with meta + sections)
│   ├── output/                      # Final ranked idea lists (latest results)
│   ├── runs/                        # Pipeline run directories
│   │   └── <timestamp>/
│   │       ├── run_meta.json        # Git commit, parameters, config snapshot
│   │       ├── source/              # Source stage output
│   │       ├── generate/            # Idea sketches (markdown)
│   │       ├── filter_score/        # Scored ideas (JSON)
│   │       ├── refine/              # Refined ideas (markdown)
│   │       ├── rank/                # Final ranked output (markdown)
│   │       └── pipeline.log.json    # Consolidated run log
│   └── ideas/                       # Persistent idea repository (FR64-65)
├── config/
│   ├── teams.yaml                   # Team profiles, default_team, default_participant
│   ├── criteria.yaml                # Scoring criteria and weights
│   ├── kb-criteria.yaml             # KB inclusion criteria
│   ├── pipeline.yaml                # Pipeline settings (model assignments, thresholds)
│   └── participants/                # Participant profiles (FR66)
│       └── <name>.yaml
├── tests/
│   ├── conftest.py                  # Shared fixtures
│   ├── config/
│   │   └── test_schemas.py
│   ├── kb/
│   │   ├── test_builder.py
│   │   ├── test_query.py
│   │   └── test_document.py
│   ├── connectors/
│   │   ├── test_arxiv.py
│   │   ├── test_semantic_scholar.py
│   │   ├── test_lesswrong.py
│   │   └── parsers/
│   │       ├── test_pdf_parser.py
│   │       └── test_html_parser.py
│   ├── pipeline/
│   │   ├── test_orchestrator.py
│   │   ├── test_source.py
│   │   ├── test_generate.py
│   │   ├── test_filter_score.py
│   │   ├── test_refine.py
│   │   └── test_rank.py
│   └── verification/
│       └── test_citation.py
├── .env                             # API keys (gitignored)
├── .env.example                     # Template for required env vars
├── .gitignore
├── pyproject.toml                   # uv project config, CLI entry points, ruff config
├── uv.lock
└── README.md
```

### KB Document Format (JSON)

```json
{
  "meta": {
    "title": "Paper title",
    "source_type": "paper",
    "source_venue": "arxiv",
    "organization": "Anthropic",
    "authors": ["Author Name"],
    "date": "2026-01-15",
    "subfields": ["mechanistic_interpretability", "scalable_oversight"],
    "tags": ["deceptive_alignment", "tool_use"],
    "priority": 2,
    "url": "https://...",
    "doi": "10.xxxx/xxxxx",
    "key_findings": "LLM-extracted from parsed sections",
    "limitations": "LLM-extracted from parsed sections",
    "relevance_notes": "LLM-extracted: why this matters for AI Safety research",
    "source_code_available": "available"
  },
  "sections": {
    "abstract": "...",
    "introduction": "...",
    "conclusion": "...",
    "discussion": "...",
    "limitations": "..."
  }
}
```

**KB Query API:**
```python
# Metadata only (cheapest — for filtering, listing)
docs = kb.query(subfield="interpretability")

# Metadata + specific sections (for pipeline stages)
docs = kb.query(subfield="interpretability", sections=["abstract", "key_findings"])

# Caller always specifies which sections — never returns all sections at once
```

### Requirements to Structure Mapping

| FR Category | Primary Location | Key Files |
|---|---|---|
| KB Management (FR1-FR4, FR6, FR8-FR10) | `src/saim/kb/` | `builder.py`, `query.py`, `document.py` |
| Pipeline Execution (FR18-FR22) | `src/saim/pipeline/` | `orchestrator.py` |
| Idea Generation (FR23-FR27) | `src/saim/pipeline/` | `source.py`, `generate.py` |
| Evaluation & Scoring (FR28-FR35) | `src/saim/pipeline/` | `filter_score.py` + `verification/citation.py` |
| Idea Refinement & Proposal Assembly (FR36-FR38, FR40) | `src/saim/pipeline/` | `refine.py` |
| Ranking & Output (FR39, FR41-FR42) | `src/saim/pipeline/` | `rank.py` |
| Brainstorming (FR43-FR48, FR66) | `.claude/commands/` | `brainstorm.md` |
| Evaluate Existing Ideas (FR49-FR51) | `.claude/commands/` | `evaluate-idea.md` |
| Configuration (FR52-FR57) | `src/saim/config/` + `config/` | `schemas.py`, `loader.py`, YAML files |
| Memory & Learning (FR60-FR63) | `data/` | `ideas/`, `runs/` |
| Idea Repository (FR64-FR65) | `data/ideas/` | Markdown files with scores |

**Post-MVP:** FR58-FR59 (Priority Areas), FR11-FR17 (KB Updates & Suggestions)

### Architectural Boundaries

**Boundary 1: Skills ↔ Python**
- Skills (`.claude/commands/`) orchestrate and present to user
- Python (`src/saim/`) does computation
- Communication: skills invoke `uv run python -m saim.<module>` via Bash
- Skills never import Python directly; Python never writes skill files

**Boundary 2: Pipeline Stages**
- Each stage reads from previous stage's output directory
- Each stage writes to its own output directory within the run
- Stages communicate only through files — no shared state, no function calls between stages
- Orchestrator manages sequencing and run directory setup

**Boundary 3: KB ↔ Pipeline**
- `kb/query.py` is the interface between KB and pipeline stages **when KB content exists**
- Pipeline stages and brainstorming MUST function without KB — Claude's native knowledge + active web search is the baseline; KB is augmentation
- When KB is available, pipeline stages never read KB files directly — always go through query module
- Query module returns metadata by default; specific sections only when explicitly requested
- Full section dumps are never returned — caller always specifies which sections
- Hybrid novelty assessment always follows: KB check (if available) → web search (always) → classification → hard gate on "already solved" → derived novelty score. Never relies entirely on KB

**Boundary 4: Config ↔ Everything**
- `config/loader.py` is the single entry point for all configuration
- All modules receive validated Pydantic models, never raw YAML
- Config files in `config/` are the source of truth; Pydantic models in `config/schemas.py` define the shape

### Data Flow

```
[Track A — Ideas without KB (day 1)]
config/ → generate-ideas skill → Claude generates from training knowledge + web search
→ score (hybrid novelty: KB if available → web search always → hard gate "already solved" → derived novelty score) → refine → rank
→ data/output/

[Track A — Ideas with KB (after Track B populates KB)]
config/ → generate-ideas skill → reads KB via query.py + Claude knowledge + web search
→ score (hybrid novelty: KB first → web always → hard gate → derived score) → refine → rank → data/output/

[Track B — KB Bootstrap]
800-paper CSV (arb-consulting/shallow-review-2025) → ingestion script → data/kb/*.json
Semantic Scholar API → key authors' recent work → data/kb/*.json

[Track B — Full KB Build (later)]
Semantic Scholar / ArXiv / Web → connectors/ → parsers/ → kb/builder.py → data/kb/*.json

[Brainstorming (secondary mode)]
brainstorm.md skill → loads participant profile from config/participants/
→ queries KB via kb/query.py if available, else uses Claude knowledge + web search
→ conversational idea generation with user
```

### External Integrations

| Integration | Module | Purpose |
|---|---|---|
| Semantic Scholar API | `connectors/semantic_scholar.py` | Paper discovery, metadata, abstracts (requires free API key) |
| ArXiv API | `connectors/arxiv.py` | ArXiv paper search and PDF download |
| LessWrong / Alignment Forum GraphQL API | `connectors/lesswrong.py` | Forum post content retrieval (no scraping — direct API) |
| Research org blogs | `connectors/web_scraper.py` | Blog post scraping via Trafilatura |
| Docling (IBM) | `connectors/parsers/pdf_parser.py` | PDF section extraction (pure Python, no Docker) |

## Architecture Validation Results

### Coherence Validation

**Decision Compatibility:** All technology choices are compatible. Python + uv + pytest + ruff is a clean, standard stack. JSON KB with Python query module uses built-in `json`. Pydantic validates YAML config loaded via pyyaml. Claude Code skills invoke Python via Bash — standard pattern. No conflicts detected.

**Pattern Consistency:** Naming conventions are consistent (`snake_case` throughout Python and data formats). Structure patterns align with the Python package layout. Communication between skills and Python is uniform (`uv run python -m saim.<module>`).

**Structure Alignment:** Project structure supports all decisions. Boundaries are clear (skills ↔ Python, pipeline stages via files, KB accessed only through query module, config only through Pydantic). Integration points are properly structured.

### Requirements Coverage Validation

**MVP Functional Requirements:**

| FR Category | Status | Coverage |
|---|---|---|
| KB Management (FR1-FR4, FR6, FR8-FR10) | ✅ Covered | `kb/` module + `build-kb.md` skill |
| Pipeline Execution (FR18-FR22) | ✅ Covered | `pipeline/orchestrator.py` + per-stage skills |
| Idea Generation (FR23-FR27) | ✅ Covered | `source.py` + `generate.py`. Multi-LLM deferred, model tiering via Claude family |
| Evaluation & Scoring (FR28-FR35) | ✅ Covered | `filter_score.py` + `citation.py`. FR34 hybrid novelty assessment in filter_score (evidence-based search → hard gate → derived score) |
| Refinement & Proposal Assembly (FR36-FR38, FR40) | ✅ Covered | `refine.py` |
| Ranking & Output (FR39, FR41-FR42) | ✅ Covered | `rank.py` |
| Brainstorming (FR43-FR48, FR66) | ✅ Covered | `brainstorm.md` skill + participant profiles |
| Evaluate Existing (FR49-FR51) | ✅ Covered | `evaluate-idea.md` skill |
| Configuration (FR52-FR57) | ✅ Covered | `config/` + Pydantic schemas |
| Memory & Learning (FR60-FR63) | ✅ Covered (minimal) | `pipeline/memory.py` — loads past idea titles to avoid repetition. Enriched post-MVP |

**Post-MVP (correctly deferred):**
- FR11-FR17 (KB Updates & Suggestions)
- FR58-FR59 (Priority Areas)
- FR64-FR65 (Idea Repository management, retrospective feedback)

**Non-Functional Requirements:**

| NFR | Status | How Addressed |
|---|---|---|
| NFR1-NFR3 (Cost Efficiency) | ✅ | Model tiering within Claude family, token-efficient KB build (parse first, LLM reads sections only), progressive elaboration |
| NFR4-NFR7 (Accuracy & Reliability) | ✅ | Citation verification module, section-level source traceability, explicit scoring reasoning in JSON output |
| NFR8-NFR10 (Integration) | ✅ | Modular connectors per source type. LLM provider abstraction deferred to post-MVP |
| NFR11-NFR13 (Maintainability) | ✅ | Stage independence (file-based communication), externalized YAML config, Pydantic interfaces |
| NFR14 (Security) | ✅ | `.env` for credentials, gitignored, no secrets in config or output |

### Gap Analysis Results

**Gap 1 — Pipeline Memory (FR60-FR63): Resolved**
MVP implementation: `pipeline/memory.py` loads idea titles/summaries from `data/ideas/` and passes them to Generate stage as "already generated — don't repeat." No run history analysis, no source material tracking. Cheapest possible dedup. Enriched post-MVP.

**Gap 2 — Idea Repository Management (FR64-FR65): Deferred**
Moved to post-MVP. `data/ideas/` directory remains (rank.py copies final output there), but no repository management, no feedback mechanism, no retrospective scoring.

**No critical gaps remain for MVP.**

### Architecture Completeness Checklist

**✅ Requirements Analysis**
- [x] Project context thoroughly analyzed
- [x] Scale and complexity assessed
- [x] Technical constraints identified
- [x] Cross-cutting concerns mapped
- [x] MVP scope clearly defined with deferred items documented

**✅ Architectural Decisions**
- [x] Technology stack fully specified (Python, uv, pytest, ruff, Pydantic)
- [x] Storage format decided (JSON KB with section-level access)
- [x] Inter-stage data format decided (hybrid markdown/JSON)
- [x] External libraries selected (Docling, Trafilatura, arxiv.py, Semantic Scholar, LessWrong/AF GraphQL API)
- [x] Credential management decided (.env + python-dotenv)

**✅ Implementation Patterns**
- [x] Naming conventions established (Python standard, snake_case data)
- [x] Structure patterns defined (tests mirror src, utils.py, constants.py)
- [x] Error handling specified (built-in exceptions, logging module)
- [x] Config access pattern defined (always through Pydantic)
- [x] Skill invocation pattern defined (uv run python -m)

**✅ Project Structure**
- [x] Complete directory structure defined
- [x] Component boundaries established (4 boundaries documented)
- [x] Data flow mapped (KB build, pipeline run, brainstorming)
- [x] Requirements to structure mapping complete
- [x] External integrations documented

### Architecture Readiness Assessment

**Overall Status:** READY FOR IMPLEMENTATION

**Confidence Level:** High

**Key Strengths:**
- Clean separation between Claude Code skills (orchestration) and Python (computation)
- Token-efficient KB build pipeline (parse first, LLM reads sections only)
- Section-level KB access prevents accidental token waste
- Modular pipeline stages with file-based communication — easy to debug and iterate independently
- Standard Python tooling (uv, pytest, ruff, Pydantic) — no exotic dependencies, no Docker/Java required
- Source priority system ensures highest-value content drives idea generation

**Areas for Future Enhancement (Post-MVP):**
- Multi-LLM generation via LiteLLM for idea diversity
- SQLite caching if KB grows beyond 3000 docs
- KB update automation (push/pull mechanisms)
- Idea repository with retrospective feedback loop
- Priority areas feature
- Richer pipeline memory (source material tracking, run history analysis)

### Implementation Handoff

**AI Agent Guidelines:**
- Follow all architectural decisions exactly as documented
- Use implementation patterns consistently across all components
- Respect project structure and boundaries (especially: KB only via query module, config only via Pydantic)
- Refer to this document for all architectural questions

**Implementation: Two Parallel Tracks**

*Track A — Ideas (from day 1, parallel with Track B):*
1. Project initialization (uv, package structure, config schemas for teams/criteria/participants)
2. `/research-landscape` skill — discover open problems lists, research agendas, key sources, and which categories to cover
3. `/generate-ideas` skill — auto-batch idea generation, balanced across researched categories. Uses KB when available, Claude knowledge + web search otherwise
4. `/score-ideas` with hybrid novelty assessment — evidence-based search (KB first pass if available, then always web search), hard gate on "already solved", derived novelty score feeds into configurable criteria. Confidence reported on every assessment
5. `/refine-ideas` — auto-strengthen, alternative framings, assemble full proposals, with confidence reported
6. `/rank-ideas` — re-score full proposals, sort, filter, with confidence reported throughout
7. `/brainstorm` skill — interactive collaborative mode (secondary to auto-generation)
8. `/evaluate-idea` skill — score existing ideas against criteria

*Track B — Knowledge Base (parallel with Track A):*
1. Ingest 800-paper shallow review CSV — auto-map to KB schema using existing taxonomy
2. KB query module (filtering by subfield, org, venue, recency, tags)
3. Discover key AI Safety authors' recent work via Semantic Scholar API
4. `/research-sources` skill — find additional open problems lists, agendas, sources
5. Source connectors (ArXiv, Semantic Scholar, LessWrong/AF GraphQL API, blog scraper) and document parsers
6. Full KB build pipeline with approval workflow

*Convergence:* As Track B populates the KB, Track A stages automatically get richer context.

## Architecture Completion Summary

**Architecture Decision Workflow:** COMPLETED
**Total Steps Completed:** 8
**Date Completed:** 2026-03-16
**Document Location:** docs/architecture.md

**Architecture Status:** READY FOR IMPLEMENTATION

**Document Maintenance:** Update this architecture when major technical decisions are made during implementation.
