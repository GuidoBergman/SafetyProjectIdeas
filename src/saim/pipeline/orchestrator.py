"""Pipeline orchestrator: run directory creation, metadata, and logging."""

from __future__ import annotations

import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from saim.constants import RUNS_DIR, STAGE_NAMES


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


def log_entry(run_dir_str: str, stage: str, level: str, message: str, data_json: str | None = None) -> None:
    """Append a structured log entry to a run's pipeline log."""
    data = json.loads(data_json) if data_json else None
    logger = PipelineLogger(Path(run_dir_str))
    # Load existing entries so we append rather than overwrite
    if logger._log_path.exists():
        with open(logger._log_path) as f:
            logger._entries = json.load(f)
    logger.log(stage, level, message, data)


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m saim.pipeline.orchestrator <command>")
        print("Commands: init [stages...], log <run_dir> <stage> <level> <message> [data_json]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "init":
        stages = sys.argv[2:] if len(sys.argv) > 2 else None
        run_dir = create_run_dir(stages)
        print(run_dir)
    elif cmd == "log":
        if len(sys.argv) < 6:
            print("Usage: ... log <run_dir> <stage> <level> <message> [data_json]", file=sys.stderr)
            sys.exit(1)
        data_json = sys.argv[6] if len(sys.argv) > 6 else None
        log_entry(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], data_json)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
