---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
inputDocuments:
  - 'docs/analysis/research/domain-ai-safety-open-problems-research-2026-03-02.md'
  - 'docs/analysis/research/technical-ai-safety-pipeline-research-2026-03-03.md'
  - 'docs/analysis/brainstorming-session-2026-02-12.md'
documentCounts:
  briefs: 0
  research: 2
  brainstorming: 1
  projectDocs: 0
workflowType: 'prd'
lastStep: 11
project_name: 'SafetyProjectIdeas'
user_name: 'guido'
date: '2026-03-03'
---

# Product Requirements Document - SafetyProjectIdeas

**Author:** guido
**Date:** 2026-03-03

## Executive Summary

SafetyProjectIdeas is an AI-powered research idea generation pipeline for BAISH (Buenos Aires AI Safety Hub). BAISH is building new research teams and needs a systematic way to discover, evaluate, and curate AI Safety research project ideas — a process that is currently entirely ad hoc.

The pipeline automates the labor-intensive work of scanning the AI Safety research landscape — open problems lists, research agendas, recent papers, system cards, forums — and generates candidate project ideas that are scored against five quality criteria: soundness, relevance, theory of impact, low compute requirements, and accessible technical complexity. Ideas are calibrated to three team configurations: mentor-guided novice projects, individual novice projects with mentorship, and experienced researcher groups.

Beyond automation, SafetyProjectIdeas provides an always-up-to-date AI research partner that BAISH team leads can brainstorm with — one that has internalized the current state of AI Safety research and can surface connections and directions that manual curation would miss.

### What Makes This Special

- **From ad hoc to systematic:** Replaces an unstructured process with a 7-stage pipeline (Source, Generate, Filter/Score, Refine, Rank, Monitor, Learn) designed for token efficiency and modularity
- **Always-current research awareness:** Continuous monitoring of the AI Safety landscape means the pipeline never goes stale
- **Team-aware recommendations:** Ideas are matched to team capability profiles, ensuring feasibility for BAISH's specific team configurations
- **Impact maximization:** Every idea requires an explicit impact chain ("This research leads to X, which reduces risk Y, because Z"), focusing BAISH's limited resources on highest-leverage directions
- **Human-AI collaboration:** Two modes — autonomous pipeline for batch generation, and collaborative chat for directed brainstorming with domain experts

## Project Classification

**Technical Type:** cli_tool / developer_tool (Claude Code skills + LiteLLM orchestration)
**Domain:** Scientific research tooling (AI Safety)
**Complexity:** Medium
**Project Context:** Greenfield - new project
**Scope:** BAISH-specific (extensibility to other orgs is out of scope)

The pipeline is built as Claude Code skills with LiteLLM as the provider abstraction gateway, enabling model tiering across pipeline stages. Each stage is modular and independently modifiable. The system is designed for a single organization's workflow but with clean enough boundaries to extend later.

## Success Criteria

### User Success

- **Discovery of non-obvious directions:** Users find research ideas they wouldn't have discovered on their own — the "aha!" moment when the pipeline surfaces a valuable, unexpected direction
- **Collaborative refinement:** Ideas aren't just handed to users — they're co-developed through human-AI dialogue where the user's domain expertise shapes the output
- **Team-appropriate proposals:** Ideas are calibrated to the user's team configuration and constraints, producing actionable project proposals ready to pursue
- **Confidence in coverage:** Users trust that the pipeline has scanned the relevant landscape comprehensively, so they're not missing important directions

### Business Success

- **Primary metric:** Number of pipeline-generated ideas that are good enough to actually pursue as research projects
- **Capacity target:** Pipeline should produce sufficient quality ideas to staff up to ~15 individual projects and ~4 team projects (upper bound)
- **Secondary signal:** Downstream project outcomes (tracked but not used as primary metric due to confounding factors unrelated to idea quality)

### Technical Success

- **Output quality over operational reliability:** The system should produce high-quality, well-scored ideas even if it requires some manual intervention — quality is non-negotiable, automation is nice-to-have
- **Multi-LLM diversity:** Generation phase calls multiple LLM providers in parallel via LiteLLM, producing diverse idea pools that are then refined and deduplicated
- **Configurability:** Team profiles and scoring criteria are configurable — what defines a "good project" varies by team type (compute constraints matter for some teams, not others)
- **Auditability:** Every pipeline stage logs inputs, decisions, and outputs so users can understand why ideas were scored/filtered the way they were
- **Citation integrity:** Every referenced paper is verifiable (link or DOI), every claim traces to a specific source passage

### Measurable Outcomes

| Metric | Target | How Measured |
|---|---|---|
| Ideas good enough to pursue | Sufficient to staff ~19 projects | User acceptance of pipeline output |
| Non-obvious discovery rate | Users report finding ideas they wouldn't have found manually | User feedback after pipeline runs |
| Scoring accuracy | User agrees with pipeline scoring in >70% of cases | User override rate in Filter/Score stage |
| Source coverage | Pipeline monitors all major AI Safety sources (open problems lists, key orgs, ArXiv, Alignment Forum, LessWrong) | Source coverage audit |
| Citation accuracy | 100% of referenced papers are verifiable | Automated verification check |

## Product Scope

### MVP - Minimum Viable Product

- **Source → Generate → Filter/Score → Refine → Rank flow** for a complete pipeline run
- One-liner hypothesis generation with staged filtering against configurable quality criteria
- Relevant-context-only feeding (abstract + limitations, not full papers)
- Multi-LLM parallel generation via LiteLLM with deduplication
- **Model tiering** — cheaper models for quick screens, capable models for deep analysis
- **Refine/Iterate stage** with auto-strengthen and alternative framing
- **Basic ranking** — scored and sorted output list of ideas
- Collaborative chat interface for human-AI co-generation and refinement
- Configurable team profiles (mentor+novice, solo novice, experienced group)
- Configurable scoring criteria and weights per team type
- **Knowledge base creation and update mechanism** — build, persist, and manually update the research knowledge base the pipeline draws from
- **Persistent memory** — pipeline accumulates knowledge and applies it across sessions
- Basic pipeline logging for auditability
- Citation verification for referenced papers

### Growth Features (Post-MVP)

- **Advanced ranking** with Pareto frontier and tier system (pursue now / promising / park)
- **Continuous paper scanning** — automated monitoring of ArXiv, Alignment Forum, LessWrong, conferences
- Idea invalidation/strengthening based on new publications
- Source quality tracking (which sources produce the best ideas over time)
- Filter calibration from user feedback
- Graveyard review — periodic resurfacing of killed ideas for human spot-check
- **Public chat interface** — anyone can use the chatbot to generate ideas fitting their specific needs

### Vision (Future)

- **Learn stage** — blind spot audits, automated feedback loop integration
- Landscape shift detection (org pivots, new agendas)
- Extensibility to other AI Safety research organizations beyond BAISH

## User Journeys

### Journey 1: Guido — From Ad Hoc to Systematic Research Agenda

Guido is the Research Coordinator at BAISH, a young AI Safety hub in Buenos Aires building its first wave of research teams. He has ~19 project slots to fill — 15 individual projects for grad students (some with mentors, some solo with guidance) and 4 team projects for more experienced groups. Until now, finding good project ideas has been entirely ad hoc: reading papers when he has time, following conversations on the Alignment Forum, occasionally stumbling on something promising. He knows he's missing important directions, but the landscape is too vast to cover manually.

One morning, Guido decides it's time to run SafetyProjectIdeas for real. He starts by updating the knowledge base — the pipeline already has persistent memory from previous sessions, so it builds on what it already knows. He kicks off a full pipeline run. Multiple LLMs generate ideas in parallel — Claude, GPT, Gemini — each bringing a different creative angle to the same source material. The pipeline deduplicates, scores each idea against his configured criteria, auto-strengthens the promising ones, and produces a ranked list. Guido scans the output and immediately spots three ideas he never would have found on his own: a novel approach to evaluating deceptive alignment in tool-using agents, a low-compute replication study that could challenge a key assumption in the scalable oversight literature, and a cross-pollination between mechanistic interpretability and developmental psychology.

But the real value comes next. He opens the collaborative chat and says: "I have a grad student with strong NLP experience but no safety background, and she has access to a single A100 for three months. What from this list could work for her?" The agent refines its recommendations, adjusting for compute constraints and technical accessibility, and proposes a scoped project with a clear methodology. Guido iterates on it, pushes back on the impact framing, and together they shape a project proposal ready to present.

Over the next weeks, Guido repeats this for different team configurations. By the end, he has a full research agenda — 19 staffed projects, each with a clear rationale, and the confidence that the pipeline scanned sources he never would have reached alone.

### Journey 2: Guido — Configuring the Pipeline for Different Teams

Before running his first real pipeline cycle, Guido needs to set up SafetyProjectIdeas for BAISH's specific needs. He opens the configuration and defines three team profiles:

- **Mentor+Novice:** Low compute ceiling, accessible complexity required, mentor provides domain guidance. Weight "accessible complexity" and "low compute" heavily. De-prioritize ideas requiring deep safety background.
- **Solo Novice with Guidance:** Similar constraints but even more emphasis on clear methodology — the student needs to be able to follow a well-defined research plan with periodic mentor check-ins.
- **Experienced Group:** Compute is less of a constraint, technical depth is welcome, but theory of impact must be exceptionally strong — these projects should move the needle on real safety problems.

He also adjusts the scoring criteria. For the experienced group, he removes the "low compute" criterion entirely and doubles the weight on "theory of impact." For the novice profiles, he adds a custom criterion: "learning value" — does this project teach the researcher important safety concepts?

He saves the configuration and runs a test batch. The output looks different for each profile — the experienced group gets ambitious multi-month projects, while the novice profiles get focused, well-scoped studies. Guido tweaks the weights after seeing the first results, and the pipeline remembers his adjustments for next time.

### Journey 3: Guido — Bootstrapping and Maintaining the Knowledge Base

Before SafetyProjectIdeas can generate anything useful, it needs to know the field. Guido starts by defining the inclusion criteria for the knowledge base: which subfields of AI Safety are in scope, which organizations to track, which publication venues matter, and any explicit exclusions (e.g., "no AI governance policy papers, only technical safety"). These criteria become the persistent filter for all knowledge base operations.

He then runs the initial build. The pipeline autonomously identifies and crawls the major AI Safety sources — open problems lists, research agendas, ArXiv papers, Alignment Forum and LessWrong posts, conference proceedings — using its understanding of the field, filtered through Guido's criteria. Before incorporating anything, it presents a structured summary for approval: "I found 340 papers, 85 forum posts, 12 organizational agendas, and 45 active authors matching your criteria. Here's a breakdown by subfield and source — should I incorporate all of this, or do you want to adjust?" Guido reviews the summary, spots a cluster of papers on AI ethics that don't match BAISH's technical focus, tightens the criteria to exclude that cluster, and approves the rest. The system builds the comprehensive baseline.

Weeks later, Guido runs the update command. The pipeline identifies what's new since the last update, applies the same inclusion criteria, and presents a summary before incorporating: "23 new papers, 8 forum posts, 1 updated agenda. I also detected 2 new authors. Here's the breakdown." Guido excludes one tangential author and approves the rest. The system integrates the updates and flags notable changes.

The criteria are editable — as BAISH's research focus evolves, Guido can broaden or narrow what the pipeline tracks.

### Journey 4: Future Researcher — Self-Service Idea Generation (Post-MVP)

_This journey is out of scope for MVP but informs architectural decisions._

Sofia is a grad student in Buenos Aires who just joined an AI Safety reading group. She's interested in mechanistic interpretability but isn't sure what projects are feasible for someone at her level. She opens the SafetyProjectIdeas web interface. The chatbot greets her and asks about her background: "What's your technical experience? What areas of AI Safety interest you? What compute resources do you have access to? How much time can you dedicate?" Sofia answers: PyTorch experience, transformer architectures, some familiarity with activation patching from Neel Nanda's tutorials, one A100, six months.

The chatbot draws on the pipeline's knowledge base and generates five project ideas tailored to her profile — each with a difficulty rating, estimated compute needs, key papers to read, and a theory of impact. Sofia picks one that excites her, and the chatbot helps her refine it into a concrete proposal she can bring to her mentor.

### Journey Requirements Summary

| Journey | Key Capabilities Revealed |
|---|---|
| 1: Research Coordination | Full pipeline flow (Source→Generate→Filter/Score→Refine→Rank), multi-LLM generation, collaborative chat, team-aware filtering, persistent memory |
| 2: Pipeline Configuration | Configurable team profiles, custom scoring criteria and weights, per-profile pipeline behavior, configuration persistence |
| 3: Knowledge Base Management | Autonomous source discovery with user-defined inclusion criteria, coarse-grained approval workflow, knowledge base updates, contradiction detection, gap analysis |
| 4: Self-Service (Post-MVP) | Web interface, prompted user profiling, real-time idea generation, guided project scoping |

## Innovation & Novel Patterns

### Detected Innovation Areas

**1. Autonomous Knowledge Base Construction with Human Governance**
The pipeline autonomously discovers and structures the AI Safety research landscape — identifying relevant papers, organizations, agendas, and authors without being told what to look for. The human defines inclusion criteria and provides coarse-grained approval, but the system does the discovery. This is a novel collaboration pattern: the AI handles breadth and completeness, the human maintains strategic focus.

**2. Team-Aware Research Idea Generation**
No existing tool systematically generates research project ideas calibrated to specific team configurations. SafetyProjectIdeas doesn't just produce "good ideas" — it produces ideas that are feasible for a specific team's compute budget, technical experience, and mentorship structure. The same source material produces fundamentally different recommendations depending on who will execute the research.

**3. AI Safety Research as an AI Agent Domain**
Applying AI agents to systematically accelerate AI Safety research is a meta-level innovation. The pipeline uses AI capabilities (multi-LLM generation, automated landscape scanning, intelligent scoring) to advance the field that studies the safety of those same capabilities. This creates unique requirements around citation integrity, source grounding, and avoiding the pipeline's own biases influencing the safety research agenda.

### Validation Approach

| Innovation | How to Validate |
|---|---|
| Autonomous KB construction | Compare pipeline-discovered sources against expert-curated source list — measure coverage and precision |
| Team-aware generation | Run same pipeline with different team profiles, verify output meaningfully differs and matches team constraints |
| AI Safety meta-tooling | Track whether pipeline-generated ideas pass expert review at rates comparable to or better than ad-hoc human curation |

### Risk Mitigation

| Risk | Mitigation |
|---|---|
| KB construction misses critical sources or includes noise | Coarse-grained human approval before incorporation; editable inclusion criteria; coverage gap detection |
| Team-aware scoring produces false sense of fit | Human review of all project proposals before staffing; collaborative refinement chat to stress-test fit |
| AI biases shape safety research agenda | Multi-LLM generation for diversity; auditability at every stage; human-in-the-loop for final decisions; explicit impact chain requirement forces grounded reasoning |

## CLI Tool / Developer Tool Specific Requirements

### Project-Type Overview

SafetyProjectIdeas is a hybrid CLI/conversational AI tool built as Claude Code skills with LiteLLM as the provider gateway. It operates in two interaction modes: skill-invoked commands for defined operations (pipeline runs, KB updates, configuration) and conversational flow for brainstorming, refinement, and interactions with less technical users.

### Command Structure

**Skill-Invoked Commands (MVP):**
- `/run-pipeline` — Execute full Source → Generate → Filter/Score → Refine → Rank flow
- `/update-kb` — Fetch new sources, present summary for approval, integrate
- `/build-kb` — Initial knowledge base construction with criteria definition
- `/configure-teams` — Define/edit team profiles, scoring criteria, weights
- `/brainstorm` — Enter collaborative chat mode for human-AI idea co-generation

**Batch/Scheduled Operations:**
- Long-running processes (full pipeline runs, KB builds/updates) must be schedulable as batch jobs
- Batch runs produce output files without requiring interactive approval (using pre-approved criteria)

**Conversational Mode:**
- Available after any skill invocation for follow-up refinement
- Primary mode for brainstorming and collaborative idea development
- Default mode for non-technical users (post-MVP web interface)

### Output Formats

- **Ranked idea lists:** Markdown files — human-readable, each idea includes cited papers with verifiable links/DOIs
- **Pipeline logs:** JSON — compact, structured, one log file per pipeline run with timestamped decisions at each stage
- **Configuration:** YAML files — human-editable, can also be modified through conversation
- **Knowledge base:** Structured storage (format TBD in architecture) — must support efficient querying and incremental updates

### Configuration Schema

All configuration lives in YAML files:

- **Team profiles** (`teams.yaml`) — Team name, type (mentor+novice / solo novice / experienced group), compute budget, technical skills, custom criteria and weights
- **Scoring criteria** (`criteria.yaml`) — Criteria definitions, default weights, per-team-type weight overrides
- **Knowledge base inclusion criteria** (`kb-criteria.yaml`) — Subfields in scope, organizations to track, publication venues, explicit exclusions
- **Pipeline settings** (`pipeline.yaml`) — Model assignments per stage (tiering), LLM providers for parallel generation, threshold settings per filter stage

Configuration can be edited directly or modified through conversational commands — no special tooling needed since Claude Code can read and edit YAML natively.

### Provenance & Citation

Every generated idea must include:
- Papers cited with verifiable links or DOIs
- Source passages that informed the idea
- Which knowledge base sources contributed

Pipeline internals (how stages processed the idea) are logged but not exposed to end users.

### Implementation Considerations

- **Claude Code skills architecture** — Each major operation is a discrete skill, enabling clean separation of concerns and independent iteration
- **LiteLLM provider abstraction** — All LLM calls go through LiteLLM, enabling model tiering and multi-provider parallel generation without provider-specific code
- **Persistent memory** — Pipeline state, learned preferences, and accumulated knowledge persist across sessions via Claude Code's native memory or dedicated storage
- **Batch mode** — Skills must support non-interactive execution for scheduled runs, using pre-configured criteria instead of interactive approval

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach:** Experience MVP with stage-by-stage validation
**Core Principle:** Build a transparent, interactive pipeline where each stage can be run, inspected, and refined independently. The full automated pipeline is the convergence point, not the starting point.
**Resource Requirements:** Solo developer (guido) with Claude Code as development environment

### Progressive Elaboration Format

Ideas evolve through the pipeline — cheap to generate, progressively enriched as they survive:

| Stage | Idea Format | Purpose |
|---|---|---|
| Generate | Brief idea sketch (2-3 sentences: problem + direction + why it matters) | Cheap to produce, easy to kill bad ideas early |
| Filter/Score | Sketch + scores + reasoning per criterion | Evaluate against configurable criteria |
| Refine | Expanded: research question, approach outline, why this framing is strong | Strengthen promising ideas before final ranking |
| Rank | Full concise proposal (see below) | Human-scannable output for decision-making |

**Final Proposal Output (post-Rank):**
- Research question
- Approach (concise methodology outline)
- Proposed first experiments
- Theory of impact chain ("This research leads to X, which reduces risk Y, because Z")
- Scores per criterion
- Cited sources with verifiable links/DOIs

**Design constraint:** Proposals must be short enough that a human can scan 20+ in a sitting and compare them meaningfully, yet concrete enough to be directly actionable. Team fit is assessed separately via collaborative chat when matching proposals to specific teams.

### MVP Development Arc

The MVP follows a stage-by-stage buildout that converges to the full pipeline:

1. **Knowledge Base Build** — Define inclusion criteria, autonomous discovery, coarse-grained approval, structured storage
2. **Source Stage** — Pull relevant material from KB based on criteria
3. **Generate Stage** — Multi-LLM parallel generation via LiteLLM, brief idea sketches from source material
4. **Filter/Score Stage** — Staged evaluation against configurable criteria, with human inspection of scoring decisions
5. **Refine Stage** — Auto-strengthen weak scores, alternative framing, deduplication
6. **Rank Stage** — Scored and sorted output as markdown with full citation provenance
7. **Full Pipeline Run** — Connect all validated stages into end-to-end flow

Each stage is iterable — run it, inspect output, adjust configuration, re-run until satisfied before moving on.

### MVP Feature Set (Phase 1)

**Core User Journeys Supported:**
- Journey 1 (Research Coordination) — full support via stage-by-stage and eventual full pipeline
- Journey 2 (Pipeline Configuration) — team profiles and scoring criteria in YAML config files
- Journey 3 (Knowledge Base Management) — initial build with inclusion criteria and coarse-grained approval; manual update command

**Must-Have Capabilities:**
- Stage-by-stage pipeline execution (run individual stages independently)
- Full pipeline run (all stages in sequence once validated)
- Multi-LLM parallel generation via LiteLLM with deduplication
- Model tiering — cheaper models for quick screens, capable models for deep analysis
- Refine/Iterate stage with auto-strengthen and alternative framing
- Basic ranking — scored and sorted output as markdown
- Collaborative chat for inspection, steering, and brainstorming at every stage
- Configurable team profiles and scoring criteria (YAML config files)
- Knowledge base: autonomous initial build with user-defined inclusion criteria and coarse-grained approval
- Knowledge base: update command with same approval workflow
- Persistent memory across sessions
- Pipeline logging (JSON)
- Citation verification — every idea cites papers with verifiable links/DOIs

### Post-MVP Features (Phase 2)

- **Batch/scheduled pipeline runs** — automated execution once trust is established
- **Advanced ranking** with Pareto frontier and tier system (pursue now / promising / park)
- **Continuous paper scanning** — automated KB updates on schedule
- Idea invalidation/strengthening based on new publications
- Source quality tracking (which sources produce best ideas)
- Filter calibration from user feedback
- Graveyard review — periodic resurfacing of killed ideas
- **Public chat interface** — web UI where researchers self-serve idea generation

### Vision (Phase 3)

- **Learn stage** — blind spot audits, automated feedback loop integration
- Landscape shift detection (org pivots, new agendas)
- Extensibility to other AI Safety research organizations beyond BAISH

### Risk Mitigation Strategy

| Risk Area | Risk | Mitigation |
|---|---|---|
| Technical | Multi-LLM generation produces low-diversity or low-quality ideas | Stage-by-stage validation lets you catch this early; iterate on prompts and model selection before connecting stages |
| Technical | Knowledge base misses critical sources or includes noise | Inclusion criteria + coarse-grained approval; coverage gap detection; iterative refinement |
| Technical | Scoring doesn't match human judgment | Interactive Filter/Score stage with human inspection; tune criteria weights based on override patterns |
| Market | Pipeline ideas aren't good enough to pursue | The entire MVP is designed for validation — if ideas aren't good, you see exactly which stage is failing and fix it |
| Resource | Solo developer, limited time | Stage-by-stage approach means each stage delivers incremental value; no need to finish everything before getting utility |

## Functional Requirements

### Knowledge Base Management

- **FR1:** Coordinator can define inclusion criteria specifying which AI Safety subfields, organizations, publication venues, and authors are in scope or explicitly excluded
- **FR2:** Coordinator can trigger an initial knowledge base build that autonomously discovers and crawls relevant AI Safety sources filtered by the defined inclusion criteria
- **FR3:** System presents a structured summary of discovered sources for coordinator approval before incorporating them into the knowledge base
- **FR4:** Coordinator can exclude specific items or tighten criteria during the approval workflow before incorporation
- **FR5:** Coordinator can trigger a knowledge base update that fetches new sources published since the last update, applying the same inclusion criteria and approval workflow
- **FR6:** Coordinator can edit inclusion criteria at any time to broaden or narrow what the pipeline tracks
- **FR7:** System detects and flags notable changes during updates: contradictions with existing knowledge, alignment with existing ideas, and coverage gaps
- **FR8:** Knowledge base is organized to support selective context retrieval — agents browse only the relevant subset for each task or conversation
- **FR9:** System can filter KB content by subfield, organization, publication venue, recency, or custom tags when providing context to pipeline stages or brainstorming
- **FR10:** Coordinator can browse, search, and query the knowledge base to understand its contents, coverage, and structure

### Knowledge Base Update Mechanisms

- **FR11:** System supports push-based updates triggered by external notification subscriptions (e.g., Google Scholar alerts, LessWrong digests, newsletters) for low-cost targeted updates
- **FR12:** System can suggest new subscriptions based on knowledge base coverage gaps or emerging relevant sources
- **FR13:** System supports pull-based updates that search broadly and catch blind spots missed by push-based notifications
- **FR14:** Both update mechanisms feed through the same coarse-grained approval workflow before KB incorporation
- **FR15:** System can process newsletters and curated digests to identify relevant items to add to the knowledge base or the suggestions list, without incorporating newsletter content directly into the KB

### Knowledge Base Suggestions

- **FR16:** When the system encounters potentially relevant material during updates or novelty assessments, it adds items to a persistent "suggestions list" for potential KB inclusion
- **FR17:** Coordinator can review the suggestions list — approving, rejecting, or discussing items in a chat session

### Pipeline Execution

- **FR18:** Coordinator can run individual pipeline stages independently (Source, Generate, Filter/Score, Refine, Rank)
- **FR19:** Coordinator can run the full pipeline end-to-end (all stages in sequence)
- **FR20:** Coordinator can inspect the output of each stage before proceeding to the next
- **FR21:** Coordinator can intervene at any stage to correct, override, or redirect the pipeline
- **FR22:** System logs every pipeline stage's inputs, decisions, and outputs in structured format

### Idea Generation

- **FR23:** System generates ideas using multiple LLM providers in parallel via LiteLLM
- **FR24:** System deduplicates ideas across LLM providers after parallel generation
- **FR25:** System generates ideas as brief sketches (problem + direction + why it matters) for token efficiency
- **FR26:** System feeds only relevant context (abstracts, limitations) to generation — never full papers
- **FR27:** System uses cheaper models for simple generation tasks and more capable models for deeper analysis (model tiering)

### Idea Evaluation & Scoring

- **FR28:** System evaluates ideas against configurable quality criteria with configurable weights
- **FR29:** System applies staged filtering — progressively more expensive evaluation, killing bad ideas early
- **FR30:** System scores each idea per criterion with explicit reasoning for each score
- **FR31:** System applies threshold settings per filter stage to control which ideas advance
- **FR32:** Every scored idea includes cited papers with verifiable links or DOIs
- **FR33:** Every claim in an idea traces back to a specific source passage in the knowledge base
- **FR34:** System assesses novelty of each idea against existing published work, including sources beyond the knowledge base (e.g., via web search or broader literature access), to flag whether the idea is novel, partially addressed, or already solved
- **FR35:** System actively verifies that cited papers exist and links/DOIs resolve

### Idea Refinement

- **FR36:** System auto-strengthens ideas with weak scores by attempting to improve the weakest dimensions
- **FR37:** System generates alternative framings for promising ideas (2-3 angles on the same core insight)
- **FR38:** System expands surviving ideas from brief sketches to include: research question, approach outline, and strength rationale

### Ranking & Output

- **FR39:** System produces a ranked list of ideas sorted by overall score as a markdown file
- **FR40:** Each final proposal includes: research question, approach, proposed first experiments, theory of impact chain, scores per criterion, and cited sources with verifiable links/DOIs
- **FR41:** Final proposals are concise enough for a human to scan 20+ proposals in a sitting and compare meaningfully
- **FR42:** System preserves the provenance of each idea (which KB sources contributed, which generation method produced it)

### Collaborative Brainstorming

- **FR43:** Coordinator can enter a collaborative chat mode to brainstorm ideas with the AI agent
- **FR44:** Coordinator can direct brainstorming by specifying topics, research areas, or specific problems to explore
- **FR45:** Coordinator can combine topic direction with team constraints (e.g., "interpretability ideas for a novice with one A100")
- **FR46:** Coordinator can refine, iterate, and push back on ideas interactively during brainstorming
- **FR47:** Collaborative chat has access to the full knowledge base and pipeline memory
- **FR48:** Coordinator can pose open research questions and the system assesses whether they have been addressed in the literature, citing relevant work if found or confirming the question remains open

### Evaluate Existing Ideas

- **FR49:** Coordinator can submit an existing project idea (their own or externally sourced) for evaluation against the configured scoring criteria
- **FR50:** System assesses the novelty of submitted ideas against published work (same capability as FR34)
- **FR51:** System can refine and strengthen submitted ideas using the same Refine stage capabilities (auto-strengthen, alternative framing)

### Configuration Management

- **FR52:** Coordinator can define and edit team profiles specifying team type, compute budget, technical skills, and custom criteria weights
- **FR53:** Coordinator can define and edit scoring criteria including definitions, default weights, and per-team-type weight overrides
- **FR54:** Coordinator can add custom scoring criteria beyond the default set
- **FR55:** Coordinator can configure pipeline settings including model assignments per stage and LLM providers for parallel generation
- **FR56:** All configuration is stored in human-editable YAML files
- **FR57:** Configuration persists across sessions

### Priority Areas

- **FR58:** Coordinator can define organizational priority areas, and the pipeline can suggest new priority areas based on landscape analysis
- **FR59:** Priority areas are stored persistently and browsable, similar to project ideas

### Pipeline Memory & Learning

- **FR60:** System persists accumulated knowledge and learned preferences across sessions
- **FR61:** System remembers previous pipeline runs, user overrides, and configuration adjustments
- **FR62:** System applies accumulated knowledge to improve future pipeline runs
- **FR63:** System tracks previously generated ideas and ensures subsequent runs prioritize unexplored directions and source material not yet used

### Idea Repository

- **FR64:** System maintains a persistent, searchable repository of all generated ideas across pipeline runs
- **FR65:** Coordinator can provide retrospective feedback on past ideas (upgrade/downgrade scores, flag false negatives) and the system incorporates this into future scoring

## Non-Functional Requirements

### Cost Efficiency

- **NFR1:** Pipeline minimizes external LLM API costs by using Claude Code for all tasks where it is sufficient, reserving external providers (via LiteLLM) only for multi-LLM diversity in the Generate stage or when specific model capabilities are required
- **NFR2:** Token usage is minimized at every stage through relevant-context-only feeding, progressive elaboration (cheap sketches first, expand only winners), and early killing of low-quality ideas
- **NFR3:** Model tiering assigns the cheapest capable model to each task — expensive models are reserved for tasks where cheaper alternatives are insufficient

### Accuracy & Reliability

- **NFR4:** Zero tolerance for hallucinated citations — if a referenced paper cannot be verified to exist (valid link or DOI resolves), it is excluded from the output entirely
- **NFR5:** Factual claims about existing research or findings must trace back to a verifiable source. Novel insights and cross-pollinations generated by the pipeline are not required to trace to a single source.
- **NFR6:** Novelty assessments must include evidence — confirming no existing work was found via both KB and broader search, or flagging the idea as partially or fully addressed
- **NFR7:** Scoring reasoning must be explicit and auditable — no opaque scores without justification

### Integration

- **NFR8:** All external LLM calls go through LiteLLM provider abstraction, enabling provider switching without code changes
- **NFR9:** Knowledge base sources (ArXiv, Alignment Forum, LessWrong, Google Scholar, organizational agendas, newsletters) are accessed through modular connectors that can be added or replaced independently
- **NFR10:** Architecture supports future integration with additional external systems without requiring core pipeline changes

### Maintainability & Modularity

- **NFR11:** Each pipeline stage (Source, Generate, Filter/Score, Refine, Rank) is independently modifiable, testable, and replaceable without affecting other stages
- **NFR12:** All configurable parameters (team profiles, scoring criteria, inclusion criteria, pipeline settings) are externalized in YAML files, not hardcoded
- **NFR13:** Pipeline stages communicate through well-defined interfaces so that internal implementation can change without breaking the pipeline flow

### Security

- **NFR14:** API keys for LLM providers and external services are stored securely and never logged or exposed in pipeline output
