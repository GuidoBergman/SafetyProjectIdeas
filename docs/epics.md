---
stepsCompleted: [1, 2, 3, 4]
status: 'complete'
completedAt: '2026-03-16'
inputDocuments:
  - 'docs/prd.md'
  - 'docs/architecture.md'
---

# SafetyProjectIdeas - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for SafetyProjectIdeas, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

**Knowledge Base Management (Track B — parallel KB construction):**
- FR1: Coordinator can define inclusion criteria specifying which AI Safety subfields, organizations, publication venues, and authors are in scope or explicitly excluded
- FR2: Coordinator can trigger an initial knowledge base build that autonomously discovers and crawls relevant AI Safety sources filtered by the defined inclusion criteria
- FR3: System presents a structured summary of discovered sources for coordinator approval before incorporating them into the knowledge base
- FR4: Coordinator can exclude specific items or tighten criteria during the approval workflow before incorporation
- FR5: Coordinator can trigger a knowledge base update that fetches new sources published since the last update, applying the same inclusion criteria and approval workflow *(moved to post-MVP)*
- FR6: Coordinator can edit inclusion criteria at any time to broaden or narrow what the pipeline tracks
- FR7: System detects and flags notable changes during updates: contradictions with existing knowledge, alignment with existing ideas, and coverage gaps *(moved to post-MVP)*
- FR8: Knowledge base is organized to support selective context retrieval — agents browse only the relevant subset for each task or conversation
- FR9: System can filter KB content by subfield, organization, recency, source code availability, or custom tags when providing context to pipeline stages or brainstorming
- FR10: Coordinator can browse, search, and query the knowledge base to understand its contents, coverage, and structure
- FR69: Knowledge base tracks source code availability as a per-paper attribute (available / partially available / not available / unknown). Papers with publicly available source code are significantly more valuable as a basis for extension work

**Knowledge Base Update Mechanisms (Post-MVP):**
- FR11: System supports push-based updates triggered by external notification subscriptions
- FR12: System can suggest new subscriptions based on knowledge base coverage gaps
- FR13: System supports pull-based updates that search broadly and catch blind spots
- FR14: Both update mechanisms feed through the same coarse-grained approval workflow
- FR15: System can process newsletters and curated digests to identify relevant items

**Knowledge Base Suggestions (Post-MVP):**
- FR16: System adds potentially relevant material to a persistent "suggestions list" for potential KB inclusion
- FR17: Coordinator can review the suggestions list — approving, rejecting, or discussing items

**Pipeline Execution (Track A — day 1):**
- FR18: Coordinator can run individual pipeline stages independently (Source, Generate, Filter/Score, Refine, Rank)
- FR19: Coordinator can run the full pipeline end-to-end (all stages in sequence)
- FR20: Coordinator can inspect the output of each stage before proceeding to the next
- FR21: Coordinator can intervene at any stage to correct, override, or redirect the pipeline
- FR22: System logs every pipeline stage's inputs, decisions, and outputs in structured format

**Idea Generation (Track A — day 1; FR23-FR24 multi-LLM deferred to post-MVP):**
- FR23: System generates ideas using multiple LLM providers in parallel via LiteLLM *(post-MVP — V1 uses Claude Code only)*
- FR24: System deduplicates ideas across LLM providers after parallel generation *(post-MVP)*
- FR25: System generates ideas as brief sketches (problem + direction + why it matters) for token efficiency
- FR26: System feeds only relevant context (abstracts, limitations) to generation — never full papers
- FR27: System uses cheaper models for simple generation tasks and more capable models for deeper analysis (model tiering)
- FR67: System generates ideas by proposing variations of existing experiments — modifying variables, populations, methodologies, or scope of published work
- FR68: System generates ideas by proposing follow-up experiments to explain observed effects

**Idea Evaluation & Scoring (Track A — day 1):**
- FR28: System evaluates ideas against configurable quality criteria with configurable weights
- FR29: System applies staged filtering — progressively more expensive evaluation, killing bad ideas early
- FR30: System scores each idea per criterion against a well-defined rubric with explicit reasoning for each score, ensuring consistency across scoring runs
- FR31: System applies threshold settings per filter stage to control which ideas advance
- FR32: Every scored idea includes cited papers with verifiable links or DOIs
- FR33: Every claim in an idea traces back to a specific source passage in the knowledge base
- FR34: System performs hybrid novelty assessment — evidence-based search (KB if available → web search always), hard gate on "already solved", derived novelty score feeds into configurable criteria with per-team weighting
- FR35: System actively verifies that cited papers exist and links/DOIs resolve

**Idea Refinement (Track A — day 1):**
- FR36: System auto-strengthens ideas with weak scores by attempting to improve the weakest dimensions
- FR37: System generates alternative framings for promising ideas (2-3 angles on the same core insight)
- FR38: System expands surviving ideas from brief sketches to include: research question, approach outline, and strength rationale

**Ranking & Output (Track A — day 1):**
- FR39: System produces a ranked list of ideas sorted by overall score as a markdown file
- FR40: Each final proposal includes: research question, approach, proposed first experiments, theory of impact chain, scores per criterion, and cited sources with verifiable links/DOIs
- FR41: Final proposals are concise enough for a human to scan 20+ proposals in a sitting
- FR42: System preserves the provenance of each idea (which KB sources contributed, which generation method produced it)

**Collaborative Brainstorming (Track A — day 1, secondary mode):**
- FR43: Coordinator can enter a collaborative chat mode to brainstorm ideas with the AI agent
- FR44: Coordinator can direct brainstorming by specifying topics, research areas, or specific problems
- FR45: Coordinator can combine topic direction with team constraints
- FR46: Coordinator can refine, iterate, and push back on ideas interactively
- FR47: Collaborative chat has access to the full knowledge base and pipeline memory
- FR48: Coordinator can pose open research questions and the system assesses whether they have been addressed in the literature

**Evaluate Existing Ideas (Track A — day 1):**
- FR49: Coordinator can submit an existing project idea for evaluation against the configured scoring criteria
- FR50: System assesses the novelty of submitted ideas against published work (same hybrid approach as FR34)
- FR51: System can refine and strengthen submitted ideas using the same Refine stage capabilities

**Configuration Management (Track A — day 1):**
- FR52: Coordinator can define and edit team profiles specifying team type, compute budget, technical skills, and custom criteria weights
- FR53: Coordinator can define and edit scoring criteria including definitions, rubrics (score levels anchored to concrete descriptions), default weights, and per-team-type weight overrides
- FR54: Coordinator can add custom scoring criteria beyond the default set
- FR55: Coordinator can configure pipeline settings including model assignments per stage
- FR56: All configuration is stored in human-editable YAML files
- FR57: Configuration persists across sessions

**Priority Areas (Post-MVP):**
- FR58: Coordinator can define organizational priority areas, and the pipeline can suggest new ones based on landscape analysis
- FR59: Priority areas are stored persistently and browsable

**Pipeline Memory & Learning (Post-MVP; minimal dedup in Track A):**
- FR60: System persists accumulated knowledge and learned preferences across sessions
- FR61: System remembers previous pipeline runs, user overrides, and configuration adjustments
- FR62: System applies accumulated knowledge to improve future pipeline runs
- FR63: System tracks previously generated ideas and ensures subsequent runs prioritize unexplored directions

**Idea Repository (FR64 MVP — persistence only; FR65 Post-MVP):**
- FR64: System maintains a persistent repository of all generated ideas across pipeline runs (ideas stored in `data/ideas/` and accumulate over time). Searchability is post-MVP
- FR65: Coordinator can provide retrospective feedback on past ideas and the system incorporates this into future scoring *(post-MVP)*

**Participant Profiles (from Architecture — Track A):**
- FR66: System can load pre-defined participant profiles (experience level, technical background, compute resources, time availability) and use them to tailor idea generation and brainstorming. Profiles stored as YAML. Falls back to conversational discovery if no profile exists

### NonFunctional Requirements

**Cost Efficiency:**
- NFR1: Pipeline minimizes external LLM API costs by using Claude Code for all tasks where it is sufficient, reserving external providers only for multi-LLM diversity in Generate stage or when specific model capabilities are required
- NFR2: Token usage is minimized at every stage through relevant-context-only feeding, progressive elaboration (cheap sketches first, expand only winners), and early killing of low-quality ideas
- NFR3: Model tiering assigns the cheapest capable model to each task

**Accuracy & Reliability:**
- NFR4: Zero tolerance for hallucinated citations — if a referenced paper cannot be verified to exist, it is excluded from the output entirely
- NFR5: Factual claims about existing research must trace back to a verifiable source. Novel insights generated by the pipeline are not required to trace to a single source
- NFR6: Novelty assessments must include evidence — confirming no existing work was found via both KB and broader search, or flagging as partially/fully addressed. The derived novelty score must be traceable to the underlying evidence and classification
- NFR7: Scoring reasoning must be explicit and auditable — no opaque scores without justification

**Integration:**
- NFR8: All external LLM calls go through LiteLLM provider abstraction (post-MVP)
- NFR9: Knowledge base sources are accessed through modular connectors that can be added or replaced independently
- NFR10: Architecture supports future integration with additional external systems without requiring core pipeline changes

**Maintainability & Modularity:**
- NFR11: Each pipeline stage is independently modifiable, testable, and replaceable without affecting other stages
- NFR12: All configurable parameters are externalized in YAML files, not hardcoded
- NFR13: Pipeline stages communicate through well-defined interfaces so internal implementation can change without breaking the pipeline flow

**Security:**
- NFR14: API keys for LLM providers and external services are stored securely and never logged or exposed in pipeline output

### Additional Requirements

**From Architecture — Starter Template & Project Initialization:**
- Custom project structure using `uv init` with Python 3.11+, pytest, ruff, pyyaml, pydantic, python-dotenv
- Claude Code skills (markdown) for pipeline orchestration; Python for programmatic components
- Skills invoke Python via `uv run python -m saim.<module>`
- Project initialization is the first implementation story

**From Architecture — Storage & Data Format:**
- KB storage: JSON files with `meta` and `sections` keys — section-level access, query module never returns all sections at once
- Inter-stage data: Hybrid markdown (creative content) + JSON (structured scores/reasoning)
- Pipeline run directories: `data/runs/<timestamp>/` with per-stage output and consolidated JSON log
- Run metadata (`run_meta.json`) captures git commit, parameters, and config snapshot for reproducibility
- KB document naming: `{source_venue}_{sanitized_title}_{date}.json`

**From Architecture — KB Build Pipeline (Token-Efficient):**
- Discovery via Semantic Scholar API and ArXiv API (arxiv.py)
- Automated parsing (zero LLM cost): Docling (IBM) for PDFs, LessWrong/AF GraphQL API for forum content, Trafilatura for research org blogs
- LLM extraction reads parsed sections only (not full papers) — generates frontmatter fields
- 800-paper shallow review CSV bootstrap from github.com/arb-consulting/shallow-review-2025

**From Architecture — Source Priority System:**
- Priority 1: Open problems lists — most actionable, ingested first
- Priority 2: Key papers — specific findings, concrete results
- Priority 3: Research agendas, org reports, regular papers, forum posts — broad context. Long documents (e.g., system cards) have only relevant subsections extracted and summarized by cheap models — summaries must capture all relevant results while excluding irrelevant content

**From Architecture — Configuration Validation:**
- All config access through Pydantic models — never raw YAML parsing in pipeline code
- Schemas: TeamProfile, ScoringCriteria, KBCriteria, PipelineSettings, ParticipantProfile

**From Architecture — Cross-Cutting Concerns:**
- Citation integrity verification at multiple pipeline stages
- Auditability: every stage logs inputs, decisions, outputs in structured format
- Confidence reporting on all outputs — always reported, never used for automated filtering
- Graceful KB degradation: all pipeline stages must function without KB, using Claude knowledge + web search
- Hybrid novelty assessment: evidence-based search (KB first pass, web mandatory second pass) → hard gate on "already solved" → derived novelty score feeds into configurable criteria with per-team weighting
- Persistent state across sessions (KB, pipeline memory, configuration)

**From Architecture — Credential Management:**
- `.env` + python-dotenv for API keys (Semantic Scholar, etc.)
- `.env` added to `.gitignore`
- No secrets in YAML config or pipeline output

**From Architecture — Infrastructure:**
- Local-only for MVP — runs entirely on local machine via Claude Code
- Git + GitHub for backup and version control
- No cloud compute, no CI/CD, no containers

**From Architecture — MVP Scope Adjustments:**
- FR5, FR7 moved to post-MVP (no automated KB updates for MVP)
- FR11-FR17 moved to post-MVP (KB update mechanisms, suggestions)
- MVP KB scope: FR1-FR4, FR6, FR8-FR10, FR69
- Three user types: Guido (power user), external users with profile, external users without profile

### FR Coverage Map

FR1: Epic 7 - KB inclusion criteria definition
FR2: Epic 7 - KB initial build with autonomous discovery
FR3: Epic 7 - Structured summary for coordinator approval
FR4: Epic 7 - Exclude items / tighten criteria during approval
FR6: Epic 7 - Edit inclusion criteria at any time
FR8: Epic 7 - Selective context retrieval from KB
FR9: Epic 7 - Filter KB by subfield, org, venue, recency, source code, tags
FR10: Epic 7 - Browse, search, and query KB
FR18: Epic 3 - Run individual pipeline stages independently
FR19: Epic 8 - Run full pipeline end-to-end
FR20: Epic 3 - Inspect stage output before proceeding
FR21: Epic 3 - Intervene at any stage
FR22: Epic 3 - Log every stage's inputs, decisions, outputs
FR25: Epic 3 - Generate ideas as brief sketches
FR26: Epic 3 - Feed only relevant context to generation
FR27: Epic 3 - Model tiering for generation tasks
FR28: Epic 4 - Evaluate ideas against configurable criteria
FR29: Epic 4 - Staged filtering, kill bad ideas early
FR30: Epic 4 - Score per criterion with explicit reasoning
FR31: Epic 4 - Threshold settings per filter stage
FR32: Epic 4 - Cited papers with verifiable links/DOIs
FR33: Epic 4 - Claims trace to source passages
FR34: Epic 4 - Hybrid novelty assessment (KB if available → web always → hard gate → derived score)
FR35: Epic 4 - Verify cited papers exist
FR36: Epic 5 - Auto-strengthen ideas with weak scores
FR37: Epic 5 - Alternative framings for promising ideas
FR38: Epic 5 - Assemble full proposals in Refine (question, approach, experiments, impact chain, citations)
FR39: Epic 5 - Re-score full proposals and produce ranked list sorted by overall score
FR40: Epic 5 - Full proposal content assembled in Refine, carried through Rank
FR41: Epic 5 - Concise proposals for human scanning
FR42: Epic 5 - Preserve provenance of each idea
FR43: Epic 6 - Collaborative chat mode for brainstorming
FR44: Epic 6 - Direct brainstorming by topic/area/problem
FR45: Epic 6 - Combine topic direction with team constraints
FR46: Epic 6 - Refine, iterate, push back interactively
FR47: Epic 6 - Chat accesses KB and pipeline memory
FR48: Epic 6 - Assess open research questions against literature
FR49: Epic 6 - Submit existing idea for evaluation
FR50: Epic 6 - Hybrid novelty assessment for submitted ideas (same approach as FR34)
FR51: Epic 6 - Refine/strengthen submitted ideas
FR52: Epic 1 - Define/edit team profiles
FR53: Epic 1 - Define/edit scoring criteria with weights
FR54: Epic 1 - Add custom scoring criteria
FR55: Epic 1 - Configure pipeline settings
FR56: Epic 1 - YAML config files
FR57: Epic 1 - Configuration persists across sessions
FR64: Epic 5 - Persistent idea repository (storage only for MVP)
FR66: Epic 1 - Participant profiles for tailored generation
FR67: Epic 3 - Generate variations of existing experiments
FR68: Epic 3 - Generate follow-up experiments to explain observed effects
FR69: Epic 7 - Track source code availability per paper

**Post-MVP FRs (not mapped to MVP epics):**
FR5, FR7, FR11-FR17, FR23-FR24, FR58-FR59, FR60-FR63, FR65

## Epic List

### Epic 1: Project Foundation & Team Configuration
Coordinator can set up the system and configure it for BAISH's team types, scoring criteria, and participant profiles — making it ready for idea generation and brainstorming.
**FRs covered:** FR52, FR53, FR54, FR55, FR56, FR57, FR66

### Epic 2: Research Landscape Discovery
Coordinator can map the AI Safety research landscape — discovering open problems lists, research agendas, key sources, and which categories to prioritize for idea generation.
**FRs covered:** (Supports FR25-FR27 context; `/research-landscape` skill)

### Epic 3: Idea Generation
Coordinator can auto-generate a batch of research idea sketches balanced across categories, using Claude's AI Safety knowledge + active web search, with pipeline stage logging and inspection.
**FRs covered:** FR18, FR20, FR21, FR22, FR25, FR26, FR27, FR67, FR68

### Epic 4: Idea Scoring & Hybrid Novelty Assessment
Coordinator can evaluate generated ideas against configurable criteria with explicit reasoning, run the hybrid novelty assessment (evidence-based search → hard gate on "already solved" → derived novelty score with per-team weighting), and verify all citations.
**FRs covered:** FR28, FR29, FR30, FR31, FR32, FR33, FR34, FR35

### Epic 5: Idea Refinement, Proposal Assembly & Ranked Output
Coordinator receives auto-strengthened ideas assembled into full proposals (research question, approach, first experiments, impact chain, cited sources) in the Refine stage, then Rank re-scores these complete proposals and produces a sorted, filtered output that persists across runs.
**FRs covered:** FR36, FR37, FR38, FR39, FR40, FR41, FR42, FR64

### Epic 6: Collaborative Brainstorming & Idea Evaluation
Coordinator (or external users) can interactively brainstorm research directions, evaluate existing ideas against criteria, and refine them — with participant profile support for tailored generation.
**FRs covered:** FR43, FR44, FR45, FR46, FR47, FR48, FR49, FR50, FR51

### Epic 7: Knowledge Base Construction
Coordinator can build a structured, queryable AI Safety knowledge base (starting with 800-paper CSV bootstrap) that enriches all pipeline stages and brainstorming with grounded context.
**FRs covered:** FR1, FR2, FR3, FR4, FR6, FR8, FR9, FR10, FR69

### Epic 8: Full Pipeline Integration
Coordinator can run the complete pipeline end-to-end with one command, producing a fully scored, refined, and ranked set of research proposals with full auditability.
**FRs covered:** FR19

**Parallelization:**
- Track A (Epics 2-6): Sequential within track, each stage builds on previous
- Track B (Epic 7): Fully parallel with Track A — KB enriches Track A progressively
- Epic 1: Prerequisite for both tracks
- Epic 8: Convergence point — requires Epics 3-5, benefits from Epic 7

## Epic 1: Project Foundation & Team Configuration

Coordinator can set up the system and configure it for BAISH's team types, scoring criteria, and participant profiles — making it ready for idea generation and brainstorming.

### Story 1.1: Project Initialization, Config Schemas & Default Configuration

As a coordinator,
I want the project set up with proper structure, validated configuration schemas, and sensible defaults for BAISH's teams,
So that the system is ready for idea generation from day one.

**Acceptance Criteria:**

**Given** no project structure exists
**When** the developer initializes the project
**Then** the following structure is created:
- `src/saim/` Python package with subpackages: `config/`, `kb/`, `connectors/`, `pipeline/`, `verification/`
- `data/kb/`, `data/output/`, `data/runs/`, `data/ideas/` directories
- `config/` directory with `participants/` subdirectory
- `tests/` directory mirroring `src/` structure
- `.claude/commands/` directory for Claude Code skills
**And** `pyproject.toml` is configured with dependencies (`pytest`, `ruff`, `pyyaml`, `pydantic`, `python-dotenv`), ruff config, and project metadata
**And** `.env.example` documents required environment variables
**And** `.gitignore` excludes `.env`, `__pycache__/`, `.venv/`, `data/runs/`
**And** `src/saim/constants.py` and `src/saim/utils.py` exist
**And** `README.md` exists with project overview and setup instructions
**And** `LICENSE` exists with MIT license
**And** `uv sync` succeeds without errors

**Given** the project structure exists
**When** Pydantic models are defined in `src/saim/config/schemas.py`
**Then** the following models exist: `TeamProfile`, `ScoringCriteria`, `KBCriteria`, `PipelineSettings`, `ParticipantProfile`
**And** `TeamProfile` includes: team name, type (mentor_novice / solo_novice / experienced_group), compute_budget, technical_skills, custom criteria weights
**And** `ScoringCriteria` includes: criteria name, description, default weight, per-team-type weight overrides
**And** `PipelineSettings` includes: model assignments per stage, threshold settings per filter stage
**And** `ParticipantProfile` includes: name, experience_level, technical_background, compute_resources, time_availability
**And** `KBCriteria` includes: subfields_in_scope, organizations, authors, exclusions

**Given** Pydantic models are defined
**When** `load_config()` is called from `src/saim/config/loader.py`
**Then** it loads and validates all YAML files from `config/` directory
**And** returns validated Pydantic model instances
**And** raises clear error messages if YAML is malformed or missing required fields
**And** loads `.env` via python-dotenv for API keys

**Given** no config files exist yet
**When** the developer creates default config files
**Then** `config/teams.yaml` contains BAISH's three team profiles (mentor_novice, solo_novice, experienced_group)
**And** `config/criteria.yaml` contains the four default scoring criteria (theory_of_impact, low_compute, accessible_complexity, narrow_scope) each with a well-defined rubric anchoring score levels to concrete descriptions, default weights, and per-team-type overrides, plus a derived "novelty" criterion whose score comes from the hybrid novelty assessment (FR34) — configurable weight per team type but score is not manually assigned
**And** `config/pipeline.yaml` contains default model assignments and threshold settings
**And** `config/kb-criteria.yaml` contains default inclusion criteria for AI Safety subfields
**And** all config files are human-readable and editable YAML

### Story 1.2: Configuration Management Skill & Participant Profiles

As a coordinator,
I want to manage team profiles, scoring criteria, pipeline settings, and participant profiles through conversation or direct YAML editing,
So that the pipeline is calibrated to BAISH's teams and individual researchers.

**Acceptance Criteria:**

**Given** the config schemas and loader from Story 1.1 exist
**When** the coordinator invokes `/configure-teams`
**Then** the skill displays current team profiles, scoring criteria, and the current default participant (if set)
**And** the coordinator can add, edit, or remove team profiles through conversation
**And** the coordinator can modify scoring criteria weights per team type
**And** the coordinator can add custom scoring criteria beyond the default set (FR54)
**And** the coordinator can configure pipeline settings including model assignments per stage (FR55)
**And** the coordinator can set or clear the default participant (used when no participant is specified at pipeline runtime)
**And** all changes are written back to the appropriate YAML config files
**And** changes are validated against Pydantic schemas before saving
**And** updated config persists across sessions (FR57)

**Given** a participant profile YAML file is created in `config/participants/<name>.yaml`
**When** the profile is loaded
**Then** it is validated against the ParticipantProfile Pydantic schema
**And** contains: name, experience_level, technical_background (list of skills), compute_resources, time_availability

**Given** a participant profile exists for a user
**When** an idea generation or brainstorming skill is invoked
**Then** the system loads the matching participant profile automatically and uses it to tailor generation

**Given** no participant profile exists for a user
**When** an idea generation or brainstorming skill is invoked
**Then** the system falls back to conversational discovery, guiding the user through describing their constraints

## Epic 2: Research Landscape Discovery

Coordinator can map the AI Safety research landscape — discovering open problems lists, research agendas, key sources, and active subfields — to inform which areas to target for idea generation.

### Story 2.1: Research Landscape Skill

As a coordinator,
I want to discover and map the AI Safety research landscape before generating ideas,
So that I know which subfields and open problems exist and can decide which areas to target for idea generation.

**Acceptance Criteria:**

**Given** the project foundation from Epic 1 exists
**When** the coordinator invokes `/research-landscape`
**Then** the skill searches for open problems lists, research agendas, and key sources across AI Safety using Claude's knowledge + active web search
**And** identifies active AI Safety subfields and maps what open problems and research directions exist in each
**And** identifies key organizations, authors, and important source documents (open problems lists, research agendas)
**And** outputs a structured markdown summary to `data/output/` with subfields, open problems per subfield, key sources, and organizations
**And** the coordinator can review and select which subfields to target for subsequent idea generation

**Given** a landscape summary has been generated
**When** the coordinator runs `/generate-ideas` (Epic 3)
**Then** the generation skill can reference the landscape summary to generate ideas covering all coordinator-specified subfields heavily

## Epic 3: Idea Generation

Coordinator can auto-generate a batch of research idea sketches covering all specified subfields heavily, using Claude's AI Safety knowledge + active web search, with pipeline stage logging and inspection.

### Story 3.1: Idea Generation Skill & Pipeline Stage Infrastructure

As a coordinator,
I want to auto-generate a batch of research idea sketches covering all my specified subfields heavily,
So that I get thorough coverage of candidate project ideas across every area I care about.

**Acceptance Criteria:**

**Given** the project config exists (team profiles, scoring criteria)
**When** the coordinator invokes `/generate-ideas`
**Then** the system creates a pipeline run directory at `data/runs/<timestamp>/` with `run_meta.json` capturing git commit, parameters, and config snapshot
**And** the coordinator can specify which subfields to target for generation
**And** the generation stage can be invoked independently via `/generate-ideas`, just as each other pipeline stage (`/score-ideas`, `/refine-ideas` for refinement + proposal assembly, `/rank-ideas` for re-scoring + sorting) can be invoked independently (FR18)
**And** generates idea sketches as brief descriptions (problem + direction + why it matters) covering all specified subfields heavily (FR25)
**And** uses generation strategies including: novel directions, variations of existing experiments (FR67), and follow-up experiments to explain observed effects (FR68)
**And** feeds only relevant context (abstracts, limitations) to generation — never full papers (FR26)
**And** uses cheaper models for simple generation tasks and more capable models for deeper analysis (FR27)
**And** each idea sketch is written as a markdown file in `data/runs/<timestamp>/generate/`
**And** the system logs inputs, decisions, and outputs in structured JSON format (FR22)
**And** confidence is reported on each generated idea

**Given** a generation run has completed
**When** the coordinator inspects the output
**Then** they can review individual idea sketches before proceeding to scoring (FR20)
**And** they can intervene to add, remove, or redirect ideas (FR21)

**Given** the KB is not yet populated
**When** idea generation runs
**Then** the system functions using Claude's native AI Safety knowledge + active web search (graceful KB degradation)

**Given** the KB has been populated (Epic 7)
**When** idea generation runs
**Then** the system queries the KB via the query module for relevant context to enrich generation

## Epic 4: Idea Scoring & Hybrid Novelty Assessment

Coordinator can evaluate generated ideas against configurable criteria with explicit reasoning, run the hybrid novelty assessment (evidence-based search → hard gate on "already solved" → derived novelty score with per-team weighting), and verify all citations.

### Story 4.1: Scoring, Novelty & Citation Verification Skill

As a coordinator,
I want generated ideas scored against my configured criteria with novelty assessment and verified citations,
So that I can trust the evaluations and focus review time on the most promising ideas.

**Acceptance Criteria:**

**Given** idea sketches exist from a generation run (Epic 3)
**When** the coordinator invokes `/score-ideas`
**Then** the system evaluates each idea against the configured scoring criteria with configurable weights (FR28)
**And** scores each idea per criterion against the criterion's rubric with explicit reasoning for each score (FR30)
**And** applies staged filtering — progressively more expensive evaluation, killing bad ideas early (FR29)
**And** applies threshold settings per filter stage to control which ideas advance (FR31)
**And** outputs scored ideas as JSON files in `data/runs/<timestamp>/filter_score/`

**Given** an idea is being scored
**When** the hybrid novelty assessment runs
**Then** the system checks the KB first if available (fast, cheap), then always searches the web — ArXiv, Semantic Scholar, Google Scholar (FR34)
**And** classifies each idea as: novel / partially addressed / already solved
**And** includes evidence for the assessment (NFR6)
**And** if classified as "already solved", the idea is eliminated immediately (hard gate) — no further scoring or refinement regardless of other criteria scores
**And** if classified as "novel" or "partially addressed", the classification is converted to a derived "novelty" score that feeds into the configurable scoring criteria
**And** the novelty score is weighted per team type (e.g., low for novice teams doing replication studies per FR67, high for experienced groups)
**And** reports confidence in the novelty assessment

**Given** an idea references papers
**When** citation verification runs
**Then** every cited paper has a verifiable link or DOI (FR32)
**And** the system actively verifies that cited papers exist and links/DOIs resolve (FR35) — using the cheapest possible method (API lookups via Semantic Scholar/CrossRef, not LLM calls) and only falling back to cheap models when programmatic verification is insufficient
**And** papers that cannot be verified are excluded from the output entirely (NFR4)
**And** factual claims trace back to specific source passages (FR33)

**Given** scoring is complete
**When** the coordinator reviews results
**Then** all scoring reasoning is explicit and auditable — no opaque scores (NFR7)
**And** confidence is reported but never used for automated filtering — human decides what to act on

## Epic 5: Idea Refinement & Ranked Output

Coordinator receives auto-strengthened ideas assembled into full proposals in the Refine stage, then Rank re-scores and produces a sorted, filtered output that persists across runs.

### Story 5.1: Refinement, Proposal Assembly, Ranking & Persistent Idea Storage

As a coordinator,
I want promising ideas auto-strengthened and assembled into full proposals, then re-scored and ranked so I can scan them efficiently and they accumulate across runs,
So that I get actionable research project proposals ranked on complete information and build a growing library of ideas over time.

**Acceptance Criteria:**

**Given** scored ideas exist from Epic 4
**When** the coordinator invokes `/refine-ideas`
**Then** the system auto-strengthens ideas with weak scores by improving the weakest dimensions (FR36)
**And** generates 2-3 alternative framings for promising ideas (FR37)
**And** assembles surviving ideas into full proposals including: research question, approach outline, proposed first experiments, theory of impact chain, strength rationale, and cited sources with verifiable links/DOIs (FR38, FR40)
**And** outputs full proposals as markdown files in `data/runs/<timestamp>/refine/`
**And** reports confidence that refinement improved each idea

**Given** full proposals exist from Refine
**When** the coordinator invokes `/rank-ideas`
**Then** the system re-scores full proposals against criteria — now with richer signal from complete proposals (first experiments, impact chain) — and produces a ranked list sorted by overall score as a markdown file (FR39)
**And** proposals are concise enough for a human to scan 20+ in a sitting (FR41)
**And** the provenance of each idea is preserved — which KB sources contributed, which generation method produced it (FR42)
**And** ranked output is written to `data/runs/<timestamp>/rank/` and copied to `data/output/`

**Given** a ranking run completes
**When** final proposals are produced
**Then** they are also copied to `data/ideas/` for persistent accumulation across pipeline runs (FR64)
**And** subsequent generation runs can reference `data/ideas/` to avoid repeating previously generated ideas

## Epic 6: Collaborative Brainstorming & Idea Evaluation

Coordinator (or external users) can interactively brainstorm research directions, evaluate existing ideas against criteria, and refine them — with participant profile support.

### Story 6.1: Brainstorming & Idea Evaluation Skills

As a coordinator or external researcher,
I want to interactively brainstorm AI Safety research directions and evaluate existing ideas against the pipeline's criteria,
So that I can explore specific areas in depth and assess ideas I bring from outside the pipeline.

**Acceptance Criteria:**

**Given** the project config and optionally the KB exist
**When** the coordinator invokes `/brainstorm`
**Then** the system enters collaborative chat mode for idea exploration (FR43)
**And** the coordinator can direct brainstorming by specifying topics, research areas, or specific problems (FR44)
**And** the coordinator can combine topic direction with team constraints (e.g., "interpretability ideas for a novice with one A100") (FR45)
**And** the coordinator can refine, iterate, and push back on ideas interactively (FR46)
**And** the chat has access to the KB and pipeline memory when available (FR47)
**And** the coordinator can pose open research questions and the system assesses whether they have been addressed in the literature (FR48)

**Given** a participant profile exists in `config/participants/`
**When** the brainstorming or evaluation skill is invoked
**Then** the system loads the profile automatically and tailors generation to the participant's constraints (FR66)

**Given** no participant profile exists
**When** brainstorming is invoked
**Then** the system guides the user through describing their constraints conversationally

**Given** the coordinator has an existing idea
**When** they invoke `/evaluate-idea`
**Then** the system evaluates the submitted idea against the configured scoring criteria (FR49)
**And** assesses novelty against published work using the same hybrid novelty assessment flow — evidence-based search, hard gate on "already solved", derived novelty score (FR50)
**And** can refine and strengthen the idea using auto-strengthen and alternative framing (FR51)

## Epic 7: Knowledge Base Construction

Coordinator can build a structured, queryable AI Safety knowledge base (starting with 800-paper CSV bootstrap) that enriches all pipeline stages and brainstorming with grounded context.

### Story 7.1: CSV Bootstrap, Section Extraction & KB Query Module

As a coordinator,
I want to bootstrap the knowledge base from the 800-paper shallow review with full section extraction and query it for relevant context,
So that pipeline stages and brainstorming can draw on structured AI Safety research from day one of Track B.

**Acceptance Criteria:**

**Given** the 800-paper shallow review CSV and scraped HTML (`.html.zst`) from github.com/arb-consulting/shallow-review-2025 are available
**When** the ingestion script runs
**Then** CSV fields are mapped to KB JSON schema: title→title, authors→authors, kind→source_type, categories→subfields/tags, summary→key_findings, ai_safety_relevance→priority
**And** sections are extracted from the scraped HTML using Trafilatura (for blog sources) and from linked PDFs using Docling where available
**And** LLM extraction (using cheap models) reads parsed sections to generate frontmatter fields: key_findings, limitations, relevance_notes, subfield/tag classification
**And** each paper is stored as a JSON file in `data/kb/` following the naming convention `{source_venue}_{sanitized_title}_{date}.json`
**And** each JSON file has `meta` and `sections` keys per the architecture spec
**And** source_code_available is populated where detectable (FR69)
**And** the existing taxonomy (7 AI Safety categories) provides initial subfield classification

**Given** the KB is populated
**When** `kb.query()` is called from `src/saim/kb/query.py`
**Then** it loads and filters JSON meta from KB files
**And** supports filtering by subfield, organization, recency, tags, priority, and source_code_available (FR9)
**And** returns metadata by default; specific sections only when caller explicitly requests them via `sections=[]` parameter
**And** never returns all sections at once — caller always specifies which sections they need
**And** the coordinator can browse, search, and query the KB to understand its contents (FR10)

### Story 7.2: Full KB Build Pipeline with Source Connectors

As a coordinator,
I want to build the knowledge base from live sources (ArXiv, Semantic Scholar, Alignment Forum, LessWrong) with inclusion criteria and approval workflow,
So that the KB stays comprehensive and grounded in current AI Safety research beyond the initial CSV bootstrap.

**Acceptance Criteria:**

**Given** the coordinator has defined inclusion criteria in `config/kb-criteria.yaml` (FR1)
**When** the coordinator invokes `/build-kb`
**Then** the system autonomously discovers and crawls relevant AI Safety sources filtered by inclusion criteria (FR2)
**And** uses source connectors: Semantic Scholar API for paper search and metadata, ArXiv API (arxiv.py) for ArXiv papers, LessWrong/Alignment Forum GraphQL API for forum posts, Trafilatura for research org blog posts
**And** uses document parsers: Docling for PDF section extraction, Trafilatura for HTML from blogs
**And** applies the source priority system: Priority 1 (open problems lists), Priority 2 (key papers), Priority 3 (research agendas, org reports, regular papers, forum posts)
**And** for long documents (e.g., system cards 150+ pages), only relevant subsections are extracted and summarized by cheap models — summaries must capture all relevant results (safety evaluations, capability assessments, risk findings) while excluding irrelevant content
**And** automated parsing (zero LLM cost) extracts sections first; LLM extraction using cheap models reads parsed sections only to generate frontmatter fields (key_findings, limitations, relevance_notes, subfield/tag classification)

**Given** discovery is complete
**When** the system presents results
**Then** it shows a structured summary of discovered sources for coordinator approval before incorporation (FR3)
**And** the coordinator can exclude specific items or tighten criteria during the approval workflow (FR4)
**And** approved sources are stored as JSON files in `data/kb/` following the KB document schema

**Given** the KB exists
**When** the coordinator wants to adjust scope
**Then** they can edit inclusion criteria at any time to broaden or narrow what the pipeline tracks (FR6)
**And** the KB is organized to support selective context retrieval (FR8)

## Epic 8: Full Pipeline Integration

Coordinator can run the complete pipeline end-to-end with one command, producing a fully scored, refined (with full proposal assembly), and ranked set of research proposals with full auditability.

### Story 8.1: End-to-End Pipeline Orchestration

As a coordinator,
I want to run the entire pipeline (Source → Generate → Filter/Score → Refine/Assemble → Rank) with a single command,
So that I can produce a complete set of ranked research proposals without manually invoking each stage.

**Acceptance Criteria:**

**Given** all pipeline stages from Epics 3-5 are implemented and the project config exists
**When** the coordinator invokes `/run-pipeline`
**Then** the pipeline orchestrator creates a run directory at `data/runs/<timestamp>/`
**And** executes all stages in sequence: source context selection → generate → filter/score → refine → rank (FR19)
**And** each stage reads from the previous stage's output directory and writes to its own
**And** a single consolidated JSON log captures the full pipeline trace with timestamped decisions at each stage
**And** `run_meta.json` records git commit, parameters, and config snapshot for reproducibility
**And** final ranked output is copied to `data/output/` and `data/ideas/`

**Given** the KB is available
**When** the pipeline runs
**Then** pipeline stages query the KB via the query module for enriched context

**Given** the KB is not available
**When** the pipeline runs
**Then** all stages function using Claude's native knowledge + active web search (graceful degradation)

**Given** a pipeline run completes
**When** the coordinator reviews results
**Then** every stage's inputs, decisions, and outputs are auditable via the consolidated log (FR22)
**And** confidence is reported throughout but never used for automated filtering
