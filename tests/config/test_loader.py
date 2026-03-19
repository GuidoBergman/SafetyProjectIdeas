"""Tests for config loader."""

from pathlib import Path

import pytest
import yaml

from safety_ideas.config.loader import AppConfig, load_config


@pytest.fixture
def config_dir(tmp_path):
    """Create a temporary config directory with valid YAML files."""
    teams = {
        "teams": [
            {
                "name": "Test Team",
                "team_type": "mentor_novice",
                "technical_skills": ["python"],
                "criteria_weights": {"low_compute": 2.0},
            }
        ]
    }
    criteria = {
        "criteria": [
            {
                "name": "theory_of_impact",
                "description": "Does this idea advance AI Safety?",
                "default_weight": 1.5,
            }
        ]
    }
    pipeline = {
        "model_assignments": {
            "generate": {"model": "sonnet", "fallback": "haiku"},
        },
        "thresholds": {
            "filter_score": {"min_score": 3.0, "max_ideas": 20},
        },
    }
    kb_criteria = {
        "subfields_in_scope": ["mechanistic_interpretability"],
        "organizations": ["Anthropic"],
        "authors": [],
        "exclusions": [],
    }

    for name, data in [
        ("teams.yaml", teams),
        ("criteria.yaml", criteria),
        ("pipeline.yaml", pipeline),
        ("kb-criteria.yaml", kb_criteria),
    ]:
        (tmp_path / name).write_text(yaml.dump(data))

    return tmp_path


def test_load_config_valid(config_dir):
    config = load_config(config_dir=config_dir, load_env=False)
    assert isinstance(config, AppConfig)
    assert "mentor_novice" in config.teams
    assert config.teams["mentor_novice"].name == "Test Team"
    assert len(config.criteria) == 1
    assert config.criteria[0].name == "theory_of_impact"
    assert config.pipeline.model_assignments["generate"].model == "sonnet"
    assert config.kb_criteria.subfields_in_scope == ["mechanistic_interpretability"]


def test_load_config_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_config(config_dir=tmp_path, load_env=False)


def test_load_config_malformed_yaml(tmp_path):
    """Malformed YAML should raise an error."""
    # Create valid files for everything except teams
    valid_criteria = yaml.dump({"criteria": []})
    valid_pipeline = yaml.dump({"model_assignments": {}, "thresholds": {}})
    valid_kb = yaml.dump({"subfields_in_scope": []})

    (tmp_path / "criteria.yaml").write_text(valid_criteria)
    (tmp_path / "pipeline.yaml").write_text(valid_pipeline)
    (tmp_path / "kb-criteria.yaml").write_text(valid_kb)

    # Write invalid YAML for teams
    (tmp_path / "teams.yaml").write_text("teams:\n  - name: [invalid\n")

    with pytest.raises(Exception):
        load_config(config_dir=tmp_path, load_env=False)


def test_load_config_invalid_data(config_dir):
    """Invalid data should raise ValueError."""
    # Overwrite teams.yaml with invalid team_type
    bad_teams = {
        "teams": [
            {
                "name": "Bad Team",
                "team_type": "nonexistent_type",
            }
        ]
    }
    (config_dir / "teams.yaml").write_text(yaml.dump(bad_teams))

    with pytest.raises(ValueError, match="Invalid team profile"):
        load_config(config_dir=config_dir, load_env=False)


def test_load_default_config_files():
    """Integration test: load the actual default config files."""
    from safety_ideas.constants import CONFIG_DIR

    if not CONFIG_DIR.exists():
        pytest.skip("Default config directory not found")

    config = load_config(config_dir=CONFIG_DIR, load_env=False)
    assert len(config.teams) == 3
    assert "mentor_novice" in config.teams
    assert "solo_novice" in config.teams
    assert "experienced_group" in config.teams
    assert len(config.criteria) == 5
    assert len(config.kb_criteria.subfields_in_scope) > 0
