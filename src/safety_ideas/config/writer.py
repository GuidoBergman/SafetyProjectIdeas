"""Configuration writer with Pydantic validation before save."""

from pathlib import Path

import yaml
from pydantic import ValidationError

from safety_ideas.config.schemas import (
    DEFAULT_TEAM,
    KBCriteria,
    ParticipantProfile,
    PipelineSettings,
    ScoringCriteria,
    StageModelAssignment,
    StageThreshold,
    TeamProfile,
    TeamType,
)
from safety_ideas.constants import (
    CRITERIA_CONFIG,
    KB_CRITERIA_CONFIG,
    PARTICIPANTS_DIR,
    PIPELINE_CONFIG,
    TEAMS_CONFIG,
)


def _write_yaml(path: Path, data: dict) -> None:
    """Write data to a YAML file, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def save_teams(
    teams: list[TeamProfile],
    path: Path | None = None,
    default_team: TeamType | None = None,
) -> None:
    """Validate and save team profiles to YAML.

    Args:
        teams: List of TeamProfile objects to save.
        path: Override file path (defaults to config/teams.yaml).
        default_team: Default team type for pipeline runs. Preserved from
            existing file if not specified.

    Raises:
        ValidationError: If any team profile fails validation.
    """
    # Re-validate all profiles before saving
    validated = []
    for team in teams:
        validated.append(TeamProfile.model_validate(team.model_dump()))

    # Preserve existing default_team from file if not explicitly provided
    target = path or TEAMS_CONFIG
    if default_team is None and target.exists():
        from safety_ideas.utils import load_yaml

        existing = load_yaml(target)
        default_team = existing.get("default_team", DEFAULT_TEAM)

    data = {
        "default_team": default_team or DEFAULT_TEAM,
        "teams": [t.model_dump() for t in validated],
    }
    _write_yaml(target, data)


def save_criteria(criteria: list[ScoringCriteria], path: Path | None = None) -> None:
    """Validate and save scoring criteria to YAML.

    Args:
        criteria: List of ScoringCriteria objects to save.
        path: Override file path (defaults to config/criteria.yaml).

    Raises:
        ValidationError: If any criterion fails validation.
    """
    validated = []
    for c in criteria:
        validated.append(ScoringCriteria.model_validate(c.model_dump()))

    data = {
        "criteria": [c.model_dump() for c in validated]
    }
    _write_yaml(path or CRITERIA_CONFIG, data)


def save_pipeline(pipeline: PipelineSettings, path: Path | None = None) -> None:
    """Validate and save pipeline settings to YAML.

    Args:
        pipeline: PipelineSettings object to save.
        path: Override file path (defaults to config/pipeline.yaml).

    Raises:
        ValidationError: If pipeline settings fail validation.
    """
    validated = PipelineSettings.model_validate(pipeline.model_dump())
    _write_yaml(path or PIPELINE_CONFIG, validated.model_dump())


def save_participant(profile: ParticipantProfile, path: Path | None = None) -> None:
    """Validate and save a participant profile to YAML.

    Args:
        profile: ParticipantProfile object to save.
        path: Override file path (defaults to config/participants/<name>.yaml).

    Raises:
        ValidationError: If profile fails validation.
    """
    validated = ParticipantProfile.model_validate(profile.model_dump())
    if path is None:
        filename = validated.name.lower().replace(" ", "_") + ".yaml"
        path = PARTICIPANTS_DIR / filename
    _write_yaml(path, validated.model_dump())
