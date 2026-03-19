"""Tests for safety_ideas.pipeline.memory."""

import json
import subprocess
import sys
from pathlib import Path

from safety_ideas.pipeline.memory import load_previous_ideas


def _write_idea(directory: Path, filename: str, content: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / filename).write_text(content, encoding="utf-8")


def test_extracts_titles_from_markdown_files(tmp_path: Path) -> None:
    _write_idea(tmp_path, "idea1.md", "---\nstatus: draft\n---\n# First Idea\nBody text.")
    _write_idea(tmp_path, "idea2.md", "---\nstatus: draft\n---\n# Second Idea\nMore text.")

    titles = load_previous_ideas(tmp_path)

    assert sorted(titles) == ["First Idea", "Second Idea"]


def test_returns_empty_list_when_directory_missing(tmp_path: Path) -> None:
    nonexistent = tmp_path / "no_such_dir"
    assert load_previous_ideas(nonexistent) == []


def test_returns_empty_list_when_no_md_files(tmp_path: Path) -> None:
    (tmp_path / "notes.txt").write_text("not markdown")
    assert load_previous_ideas(tmp_path) == []


def test_skips_files_without_h1_heading(tmp_path: Path) -> None:
    _write_idea(tmp_path, "no_title.md", "Just some text\nwithout a heading.")
    _write_idea(tmp_path, "has_title.md", "# Real Title\nBody.")

    titles = load_previous_ideas(tmp_path)

    assert titles == ["Real Title"]


def test_cli_entry_point(tmp_path: Path) -> None:
    (tmp_path / "idea.md").write_text("# CLI Test Idea\nBody.", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-m", "safety_ideas.pipeline.memory", str(tmp_path)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    titles = json.loads(result.stdout)
    assert titles == ["CLI Test Idea"]
