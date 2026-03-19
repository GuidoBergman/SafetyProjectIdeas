"""Tests for config CLI commands."""

from unittest.mock import patch

import pytest

from safety_ideas.config.cli import (
    show_config,
    show_generate_config,
    show_scoring_config,
)
from safety_ideas.config.loader import AppConfig
from safety_ideas.config.schemas import (
    GenerateSettings,
    PipelineSettings,
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
        config = _make_config(generate=GenerateSettings(min_ideas_per_strategy_per_subfield=30, combinatorial_top_n=5))
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
