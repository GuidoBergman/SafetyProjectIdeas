"""Tests for config writer (write-back to YAML with validation)."""

import yaml
import pytest
from pathlib import Path
from pydantic import ValidationError

from saim.config.schemas import (
    ParticipantProfile,
    PipelineSettings,
    ScoringCriteria,
    StageModelAssignment,
    StageThreshold,
    TeamProfile,
)
from saim.config.writer import (
    save_criteria,
    save_participant,
    save_pipeline,
    save_teams,
)
from saim.utils import load_yaml


class TestSaveTeams:
    def test_save_and_reload(self, tmp_path):
        teams = [
            TeamProfile(
                name="Test Team",
                team_type="mentor_novice",
                technical_skills=["python"],
                criteria_weights={"low_compute": 2.0},
            ),
            TeamProfile(
                name="Expert Team",
                team_type="experienced_group",
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
                name="theory_of_impact",
                description="Does this idea advance AI Safety?",
                default_weight=1.5,
            ),
        ]
        path = tmp_path / "criteria.yaml"
        save_criteria(criteria, path)

        data = load_yaml(path)
        assert len(data["criteria"]) == 1
        assert data["criteria"][0]["name"] == "theory_of_impact"
        assert data["criteria"][0]["default_weight"] == 1.5

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
                "filter_score": StageThreshold(min_score=3.0, max_ideas=15),
            },
        )
        path = tmp_path / "pipeline.yaml"
        save_pipeline(pipeline, path)

        data = load_yaml(path)
        assert data["model_assignments"]["generate"]["model"] == "opus"
        assert data["thresholds"]["filter_score"]["min_score"] == 3.0


class TestSaveParticipant:
    def test_save_and_reload(self, tmp_path):
        profile = ParticipantProfile(
            name="Alice",
            background="CS undergrad, first AI safety research experience",
            technical_skills="Beginner Python, basic ML/stats",
            compute_resources="low",
            total_hours=30,
            time_context="30 hours total including writing a blog post",
        )
        path = tmp_path / "alice.yaml"
        save_participant(profile, path)

        data = load_yaml(path)
        assert data["name"] == "Alice"
        assert data["background"] == "CS undergrad, first AI safety research experience"
        assert data["total_hours"] == 30

    def test_save_to_default_path(self, tmp_path, monkeypatch):
        """Saves to config/participants/<name>.yaml by default."""
        monkeypatch.setattr(
            "saim.config.writer.PARTICIPANTS_DIR", tmp_path
        )
        profile = ParticipantProfile(
            name="Bob Smith",
            background="PhD student in ML",
            technical_skills="Advanced Python, deep learning",
        )
        save_participant(profile)
        expected = tmp_path / "bob_smith.yaml"
        assert expected.exists()
        data = load_yaml(expected)
        assert data["name"] == "Bob Smith"
