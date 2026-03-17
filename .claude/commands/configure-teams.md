# Configure Teams

Manage BAISH team profiles, scoring criteria, pipeline settings, and participant profiles.

## Getting Started

First, display the current configuration:

```bash
uv run python -m safety_ideas.config.cli show
```

Review the output and tell me what you'd like to change. I can help with:

## Available Operations

### Team Profiles
- **Add/edit a team profile** - Specify name, team_type (mentor_novice | solo_novice | experienced_group), compute_budget, technical_skills, and criteria_weights
- **Remove a team profile** - Remove by team_type

To add or update a team:
```bash
uv run python -m safety_ideas.config.cli add-team '{"name": "Team Name", "team_type": "mentor_novice", "compute_budget": "low", "technical_skills": ["python_basics"], "criteria_weights": {"low_compute": 2.0}}'
```

To remove a team:
```bash
uv run python -m safety_ideas.config.cli remove-team mentor_novice
```

### Scoring Criteria
- **Add/edit scoring criteria** - Specify name, description, default_weight (0-10), and optional team_type_overrides
- **Add custom criteria** beyond the default set (FR54)
- **Remove scoring criteria** by name
- **Modify weights** per team type

To add or update a criterion:
```bash
uv run python -m safety_ideas.config.cli add-criterion '{"name": "novelty", "description": "How novel is this idea?", "default_weight": 2.0, "team_type_overrides": {"experienced_group": 3.0}}'
```

To remove a criterion:
```bash
uv run python -m safety_ideas.config.cli remove-criterion novelty
```

### Pipeline Settings (FR55)
- **Change model assignments** per pipeline stage (source, generate, filter_score, refine, rank)
- **Adjust thresholds** for filter stages (min_score, max_ideas)

To update pipeline settings:
```bash
uv run python -m safety_ideas.config.cli update-pipeline '{"model_assignments": {"generate": {"model": "opus", "fallback": "sonnet"}}, "thresholds": {"filter_score": {"min_score": 6.0, "max_ideas": 15}}}'
```

### Participant Profiles
- **Add/edit participant profiles** - Specify name, experience_level, technical_background, compute_resources, time_availability
- Profiles are saved to `config/participants/<name>.yaml`
- Profiles are auto-loaded when available (AC3), with conversational fallback when not (AC4)

To save a participant profile:
```bash
uv run python -m safety_ideas.config.cli save-participant '{"name": "alice", "experience_level": "beginner", "technical_background": ["python_basics"], "compute_resources": "low", "time_availability": "part_time"}'
```

## Validation

All changes are validated against Pydantic schemas before saving. If validation fails, the error is displayed and no changes are written to disk (FR57).

To validate without saving:
```bash
uv run python -m safety_ideas.config.cli validate-team '{"name": "Test", "team_type": "mentor_novice", "compute_budget": "low"}'
uv run python -m safety_ideas.config.cli validate-criterion '{"name": "test", "description": "desc", "default_weight": 2.0}'
uv run python -m safety_ideas.config.cli validate-participant '{"name": "test", "experience_level": "beginner"}'
```

## Workflow

1. I'll show you the current configuration
2. Tell me what you'd like to change (add team, modify weights, add custom criteria, etc.)
3. I'll validate the changes and save them to the appropriate YAML files
4. Changes persist across sessions (FR57) -- you can also edit the YAML files directly

All configuration files are in the `config/` directory:
- `config/teams.yaml` - Team profiles
- `config/criteria.yaml` - Scoring criteria with weights
- `config/pipeline.yaml` - Pipeline settings and model assignments
- `config/participants/<name>.yaml` - Individual participant profiles
