"""Tests for participant profile loading and auto-detection."""

import pytest
import yaml

from safety_ideas.config.participants import (
    get_participant_or_none,
    list_participants,
    load_participant,
)
from safety_ideas.config.schemas import ParticipantProfile


@pytest.fixture
def participants_dir(tmp_path):
    """Create a temporary participants directory with sample profiles."""
    alice_data = {
        "name": "Alice",
        "experience_level": "beginner",
        "technical_background": ["python"],
        "compute_resources": "low",
        "time_availability": "part_time",
    }
    bob_data = {
        "name": "Bob",
        "experience_level": "advanced",
        "technical_background": ["python_advanced", "ml_advanced"],
        "compute_resources": "high",
        "time_availability": "full_time",
    }
    (tmp_path / "alice.yaml").write_text(yaml.dump(alice_data))
    (tmp_path / "bob.yaml").write_text(yaml.dump(bob_data))
    return tmp_path


class TestLoadParticipant:
    def test_load_existing_profile(self, participants_dir):
        profile = load_participant("alice", participants_dir)
        assert profile is not None
        assert profile.name == "Alice"
        assert profile.experience_level == "beginner"
        assert "python" in profile.technical_background

    def test_load_nonexistent_profile(self, participants_dir):
        profile = load_participant("charlie", participants_dir)
        assert profile is None

    def test_case_insensitive_lookup(self, participants_dir):
        profile = load_participant("Alice", participants_dir)
        assert profile is not None
        assert profile.name == "Alice"

    def test_invalid_profile_raises(self, tmp_path):
        """Invalid YAML content should raise ValueError."""
        bad_data = {"name": "Bad"}  # missing experience_level
        (tmp_path / "bad.yaml").write_text(yaml.dump(bad_data))
        with pytest.raises(ValueError, match="Invalid participant profile"):
            load_participant("bad", tmp_path)


class TestListParticipants:
    def test_list_all(self, participants_dir):
        profiles = list_participants(participants_dir)
        assert len(profiles) == 2
        names = {p.name for p in profiles}
        assert names == {"Alice", "Bob"}

    def test_empty_directory(self, tmp_path):
        profiles = list_participants(tmp_path)
        assert profiles == []

    def test_nonexistent_directory(self, tmp_path):
        profiles = list_participants(tmp_path / "nonexistent")
        assert profiles == []

    def test_skips_invalid_files(self, tmp_path):
        """Invalid profiles are skipped, valid ones loaded."""
        good = {"name": "Good", "experience_level": "beginner"}
        bad = {"name": "Bad"}  # missing required field
        (tmp_path / "good.yaml").write_text(yaml.dump(good))
        (tmp_path / "bad.yaml").write_text(yaml.dump(bad))

        profiles = list_participants(tmp_path)
        assert len(profiles) == 1
        assert profiles[0].name == "Good"


class TestGetParticipantOrNone:
    def test_existing_profile(self, participants_dir):
        """AC3: auto-load when profile exists."""
        profile = get_participant_or_none("alice", participants_dir)
        assert profile is not None
        assert isinstance(profile, ParticipantProfile)

    def test_missing_profile(self, participants_dir):
        """AC4: return None for conversational fallback."""
        profile = get_participant_or_none("charlie", participants_dir)
        assert profile is None

    def test_invalid_profile_returns_none(self, tmp_path):
        """Invalid profiles return None (graceful degradation)."""
        bad = {"name": "Bad"}
        (tmp_path / "bad.yaml").write_text(yaml.dump(bad))
        profile = get_participant_or_none("bad", tmp_path)
        assert profile is None


class TestLoadDefaultParticipant:
    def test_load_guido_profile(self):
        """Integration test: load the sample guido.yaml profile."""
        from safety_ideas.constants import PARTICIPANTS_DIR

        if not (PARTICIPANTS_DIR / "guido.yaml").exists():
            pytest.skip("guido.yaml not found")

        profile = load_participant("guido")
        assert profile is not None
        assert profile.name == "Guido"
        assert profile.experience_level == "advanced"
        assert "python_advanced" in profile.technical_background
