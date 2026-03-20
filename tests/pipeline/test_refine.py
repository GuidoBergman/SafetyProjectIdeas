"""Tests for the refine pipeline stage."""

from pathlib import Path

from safety_ideas.config.schemas import ScoringCriteria
from safety_ideas.pipeline.refine import (
    build_proposal_skeleton,
    build_refinement_context,
    identify_weak_dimensions,
    read_refined_proposals,
    write_refined_proposal,
)


def _make_criteria() -> list[ScoringCriteria]:
    """Create test scoring criteria."""
    return [
        ScoringCriteria(name="theory_of_impact", description="ToI", default_weight=1.0),
        ScoringCriteria(name="low_compute", description="Compute", default_weight=1.0),
        ScoringCriteria(name="feasibility", description="Feasibility", default_weight=1.0),
        ScoringCriteria(name="novelty", description="Novelty", default_weight=1.0),
    ]


def _make_scored_idea(
    scores: dict[str, int] | None = None,
) -> dict:
    """Create a test scored idea."""
    if scores is None:
        scores = {
            "theory_of_impact": 4,
            "low_compute": 2,
            "feasibility": 5,
            "novelty": 3,
        }
    return {
        "idea_id": "gen-001",
        "run_id": "2026-03-19T14-30-00",
        "stage": "filter_score",
        "title": "Test Idea",
        "original_idea": {
            "idea_id": "gen-001",
            "run_id": "2026-03-19T14-30-00",
            "body": "A research idea about interpretability.",
            "subfield": "interpretability",
            "generation_strategy": "novel_directions",
        },
        "scores": {
            name: {"score": val, "reasoning": f"Reasoning for {name}", "confidence": 0.8}
            for name, val in scores.items()
        },
        "novelty_assessment": {
            "classification": "mostly_novel",
            "derived_score": 4,
            "confidence": 0.7,
        },
        "weighted_score": 3.5,
    }


class TestIdentifyWeakDimensions:
    def test_returns_bottom_two(self):
        scored = _make_scored_idea()
        criteria = _make_criteria()
        weak = identify_weak_dimensions(scored, criteria)
        assert weak == ["low_compute", "novelty"]

    def test_returns_up_to_two(self):
        scored = _make_scored_idea({"only_one": 3})
        criteria = [ScoringCriteria(name="only_one", description="x", default_weight=1.0)]
        weak = identify_weak_dimensions(scored, criteria)
        assert len(weak) == 1
        assert weak == ["only_one"]

    def test_ignores_criteria_not_in_list(self):
        scored = _make_scored_idea()
        # Only include two criteria
        criteria = [
            ScoringCriteria(name="theory_of_impact", description="ToI", default_weight=1.0),
            ScoringCriteria(name="feasibility", description="F", default_weight=1.0),
        ]
        weak = identify_weak_dimensions(scored, criteria)
        assert weak == ["theory_of_impact", "feasibility"]

    def test_empty_scores(self):
        scored = {"scores": {}}
        criteria = _make_criteria()
        assert identify_weak_dimensions(scored, criteria) == []


class TestBuildRefinementContext:
    def test_structure(self):
        scored = _make_scored_idea()
        weak = ["low_compute", "novelty"]
        ctx = build_refinement_context(scored, weak)

        assert ctx["idea_id"] == "gen-001"
        assert ctx["title"] == "Test Idea"
        assert ctx["original_body"] == "A research idea about interpretability."
        assert ctx["novelty_classification"] == "mostly_novel"
        assert len(ctx["weak_dimensions"]) == 2
        assert ctx["weak_dimensions"][0]["name"] == "low_compute"
        assert ctx["weak_dimensions"][0]["score"] == 2
        assert len(ctx["strong_dimensions"]) == 2
        assert len(ctx["suggestions"]) == 2

    def test_suggestions_reference_weak_dims(self):
        scored = _make_scored_idea()
        weak = ["low_compute"]
        ctx = build_refinement_context(scored, weak)
        assert "low_compute" in ctx["suggestions"][0]
        assert "2" in ctx["suggestions"][0]

    def test_strong_dims_sorted_descending(self):
        scored = _make_scored_idea()
        weak = ["low_compute"]
        ctx = build_refinement_context(scored, weak)
        scores = [d["score"] for d in ctx["strong_dimensions"]]
        assert scores == sorted(scores, reverse=True)


class TestBuildProposalSkeleton:
    def test_structure(self):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, ["low_compute"])
        skeleton = build_proposal_skeleton(scored, refinement)

        assert skeleton["idea_id"] == "gen-001"
        assert skeleton["stage"] == "refine"
        assert skeleton["subfield"] == "interpretability"
        assert skeleton["generation_strategy"] == "novel_directions"
        assert skeleton["novelty_classification"] == "mostly_novel"
        assert skeleton["novelty_score"] == 4
        assert skeleton["pre_refine_weighted_score"] == 3.5
        assert skeleton["weak_dimensions_addressed"] == ["low_compute"]
        assert skeleton["num_alternative_framings"] == 0
        assert skeleton["refinement_confidence"] == 0.0
        assert "provenance" in skeleton
        assert skeleton["provenance"]["generation_method"] == "novel_directions"

    def test_sections_present(self):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, [])
        skeleton = build_proposal_skeleton(scored, refinement)

        sections = skeleton["sections"]
        assert "research_question" in sections
        assert "approach_outline" in sections
        assert "proposed_first_experiments" in sections
        assert "theory_of_impact_chain" in sections
        assert "strength_rationale" in sections
        assert isinstance(sections["alternative_framings"], list)
        assert isinstance(sections["cited_sources"], list)

    def test_original_scores_are_ints(self):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, [])
        skeleton = build_proposal_skeleton(scored, refinement)
        for val in skeleton["original_scores"].values():
            assert isinstance(val, int)


class TestWriteAndReadProposals:
    def test_roundtrip(self, tmp_path: Path):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, ["low_compute"])
        proposal = build_proposal_skeleton(scored, refinement)
        proposal["sections"]["research_question"] = "How does X affect Y?"
        proposal["sections"]["cited_sources"] = ["Paper A", "Paper B"]

        path = write_refined_proposal(tmp_path, proposal)
        assert path.exists()
        assert path.name == "gen-001.md"

        # Read back
        proposals = read_refined_proposals(tmp_path)
        assert len(proposals) == 1
        p = proposals[0]
        assert p["idea_id"] == "gen-001"
        assert p["stage"] == "refine"
        assert p["sections"]["research_question"] == "How does X affect Y?"
        assert p["sections"]["cited_sources"] == ["Paper A", "Paper B"]

    def test_empty_dir(self, tmp_path: Path):
        assert read_refined_proposals(tmp_path) == []

    def test_nonexistent_dir(self, tmp_path: Path):
        assert read_refined_proposals(tmp_path / "nope") == []

    def test_multiple_proposals_sorted(self, tmp_path: Path):
        for idea_id in ["gen-003", "gen-001", "gen-002"]:
            scored = _make_scored_idea()
            scored["idea_id"] = idea_id
            refinement = build_refinement_context(scored, [])
            proposal = build_proposal_skeleton(scored, refinement)
            write_refined_proposal(tmp_path, proposal)

        proposals = read_refined_proposals(tmp_path)
        ids = [p["idea_id"] for p in proposals]
        assert ids == ["gen-001", "gen-002", "gen-003"]

    def test_list_sections_roundtrip(self, tmp_path: Path):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, [])
        proposal = build_proposal_skeleton(scored, refinement)
        proposal["sections"]["alternative_framings"] = ["Framing A", "Framing B"]

        write_refined_proposal(tmp_path, proposal)
        proposals = read_refined_proposals(tmp_path)
        assert proposals[0]["sections"]["alternative_framings"] == ["Framing A", "Framing B"]

    def test_frontmatter_contains_metadata(self, tmp_path: Path):
        scored = _make_scored_idea()
        refinement = build_refinement_context(scored, ["low_compute"])
        proposal = build_proposal_skeleton(scored, refinement)

        path = write_refined_proposal(tmp_path, proposal)
        content = path.read_text()
        assert "---" in content
        assert "idea_id: gen-001" in content
        assert "stage: refine" in content
        assert "novelty_classification: mostly_novel" in content
