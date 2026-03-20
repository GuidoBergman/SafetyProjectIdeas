"""Pydantic models for all configuration schemas."""

from typing import Literal

from pydantic import BaseModel, Field


TeamType = Literal["mentor_novice", "solo_novice", "experienced_group"]

DEFAULT_TEAM: TeamType = "mentor_novice"


class TeamProfile(BaseModel):
    """Profile for a BAISH team configuration."""

    name: str = Field(description="Team display name")
    team_type: TeamType = Field(description="Team type classification")
    technical_skills: list[str] = Field(
        default_factory=list, description="Technical skills available"
    )
    criteria_weights: dict[str, float] = Field(
        default_factory=dict,
        description="Custom scoring criteria weight overrides for this team type",
    )


class RubricLevel(BaseModel):
    """A single level in a scoring rubric."""

    score: int = Field(ge=1, le=5, description="Numeric score for this level")
    label: str = Field(description="Short label (e.g., 'Weak', 'Strong')")
    description: str = Field(description="What this score level means for this criterion")


class ScoringCriteria(BaseModel):
    """A single scoring criterion for idea evaluation."""

    name: str = Field(description="Criterion identifier")
    description: str = Field(description="Human-readable description of the criterion")
    default_weight: float = Field(ge=0.0, le=5.0, description="Default weight for scoring")
    rubric: list[RubricLevel] = Field(
        default_factory=list,
        description="Ordered rubric levels defining what each score means for this criterion",
    )


class KBCriteria(BaseModel):
    """Inclusion criteria for the knowledge base."""

    subfields_in_scope: list[str] = Field(
        default_factory=list, description="AI Safety subfields to include"
    )
    organizations: list[str] = Field(
        default_factory=list, description="Organizations whose work to prioritize"
    )
    authors: list[str] = Field(default_factory=list, description="Key authors to track")
    exclusions: list[str] = Field(default_factory=list, description="Topics or sources to exclude")


class StageModelAssignment(BaseModel):
    """Model assignment for a single pipeline stage."""

    model: str = Field(description="Model name/tier to use for this stage")
    fallback: str = Field(default="", description="Fallback model if primary unavailable")


class StageThreshold(BaseModel):
    """Threshold settings for a filter stage."""

    min_score: float = Field(ge=0.0, le=5.0, description="Minimum score to pass filter")
    max_ideas: int = Field(ge=1, description="Maximum ideas to pass through")


class QuickFilterConfig(BaseModel):
    """Configuration for the Stage 1 quick relevance filter."""

    threshold: float = Field(
        default=2.0,
        ge=0.0,
        le=5.0,
        description="Minimum score to pass the quick relevance filter",
    )
    rubric: list[RubricLevel] = Field(
        default_factory=list,
        description="Rubric levels defining what each quick-filter score means",
    )


class ConfidenceRubricLevel(BaseModel):
    """A single level in the confidence rubric."""

    min: float = Field(
        ge=0.0, le=1.0, description="Lower bound of this confidence band (inclusive)"
    )
    max: float = Field(
        ge=0.0, le=1.0, description="Upper bound of this confidence band (inclusive)"
    )
    label: str = Field(description="Short label (e.g., 'High', 'Very low')")
    description: str = Field(description="What this confidence range means")


class CitationRelevanceConfig(BaseModel):
    """Configuration for citation relevance scoring in Phase 3b."""

    threshold: int = Field(
        default=3,
        ge=1,
        le=5,
        description="Minimum relevance score for a citation to be verified. "
        "Citations below this threshold are kept as-is without verification.",
    )
    rubric: list[RubricLevel] = Field(
        default_factory=list,
        description="Rubric levels defining citation relevance to the idea",
    )


class BatchSizeConfig(BaseModel):
    """Batch sizes for parallel scoring subagents."""

    stage1_quick_filter: int = Field(
        default=100,
        ge=1,
        description="Ideas per subagent in Stage 1 quick filter",
    )
    stage2_full_scoring: int = Field(
        default=30,
        ge=1,
        description="Ideas per subagent in Stage 2 full scoring",
    )
    stage3_novelty_citations: int = Field(
        default=15,
        ge=1,
        description="Ideas per subagent in Stage 3 novelty + citations",
    )


class GenerateSettings(BaseModel):
    """Settings for the idea generation stage."""

    min_ideas_per_strategy_per_subfield: int = Field(
        default=25,
        ge=1,
        description="Minimum number of ideas to generate per strategy per subfield",
    )
    combinatorial_top_n: int = Field(
        default=10,
        ge=1,
        description="Number of top problems/methods for the combinatorial matrix pass",
    )


class PipelineSettings(BaseModel):
    """Pipeline configuration including model assignments and thresholds."""

    model_assignments: dict[str, StageModelAssignment] = Field(
        default_factory=dict,
        description="Model assignment per pipeline stage",
    )
    generate: GenerateSettings = Field(
        default_factory=GenerateSettings,
        description="Settings for the idea generation stage",
    )
    batch_sizes: BatchSizeConfig = Field(
        default_factory=BatchSizeConfig,
        description="Batch sizes for parallel scoring subagents",
    )
    quick_filter: QuickFilterConfig = Field(
        default_factory=QuickFilterConfig,
        description="Stage 1 quick relevance filter configuration",
    )
    confidence_rubric: list[ConfidenceRubricLevel] = Field(
        default_factory=list,
        description="Rubric defining what each confidence score range (0.0-1.0) means",
    )
    citation_relevance: CitationRelevanceConfig = Field(
        default_factory=CitationRelevanceConfig,
        description="Citation relevance scoring configuration for Phase 3b",
    )
    thresholds: dict[str, StageThreshold] = Field(
        default_factory=dict,
        description="Threshold settings per filter stage",
    )


class ParticipantProfile(BaseModel):
    """Profile for an external participant (FR66).

    Fields are mostly free-text strings so that rich context is preserved
    when injected into LLM prompts.  Only ``total_hours`` is typed for
    machine-readable constraints.
    """

    name: str = Field(description="Participant name or role identifier")
    background: str = Field(
        description="Who this person is: education, role, domain experience. "
        "E.g., 'CS undergrad, first AI safety research experience'",
    )
    technical_skills: str = Field(
        description="Technical skills and proficiency levels. "
        "E.g., 'Beginner Python, basic ML/stats, no prior interpretability work'",
    )
    compute_resources: str = Field(
        default="low",
        description="Available compute and what that means concretely. "
        "E.g., 'Medium — access to Colab Pro with T4/A100 GPUs'",
    )
    total_hours: int | None = Field(
        default=None,
        description="Hard cap on total hours for the entire project, if applicable",
    )
    time_context: str = Field(
        default="",
        description="What the time budget must cover. "
        "E.g., '30 hours total including implementation, analysis, and writing a blog post'",
    )
    deliverables: str = Field(
        default="",
        description="What the participant must produce. "
        "E.g., 'Working experiment + well-written blog post communicating findings'",
    )
    goals: str = Field(
        default="",
        description="What the participant hopes to get out of this. "
        "E.g., 'First hands-on AI safety research experience, publishable output'",
    )
