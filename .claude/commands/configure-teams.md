# Configure Teams

Manage BAISH team profiles, scoring criteria, pipeline settings, and participant profiles.

## Getting Started

**IMPORTANT:** Before presenting any configuration options to the user, always read the Pydantic schemas in `src/safety_ideas/config/schemas.py` and `src/safety_ideas/config/participants.py` to discover the current valid values for all constrained fields (Literals, enums, validators). Do not assume values — they may have changed. Always list all valid values for each constrained field when presenting options to the user.

First, display the current configuration:

```bash
uv run python -m safety_ideas.config.cli show
```

Review the output and tell me what you'd like to change. I can help with:

## Available Operations

### Team Profiles
- **Add/edit a team profile** - Specify name, team_type, compute_budget, technical_skills, and criteria_weights
- **Remove a team profile** - Remove by team_type

When presenting team profile options, read the schemas to list all current valid values for `team_type`, `compute_budget`, and `technical_skills`.

To add or update a team:
```bash
uv run python -m safety_ideas.config.cli add-team '{"name": "Team Name", "team_type": "<valid_team_type>", "compute_budget": "<valid_budget>", "technical_skills": ["<valid_skill>"], "criteria_weights": {"<criterion_name>": 2.0}}'
```

To remove a team:
```bash
uv run python -m safety_ideas.config.cli remove-team <team_type>
```

### Scoring Criteria
- **Add/edit scoring criteria** - Specify name, description, and default_weight (0-5)
- **Add custom criteria** beyond the default set (FR54)
- **Remove scoring criteria** by name
- Per-team weight overrides are configured in team profiles via `criteria_weights`

When presenting criteria options, read the schemas to list the valid range for `default_weight`. Also check `config/criteria.yaml` for the existing criteria names.

To add or update a criterion:
```bash
uv run python -m safety_ideas.config.cli add-criterion '{"name": "learning_value", "description": "Does this project teach the researcher important safety concepts?", "default_weight": 2.0}'
```

To remove a criterion:
```bash
uv run python -m safety_ideas.config.cli remove-criterion learning_value
```

> **Note:** The "novelty" criterion is derived from the hybrid novelty assessment (FR34) — its score comes from evidence-based search, not manual assignment. Its weight is configurable per team type via `criteria_weights` in team profiles.

### Pipeline Settings (FR55)
- **Change model assignments** per pipeline stage
- **Adjust thresholds** for filter stages

When presenting pipeline options, read the schemas to list all valid pipeline stage names, model options, and threshold constraints.

To update pipeline settings:
```bash
uv run python -m safety_ideas.config.cli update-pipeline '{"model_assignments": {"<stage>": {"model": "<model>", "fallback": "<model>"}}, "thresholds": {"<stage>": {"min_score": 3.0, "max_ideas": 15}}}'
```

### Participant Profiles
- **Add/edit participant profiles** - Specify name, experience_level, technical_background, compute_resources, time_availability
- Profiles are saved to `config/participants/<name>.yaml`
- Profiles are auto-loaded when available (AC3), with conversational fallback when not (AC4)

When presenting participant options, read the schemas to list all valid values for `experience_level`, `compute_resources`, `time_availability`, and `technical_background`.

To save a participant profile:
```bash
uv run python -m safety_ideas.config.cli save-participant '{"name": "alice", "experience_level": "<valid_level>", "technical_background": ["<valid_skill>"], "compute_resources": "<valid_resource>", "time_availability": "<valid_availability>"}'
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
