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


_LABEL_TO_CLASSIFICATION: dict[str, str] = {
    "already_solved": "already_solved",
    "largely_addressed": "largely_addressed",
    "partially_addressed": "partially_addressed",
    "mostly_novel": "mostly_novel",
    "novel": "novel",
    # Labels that appeared in old-format assessments
    "Already solved": "already_solved",
    "Largely addressed": "largely_addressed",
    "Partially addressed": "partially_addressed",
    "Mostly novel": "mostly_novel",
    "Novel": "novel",
}

# Default score assigned when no novelty information exists at all.
_DEFAULT_ESTIMATED_SCORE = 3
_DEFAULT_ESTIMATED_CLASSIFICATION = "partially_addressed"


def normalize_novelty_scores(idea: dict) -> dict:
    """Normalize novelty data on a scored idea dict, resolving duplicates.

    Handles four cases:

    1. **Proper assessment** — ``novelty_assessment`` has ``classification``
       (not ``"not_assessed"``) with ``evidence``.  Keep ``derived_score``,
       set ``scores.novelty`` to match, mark ``novelty_method = "novelty_assessed"``.

    2. **Old-format assessment** — ``novelty_assessment`` uses ``label``/``score``
       or ``novelty_label``/``novelty_score`` keys instead of the standard format.
       Convert to standard format, mark ``novelty_method = "novelty_estimated"``.

    3. **scores.novelty only** — ``novelty_assessment`` is missing or has
       ``classification = "not_assessed"`` but ``scores.novelty`` exists.
       Build a minimal assessment from it, mark ``novelty_method = "novelty_estimated"``.

    4. **No novelty at all** — Assign default score (3 / partially_addressed),
       mark ``novelty_method = "novelty_estimated"``.

    The function mutates *idea* in place and returns it.
    """
    scores = idea.setdefault("scores", {})
    na = idea.get("novelty_assessment") or {}

    # --- Detect which case we're in ---

    # Case 1: proper assessment
    classification = na.get("classification", "")
    has_proper = (
        classification
        and classification != "not_assessed"
        and classification in _CLASSIFICATION_SCORES
        and "evidence" in na
    )

    if has_proper:
        derived = na.get("derived_score") or novelty_to_score(classification)
        na["derived_score"] = derived
        scores["novelty"] = {
            "score": derived,
            "reasoning": na.get("reasoning", ""),
            "confidence": na.get("confidence", 0.0),
        }
        idea["novelty_assessment"] = na
        idea["novelty_method"] = "novelty_assessed"
        return idea

    # Case 2: old-format assessment (label/score or novelty_label/novelty_score)
    old_label = na.get("label") or na.get("novelty_label") or ""
    old_score = na.get("score") or na.get("novelty_score")

    if old_label or old_score:
        # Resolve classification from label
        resolved_cls = _LABEL_TO_CLASSIFICATION.get(old_label, "")
        if resolved_cls:
            resolved_score = novelty_to_score(resolved_cls)
        elif old_score and 1 <= old_score <= 5:
            # Reverse-map score to classification
            score_to_cls = {v: k for k, v in _CLASSIFICATION_SCORES.items()}
            resolved_cls = score_to_cls.get(old_score, _DEFAULT_ESTIMATED_CLASSIFICATION)
            resolved_score = old_score
        else:
            resolved_cls = _DEFAULT_ESTIMATED_CLASSIFICATION
            resolved_score = _DEFAULT_ESTIMATED_SCORE

        idea["novelty_assessment"] = {
            "classification": resolved_cls,
            "evidence": na.get("existing_work", na.get("key_existing_work", na.get("key_references", []))),
            "confidence": na.get("confidence", 0.0),
            "derived_score": resolved_score,
            "reasoning": na.get("reasoning", ""),
        }
        scores["novelty"] = {
            "score": resolved_score,
            "reasoning": na.get("reasoning", ""),
            "confidence": na.get("confidence", 0.0),
        }
        idea["novelty_method"] = "novelty_estimated"
        return idea

    # Case 3: only scores.novelty exists
    sn = scores.get("novelty")
    if sn and sn.get("score") is not None and sn["score"] > 0:
        score_val = sn["score"]
        score_to_cls = {v: k for k, v in _CLASSIFICATION_SCORES.items()}
        inferred_cls = score_to_cls.get(score_val, _DEFAULT_ESTIMATED_CLASSIFICATION)
        idea["novelty_assessment"] = {
            "classification": inferred_cls,
            "evidence": [],
            "confidence": sn.get("confidence", 0.0),
            "derived_score": score_val,
            "reasoning": sn.get("reasoning", ""),
        }
        idea["novelty_method"] = "novelty_estimated"
        return idea

    # Case 4: no novelty information at all
    idea["novelty_assessment"] = {
        "classification": _DEFAULT_ESTIMATED_CLASSIFICATION,
        "evidence": [],
        "confidence": 0.0,
        "derived_score": _DEFAULT_ESTIMATED_SCORE,
        "reasoning": "No novelty assessment available; default estimated score assigned.",
    }
    scores["novelty"] = {
        "score": _DEFAULT_ESTIMATED_SCORE,
        "reasoning": "No novelty assessment available; default estimated score assigned.",
        "confidence": 0.0,
    }
    idea["novelty_method"] = "novelty_estimated"
    return idea


def main() -> None:
    import json
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m saim.pipeline.novelty <command> [args]")
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
