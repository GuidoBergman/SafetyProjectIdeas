"""Project-wide constants for Safety Ideas."""

from pathlib import Path

# Project root (two levels up from this file: src/safety_ideas/ -> project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Directory paths
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
KB_DIR = DATA_DIR / "kb"
OUTPUT_DIR = DATA_DIR / "output"
RUNS_DIR = DATA_DIR / "runs"
IDEAS_DIR = DATA_DIR / "ideas"

# Config file paths
TEAMS_CONFIG = CONFIG_DIR / "teams.yaml"
CRITERIA_CONFIG = CONFIG_DIR / "criteria.yaml"
PIPELINE_CONFIG = CONFIG_DIR / "pipeline.yaml"
KB_CRITERIA_CONFIG = CONFIG_DIR / "kb-criteria.yaml"
PARTICIPANTS_DIR = CONFIG_DIR / "participants"

# Pipeline stage names
STAGE_NAMES = ["source", "generate", "filter_score", "refine", "rank"]

# Default priority levels
DEFAULT_PRIORITY = 2
PRIORITY_HIGH = 1
PRIORITY_MEDIUM = 2
PRIORITY_LOW = 3

# Team types
TEAM_TYPES = ["mentor_novice", "solo_novice", "experienced_group"]

# Scoring criteria names
SCORING_CRITERIA = [
    "soundness",
    "relevance",
    "theory_of_impact",
    "low_compute",
    "accessible_complexity",
]
