"""Tests for the generate pipeline stage."""

import yaml

from saim.pipeline.generate import (
    list_idea_files,
    read_idea_sketches,
    write_idea_sketch,
)


def _make_idea(idea_id="gen-001"):
    return {
        "idea_id": idea_id,
        "run_id": "2026-03-19T14-30-00",
        "subfield": "mechanistic_interpretability",
        "generation_strategy": "novel_direction",
        "confidence": 0.7,
        "title": "Test Idea",
        "problem": "A test problem",
        "direction": "A test direction",
        "why_it_matters": "A test impact theory",
        "relevant_context": "Some references",
    }


def test_write_idea_sketch_creates_file(tmp_path):
    idea = _make_idea()
    path = write_idea_sketch(tmp_path, idea)

    assert path.exists()
    assert path.parent.name == "generate"
    assert path.name == "gen-001.md"


def test_write_idea_sketch_frontmatter(tmp_path):
    idea = _make_idea()
    path = write_idea_sketch(tmp_path, idea)
    text = path.read_text()

    parts = text.split("---", 2)
    assert len(parts) >= 3
    fm = yaml.safe_load(parts[1])

    assert fm["idea_id"] == "gen-001"
    assert fm["run_id"] == "2026-03-19T14-30-00"
    assert fm["stage"] == "generate"
    assert fm["subfield"] == "mechanistic_interpretability"
    assert fm["generation_strategy"] == "novel_direction"
    assert fm["confidence"] == 0.7
    assert "timestamp" in fm


def test_write_idea_sketch_body(tmp_path):
    idea = _make_idea()
    path = write_idea_sketch(tmp_path, idea)
    text = path.read_text()

    parts = text.split("---", 2)
    body = parts[2].strip()

    assert body.startswith("# Test Idea")
    assert "**Problem:** A test problem" in body
    assert "**Direction:** A test direction" in body
    assert "**Why it matters:** A test impact theory" in body
    assert "**Relevant context:** Some references" in body


def test_read_idea_sketches_roundtrip(tmp_path):
    idea = _make_idea()
    write_idea_sketch(tmp_path, idea)

    results = read_idea_sketches(tmp_path)
    assert len(results) == 1

    r = results[0]
    assert r["idea_id"] == "gen-001"
    assert r["stage"] == "generate"
    assert r["subfield"] == "mechanistic_interpretability"
    assert "# Test Idea" in r["body"]
    assert "**Problem:** A test problem" in r["body"]


def test_read_idea_sketches_multiple(tmp_path):
    write_idea_sketch(tmp_path, _make_idea("gen-001"))
    write_idea_sketch(tmp_path, _make_idea("gen-002"))

    results = read_idea_sketches(tmp_path)
    assert len(results) == 2
    ids = [r["idea_id"] for r in results]
    assert ids == ["gen-001", "gen-002"]


def test_list_idea_files_sorted(tmp_path):
    write_idea_sketch(tmp_path, _make_idea("gen-003"))
    write_idea_sketch(tmp_path, _make_idea("gen-001"))
    write_idea_sketch(tmp_path, _make_idea("gen-002"))

    files = list_idea_files(tmp_path)
    assert len(files) == 3
    assert [f.name for f in files] == ["gen-001.md", "gen-002.md", "gen-003.md"]


def test_list_idea_files_empty(tmp_path):
    assert list_idea_files(tmp_path) == []


def test_read_idea_sketches_empty(tmp_path):
    assert read_idea_sketches(tmp_path) == []


def test_write_idea_sketch_validates_required_keys(tmp_path):
    import pytest

    incomplete = {"idea_id": "gen-001", "run_id": "test"}
    with pytest.raises(ValueError, match="missing required keys"):
        write_idea_sketch(tmp_path, incomplete)
