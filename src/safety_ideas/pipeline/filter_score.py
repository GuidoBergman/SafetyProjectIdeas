"""Filter/score stage: scoring computation, staged filtering, and scored idea I/O."""

import json
from datetime import UTC, datetime
from pathlib import Path

from safety_ideas.config.schemas import (
    QuickFilterConfig,
    ScoringCriteria,
    StageThreshold,
    TeamProfile,
)


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
        "scores": {c.name: {"score": 0, "reasoning": "", "confidence": 0.0} for c in criteria},
        "novelty_assessment": {
            "classification": "",
            "evidence": [],
            "confidence": 0.0,
            "derived_score": 0,
        },
        "novelty_method": None,
        "citation_verification": {
            "relevance_scores": [],
            "verified": [],
            "corrected": [],
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
    quick_filter: QuickFilterConfig | None = None,
) -> list[dict]:
    """Apply staged filtering to a list of scored idea dicts.

    Stage 1: Quick relevance — eliminate ideas with weighted_score below
             the quick_filter threshold (default 2.0).
    Stage 2: Full scoring — eliminate ideas below thresholds.min_score.
    Stage 3: Novelty hard gate — eliminate ideas classified as "already_solved".

    Each stage updates the ``filter_stage_passed``, ``eliminated``, and
    ``elimination_reason`` fields on the scored idea dicts **in place**.

    Args:
        ideas: List of scored idea dicts (must already have scores populated).
        criteria: Scoring criteria list.
        thresholds: Stage threshold settings from pipeline config.
        team_profile: Team profile for weight computation.
        quick_filter: Quick filter config with threshold and rubric.
            If None, uses default QuickFilterConfig (threshold=2.0).

    Returns:
        List of surviving (non-eliminated) scored idea dicts.
    """
    if quick_filter is None:
        quick_filter = QuickFilterConfig()

    relevance_threshold = quick_filter.threshold
    survivors = []

    for idea in ideas:
        # Stage 1: Quick relevance check
        weighted = apply_weights(idea.get("scores", {}), criteria, team_profile)
        idea["weighted_score"] = weighted

        if weighted < relevance_threshold:
            idea["eliminated"] = True
            idea["elimination_reason"] = (
                f"Stage 1: weighted score {weighted:.2f} < {relevance_threshold}"
            )
            idea["filter_stage_passed"] = 0
            continue

        idea["filter_stage_passed"] = 1

        # Stage 2: Full scoring threshold
        min_score = thresholds.min_score
        if weighted < min_score:
            idea["eliminated"] = True
            idea["elimination_reason"] = f"Stage 2: weighted score {weighted:.2f} < {min_score}"
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
            dropped["elimination_reason"] = f"Exceeded max_ideas limit ({thresholds.max_ideas})"
        survivors = survivors[: thresholds.max_ideas]

    return survivors


def write_scored_idea(run_dir: Path, scored: dict) -> Path:
    """Write a scored idea as a JSON file in filter_score/scored/.

    Args:
        run_dir: Run directory path.
        scored: Scored idea dict.

    Returns:
        Path to the written JSON file.
    """
    scored_dir = run_dir / "filter_score" / "scored"
    scored_dir.mkdir(parents=True, exist_ok=True)

    idea_id = scored.get("idea_id", "unknown")
    file_path = scored_dir / f"{idea_id}.json"
    with open(file_path, "w") as f:
        json.dump(scored, f, indent=2, default=str)
    return file_path


def read_scored_ideas(run_dir: Path) -> list[dict]:
    """Read all scored idea JSON files from filter_score/scored/.

    Args:
        run_dir: Run directory path.

    Returns:
        List of scored idea dicts, sorted by idea_id.
    """
    scored_dir = run_dir / "filter_score" / "scored"
    if not scored_dir.exists():
        return []

    results = []
    for json_file in sorted(scored_dir.glob("*.json")):
        with open(json_file) as f:
            results.append(json.load(f))
    return results


def _batch_dir(run_dir: Path, stage: int) -> Path:
    """Return the batch directory for a given stage."""
    return run_dir / "filter_score" / "batches" / f"stage{stage}"


def _results_dir(run_dir: Path, stage: int) -> Path:
    """Return the results directory for a given stage."""
    return run_dir / "filter_score" / "results" / f"stage{stage}"


def _survivors_dir(run_dir: Path) -> Path:
    """Return the survivors directory."""
    return run_dir / "filter_score" / "survivors"


def create_batches(run_dir: Path, stage: int, batch_size: int) -> list[Path]:
    """Partition ideas into batch files for a given scoring stage.

    Stage 1 reads ideas from the generate directory.
    Stages 2+ read survivors from the previous stage.

    Args:
        run_dir: Run directory path.
        stage: Stage number (1, 2, or 3).
        batch_size: Number of ideas per batch.

    Returns:
        List of paths to the written batch files.
    """
    from safety_ideas.pipeline.generate import read_idea_sketches

    if stage == 1:
        ideas = read_idea_sketches(run_dir)
    else:
        survivors_file = _survivors_dir(run_dir) / f"stage{stage - 1}_survivors.json"
        with open(survivors_file) as f:
            ideas = json.load(f)

    batch_out = _batch_dir(run_dir, stage)
    batch_out.mkdir(parents=True, exist_ok=True)

    batch_paths = []
    for i in range(0, len(ideas), batch_size):
        chunk = ideas[i : i + batch_size]
        batch_num = (i // batch_size) + 1
        path = batch_out / f"batch_{batch_num:03d}.json"
        with open(path, "w") as f:
            json.dump(chunk, f, indent=2, default=str)
        batch_paths.append(path)

    return batch_paths


def read_batch(batch_path: Path) -> list[dict]:
    """Read a single batch file.

    Args:
        batch_path: Path to the batch JSON file.

    Returns:
        List of idea dicts in the batch.
    """
    with open(batch_path) as f:
        return json.load(f)


def write_batch_results(result_path: Path, results: list[dict]) -> Path:
    """Write subagent results for a batch.

    Args:
        result_path: Path to write the results JSON file.
        results: List of result dicts from the subagent.

    Returns:
        Path to the written file.
    """
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    return result_path


def merge_stage_results(run_dir: Path, stage: int) -> list[dict]:
    """Read and merge all batch result files for a stage.

    Args:
        run_dir: Run directory path.
        stage: Stage number (1, 2, or 3).

    Returns:
        Merged list of all result dicts, sorted by idea_id.
    """
    results_path = _results_dir(run_dir, stage)
    if not results_path.exists():
        return []

    merged = []
    for json_file in sorted(results_path.glob("batch_*_results.json")):
        with open(json_file) as f:
            merged.extend(json.load(f))

    merged.sort(key=lambda x: x.get("idea_id", ""))
    return merged


def filter_survivors(run_dir: Path, stage: int) -> list[dict]:
    """Filter merged stage results to keep only non-eliminated ideas.

    Writes survivors to a JSON file for the next stage's create_batches.

    Args:
        run_dir: Run directory path.
        stage: Stage number (1, 2, or 3).

    Returns:
        List of surviving idea dicts.
    """
    merged = merge_stage_results(run_dir, stage)
    survivors = [r for r in merged if not r.get("eliminated", False)]

    survivors_path = _survivors_dir(run_dir)
    survivors_path.mkdir(parents=True, exist_ok=True)
    out_file = survivors_path / f"stage{stage}_survivors.json"
    with open(out_file, "w") as f:
        json.dump(survivors, f, indent=2, default=str)

    return survivors


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.pipeline.filter_score <command> <run_dir> [args]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "write":
        run_dir = Path(sys.argv[2])
        scored_data = json.loads(sys.argv[3])
        path = write_scored_idea(run_dir, scored_data)
        print(path)
    elif cmd == "read":
        run_dir = Path(sys.argv[2])
        ideas = read_scored_ideas(run_dir)
        print(json.dumps(ideas, indent=2, default=str))
    elif cmd == "list":
        run_dir = Path(sys.argv[2])
        filter_dir = run_dir / "filter_score"
        if filter_dir.exists():
            for f in sorted(filter_dir.glob("*.json")):
                print(f)
    elif cmd == "create-batches":
        run_dir = Path(sys.argv[2])
        stage = int(sys.argv[3])
        batch_size = int(sys.argv[4])
        paths = create_batches(run_dir, stage, batch_size)
        result = {"batch_count": len(paths), "batch_paths": [str(p) for p in paths]}
        print(json.dumps(result, indent=2))
    elif cmd == "read-batch":
        batch_path = Path(sys.argv[2])
        ideas = read_batch(batch_path)
        print(json.dumps(ideas, indent=2, default=str))
    elif cmd == "write-batch-results":
        result_path = Path(sys.argv[2])
        results = json.loads(sys.argv[3])
        write_batch_results(result_path, results)
        print(result_path)
    elif cmd == "merge-results":
        run_dir = Path(sys.argv[2])
        stage = int(sys.argv[3])
        merged = merge_stage_results(run_dir, stage)
        result = {"total": len(merged), "results": merged}
        print(json.dumps(result, indent=2, default=str))
    elif cmd == "filter-survivors":
        run_dir = Path(sys.argv[2])
        stage = int(sys.argv[3])
        survivors = filter_survivors(run_dir, stage)
        eliminated_count = len(merge_stage_results(run_dir, stage)) - len(survivors)
        result = {"survivors": len(survivors), "eliminated": eliminated_count}
        print(json.dumps(result, indent=2))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
