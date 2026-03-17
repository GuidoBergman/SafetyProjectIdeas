"""CLI entry point for configuration management operations.

Invoked by the /configure-teams skill via:
    uv run python -m safety_ideas.config.cli <command> [args]
"""

import json
import sys
from pathlib import Path

import yaml
from pydantic import ValidationError

from safety_ideas.config.loader import load_config
from safety_ideas.config.participants import list_participants, load_participant
from safety_ideas.config.schemas import (
    ParticipantProfile,
    PipelineSettings,
    ScoringCriteria,
    StageModelAssignment,
    StageThreshold,
    TeamProfile,
)
from safety_ideas.config.writer import (
    save_criteria,
    save_participant,
    save_pipeline,
    save_teams,
)
from safety_ideas.constants import CONFIG_DIR, PARTICIPANTS_DIR


def show_config() -> None:
    """Display current configuration summary."""
    config = load_config(load_env=False)

    print("=== Team Profiles ===")
    for team_type, team in config.teams.items():
        print(f"\n  [{team_type}] {team.name}")
        print(f"    Compute: {team.compute_budget}")
        print(f"    Skills: {', '.join(team.technical_skills) if team.technical_skills else 'none'}")
        if team.criteria_weights:
            print(f"    Weight overrides: {team.criteria_weights}")

    print("\n=== Scoring Criteria ===")
    for c in config.criteria:
        print(f"\n  [{c.name}] {c.description}")
        print(f"    Default weight: {c.default_weight}")
        if c.team_type_overrides:
            print(f"    Overrides: {c.team_type_overrides}")

    print("\n=== Pipeline Settings ===")
    for stage, assignment in config.pipeline.model_assignments.items():
        fallback = f" (fallback: {assignment.fallback})" if assignment.fallback else ""
        print(f"  {stage}: {assignment.model}{fallback}")
    for stage, threshold in config.pipeline.thresholds.items():
        print(f"  {stage} threshold: min_score={threshold.min_score}, max_ideas={threshold.max_ideas}")

    print("\n=== Participant Profiles ===")
    participants = list_participants()
    if participants:
        for p in participants:
            print(f"\n  [{p.name}] {p.experience_level}")
            print(f"    Background: {', '.join(p.technical_background) if p.technical_background else 'none'}")
            print(f"    Compute: {p.compute_resources}, Time: {p.time_availability}")
    else:
        print("  No participant profiles found.")


def validate_team_json(json_str: str) -> None:
    """Validate a team profile JSON string against schema."""
    try:
        data = json.loads(json_str)
        team = TeamProfile(**data)
        print(f"Valid team profile: {team.name} ({team.team_type})")
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"VALIDATION ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def validate_criterion_json(json_str: str) -> None:
    """Validate a scoring criterion JSON string against schema."""
    try:
        data = json.loads(json_str)
        criterion = ScoringCriteria(**data)
        print(f"Valid criterion: {criterion.name}")
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"VALIDATION ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def validate_participant_json(json_str: str) -> None:
    """Validate a participant profile JSON string against schema."""
    try:
        data = json.loads(json_str)
        profile = ParticipantProfile(**data)
        print(f"Valid participant profile: {profile.name}")
    except (json.JSONDecodeError, ValidationError) as e:
        print(f"VALIDATION ERROR: {e}", file=sys.stderr)
        sys.exit(1)


def add_team(json_str: str) -> None:
    """Add or update a team profile."""
    data = json.loads(json_str)
    team = TeamProfile(**data)
    config = load_config(load_env=False)
    teams_list = list(config.teams.values())
    # Replace if same team_type exists, otherwise append
    teams_list = [t for t in teams_list if t.team_type != team.team_type]
    teams_list.append(team)
    save_teams(teams_list)
    print(f"Saved team profile: {team.name} ({team.team_type})")


def remove_team(team_type: str) -> None:
    """Remove a team profile by team_type."""
    config = load_config(load_env=False)
    if team_type not in config.teams:
        print(f"Team type '{team_type}' not found.", file=sys.stderr)
        sys.exit(1)
    teams_list = [t for t in config.teams.values() if t.team_type != team_type]
    save_teams(teams_list)
    print(f"Removed team profile: {team_type}")


def add_criterion(json_str: str) -> None:
    """Add or update a scoring criterion."""
    data = json.loads(json_str)
    criterion = ScoringCriteria(**data)
    config = load_config(load_env=False)
    criteria_list = [c for c in config.criteria if c.name != criterion.name]
    criteria_list.append(criterion)
    save_criteria(criteria_list)
    print(f"Saved criterion: {criterion.name}")


def remove_criterion(name: str) -> None:
    """Remove a scoring criterion by name."""
    config = load_config(load_env=False)
    before = len(config.criteria)
    criteria_list = [c for c in config.criteria if c.name != name]
    if len(criteria_list) == before:
        print(f"Criterion '{name}' not found.", file=sys.stderr)
        sys.exit(1)
    save_criteria(criteria_list)
    print(f"Removed criterion: {name}")


def update_pipeline(json_str: str) -> None:
    """Update pipeline settings (merge with existing)."""
    data = json.loads(json_str)
    config = load_config(load_env=False)
    current = config.pipeline.model_dump()
    # Merge model_assignments
    if "model_assignments" in data:
        current["model_assignments"].update(data["model_assignments"])
    # Merge thresholds
    if "thresholds" in data:
        current["thresholds"].update(data["thresholds"])
    pipeline = PipelineSettings(**current)
    save_pipeline(pipeline)
    print("Pipeline settings updated.")


def save_participant_cmd(json_str: str) -> None:
    """Save a participant profile."""
    data = json.loads(json_str)
    profile = ParticipantProfile(**data)
    save_participant(profile)
    print(f"Saved participant profile: {profile.name}")


def main() -> None:
    """CLI dispatcher."""
    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.config.cli <command> [args]")
        print("Commands: show, validate-team, validate-criterion, validate-participant,")
        print("          add-team, remove-team, add-criterion, remove-criterion,")
        print("          update-pipeline, save-participant")
        sys.exit(1)

    command = sys.argv[1]

    if command == "show":
        show_config()
    elif command == "validate-team":
        validate_team_json(sys.argv[2])
    elif command == "validate-criterion":
        validate_criterion_json(sys.argv[2])
    elif command == "validate-participant":
        validate_participant_json(sys.argv[2])
    elif command == "add-team":
        add_team(sys.argv[2])
    elif command == "remove-team":
        remove_team(sys.argv[2])
    elif command == "add-criterion":
        add_criterion(sys.argv[2])
    elif command == "remove-criterion":
        remove_criterion(sys.argv[2])
    elif command == "update-pipeline":
        update_pipeline(sys.argv[2])
    elif command == "save-participant":
        save_participant_cmd(sys.argv[2])
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
