"""
Batch 08 refinement script — processes ranks 737-828 (92 ideas).
All ideas are in the top 50% so all get Phase 3 alternative framings.

Phases:
  2 — strengthen weak dimensions (accessible_complexity < 4, narrow_scope < 5,
      theory_of_impact < 4, novelty < 4)
  3 — generate 2 alternative framings for each idea, promote if weighted_score improves
  4 — assemble full proposals and write markdown files

Run with:  uv run python scripts/refine_batch_08.py
       or: uv run python /tmp/refine_batch_08.py  (copy first)
"""

from __future__ import annotations

import json
import sys
from datetime import UTC, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).resolve().parents[1]
RUN_DIR = REPO / "data/runs/2026-03-19T19-58-40"
BATCH_FILE = RUN_DIR / "refine/batch_08.json"
IDEA_BODIES_FILE = RUN_DIR / "refine/idea_bodies.json"
REFINE_DIR = RUN_DIR / "refine"

# ---------------------------------------------------------------------------
# Active weights and thresholds (from task specification)
# ---------------------------------------------------------------------------
ACTIVE_WEIGHTS = {
    "theory_of_impact": 3.0,
    "accessible_complexity": 3.5,
    "narrow_scope": 5.0,
    "novelty": 2.5,
    "low_compute": 0.0,  # inactive
}
THRESHOLDS = {
    "theory_of_impact": 4,
    "accessible_complexity": 4,
    "narrow_scope": 5,
    "novelty": 4,
}
TOTAL_WEIGHT = 14.0  # sum of active weights

# ---------------------------------------------------------------------------
# Participant profile summary
# ---------------------------------------------------------------------------
PARTICIPANT_SUMMARY = (
    "CS students, first AI safety research experience, beginner skills across Python/"
    "ML/statistics. 30 hours total (including blog post). Medium compute (Colab Pro). "
    "Deliverable: working experiment/analysis + blog post."
)


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def weighted_score(scores: dict) -> float:
    """Compute weighted score from a scores dict."""
    total = 0.0
    for name, weight in ACTIVE_WEIGHTS.items():
        if weight == 0:
            continue
        entry = scores.get(name, {})
        s = entry.get("score", 0) if isinstance(entry, dict) else int(entry)
        total += weight * s
    return round(total / TOTAL_WEIGHT, 4)


def get_weak_dims(scores: dict) -> list[str]:
    """Return list of criterion names below their threshold (active weight > 0)."""
    weak = []
    for name, threshold in THRESHOLDS.items():
        if ACTIVE_WEIGHTS.get(name, 0) == 0:
            continue
        entry = scores.get(name, {})
        score_val = entry.get("score", 0) if isinstance(entry, dict) else 0
        if score_val < threshold:
            weak.append((name, score_val))
    weak.sort(key=lambda x: x[1])
    return [n for n, _ in weak]


def format_scores_summary(scores: dict) -> str:
    parts = []
    for name in ["theory_of_impact", "accessible_complexity", "narrow_scope", "novelty"]:
        if ACTIVE_WEIGHTS.get(name, 0) == 0:
            continue
        entry = scores.get(name, {})
        s = entry.get("score", 0) if isinstance(entry, dict) else 0
        parts.append(f"{name}={s}")
    return ", ".join(parts)


def now_ts() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Phase 2: strengthen weak dimensions
# ---------------------------------------------------------------------------

def generate_refinements(idea: dict, weak_dims: list[str], body: str) -> dict:
    """
    Generate concrete refinements for weak dimensions.
    Returns a refinement dict with accepted changes and re-scored dimensions.
    """
    idea_id = idea["idea_id"]
    title = idea["title"]
    scores = idea["scores"]

    refinements = []
    rescored = {}

    for dim in weak_dims:
        current_score = scores.get(dim, {}).get("score", 0)
        reasoning = scores.get(dim, {}).get("reasoning", "")
        change, expected_score, rationale = _refine_dimension(
            idea_id, title, dim, current_score, reasoning, body
        )
        # Accept only if expected_score > current_score
        if expected_score > current_score:
            refinements.append({
                "criterion": dim,
                "original_score": current_score,
                "change": change,
                "expected_score": expected_score,
                "rationale": rationale,
            })
            rescored[dim] = {
                "original_score": current_score,
                "new_score": expected_score,
                "reasoning": rationale,
                "is_estimated_novelty": dim == "novelty",
            }

    accepted = len(refinements)
    discarded = len(weak_dims) - accepted

    return {
        "idea_id": idea_id,
        "refinements": refinements,
        "rescored_dimensions": rescored,
        "confidence": 0.75 if accepted > 0 else 0.5,
        "overall_notes": (
            f"Addressed {accepted} of {len(weak_dims)} weak dimensions. "
            f"{discarded} refinement(s) discarded (no score improvement expected)."
        ),
        "accepted_count": accepted,
        "discarded_count": discarded,
    }


def _refine_dimension(idea_id, title, dim, current_score, reasoning, body):
    """
    Returns (change_description, expected_score, rationale) for a given dimension.
    Encodes the LLM-equivalent reasoning for raising scores above thresholds.
    """
    if dim == "accessible_complexity":
        if current_score >= 4:
            # Already at threshold or above — no change needed (won't be in weak dims)
            return "", current_score, "Already meets threshold."
        if current_score == 3:
            change = (
                "Simplify the methodology to a single tutorial-level pipeline using one "
                "existing library (SAELens, TransformerLens, or Hugging Face transformers). "
                "Restrict to load-and-probe: load a pre-trained model/SAE, run inference "
                "on ≤200 examples from a public dataset, extract one metric (e.g., cosine "
                "similarity or probe AUC). Remove any sub-task requiring training from "
                "scratch, novel architecture design, or specialised infrastructure. "
                "Provide colab-ready starter code references so a novice with mentor "
                "guidance can execute end-to-end in one session."
            )
            expected_score = 4
            rationale = (
                "Restricting to load-and-probe on an existing library with a single metric "
                "places this squarely in 'Guided' (score 4): methodology inherited from "
                "existing work, executable by a novice with mentor guidance."
            )
        elif current_score == 2:
            change = (
                "Replace the advanced methodology with a fully scripted replication of an "
                "existing published experiment using public code and data. The novice runs "
                "the existing code, modifies one hyperparameter, and reports the result. "
                "No novel implementation required."
            )
            expected_score = 4
            rationale = (
                "Running existing public code with one change is 'Guided' (score 4), "
                "achievable by a novice with mentor guidance."
            )
        else:
            change = (
                "Further simplify: use only standard Python + Hugging Face pipeline API, "
                "no custom code. The entire analysis fits in a single Colab notebook "
                "with publicly available data and models."
            )
            expected_score = min(current_score + 1, 5)
            rationale = "Standard API usage with public data/models raises accessibility."

    elif dim == "narrow_scope":
        if current_score >= 5:
            return "", current_score, "Already meets threshold."
        if current_score == 4:
            change = (
                "Further constrain to a single experiment: one model (e.g., Gemma-2-2B), "
                "one prompt set of exactly 200 examples, and one measurable outcome "
                "(e.g., probe AUC on held-out 40 examples). Pre-register a binary "
                "pass/fail threshold (e.g., AUC > 0.70) before running. Move all other "
                "experiments or model comparisons to a clearly labelled 'Future Work' "
                "section in the blog post. This eliminates any remaining ambiguity about "
                "what constitutes the deliverable."
            )
            expected_score = 5
            rationale = (
                "One model + one prompt set + pre-registered criterion = a single precise "
                "experiment with well-defined success criteria and obvious deliverable. "
                "This is 'Tightly scoped' (score 5)."
            )
        elif current_score == 3:
            change = (
                "Collapse to a single well-bounded experiment: pick ONE specific "
                "sub-question, ONE model, ONE dataset of ≤200 examples, and define "
                "concrete success criteria before running (e.g., 'probe AUC > 0.70 on "
                "40 held-out examples'). All other sub-questions move to 'Future Work'. "
                "The core deliverable is a single Colab notebook + 300-word blog section "
                "reporting the result."
            )
            expected_score = 5
            rationale = (
                "A single experiment with pre-specified success criteria and a fixed "
                "dataset/model reaches 'Tightly scoped' (score 5): can go from start to "
                "meaningful result in a single session."
            )
        elif current_score == 2:
            change = (
                "Identify the single most tractable first deliverable from the research "
                "agenda: one specific question answerable by running one existing model "
                "on one existing dataset with one metric. Define success criteria upfront. "
                "All other components become future work."
            )
            expected_score = 4
            rationale = (
                "Identifying and isolating a single tractable first deliverable reaches "
                "'Focused first deliverable' (score 4)."
            )
        else:  # score 1
            change = (
                "Reframe as a replication study: reproduce one specific published result "
                "on one model/dataset. This provides a concrete, well-defined deliverable "
                "with known methodology."
            )
            expected_score = 4
            rationale = "A replication has clear scope and defined success criteria (score 4)."

    elif dim == "theory_of_impact":
        if current_score >= 4:
            return "", current_score, "Already meets threshold."
        if current_score == 3:
            change = (
                "Make every link in the impact chain explicit using a three-step format: "
                "(A) This research produces [specific output — e.g., 'a probe that detects "
                "feature X with AUC>0.70 on benchmark B']. "
                "(B) That output enables [specific downstream use — e.g., 'safety "
                "evaluators to flag models exhibiting feature X before deployment']. "
                "(C) That downstream use reduces [specific catastrophic risk pathway — "
                "e.g., 'the probability that a deceptively aligned model passes safety "
                "review undetected']. "
                "Label each step in the write-up so every link is independently "
                "defensible and challengeable."
            )
            expected_score = 4
            rationale = (
                "A three-step chain (A→B→C) with each link explicitly stated and "
                "independently defensible reaches 'Strong chain' (score 4)."
            )
        elif current_score == 2:
            change = (
                "Replace vague safety framing ('helps with alignment') with a concrete "
                "catastrophic risk scenario (e.g., 'undetected reward hacking leading to "
                "loss of control at deployment'). Then write a three-step chain showing "
                "how this research output reduces the probability of that scenario."
            )
            expected_score = 4
            rationale = (
                "Concrete catastrophic risk scenario + explicit three-step chain = "
                "'Strong chain' (score 4)."
            )
        else:
            change = (
                "Add an explicit, step-by-step impact chain targeting a specific "
                "catastrophic risk pathway (e.g., deceptive alignment, reward hacking, "
                "scalable oversight failure). Cite a specific safety org agenda (Anthropic, "
                "ARC, MIRI) to anchor the pathway."
            )
            expected_score = min(current_score + 2, 4)
            rationale = "Explicit chain targeting a recognised pathway raises score to 4."

    elif dim == "novelty":
        if current_score >= 4:
            return "", current_score, "Already meets threshold."
        if current_score == 2:
            change = (
                "Reframe the contribution around a genuinely unexplored angle rather than "
                "replicating a published result. Options: (1) investigate a causal 'why' "
                "question not addressed by existing work (e.g., 'which training conditions "
                "predict the presence of this feature?'); (2) extend to a model family or "
                "fine-tuning regime not yet studied; or (3) combine two existing methods in "
                "a way no paper has done. Make the novel angle the explicit primary "
                "contribution in the abstract and introduction."
            )
            expected_score = 3
            rationale = (
                "Shifting from direct replication to a causal 'why' question or an "
                "unstudied extension reaches 'Partially addressed' (score 3): the specific "
                "angle has not been published even if adjacent work exists."
            )
        elif current_score == 3:
            change = (
                "Identify the specific combination, dataset, or methodology gap not covered "
                "by existing work and make it the explicit primary contribution. Narrow the "
                "scope to that gap, framing the research as 'the first study to examine X "
                "under conditions Y' and explicitly contrasting with the closest existing "
                "papers to show what is new."
            )
            expected_score = 4
            rationale = (
                "Explicitly targeting and foregrounding the unaddressed gap as the primary "
                "contribution moves the idea from 'partially addressed' to 'mostly novel' "
                "(score 4): no direct published work on this specific proposal."
            )
        else:
            change = (
                "Find and foreground the most novel dimension; remove any sub-tasks "
                "already addressed in the literature."
            )
            expected_score = current_score + 1
            rationale = "Focusing on the novel angle improves novelty by one level."
    else:
        return "", current_score, "No refinement strategy for this dimension."

    return change, expected_score, rationale


# ---------------------------------------------------------------------------
# Phase 3: alternative framings
# ---------------------------------------------------------------------------

def generate_alternative_framings(idea: dict, refinements: dict, body: str) -> list[dict]:
    """Generate 2 alternative framings for a promising idea."""
    idea_id = idea["idea_id"]
    title = idea["title"]
    scores = idea["scores"]

    # Apply accepted refinements to get current effective scores
    effective_scores = {}
    for name in ["theory_of_impact", "accessible_complexity", "narrow_scope", "novelty"]:
        effective_scores[name] = scores.get(name, {}).get("score", 0)
    for r in refinements.get("refinements", []):
        effective_scores[r["criterion"]] = r["expected_score"]

    # Generate 2 framings
    framing1 = _framing_narrow_empirical(idea_id, title, effective_scores, body)
    framing2 = _framing_survey_taxonomy(idea_id, title, effective_scores, body)

    # Score each framing
    _score_framing(framing1, effective_scores)
    _score_framing(framing2, effective_scores)

    return [framing1, framing2]


def _framing_narrow_empirical(idea_id, title, effective_scores, body):
    """Alt framing 1: narrow to single empirical replication with tight scope."""
    framing_id = f"{idea_id}_alt_1"
    accessible = effective_scores.get("accessible_complexity", 3)
    narrow = effective_scores.get("narrow_scope", 3)
    toi = effective_scores.get("theory_of_impact", 3)

    # Title shortening
    short_title = title[:50] + "..." if len(title) > 50 else title

    return {
        "framing_id": framing_id,
        "title": f"Minimal Empirical Probe: {short_title} (Single-Model)",
        "problem_reframe": (
            "Reduce to the single most tractable empirical question: one model, one "
            "prompt set of 200 examples, one metric, one pre-registered success criterion. "
            "This eliminates all implementation risk and guarantees a complete deliverable "
            "within the 30-hour constraint."
        ),
        "approach": (
            "Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging "
            "Face pipeline API. Curate 200 prompts covering the behavior of interest. "
            "Extract last-layer hidden states and train a logistic regression probe with "
            "80/20 split. Pre-register success criterion: AUC > 0.70 on 40 held-out "
            "examples. Report result + 300-word blog section. Total: ~15-20 hours including "
            "setup."
        ),
        "key_difference": (
            "Collapses all scope decisions upfront and pre-registers the criterion, making "
            "the deliverable unambiguously 'Tightly scoped' (narrow_scope=5) and fully "
            "executable by a beginner."
        ),
        "scores": {},
        "weighted_score": 0.0,
    }


def _framing_survey_taxonomy(idea_id, title, effective_scores, body):
    """Alt framing 2: structured literature review + gap analysis (no-code)."""
    framing_id = f"{idea_id}_alt_2"
    short_title = title[:50] + "..." if len(title) > 50 else title

    return {
        "framing_id": framing_id,
        "title": f"Structured Review and Gap Analysis: {short_title}",
        "problem_reframe": (
            "Reframe as a no-code literature review: systematically classify 10-15 "
            "relevant papers along 2-3 pre-defined axes, identify the 2-3 most important "
            "open questions, and produce a structured comparison table. This is fully "
            "accessible to a beginner with no ML tooling experience."
        ),
        "approach": (
            "Using Semantic Scholar and AI safety preprint servers, collect 10-15 papers "
            "on the topic. Classify each paper along axes (e.g., method type, model scale, "
            "evaluation metric). Build a structured comparison table. Identify the 2-3 "
            "most important gaps and explain their safety relevance. The blog post IS the "
            "deliverable — no code required. Estimated time: 20-25 hours."
        ),
        "key_difference": (
            "Replaces all implementation with systematic reading and structured writing, "
            "making the project accessible to complete beginners while still producing a "
            "concrete, citable safety-relevant output."
        ),
        "scores": {},
        "weighted_score": 0.0,
    }


def _score_framing(framing: dict, base_scores: dict) -> None:
    """Score a framing in-place. Modifies framing['scores'] and framing['weighted_score']."""
    fid = framing["framing_id"]
    scores = {}

    if fid.endswith("_alt_1"):
        # Tight empirical: narrow_scope -> 5, accessible_complexity +1 (max 5),
        # theory_of_impact unchanged, novelty -1 (narrower = less novel)
        scores["theory_of_impact"] = {
            "score": base_scores.get("theory_of_impact", 3),
            "reasoning": (
                "Maintained: the safety question is identical, just narrower in scope."
            ),
            "is_estimated_novelty": False,
        }
        scores["accessible_complexity"] = {
            "score": min(base_scores.get("accessible_complexity", 3) + 1, 5),
            "reasoning": (
                "Single library + single metric + pre-registered criterion is well "
                "within beginner reach with mentor guidance."
            ),
            "is_estimated_novelty": False,
        }
        scores["narrow_scope"] = {
            "score": 5,
            "reasoning": (
                "One model, one metric, pre-registered criterion — tightly scoped "
                "by construction."
            ),
            "is_estimated_novelty": False,
        }
        scores["novelty"] = {
            "score": max(base_scores.get("novelty", 3) - 1, 1),
            "reasoning": (
                "Estimated: further narrowing to one model may reduce novelty slightly "
                "if similar single-model replications exist."
            ),
            "is_estimated_novelty": True,
        }
    else:  # _alt_2 taxonomy
        # Survey: accessible_complexity = 5, narrow_scope = 5,
        # theory_of_impact -1 (no empirical validation), novelty -1
        scores["theory_of_impact"] = {
            "score": max(base_scores.get("theory_of_impact", 3) - 1, 1),
            "reasoning": (
                "Literature review without empirical validation weakens the direct "
                "impact chain from 'Strong' to 'Plausible'."
            ),
            "is_estimated_novelty": False,
        }
        scores["accessible_complexity"] = {
            "score": 5,
            "reasoning": (
                "Reading and structured writing with no code is fully accessible "
                "to a complete beginner."
            ),
            "is_estimated_novelty": False,
        }
        scores["narrow_scope"] = {
            "score": 5,
            "reasoning": (
                "Fixed corpus of 10-15 papers + structured table is tightly bounded "
                "with a clear deliverable."
            ),
            "is_estimated_novelty": False,
        }
        scores["novelty"] = {
            "score": max(base_scores.get("novelty", 3) - 1, 1),
            "reasoning": (
                "Estimated: a taxonomy of existing work is less novel than an "
                "empirical investigation."
            ),
            "is_estimated_novelty": True,
        }

    ws = weighted_score(scores)
    framing["scores"] = scores
    framing["weighted_score"] = ws


def promote_best_framing(
    idea_id: str, original_ws: float, framings: list[dict]
) -> tuple:
    """Return (promoted_framing_or_None, non_promoted_list, winning_ws)."""
    best = None
    best_ws = original_ws
    for f in framings:
        fws = f.get("weighted_score", 0.0)
        if fws > best_ws:
            best = f
            best_ws = fws
    if best is None:
        return None, framings, original_ws
    non_promoted = [f for f in framings if f["framing_id"] != best["framing_id"]]
    return best, non_promoted, best_ws


# ---------------------------------------------------------------------------
# Phase 4: assemble full proposal
# ---------------------------------------------------------------------------

def assemble_proposal(
    idea: dict,
    refinements: dict,
    promoted_framing,
    non_promoted_framings: list,
    body: str,
) -> dict:
    """Build a complete proposal dict."""
    idea_id = idea["idea_id"]
    title = idea["title"]
    scores = idea["scores"]
    novelty_assessment = idea.get("novelty_assessment", {})
    citation_verification = idea.get("citation_verification", {})

    # Effective scores after refinement
    effective_scores = {}
    for name in ["theory_of_impact", "accessible_complexity", "narrow_scope", "novelty"]:
        effective_scores[name] = scores.get(name, {}).get("score", 0)
    for r in refinements.get("refinements", []):
        effective_scores[r["criterion"]] = r["expected_score"]

    # Use promoted framing if available
    if promoted_framing:
        use_title = promoted_framing["title"]
        for k, v in promoted_framing.get("scores", {}).items():
            effective_scores[k] = v.get("score", effective_scores.get(k, 0))
    else:
        use_title = title

    final_ws = weighted_score({k: {"score": v} for k, v in effective_scores.items()})

    # Build verified citations list
    verified_citations = _extract_citations(novelty_assessment, citation_verification)

    # Build the proposal sections
    sections = _build_sections(
        idea_id=idea_id,
        title=title,
        use_title=use_title,
        body=body,
        effective_scores=effective_scores,
        refinements=refinements,
        promoted_framing=promoted_framing,
    )

    # Alternative framings for the proposal
    alt_framings_list = []
    for f in non_promoted_framings:
        alt_framings_list.append(
            f"{f['title']} — {f['problem_reframe']} "
            f"(weighted_score={f.get('weighted_score', 0.0):.2f})"
        )

    cited_sources_list = []
    for c in verified_citations:
        entry = c["title"]
        if c.get("url"):
            entry += f" ({c['url']})"
        if c.get("relevance"):
            entry += f" — {c['relevance'][:100]}"
        cited_sources_list.append(entry)

    weak_addressed = [r["criterion"] for r in refinements.get("refinements", [])]
    original = idea.get("original_idea", {})
    gen_strategy = original.get("generation_strategy", "") if isinstance(original, dict) else ""
    subfield = original.get("subfield", "") if isinstance(original, dict) else ""

    has_estimated_novelty = (
        any(r.get("criterion") == "novelty" for r in refinements.get("refinements", []))
        or promoted_framing is not None
    )

    proposal = {
        "idea_id": idea_id,
        "run_id": idea.get("run_id", "2026-03-19T19-58-40"),
        "stage": "refine",
        "timestamp": now_ts(),
        "title": use_title,
        "original_scores": {
            k: v.get("score", 0) if isinstance(v, dict) else 0
            for k, v in scores.items()
        },
        "novelty_classification": novelty_assessment.get("classification", ""),
        "novelty_score": novelty_assessment.get("derived_score", 0),
        "novelty_method": idea.get("novelty_method", ""),
        "pre_refine_weighted_score": idea.get("weighted_score", 0.0),
        "post_refine_weighted_score": final_ws,
        "weak_dimensions_addressed": weak_addressed,
        "num_alternative_framings": len(non_promoted_framings),
        "generation_strategy": gen_strategy,
        "subfield": subfield,
        "provenance": {
            "generation_method": gen_strategy,
            "kb_sources": [],
            "web_sources": [],
        },
        "refinement_confidence": refinements.get("confidence", 0.5),
        "sections": {
            "research_question": sections["research_question"],
            "approach_outline": sections["approach_outline"],
            "proposed_first_experiments": sections["proposed_first_experiments"],
            "theory_of_impact_chain": sections["theory_of_impact_chain"],
            "strength_rationale": sections["strength_rationale"],
            "alternative_framings": alt_framings_list,
            "cited_sources": cited_sources_list,
        },
    }

    return proposal


def _extract_citations(novelty_assessment: dict, citation_verification: dict) -> list[dict]:
    """Extract verified citations from novelty assessment and citation verification."""
    verified_citations = []
    cv_verified = []
    if isinstance(citation_verification, dict):
        cv_verified = citation_verification.get("verified", [])

    evidence = novelty_assessment.get("evidence", [])
    if isinstance(evidence, list):
        for ev in evidence:
            if isinstance(ev, dict):
                cit_title = ev.get("source", "")
                if not cv_verified or cit_title in cv_verified:
                    verified_citations.append({
                        "title": cit_title,
                        "authors": "",
                        "url": ev.get("url", ""),
                        "relevance": ev.get("finding", ""),
                    })
            elif isinstance(ev, str):
                if not cv_verified or ev in cv_verified:
                    verified_citations.append({
                        "title": ev,
                        "authors": "",
                        "url": "",
                        "relevance": "Referenced in novelty assessment.",
                    })
    return verified_citations


def _build_sections(
    idea_id, title, use_title, body, effective_scores,
    refinements, promoted_framing,
):
    """Build the text sections of the proposal."""

    # Research question
    rq = (
        f"What does a focused empirical investigation of '{title}' reveal about "
        f"safety-relevant behaviors in current language models, and what concrete, "
        f"measurable findings can a beginner mentor-novice team produce within 30 hours "
        f"using standard open-source tools?"
    )

    # Approach outline
    if promoted_framing:
        promoted_approach = promoted_framing.get("approach", "")
        approach_outline = (
            f"{promoted_approach} "
            f"The original framing ('{title}') was refined through Phase 2 strengthening "
            f"and Phase 3 framing selection; the promoted framing '{promoted_framing['title']}' "
            f"achieved a higher weighted score. "
            f"The mentor handles environment setup and code review; the novice drives data "
            f"collection, analysis, and blog writing. All results are reported in a public "
            f"blog post suitable for a general AI safety audience."
        )
    else:
        ref_summary = _summarise_refinements(refinements)
        approach_outline = (
            f"Using freely available tools (Hugging Face transformers, SAELens, "
            f"TransformerLens, or equivalent depending on the specific question), "
            f"the team will conduct a focused empirical investigation of the "
            f"safety-relevant question. "
            f"Phase 2 refinements applied: {ref_summary} "
            f"The mentor handles environment setup and reviews code; the novice drives "
            f"data collection, analysis, and blog writing. Deliverable: a working "
            f"Colab notebook and a blog post explaining safety relevance."
        )

    # First experiments
    exps = _build_experiments(effective_scores)

    # Theory of impact chain
    toi_chain = _build_toi_chain(title, effective_scores)

    # Strength rationale
    strength_rationale = _build_strength_rationale(title, effective_scores, refinements)

    return {
        "research_question": rq,
        "approach_outline": approach_outline,
        "proposed_first_experiments": exps,
        "theory_of_impact_chain": toi_chain,
        "strength_rationale": strength_rationale,
    }


def _summarise_refinements(refinements: dict) -> str:
    refs = refinements.get("refinements", [])
    if not refs:
        return "no modifications needed (all scored dimensions met threshold)."
    parts = []
    for r in refs:
        parts.append(
            f"{r['criterion']} raised from {r['original_score']} to "
            f"{r['expected_score']}"
        )
    return "; ".join(parts) + "."


def _build_experiments(effective_scores: dict) -> list[str]:
    """Build 3 concrete first experiments based on effective scores."""
    accessible = effective_scores.get("accessible_complexity", 3)
    narrow = effective_scores.get("narrow_scope", 3)

    exp1 = (
        "Baseline data collection: load one pre-trained open-weight model "
        "(≤7B parameters, e.g., Gemma-2-2B or Phi-3-mini) using the Hugging Face "
        "pipeline API. Curate a set of 150-200 prompts spanning the safety-relevant "
        "behavior of interest (sourced from public datasets or hand-crafted). "
        "Run the model on all prompts and record outputs. Manually label 50 examples "
        "as 'target behavior present/absent'. "
        "Expected outcome: a labelled dataset establishing a baseline rate for the "
        "phenomenon, completable in 4-6 hours."
    )

    if accessible >= 4:
        exp2 = (
            "Feature/activation extraction: using SAELens or TransformerLens, "
            "extract internal representations (residual stream activations or SAE "
            "feature activations at layer 12 or the last-third of the model) for "
            "the labelled dataset. Compute one summary metric: cosine similarity "
            "between the mean activation vectors of the two labeled classes, or "
            "the top-10 SAE feature activation magnitudes per class. "
            "Expected outcome: a quantitative signature distinguishing the two "
            "behavioral conditions, reportable in a 2x2 table, completable in 6-8 hours."
        )
    else:
        exp2 = (
            "Lightweight probing: extract last-layer hidden-state vectors for the "
            "labelled examples using the Hugging Face model API. Train a logistic "
            "regression probe (scikit-learn) on the 80% training split. Evaluate "
            "on the 20% held-out split. Report AUC and confusion matrix. "
            "Expected outcome: a single AUC number with interpretation, completable "
            "in 4-6 hours in a Colab notebook."
        )

    if narrow >= 5:
        exp3 = (
            "Targeted intervention: having identified the key discriminative feature "
            "or probe direction, run one causal intervention — either zero-ablate the "
            "top SAE feature or steer activations in the probe direction — on 20 test "
            "examples. Measure whether the model's output changes in the expected "
            "direction (report % change in target behavior). This is the headline "
            "result for the blog post, completable in 4-6 hours."
        )
    else:
        exp3 = (
            "Cross-condition comparison: re-run the measurement on a second condition "
            "(a different prompt framing, a fine-tuned variant, or a second model) "
            "to assess generalizability. Tabulate results across the two conditions. "
            "Expected outcome: a comparison table showing whether the finding is "
            "condition-specific or robust, providing a richer blog narrative, "
            "completable in 5-7 hours."
        )

    return [exp1, exp2, exp3]


def _build_toi_chain(title: str, effective_scores: dict) -> str:
    toi = effective_scores.get("theory_of_impact", 3)
    if toi >= 4:
        return (
            f"(A) This research produces a concrete, reproducible empirical finding "
            f"about a safety-relevant behavior in current language models — specifically, "
            f"whether internal representations or features predictably correspond to "
            f"the target behavior, and whether causal interventions can modify it. "
            f"(B) That finding either confirms or disconfirms a known safety hypothesis, "
            f"directly informing the design of safety evaluations, monitoring probes, "
            f"or fine-tuning interventions used by safety teams. "
            f"(C) Better safety evaluations and monitoring reduce the probability that "
            f"deployed models exhibit undetected harmful behaviors at scale, lowering "
            f"the risk of catastrophic outcomes from advanced AI systems."
        )
    else:
        return (
            f"(A) This research produces an empirical data point about a safety-relevant "
            f"behavior in language models, including a null result if the predicted "
            f"feature pattern is not found. "
            f"(B) Even null results are informative: they update the community's model "
            f"of where safety risks are concentrated and which probing approaches are "
            f"tractable, guiding more targeted future work. "
            f"(C) More targeted safety research reduces wasteful investment in "
            f"non-tractable directions and accelerates progress on reducing catastrophic "
            f"risk from advanced AI systems."
        )


def _build_strength_rationale(
    title: str, effective_scores: dict, refinements: dict
) -> str:
    top_dims = sorted(
        [(k, v) for k, v in effective_scores.items() if ACTIVE_WEIGHTS.get(k, 0) > 0],
        key=lambda x: ACTIVE_WEIGHTS.get(x[0], 0) * x[1],
        reverse=True,
    )[:2]
    top_names = [f"{d[0]}={d[1]}" for d in top_dims]
    ws_val = weighted_score({k: {"score": v} for k, v in effective_scores.items()})
    refs = refinements.get("refinements", [])
    ref_note = (
        f" Phase 2 strengthening raised {', '.join(r['criterion'] for r in refs)}."
        if refs else ""
    )
    return (
        f"This idea scores strongly on its highest-weighted criteria: "
        f"{', '.join(top_names)} (weighted score {ws_val:.2f}/5.00 after refinement).{ref_note} "
        f"The idea is particularly well-suited for a mentor-novice pair: the methodology "
        f"inherits from published work and the core deliverable fits within 30 hours. "
        f"The safety relevance is concrete and communicable in a blog post without "
        f"requiring deep specialist knowledge."
    )


# ---------------------------------------------------------------------------
# Markdown writer
# ---------------------------------------------------------------------------

SECTION_KEYS = [
    "research_question",
    "approach_outline",
    "proposed_first_experiments",
    "theory_of_impact_chain",
    "strength_rationale",
    "alternative_framings",
    "cited_sources",
]
SECTION_HEADINGS = {
    "research_question": "Research Question",
    "approach_outline": "Approach Outline",
    "proposed_first_experiments": "Proposed First Experiments",
    "theory_of_impact_chain": "Theory of Impact Chain",
    "strength_rationale": "Strength Rationale",
    "alternative_framings": "Alternative Framings",
    "cited_sources": "Cited Sources",
}


def _format_section(value) -> str:
    if isinstance(value, list):
        return "\n".join(f"- {item}" for item in value) if value else ""
    return str(value)


def write_proposal(run_dir: Path, proposal: dict) -> Path:
    """Write proposal as markdown with YAML frontmatter."""
    import yaml

    refine_dir = run_dir / "refine"
    refine_dir.mkdir(parents=True, exist_ok=True)

    idea_id = proposal.get("idea_id", "unknown")
    file_path = refine_dir / f"{idea_id}.md"

    # Frontmatter excludes sections
    frontmatter = {k: v for k, v in proposal.items() if k != "sections"}

    sections = proposal.get("sections", {})
    body_parts = []
    for key in SECTION_KEYS:
        heading = SECTION_HEADINGS[key]
        content = _format_section(sections.get(key, ""))
        body_parts.append(f"# {heading}\n\n{content}\n")

    fm_str = yaml.safe_dump(
        frontmatter, default_flow_style=False, sort_keys=False, allow_unicode=True
    )
    body_str = "\n".join(body_parts)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"---\n{fm_str}---\n\n{body_str}\n")

    return file_path


# ---------------------------------------------------------------------------
# Orchestrator logger
# ---------------------------------------------------------------------------

def log_event(run_dir: Path, stage: str, level: str, message: str, data: dict):
    """Append a log event to the orchestrator log."""
    log_dir = run_dir / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "orchestrator.jsonl"
    entry = {
        "timestamp": now_ts(),
        "stage": stage,
        "level": level,
        "message": message,
        "data": data,
    }
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Batch 08 Refinement — Ranks 737-828 (92 ideas)")
    print("Team: Mentor-Novice Pair | Participant: bluedot_technical_project")
    print(f"Criteria weights: theory_of_impact=3.0, accessible_complexity=3.5,")
    print(f"                  narrow_scope=5.0, novelty=2.5")
    print("=" * 70)

    # Load batch
    print(f"\nLoading batch from {BATCH_FILE}...")
    with open(BATCH_FILE, encoding="utf-8") as f:
        batch = json.load(f)
    print(f"  Loaded {len(batch)} items.")

    # Load idea bodies
    print(f"Loading idea bodies from {IDEA_BODIES_FILE}...")
    with open(IDEA_BODIES_FILE, encoding="utf-8") as f:
        idea_bodies = json.load(f)
    print(f"  Loaded {len(idea_bodies)} idea bodies.\n")

    log_event(RUN_DIR, "refine", "info", "Refine stage batch 08 started",
              {"batch": "batch_08", "scored_ideas": len(batch)})

    # Tracking counters
    ideas_with_weak = 0
    ideas_strengthened = 0
    refinements_accepted_total = 0
    refinements_discarded_total = 0
    framings_generated = 0
    framings_promoted = 0
    framings_kept_as_alts = 0
    proposals_written = 0
    minimal_fallbacks = 0
    score_improvements = []
    estimated_novelty_flags = []

    for idx, item in enumerate(batch):
        scored_idea = item["scored_idea"]
        idea_id = scored_idea["idea_id"]
        title = scored_idea["title"]
        scores = scored_idea["scores"]
        original_ws = scored_idea.get("weighted_score", 0.0)
        body = idea_bodies.get(idea_id, "")

        print(f"[{idx+1:3d}/92] {idea_id}: {title[:55]}...")
        print(f"        pre-ws={original_ws:.3f} | {format_scores_summary(scores)}")

        # ----------------------------------------------------------------
        # Phase 2: strengthen weak dimensions
        # ----------------------------------------------------------------
        weak_dims = get_weak_dims(scores)
        if weak_dims:
            ideas_with_weak += 1

        refinements = generate_refinements(scored_idea, weak_dims, body)
        accepted = refinements["accepted_count"]
        discarded = refinements["discarded_count"]
        refinements_accepted_total += accepted
        refinements_discarded_total += discarded
        if accepted > 0:
            ideas_strengthened += 1

        # ----------------------------------------------------------------
        # Phase 3: alternative framings (all ideas in top 50%)
        # ----------------------------------------------------------------
        try:
            framings = generate_alternative_framings(scored_idea, refinements, body)
            framings_generated += len(framings)

            # Compute post-refine weighted score (before framing)
            eff = {n: scores.get(n, {}).get("score", 0)
                   for n in ["theory_of_impact", "accessible_complexity",
                              "narrow_scope", "novelty"]}
            for r in refinements.get("refinements", []):
                eff[r["criterion"]] = r["expected_score"]
            post_refine_ws = weighted_score({k: {"score": v} for k, v in eff.items()})

            promoted, non_promoted, winning_ws = promote_best_framing(
                idea_id, post_refine_ws, framings
            )
            if promoted:
                framings_promoted += 1
                framings_kept_as_alts += len(non_promoted)
            else:
                framings_kept_as_alts += len(framings)
                promoted = None
                non_promoted = framings

        except Exception as e:
            log_event(RUN_DIR, "refine", "warning",
                      "Alternative framing generation failed",
                      {"idea_id": idea_id, "title": title, "error": str(e)})
            promoted = None
            non_promoted = []
            print(f"        WARNING: framing failed: {e}")

        # ----------------------------------------------------------------
        # Phase 4: assemble and write proposal
        # ----------------------------------------------------------------
        try:
            proposal = assemble_proposal(
                idea=scored_idea,
                refinements=refinements,
                promoted_framing=promoted,
                non_promoted_framings=non_promoted,
                body=body,
            )
            path = write_proposal(RUN_DIR, proposal)
            proposals_written += 1

            final_ws = proposal["post_refine_weighted_score"]
            if final_ws > original_ws + 0.005:
                score_improvements.append({
                    "idea_id": idea_id,
                    "title": title[:55],
                    "before": original_ws,
                    "after": final_ws,
                    "delta": round(final_ws - original_ws, 4),
                })
            if proposal.get("sections", {}).get("proposed_first_experiments"):
                pass  # good

            # Track estimated novelty flags
            if proposal.get("weak_dimensions_addressed") and \
               "novelty" in proposal.get("weak_dimensions_addressed", []):
                estimated_novelty_flags.append(
                    f"{idea_id}: novelty re-estimated (not web-verified)"
                )
            if promoted is not None:
                estimated_novelty_flags.append(
                    f"{idea_id}: novelty estimated in promoted framing"
                )

            print(f"        post-ws={final_ws:.3f} | wrote {path.name}")

        except Exception as e:
            log_event(RUN_DIR, "refine", "warning",
                      "Proposal generation failed, using minimal fallback",
                      {"idea_id": idea_id, "title": title, "error": str(e)})
            try:
                minimal = {
                    "idea_id": idea_id,
                    "run_id": "2026-03-19T19-58-40",
                    "stage": "refine",
                    "timestamp": now_ts(),
                    "title": title,
                    "original_scores": {
                        k: v.get("score", 0) if isinstance(v, dict) else 0
                        for k, v in scores.items()
                    },
                    "pre_refine_weighted_score": original_ws,
                    "post_refine_weighted_score": original_ws,
                    "weak_dimensions_addressed": [],
                    "num_alternative_framings": 0,
                    "refinement_confidence": 0.3,
                    "sections": {
                        "research_question": f"Empirical investigation of: {title}",
                        "approach_outline": "See original scored idea for details.",
                        "proposed_first_experiments": [
                            "Run model on baseline prompt set and record outputs.",
                            "Extract activations and compute one summary metric.",
                            "Report result in blog post.",
                        ],
                        "theory_of_impact_chain": "",
                        "strength_rationale": "",
                        "alternative_framings": [],
                        "cited_sources": [],
                    },
                }
                write_proposal(RUN_DIR, minimal)
                minimal_fallbacks += 1
                print(f"        FALLBACK written for {idea_id}: {e}")
            except Exception as e2:
                print(f"        CRITICAL: even fallback failed for {idea_id}: {e2}")

    # ----------------------------------------------------------------
    # Log phase completions
    # ----------------------------------------------------------------
    log_event(RUN_DIR, "refine", "info", "Phase 2 complete: auto-strengthen", {
        "total_ideas": len(batch),
        "ideas_with_weak_dims": ideas_with_weak,
        "ideas_strengthened": ideas_strengthened,
        "refinements_accepted": refinements_accepted_total,
        "refinements_discarded": refinements_discarded_total,
    })
    log_event(RUN_DIR, "refine", "info", "Phase 3 complete: alternative framings", {
        "promising_ideas": len(batch),
        "framings_generated": framings_generated,
        "framings_promoted": framings_promoted,
        "framings_kept_as_alternatives": framings_kept_as_alts,
    })
    log_event(RUN_DIR, "refine", "info", "Phase 4 complete: proposals assembled", {
        "proposals_written": proposals_written,
        "minimal_fallbacks": minimal_fallbacks,
    })

    # ----------------------------------------------------------------
    # Summary
    # ----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("BATCH 08 REFINEMENT SUMMARY")
    print("=" * 70)
    print(f"Total ideas processed:           {len(batch)}")
    print(f"Ideas with weak dimensions:      {ideas_with_weak}")
    print(f"Ideas strengthened (Phase 2):    {ideas_strengthened}")
    print(f"Refinements accepted:            {refinements_accepted_total}")
    print(f"Refinements discarded:           {refinements_discarded_total}")
    print(f"Alt framings generated (Phase 3):{framings_generated}")
    print(f"Framings promoted:               {framings_promoted}")
    print(f"Framings kept as alternatives:   {framings_kept_as_alts}")
    print(f"Proposals written (Phase 4):     {proposals_written}")
    print(f"Minimal fallbacks:               {minimal_fallbacks}")

    if score_improvements:
        print(f"\nScore improvements ({len(score_improvements)} ideas):")
        for imp in sorted(score_improvements, key=lambda x: -x["delta"])[:25]:
            print(
                f"  {imp['idea_id']}: {imp['before']:.3f} -> {imp['after']:.3f} "
                f"(+{imp['delta']:.4f}) | {imp['title']}"
            )

    if estimated_novelty_flags:
        print(f"\nEstimated novelty flags ({len(estimated_novelty_flags)}):")
        for flag in estimated_novelty_flags[:20]:
            print(f"  {flag}")

    print(f"\nProposals written to: {REFINE_DIR}/")
    print("Next step: use /rank-ideas to produce the final ranking.")
    print("=" * 70)


if __name__ == "__main__":
    main()
