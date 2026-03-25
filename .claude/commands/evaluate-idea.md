# Evaluate and Refine an AI Safety Research Idea

Collaboratively evaluate, refine, and strengthen a research idea — whether it comes from the pipeline or is submitted fresh by the user.

## Setup

Load scoring configuration (criteria with rubrics and active weights):

```bash
uv run python -m safety_ideas.config.cli show-scoring
```

Load team profile:

```bash
uv run python -m safety_ideas.config.cli show
```

Load participant profile:

```bash
uv run python -m safety_ideas.config.cli show-participant
```

Save all configuration for use throughout the session.

## Step 1: Load or Accept the Idea

Ask the coordinator how they want to provide the idea:

> How would you like to provide the idea?
> 1. **Existing idea** — provide an idea ID (e.g., "gen-0017") and I'll load it from `data/ideas/`
> 2. **New idea** — describe it and we'll build it up together

### If existing idea (option 1):

Read the idea file from `data/ideas/<idea_id>.md`. Parse the full YAML frontmatter and markdown body. The idea has these structured fields:

**Frontmatter:**
- `idea_id`, `run_id`, `stage`, `rank`, `weighted_score`
- `title`, `subfield`, `generation_strategy`
- `novelty_classification`, `novelty_score`, `novelty_method`
- `original_scores`: dict with `theory_of_impact`, `accessible_complexity`, `narrow_scope`, `novelty` (each 1-5)
- `provenance`: dict with `generation_method`, `kb_sources` (list), `web_sources` (list)
- `timestamp`

**Body sections (H1 headings):**
- Research Question
- Approach Outline
- Proposed First Experiments
- Theory Of Impact Chain
- Strength Rationale
- Alternative Framings
- Cited Sources

Present a summary of the loaded idea showing title, current scores, novelty classification, and key sections.

Since this idea is **already scored**, do NOT re-score it. Go directly to **Step 4: Collaborative Refinement**. Offer novelty re-assessment as an option (see Step 3).

### If new idea (option 2):

Guide the coordinator to describe their idea. Explain what a complete idea looks like in this system:

> To evaluate your idea thoroughly, I'll need:
> - **Title**: A concise, descriptive title
> - **Research question**: What specific question does this address?
> - **Problem**: What gap or issue motivates this?
> - **Approach outline**: High-level methodology — what would you actually do?
> - **Why it matters**: Theory of impact — how does this connect to AI safety?
>
> Optional but helpful:
> - **Proposed first experiments**: What would the first concrete steps look like?
> - **Relevant prior work**: Any papers or resources you're aware of?
>
> You can provide as much or as little as you have — we'll build it up together.

Accept whatever the coordinator provides and fill in what's missing conversationally. This is collaborative — suggest improvements, ask clarifying questions, help sharpen the framing.

Once the idea is sufficiently described, proceed to **Step 2: Score Against Criteria**.

## Step 2: Score Against Criteria (new ideas only)

**Skip this step for existing ideas that already have scores.**

For EACH scoring criterion (except novelty — that comes from Step 3):
- Read the criterion's rubric levels from the scoring config
- Assess the idea against the rubric
- Assign a score (1-5) with confidence (0.0-1.0) and reasoning
- Consider team/participant constraints when scoring

Present scores:
> **Criteria Scores:**
> - theory_of_impact: X/5 (confidence: Y) — reasoning
> - accessible_complexity: X/5 — reasoning
> - narrow_scope: X/5 — reasoning
> - (etc.)

## Step 3: Novelty Assessment & Citation Verification (optional)

For **new ideas**, run novelty assessment automatically.

For **existing ideas**, offer it as a choice:
> Your idea already has a novelty classification of "[classification]" (score: [score]).
> Would you like me to re-assess novelty against current literature? This includes full literature search, deep reading when needed, and citation verification. (y/n)

If running novelty assessment:

Read and follow the full protocol in `.claude/commands/novelty-check.md`. This includes:
- **Novelty Assessment Protocol** (steps N1-N5): multi-source literature search (WebSearch + CrossRef + Semantic Scholar), evidence collection, deep reading of paper sections when abstract-level evidence is insufficient, novelty classification against the 5-level rubric, and validation
- **Citation Verification Protocol** (steps C1-C3): relevance scoring, verification via lookup APIs, and consequence application for removed citations

Present the results to the coordinator using the Standalone Summary format from `novelty-check.md`.

## Step 4: Collaborative Refinement

This is the core of the skill. Present the current state of the idea and enter a collaborative loop.

> **What would you like to work on?**
> 1. **Discuss** — talk through concerns, questions, or specific aspects of the idea
> 2. **Strengthen weak dimensions** — improve the lowest-scoring criteria
> 3. **Reframe** — explore 2-3 alternative angles on the core insight
> 4. **Sharpen the approach** — make the methodology more concrete
> 5. **Refine experiments** — design or improve first experiments
> 6. **Improve impact chain** — strengthen the theory of why this matters
> 7. **Check novelty** — search literature for related work
> 8. **Save** — write the idea (with improvements) everywhere it exists
> 9. **Done** — end session
>
> Or just tell me what's on your mind — you don't have to pick from the list.

### If discuss (or any free-form input):
Engage naturally with whatever the coordinator wants to talk about. This could be:
- Concerns about feasibility ("I'm worried the compute requirements are too high")
- Questions about framing ("Is this really an alignment problem or more of an evaluation problem?")
- Comparisons ("How does this compare to the approach in paper X?")
- Scope decisions ("Should I focus on just GPT-2 or try multiple models?")
- Any other aspect of the idea

Respond thoughtfully, drawing on the loaded config, scoring criteria, and participant constraints. Suggest concrete changes when appropriate. This is a conversation — follow the coordinator's lead.

### If strengthen:
Identify the weakest scoring dimensions. For each:
- Explain why the score was low (referencing the rubric)
- Suggest specific, concrete improvements
- Rewrite the relevant sections with improvements applied
- Re-score to show the improvement

### If reframe:
Generate 2-3 alternative framings of the core insight:
- Each takes a different methodological or conceptual angle
- Each is tailored to the participant's constraints
- Include estimated scores for each framing so the coordinator can compare tradeoffs

### If sharpen approach:
Work with the coordinator to make the methodology more concrete:
- What specific tools, datasets, or models would be used?
- What are the key assumptions and how would you test them?
- What's the minimum viable experiment?

### If refine experiments:
Help design concrete first experiments:
- Break down into time-boxed steps
- Consider the participant's compute and skill constraints
- Identify what each experiment would prove or disprove

### If improve impact chain:
Strengthen the connection to AI safety:
- Why does this specific question matter?
- What decisions or actions would change based on the results?
- How does this connect to broader safety research agendas?

### If check novelty:
Run the full novelty assessment and citation verification protocol from Step 3 (i.e., follow `.claude/commands/novelty-check.md`).

### If save:
Save the idea with all improvements to **every location where it exists**:

1. **`data/ideas/<idea_id>.md`** — the primary idea file. Use the existing filename if updating an existing idea, or `<sanitized_title>.md` for new ideas. Include full YAML frontmatter and all body sections.

2. **Pipeline run stages** — if the idea came from a pipeline run (`run_id` is set and not "unknown"), check for the idea in `data/runs/<run_id>/` stage directories (generate/, filter_score/, refine/, rank/). For individual `.md` files, update them. For batch `.json` files, load the batch, find the matching idea by `idea_id`, update its fields, and write back.

3. **Selected ideas file** — check if a selected ideas file exists at the path configured by `SELECTED_IDEAS_FILE` in `src/safety_ideas/constants.py` (default: `data/output/selected_ideas.md`). If the file exists and contains this idea (match by idea_id or title), update the idea's section in that file. If saving a new idea that isn't in the file yet, ask the coordinator whether to add it.

```bash
uv run python -c "from safety_ideas.constants import SELECTED_IDEAS_FILE; print(SELECTED_IDEAS_FILE)"
```

For all locations, preserve the full structure:
- YAML frontmatter: idea_id, run_id, stage, rank, weighted_score, title, subfield, generation_strategy, novelty_classification, novelty_score, novelty_method, original_scores, provenance, timestamp
- Body sections: Research Question, Approach Outline, Proposed First Experiments, Theory Of Impact Chain, Strength Rationale, Alternative Framings, Cited Sources

Report which files were updated.

Return to the refinement menu until the user chooses "Done".

## Session Summary

When done, provide:
- Summary of changes made to the idea
- Current scores (if scored)
- Whether the idea was saved
- Suggestions for next steps (e.g., run full pipeline, try `/brainstorm` for related directions)
