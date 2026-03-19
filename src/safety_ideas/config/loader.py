"""Configuration loader with validation."""

import logging
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv
from pydantic import ValidationError

from safety_ideas.config.schemas import (
    DEFAULT_TEAM,
    GenerateSettings,
    KBCriteria,
    PipelineSettings,
    ScoringCriteria,
    TeamProfile,
    TeamType,
)
from safety_ideas.constants import PROJECT_ROOT
from safety_ideas.utils import load_yaml

logger = logging.getLogger(__name__)


@dataclass
class AppConfig:
    """Container for all validated configuration."""

    teams: dict[str, TeamProfile] = field(default_factory=dict)
    default_team: TeamType = DEFAULT_TEAM
    default_participant: str | None = None
    criteria: list[ScoringCriteria] = field(default_factory=list)
    pipeline: PipelineSettings = field(default_factory=PipelineSettings)
    kb_criteria: KBCriteria = field(default_factory=KBCriteria)


def _load_teams(path: Path) -> tuple[dict[str, TeamProfile], TeamType, str | None]:
    """Load and validate team profiles, default_team, and default_participant from YAML."""
    data = load_yaml(path)
    teams = {}
    for team_data in data.get("teams", []):
        try:
            profile = TeamProfile(**team_data)
            teams[profile.team_type] = profile
        except ValidationError as e:
            raise ValueError(f"Invalid team profile in {path}: {e}") from e
    default_team: TeamType = data.get("default_team", DEFAULT_TEAM)
    if teams and default_team not in teams:
        raise ValueError(
            f"default_team '{default_team}' in {path} does not match any defined team type. "
            f"Available: {list(teams.keys())}"
        )
    raw = data.get("default_participant")
    default_participant: str | None = raw if raw is not None and raw != "null" else None
    return teams, default_team, default_participant


def _load_criteria(path: Path) -> list[ScoringCriteria]:
    """Load and validate scoring criteria from YAML."""
    data = load_yaml(path)
    criteria = []
    for criterion_data in data.get("criteria", []):
        try:
            criteria.append(ScoringCriteria(**criterion_data))
        except ValidationError as e:
            raise ValueError(f"Invalid scoring criterion in {path}: {e}") from e
    return criteria


def _load_pipeline(path: Path) -> PipelineSettings:
    """Load and validate pipeline settings from YAML."""
    data = load_yaml(path)
    try:
        return PipelineSettings(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid pipeline settings in {path}: {e}") from e


def _load_kb_criteria(path: Path) -> KBCriteria:
    """Load and validate KB inclusion criteria from YAML."""
    data = load_yaml(path)
    try:
        return KBCriteria(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid KB criteria in {path}: {e}") from e


def load_config(
    config_dir: Path | None = None,
    load_env: bool = True,
) -> AppConfig:
    """Load and validate all configuration files.

    Args:
        config_dir: Override config directory (defaults to project config/).
        load_env: Whether to load .env file via python-dotenv.

    Returns:
        Validated AppConfig with all configuration.

    Raises:
        FileNotFoundError: If required config files are missing.
        ValueError: If config files contain invalid data.
    """
    if load_env:
        env_path = PROJECT_ROOT / ".env"
        load_dotenv(env_path)
        logger.debug("Loaded .env from %s", env_path)

    if config_dir is None:
        config_dir = PROJECT_ROOT / "config"

    teams_path = config_dir / "teams.yaml"
    criteria_path = config_dir / "criteria.yaml"
    pipeline_path = config_dir / "pipeline.yaml"
    kb_criteria_path = config_dir / "kb-criteria.yaml"

    teams, default_team, default_participant = _load_teams(teams_path)

    return AppConfig(
        teams=teams,
        default_team=default_team,
        default_participant=default_participant,
        criteria=_load_criteria(criteria_path),
        pipeline=_load_pipeline(pipeline_path),
        kb_criteria=_load_kb_criteria(kb_criteria_path),
    )
