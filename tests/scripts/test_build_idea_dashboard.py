"""Tests for the SAIM idea dashboard builder."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

_script_path = Path(__file__).resolve().parent.parent.parent / "scripts" / "build_idea_dashboard.py"
_spec = importlib.util.spec_from_file_location("build_idea_dashboard", _script_path)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["build_idea_dashboard"] = _mod
_spec.loader.exec_module(_mod)


def proposal(idea_id: str = "gen-aaaa1111", rank: int = 1) -> dict:
    return {
        "idea_id": idea_id,
        "run_id": "2026-08-27T23-17-39",
        "rank": rank,
        "title": "A Title",
        "weighted_score": 4.5678,
        "subfield": "AI Control / Monitoring",
        "generation_strategy": "extend_recent_paper",
        "novelty_classification": "mostly_novel",
        "novelty_score": 4,
        "novelty_method": "novelty_assessed",
        "confidence": 0.8,
        "original_scores": {"theory_of_impact": 5, "low_compute": 4},
        "scores": {"novelty": {"score": 4, "reasoning": "ASSESSED: not covered."}},
        "sections": {
            "research_question": "Does X hold?",
            "approach_outline": "Do Y.",
            "proposed_first_experiments": "Run Z.",
            "theory_of_impact_chain": "Because W.",
            "strength_rationale": "Cheap.",
            "alternative_framings": ["Framing A"],
            "cited_sources": ["Paper A"],
        },
    }


def write_run(tmp_path: Path, items: list[dict], name: str = "run") -> Path:
    run_dir = tmp_path / name
    (run_dir / "rank").mkdir(parents=True)
    (run_dir / "rank" / "ranked_proposals.json").write_text(json.dumps(items), encoding="utf-8")
    return run_dir


def test_resolve_rank_json_accepts_run_dir(tmp_path):
    run_dir = write_run(tmp_path, [proposal()])
    assert _mod.resolve_rank_json(str(run_dir)) == run_dir / "rank" / "ranked_proposals.json"


def test_resolve_rank_json_accepts_direct_file(tmp_path):
    run_dir = write_run(tmp_path, [proposal()])
    direct = run_dir / "rank" / "ranked_proposals.json"
    assert _mod.resolve_rank_json(str(direct)) == direct


def test_resolve_rank_json_raises_when_missing(tmp_path):
    with pytest.raises(FileNotFoundError):
        _mod.resolve_rank_json(str(tmp_path / "nope"))


def test_parse_run_spec_without_label():
    assert _mod.parse_run_spec("data/runs/2026-08-27") == ("data/runs/2026-08-27", "2026-08-27")


def test_parse_run_spec_with_label():
    assert _mod.parse_run_spec("data/runs/r1:Light run") == ("data/runs/r1", "Light run")


def test_parse_run_spec_with_empty_label():
    assert _mod.parse_run_spec("data/runs/r1:") == ("data/runs/r1", "r1")


@pytest.mark.parametrize(
    ("method", "expected"),
    [
        ("novelty_assessed", "calculated"),
        ("novelty_estimated", "estimated"),
        ("something_else", "something_else"),
        ("", "unknown"),
    ],
)
def test_novelty_kind(method, expected):
    assert _mod.novelty_kind(method) == expected


def test_to_record_flattens_sections_and_scores():
    record = _mod.to_record(proposal(), "Light run", "B1", "gen-aaaa1111", "")
    assert record["id"] == "gen-aaaa1111"
    assert record["score"] == 4.568
    assert record["rq"] == "Does X hold?"
    assert record["novelty_kind"] == "calculated"
    assert record["novelty_reasoning"] == "ASSESSED: not covered."
    assert record["scores"] == {"theory_of_impact": 5, "low_compute": 4}
    assert record["batch"] == "Light run"


def test_to_record_tolerates_missing_fields():
    record = _mod.to_record({"idea_id": "gen-x"}, "Run", "B1", "gen-x", "")
    assert record["score"] == 0
    assert record["rq"] == ""
    assert record["framings"] == []
    assert record["novelty_kind"] == "unknown"


def test_build_records_resolves_id_collisions_across_batches():
    batches = [
        {"label": "Run one", "short": "B1", "items": [proposal("gen-dup")]},
        {"label": "Run two", "short": "B2", "items": [proposal("gen-dup"), proposal("gen-dup")]},
    ]
    records = _mod.build_records(batches)
    assert [r["id"] for r in records] == ["gen-dup", "gen-dup-B2", "gen-dup-B2-2"]
    assert records[0]["orig_id"] == ""
    assert records[1]["orig_id"] == "gen-dup"


def test_load_batch_reads_items(tmp_path):
    run_dir = write_run(tmp_path, [proposal()])
    batch = _mod.load_batch(str(run_dir), "Light run", "B1")
    assert batch["label"] == "Light run"
    assert len(batch["items"]) == 1


TRACKER = """
| Position | ID | Title | Areas | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| #1 | [gen-0017](../ideas/gen-0017.md) | T | A | 🟢 Added | |
| #2 | [gen-1655](../ideas/gen-1655.md) | T | A | 🔵 Evaluating | |
| #3 | [gen-0127](../ideas/gen-0127.md) | T | A | 🔴 Removed | |
| #4 | [gen-9999](../ideas/gen-9999.md) | T | A | 🟣 Nonsense status | |
| #5 | no id here | T | A | 🟢 Added | |
not a table row
"""


def test_parse_tracker_statuses_keeps_known_statuses_only():
    assert _mod.parse_tracker_statuses(TRACKER) == {
        "gen-0017": "Added",
        "gen-1655": "Evaluating",
        "gen-0127": "Removed",
    }


def test_parse_tracker_statuses_ignores_empty_text():
    assert _mod.parse_tracker_statuses("") == {}


def test_seed_statuses_only_seeds_non_default_matches():
    records = [
        _mod.to_record(proposal("gen-0017"), "R", "B1", "gen-0017", ""),
        _mod.to_record(proposal("gen-0127"), "R", "B2", "gen-0127-B2", "gen-0127"),
        _mod.to_record(proposal("gen-none"), "R", "B1", "gen-none", ""),
    ]
    tracker = {"gen-0017": "Added", "gen-0127": "Removed", "gen-other": "Added"}
    seeded = _mod.seed_statuses(records, tracker)
    assert set(seeded) == {"gen-0017", "gen-0127-B2"}
    assert seeded["gen-0017"]["status"] == "Added"
    assert seeded["gen-0127-B2"]["status"] == "Removed"
    assert seeded["gen-0017"]["by"] == "idea_tracker.md"


def test_seed_statuses_skips_default_status():
    records = [_mod.to_record(proposal("gen-1"), "R", "B1", "gen-1", "")]
    assert _mod.seed_statuses(records, {"gen-1": "Not reviewed"}) == {}


def test_escape_text_escapes_markup():
    assert _mod.escape_text('a <b> & "c"') == 'a &lt;b&gt; &amp; "c"'


def test_json_for_script_escapes_closing_tags():
    payload = _mod.json_for_script({"t": "</script><script>x</script>"})
    assert "</script>" not in payload
    assert json.loads(payload)["t"] == "</script><script>x</script>"


def test_render_html_is_a_fragment_with_embedded_payloads():
    records = [_mod.to_record(proposal(), "Light run", "B1", "gen-aaaa1111", "")]
    html = _mod.render_html(records, {"gen-aaaa1111": {"status": "Added"}}, "My Board", "3 ideas")
    assert "<!DOCTYPE" not in html.upper().split("<SCRIPT")[0]
    assert "<title>My Board</title>" in html
    assert "3 ideas" in html
    assert '"gen-aaaa1111"' in html
    assert "Added" in html
    assert json.dumps(_mod.STATUSES) in html


def test_render_html_escapes_the_title():
    html = _mod.render_html([], {}, "<script>bad()</script>", "sub")
    assert "<script>bad()</script>" not in html
    assert "&lt;script&gt;bad()&lt;/script&gt;" in html


def test_main_demo_writes_a_page(tmp_path):
    out = tmp_path / "demo.html"
    _mod.main(["--demo", "--out", str(out)])
    assert out.exists()
    assert "Do Refusal Directions Transfer" in out.read_text(encoding="utf-8")


def test_main_defaults_output_into_the_run_dir(tmp_path):
    run_dir = write_run(tmp_path, [proposal()])
    out = _mod.main([str(run_dir)])
    assert out == run_dir / "dashboard.html"
    assert out.exists()


def test_main_seeds_status_from_tracker(tmp_path):
    run_dir = write_run(tmp_path, [proposal("gen-0017")])
    tracker = tmp_path / "idea_tracker.md"
    tracker.write_text(TRACKER, encoding="utf-8")
    out = tmp_path / "seeded.html"
    _mod.main([str(run_dir), "--out", str(out), "--seed-status", str(tracker)])
    html = out.read_text(encoding="utf-8")
    status_block = html.split('id="saim-status">')[1].split("</script>")[0]
    assert json.loads(status_block)["gen-0017"]["status"] == "Added"


def test_main_requires_a_run_or_demo(tmp_path):
    with pytest.raises(SystemExit):
        _mod.main([])


def test_standalone_document_wraps_the_fragment():
    doc = _mod.standalone_document("<div>hi</div>", "Board")
    assert doc.startswith("<!doctype html>")
    assert "<title>Board</title>" in doc
    assert "<div>hi</div>" in doc
    assert doc.rstrip().endswith("</html>")


def test_main_standalone_writes_a_full_document(tmp_path):
    out = tmp_path / "local.html"
    _mod.main(["--demo", "--standalone", "--out", str(out)])
    text = out.read_text(encoding="utf-8")
    assert text.startswith("<!doctype html>")
    assert "Do Refusal Directions Transfer" in text


def test_promising_is_in_the_vocabulary_before_evaluating():
    assert "Promising" in _mod.STATUSES
    assert _mod.STATUSES.index("Promising") < _mod.STATUSES.index("Evaluating")
    assert _mod.STATUSES[0] == "Not reviewed"


def test_statuses_from_dashboard_reads_back_what_render_wrote():
    records = [_mod.to_record(proposal(), "R", "B1", "gen-aaaa1111", "")]
    statuses = {
        "gen-aaaa1111": {
            "status": "Promising",
            "note": "worth a look",
            "by": "g",
            "at": "2026-08-28",
        }
    }
    html = _mod.render_html(records, statuses, "Board", "sub")
    assert _mod.statuses_from_dashboard(html) == statuses


def test_statuses_from_dashboard_drops_unknown_statuses():
    html = _mod.render_html([], {"gen-x": {"status": "Invented"}}, "Board", "sub")
    assert _mod.statuses_from_dashboard(html) == {}


def test_statuses_from_dashboard_without_a_status_block():
    assert _mod.statuses_from_dashboard("<div>no dashboard here</div>") == {}


def test_main_carries_statuses_from_a_previous_build(tmp_path):
    run_dir = write_run(tmp_path, [proposal("gen-0017")])
    first = tmp_path / "first.html"
    _mod.main([str(run_dir), "--out", str(first)])
    marked = _mod.render_html(
        [_mod.to_record(proposal("gen-0017"), "R", "B1", "gen-0017", "")],
        {"gen-0017": {"status": "Promising", "note": "", "by": "g", "at": "2026-08-28"}},
        "Board",
        "sub",
    )
    first.write_text(marked, encoding="utf-8")
    second = tmp_path / "second.html"
    _mod.main([str(run_dir), "--out", str(second), "--carry-status", str(first)])
    carried = _mod.statuses_from_dashboard(second.read_text(encoding="utf-8"))
    assert carried["gen-0017"]["status"] == "Promising"


def test_main_ignores_carried_statuses_for_ideas_not_in_this_run(tmp_path):
    run_dir = write_run(tmp_path, [proposal("gen-0017")])
    stale = tmp_path / "stale.html"
    stale.write_text(
        _mod.render_html([], {"gen-9999": {"status": "Added"}}, "Board", "sub"), encoding="utf-8"
    )
    out = tmp_path / "out.html"
    _mod.main([str(run_dir), "--out", str(out), "--carry-status", str(stale)])
    assert _mod.statuses_from_dashboard(out.read_text(encoding="utf-8")) == {}
