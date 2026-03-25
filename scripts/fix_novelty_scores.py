"""Fix novelty score inconsistencies in scored idea files and survivors.

Reads all scored idea JSON files from a run's filter_score/scored/ directory,
normalizes novelty data using normalize_novelty_scores(), recalculates weighted
scores, and rewrites all files including survivors.

Usage:
    uv run python scripts/fix_novelty_scores.py <run_dir>
    uv run python scripts/fix_novelty_scores.py data/runs/2026-03-19T19-58-40
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from safety_ideas.pipeline.novelty import normalize_novelty_scores


def fix_run(run_dir: Path) -> dict:
    """Normalize novelty scores for all scored ideas in a run directory.

    Returns a summary dict with counts per novelty_method.
    """
    scored_dir = run_dir / "filter_score" / "scored"
    if not scored_dir.exists():
        print(f"No scored directory found at {scored_dir}", file=sys.stderr)
        sys.exit(1)

    files = sorted(scored_dir.glob("gen-*.json"))
    if not files:
        print(f"No scored idea files found in {scored_dir}", file=sys.stderr)
        sys.exit(1)

    method_counts: Counter[str] = Counter()
    ideas_by_id: dict[str, dict] = {}

    for path in files:
        with open(path) as f:
            idea = json.load(f)

        normalize_novelty_scores(idea)
        method_counts[idea.get("novelty_method", "unknown")] += 1
        ideas_by_id[idea.get("idea_id", path.stem)] = idea

        with open(path, "w") as f:
            json.dump(idea, f, indent=2, default=str)

    # Update survivors files
    survivors_dir = run_dir / "filter_score" / "survivors"
    if survivors_dir.exists():
        for survivor_file in sorted(survivors_dir.glob("stage*_survivors.json")):
            with open(survivor_file) as f:
                survivors = json.load(f)

            updated = []
            for survivor in survivors:
                idea_id = survivor.get("idea_id", "")
                if idea_id in ideas_by_id:
                    updated.append(ideas_by_id[idea_id])
                else:
                    normalize_novelty_scores(survivor)
                    updated.append(survivor)

            with open(survivor_file, "w") as f:
                json.dump(updated, f, indent=2, default=str)

            print(f"  Updated {survivor_file.name}: {len(updated)} ideas")

    return dict(method_counts)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: uv run python scripts/fix_novelty_scores.py <run_dir>")
        sys.exit(1)

    run_dir = Path(sys.argv[1])
    if not run_dir.exists():
        print(f"Run directory not found: {run_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Fixing novelty scores in {run_dir}...")
    summary = fix_run(run_dir)

    print("\nSummary:")
    for method, count in sorted(summary.items()):
        print(f"  {method}: {count}")
    print(f"  total: {sum(summary.values())}")


if __name__ == "__main__":
    main()
