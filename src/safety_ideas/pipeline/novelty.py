"""Novelty assessment helpers: score derivation and formatting.

Classification is produced by the LLM in the score-ideas skill after
reading all collected evidence.  This module only handles the mechanical
parts: validating classifications, mapping them to scores, and
structuring the assessment dict.
"""

from __future__ import annotations

# Valid novelty classifications ordered from least to most novel.
NOVELTY_CLASSIFICATIONS = [
    "already_solved",
    "largely_addressed",
    "partially_addressed",
    "mostly_novel",
    "novel",
]

# Mapping from classification string to integer score (1-5).
_CLASSIFICATION_SCORES: dict[str, int] = {
    "already_solved": 1,
    "largely_addressed": 2,
    "partially_addressed": 3,
    "mostly_novel": 4,
    "novel": 5,
}


def validate_classification(classification: str) -> str:
    """Validate that a classification string is one of the known values.

    Args:
        classification: Classification string to validate.

    Returns:
        The validated classification string (unchanged).

    Raises:
        ValueError: If the classification is not recognized.
    """
    if classification not in _CLASSIFICATION_SCORES:
        raise ValueError(
            f"Unknown novelty classification: {classification!r}. "
            f"Valid values: {NOVELTY_CLASSIFICATIONS}"
        )
    return classification


def novelty_to_score(classification: str) -> int:
    """Convert a novelty classification string to an integer score (1-5).

    Args:
        classification: One of the valid novelty classification strings.

    Returns:
        Integer score from 1 (already_solved) to 5 (novel).

    Raises:
        ValueError: If the classification is not recognized.
    """
    validate_classification(classification)
    return _CLASSIFICATION_SCORES[classification]


def format_novelty_assessment(
    classification: str,
    evidence: list[dict],
    confidence: float,
    reasoning: str = "",
) -> dict:
    """Format a novelty assessment dict for inclusion in a scored idea.

    Args:
        classification: Novelty classification string (produced by the LLM).
        evidence: List of evidence dicts collected during web search.
        confidence: Confidence in the assessment (0.0-1.0), set by the LLM.
        reasoning: LLM's explanation for the classification.

    Returns:
        Dict with classification, evidence, confidence, derived_score,
        and reasoning.
    """
    return {
        "classification": validate_classification(classification),
        "evidence": evidence,
        "confidence": confidence,
        "derived_score": novelty_to_score(classification),
        "reasoning": reasoning,
    }


def main() -> None:
    import json
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.pipeline.novelty <command> [args]")
        print("Commands:")
        print("  score <classification>       — convert classification to score")
        print("  validate <classification>    — check if classification is valid")
        print("  format <assessment_json>     — format a novelty assessment dict")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "score":
        classification = sys.argv[2]
        print(novelty_to_score(classification))
    elif cmd == "validate":
        classification = sys.argv[2]
        try:
            validate_classification(classification)
            print(json.dumps({"valid": True, "classification": classification}))
        except ValueError as e:
            print(json.dumps({"valid": False, "error": str(e)}))
    elif cmd == "format":
        data = json.loads(sys.argv[2])
        result = format_novelty_assessment(
            classification=data["classification"],
            evidence=data.get("evidence", []),
            confidence=data.get("confidence", 0.5),
            reasoning=data.get("reasoning", ""),
        )
        print(json.dumps(result))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
