"""Pipeline orchestrator: run directory creation, metadata, and logging."""

from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from safety_ideas.constants import RUNS_DIR, STAGE_NAMES


def create_run_dir(stages: list[str] | None = None) -> Path:
    """Create a timestamped run directory with stage subdirectories."""
    if stages is None:
        stages = list(STAGE_NAMES)
    timestamp = datetime.now(UTC).strftime("%Y-%m-%dT%H-%M-%S")
    run_dir = RUNS_DIR / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)
    for stage in stages:
        (run_dir / stage).mkdir(exist_ok=True)
    return run_dir


def write_run_meta(run_dir: Path, params: dict) -> None:
    """Write run_meta.json with run info and parameters."""
    try:
        git_commit = (
            subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"],
                stderr=subprocess.DEVNULL,
            )
            .decode()
            .strip()
        )
    except Exception:
        git_commit = "unknown"

    meta = {
        "run_id": run_dir.name,
        "timestamp": datetime.now(UTC).isoformat(),
        "git_commit": git_commit,
        "parameters": params,
    }
    with open(run_dir / "run_meta.json", "w") as f:
        json.dump(meta, f, indent=2)


class PipelineLogger:
    """Structured JSON logger that writes to a run directory."""

    def __init__(self, run_dir: Path) -> None:
        self._log_path = run_dir / "pipeline.log.json"
        self._entries: list[dict] = []

    def log(
        self, stage: str, level: str, message: str, data: dict | None = None
    ) -> None:
        entry = {
            "timestamp": datetime.now(UTC).isoformat(),
            "run_id": self._log_path.parent.name,
            "stage": stage,
            "level": level,
            "message": message,
            "data": data,
        }
        self._entries.append(entry)
        with open(self._log_path, "w") as f:
            json.dump(self._entries, f, indent=2)

    @property
    def entries(self) -> list[dict]:
        return self._entries


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.pipeline.orchestrator <command>")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "init":
        stages = sys.argv[2:] if len(sys.argv) > 2 else None
        run_dir = create_run_dir(stages)
        print(run_dir)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
