# Brainstorm AI Safety Research Ideas

Interactive collaborative brainstorming of AI Safety research directions, tailored to team constraints and participant profiles.

## Setup

Load project configuration:

```bash
uv run python -m saim.config.cli show-scoring
```

Load team profile:

```bash
uv run python -m saim.config.cli show
```

Load participant profile (if available):

```bash
uv run python -m saim.config.cli show-participant
```

If the participant output shows "NO_PARTICIPANT", guide the user conversationally:
> No participant profile found. To tailor ideas to your constraints, tell me about:
> 1. Your background and experience level
> 2. Technical skills (programming languages, ML experience)
> 3. Available compute resources
> 4. Time budget for the project
> 5. Expected deliverables
>
> Or type "skip" to brainstorm without constraints.

Save these constraints for use throughout the session.

Load previous ideas for divergence (avoid duplicates):

```bash
uv run python -m saim.pipeline.memory
```

Echo the active context:
> **Brainstorming with:** team=[team_type], participant=[name or "none"], previous_ideas=[count]

## Interactive Brainstorming Loop

Enter collaborative mode. For each user input:

### If the user provides a topic, area, or problem direction (FR44, FR45):

Generate 3-5 research idea sketches tailored to:
- The specified topic/area/problem
- Team constraints (compute, skills, time from team and participant profiles)
- Previous ideas (avoid duplicating titles from pipeline memory)
- KB context (reference relevant papers/findings if KB is available)

For each idea, provide:
- **Title**: Concise, descriptive
- **Problem**: What gap or question this addresses
- **Approach**: High-level methodology
- **Why it fits**: How it matches the participant's constraints
- **Estimated scope**: Rough time/compute requirements

### If the user asks a research question (FR48):

Assess whether the question has been addressed in the literature:
1. Search for relevant work using citation tools:

```bash
uv run python -m saim.verification.citation search-crossref '<query>'
```

```bash
uv run python -m saim.verification.citation search-s2 '<query>'
```

2. Summarize findings: what's been done, what gaps remain, and whether the question is open or largely resolved.

### If the user wants to refine or iterate (FR46):

- Accept feedback on proposed ideas
- Strengthen weak aspects
- Combine elements from different ideas
- Adjust scope to better fit constraints
- Generate variations on promising directions

### If the user wants to save an idea:

Mint an ID with the shared generator — never write one by hand and never use a sequential ID or a title slug:

```bash
uv run python -m saim.ids
```

Write the idea as `data/ideas/<idea_id>.md`, using the printed ID (e.g. `gen-3f9a1c04`) as both the filename and the `idea_id` in the YAML frontmatter. This makes it available to future pipeline runs via pipeline memory.

Continue the loop until the user indicates they're done (e.g., "done", "exit", "that's enough").

## Session Summary

When the session ends, provide:
- Count of ideas explored
- List of any ideas saved to `data/ideas/`
- Suggestions for next steps (e.g., run `/grill-idea` on favorites, run full pipeline)
