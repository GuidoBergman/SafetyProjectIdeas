"""Tests for the fix_truncated_ideas repair script."""

import importlib.util
import json
import sys
from pathlib import Path

from safety_ideas.pipeline.generate import write_idea_sketch
from safety_ideas.pipeline.refine import write_refined_proposal

_script_path = Path(__file__).resolve().parent.parent.parent / "scripts" / "fix_truncated_ideas.py"
_spec = importlib.util.spec_from_file_location("fix_truncated_ideas", _script_path)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["fix_truncated_ideas"] = _mod
_spec.loader.exec_module(_mod)

_parse_generate_body = _mod._parse_generate_body
_build_strength_rationale = _mod._build_strength_rationale
_update_sections_in_dict = _mod._update_sections_in_dict
_fix_ranked_proposals = _mod._fix_ranked_proposals
fix_idea = _mod.fix_idea


def _write_generate_idea(tmp_path, idea_id="gen-001"):
    """Write a generate-stage idea with full content."""
    idea = {
        "idea_id": idea_id,
        "run_id": "test-run",
        "subfield": "interpretability",
        "generation_strategy": "novel_direction",
        "confidence": 0.8,
        "title": "Test Idea Title",
        "problem": "If harmful prompts are in safety training data, models memorize refusals.",
        "direction": "Take 100 harmful prompts and generate paraphrases. Compare ASR.",
        "why_it_matters": "Contamination means evaluations overestimate robustness.",
        "relevant_context": "StrongREJECT benchmark. JailbreakBench NeurIPS 2024.",
    }
    write_idea_sketch(tmp_path, idea)
    return idea


def _write_scored_idea(tmp_path, idea_id="gen-001"):
    """Write a scored idea JSON with complete reasoning."""
    scored = {
        "idea_id": idea_id,
        "title": "Test Idea Title",
        "scores": {
            "theory_of_impact": {
                "score": 5,
                "reasoning": "Compelling chain: contamination inflates safety scores.",
                "confidence": 0.85,
            },
            "accessible_complexity": {
                "score": 5,
                "reasoning": "Paraphrase prompts, run against models, compare ASR. No training.",
                "confidence": 0.85,
            },
        },
        "novelty_assessment": {
            "classification": "partially_addressed",
            "evidence": ["Paper A - studies contamination", "Paper B - benchmark risks"],
            "reasoning": "Known problem, novel methodology.",
            "confidence": 0.6,
        },
        "citation_verification": {
            "citations": [
                {"title": "JailbreakBench", "status": "verified", "notes": "Core benchmark."},
            ],
        },
    }
    scored_dir = tmp_path / "filter_score" / "scored"
    scored_dir.mkdir(parents=True, exist_ok=True)
    path = scored_dir / f"{idea_id}.json"
    with open(path, "w") as f:
        json.dump(scored, f)
    return scored


def _write_truncated_refine(tmp_path, idea_id="gen-001"):
    """Write a refine proposal with truncated content (simulating the bug)."""
    proposal = {
        "idea_id": idea_id,
        "run_id": "test-run",
        "stage": "refine",
        "title": "Test Idea Title",
        "timestamp": "2026-03-25T17:07:42Z",
        "original_scores": {"theory_of_impact": 5, "accessible_complexity": 5},
        "novelty_classification": "partially_addressed",
        "novelty_score": 3,
        "novelty_method": "novelty_estimated",
        "sections": {
            "research_question": "To what extent does if harmful prompts",
            "approach_outline": (
                "Take 100 prompts. Refined: Refine novelty for "
                "'Test': Target a specific"
            ),
            "proposed_first_experiments": "Experiment 1: Set up framework. ~8 hours.",
            "theory_of_impact_chain": "Contamination means evaluations overestimate robustness.",
            "strength_rationale": "accessible_complexity (5/5): Standard Python scripting w",
            "alternative_framings": [
                "Benchmark: Test Idea Evaluati: Reframed for feasibility. (est. 4.25)",
            ],
            "cited_sources": [],
        },
    }
    write_refined_proposal(tmp_path, proposal)
    return proposal


class TestParseGenerateBody:
    def test_extracts_all_fields(self):
        body = (
            "# My Title\n\n"
            "**Problem:** A problem.\n\n"
            "**Direction:** An approach.\n\n"
            "**Why it matters:** Impact.\n\n"
            "**Relevant context:** Paper X."
        )
        fields = _parse_generate_body(body)
        assert fields["title"] == "My Title"
        assert fields["problem"] == "A problem."
        assert fields["direction"] == "An approach."
        assert fields["why_it_matters"] == "Impact."
        assert fields["relevant_context"] == "Paper X."

    def test_handles_empty_body(self):
        fields = _parse_generate_body("")
        assert fields == {}


class TestBuildStrengthRationale:
    def test_builds_from_scores(self):
        scores = {
            "theory_of_impact": {"score": 5, "reasoning": "Strong chain."},
            "accessible_complexity": {"score": 4, "reasoning": "Clear methodology."},
        }
        result = _build_strength_rationale(scores)
        assert "theory_of_impact (5/5): Strong chain." in result
        assert "accessible_complexity (4/5): Clear methodology." in result


class TestFixIdea:
    def test_fixes_truncated_approach_outline(self, tmp_path):
        _write_generate_idea(tmp_path)
        _write_scored_idea(tmp_path)
        refine = _write_truncated_refine(tmp_path)

        from safety_ideas.pipeline.generate import read_idea_sketches

        gen = read_idea_sketches(tmp_path)[0]
        scored_path = tmp_path / "filter_score" / "scored" / "gen-001.json"

        result = fix_idea("gen-001", gen, scored_path, refine, tmp_path)
        sections = result["proposal"]["sections"]

        assert "approach_outline" in result["changes"]
        # Should use the generate-stage direction, not the truncated version
        assert "Refined:" not in sections["approach_outline"]
        assert "paraphrases" in sections["approach_outline"]

    def test_fixes_truncated_strength_rationale(self, tmp_path):
        _write_generate_idea(tmp_path)
        _write_scored_idea(tmp_path)
        refine = _write_truncated_refine(tmp_path)

        from safety_ideas.pipeline.generate import read_idea_sketches

        gen = read_idea_sketches(tmp_path)[0]
        scored_path = tmp_path / "filter_score" / "scored" / "gen-001.json"

        result = fix_idea("gen-001", gen, scored_path, refine, tmp_path)
        sections = result["proposal"]["sections"]

        assert "strength_rationale" in result["changes"]
        assert "Compelling chain" in sections["strength_rationale"]

    def test_clears_truncated_alternative_framings(self, tmp_path):
        _write_generate_idea(tmp_path)
        _write_scored_idea(tmp_path)
        refine = _write_truncated_refine(tmp_path)

        from safety_ideas.pipeline.generate import read_idea_sketches

        gen = read_idea_sketches(tmp_path)[0]
        scored_path = tmp_path / "filter_score" / "scored" / "gen-001.json"

        result = fix_idea("gen-001", gen, scored_path, refine, tmp_path)

        assert any("alternative_framings" in c for c in result["changes"])
        assert result["proposal"]["sections"]["alternative_framings"] == []

    def test_populates_empty_cited_sources(self, tmp_path):
        _write_generate_idea(tmp_path)
        _write_scored_idea(tmp_path)
        refine = _write_truncated_refine(tmp_path)

        from safety_ideas.pipeline.generate import read_idea_sketches

        gen = read_idea_sketches(tmp_path)[0]
        scored_path = tmp_path / "filter_score" / "scored" / "gen-001.json"

        result = fix_idea("gen-001", gen, scored_path, refine, tmp_path)
        sections = result["proposal"]["sections"]

        assert "cited_sources" in result["changes"]
        assert len(sections["cited_sources"]) > 0

    def test_no_changes_if_not_truncated(self, tmp_path):
        _write_generate_idea(tmp_path)
        _write_scored_idea(tmp_path)

        from safety_ideas.pipeline.generate import read_idea_sketches

        gen = read_idea_sketches(tmp_path)[0]
        scored_path = tmp_path / "filter_score" / "scored" / "gen-001.json"

        # Proposal with complete, non-truncated content
        proposal = {
            "idea_id": "gen-001",
            "run_id": "test-run",
            "stage": "refine",
            "title": "Test Idea Title",
            "sections": {
                "research_question": "A complete research question about contamination.",
                "approach_outline": (
                    "Take 100 prompts and generate paraphrases."
                    " Compare ASR on models."
                ),
                "proposed_first_experiments": "Experiment 1: baseline.",
                "theory_of_impact_chain": (
                    "Contamination means evaluations overestimate"
                    " robustness."
                ),
                "strength_rationale": "Strong across all dimensions.",
                "alternative_framings": ["A valid framing without truncation."],
                "cited_sources": ["Paper A - relevant work"],
            },
        }
        write_refined_proposal(tmp_path, proposal)

        result = fix_idea("gen-001", gen, scored_path, proposal, tmp_path)
        assert result["changes"] == []


class TestUpdateSectionsInDict:
    def test_updates_matching_sections(self):
        idea = {"sections": {"approach_outline": "old", "cited_sources": []}}
        fixed = {"approach_outline": "new approach", "cited_sources": ["Paper A"]}
        changed = _update_sections_in_dict(idea, fixed)
        assert changed is True
        assert idea["sections"]["approach_outline"] == "new approach"
        assert idea["sections"]["cited_sources"] == ["Paper A"]

    def test_returns_false_when_unchanged(self):
        idea = {"sections": {"approach_outline": "same"}}
        changed = _update_sections_in_dict(idea, {"approach_outline": "same"})
        assert changed is False


class TestFixRankedProposals:
    def test_updates_json_and_regenerates_md(self, tmp_path):
        rank_dir = tmp_path / "rank"
        rank_dir.mkdir(parents=True)
        ranked = [
            {
                "idea_id": "gen-001",
                "rank": 1,
                "title": "Test",
                "weighted_score": 4.5,
                "sections": {
                    "research_question": "Q?",
                    "approach_outline": "old truncated",
                    "strength_rationale": "trunc",
                },
                "original_scores": {"theory_of_impact": 5},
            },
        ]
        with open(rank_dir / "ranked_proposals.json", "w") as f:
            json.dump(ranked, f)
        with open(rank_dir / "ranked_proposals.md", "w") as f:
            f.write("old markdown")

        fixed = {"gen-001": {"approach_outline": "complete approach."}}
        count = _fix_ranked_proposals(tmp_path, fixed)
        assert count == 3

        with open(rank_dir / "ranked_proposals.json") as f:
            updated = json.load(f)
        assert updated[0]["sections"]["approach_outline"] == "complete approach."

        with open(rank_dir / "ranked_proposals.md") as f:
            md = f.read()
        assert "complete approach." in md

    def test_returns_zero_when_no_rank_dir(self, tmp_path):
        count = _fix_ranked_proposals(tmp_path, {"gen-001": {"x": "y"}})
        assert count == 0
