"""Tests for config loader."""

from pathlib import Path

import pytest
import yaml

from saim.config.loader import AppConfig, load_config


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
    from saim.constants import CONFIG_DIR

    if not CONFIG_DIR.exists():
        pytest.skip("Default config directory not found")

    config = load_config(config_dir=CONFIG_DIR, load_env=False)
    assert len(config.teams) == 4
    assert "baish_labs" in config.teams
    assert "mentor_novice" in config.teams
    assert "solo_novice" in config.teams
    assert "experienced_group" in config.teams
    assert len(config.criteria) == 7
    assert len(config.kb_criteria.subfields_in_scope) > 0


def test_impact_criteria_are_split_and_fully_rubricked():
    """theory_of_impact and impact_pathway are separate, each with a full 1-5 rubric."""
    from saim.constants import CONFIG_DIR

    if not CONFIG_DIR.exists():
        pytest.skip("Default config directory not found")

    config = load_config(config_dir=CONFIG_DIR, load_env=False)
    by_name = {c.name: c for c in config.criteria}

    for name in ("theory_of_impact", "impact_pathway"):
        assert name in by_name, f"{name} missing from criteria.yaml"
        rubric = by_name[name].rubric
        assert [level.score for level in rubric] == [1, 2, 3, 4, 5]
        assert all(level.description.strip() for level in rubric)


def test_impact_pair_counts_as_one_dimension_for_baish_labs():
    """BAISH Labs weights impact as one of three equal dimensions, so the pair sums to 1.0.

    Guards the design invariant in config/teams.yaml: novelty, the impact pair,
    and the feasibility cluster each total 1.0.
    """
    from saim.constants import CONFIG_DIR

    if not CONFIG_DIR.exists():
        pytest.skip("Default config directory not found")

    config = load_config(config_dir=CONFIG_DIR, load_env=False)
    weights = config.teams["baish_labs"].criteria_weights

    impact = weights["theory_of_impact"] + weights["impact_pathway"]
    feasibility = (
        weights["low_compute"] + weights["accessible_complexity"] + weights["narrow_scope"]
    )
    assert impact == pytest.approx(1.0)
    assert feasibility == pytest.approx(1.0)
    assert weights["novelty"] == pytest.approx(1.0)
