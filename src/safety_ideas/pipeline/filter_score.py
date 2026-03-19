"""Filter/score stage: scoring computation, staged filtering, and scored idea I/O."""

import json
from datetime import UTC, datetime
from pathlib import Path

from safety_ideas.config.schemas import ScoringCriteria, StageThreshold, TeamProfile
from safety_ideas.constants import STAGE1_RELEVANCE_THRESHOLD


def score_idea(idea: dict, criteria: list[ScoringCriteria], team_profile: TeamProfile) -> dict:
    """Build a scored idea dict structure from an idea and its per-criterion scores.

    This function creates the scored idea *skeleton* with metadata.  The actual
    per-criterion scores (with reasoning) are expected to be filled in by the
    calling skill via LLM evaluation.  The skeleton includes empty score slots
    so the caller knows which criteria to evaluate.

    Args:
        idea: Idea dict (from the generate stage).
        criteria: List of scoring criteria from config.
        team_profile: Team profile for weight overrides.

    Returns:
        A scored idea dict ready to be populated with scores.
    """
    now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    idea_id = idea.get("idea_id", "unknown")
    run_id = idea.get("run_id", "unknown")

    scored = {
        "idea_id": idea_id,
        "run_id": run_id,
        "stage": "filter_score",
        "timestamp": now,
        "title": idea.get("title", ""),
        "original_idea": idea,
        "filter_stage_passed": 0,
        "scores": {
            c.name: {"score": 0, "reasoning": "", "confidence": 0.0} for c in criteria
        },
        "novelty_assessment": {
            "classification": "",
            "evidence": [],
            "confidence": 0.0,
            "derived_score": 0,
        },
        "citation_verification": {
            "verified": [],
            "failed": [],
            "removed": [],
        },
        "weighted_score": 0.0,
        "confidence": 0.0,
        "eliminated": False,
        "elimination_reason": None,
    }
    return scored


def apply_weights(
    scores: dict[str, dict],
    criteria: list[ScoringCriteria],
    team_profile: TeamProfile,
) -> float:
    """Compute a weighted score from per-criterion scores.

    For each criterion, uses the team's criteria_weights override if present,
    otherwise the criterion's default_weight.

    Args:
        scores: Dict of criterion_name -> {score, reasoning, confidence}.
        criteria: List of scoring criteria (for default weights).
        team_profile: Team profile (for weight overrides).

    Returns:
        Weighted average score as a float.
    """
    total_weighted = 0.0
    total_weight = 0.0

    criteria_by_name = {c.name: c for c in criteria}

    for name, score_entry in scores.items():
        score_val = score_entry.get("score", 0)
        if score_val == 0:
            continue

        # Team override takes priority, then criterion default
        if name in team_profile.criteria_weights:
            weight = team_profile.criteria_weights[name]
        elif name in criteria_by_name:
            weight = criteria_by_name[name].default_weight
        else:
            weight = 1.0

        total_weighted += score_val * weight
        total_weight += weight

    if total_weight == 0:
        return 0.0
    return total_weighted / total_weight


def staged_filter(
    ideas: list[dict],
    criteria: list[ScoringCriteria],
    thresholds: StageThreshold,
    team_profile: TeamProfile,
) -> list[dict]:
    """Apply staged filtering to a list of scored idea dicts.

    Stage 1: Quick relevance — eliminate ideas with weighted_score < 2.0.
    Stage 2: Full scoring — eliminate ideas below thresholds.min_score (default 2.5).
    Stage 3: Novelty hard gate — eliminate ideas classified as "already_solved".

    Each stage updates the ``filter_stage_passed``, ``eliminated``, and
    ``elimination_reason`` fields on the scored idea dicts **in place**.

    Args:
        ideas: List of scored idea dicts (must already have scores populated).
        criteria: Scoring criteria list.
        thresholds: Stage threshold settings from pipeline config.
        team_profile: Team profile for weight computation.

    Returns:
        List of surviving (non-eliminated) scored idea dicts.
    """
    survivors = []

    for idea in ideas:
        # Stage 1: Quick relevance check (threshold 2.0)
        weighted = apply_weights(idea.get("scores", {}), criteria, team_profile)
        idea["weighted_score"] = weighted

        if weighted < STAGE1_RELEVANCE_THRESHOLD:
            idea["eliminated"] = True
            idea["elimination_reason"] = (
                f"Stage 1: weighted score {weighted:.2f} < {STAGE1_RELEVANCE_THRESHOLD}"
            )
            idea["filter_stage_passed"] = 0
            continue

        idea["filter_stage_passed"] = 1

        # Stage 2: Full scoring threshold
        min_score = thresholds.min_score
        if weighted < min_score:
            idea["eliminated"] = True
            idea["elimination_reason"] = (
                f"Stage 2: weighted score {weighted:.2f} < {min_score}"
            )
            idea["filter_stage_passed"] = 1
            continue

        idea["filter_stage_passed"] = 2

        # Stage 3: Novelty hard gate
        novelty = idea.get("novelty_assessment", {})
        classification = novelty.get("classification", "")
        if classification == "already_solved":
            idea["eliminated"] = True
            idea["elimination_reason"] = (
                "Stage 3: novelty classification is 'already_solved' (hard gate)"
            )
            idea["filter_stage_passed"] = 2
            continue

        idea["filter_stage_passed"] = 3
        survivors.append(idea)

    # Enforce max_ideas by taking top scorers
    if len(survivors) > thresholds.max_ideas:
        survivors.sort(key=lambda x: x.get("weighted_score", 0), reverse=True)
        for dropped in survivors[thresholds.max_ideas :]:
            dropped["eliminated"] = True
            dropped["elimination_reason"] = (
                f"Exceeded max_ideas limit ({thresholds.max_ideas})"
            )
        survivors = survivors[: thresholds.max_ideas]

    return survivors


def write_scored_idea(run_dir: Path, scored: dict) -> Path:
    """Write a scored idea as a JSON file in filter_score/.

    Args:
        run_dir: Run directory path.
        scored: Scored idea dict.

    Returns:
        Path to the written JSON file.
    """
    filter_dir = run_dir / "filter_score"
    filter_dir.mkdir(parents=True, exist_ok=True)

    idea_id = scored.get("idea_id", "unknown")
    file_path = filter_dir / f"{idea_id}.json"
    with open(file_path, "w") as f:
        json.dump(scored, f, indent=2, default=str)
    return file_path


def read_scored_ideas(run_dir: Path) -> list[dict]:
    """Read all scored idea JSON files from filter_score/.

    Args:
        run_dir: Run directory path.

    Returns:
        List of scored idea dicts, sorted by idea_id.
    """
    filter_dir = run_dir / "filter_score"
    if not filter_dir.exists():
        return []

    results = []
    for json_file in sorted(filter_dir.glob("*.json")):
        with open(json_file) as f:
            results.append(json.load(f))
    return results


def main() -> None:
    import sys

    if len(sys.argv) < 3:
        print(
            "Usage: python -m safety_ideas.pipeline.filter_score <command> <run_dir> [json_data]"
        )
        sys.exit(1)

    cmd = sys.argv[1]
    run_dir = Path(sys.argv[2])

    if cmd == "write":
        scored_data = json.loads(sys.argv[3])
        path = write_scored_idea(run_dir, scored_data)
        print(path)
    elif cmd == "read":
        ideas = read_scored_ideas(run_dir)
        print(json.dumps(ideas, indent=2, default=str))
    elif cmd == "list":
        filter_dir = run_dir / "filter_score"
        if filter_dir.exists():
            for f in sorted(filter_dir.glob("*.json")):
                print(f)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
