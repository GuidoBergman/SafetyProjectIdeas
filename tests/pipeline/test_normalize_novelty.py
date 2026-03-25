"""Tests for normalize_novelty_scores in novelty.py."""

import copy

import pytest

from safety_ideas.pipeline.novelty import normalize_novelty_scores


def _make_idea(**overrides):
    """Build a minimal scored idea dict for testing."""
    base = {
        "idea_id": "gen-test",
        "scores": {
            "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
        },
        "novelty_assessment": None,
    }
    base.update(overrides)
    return base


class TestProperAssessment:
    """Case 1: idea has classification + evidence (the real novelty method)."""

    def test_keeps_derived_score_and_marks_assessed(self):
        idea = _make_idea(
            scores={
                "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
                "novelty": {"score": 3, "reasoning": "LLM guess", "confidence": 0.5},
            },
            novelty_assessment={
                "classification": "mostly_novel",
                "evidence": [{"source": "arxiv", "title": "Paper A"}],
                "confidence": 0.8,
                "derived_score": 4,
                "reasoning": "Web search found no direct match.",
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_assessed"
        assert result["scores"]["novelty"]["score"] == 4
        assert result["novelty_assessment"]["derived_score"] == 4
        assert result["novelty_assessment"]["classification"] == "mostly_novel"

    def test_derives_score_from_classification_if_missing(self):
        idea = _make_idea(
            novelty_assessment={
                "classification": "largely_addressed",
                "evidence": [{"source": "scholar"}],
                "confidence": 0.7,
                "derived_score": None,
                "reasoning": "Found related work.",
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_assessed"
        assert result["novelty_assessment"]["derived_score"] == 2
        assert result["scores"]["novelty"]["score"] == 2

    def test_already_solved_is_assessed(self):
        idea = _make_idea(
            novelty_assessment={
                "classification": "already_solved",
                "evidence": [{"source": "arxiv", "title": "Exact match"}],
                "confidence": 0.95,
                "derived_score": 1,
                "reasoning": "Exact match found.",
            },
        )
        result = normalize_novelty_scores(idea)
        assert result["novelty_method"] == "novelty_assessed"
        assert result["scores"]["novelty"]["score"] == 1


class TestOldFormatAssessment:
    """Case 2: novelty_assessment uses label/score or novelty_label/novelty_score."""

    def test_label_score_format(self):
        idea = _make_idea(
            scores={
                "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
                "novelty": {"score": 3, "reasoning": "LLM guess", "confidence": 0.5},
            },
            novelty_assessment={
                "label": "largely_addressed",
                "score": 2,
                "reasoning": "Multiple papers cover this.",
                "key_references": ["Paper A", "Paper B"],
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 2
        assert result["novelty_assessment"]["classification"] == "largely_addressed"
        assert result["novelty_assessment"]["derived_score"] == 2
        assert result["novelty_assessment"]["evidence"] == ["Paper A", "Paper B"]

    def test_novelty_label_novelty_score_format(self):
        idea = _make_idea(
            novelty_assessment={
                "novelty_label": "mostly_novel",
                "novelty_score": 4,
                "reasoning": "New angle.",
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 4
        assert result["novelty_assessment"]["classification"] == "mostly_novel"

    def test_label_with_existing_work_key(self):
        idea = _make_idea(
            novelty_assessment={
                "label": "partially_addressed",
                "score": 3,
                "reasoning": "Some related work.",
                "existing_work": ["Work A"],
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_assessment"]["evidence"] == ["Work A"]

    def test_score_only_no_label(self):
        """Old format with score but unrecognized label falls back to score-based mapping."""
        idea = _make_idea(
            novelty_assessment={
                "label": "",
                "score": 4,
                "reasoning": "Mostly new.",
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 4
        assert result["novelty_assessment"]["classification"] == "mostly_novel"


class TestScoresNoveltyOnly:
    """Case 3: only scores.novelty exists, no real novelty_assessment."""

    def test_builds_assessment_from_scores_novelty(self):
        idea = _make_idea(
            scores={
                "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
                "novelty": {"score": 4, "reasoning": "Seems novel", "confidence": 0.6},
            },
            novelty_assessment=None,
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 4
        assert result["novelty_assessment"]["classification"] == "mostly_novel"
        assert result["novelty_assessment"]["derived_score"] == 4
        assert result["novelty_assessment"]["evidence"] == []

    def test_not_assessed_classification_treated_as_missing(self):
        idea = _make_idea(
            scores={
                "novelty": {"score": 3, "reasoning": "LLM scored", "confidence": 0.5},
            },
            novelty_assessment={
                "classification": "not_assessed",
                "evidence": [],
                "confidence": 0.0,
                "derived_score": None,
                "reasoning": "Novelty not assessed.",
            },
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 3


class TestNoNovelty:
    """Case 4: no novelty information at all."""

    def test_assigns_default_score(self):
        idea = _make_idea(
            scores={"theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5}},
            novelty_assessment=None,
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 3
        assert result["novelty_assessment"]["classification"] == "partially_addressed"
        assert result["novelty_assessment"]["derived_score"] == 3

    def test_empty_scores_novelty_treated_as_missing(self):
        idea = _make_idea(
            scores={
                "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
                "novelty": {"score": 0, "reasoning": "", "confidence": 0.0},
            },
            novelty_assessment=None,
        )
        result = normalize_novelty_scores(idea)

        assert result["novelty_method"] == "novelty_estimated"
        assert result["scores"]["novelty"]["score"] == 3

    def test_null_novelty_assessment(self):
        idea = _make_idea(novelty_assessment=None)
        result = normalize_novelty_scores(idea)
        assert result["novelty_method"] == "novelty_estimated"
        assert result["novelty_assessment"]["derived_score"] == 3


class TestMutatesInPlace:
    def test_returns_same_object(self):
        idea = _make_idea()
        result = normalize_novelty_scores(idea)
        assert result is idea

    def test_idempotent_for_assessed(self):
        idea = _make_idea(
            novelty_assessment={
                "classification": "novel",
                "evidence": [{"source": "web"}],
                "confidence": 0.9,
                "derived_score": 5,
                "reasoning": "Totally new.",
            },
        )
        first = normalize_novelty_scores(idea)
        snapshot = copy.deepcopy(first)
        second = normalize_novelty_scores(first)
        assert second["novelty_method"] == snapshot["novelty_method"]
        assert second["scores"]["novelty"]["score"] == snapshot["scores"]["novelty"]["score"]
