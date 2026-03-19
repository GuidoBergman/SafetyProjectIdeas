# Configure Teams

Manage BAISH team profiles, scoring criteria, pipeline settings, and participant profiles.

## Getting Started

**IMPORTANT:** Before presenting any configuration options to the user, always read the Pydantic schemas in `src/safety_ideas/config/schemas.py` and `src/safety_ideas/config/participants.py` to discover the current valid values for all constrained fields (Literals, enums, validators). Do not assume values — they may have changed. Always list all valid values for each constrained field when presenting options to the user.

First, display the current configuration:

```bash
uv run python -m safety_ideas.config.cli show
```

After running `show`, you MUST present the user with a clear summary of all current settings, organized as follows:

1. **Default team** — which team is currently the default (used when no team is specified at pipeline runtime). Explicitly tell the user they can change this.
2. **Default participant** — which participant is currently the default (used when no participant is specified at pipeline runtime). List the current default participant and offer to change it.
3. **Team profiles** — list each team by name and type, noting which is the default.
4. **Scoring criteria** — list each criterion with its current default_weight.
5. **Pipeline settings** — model assignments per stage and thresholds.
6. **Participant profiles** — any saved profiles and their settings, noting which (if any) is the default.
7. **Schema defaults** — mention that new participant profiles default to compute_resources=low and time_availability=part_time unless overridden.

Then ask the user what they'd like to change. Every setting shown should be presented as configurable.

## Shipped Defaults (reference)

These are the factory defaults. Always run `show` to confirm current values — they may have been changed.

- **Default team:** `mentor_novice` (configurable via `set-default-team`)
- **Default participant:** none (configurable via `set-default-participant`)
- **Team profiles:** `mentor_novice`, `solo_novice`, `experienced_group`
- **Scoring criteria:** `theory_of_impact` (1.5), `low_compute` (1.5), `accessible_complexity` (1.5), `narrow_scope` (1.5), `novelty` (1.0)
- **Pipeline models:** source=haiku, generate=sonnet, filter_score=sonnet, refine=opus, rank=haiku
- **Pipeline thresholds:** filter_score (min_score=2.5, max_ideas=20), rank (min_score=3.0, max_ideas=10)
- **Participant schema defaults:** compute_resources=low, time_availability=part_time

## Available Operations

### Default Team
- **Set the default team** - The default team is used when no team is specified at pipeline runtime

To set the default team:
```bash
uv run python -m safety_ideas.config.cli set-default-team <team_type>
```

### Team Profiles
- **Add/edit a team profile** - Specify name, team_type, compute_budget, technical_skills, and criteria_weights
- **Remove a team profile** - Remove by team_type (cannot remove the current default team)

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

### Default Participant
- **Set the default participant** - The default participant is used when no participant is specified at pipeline runtime
- **Clear the default participant** - Remove the default so no participant is pre-selected

To set the default participant:
```bash
uv run python -m safety_ideas.config.cli set-default-participant <name>
```

To clear the default participant:
```bash
uv run python -m safety_ideas.config.cli clear-default-participant
```

### Participant Profiles
- **Add/edit participant profiles** - Specify name, experience_level, technical_background, compute_resources, time_availability
- **Set as default** - After adding a profile, offer to set it as the default participant
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

1. Run `show` and present ALL current settings to the user — default team, default participant, team profiles, criteria weights, pipeline models/thresholds, participant profiles, and schema defaults. Every value shown must be presented as something the user can change.
2. Ask: "What would you like to change?" — explicitly mention key options: set default team, set default participant, add/edit/remove teams, modify criteria weights, change pipeline models or thresholds, manage participants.
3. Validate and save changes to the appropriate YAML files.
4. After each change, re-run `show` to confirm the update took effect.
5. Changes persist across sessions (FR57) — the user can also edit the YAML files directly.

All configuration files are in the `config/` directory:
- `config/teams.yaml` - Team profiles, default_team, and default_participant settings
- `config/criteria.yaml` - Scoring criteria with weights
- `config/pipeline.yaml` - Pipeline settings and model assignments
- `config/participants/<name>.yaml` - Individual participant profiles
