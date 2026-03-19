"""Tests for the filter_score pipeline stage."""

import json

from safety_ideas.config.schemas import ScoringCriteria, StageThreshold, TeamProfile
from safety_ideas.pipeline.filter_score import (
    apply_weights,
    read_scored_ideas,
    score_idea,
    staged_filter,
    write_scored_idea,
)


def _make_criteria():
    return [
        ScoringCriteria(
            name="theory_of_impact",
            description="Impact theory",
            default_weight=1.5,
            rubric=[],
        ),
        ScoringCriteria(
            name="low_compute",
            description="Compute requirements",
            default_weight=1.5,
            rubric=[],
        ),
        ScoringCriteria(
            name="novelty",
            description="Novelty",
            default_weight=1.0,
            rubric=[],
        ),
    ]


def _make_team(criteria_weights=None):
    return TeamProfile(
        name="Test Team",
        team_type="mentor_novice",
        criteria_weights=criteria_weights or {},
    )


def _make_idea(idea_id="gen-001"):
    return {
        "idea_id": idea_id,
        "run_id": "2026-03-19T14-30-00",
        "title": "Test Idea",
        "problem": "A test problem",
        "direction": "A test direction",
        "subfield": "interpretability",
    }


def _make_scored_idea(idea_id="gen-001", weighted_score=3.5, novelty_class="mostly_novel"):
    criteria = _make_criteria()
    team = _make_team()
    idea = _make_idea(idea_id)
    scored = score_idea(idea, criteria, team)
    scored["scores"]["theory_of_impact"] = {"score": 4, "reasoning": "Good", "confidence": 0.8}
    scored["scores"]["low_compute"] = {"score": 3, "reasoning": "OK", "confidence": 0.7}
    scored["scores"]["novelty"] = {"score": 4, "reasoning": "Derived", "confidence": 0.6}
    scored["weighted_score"] = weighted_score
    scored["novelty_assessment"]["classification"] = novelty_class
    return scored


class TestScoreIdea:
    def test_creates_scored_skeleton(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, criteria, team)

        assert scored["idea_id"] == "gen-001"
        assert scored["stage"] == "filter_score"
        assert scored["title"] == "Test Idea"
        assert scored["original_idea"] == idea
        assert "theory_of_impact" in scored["scores"]
        assert "low_compute" in scored["scores"]
        assert "novelty" in scored["scores"]
        assert scored["eliminated"] is False
        assert scored["elimination_reason"] is None

    def test_scores_have_empty_defaults(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, criteria, team)

        for name in ["theory_of_impact", "low_compute", "novelty"]:
            assert scored["scores"][name]["score"] == 0
            assert scored["scores"][name]["reasoning"] == ""
            assert scored["scores"][name]["confidence"] == 0.0


class TestApplyWeights:
    def test_default_weights(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 3, "reasoning": "", "confidence": 0.7},
            "novelty": {"score": 5, "reasoning": "", "confidence": 0.9},
        }
        # (4*1.5 + 3*1.5 + 5*1.0) / (1.5 + 1.5 + 1.0) = (6+4.5+5)/4 = 15.5/4 = 3.875
        result = apply_weights(scores, criteria, team)
        assert abs(result - 3.875) < 0.001

    def test_team_weight_overrides(self):
        criteria = _make_criteria()
        team = _make_team(criteria_weights={"novelty": 0.5})
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 3, "reasoning": "", "confidence": 0.7},
            "novelty": {"score": 5, "reasoning": "", "confidence": 0.9},
        }
        # (4*1.5 + 3*1.5 + 5*0.5) / (1.5 + 1.5 + 0.5) = (6+4.5+2.5)/3.5 = 13/3.5 = 3.714...
        result = apply_weights(scores, criteria, team)
        assert abs(result - 13.0 / 3.5) < 0.001

    def test_zero_scores_excluded(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 0, "reasoning": "", "confidence": 0.0},
            "novelty": {"score": 0, "reasoning": "", "confidence": 0.0},
        }
        # Only theory_of_impact: 4*1.5 / 1.5 = 4.0
        result = apply_weights(scores, criteria, team)
        assert abs(result - 4.0) < 0.001

    def test_all_zero_returns_zero(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 0, "reasoning": "", "confidence": 0.0},
        }
        result = apply_weights(scores, criteria, team)
        assert result == 0.0


class TestStagedFilter:
    def test_stage1_eliminates_low_scores(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(weighted_score=1.5)
        # Override scores so apply_weights returns < 2.0
        scored["scores"] = {
            "theory_of_impact": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "low_compute": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "novelty": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 1" in scored["elimination_reason"]

    def test_stage2_eliminates_below_threshold(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=3.5, max_ideas=500)

        scored = _make_scored_idea()
        # Scores that give weighted avg between 2.0 and 3.5
        scored["scores"] = {
            "theory_of_impact": {"score": 3, "reasoning": "OK", "confidence": 0.7},
            "low_compute": {"score": 2, "reasoning": "Low", "confidence": 0.6},
            "novelty": {"score": 3, "reasoning": "OK", "confidence": 0.6},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 2" in scored["elimination_reason"]

    def test_stage3_eliminates_already_solved(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(novelty_class="already_solved")
        scored["scores"] = {
            "theory_of_impact": {"score": 5, "reasoning": "Great", "confidence": 0.9},
            "low_compute": {"score": 5, "reasoning": "Great", "confidence": 0.9},
            "novelty": {"score": 1, "reasoning": "Solved", "confidence": 0.9},
        }
        scored["novelty_assessment"]["classification"] = "already_solved"

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "already_solved" in scored["elimination_reason"]
        assert scored["filter_stage_passed"] == 2

    def test_surviving_ideas_pass_all_stages(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(novelty_class="mostly_novel")
        scored["scores"] = {
            "theory_of_impact": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "low_compute": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "novelty": {"score": 4, "reasoning": "Good", "confidence": 0.8},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 1
        assert result[0]["filter_stage_passed"] == 3
        assert result[0]["eliminated"] is False

    def test_max_ideas_limit(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=2)

        ideas = []
        for i, score_val in enumerate([5, 3, 4], start=1):
            scored = _make_scored_idea(f"gen-{i:03d}", novelty_class="novel")
            scored["scores"] = {
                "theory_of_impact": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "low_compute": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "novelty": {"score": score_val, "reasoning": "X", "confidence": 0.8},
            }
            ideas.append(scored)

        result = staged_filter(ideas, criteria, thresholds, team)
        assert len(result) == 2
        # Top two by weighted score should survive
        surviving_ids = {r["idea_id"] for r in result}
        assert "gen-001" in surviving_ids  # score 5
        assert "gen-003" in surviving_ids  # score 4


class TestWriteRead:
    def test_write_creates_json(self, tmp_path):
        scored = _make_scored_idea()
        path = write_scored_idea(tmp_path, scored)

        assert path.exists()
        assert path.parent.name == "filter_score"
        assert path.name == "gen-001.json"

    def test_write_read_roundtrip(self, tmp_path):
        scored = _make_scored_idea("gen-001")
        write_scored_idea(tmp_path, scored)

        results = read_scored_ideas(tmp_path)
        assert len(results) == 1
        assert results[0]["idea_id"] == "gen-001"
        assert results[0]["stage"] == "filter_score"

    def test_read_multiple(self, tmp_path):
        for i in range(3):
            scored = _make_scored_idea(f"gen-{i+1:03d}")
            write_scored_idea(tmp_path, scored)

        results = read_scored_ideas(tmp_path)
        assert len(results) == 3
        ids = [r["idea_id"] for r in results]
        assert ids == ["gen-001", "gen-002", "gen-003"]

    def test_read_empty_dir(self, tmp_path):
        assert read_scored_ideas(tmp_path) == []

    def test_write_content_valid_json(self, tmp_path):
        scored = _make_scored_idea()
        path = write_scored_idea(tmp_path, scored)

        with open(path) as f:
            data = json.load(f)

        assert data["idea_id"] == "gen-001"
        assert data["stage"] == "filter_score"
        assert "scores" in data
        assert "novelty_assessment" in data
        assert "citation_verification" in data
