"""Participant profile loading and auto-detection."""

import logging
from pathlib import Path

from pydantic import ValidationError

from safety_ideas.config.schemas import ParticipantProfile
from safety_ideas.constants import PARTICIPANTS_DIR, TEAMS_CONFIG
from safety_ideas.utils import load_yaml

logger = logging.getLogger(__name__)


def load_participant(name: str, participants_dir: Path | None = None) -> ParticipantProfile | None:
    """Load a participant profile by name.

    Looks for config/participants/<name>.yaml (case-insensitive, spaces replaced with underscores).

    Args:
        name: Participant name to look up.
        participants_dir: Override directory (defaults to config/participants/).

    Returns:
        Validated ParticipantProfile if found, None otherwise.

    Raises:
        ValueError: If profile file exists but contains invalid data.
    """
    if participants_dir is None:
        participants_dir = PARTICIPANTS_DIR

    filename = name.lower().replace(" ", "_") + ".yaml"
    path = participants_dir / filename

    if not path.exists():
        logger.info("No participant profile found for '%s' at %s", name, path)
        return None

    data = load_yaml(path)
    try:
        return ParticipantProfile(**data)
    except ValidationError as e:
        raise ValueError(f"Invalid participant profile in {path}: {e}") from e


def list_participants(participants_dir: Path | None = None) -> list[ParticipantProfile]:
    """Load all participant profiles from the participants directory.

    Args:
        participants_dir: Override directory (defaults to config/participants/).

    Returns:
        List of validated ParticipantProfile objects.
    """
    if participants_dir is None:
        participants_dir = PARTICIPANTS_DIR

    if not participants_dir.exists():
        return []

    profiles = []
    for path in sorted(participants_dir.glob("*.yaml")):
        data = load_yaml(path)
        try:
            profiles.append(ParticipantProfile(**data))
        except ValidationError as e:
            logger.warning("Skipping invalid participant profile %s: %s", path, e)
    return profiles


def get_default_participant(participants_dir: Path | None = None) -> ParticipantProfile | None:
    """Load the default participant profile if one is configured.

    Reads the default_participant setting from teams.yaml and loads that profile.

    Args:
        participants_dir: Override directory (defaults to config/participants/).

    Returns:
        ParticipantProfile if a default is configured and valid, None otherwise.
    """
    if not TEAMS_CONFIG.exists():
        return None

    data = load_yaml(TEAMS_CONFIG)
    default_name = data.get("default_participant")
    if not default_name or default_name == "null":
        return None

    return get_participant_or_none(default_name, participants_dir)


def get_participant_or_none(name: str, participants_dir: Path | None = None) -> ParticipantProfile | None:
    """Auto-detect participant profile, returning None for conversational fallback.

    This is the main entry point for pipeline stages and skills:
    - If a profile exists, load and return it (AC3)
    - If no profile exists, return None to signal conversational fallback (AC4)

    Args:
        name: Participant name to look up.
        participants_dir: Override directory.

    Returns:
        ParticipantProfile if found, None for conversational fallback.
    """
    try:
        return load_participant(name, participants_dir)
    except ValueError:
        logger.warning("Invalid profile for '%s', falling back to conversational discovery", name)
        return None
