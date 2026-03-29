#!/usr/bin/env python3
"""
Refine pipeline batch 15: Phase 2 (strengthen weak dimensions) + Phase 4 (full proposals).
Skips Phase 3 (alternative framings / bottom 50%).

Team: Mentor-Novice Pair, CS students, beginner skills, 30 hours, Colab Pro
Active weights: theory_of_impact=3.0, accessible_complexity=3.5, narrow_scope=5.0, novelty=2.5
Divisor: 14.0

Run with:
    uv run python scripts/refine_batch_15.py
"""

from __future__ import annotations

import json
import sys
import re
from pathlib import Path

# Project root is CWD when invoked via uv run
PROJECT_ROOT = Path(__file__).parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "src"))

from saim.pipeline.refine import (
    analyze_weaknesses,
    build_proposal_skeleton,
    write_refined_proposal,
)
from saim.config.schemas import ScoringCriteria, RubricLevel
from saim.pipeline.orchestrator import log_entry


def log_event(run_dir: Path, stage: str, level: str, message: str, data: dict | None = None) -> None:
    """Thin wrapper so callers can pass a Path and a dict."""
    import json as _json
    data_json = _json.dumps(data) if data else None
    log_entry(str(run_dir), stage, level, message, data_json)

# ── Configuration ────────────────────────────────────────────────────────────
RUN_DIR = PROJECT_ROOT / "data/runs/2026-03-19T19-58-40"
BATCH_FILE = RUN_DIR / "refine/batch_15.json"
IDEA_BODIES_FILE = RUN_DIR / "refine/idea_bodies.json"
GENERATE_DIR = RUN_DIR / "generate"

ACTIVE_WEIGHTS: dict[str, float] = {
    "theory_of_impact": 3.0,
    "accessible_complexity": 3.5,
    "narrow_scope": 5.0,
    "novelty": 2.5,
    "low_compute": 0.0,  # inactive for this team
}
WEIGHT_DIVISOR = 14.0

PARTICIPANT_SUMMARY = (
    "Mentor-Novice Pair: CS students with beginner Python/ML skills, guided by a mentor. "
    "Total time budget: 30 hours (implementation + analysis + blog post). "
    "Compute: Colab Pro (T4/A100 GPU). "
    "Goals: first hands-on AI safety research experience, aim for a publishable or shareable result. "
    "Deliverable: working experiment + well-written blog post communicating findings."
)

# ── Criteria definition (mirrors config/criteria.yaml) ──────────────────────
CRITERIA = [
    ScoringCriteria(
        name="theory_of_impact",
        description="Does this idea have a clear, specific theory of how it reduces catastrophic risks from advanced AI?",
        default_weight=1.5,
        refinement_threshold=4,
        rubric=[
            RubricLevel(score=1, label="No impact chain",
                        description="No articulated connection between the research and reducing catastrophic risk from advanced AI."),
            RubricLevel(score=2, label="Vague impact",
                        description="Claims safety relevance but does not trace to a specific catastrophic risk scenario."),
            RubricLevel(score=3, label="Plausible chain",
                        description="Names a specific catastrophic risk mechanism and proposes research that could address it, but the chain has a gap — it skips a step or the link to catastrophic risk reduction is underspecified."),
            RubricLevel(score=4, label="Strong chain",
                        description="Every link from research output to reduction of catastrophic AI risk is explicit and independently defensible. The catastrophic risk scenario is concrete, not generic."),
            RubricLevel(score=5, label="Compelling chain",
                        description="Strong chain (score 4) that additionally targets a catastrophic risk pathway recognized as critical by major safety orgs, and intermediate deliverables also have independent safety value."),
        ],
    ),
    ScoringCriteria(
        name="low_compute",
        description="Can this idea be explored with limited compute resources?",
        default_weight=1.5,
        refinement_threshold=0,  # never refine (weight=0 for this team)
        rubric=[
            RubricLevel(score=1, label="Infeasible", description="Requires large-scale training runs, hundreds of GPU-hours, or frontier model weights."),
            RubricLevel(score=2, label="Heavy", description="Requires multiple A100-days or significant cloud budget."),
            RubricLevel(score=3, label="Moderate", description="Feasible with a single mid-range GPU over days, or moderate API costs."),
            RubricLevel(score=4, label="Light", description="Runs on a single consumer GPU or modest API budget."),
            RubricLevel(score=5, label="Minimal", description="Can be done with CPU-only, free-tier APIs, or purely analytical/theoretical work."),
        ],
    ),
    ScoringCriteria(
        name="accessible_complexity",
        description="Is the technical complexity appropriate for the team's skill level?",
        default_weight=1.5,
        refinement_threshold=4,
        rubric=[
            RubricLevel(score=1, label="Expert-only",
                        description="Requires deep specialist knowledge (e.g., novel architecture design, advanced math) with no clear simplification path."),
            RubricLevel(score=2, label="Advanced",
                        description="Requires strong ML/research background and familiarity with specific subfield literature; a motivated grad student could attempt it with significant ramp-up."),
            RubricLevel(score=3, label="Intermediate",
                        description="Requires solid ML fundamentals and comfort with existing frameworks/tools; methodology is well-established but application is novel."),
            RubricLevel(score=4, label="Guided",
                        description="Clear methodology inherited from existing work (e.g., replication with variation); a novice with mentor guidance can execute it."),
            RubricLevel(score=5, label="Accessible",
                        description="Well-defined steps using standard tools and public datasets; a motivated beginner with basic Python/ML can make meaningful progress independently."),
        ],
    ),
    ScoringCriteria(
        name="narrow_scope",
        description="Does the idea have a self-contained first deliverable that is valuable on its own, with a clear methodology and success criteria?",
        default_weight=1.5,
        refinement_threshold=5,
        rubric=[
            RubricLevel(score=1, label="Open-ended program",
                        description="An entire research agenda or open-ended question with no clear stopping point and no identifiable first deliverable."),
            RubricLevel(score=2, label="No clear first milestone",
                        description="Multiple loosely connected sub-questions or a large design space; a deliverable might exist but depends on resolving many unknowns first."),
            RubricLevel(score=3, label="Deliverable requires sustained effort",
                        description="A concrete first deliverable exists but requires multiple workstreams or experimental dimensions to reach."),
            RubricLevel(score=4, label="Focused first deliverable",
                        description="A specific, well-bounded first deliverable with clear methodology and few dependencies; the first milestone stands on its own."),
            RubricLevel(score=5, label="Tightly scoped",
                        description="A single, precise experiment with well-defined success criteria and an obvious deliverable (e.g., one replication, one benchmark, one ablation study); can go from start to meaningful result quickly."),
        ],
    ),
    ScoringCriteria(
        name="novelty",
        description="How novel is this idea relative to published work?",
        default_weight=1.0,
        refinement_threshold=4,
        rubric=[
            RubricLevel(score=1, label="Already solved",
                        description="HARD GATE — existing published work fully addresses this idea; proposed research would not produce new knowledge."),
            RubricLevel(score=2, label="Largely addressed",
                        description="Multiple published works cover most of the proposed contribution; remaining gaps are minor or incremental."),
            RubricLevel(score=3, label="Partially addressed",
                        description="Published work exists on the topic but the specific angle, method, or combination proposed has not been explored; the idea extends existing work meaningfully."),
            RubricLevel(score=4, label="Mostly novel",
                        description="No direct published work on this specific proposal; related work exists in adjacent areas but the core contribution is new."),
            RubricLevel(score=5, label="Novel",
                        description="No published work found addressing this question or approach; the idea opens a genuinely new direction."),
        ],
    ),
]

CRITERIA_BY_NAME = {c.name: c for c in CRITERIA}


# ── Helpers ───────────────────────────────────────────────────────────────────

def compute_weighted_score(scores: dict) -> float:
    total = 0.0
    for name, weight in ACTIVE_WEIGHTS.items():
        if weight == 0:
            continue
        entry = scores.get(name, {})
        score_val = entry.get("score", 0) if isinstance(entry, dict) else 0
        total += weight * score_val
    return round(total / WEIGHT_DIVISOR, 4)


def get_idea_body(idea_id: str, idea_bodies: dict, scored_idea: dict) -> str:
    """Return the full idea body text, trying multiple sources."""
    # 1. idea_bodies lookup
    if idea_id in idea_bodies:
        body = idea_bodies[idea_id]
        if isinstance(body, str) and body.strip():
            return body.strip()
        if isinstance(body, dict):
            text = body.get("body", "")
            if text:
                return text.strip()

    # 2. original_idea structured fields
    original = scored_idea.get("original_idea", {})
    if isinstance(original, dict) and original.get("problem"):
        parts = []
        if original.get("title"):
            parts.append(f"**Title:** {original['title']}")
        for key in ("problem", "direction", "why_it_matters", "relevant_context"):
            val = original.get(key, "")
            if val:
                label = key.replace("_", " ").title()
                parts.append(f"**{label}:** {val}")
        return "\n\n".join(parts)

    # 3. generate/*.md file
    md_path = GENERATE_DIR / f"{idea_id}.md"
    if md_path.exists():
        text = md_path.read_text()
        m = re.match(r"^---\n.*?\n---\n\n?(.*)", text, re.DOTALL)
        if m:
            return m.group(1).strip()
        return text.strip()

    return ""


def parse_json_from_response(text: str) -> dict | None:
    """Extract the first JSON object from an LLM response."""
    # Direct parse
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError:
        pass
    # Code block
    m = re.search(r"```(?:json)?\s*(\{[\s\S]*?\})\s*```", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # Bare JSON object (greedy from first { to last })
    m = re.search(r"\{[\s\S]*\}", text)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


def call_claude(prompt: str, max_tokens: int = 4096) -> str | None:
    try:
        import anthropic
        client = anthropic.Anthropic()
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
    except Exception as e:
        print(f"    [ERROR] Claude API call failed: {e}", file=sys.stderr)
        return None


def get_verified_citations(scored_idea: dict) -> list[dict]:
    cv = scored_idea.get("citation_verification", {})
    verified: list[dict] = []
    if isinstance(cv, dict):
        # Old format: {title: {status, ...}}
        for key, val in cv.items():
            if isinstance(val, dict) and val.get("status") in ("verified", "corrected"):
                verified.append({"title": key, **val})
        # New format: {citations: [...]}
        for c in cv.get("citations", []):
            if isinstance(c, dict) and c.get("status") in ("verified", "corrected"):
                verified.append(c)
    return verified


def rubric_block(criterion_name: str) -> str:
    crit = CRITERIA_BY_NAME.get(criterion_name)
    if not crit:
        return ""
    lines = []
    for level in crit.rubric:
        lines.append(f"    Score {level.score} ({level.label}): {level.description}")
    return "\n".join(lines)


# ── LLM prompt builders ──────────────────────────────────────────────────────

def build_refinement_prompt(idea_id: str, title: str, idea_body: str,
                             weak_dims: list, strong_dims: list) -> str:
    weak_block = ""
    for wd in weak_dims:
        weak_block += (
            f"\n**{wd['name']}** — current score: {wd['score']}, threshold: {wd['threshold']}\n"
            f"  Scoring reasoning: {wd['reasoning']}\n"
            f"  Full rubric:\n{rubric_block(wd['name'])}\n"
        )

    strong_block = "\n".join(f"  - {sd['name']}: {sd['score']}/5" for sd in strong_dims)

    return f"""You are brainstorming improvements to an AI Safety research idea. Your goal is to maximize scores on the weak dimensions according to the rubric.

**Idea:** {title}
{idea_body}

**Weak Dimensions (need improvement):**
{weak_block}
**Strong Dimensions (already passing):**
{strong_block}

**Participant Profile:**
{PARTICIPANT_SUMMARY}

**Task:** For each weak dimension, propose a concrete change to the idea that would raise its score above the threshold on the rubric. The improvement must be:
- Specific and actionable (not vague advice)
- Compatible with beginner CS students guided by a mentor, 30 hours total, Colab Pro

**Output format (JSON only, no other text):**
```json
{{
  "idea_id": "{idea_id}",
  "refinements": [
    {{
      "criterion": "<name>",
      "original_score": <int>,
      "change": "<2-4 sentences describing the concrete change to the idea>",
      "expected_score": <int>,
      "rationale": "<1-2 sentences why this raises the score per the rubric>"
    }}
  ],
  "confidence": <0.0-1.0>,
  "overall_notes": "<any cross-cutting observations>"
}}
```"""


def build_rescore_prompt(idea_id: str, title: str, idea_body: str,
                          proposed_refinements: list, weak_dims: list) -> str:
    changes_block = "\n".join(
        f"  - [{r.get('criterion', '?')}] {r.get('change', '')}" for r in proposed_refinements
    )
    criteria_block = ""
    for wd in weak_dims:
        criteria_block += (
            f"\n**{wd['name']}** (original score: {wd['score']}):\n"
            f"{rubric_block(wd['name'])}\n"
        )

    return f"""You are re-scoring a refined AI Safety research idea on specific dimensions.

**Original Idea:** {title}
{idea_body}

**Refinements Applied:**
{changes_block}

**Task:** Re-score the idea as modified by the refinements on each criterion below. Use the exact rubric. If a refinement meaningfully changes the novelty picture, mark is_estimated_novelty=true.

**Criteria to re-score:**
{criteria_block}

**Output format (JSON only, no other text):**
```json
{{
  "idea_id": "{idea_id}",
  "rescored_dimensions": [
    {{
      "criterion": "<name>",
      "original_score": <int>,
      "new_score": <int>,
      "reasoning": "<1-2 sentences>",
      "is_estimated_novelty": <true|false>
    }}
  ]
}}
```"""


def build_proposal_prompt(idea_id: str, title: str, idea_body: str,
                           final_scores: dict, accepted_refinements: list,
                           cited_sources: list, weighted_score: float,
                           novelty_classification: str) -> str:
    scores_block = ""
    for name, weight in ACTIVE_WEIGHTS.items():
        if weight == 0:
            continue
        entry = final_scores.get(name, {})
        score_val = entry.get("score", "?") if isinstance(entry, dict) else "?"
        reasoning = entry.get("reasoning", "") if isinstance(entry, dict) else ""
        scores_block += f"  - **{name}** ({weight}×): {score_val}/5 — {reasoning}\n"

    refinements_block = (
        "\n".join(f"  - [{r.get('criterion')}] {r.get('change', '')}"
                  for r in accepted_refinements)
        if accepted_refinements else "  None"
    )

    citations_block = ""
    for c in cited_sources:
        if isinstance(c, dict):
            citations_block += f"  - {c.get('title', '?')} — {c.get('details', c.get('notes', ''))}\n"
        else:
            citations_block += f"  - {c}\n"
    if not citations_block:
        citations_block = "  None"

    return f"""You are assembling a full research proposal for an AI Safety idea.

**Idea:** {title}
{idea_body}

**Current Scores (weighted score: {weighted_score:.3f}/5):**
{scores_block}

**Refinements Incorporated:**
{refinements_block}

**Verified Citations from Prior Stages:**
{citations_block}

**Participant Profile:**
{PARTICIPANT_SUMMARY}

**Task:** Produce a structured, detailed research proposal. Be specific and concrete. All experiments must be achievable in ~25 hours (leaving 5 hours for blog post) by a beginner CS student with mentor guidance on Colab Pro. Cite sources precisely where known.

**Output format (JSON only, no other text):**
```json
{{
  "idea_id": "{idea_id}",
  "title": "<final title — may refine the original>",
  "research_question": "<1-2 clear sentences framing the core research question>",
  "approach_outline": "<3-5 sentences describing the methodology and key steps>",
  "proposed_first_experiments": [
    "<Experiment 1: what to do, what to measure, what outcome would confirm/refute the hypothesis>",
    "<Experiment 2>",
    "<Experiment 3>"
  ],
  "theory_of_impact_chain": "<2-4 sentences: if this works, then X, which leads to Y, which improves safety because Z>",
  "strength_rationale": "<2-3 sentences on why this idea scores well, referencing the highest-scoring criteria>",
  "cited_sources": [
    {{"title": "<paper title>", "authors": "<authors>", "url": "<DOI or arXiv URL>", "relevance": "<one sentence>"}}
  ],
  "refinements_applied": ["<change 1>", "<change 2>"],
  "alternative_framings": [],
  "metadata": {{
    "weighted_score": {weighted_score},
    "confidence": <0.0-1.0>,
    "novelty_classification": "{novelty_classification}",
    "has_estimated_novelty": <true|false>,
    "weak_dimensions_addressed": <count of accepted refinements>
  }}
}}
```"""


# ── Per-idea processing ───────────────────────────────────────────────────────

def process_idea(item: dict, idea_bodies: dict) -> dict:
    scored_idea = item["scored_idea"]
    idea_id = scored_idea.get("idea_id", "unknown")
    title = scored_idea.get("title", "")
    scores = scored_idea.get("scores", {})
    original_weighted = scored_idea.get("weighted_score", 0.0)
    novelty_assessment = scored_idea.get("novelty_assessment", {})
    novelty_classification = novelty_assessment.get("classification", "unknown")

    idea_body = get_idea_body(idea_id, idea_bodies, scored_idea)

    print(f"\n{'─'*60}")
    print(f"  {idea_id}: {title}")
    print(f"  Pre-refine weighted score: {original_weighted:.3f}")

    # Deep-copy scores to track modifications
    final_scores: dict[str, dict] = {}
    for k, v in scores.items():
        final_scores[k] = dict(v) if isinstance(v, dict) else {"score": v, "reasoning": "", "confidence": 0.0}

    # ── Phase 2 ───────────────────────────────────────────────────────────────
    weakness_ctx = analyze_weaknesses(scored_idea, CRITERIA, ACTIVE_WEIGHTS)
    weak_dims = weakness_ctx.get("weak_dimensions", [])
    strong_dims = weakness_ctx.get("strong_dimensions", [])

    accepted_refinements: list[dict] = []
    refinement_confidence = 0.0
    has_estimated_novelty = False

    if weak_dims:
        weak_names = [w["name"] for w in weak_dims]
        print(f"  Weak dimensions: {', '.join(weak_names)}")

        # 2.2: LLM refinement suggestions
        ref_prompt = build_refinement_prompt(idea_id, title, idea_body, weak_dims, strong_dims)
        ref_response = call_claude(ref_prompt, max_tokens=3000)

        if ref_response:
            ref_data = parse_json_from_response(ref_response)
        else:
            ref_data = None

        if ref_data and isinstance(ref_data.get("refinements"), list):
            proposed = ref_data["refinements"]
            refinement_confidence = float(ref_data.get("confidence", 0.5))

            # 2.3: Re-score on weak dimensions
            rescore_prompt = build_rescore_prompt(idea_id, title, idea_body, proposed, weak_dims)
            rescore_response = call_claude(rescore_prompt, max_tokens=2000)

            if rescore_response:
                rescore_data = parse_json_from_response(rescore_response)
            else:
                rescore_data = None

            if rescore_data and isinstance(rescore_data.get("rescored_dimensions"), list):
                rescore_map = {rd["criterion"]: rd for rd in rescore_data["rescored_dimensions"]}
                discarded_count = 0
                for ref in proposed:
                    criterion = ref.get("criterion", "")
                    original_score = ref.get("original_score", 0)
                    rd = rescore_map.get(criterion, {})
                    new_score = rd.get("new_score", 0)

                    if new_score > original_score:
                        accepted_refinements.append(ref)
                        if criterion in final_scores:
                            final_scores[criterion]["score"] = new_score
                            base_reasoning = final_scores[criterion].get("reasoning", "")
                            rd_reasoning = rd.get("reasoning", "")
                            final_scores[criterion]["reasoning"] = (
                                f"{base_reasoning} [Refined: {rd_reasoning}]".strip()
                            )
                        if rd.get("is_estimated_novelty") and criterion == "novelty":
                            has_estimated_novelty = True
                        print(f"    [ACCEPT] {criterion}: {original_score} → {new_score}")
                    else:
                        discarded_count += 1
                        print(f"    [DISCARD] {criterion}: no improvement ({original_score} → {new_score})")
            else:
                print("    [WARN] Could not parse rescore response; keeping originals")
                log_event(RUN_DIR, "refine", "warning",
                          "LLM rescore parse failed",
                          {"idea_id": idea_id, "title": title})
        else:
            print("    [WARN] Could not parse refinement response; keeping originals")
            log_event(RUN_DIR, "refine", "warning",
                      "LLM refinement failed, keeping original",
                      {"idea_id": idea_id, "title": title})
    else:
        print("  No weak dimensions (all active criteria above threshold)")

    new_weighted = compute_weighted_score(final_scores)

    # ── Phase 4: Full proposal ────────────────────────────────────────────────
    print("  Assembling full proposal...")
    cited_sources = get_verified_citations(scored_idea)

    prop_prompt = build_proposal_prompt(
        idea_id, title, idea_body, final_scores,
        accepted_refinements, cited_sources, new_weighted, novelty_classification,
    )
    prop_response = call_claude(prop_prompt, max_tokens=6000)

    # Build skeleton (always succeeds)
    skeleton = build_proposal_skeleton(
        scored_idea,
        {"weak_dimensions": weak_dims, "strong_dimensions": strong_dims},
    )
    skeleton["refinement_confidence"] = refinement_confidence
    skeleton["post_refine_weighted_score"] = new_weighted
    skeleton["has_estimated_novelty"] = has_estimated_novelty

    used_minimal = False

    if prop_response:
        prop_data = parse_json_from_response(prop_response)
    else:
        prop_data = None

    if prop_data:
        # Fill in sections from LLM output
        skeleton["title"] = prop_data.get("title", title)

        secs = skeleton["sections"]
        secs["research_question"] = prop_data.get("research_question", "")
        secs["approach_outline"] = prop_data.get("approach_outline", "")

        expts = prop_data.get("proposed_first_experiments", [])
        if isinstance(expts, list):
            secs["proposed_first_experiments"] = "\n".join(f"- {e}" for e in expts)
        else:
            secs["proposed_first_experiments"] = str(expts)

        secs["theory_of_impact_chain"] = prop_data.get("theory_of_impact_chain", "")
        secs["strength_rationale"] = prop_data.get("strength_rationale", "")

        cited_list = prop_data.get("cited_sources", [])
        if isinstance(cited_list, list):
            secs["cited_sources"] = [
                (f"{c.get('title', '?')} — {c.get('relevance', '')} ({c.get('url', '')})"
                 if isinstance(c, dict) else str(c))
                for c in cited_list
            ]

        secs["alternative_framings"] = prop_data.get("alternative_framings", [])

        meta = prop_data.get("metadata", {})
        skeleton["refinement_confidence"] = float(meta.get("confidence", refinement_confidence))
        if meta.get("has_estimated_novelty"):
            has_estimated_novelty = True
            skeleton["has_estimated_novelty"] = True
    else:
        used_minimal = True
        log_event(RUN_DIR, "refine", "warning",
                  "Proposal generation failed, using minimal proposal",
                  {"idea_id": idea_id, "title": title})
        print("    [WARN] Using minimal proposal (LLM failed)")

    # Write proposal to disk
    try:
        out_path = write_refined_proposal(RUN_DIR, skeleton)
        written = True
        print(f"  → Written: {out_path.name}  (score: {original_weighted:.3f} → {new_weighted:.3f})")
    except Exception as e:
        written = False
        print(f"  [ERROR] Failed to write proposal for {idea_id}: {e}", file=sys.stderr)

    return {
        "idea_id": idea_id,
        "title": title,
        "pre_refine_weighted_score": original_weighted,
        "post_refine_weighted_score": new_weighted,
        "score_delta": round(new_weighted - original_weighted, 4),
        "weak_dims_found": len(weak_dims),
        "refinements_accepted": len(accepted_refinements),
        "has_estimated_novelty": has_estimated_novelty,
        "used_minimal": used_minimal,
        "written": written,
        "novelty_classification": novelty_classification,
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("=" * 70)
    print("Refine Pipeline — Batch 15")
    print("Phases: 2 (strengthen weak dims) + 4 (full proposals)  |  Phase 3 SKIPPED")
    print(f"Run dir:    {RUN_DIR}")
    print(f"Batch file: {BATCH_FILE}")
    print("=" * 70)

    # Load batch
    print(f"\nLoading batch...")
    with open(BATCH_FILE) as f:
        batch: list[dict] = json.load(f)
    print(f"  {len(batch)} ideas loaded")

    # Load idea bodies
    print("Loading idea bodies...")
    try:
        with open(IDEA_BODIES_FILE) as f:
            idea_bodies: dict = json.load(f)
        if not isinstance(idea_bodies, dict):
            idea_bodies = {}
            print("  idea_bodies.json not a dict; will use generate/*.md files")
        else:
            print(f"  {len(idea_bodies)} entries loaded")
    except Exception as e:
        idea_bodies = {}
        print(f"  Could not load idea_bodies.json ({e}); will use generate/*.md files")

    log_event(RUN_DIR, "refine", "info",
              "Refine batch 15 started (phase 2+4)",
              {"scored_ideas": len(batch)})

    # Process
    results: list[dict] = []
    stats = {
        "total": len(batch),
        "ideas_with_weak_dims": 0,
        "ideas_strengthened": 0,
        "refinements_accepted": 0,
        "refinements_discarded": 0,
        "proposals_written": 0,
        "minimal_fallbacks": 0,
        "estimated_novelty_flags": 0,
    }

    for i, item in enumerate(batch):
        print(f"\n[{i+1:3d}/{len(batch)}]", end="")
        try:
            r = process_idea(item, idea_bodies)
        except Exception as exc:
            import traceback
            idea_id = item.get("scored_idea", {}).get("idea_id", "?")
            title = item.get("scored_idea", {}).get("title", "?")
            print(f"\n  [EXCEPTION] {idea_id}: {exc}", file=sys.stderr)
            traceback.print_exc()
            log_event(RUN_DIR, "refine", "warning",
                      f"Exception in process_idea: {exc}",
                      {"idea_id": idea_id, "title": title})
            r = {
                "idea_id": idea_id, "title": title,
                "pre_refine_weighted_score": 0.0, "post_refine_weighted_score": 0.0,
                "score_delta": 0.0, "weak_dims_found": 0, "refinements_accepted": 0,
                "has_estimated_novelty": False, "used_minimal": True, "written": False,
                "novelty_classification": "unknown",
            }

        results.append(r)
        if r["weak_dims_found"] > 0:
            stats["ideas_with_weak_dims"] += 1
        if r["refinements_accepted"] > 0:
            stats["ideas_strengthened"] += 1
        stats["refinements_accepted"] += r["refinements_accepted"]
        stats["refinements_discarded"] += max(0, r["weak_dims_found"] - r["refinements_accepted"])
        if r["written"]:
            stats["proposals_written"] += 1
        if r["used_minimal"]:
            stats["minimal_fallbacks"] += 1
        if r["has_estimated_novelty"]:
            stats["estimated_novelty_flags"] += 1

    # Log phase completions
    log_event(RUN_DIR, "refine", "info",
              "Phase 2 complete: auto-strengthen",
              {
                  "total_ideas": stats["total"],
                  "ideas_with_weak_dims": stats["ideas_with_weak_dims"],
                  "ideas_strengthened": stats["ideas_strengthened"],
                  "refinements_accepted": stats["refinements_accepted"],
                  "refinements_discarded": stats["refinements_discarded"],
              })

    log_event(RUN_DIR, "refine", "info",
              "Phase 4 complete: proposals assembled",
              {
                  "proposals_written": stats["proposals_written"],
                  "minimal_fallbacks": stats["minimal_fallbacks"],
              })

    # ── Print summary ─────────────────────────────────────────────────────────
    print("\n\n" + "=" * 70)
    print("BATCH 15 SUMMARY")
    print("=" * 70)
    print(f"Total ideas processed:         {stats['total']}")
    print(f"Ideas with weak dimensions:    {stats['ideas_with_weak_dims']}")
    print(f"Ideas strengthened (≥1 accept):{stats['ideas_strengthened']}")
    print(f"Refinements accepted:          {stats['refinements_accepted']}")
    print(f"Refinements discarded:         {stats['refinements_discarded']}")
    print(f"Proposals written:             {stats['proposals_written']}")
    print(f"Minimal fallbacks:             {stats['minimal_fallbacks']}")
    print(f"Estimated novelty flags:       {stats['estimated_novelty_flags']}")

    # Score improvements
    improved = [r for r in results if r["score_delta"] > 0.0001]
    print(f"\nScore improvements ({len(improved)} ideas):")
    for r in sorted(improved, key=lambda x: -x["score_delta"]):
        print(f"  {r['idea_id']}: {r['pre_refine_weighted_score']:.3f} → "
              f"{r['post_refine_weighted_score']:.3f} (+{r['score_delta']:.4f})")

    # Estimated novelty
    if stats["estimated_novelty_flags"]:
        est_nov = [r for r in results if r["has_estimated_novelty"]]
        print(f"\nEstimated novelty flags (not re-verified via web search):")
        for r in est_nov:
            print(f"  {r['idea_id']}: {r['title']}")

    # Full proposals listing
    print(f"\nProposals written to: {RUN_DIR}/refine/")
    print(f"\nAll proposals (idea_id | score | novelty | title):")
    for r in results:
        status = "OK  " if r["written"] else "FAIL"
        print(f"  [{status}] {r['idea_id']} | {r['post_refine_weighted_score']:.3f} "
              f"| {r['novelty_classification']:<20} | {r['title'][:55]}")

    print(f"\nDone. Run /rank-ideas next to produce the final ranking.")


if __name__ == "__main__":
    main()
