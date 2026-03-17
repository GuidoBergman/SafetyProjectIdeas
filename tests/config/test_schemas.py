"""Tests for Pydantic config schemas."""

import pytest
from pydantic import ValidationError

from safety_ideas.config.schemas import (
    KBCriteria,
    ParticipantProfile,
    PipelineSettings,
    ScoringCriteria,
    StageModelAssignment,
    StageThreshold,
    TeamProfile,
)


class TestTeamProfile:
    def test_valid_mentor_novice(self):
        profile = TeamProfile(
            name="Test Team",
            team_type="mentor_novice",
            compute_budget="low",
            technical_skills=["python_basics"],
            criteria_weights={"low_compute": 2.0},
        )
        assert profile.team_type == "mentor_novice"
        assert profile.compute_budget == "low"

    def test_valid_experienced_group(self):
        profile = TeamProfile(
            name="Experts",
            team_type="experienced_group",
            compute_budget="high",
        )
        assert profile.criteria_weights == {}
        assert profile.technical_skills == []

    def test_invalid_team_type(self):
        with pytest.raises(ValidationError):
            TeamProfile(
                name="Bad",
                team_type="invalid_type",
                compute_budget="low",
            )

    def test_missing_required_fields(self):
        with pytest.raises(ValidationError):
            TeamProfile(name="Incomplete")


class TestScoringCriteria:
    def test_valid_criterion(self):
        criterion = ScoringCriteria(
            name="soundness",
            description="Is the idea sound?",
            default_weight=2.0,
            team_type_overrides={"mentor_novice": 1.5},
        )
        assert criterion.default_weight == 2.0
        assert criterion.team_type_overrides["mentor_novice"] == 1.5

    def test_weight_boundaries(self):
        # Valid at boundaries
        ScoringCriteria(name="min", description="test", default_weight=0.0)
        ScoringCriteria(name="max", description="test", default_weight=10.0)

    def test_weight_out_of_range(self):
        with pytest.raises(ValidationError):
            ScoringCriteria(name="bad", description="test", default_weight=11.0)

        with pytest.raises(ValidationError):
            ScoringCriteria(name="bad", description="test", default_weight=-1.0)

    def test_defaults(self):
        criterion = ScoringCriteria(name="test", description="desc", default_weight=1.0)
        assert criterion.team_type_overrides == {}


class TestKBCriteria:
    def test_valid_criteria(self):
        kb = KBCriteria(
            subfields_in_scope=["mechanistic_interpretability"],
            organizations=["Anthropic"],
            authors=["Alice"],
            exclusions=["non_ai_safety"],
        )
        assert len(kb.subfields_in_scope) == 1

    def test_all_defaults(self):
        kb = KBCriteria()
        assert kb.subfields_in_scope == []
        assert kb.organizations == []
        assert kb.authors == []
        assert kb.exclusions == []


class TestPipelineSettings:
    def test_valid_settings(self):
        settings = PipelineSettings(
            model_assignments={
                "generate": StageModelAssignment(model="sonnet", fallback="haiku"),
            },
            thresholds={
                "filter_score": StageThreshold(min_score=5.0, max_ideas=20),
            },
        )
        assert settings.model_assignments["generate"].model == "sonnet"
        assert settings.thresholds["filter_score"].min_score == 5.0

    def test_empty_defaults(self):
        settings = PipelineSettings()
        assert settings.model_assignments == {}
        assert settings.thresholds == {}

    def test_threshold_boundaries(self):
        StageThreshold(min_score=0.0, max_ideas=1)
        StageThreshold(min_score=10.0, max_ideas=100)

    def test_threshold_invalid(self):
        with pytest.raises(ValidationError):
            StageThreshold(min_score=11.0, max_ideas=1)
        with pytest.raises(ValidationError):
            StageThreshold(min_score=5.0, max_ideas=0)


class TestParticipantProfile:
    def test_valid_profile(self):
        profile = ParticipantProfile(
            name="Alice",
            experience_level="beginner",
            technical_background=["python"],
            compute_resources="low",
            time_availability="part_time",
        )
        assert profile.name == "Alice"
        assert profile.experience_level == "beginner"

    def test_defaults(self):
        profile = ParticipantProfile(
            name="Bob",
            experience_level="intermediate",
        )
        assert profile.compute_resources == "low"
        assert profile.time_availability == "part_time"
        assert profile.technical_background == []

    def test_missing_required(self):
        with pytest.raises(ValidationError):
            ParticipantProfile(name="NoLevel")
