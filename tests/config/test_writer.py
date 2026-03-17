"""Tests for config writer (write-back to YAML with validation)."""

import yaml
import pytest
from pathlib import Path
from pydantic import ValidationError

from safety_ideas.config.schemas import (
    ParticipantProfile,
    PipelineSettings,
    ScoringCriteria,
    StageModelAssignment,
    StageThreshold,
    TeamProfile,
)
from safety_ideas.config.writer import (
    save_criteria,
    save_participant,
    save_pipeline,
    save_teams,
)
from safety_ideas.utils import load_yaml


class TestSaveTeams:
    def test_save_and_reload(self, tmp_path):
        teams = [
            TeamProfile(
                name="Test Team",
                team_type="mentor_novice",
                compute_budget="low",
                technical_skills=["python"],
                criteria_weights={"low_compute": 2.0},
            ),
            TeamProfile(
                name="Expert Team",
                team_type="experienced_group",
                compute_budget="high",
            ),
        ]
        path = tmp_path / "teams.yaml"
        save_teams(teams, path)

        data = load_yaml(path)
        assert len(data["teams"]) == 2
        assert data["teams"][0]["name"] == "Test Team"
        assert data["teams"][1]["team_type"] == "experienced_group"

    def test_save_empty_list(self, tmp_path):
        path = tmp_path / "teams.yaml"
        save_teams([], path)
        data = load_yaml(path)
        assert data["teams"] == []


class TestSaveCriteria:
    def test_save_and_reload(self, tmp_path):
        criteria = [
            ScoringCriteria(
                name="soundness",
                description="Is the idea sound?",
                default_weight=2.0,
                team_type_overrides={"mentor_novice": 1.5},
            ),
        ]
        path = tmp_path / "criteria.yaml"
        save_criteria(criteria, path)

        data = load_yaml(path)
        assert len(data["criteria"]) == 1
        assert data["criteria"][0]["name"] == "soundness"
        assert data["criteria"][0]["default_weight"] == 2.0

    def test_save_custom_criterion(self, tmp_path):
        """FR54: custom criteria beyond defaults."""
        criteria = [
            ScoringCriteria(
                name="reproducibility",
                description="Can others reproduce this work?",
                default_weight=1.5,
            ),
        ]
        path = tmp_path / "criteria.yaml"
        save_criteria(criteria, path)
        data = load_yaml(path)
        assert data["criteria"][0]["name"] == "reproducibility"


class TestSavePipeline:
    def test_save_and_reload(self, tmp_path):
        pipeline = PipelineSettings(
            model_assignments={
                "generate": StageModelAssignment(model="opus", fallback="sonnet"),
            },
            thresholds={
                "filter_score": StageThreshold(min_score=6.0, max_ideas=15),
            },
        )
        path = tmp_path / "pipeline.yaml"
        save_pipeline(pipeline, path)

        data = load_yaml(path)
        assert data["model_assignments"]["generate"]["model"] == "opus"
        assert data["thresholds"]["filter_score"]["min_score"] == 6.0


class TestSaveParticipant:
    def test_save_and_reload(self, tmp_path):
        profile = ParticipantProfile(
            name="Alice",
            experience_level="beginner",
            technical_background=["python"],
            compute_resources="low",
            time_availability="part_time",
        )
        path = tmp_path / "alice.yaml"
        save_participant(profile, path)

        data = load_yaml(path)
        assert data["name"] == "Alice"
        assert data["experience_level"] == "beginner"
        assert data["technical_background"] == ["python"]

    def test_save_to_default_path(self, tmp_path, monkeypatch):
        """Saves to config/participants/<name>.yaml by default."""
        monkeypatch.setattr(
            "safety_ideas.config.writer.PARTICIPANTS_DIR", tmp_path
        )
        profile = ParticipantProfile(
            name="Bob Smith",
            experience_level="intermediate",
        )
        save_participant(profile)
        expected = tmp_path / "bob_smith.yaml"
        assert expected.exists()
        data = load_yaml(expected)
        assert data["name"] == "Bob Smith"
