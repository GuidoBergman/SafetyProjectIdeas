"""Tests for pipeline orchestrator."""

from __future__ import annotations

import json
import subprocess
import sys

from safety_ideas.pipeline.orchestrator import (
    PipelineLogger,
    create_run_dir,
    write_run_meta,
)


def test_create_run_dir_all_stages(tmp_path, monkeypatch):
    monkeypatch.setattr("safety_ideas.pipeline.orchestrator.RUNS_DIR", tmp_path)
    run_dir = create_run_dir()
    assert run_dir.exists()
    assert run_dir.parent == tmp_path
    for stage in ["source", "generate", "filter_score", "refine", "rank"]:
        assert (run_dir / stage).is_dir()


def test_create_run_dir_custom_stages(tmp_path, monkeypatch):
    monkeypatch.setattr("safety_ideas.pipeline.orchestrator.RUNS_DIR", tmp_path)
    run_dir = create_run_dir(["generate"])
    assert (run_dir / "generate").is_dir()
    assert not (run_dir / "source").exists()


def test_write_run_meta(tmp_path):
    run_dir = tmp_path / "2026-01-01T00-00-00"
    run_dir.mkdir()
    params = {"model": "test", "temperature": 0.7}
    write_run_meta(run_dir, params)
    meta_path = run_dir / "run_meta.json"
    assert meta_path.exists()
    meta = json.loads(meta_path.read_text())
    assert meta["run_id"] == "2026-01-01T00-00-00"
    assert "timestamp" in meta
    assert "git_commit" in meta
    assert meta["parameters"] == params


def test_pipeline_logger(tmp_path):
    run_dir = tmp_path / "2026-01-01T00-00-00"
    run_dir.mkdir()
    logger = PipelineLogger(run_dir)
    logger.log("source", "INFO", "Starting source stage", {"count": 5})
    logger.log("source", "DEBUG", "Done")

    assert len(logger.entries) == 2
    assert logger.entries[0]["stage"] == "source"
    assert logger.entries[0]["level"] == "INFO"
    assert logger.entries[0]["message"] == "Starting source stage"
    assert logger.entries[0]["data"] == {"count": 5}
    assert logger.entries[1]["data"] is None

    log_path = run_dir / "pipeline.log.json"
    assert log_path.exists()
    written = json.loads(log_path.read_text())
    assert len(written) == 2


def test_cli_init(tmp_path):
    """Test CLI init command creates run directory with requested stages."""
    from pathlib import Path

    result = subprocess.run(
        [sys.executable, "-m", "safety_ideas.pipeline.orchestrator", "init", "generate"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    run_dir = Path(result.stdout.strip())
    assert run_dir.exists()
    assert (run_dir / "generate").is_dir()
    # Cleanup
    import shutil
    shutil.rmtree(run_dir)
