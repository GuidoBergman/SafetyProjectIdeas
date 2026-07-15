# SAIM (Safety Idea Machine)

AI Safety Research Idea Generation Pipeline for BAISH (Buenos Aires AI Safety Hub).

## Overview

SAIM is a Claude Code skills-based pipeline that generates, evaluates, refines, and ranks AI Safety research project ideas tailored to different team configurations and participant profiles. It uses configurable scoring criteria, literature search, and citation verification to produce actionable research proposals.

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


## Configuration

All configuration is managed through YAML files in `config/`:

- **`teams.yaml`** — Team profiles with skill sets and per-team criteria weight overrides. Ships with three teams: `mentor_novice` (default), `solo_novice`, and `experienced_group`.
- **`criteria.yaml`** — Five scoring criteria (`theory_of_impact`, `low_compute`, `accessible_complexity`, `narrow_scope`, `novelty`), each with a 1-5 rubric and refinement threshold.
- **`pipeline.yaml`** — Model assignments per stage, batch sizes, thresholds, and rubrics for quick-filter, confidence, and citation relevance scoring.
- **`kb-criteria.yaml`** — Knowledge base inclusion criteria (subfields in scope, organizations, exclusions).
- **`participants/<name>.yaml`** — Individual participant profiles (background, time, resources).

Use `/configure-teams` to manage all of these interactively.

## Recommended Workflow

Three steps. See [Typical Workflow](#typical-workflow) below for the granular, stage-by-stage alternative.

**1. Configure** — `/configure-teams`

Set the active team and participant first: the team's weights drive scoring, and the participant's constraints become hard requirements in every later prompt.

**2. Generate** — `/run-pipeline-light`

Harvests recent safety papers from curated sources, grounds ~2 ideas in each, then scores, refines, ranks, and novelty-checks the top 100 autonomously. Everything lands in an isolated `data/runs/<timestamp>/`; nothing touches `data/ideas/`.

Scoped by **time window and source, not topic** — it sweeps the last ~2 months of the ML Safety Newsletter, AI Safety at the Frontier, major org publications, and Alignment Forum / LessWrong. It takes no topic parameter; use `/run-pipeline` if you need subfield scoping, which consumes more tokens. You can steer the light pipeline from the prompt by asking it to include a specific paper, widen the window, or skip the novelty check.

**3. Refine** — `/evaluate-idea`, once per promising idea

The most promising ideas are the top-ranked ones in `data/runs/<timestamp>/rank/ranked_proposals.md`, sorted best-first behind a top-10 summary table. Pick from there and run `/evaluate-idea` once per idea you picked. It checks the idea is **operationalizable** (concrete experiments, baselines, success criteria) and **contextualized** (re-running the novelty check from scratch rather than trusting the pipeline's), then opens an interactive loop to sharpen the approach, refine the experiments, strengthen the impact chain, reframe it, or drop it. Saving writes the idea to the selected ideas file and updates `data/output/idea_tracker.md`.

## Pipeline Skills

The pipeline is orchestrated through Claude Code slash commands. These are the skills available in this project, roughly ordered by typical workflow sequence.

### Research & Discovery

#### `/research-landscape` — Research Landscape Discovery

Maps the AI Safety research landscape to guide idea generation. Runs parallelized searches across 11 categories (open problems, research agendas, key orgs, recent papers, safety evaluations, community discussions, funding priorities, government policy, tools/benchmarks, failure modes, and curated project lists).

**Output:** `data/output/research-landscape.md` — structured by subfield with open problems, key authors, methodologies, and a gap analysis. Includes coordinator selection checkboxes used by `/generate-ideas`.

#### `/research-topic` — Research Topic Deep Dive

Deep-dives into a specific research topic. Negotiates which dimensions to track (methodology, scale, findings, open questions, reproducibility), then launches parallel literature search agents (academic, web, community). Produces a synthesis with gap analysis.

**Usage:** Provide a research question, area, technique, or problem framing when prompted.

**Output:** `data/output/research-topic-[TOPIC].md`

### Idea Generation

#### `/generate-ideas` — Generate AI Safety Research Idea Sketches

Generates 250+ research idea sketches using 14 generation strategies across AI Safety subfields. Works in phases:

1. Load context from research landscape and participant profiles
2. Source-driven seed extraction from landscape documents
3. Per-subfield generation (10 strategies per subfield, parallel subagents)
4. Cross-subfield synthesis (methodology bridging, problem decomposition, landscape gap targeting)
5. Combinatorial matrix pass (problem x method pairwise generation)
6. Write ideas and metadata to run directory
7. Coordinator review with duplicate detection

**Generation strategies:** `novel_direction`, `experiment_variation`, `follow_up_experiment`, `replication_with_twist`, `tool_or_benchmark_gap`, `failure_mode_investigation`, `cross_domain_transfer`, `causal_chain_intervention`, `backcast_from_success`, `compounding_risks`, plus 3 cross-subfield and 1 combinatorial strategy.

**Output:** Individual idea markdown files in `data/runs/<timestamp>/generate/`

#### `/brainstorm-ideas` — Interactive Brainstorming

Collaborative brainstorming session tailored to your team constraints and participant profile. Accepts topics, areas, problems, or research questions and generates 3-5 idea sketches per input. Uses citation tools to assess literature. Saves promising ideas to `data/ideas/`.

### Scoring & Filtering

#### `/score-ideas` — Score and Filter Ideas

Two-wave scoring pipeline:

- **Wave 1 (Quick Relevance Filter):** Scores ideas 1-5 against a quick-filter rubric, eliminates below threshold (default 2.0). Processes in batches of 100 via parallel subagents.
- **Wave 2 (Full Criteria Scoring):** Scores survivors against all criteria (except novelty) with per-criterion rubrics. Computes weighted scores using active team weights. Batches of 30 via parallel subagents.

**Output:** Scored idea JSON files in `data/runs/<timestamp>/filter_score/results/`

#### `/novelty-check` — Novelty Assessment & Citation Verification

Evidence-based novelty assessment using multi-source literature search (WebSearch, CrossRef, Semantic Scholar, LessWrong, Alignment Forum).

**Novelty protocol (N1-N5):** Literature search, evidence collection, deep reading, classification (5-level rubric), and formatted output.

**Novelty levels:**
| Score | Classification | Meaning |
|-------|---------------|---------|
| 1 | Already solved | Hard gate — idea eliminated |
| 2 | Largely addressed | Multiple works cover most contribution |
| 3 | Partially addressed | Specific angle/method unexplored |
| 4 | Mostly novel | No direct work, related work in adjacent areas |
| 5 | Novel | No published work found |

**Citation verification (C1-C3):** Scores citation relevance, verifies via CrossRef + Semantic Scholar, applies consequences for unverified load-bearing citations.

Can run standalone or as a sub-agent within `/score-ideas`.

### Refinement & Ranking

#### `/refine-ideas` — Refine Ideas into Full Proposals

Strengthens weak idea dimensions and generates alternative framings:

1. **Auto-strengthen:** Identifies weak dimensions (below refinement threshold), generates improvements, re-scores, accepts only if improved.
2. **Alternative framings:** For top 50% of ideas, generates 2-3 alternative framings (different methodology, scope, or lens), promotes those that improve weighted score.
3. **Assemble full proposals:** Produces structured proposals with research question, approach outline, proposed experiments, theory of impact chain, strength rationale, and cited sources.

**Output:** Full proposals in `data/runs/<timestamp>/refine/`

#### `/rank-ideas` — Rank Refined Proposals

Re-scores refined proposals on full content and produces final rankings. Retains novelty scores from filter_score (does not re-assess without new evidence). Generates a human-scannable ranked list with top-10 summary table.

**Output:**
- `data/runs/<timestamp>/rank/ranked_proposals.md` and `.json`
- Persistent copy at `data/output/ranked_proposals.md`

### Evaluation & Management

#### `/evaluate-idea` — Evaluate a Single Idea

Interactive evaluation workflow for any idea (pipeline-generated or user-submitted):

1. Load existing idea from `data/ideas/` or describe a new one
2. Score against all criteria (new ideas only)
3. Optional novelty check with literature search
4. Collaborative refinement loop (discuss, strengthen, reframe, check novelty, or remove)
5. Save to `data/ideas/` and update idea tracker

Updates `data/output/idea_tracker.md` with status transitions: `Not reviewed` -> `Evaluating` -> `Added and needs manual review` / `Not promising` / `Removed` -> `Added`.

**Important:** Ideas with only estimated novelty (`novelty_method: "novelty_estimated"`) trigger an automatic novelty check before saving.

#### `/configure-teams` — Configure Teams and Profiles

Manage all project configuration interactively:
- Display current configuration
- Add/edit/remove team profiles
- Add/edit/remove scoring criteria
- Update pipeline settings (models, thresholds)
- Manage participant profiles

## Typical Workflow

```
1. /configure-teams          # Set up team profile and participant
2. /research-landscape       # Map the AI Safety research landscape
3. /research-topic           # (Optional) Deep-dive into specific areas
4. /generate-ideas           # Generate 250+ idea sketches
5. /score-ideas              # Score and filter to top candidates
6. /refine-ideas             # Strengthen and expand into full proposals
7. /rank-ideas               # Produce final ranked list
8. /evaluate-idea            # Interactively evaluate individual ideas
9. /novelty-check            # (Anytime) Verify novelty with literature search. This is recommended for top ideas only since it consumes a lot of tokens.
10. /brainstorm-ideas        # (Anytime) Collaborative idea exploration
```

## Project Structure

```
src/saim/
├── pipeline/        # Pipeline stages (generate, filter_score, novelty, memory, orchestrator)
├── config/          # Config loading, CLI, Pydantic schemas, participant profiles
├── verification/    # Citation lookup (CrossRef, Semantic Scholar)
├── connectors/      # Source connectors for KB ingestion
└── kb/              # Knowledge base management

config/
├── teams.yaml       # Team profiles and defaults
├── criteria.yaml    # Scoring criteria with rubrics
├── pipeline.yaml    # Model assignments, thresholds, batch sizes
├── kb-criteria.yaml # Knowledge base inclusion criteria
└── participants/    # Individual participant profiles

data/
├── ideas/           # Persistent idea files (cross-run)
├── output/          # Final outputs (ranked proposals, idea tracker, landscape)
├── kb/              # Knowledge base
└── runs/            # Timestamped pipeline run directories
    └── YYYY-MM-DDTHH-MM-SS/
        ├── generate/
        ├── filter_score/
        ├── refine/
        ├── rank/
        ├── run_meta.json
        └── pipeline.log.json

tests/               # Test suite mirroring src/ structure
.claude/commands/    # Claude Code skills
```



## Development

```bash
uv run python -m pytest          # Run tests
uv run ruff check src/ tests/ scripts/   # Lint
uv run ruff format src/ tests/ scripts/  # Format
```

## License

MIT
