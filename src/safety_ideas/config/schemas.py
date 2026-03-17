"""Pydantic models for all configuration schemas."""

from typing import Literal

from pydantic import BaseModel, Field


TeamType = Literal["mentor_novice", "solo_novice", "experienced_group"]


class TeamProfile(BaseModel):
    """Profile for a BAISH team configuration."""

    name: str = Field(description="Team display name")
    team_type: TeamType = Field(description="Team type classification")
    compute_budget: str = Field(description="Available compute resources (e.g., 'low', 'medium', 'high')")
    technical_skills: list[str] = Field(default_factory=list, description="Technical skills available")
    criteria_weights: dict[str, float] = Field(
        default_factory=dict,
        description="Custom scoring criteria weight overrides for this team type",
    )


class ScoringCriteria(BaseModel):
    """A single scoring criterion for idea evaluation."""

    name: str = Field(description="Criterion identifier")
    description: str = Field(description="Human-readable description of the criterion")
    default_weight: float = Field(ge=0.0, le=10.0, description="Default weight for scoring")
    team_type_overrides: dict[str, float] = Field(
        default_factory=dict,
        description="Per-team-type weight overrides (team_type -> weight)",
    )


class KBCriteria(BaseModel):
    """Inclusion criteria for the knowledge base."""

    subfields_in_scope: list[str] = Field(
        default_factory=list, description="AI Safety subfields to include"
    )
    organizations: list[str] = Field(
        default_factory=list, description="Organizations whose work to prioritize"
    )
    authors: list[str] = Field(
        default_factory=list, description="Key authors to track"
    )
    exclusions: list[str] = Field(
        default_factory=list, description="Topics or sources to exclude"
    )


class StageModelAssignment(BaseModel):
    """Model assignment for a single pipeline stage."""

    model: str = Field(description="Model name/tier to use for this stage")
    fallback: str = Field(default="", description="Fallback model if primary unavailable")


class StageThreshold(BaseModel):
    """Threshold settings for a filter stage."""

    min_score: float = Field(ge=0.0, le=10.0, description="Minimum score to pass filter")
    max_ideas: int = Field(ge=1, description="Maximum ideas to pass through")


class PipelineSettings(BaseModel):
    """Pipeline configuration including model assignments and thresholds."""

    model_assignments: dict[str, StageModelAssignment] = Field(
        default_factory=dict,
        description="Model assignment per pipeline stage",
    )
    thresholds: dict[str, StageThreshold] = Field(
        default_factory=dict,
        description="Threshold settings per filter stage",
    )


class ParticipantProfile(BaseModel):
    """Profile for an external participant (FR66)."""

    name: str = Field(description="Participant name")
    experience_level: str = Field(description="e.g., 'beginner', 'intermediate', 'advanced'")
    technical_background: list[str] = Field(
        default_factory=list, description="Technical areas of expertise"
    )
    compute_resources: str = Field(
        default="low", description="Available compute (e.g., 'low', 'medium', 'high')"
    )
    time_availability: str = Field(
        default="part_time", description="Time commitment (e.g., 'full_time', 'part_time', 'minimal')"
    )
