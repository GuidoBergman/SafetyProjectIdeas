"""Tests for the rank pipeline stage."""

import json

from saim.config.schemas import ScoringCriteria, TeamProfile
from saim.pipeline.rank import (
    format_ranked_output,
    persist_ideas,
    rank_proposals,
    write_ranked_output,
)


def _make_criteria() -> list[ScoringCriteria]:
    return [
        ScoringCriteria(name="theory_of_impact", description="ToI", default_weight=2.0),
        ScoringCriteria(name="low_compute", description="LC", default_weight=1.5),
        ScoringCriteria(name="novelty", description="Nov", default_weight=1.0),
    ]


def _make_team() -> TeamProfile:
    return TeamProfile(name="Test Team", team_type="mentor_novice", criteria_weights={})


def _make_proposal(idea_id: str, scores: dict | None = None, novelty_score: int = 3) -> dict:
    return {
        "idea_id": idea_id,
        "run_id": "run_001",
        "stage": "refine",
        "timestamp": "2026-01-01T00:00:00Z",
        "title": f"Proposal {idea_id}",
        "original_scores": {"theory_of_impact": 4, "low_compute": 3},
        "scores": scores,
        "novelty_classification": "novel_contribution",
        "novelty_score": novelty_score,
        "subfield": "interpretability",
        "generation_strategy": "divergent",
        "provenance": {
            "generation_method": "brainstorm",
            "kb_sources": ["src1"],
            "web_sources": ["web1", "web2"],
        },
        "sections": {
            "research_question": "How does X affect Y?",
            "approach_outline": "We will do A then B then C.",
            "proposed_first_experiments": "Experiment 1: ...",
            "theory_of_impact_chain": "If X then Y then Z.",
        },
    }


class TestRankProposals:
    def test_sorts_descending_by_weighted_score(self):
        criteria = _make_criteria()
        team = _make_team()
        proposals = [
            _make_proposal("low", novelty_score=1),
            _make_proposal("high", novelty_score=5),
        ]
        # Give "high" better original_scores
        proposals[1]["original_scores"] = {"theory_of_impact": 5, "low_compute": 5}

        result = rank_proposals(proposals, criteria, team)

        assert result[0]["idea_id"] == "high"
        assert result[1]["idea_id"] == "low"

    def test_adds_rank_field(self):
        criteria = _make_criteria()
        team = _make_team()
        proposals = [_make_proposal("a"), _make_proposal("b")]

        result = rank_proposals(proposals, criteria, team)

        ranks = [p["rank"] for p in result]
        assert ranks == [1, 2]

    def test_uses_scores_dict_when_present(self):
        criteria = _make_criteria()
        team = _make_team()
        full_scores = {
            "theory_of_impact": {"score": 5, "reasoning": "good", "confidence": 0.9},
            "low_compute": {"score": 5, "reasoning": "good", "confidence": 0.9},
        }
        proposal = _make_proposal("full", scores=full_scores)

        result = rank_proposals([proposal], criteria, team)

        assert result[0]["weighted_score"] > 0

    def test_falls_back_to_original_scores(self):
        criteria = _make_criteria()
        team = _make_team()
        proposal = _make_proposal("fallback", scores=None)

        result = rank_proposals([proposal], criteria, team)

        assert result[0]["weighted_score"] > 0

    def test_includes_novelty_score(self):
        criteria = _make_criteria()
        team = _make_team()
        # One with novelty, one without
        with_novelty = _make_proposal("with_nov", novelty_score=5)
        without_novelty = _make_proposal("without_nov", novelty_score=None)
        # Same base scores
        without_novelty["original_scores"] = with_novelty["original_scores"].copy()

        result_with = rank_proposals([with_novelty], criteria, team)
        result_without = rank_proposals([without_novelty], criteria, team)

        # With novelty=5 should score higher (novelty adds to weighted avg)
        assert result_with[0]["weighted_score"] >= result_without[0]["weighted_score"]

    def test_empty_proposals(self):
        result = rank_proposals([], _make_criteria(), _make_team())
        assert result == []

    def test_does_not_mutate_input(self):
        criteria = _make_criteria()
        team = _make_team()
        proposal = _make_proposal("orig")
        original_keys = set(proposal.keys())

        rank_proposals([proposal], criteria, team)

        # Original should not have rank or weighted_score added
        assert "rank" not in proposal
        assert set(proposal.keys()) == original_keys


class TestFormatRankedOutput:
    def test_contains_header_and_count(self):
        proposals = [_make_proposal("a")]
        proposals[0]["rank"] = 1
        proposals[0]["weighted_score"] = 3.75

        md = format_ranked_output(proposals)

        assert "# Ranked Research Proposals" in md
        assert "Total proposals: 1" in md

    def test_contains_proposal_details(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.75

        md = format_ranked_output([proposal])

        assert "## #1: Proposal a (Score: 3.75)" in md
        assert "**ID:** a" in md
        assert "**Research Question:**" in md
        assert "**Approach:**" in md
        assert "**Subfield:** interpretability" in md
        assert "**Provenance:** brainstorm, sources: 1 KB, 2 web" in md

    def test_displays_rescored_scores_with_reasoning_and_confidence(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 4.0
        proposal["scores"] = {
            "theory_of_impact": {"score": 5, "reasoning": "great", "confidence": 0.9},
            "low_compute": {"score": 4, "reasoning": "good", "confidence": 0.8},
        }

        md = format_ranked_output([proposal])

        assert "**theory_of_impact:** 5, confidence: 0.9 — great" in md
        assert "**low_compute:** 4, confidence: 0.8 — good" in md

    def test_does_not_truncate_long_approach(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.0
        long_approach = "x" * 200
        proposal["sections"]["approach_outline"] = long_approach

        md = format_ranked_output([proposal])

        approach_line = [line for line in md.split("\n") if "**Approach:**" in line][0]
        assert long_approach in approach_line

    def test_includes_experiments_and_impact_chain(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.0

        md = format_ranked_output([proposal])

        assert "**Experiments:** Experiment 1: ..." in md
        assert "**Impact Chain:** If X then Y then Z." in md

    def test_includes_alternative_framings_and_cited_sources(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.0
        proposal["sections"]["alternative_framings"] = ["Framing A", "Framing B"]
        proposal["sections"]["cited_sources"] = ["Source 1", "Source 2"]

        md = format_ranked_output([proposal])

        assert "**Alternative Framings:** Framing A; Framing B" in md
        assert "**Cited Sources:** Source 1; Source 2" in md

    def test_includes_strength_rationale(self):
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.0
        proposal["sections"]["strength_rationale"] = "This is strong because X."

        md = format_ranked_output([proposal])

        assert "**Strength Rationale:** This is strong because X." in md


class TestPersistIdeas:
    def test_writes_markdown_files(self, tmp_path):
        proposal = _make_proposal("idea_001")
        proposal["rank"] = 1
        proposal["weighted_score"] = 4.0

        paths = persist_ideas([proposal], ideas_dir=tmp_path)

        assert len(paths) == 1
        assert paths[0].name == "idea_001.md"
        assert paths[0].exists()

    def test_file_has_frontmatter_and_body(self, tmp_path):
        proposal = _make_proposal("idea_002")
        proposal["rank"] = 1
        proposal["weighted_score"] = 4.0

        persist_ideas([proposal], ideas_dir=tmp_path)

        content = (tmp_path / "idea_002.md").read_text()
        assert content.startswith("---\n")
        assert "idea_id: idea_002" in content
        assert "# Research Question" in content
        assert "# Approach Outline" in content

    def test_creates_directory(self, tmp_path):
        target = tmp_path / "subdir" / "ideas"
        proposal = _make_proposal("idea_003")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.0

        persist_ideas([proposal], ideas_dir=target)

        assert target.exists()

    def test_empty_list(self, tmp_path):
        paths = persist_ideas([], ideas_dir=tmp_path)
        assert paths == []


class TestWriteRankedOutput:
    def test_writes_md_and_json(self, tmp_path, monkeypatch):
        # Monkeypatch OUTPUT_DIR to avoid writing to real data/
        fake_output = tmp_path / "output"
        monkeypatch.setattr("saim.pipeline.rank.OUTPUT_DIR", fake_output)

        run_dir = tmp_path / "run_001"
        proposal = _make_proposal("a")
        proposal["rank"] = 1
        proposal["weighted_score"] = 3.5
        md = "# Test markdown"

        result = write_ranked_output(run_dir, [proposal], md)

        assert result == run_dir / "rank" / "ranked_proposals.md"
        assert result.read_text() == "# Test markdown"

        json_path = run_dir / "rank" / "ranked_proposals.json"
        assert json_path.exists()
        data = json.loads(json_path.read_text())
        assert len(data) == 1
        assert data[0]["idea_id"] == "a"

    def test_copies_to_output_dir(self, tmp_path, monkeypatch):
        fake_output = tmp_path / "output"
        monkeypatch.setattr("saim.pipeline.rank.OUTPUT_DIR", fake_output)

        run_dir = tmp_path / "run_001"
        md = "# Output copy test"

        write_ranked_output(run_dir, [], md)

        output_copy = fake_output / "ranked_proposals.md"
        assert output_copy.exists()
        assert output_copy.read_text() == "# Output copy test"
