"""Tests for the novelty assessment helpers."""

import pytest

from safety_ideas.pipeline.novelty import (
    NOVELTY_CLASSIFICATIONS,
    format_novelty_assessment,
    novelty_to_score,
    validate_classification,
)


class TestValidateClassification:
    def test_all_valid_classifications(self):
        for cls in NOVELTY_CLASSIFICATIONS:
            assert validate_classification(cls) == cls

    def test_invalid_classification_raises(self):
        with pytest.raises(ValueError, match="Unknown novelty classification"):
            validate_classification("not_valid")

    def test_returns_input_unchanged(self):
        assert validate_classification("novel") == "novel"


class TestNoveltyToScore:
    def test_all_classifications_have_scores(self):
        for cls in NOVELTY_CLASSIFICATIONS:
            score = novelty_to_score(cls)
            assert 1 <= score <= 5

    def test_already_solved_is_1(self):
        assert novelty_to_score("already_solved") == 1

    def test_largely_addressed_is_2(self):
        assert novelty_to_score("largely_addressed") == 2

    def test_partially_addressed_is_3(self):
        assert novelty_to_score("partially_addressed") == 3

    def test_mostly_novel_is_4(self):
        assert novelty_to_score("mostly_novel") == 4

    def test_novel_is_5(self):
        assert novelty_to_score("novel") == 5

    def test_invalid_classification_raises(self):
        with pytest.raises(ValueError, match="Unknown novelty classification"):
            novelty_to_score("not_a_valid_classification")

    def test_scores_are_monotonically_increasing(self):
        scores = [novelty_to_score(cls) for cls in NOVELTY_CLASSIFICATIONS]
        assert scores == sorted(scores)


class TestFormatNoveltyAssessment:
    def test_format_structure(self):
        evidence = [{"source": "arxiv", "title": "Paper A", "summary": "Does X"}]
        result = format_novelty_assessment(
            "mostly_novel", evidence, 0.7, "No direct work found on this approach."
        )
        assert result["classification"] == "mostly_novel"
        assert result["evidence"] == evidence
        assert result["confidence"] == 0.7
        assert result["derived_score"] == 4
        assert result["reasoning"] == "No direct work found on this approach."

    def test_format_already_solved(self):
        result = format_novelty_assessment("already_solved", [], 0.9, "Solved by X.")
        assert result["derived_score"] == 1
        assert result["reasoning"] == "Solved by X."

    def test_format_novel(self):
        result = format_novelty_assessment("novel", [], 0.5)
        assert result["derived_score"] == 5
        assert result["reasoning"] == ""

    def test_format_with_empty_reasoning(self):
        result = format_novelty_assessment("partially_addressed", [], 0.6)
        assert result["reasoning"] == ""
        assert result["derived_score"] == 3

    def test_format_rejects_invalid_classification(self):
        with pytest.raises(ValueError, match="Unknown novelty classification"):
            format_novelty_assessment("invalid", [], 0.5)

    def test_format_preserves_all_evidence(self):
        evidence = [
            {"source": "arxiv", "title": "P1", "summary": "S1"},
            {"source": "semantic_scholar", "title": "P2", "summary": "S2"},
            {"source": "google_scholar", "title": "P3", "summary": "S3"},
        ]
        result = format_novelty_assessment(
            "largely_addressed", evidence, 0.8, "Multiple papers cover this."
        )
        assert len(result["evidence"]) == 3
        assert result["derived_score"] == 2
