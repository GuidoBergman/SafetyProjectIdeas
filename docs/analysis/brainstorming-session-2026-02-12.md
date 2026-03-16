---
stepsCompleted: [1, 2, 3, 4]
inputDocuments: []
session_topic: 'Pipeline for generating AI Safety research project ideas'
session_goals: 'Produce project ideas that are sound, relevant, have good theory of impact, low compute requirements, and accessible technical complexity'
selected_approach: 'ai-recommended'
techniques_used: ['Question Storming', 'Morphological Analysis', 'Reverse Brainstorming']
ideas_generated: [7]
technique_execution_complete: true
context_file: ''
---

# Brainstorming Session Results

**Facilitator:** guido
**Date:** 2026-02-12

## Session Overview

**Topic:** Pipeline for generating AI Safety research project ideas for an AI Safety research organization's open problems list

**Goals:** Design a systematic pipeline that produces research project ideas meeting five quality criteria:
1. Sound — methodologically rigorous and technically well-grounded
2. Relevant — aligned with current open problems in AI Safety
3. Good theory of impact — clear causal pathway from research to meaningful safety outcomes
4. Low compute requirements — prioritize ideas not requiring massive computational resources
5. Accessible complexity — favor technically tractable projects

### Session Setup

_The session focuses on designing a repeatable, systematic process (pipeline) rather than generating individual project ideas directly. The pipeline itself is the brainstorming target — how to source, filter, evaluate, and curate AI Safety research ideas at an organizational level._

## Technique Selection

**Approach:** AI-Recommended Techniques
**Analysis Context:** Pipeline for generating AI Safety research project ideas with focus on soundness, relevance, impact, low compute, and tractability

**Recommended Techniques:**

- **Question Storming (Phase 1 — Foundation):** Define the right questions the pipeline must answer before designing it. Ensures we solve the right problem.
- **Morphological Analysis (Phase 2 — Design):** Systematically map all pipeline components, stages, inputs, filters, and outputs. Explores combinations for optimal configuration.
- **Reverse Brainstorming (Phase 3 — Stress-Test):** Identify how the pipeline could fail to produce good ideas, then design safeguards against each failure mode.

**AI Rationale:** The session topic is meta-level process design (not idea generation), requiring analytical depth. This sequence follows a define-build-test progression that matches the systematic, research-oriented tone of the session.

## Technique Execution Results

### Phase 1: Question Storming — Defining the Problem Space

**Questions the pipeline must answer (user-generated):**

1. What is the expected computational cost of the project?
2. What is the theory of impact of the project?
3. Has the project the potential to reduce risks from advanced AI systems?
4. What is the technical experience required to implement the project?
5. Is someone else doing exactly the same?
6. Are relevant organizations interested in this problem?
7. Can we design cheap experiments to test the ideas?
8. What is the expected outcome of the project?
9. How certain are we that the project will be successful?
10. Can we establish a "backup" plan to increase the probability of success?
11. How certain are we that this direction is relevant?
12. Are there better solutions to solve the problem?

**Additional questions surfaced during facilitation:**

- Where do candidate ideas come from? (Sources)
- At what point do we apply filters — all at once, or in stages?
- Who generates the ideas — internal, external, or AI?
- How often does the list need updating?
- What happens to ideas that almost pass filters?
- How do we prevent pipeline blind spots?
- Should the pipeline produce a ranked list or an unranked set?
- How do we know the pipeline is working?

**Key discoveries:**

- Ideas are literature-centric: sourced from papers, agendas, system cards, forums
- The pipeline is for an AI Agent to generate ideas, with a collaborative chat interface for human-AI co-generation
- Filtering should be staged (not all-at-once)
- Ideas should be ranked with graduated scores (not binary pass/fail)
- AI Safety moves fast — continuous monitoring and freshness checks are essential
- The pipeline should incorporate human feedback and learn from it
- An AI Agent should periodically audit the pipeline for blind spots

### Phase 2: Morphological Analysis — 7-Stage Pipeline Design

#### Stage 1: Source — Where ideas come from

| Source | Automation Potential |
|---|---|
| Open problems lists in AI Safety | Medium |
| Research agendas from relevant orgs | Medium |
| Limitations/extensions of recent papers | High |
| Gaps in SOTA model system cards | High |
| Cross-pollinating approaches between papers | High |
| LessWrong top-voted posts | High |
| Relevant authors' new work | High |
| Alignment Forum | High |
| Relevant conference proceedings | Medium |

**Design decisions:**
- Agent maintains an evolving relevance profile (authors, keywords, subfields) for filtered fetching
- No firehose — only fetch papers matching relevance criteria
- Token efficiency is a first-class constraint

#### Stage 2: Generate — How raw ideas are produced

| Method | Description |
|---|---|
| Limitation mining | Parse paper limitation sections, generate projects addressing them |
| Gap analysis | Compare system card capabilities against safety desiderata |
| Cross-pollination | Take approach from Paper A, apply to problem in Paper B |
| Agenda decomposition | Break broad agenda items into project-sized pieces |
| Delta detection | What changed since last check? New papers, results, failures |
| Collaborative generation | Human-AI chat where user provides direction |

**Design decisions:**
- Generate as cheap one-liners first, expand only winners (token efficient)
- Both batch and single-idea modes available
- Feed only relevant context at each stage (e.g., abstract + limitations, not full paper)

#### Stage 3: Filter/Score — Staged evaluation funnel

| Filter Stage | What it checks | Cost | Action |
|---|---|---|---|
| Quick screen | Duplicates, out-of-scope, already solved | Very cheap | Kill or pass |
| Relevance check | Is this an AI Safety problem? Connects to open problems? | Cheap | Score 1-5 |
| Feasibility check | Compute requirements, complexity, team capability match | Cheap | Score 1-5 |
| Impact assessment | Theory of impact, risk reduction potential, expected outcome | Medium | Score 1-5 |
| Redundancy check | Is someone already doing exactly this, or is it already solved? | Medium | Score 1-5 |
| Experiment design | Can we design cheap experiments? Backup plan? | Expensive | Score 1-5 |

**Design decisions:**
- Each stage progressively more expensive — bad ideas killed early and cheap
- Thresholds at each stage to prevent token waste on bad ideas
- Cheaper models for simple decisions, more capable models for harder decisions
- Each stage logs inputs, decisions, and outputs for auditability

#### Stage 4: Refine/Iterate — Improving promising ideas

| Method | Mode |
|---|---|
| Auto-strengthen | Autonomous — AI attempts to improve weak scores |
| Alternative framing | Autonomous — generate 2-3 angles on same idea |
| Scope adjustment | Autonomous — break down or combine ideas |
| Human-in-the-loop refinement | Collaborative — iterate via chat |
| Granular feedback integration | Collaborative — user explains what failed |

**Design decisions:**
- Auto-refine first, escalate to human only when agent gets stuck
- Keeps human attention focused on ideas that genuinely need expert judgment

#### Stage 5: Rank — Prioritizing the final list

**Design decisions:**
- Pareto ranking to surface frontier of non-dominated ideas
- Tier system for actionability (Tier 1: pursue now, Tier 2: promising, Tier 3: park)
- Presentation format to be decided when team starts using it

#### Stage 6: Monitor — Freshness and new paper scanning

| Function | What it watches |
|---|---|
| New paper detection | ArXiv, Alignment Forum, LessWrong, conferences (relevance-filtered) |
| Idea invalidation | Has someone published a solution to a listed problem? |
| Idea strengthening | New evidence supporting an existing idea |
| Landscape shift | Org announced new agenda or pivoted |
| Staleness flag | Ideas sitting too long without action or updates |

**Design decisions:**
- Relevance-filtered fetching via evolving search profile
- Auto-update reviewed ideas with clear changelog (what changed and why)
- Agent maintains and refines relevance profile over time

#### Stage 7: Learn — Incorporating feedback

| Mechanism | What it improves |
|---|---|
| Granular idea feedback | Scoring accuracy (user explains what specifically failed) |
| Source quality tracking | Which sources produce best ideas over time |
| Filter calibration | User overrides when good ideas killed or bad ideas pass |
| Blind spot detection | AI agent periodically audits for missing subfields/approaches |

**Design decisions:**
- Persistent memory read at session start — flexible, accumulates naturally
- No hard rule formalization required

### Phase 3: Reverse Brainstorming — Failure Modes & Safeguards

#### Cluster 1: Token & Resource Waste

| Failure Mode | Safeguard |
|---|---|
| Pipeline overly complex, massive token waste | Start minimal, add complexity only when validated |
| Full papers fed raw into LLM | Feed only relevant sections (abstract, limitations) — never full papers |
| Hundreds of useless papers fetched | Relevance pre-filter via keyword/abstract screening |
| Too much time/compute for simple decisions | Model tiering — cheaper models for quick screens, capable models for deep analysis |
| Unnecessary steps killing good ideas | Each filter stage must justify its existence; remove if not adding value |

#### Cluster 2: Hallucination & Reliability

| Failure Mode | Safeguard |
|---|---|
| Agent includes non-existent papers | Citation verification — every paper must include verifiable link or DOI |
| Hallucinated info causes bad decisions | Source grounding — every claim traces back to a specific source passage |
| Agent proposes impossible solutions | Sanity check — verify basic feasibility with explicit reasoning before advancing |

#### Cluster 3: Context Overload

| Failure Mode | Safeguard |
|---|---|
| Too much information hurts agent performance | Context hygiene — each stage gets only the information it needs. Modular context windows |

#### Cluster 4: Alignment with User

| Failure Mode | Safeguard |
|---|---|
| Ranking doesn't match user preferences | Preference calibration — periodically show borderline ideas, ask user to rank, compare |
| Agent's criteria differs from user's | Explicit criteria document read at session start, reviewed regularly |
| User criteria underspecified or ambiguous | Agent flags ambiguities and asks for clarification rather than guessing |
| Doesn't understand team's technical skills | Team profile document, updated when team changes |
| Doesn't estimate technical effort properly | Effort estimation with uncertainty ranges, flag low confidence |
| Projects irrelevant / weak theory of impact | Impact chain requirement: "This research leads to X, which reduces risk Y, because Z" |
| Pipeline miscalculates project cost | Compare estimates against actual costs of past projects via persistent memory |

#### Cluster 5: Filtering Errors

| Failure Mode | Safeguard |
|---|---|
| Kills good ideas too early | Graveyard review — periodically resurface killed ideas for human spot-check |

#### Cluster 6: Learning Loop Failures

| Failure Mode | Safeguard |
|---|---|
| User feedback wasted | Feedback audit — persistent memory must show how feedback changed behavior |
| Relevant sources never incorporated | Source coverage review — agent checks if all configured sources consulted recently |

#### Cluster 7: Rigidity vs. Autonomy

| Failure Mode | Safeguard |
|---|---|
| Too rigid to improve | Pipeline stages and thresholds stored as editable configuration |
| Too complex to maintain | Modular design — each stage independent, modifiable without breaking others |
| Agent too constrained | Autonomous exploration mode — agent can flag ideas outside current scope |
| Agent too autonomous | Guardrails with transparency — agent explains reasoning when deviating |

### Post-Session Corrections (User Feedback)

1. **No summarization step** — feed only relevant context per stage (abstract + limitations, not summaries of full papers)
2. **Model tiering** — cheaper models for simple decisions, capable models for hard decisions. Subagent design is critical.
3. **Pipeline logging** — each stage logs inputs, decisions, and outputs for auditability
4. **No "simplicity budget"** — just start minimal, add complexity when validated. No mathematical overhead.
5. **No hit-rate tracking** — avoid over-engineering that could break things
6. **Ambiguity flagging** — agent must flag ambiguous or contradictory user criteria rather than guessing

### Cross-Cutting Design Principles

1. **Token efficiency at every stage** — relevant context only, model tiering, kill bad ideas early
2. **Two operating modes** — autonomous agent + collaborative chat interface
3. **Human stays in the loop for refinement and feedback**, not grunt work
4. **Modular and simple** — each stage independent, easy to modify
5. **Auditable** — every stage logs its decisions
6. **Carefully designed subagents** — right model for right task
7. **Living system** — learns from feedback, monitors for new sources, evolves over time

## Idea Organization and Prioritization

### Thematic Organization

**Theme 1: Core Pipeline Architecture**
_The fundamental stages and flow of the system_

- 7-stage pipeline: Source → Generate → Filter/Score → Refine → Rank → Monitor → Learn
- 9 idea sources (papers, agendas, system cards, forums, conferences)
- 6 generation methods (limitation mining, gap analysis, cross-pollination, agenda decomposition, delta detection, collaborative)
- 6-stage evaluation funnel with progressive cost and thresholds

**Theme 2: Token Efficiency & Cost Control**
_Making the pipeline economically viable_

- One-liner hypotheses first, expand only winners
- Feed relevant sections only (abstract + limitations), never full papers
- Model tiering — cheaper models for simple decisions, capable models for hard ones
- Thresholds at each stage to kill bad ideas early
- Relevance-filtered paper fetching (no firehose)

**Theme 3: Reliability & Trust**
_Preventing the pipeline from producing garbage_

- Citation verification (every paper needs verifiable link/DOI)
- Source grounding (every claim traces to a specific passage)
- Sanity check before ideas advance
- Pipeline logging at every stage for auditability
- Impact chain requirement ("This leads to X, which reduces risk Y, because Z")

**Theme 4: Human-AI Collaboration**
_How humans and the agent work together_

- Two modes: autonomous agent + collaborative chat interface
- Auto-refine first, escalate to human when stuck
- Granular feedback (user explains what specifically failed)
- Agent flags ambiguities in user-defined criteria
- Human spot-check of killed ideas (graveyard review)

**Theme 5: Adaptive Intelligence**
_The pipeline as a living, learning system_

- Persistent memory read at session start
- Evolving relevance profile for paper fetching
- Auto-update of reviewed ideas with changelog
- Blind spot audits by the agent
- Source coverage review

**Theme 6: Modularity & Maintainability**
_Keeping the system simple enough to actually build and iterate_

- Each stage independent and modifiable
- Pipeline config as editable settings, not hardcoded logic
- Start minimal, add complexity only when validated
- Agent can flag ideas outside current scope (autonomous exploration mode)
- Guardrails with transparency when agent deviates

### Prioritization Results

**Tier 1 — Build First (Core value, minimum viable pipeline):**

- The basic Source → Generate → Filter/Score flow
- One-liner hypothesis generation with staged filtering
- Relevant-context-only feeding (abstract + limitations)
- Basic collaborative chat interface

**Tier 2 — Add Next (Quality and trust):**

- Citation verification and source grounding
- Model tiering across stages
- Pipeline logging for auditability
- Refine/iterate stage with auto-refine + human escalation

**Tier 3 — Mature Over Time (Adaptive, self-improving):**

- Monitoring and continuous paper scanning
- Persistent memory and learning from feedback
- Pareto ranking + tier system
- Blind spot audits and graveyard reviews

### Action Plan

**Immediate next steps to build Tier 1:**

1. **Define the explicit criteria document** — write down the 5 quality criteria with concrete scoring rubrics so the agent has unambiguous guidance
2. **Define the team profile** — document team capabilities, compute budget, and technical skills
3. **Build the Source → Generate → Filter MVP** — a single flow that takes one paper (abstract + limitations), generates one-liner ideas, and runs them through quick screen + relevance check
4. **Build the collaborative chat interface** — the human-AI mode where a user can provide direction and iterate on ideas together
5. **Test with a real paper** — run the MVP end-to-end on a recent AI Safety paper and evaluate the output quality

## Session Summary

**Key Achievements:**

- Designed a complete 7-stage pipeline architecture for AI Safety research idea generation
- Identified 22 failure modes with concrete safeguards
- Established 6 cross-cutting design principles with strong emphasis on token efficiency and simplicity
- Created a 3-tier implementation roadmap with clear priorities
- Defined 5 actionable next steps to begin building the MVP

**Session Insights:**

- The pipeline is fundamentally a methodology-driven AI research assistant, not a static script
- Token efficiency is a first-class design constraint that shapes every architectural decision
- Simplicity and modularity are themselves safeguards — complexity is a failure mode
- The system needs two modes (autonomous + collaborative) to serve different use cases
- Human involvement should be reserved for high-value decisions (refinement, feedback), not grunt work
