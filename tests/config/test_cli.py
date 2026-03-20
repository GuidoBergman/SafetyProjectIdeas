"""Tests for config CLI commands."""

from unittest.mock import patch

import pytest

from safety_ideas.config.cli import (
    show_batch_sizes_config,
    show_citation_relevance_config,
    show_config,
    show_generate_config,
    show_participant,
    show_quick_filter_config,
    show_scoring_config,
)
from safety_ideas.config.loader import AppConfig
from safety_ideas.config.schemas import (
    BatchSizeConfig,
    CitationRelevanceConfig,
    ConfidenceRubricLevel,
    GenerateSettings,
    ParticipantProfile,
    PipelineSettings,
    QuickFilterConfig,
    RubricLevel,
    ScoringCriteria,
    StageThreshold,
    TeamProfile,
)


def _make_config(
    *,
    team_type="mentor_novice",
    team_name="Test Team",
    criteria_weights=None,
    criteria=None,
    generate=None,
    thresholds=None,
):
    """Build an AppConfig for testing."""
    team = TeamProfile(
        name=team_name,
        team_type=team_type,
        technical_skills=["python"],
        criteria_weights=criteria_weights or {},
    )
    if criteria is None:
        criteria = [
            ScoringCriteria(
                name="theory_of_impact",
                description="Does this idea advance AI Safety?",
                default_weight=1.5,
            ),
            ScoringCriteria(
                name="low_compute",
                description="Can it run on limited compute?",
                default_weight=1.5,
            ),
        ]
    pipeline = PipelineSettings(
        generate=generate or GenerateSettings(),
        thresholds=thresholds or {"filter_score": StageThreshold(min_score=2.0, max_ideas=100)},
    )
    return AppConfig(
        teams={team_type: team},
        default_team=team_type,
        criteria=criteria,
        pipeline=pipeline,
    )


# --- show-generate ---


class TestShowGenerateConfig:
    def test_outputs_both_settings(self, capsys):
        config = _make_config(
            generate=GenerateSettings(min_ideas_per_strategy_per_subfield=30, combinatorial_top_n=5)
        )
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_generate_config()
        out = capsys.readouterr().out
        assert "min_ideas_per_strategy_per_subfield: 30" in out
        assert "combinatorial_top_n: 5" in out

    def test_outputs_defaults_when_not_customized(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_generate_config()
        out = capsys.readouterr().out
        assert "min_ideas_per_strategy_per_subfield: 25" in out
        assert "combinatorial_top_n: 10" in out

    def test_does_not_leak_other_config(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_generate_config()
        out = capsys.readouterr().out
        assert "Scoring" not in out
        assert "Team" not in out
        assert "Threshold" not in out


# --- show-scoring ---


class TestShowScoringConfig:
    def test_shows_default_weights_when_no_overrides(self, capsys):
        config = _make_config(criteria_weights={})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "[theory_of_impact] weight=1.5" in out
        assert "[low_compute] weight=1.5" in out

    def test_shows_active_weights_with_team_overrides(self, capsys):
        config = _make_config(criteria_weights={"low_compute": 0.0, "theory_of_impact": 3.0})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "[theory_of_impact] weight=3.0" in out
        assert "[low_compute] weight=0.0" in out
        # Should NOT show the default weights anywhere
        assert "weight=1.5" not in out

    def test_partial_overrides_mix_default_and_active(self, capsys):
        config = _make_config(criteria_weights={"low_compute": 2.0})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "[low_compute] weight=2.0" in out
        assert "[theory_of_impact] weight=1.5" in out

    def test_shows_default_team(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Default Team: mentor_novice" in out

    def test_shows_thresholds(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "filter_score: min_score=2.0, max_ideas=100" in out

    def test_does_not_leak_generate_settings(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "min_ideas_per_strategy" not in out
        assert "combinatorial" not in out

    def test_does_not_leak_participant_profiles(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Participant" not in out

    def test_does_not_leak_inactive_team_profiles(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Skills:" not in out
        assert "Team Profiles" not in out

    def test_shows_confidence_rubric(self, capsys):
        config = _make_config()
        config.pipeline.confidence_rubric = [
            ConfidenceRubricLevel(
                min=0.0, max=0.2, label="Very low", description="Essentially guessing"
            ),
            ConfidenceRubricLevel(
                min=0.8, max=1.0, label="Very high", description="Thorough evidence"
            ),
        ]
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Confidence Rubric" in out
        assert "[0.0-0.2] Very low: Essentially guessing" in out
        assert "[0.8-1.0] Very high: Thorough evidence" in out

    def test_hides_confidence_rubric_when_empty(self, capsys):
        config = _make_config()
        config.pipeline.confidence_rubric = []
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Confidence Rubric" not in out

    def test_shows_rubric_levels_for_criteria(self, capsys):
        criteria = [
            ScoringCriteria(
                name="theory_of_impact",
                description="Does this idea advance AI Safety?",
                default_weight=1.5,
                rubric=[
                    RubricLevel(score=1, label="No chain", description="No connection"),
                    RubricLevel(score=5, label="Compelling", description="Full chain"),
                ],
            ),
        ]
        config = _make_config(criteria=criteria)
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "[1] No chain: No connection" in out
        assert "[5] Compelling: Full chain" in out

    def test_novelty_marked_as_skip(self, capsys):
        criteria = [
            ScoringCriteria(
                name="theory_of_impact",
                description="Impact",
                default_weight=1.5,
            ),
            ScoringCriteria(
                name="novelty",
                description="How novel",
                default_weight=1.0,
                rubric=[
                    RubricLevel(score=1, label="Solved", description="Already done"),
                ],
            ),
        ]
        config = _make_config(criteria=criteria)
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "SKIP in Phase 2" in out
        assert "[novelty] weight=1.0" in out
        # Novelty rubric levels should NOT be printed
        assert "Solved" not in out

    def test_does_not_show_quick_filter(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_scoring_config()
        out = capsys.readouterr().out
        assert "Quick Filter" not in out


# --- show (full, for configure-teams) ---


class TestShowConfig:
    def test_show_config_runs(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            with patch("safety_ideas.config.cli.list_participants", return_value=[]):
                show_config()
        out = capsys.readouterr().out
        assert "Test Team" in out
        assert "theory_of_impact" in out

    def test_show_config_displays_active_weight_for_overridden_criteria(self, capsys):
        config = _make_config(criteria_weights={"low_compute": 0.0, "theory_of_impact": 3.0})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            with patch("safety_ideas.config.cli.list_participants", return_value=[]):
                show_config()
        out = capsys.readouterr().out
        # Overridden criteria should show active weight
        assert "Active weight (mentor_novice): 3.0" in out  # theory_of_impact
        assert "Active weight (mentor_novice): 0.0" in out  # low_compute

    def test_show_config_displays_active_weight_using_default_when_not_overridden(self, capsys):
        config = _make_config(criteria_weights={"low_compute": 0.0})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            with patch("safety_ideas.config.cli.list_participants", return_value=[]):
                show_config()
        out = capsys.readouterr().out
        # Non-overridden criteria should show active weight = default
        assert "Active weight (mentor_novice): 1.5 (using default)" in out

    def test_show_config_displays_both_default_and_active_weights(self, capsys):
        """Full show must display both default_weight and active weight so the user
        can see what's configured at the criterion level vs what the team overrides."""
        config = _make_config(criteria_weights={"low_compute": 0.0})
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            with patch("safety_ideas.config.cli.list_participants", return_value=[]):
                show_config()
        out = capsys.readouterr().out
        # Both should be present
        assert "Default weight: 1.5" in out
        assert "Active weight (mentor_novice): 0.0" in out


# --- show-participant ---


class TestShowParticipant:
    def test_prints_all_fields(self, capsys):
        profile = ParticipantProfile(
            name="alice",
            background="CS student",
            technical_skills="Python, basic ML",
            compute_resources="low",
            total_hours=30,
            time_context="30h total",
            deliverables="blog post",
            goals="learn safety",
        )
        with patch("safety_ideas.config.cli.get_default_participant", return_value=profile):
            show_participant()
        out = capsys.readouterr().out
        assert "name: alice" in out
        assert "background: CS student" in out
        assert "technical_skills: Python, basic ML" in out
        assert "compute_resources: low" in out
        assert "total_hours: 30" in out
        assert "time_context: 30h total" in out
        assert "deliverables: blog post" in out
        assert "goals: learn safety" in out

    def test_prints_no_participant_when_none(self, capsys):
        with patch("safety_ideas.config.cli.get_default_participant", return_value=None):
            show_participant()
        out = capsys.readouterr().out
        assert out.strip() == "NO_PARTICIPANT"

    def test_prints_every_model_field(self, capsys):
        """Ensure output covers all fields defined on ParticipantProfile."""
        profile = ParticipantProfile(
            name="test",
            background="bg",
            technical_skills="skills",
        )
        with patch("safety_ideas.config.cli.get_default_participant", return_value=profile):
            show_participant()
        out = capsys.readouterr().out
        for field_name in ParticipantProfile.model_fields:
            assert f"{field_name}:" in out


# --- show-quick-filter ---


class TestShowQuickFilterConfig:
    def test_shows_threshold_and_rubric(self, capsys):
        qf = QuickFilterConfig(
            threshold=2.0,
            rubric=[
                RubricLevel(score=1, label="Off-topic", description="Not AI Safety"),
                RubricLevel(score=3, label="Relevant", description="Clearly AI Safety"),
            ],
        )
        config = _make_config()
        config.pipeline.quick_filter = qf
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_quick_filter_config()
        out = capsys.readouterr().out
        assert "threshold: 2.0" in out
        assert "[1] Off-topic: Not AI Safety" in out
        assert "[3] Relevant: Clearly AI Safety" in out

    def test_does_not_leak_other_config(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_quick_filter_config()
        out = capsys.readouterr().out
        assert "Scoring" not in out
        assert "Team" not in out
        assert "Threshold" not in out
        assert "min_ideas" not in out


# --- show-citation-relevance ---


class TestShowCitationRelevanceConfig:
    def test_shows_threshold_and_rubric(self, capsys):
        cr = CitationRelevanceConfig(
            threshold=3,
            rubric=[
                RubricLevel(score=1, label="Decorative", description="Background only"),
                RubricLevel(score=3, label="Substantive", description="Supports a claim"),
                RubricLevel(score=5, label="Foundational", description="Idea builds on this"),
            ],
        )
        config = _make_config()
        config.pipeline.citation_relevance = cr
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_citation_relevance_config()
        out = capsys.readouterr().out
        assert "threshold: 3" in out
        assert "[1] Decorative: Background only" in out
        assert "[3] Substantive: Supports a claim" in out
        assert "[5] Foundational: Idea builds on this" in out

    def test_does_not_leak_other_config(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_citation_relevance_config()
        out = capsys.readouterr().out
        assert "Scoring" not in out
        assert "Team" not in out
        assert "min_ideas" not in out


# --- show-batch-sizes ---


class TestShowBatchSizesConfig:
    def test_shows_all_batch_sizes(self, capsys):
        config = _make_config()
        config.pipeline.batch_sizes = BatchSizeConfig(
            stage1_quick_filter=100,
            stage2_full_scoring=30,
            stage3_novelty_citations=15,
        )
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_batch_sizes_config()
        out = capsys.readouterr().out
        assert "stage1_quick_filter: 100" in out
        assert "stage2_full_scoring: 30" in out
        assert "stage3_novelty_citations: 15" in out

    def test_shows_defaults(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_batch_sizes_config()
        out = capsys.readouterr().out
        assert "stage1_quick_filter: 100" in out
        assert "stage2_full_scoring: 30" in out
        assert "stage3_novelty_citations: 15" in out

    def test_does_not_leak_other_config(self, capsys):
        config = _make_config()
        with patch("safety_ideas.config.cli.load_config", return_value=config):
            show_batch_sizes_config()
        out = capsys.readouterr().out
        assert "Scoring" not in out
        assert "Team" not in out
        assert "Threshold" not in out
        assert "min_ideas" not in out
