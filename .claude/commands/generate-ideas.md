# Generate AI Safety Research Idea Sketches

Generate research idea sketches across AI Safety subfields, grounded in the research landscape. Target: at least 250 ideas per subfield (10 strategies × 25+ each).

**IMPORTANT — Source reading policy:** Throughout this entire skill, NEVER read full papers or full system cards. Only read **abstracts, summaries, and introductions**. WebFetch should target summary pages, not full documents. **Exception for deeper context:** When a generation strategy requires information beyond the abstract (e.g., limitations, methodology details, failure modes), prefer ArXiv HTML versions (`arxiv.org/html/<paper_id>`) which are readable by WebFetch. Only read the specific sections you need (e.g., Limitations, Discussion, Methods) — do not read the entire paper. Not all papers have HTML versions; fall back to abstract-only when HTML is unavailable.

## Setup

Create a run directory for this generation run:

```bash
uv run python -m saim.pipeline.orchestrator init generate
```

Save the printed run directory path — it will be used throughout as `<run_dir>`.

Load generation settings:

```bash
uv run python -m saim.config.cli show-generate
```

This outputs the two values needed throughout:
- `min_ideas_per_strategy_per_subfield` — minimum ideas per strategy per subfield
- `combinatorial_top_n` — number of top problems/methods for the combinatorial matrix pass

Before proceeding, echo the active configuration:
> **Generating with:** min_ideas_per_strategy_per_subfield=[value], combinatorial_top_n=[value]

Load previously generated ideas for divergence steering:

```bash
uv run python -m saim.pipeline.memory
```

Save the returned JSON list of previous idea titles — these will be passed to subagents as "covered ground" to diverge from (see Phase 2a prompt).

## Phase 1: Load Context

Check if the research landscape file exists and load subfield context from it.

```bash
test -f data/output/research-landscape.md && echo "EXISTS" || echo "MISSING"
```

**If the landscape file EXISTS:**
- Read `data/output/research-landscape.md`
- Parse the `## Coordinator Selection` section to find subfields marked `[x]`
- If no subfields are marked `[x]`, use ALL subfields ordered by their priority (high > medium > low)
- For each targeted subfield, extract from its `###` section:
  - Open problems (from `**Open Problems:**`)
  - Generation strategy hints (from `**Generation Strategy Hints:**`)
  - Recent surprising results (from `**Recent Surprising Results:**`)
  - Key datasets & benchmarks (from `**Key Datasets & Benchmarks:**`)
  - Common methodologies (from `**Common Methodologies:**`)
  - Source code availability (from `**Source Code Availability:**`)
- Extract landscape gaps from `## Landscape Gaps` — these will be targeted by dedicated subagents in Phase 2b
- Extract the **Quick Reference** section's "Top 5 most actionable sources" — these will be used for source-driven seeding in Phase 1.5

**If the landscape file is MISSING:**
- Ask the coordinator which subfields to target
- If the coordinator does not specify, use these defaults:
  1. Black-box Safety
  2. Interpretability
  3. Safety by Construction
  4. Make AI Solve It
  5. Theory
  6. Multi-agent & Evals
  7. Labs

### Load Participant Profile

Load the configured participant profile and translate it into concrete generation constraints:

```bash
uv run python -m saim.config.cli show-participant
```

**If a participant profile is loaded**, derive explicit constraints for subagent prompts. Map each profile field to a concrete generation constraint:

- `total_hours` + `time_context` → "Ideas must be completable in ~{total_hours} hours, covering {time_context}"
- `technical_skills` → "Methods should only use: {skills}. Avoid techniques requiring: {gaps}"
- `deliverables` → "Final output must include: {deliverables}"
- `background` → "Participant context: {background}" (helps calibrate ambition level)
- `goals` → "Participant goals: {goals}" (helps prioritize ideas that align with what the participant hopes to achieve)

Store these as the `participant_constraints` block — a bullet list of concrete rules, not the raw profile text.

**If no participant profile is loaded**, set `participant_constraints` to "none specified".

## Phase 1.5: Source-Driven Idea Seeding

If the landscape file exists and contains a **Quick Reference** section with actionable sources, launch parallel subagents (one per source) to extract seed problems.

**Subagent prompt for each source:**

> You are extracting concrete research problem statements from a source document for AI Safety idea generation.
>
> Source: [SOURCE_TITLE_AND_URL]
>
> Use WebFetch to load the source page. Read ONLY the abstract, introduction, summary, or table of contents — NEVER the full document.
>
> Extract as many concrete, well-scoped problem statements or research questions as you can find from this source. For each, note:
> - The problem statement (1-2 sentences)
> - Which subfield it belongs to
> - Any suggested methodology or approach mentioned
>
> Return as a JSON array of objects with keys: `problem`, `subfield`, `suggested_method`.

Collect all seed problems and distribute them to Phase 2a subagents as additional input alongside the landscape context.

## Phase 2a: Generate Ideas per Subfield (Parallelized)

Generate ideas across all targeted subfields using **parallel subagents**. Launch **one subagent per strategy per subfield** (10 strategies × N subfields = 10N subagents). Launch all subagent Agent calls in a single message for maximum parallelism.

### Generation Strategies

Each subfield gets 10 subagents, one per strategy:

1. **novel_direction** — A new research direction addressing an open problem in this subfield.
2. **experiment_variation** — Propose variations of existing experiments: modify variables, populations, methodologies, or scope (FR67).
3. **follow_up_experiment** — Propose follow-up experiments to explain observed effects from recent surprising results (FR68).
4. **replication_with_twist** — Take a known result and replicate it on a different model family, dataset, modality, or scale. Particularly accessible for beginners.
5. **tool_or_benchmark_gap** — Propose an idea that fills a gap in evaluation tooling, extends an existing benchmark, or creates a new measurement for an unmeasured property. Use the Key Datasets & Benchmarks context.
6. **failure_mode_investigation** — Target a known failure mode, incident, or surprising result and design an experiment to characterize it more precisely, identify root causes, or test boundary conditions.
7. **cross_domain_transfer** — Import a technique from outside AI safety (e.g., software testing, cognitive science, formal methods, biology, economics) into this subfield.
8. **causal_chain_intervention** — Take a known safety risk in this subfield, decompose it into its causal chain (risk → scenario → causal steps), and propose research targeting an under-studied link in that chain. Inspired by Jones (2025) systematic risk analysis: risks have multiple causal steps, and interventions at earlier/overlooked links are often more tractable than attacking the end-state.
9. **backcast_from_success** — Define a concrete safety success state for this subfield (e.g., "we can reliably detect deceptive alignment in production models"), then work backward: what research results would need to exist to achieve or verify that state? Propose research filling one of those gaps. This is deliberately goal-forward rather than problem-forward.
10. **compounding_risks** — Identify how a safety failure in this subfield interacts with or amplifies a failure in a different subfield (e.g., deception + scalable oversight failure = qualitatively worse than either alone). Propose research that studies, measures, or mitigates the compound effect. Each idea must name the two interacting failure modes.

**Orchestration instructions:**
1. Launch one Agent call per (subfield, strategy) pair, all in a single message
2. Each subagent receives a self-contained prompt with all context needed
3. Each subagent returns its ideas as a JSON array (not files) — the orchestrator writes files in Phase 3
4. If a subagent fails, record the failure in the `warnings` list (see Phase 4) and proceed with results from successful subagents
5. After all subagents complete, collect all idea JSON arrays and proceed to Phase 2b

**Subagent prompt template** (adapt per subfield and strategy):

> You are generating AI Safety research idea sketches for subfield: [SUBFIELD].
> Your assigned generation strategy: **[STRATEGY_NAME]** — [STRATEGY_DESCRIPTION].
>
> **Subfield context:**
> Open problems: [LIST FROM LANDSCAPE OR DEFAULTS].
> Generation strategy hints: [HINTS FROM LANDSCAPE OR "use all strategies"].
> Recent surprising results: [RESULTS FROM LANDSCAPE OR "none available"].
> Key datasets & benchmarks: [FROM LANDSCAPE OR "none listed"].
> Common methodologies: [FROM LANDSCAPE OR "none listed"].
> Available tools/code: [FROM LANDSCAPE OR "none listed"].
>
> **Seed problems from source documents** (use as starting points where relevant):
> [SEED PROBLEMS FROM PHASE 1.5 THAT MATCH THIS SUBFIELD, OR "none available"]
>
> **Participant constraints (all ideas MUST satisfy these):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST — the concrete rules derived in Phase 1, NOT raw profile text]
>
> **Previously explored ideas** (these represent covered ground — use them to deliberately go in DIFFERENT directions. Explore unexplored angles, methods, and combinations rather than repeating what exists):
> [LIST OF PREVIOUS IDEA TITLES]
>
> Generate at least [MIN_IDEAS_PER_STRATEGY_PER_SUBFIELD] idea sketches using ONLY the **[STRATEGY_NAME]** strategy.
>
> For each idea, use WebSearch to verify it is grounded in real research. Read ONLY abstracts and summaries — never full papers.
>
> Each idea must be a brief sketch: problem + direction + why it matters (FR25). Feed only relevant context such as abstracts and limitations — never full papers (FR26).
>
> Return each idea as a JSON object with these keys:
> - `title` (string): concise descriptive title
> - `problem` (string): what problem this addresses
> - `direction` (string): proposed research direction
> - `why_it_matters` (string): why this is important
> - `relevant_context` (string): grounding references (abstracts, key findings cited)
> - `subfield` (string): the subfield name
> - `generation_strategy` (string): "[STRATEGY_NAME]"
> - `confidence` (float): 0.0-1.0 confidence score (use the confidence rubric from `config/pipeline.yaml`)
>
> Return results as a JSON array.

## Phase 2b: Cross-Subfield Synthesis (3 Parallel Lenses)

After all per-subfield subagents complete, launch **three** cross-synthesis subagents in parallel, each with a different lens:

### Lens 1: Methodology Bridging

> You are generating AI Safety research ideas by transferring methodologies across subfields.
>
> **Ideas generated so far** (titles and subfields only, for context — do NOT duplicate these):
> [LIST OF {title, subfield} FROM PHASE 2a RESULTS]
>
> **Methodologies available per subfield:**
> [COMPILED FROM LANDSCAPE: subfield → common methodologies]
>
> **Participant constraints (all ideas MUST satisfy these):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> **Previously explored ideas** (covered ground — go in different directions):
> [LIST OF PREVIOUS IDEA TITLES]
>
> Generate at least [MIN_IDEAS_PER_STRATEGY_PER_SUBFIELD] idea sketches using this strategy:
>
> **methodology_bridging** — Take a methodology that works well in one subfield and apply it to an open problem in a different subfield where it hasn't been tried. For each idea, name the source subfield (where the method is proven) and the target subfield (where it's applied).
>
> For each idea, use WebSearch to verify it is grounded in real research. Read ONLY abstracts and summaries — never full papers.
>
> Return each idea as a JSON object with these keys:
> - `title` (string): concise descriptive title
> - `problem` (string): what problem this addresses
> - `direction` (string): proposed research direction
> - `why_it_matters` (string): why this is important
> - `relevant_context` (string): grounding references (abstracts, key findings cited)
> - `subfield` (string): comma-separated list of bridged subfields
> - `generation_strategy` (string): "methodology_bridging"
> - `confidence` (float): 0.0-1.0 confidence score (use the confidence rubric from `config/pipeline.yaml`)
>
> Return results as a JSON array.

### Lens 2: Problem Decomposition

> You are generating AI Safety research ideas by decomposing hard problems into tractable pieces using tools from multiple subfields.
>
> **Ideas generated so far** (titles and subfields only, for context — do NOT duplicate these):
> [LIST OF {title, subfield} FROM PHASE 2a RESULTS]
>
> **Open problems per subfield** (focus on the hardest ones — scored as high priority):
> [COMPILED FROM LANDSCAPE: hardest open problems per subfield]
>
> **Participant constraints (all ideas MUST satisfy these):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> **Previously explored ideas** (covered ground — go in different directions):
> [LIST OF PREVIOUS IDEA TITLES]
>
> Generate at least [MIN_IDEAS_PER_STRATEGY_PER_SUBFIELD] idea sketches using this strategy:
>
> **problem_decomposition** — Take a hard open problem from one subfield and break it into sub-problems that can be partially addressed using methods or tools from other subfields. Each idea should tackle one specific sub-problem, not the whole thing.
>
> For each idea, use WebSearch to verify it is grounded in real research. Read ONLY abstracts and summaries — never full papers.
>
> Return each idea as a JSON object with these keys:
> - `title` (string): concise descriptive title
> - `problem` (string): what problem this addresses
> - `direction` (string): proposed research direction
> - `why_it_matters` (string): why this is important
> - `relevant_context` (string): grounding references (abstracts, key findings cited)
> - `subfield` (string): comma-separated list of bridged subfields
> - `generation_strategy` (string): "problem_decomposition"
> - `confidence` (float): 0.0-1.0 confidence score (use the confidence rubric from `config/pipeline.yaml`)
>
> Return results as a JSON array.

### Lens 3: Landscape Gap Targeting

> You are generating AI Safety research ideas that target identified gaps in the research landscape.
>
> **Ideas generated so far** (titles and subfields only, for context — do NOT duplicate these):
> [LIST OF {title, subfield} FROM PHASE 2a RESULTS]
>
> **Landscape gaps to target** (high-priority):
> [GAPS FROM LANDSCAPE FILE, OR "none identified" IF NO LANDSCAPE]
>
> **Participant constraints (all ideas MUST satisfy these):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> **Previously explored ideas** (covered ground — go in different directions):
> [LIST OF PREVIOUS IDEA TITLES]
>
> Generate at least [MIN_IDEAS_PER_STRATEGY_PER_SUBFIELD] idea sketches using this strategy:
>
> **landscape_gap_targeting** — Propose ideas that directly address gaps where no subfield naturally owns the problem, or where coverage is thin relative to importance. Each idea must name which gap it targets and why existing subfields haven't addressed it.
>
> For each idea, use WebSearch to verify it is grounded in real research. Read ONLY abstracts and summaries — never full papers.
>
> Return each idea as a JSON object with these keys:
> - `title` (string): concise descriptive title
> - `problem` (string): what problem this addresses
> - `direction` (string): proposed research direction
> - `why_it_matters` (string): why this is important
> - `relevant_context` (string): grounding references (abstracts, key findings cited)
> - `subfield` (string): comma-separated list of relevant subfields
> - `generation_strategy` (string): "landscape_gap_targeting"
> - `confidence` (float): 0.0-1.0 confidence score (use the confidence rubric from `config/pipeline.yaml`)
>
> Return results as a JSON array.

## Phase 2c: Combinatorial Matrix Pass

After Phase 2b, run a structured combinatorial pass. This generates ideas from explicit (problem, method) pairings across subfields.

**Orchestrator builds the matrix:**
1. Select the top `combinatorial_top_n` open problems across all subfields (by priority)
2. Select the top `combinatorial_top_n` methodologies from across all subfields
3. Form the cross-product: each (problem, method) pair where problem and method come from *different* subfields

**Launch one subagent** with the matrix:

> You are generating AI Safety research ideas from a structured combinatorial matrix of problems and methods.
>
> **Problem × Method matrix:**
> [LIST OF (problem, source_subfield, method, method_source_subfield) PAIRS]
>
> For each pair, assess: "Could this method shed light on this problem?" If yes, generate an idea sketch. If the pairing is nonsensical, skip it.
>
> **Participant constraints (all ideas MUST satisfy these):**
> [PARTICIPANT_CONSTRAINTS BULLET LIST]
>
> **Previously explored ideas** (covered ground — go in different directions):
> [LIST OF PREVIOUS IDEA TITLES]
>
> For each viable idea, use WebSearch to verify it is grounded in real research. Read ONLY abstracts and summaries — never full papers.
>
> Return each idea as a JSON object with these keys:
> - `title` (string): concise descriptive title
> - `problem` (string): what problem this addresses
> - `direction` (string): proposed research direction
> - `why_it_matters` (string): why this is important
> - `relevant_context` (string): grounding references (abstracts, key findings cited)
> - `subfield` (string): comma-separated list of bridged subfields
> - `generation_strategy` (string): "combinatorial_matrix"
> - `confidence` (float): 0.0-1.0 confidence score (use the confidence rubric from `config/pipeline.yaml`)
>
> Return results as a JSON array. Skip nonsensical pairings — only return viable ideas.

## Phase 3: Write Ideas

For each idea returned by the subagents (Phase 2a + 2b + 2c), write it to the run directory.

Assign sequential idea IDs: `gen-001`, `gen-002`, etc., across all subfields.

For each idea, add the `idea_id` and `run_id` (extracted from the run directory name) to the JSON, then write:

```bash
uv run python -m saim.pipeline.generate write <run_dir> '<json_data>'
```

Where `<json_data>` is the full JSON object for the idea including `idea_id` and `run_id`.

## Phase 4: Write Run Metadata

Use the orchestrator's `write_run_meta()` function to write `run_meta.json`. This automatically captures the git commit hash and timestamp. Pass the generation parameters as the `params` dict, including the config snapshot for reproducibility (AC1).

**Include a `warnings` array** in params to capture any issues encountered during generation:

The orchestrator must substitute the `<PLACEHOLDER>` values below with actual values collected during generation.

```bash
uv run python -c "
from pathlib import Path
from saim.pipeline.orchestrator import write_run_meta
from saim.config.loader import load_config
config = load_config(load_env=False)
params = {
    'subfields_targeted': <SUBFIELDS_LIST>,          # e.g. ['Black-box Safety', 'Interpretability']
    'participant_profile': '<PROFILE_NAME>',          # e.g. 'bluedot_technical_project_participant' or 'none'
    'total_ideas_generated': <TOTAL_COUNT>,            # e.g. 350
    'min_ideas_per_strategy_per_subfield': <MIN_IDEAS>,# e.g. 25
    'generation_strategies_used': ['novel_direction', 'experiment_variation', 'follow_up_experiment', 'replication_with_twist', 'tool_or_benchmark_gap', 'failure_mode_investigation', 'cross_domain_transfer', 'causal_chain_intervention', 'backcast_from_success', 'compounding_risks', 'methodology_bridging', 'problem_decomposition', 'landscape_gap_targeting', 'combinatorial_matrix'],
    'landscape_file_used': <True_OR_False>,            # e.g. True
    'landscape_gaps_targeted': <True_OR_False>,        # e.g. True
    'source_seeding_used': <True_OR_False>,            # e.g. False
    'combinatorial_top_n': <COMBINATORIAL_TOP_N>,      # e.g. 10
    'previous_ideas_count': <PREV_COUNT>,              # e.g. 0
    'warnings': <WARNINGS_LIST>,                       # e.g. [] or [{'subfield': 'interpretability', 'strategy': 'novel_direction', 'issue': 'subagent failed', 'fallback_used': 'skipped'}]
    'config_snapshot': {
        'team_profile': config.default_team,
        'criteria_weights': {c.name: config.teams[config.default_team].criteria_weights.get(c.name, c.default_weight) for c in config.criteria},
        'pipeline_model': config.pipeline.model_assignments['generate'].model_dump() if 'generate' in config.pipeline.model_assignments else {}
    }
}
write_run_meta(Path('<RUN_DIR>'), params)
"
```

## Phase 5: Coordinator Review (FR20, FR21)

**First, display any warnings** from generation (subagent failures, degraded web search, etc.). If warnings exist, list them prominently before the idea summary.

**Then, check for partial duplicates** among the generated ideas and any previous ideas. Compare all idea titles pairwise — if two titles share significant keyword overlap or address the same problem statement, flag them as a **potential duplicate pair**. List flagged pairs for the coordinator to review (do NOT auto-remove them — the coordinator decides).

Present the coordinator with a summary:

1. **Warnings** (if any): list of issues encountered during generation
2. **Potential duplicate pairs** (if any): pairs of ideas with similar titles/problems for coordinator review
3. **Total ideas generated** and count per subfield
4. **Count per generation strategy** (all 14 strategies)
5. **All ideas listed** with: idea_id, title, subfield, generation_strategy, confidence score
6. Sort by confidence (highest first) within each subfield

The coordinator can:
- **Review** individual ideas: `uv run python -m saim.pipeline.generate read <run_dir>` to see all, or read specific files
- **Remove** ideas they don't want (including flagged duplicates)
- **Add** additional ideas through conversation (write them with the same pipeline command)
- **Redirect** generation to specific areas (re-run Phase 2a for specific subfields/strategies)

Tell the coordinator:
> Your ideas are in `data/runs/<timestamp>/generate/`. When you're satisfied with the idea set, proceed to scoring with `/score-ideas`.

## Output Contract

The skill produces markdown idea files in `data/runs/<timestamp>/generate/`:
- Each file has YAML frontmatter with: idea_id, run_id, stage, timestamp, subfield, generation_strategy, confidence
- Each file has a markdown body with: Problem, Direction, Why It Matters, Relevant Context sections
- The run directory also contains `run_meta.json` (with `warnings` array) and `pipeline.log.json`

## Error Handling

- If web search fails: fall back to Claude's training knowledge, note degraded sourcing in idea's `relevant_context` AND add to `warnings`
- If config loading fails: use defaults for participant constraints, add to `warnings`
- If participant profile not found: proceed without constraints, add to `warnings`
- If landscape file doesn't exist: proceed without it — ask for subfields or use defaults (Phase 1.5 source seeding is skipped)
- If individual subagents fail: proceed with results from successful subagents, add to `warnings`
- If cross-subfield subagents fail: proceed with per-subfield ideas only, add to `warnings`
- If combinatorial matrix subagent fails: proceed with Phase 2a + 2b ideas, add to `warnings`
- If source seeding subagents fail: proceed without seeds (Phase 2a still runs with landscape context), add to `warnings`
- Always produce output even with degraded sources — partial idea generation is better than none
