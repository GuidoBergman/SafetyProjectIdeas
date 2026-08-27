"""Tests for idea ID generation."""

import subprocess
import sys

from saim.ids import IDEA_ID_HEX_LEN, IDEA_ID_PREFIX, is_idea_id, new_idea_id


def test_new_idea_id_format():
    idea_id = new_idea_id()

    assert idea_id.startswith(IDEA_ID_PREFIX)
    suffix = idea_id[len(IDEA_ID_PREFIX) :]
    assert len(suffix) == IDEA_ID_HEX_LEN
    assert all(c in "0123456789abcdef" for c in suffix)


def test_new_idea_id_is_unique_across_calls():
    ids = {new_idea_id() for _ in range(1000)}

    assert len(ids) == 1000


def test_is_idea_id_accepts_generated_ids():
    assert is_idea_id(new_idea_id())


def test_is_idea_id_rejects_legacy_and_invalid_values():
    assert not is_idea_id("gen-001")
    assert not is_idea_id("gen-0017")
    assert not is_idea_id("gen-3F9A1C04")  # uppercase hex
    assert not is_idea_id("3f9a1c04")
    assert not is_idea_id("")
    assert not is_idea_id(None)


def test_cli_prints_requested_number_of_ids():
    result = subprocess.run(
        [sys.executable, "-m", "saim.ids", "3"],
        capture_output=True,
        text=True,
        check=True,
    )

    lines = result.stdout.split()
    assert len(lines) == 3
    assert all(is_idea_id(line) for line in lines)
    assert len(set(lines)) == 3


def test_cli_defaults_to_one_id():
    result = subprocess.run(
        [sys.executable, "-m", "saim.ids"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert is_idea_id(result.stdout.strip())


def test_cli_rejects_non_positive_count():
    result = subprocess.run(
        [sys.executable, "-m", "saim.ids", "0"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
