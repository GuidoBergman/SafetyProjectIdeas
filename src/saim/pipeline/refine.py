"""Refine stage: identify weak dimensions, build refinement context, and proposal I/O.

After scoring and filtering, the refine stage prepares ideas for LLM-driven
improvement by identifying weak scoring dimensions, building context for
targeted refinement, and structuring full proposal skeletons.  Proposals are
persisted as markdown files with YAML frontmatter.
"""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path

import yaml

from saim.config.schemas import ScoringCriteria

# Section keys in the order they appear in proposal markdown.
_SECTION_KEYS = [
    "research_question",
    "approach_outline",
    "proposed_first_experiments",
    "theory_of_impact_chain",
    "strength_rationale",
    "alternative_framings",
    "cited_sources",
]

# Mapping from section key to markdown heading.
_SECTION_HEADINGS = {
    "research_question": "Research Question",
    "approach_outline": "Approach Outline",
    "proposed_first_experiments": "Proposed First Experiments",
    "theory_of_impact_chain": "Theory of Impact Chain",
    "strength_rationale": "Strength Rationale",
    "alternative_framings": "Alternative Framings",
    "cited_sources": "Cited Sources",
}


def identify_weak_dimensions(
    scored_idea: dict,
    criteria: list[ScoringCriteria],
    active_weights: dict[str, float] | None = None,
) -> list[str]:
    """Find criteria scoring below their refinement threshold.

    Only criteria whose current weight is non-zero are considered.  The
    effective weight for each criterion is looked up in *active_weights*
    first (team overrides), falling back to ``default_weight``.

    Args:
        scored_idea: Scored idea dict with a ``scores`` mapping of
            criterion_name -> {score, reasoning, confidence}.
        criteria: List of ScoringCriteria objects from config.
        active_weights: Optional mapping of criterion name to effective
            weight (e.g. from team profile overrides).  When ``None``,
            ``default_weight`` from each criterion is used.

    Returns:
        List of criterion names that are below their refinement threshold,
        sorted by score ascending.  Criteria with zero effective weight
        are skipped.
    """
    scores = scored_idea.get("scores", {})
    criteria_by_name = {c.name: c for c in criteria}

    weak = []
    for name, crit in criteria_by_name.items():
        weight = (active_weights or {}).get(name, crit.default_weight)
        if weight == 0:
            continue
        entry = scores.get(name)
        if entry is None:
            continue
        score_val = entry.get("score", 0)
        if score_val < crit.refinement_threshold:
            weak.append((name, score_val))

    weak.sort(key=lambda x: x[1])
    return [name for name, _ in weak]


def analyze_weaknesses(
    scored_idea: dict,
    criteria: list[ScoringCriteria],
    active_weights: dict[str, float] | None = None,
) -> dict:
    """Identify weak dimensions and build refinement context in one step.

    Combines weak-dimension identification (threshold-based) with context
    assembly for LLM refinement.

    Args:
        scored_idea: Scored idea dict.
        criteria: List of ScoringCriteria objects from config.
        active_weights: Optional mapping of criterion name to effective
            weight (e.g. from team profile overrides).

    Returns:
        Dict with keys: idea_id, title, original_body, weak_dimensions,
        strong_dimensions, novelty_classification.
    """
    weak_dims = identify_weak_dimensions(scored_idea, criteria, active_weights)

    scores = scored_idea.get("scores", {})
    original = scored_idea.get("original_idea", {})
    novelty = scored_idea.get("novelty_assessment", {})

    criteria_by_name = {c.name: c for c in criteria}

    weak_dimensions = []
    for name in weak_dims:
        entry = scores.get(name, {})
        crit = criteria_by_name.get(name)
        weak_dimensions.append({
            "name": name,
            "score": entry.get("score", 0),
            "reasoning": entry.get("reasoning", ""),
            "threshold": crit.refinement_threshold if crit else 3,
        })

    weak_set = set(weak_dims)
    strong_dimensions = []
    for name, entry in scores.items():
        if name not in weak_set:
            strong_dimensions.append({
                "name": name,
                "score": entry.get("score", 0),
            })
    strong_dimensions.sort(key=lambda x: x["score"], reverse=True)

    # original_idea may be a dict or a plain string (the idea body text)
    if isinstance(original, dict):
        original_body = original.get("body", "")
    else:
        original_body = str(original) if original else ""

    return {
        "idea_id": scored_idea.get("idea_id", "unknown"),
        "title": scored_idea.get("title", ""),
        "original_body": original_body,
        "weak_dimensions": weak_dimensions,
        "strong_dimensions": strong_dimensions,
        "novelty_classification": novelty.get("classification", ""),
    }


def build_proposal_skeleton(scored_idea: dict, refinement: dict) -> dict:
    """Structure a full proposal dict from a scored idea and refinement context.

    The skeleton contains all metadata fields (written as YAML frontmatter)
    and empty section placeholders (written as markdown body).

    Args:
        scored_idea: Scored idea dict.
        refinement: Refinement context dict (from ``analyze_weaknesses``).

    Returns:
        Full proposal dict ready for LLM completion and persistence.
    """
    now = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    original = scored_idea.get("original_idea", {})
    scores = scored_idea.get("scores", {})
    novelty = scored_idea.get("novelty_assessment", {})

    original_scores = {}
    for name, entry in scores.items():
        original_scores[name] = entry.get("score", 0)

    weak_addressed = [d["name"] for d in refinement.get("weak_dimensions", [])]

    # original_idea may be a dict or a plain string
    if isinstance(original, dict):
        gen_strategy = original.get("generation_strategy", "")
        subfield = original.get("subfield", "")
        orig_run_id = original.get("run_id", "")
    else:
        gen_strategy = ""
        subfield = ""
        orig_run_id = ""

    # run_id may be at top level or nested in original_idea
    run_id = scored_idea.get("run_id") or orig_run_id or "unknown"

    return {
        "idea_id": scored_idea.get("idea_id", "unknown"),
        "run_id": run_id,
        "stage": "refine",
        "timestamp": now,
        "title": scored_idea.get("title", ""),
        "original_scores": original_scores,
        "novelty_classification": novelty.get("classification", ""),
        "novelty_score": novelty.get("derived_score", 0),
        "novelty_method": scored_idea.get("novelty_method"),
        "pre_refine_weighted_score": scored_idea.get("weighted_score", 0.0),
        "weak_dimensions_addressed": weak_addressed,
        "num_alternative_framings": 0,
        "generation_strategy": gen_strategy,
        "subfield": subfield,
        "provenance": {
            "generation_method": gen_strategy,
            "kb_sources": [],
            "web_sources": [],
        },
        "refinement_confidence": 0.0,
        "sections": {
            "research_question": "",
            "approach_outline": "",
            "proposed_first_experiments": "",
            "theory_of_impact_chain": "",
            "strength_rationale": "",
            "alternative_framings": [],
            "cited_sources": [],
        },
    }


def _format_section_content(value: str | list) -> str:
    """Format a section value as a string for markdown output."""
    if isinstance(value, list):
        if not value:
            return ""
        return "\n".join(f"- {item}" for item in value)
    return str(value)


def _parse_section_content(key: str, content: str) -> str | list:
    """Parse markdown section content back to the appropriate type."""
    content = content.strip()
    if key in ("alternative_framings", "cited_sources"):
        if not content:
            return []
        items = []
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("- "):
                items.append(line[2:].strip())
            elif line:
                items.append(line)
        return items
    return content


def write_refined_proposal(run_dir: Path, proposal: dict) -> Path:
    """Write a proposal as a markdown file with YAML frontmatter.

    The file is stored at ``<run_dir>/refine/<idea_id>.md``.

    Frontmatter contains all proposal keys except ``sections``.
    The body contains each section as a markdown heading followed by content.

    Args:
        run_dir: Run directory path.
        proposal: Proposal dict (from ``build_proposal_skeleton``).

    Returns:
        Path to the written markdown file.
    """
    refine_dir = run_dir / "refine"
    refine_dir.mkdir(parents=True, exist_ok=True)

    idea_id = proposal.get("idea_id", "unknown")
    file_path = refine_dir / f"{idea_id}.md"

    # Build frontmatter from all keys except sections
    frontmatter = {k: v for k, v in proposal.items() if k != "sections"}

    # Build markdown body from sections
    sections = proposal.get("sections", {})
    body_parts = []
    for key in _SECTION_KEYS:
        heading = _SECTION_HEADINGS[key]
        content = _format_section_content(sections.get(key, ""))
        body_parts.append(f"# {heading}\n\n{content}\n")

    frontmatter_str = yaml.safe_dump(frontmatter, default_flow_style=False, sort_keys=False)
    body_str = "\n".join(body_parts)

    with open(file_path, "w") as f:
        f.write(f"---\n{frontmatter_str}---\n\n{body_str}\n")

    return file_path


def read_refined_proposals(run_dir: Path) -> list[dict]:
    """Read all refined proposal markdown files from refine/.

    Parses YAML frontmatter and markdown body back into proposal dicts.

    Args:
        run_dir: Run directory path.

    Returns:
        List of proposal dicts, sorted by idea_id.
    """
    refine_dir = run_dir / "refine"
    if not refine_dir.exists():
        return []

    results = []
    for md_file in sorted(refine_dir.glob("*.md")):
        text = md_file.read_text()
        proposal = _parse_proposal_markdown(text)
        if proposal:
            results.append(proposal)

    results.sort(key=lambda x: x.get("idea_id", ""))
    return results


def _parse_proposal_markdown(text: str) -> dict | None:
    """Parse a proposal markdown file into a dict.

    Args:
        text: Full file content with YAML frontmatter and markdown body.

    Returns:
        Proposal dict, or None if parsing fails.
    """
    # Split frontmatter from body
    match = re.match(r"^---\n(.*?\n)---\n\n?(.*)", text, re.DOTALL)
    if not match:
        return None

    frontmatter_str, body = match.groups()
    proposal = yaml.safe_load(frontmatter_str)
    if not isinstance(proposal, dict):
        return None

    # Parse sections from markdown body
    sections = {}
    # Split on heading pattern
    heading_pattern = re.compile(r"^# (.+)$", re.MULTILINE)
    parts = heading_pattern.split(body)

    # parts[0] is text before first heading (usually empty)
    # Then alternating: heading_text, content, heading_text, content, ...
    heading_to_key = {v: k for k, v in _SECTION_HEADINGS.items()}
    for i in range(1, len(parts), 2):
        heading_text = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        key = heading_to_key.get(heading_text)
        if key:
            sections[key] = _parse_section_content(key, content)

    # Ensure all section keys exist
    for key in _SECTION_KEYS:
        if key not in sections:
            if key in ("alternative_framings", "cited_sources"):
                sections[key] = []
            else:
                sections[key] = ""

    proposal["sections"] = sections
    return proposal


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m saim.pipeline.refine <command> <run_dir> [args]")
        print("Commands: analyze-weaknesses, build-skeleton, write, read, list")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "analyze-weaknesses":
        scored_data = json.loads(sys.argv[2])
        criteria_data = json.loads(sys.argv[3])
        criteria = [ScoringCriteria(**c) for c in criteria_data]
        active_weights = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
        ctx = analyze_weaknesses(scored_data, criteria, active_weights)
        print(json.dumps(ctx, indent=2, default=str))
    elif cmd == "build-skeleton":
        scored_data = json.loads(sys.argv[2])
        refinement_data = json.loads(sys.argv[3])
        skeleton = build_proposal_skeleton(scored_data, refinement_data)
        print(json.dumps(skeleton, indent=2, default=str))
    elif cmd == "write":
        run_dir = Path(sys.argv[2])
        proposal_data = json.loads(sys.argv[3])
        path = write_refined_proposal(run_dir, proposal_data)
        print(path)
    elif cmd == "read":
        run_dir = Path(sys.argv[2])
        proposals = read_refined_proposals(run_dir)
        print(json.dumps(proposals, indent=2, default=str))
    elif cmd == "list":
        run_dir = Path(sys.argv[2])
        refine_dir = run_dir / "refine"
        if refine_dir.exists():
            for f in sorted(refine_dir.glob("*.md")):
                print(f)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
