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
    "why_this_matters",
    "day1_check",
    "approach_outline",
    "scope_and_deliverables",
    "proposed_first_experiments",
    "risks",
    "prerequisites",
    "who_this_is_for",
    "open_questions",
    "scores_rationale",
    "alternative_framings",
    "cited_sources",
]

# Mapping from section key to markdown heading.
_SECTION_HEADINGS = {
    "research_question": "Research Question",
    "why_this_matters": "Why This Matters",
    "day1_check": "Day-1 Check",
    "approach_outline": "Approach",
    "scope_and_deliverables": "Scope and Deliverables",
    "proposed_first_experiments": "Experiments",
    "risks": "Risks",
    "prerequisites": "Prerequisites",
    "who_this_is_for": "Who This Is For",
    "open_questions": "Open Questions",
    "scores_rationale": "Scores and rationale",
    "alternative_framings": "Alternative framings",
    "cited_sources": "Cited sources",
}

# Rendered inside <details> below the visible layer, so the reader decides
# from the sections above them.
_COLLAPSED_KEYS = {"scores_rationale", "alternative_framings", "cited_sources"}

# Sections stored as a list of strings rather than a prose block.
_LIST_KEYS = {
    "proposed_first_experiments",
    "prerequisites",
    "open_questions",
    "alternative_framings",
    "cited_sources",
}

# Headings used before the 2026-08 format change, so existing files still read.
_LEGACY_HEADINGS = {
    "Approach Outline": "approach_outline",
    "Proposed First Experiments": "proposed_first_experiments",
    "Theory of Impact Chain": "why_this_matters",
    "Impact Pathway": "who_this_is_for",
    "Strength Rationale": "scores_rationale",
    "Alternative Framings": "alternative_framings",
    "Cited Sources": "cited_sources",
}

# Fields every entry in the structured ``risks`` section carries.  The shape is
# the enforcement: a risk that cannot say what detects it or what to do about it
# fails to round-trip, so vague filler cannot survive the format.
_RISK_FIELDS = ["consequence", "detected_by", "response"]
_RISK_LABELS = {
    "consequence": "Consequence",
    "detected_by": "Detected by",
    "response": "Response",
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
        weak_dimensions.append(
            {
                "name": name,
                "score": entry.get("score", 0),
                "reasoning": entry.get("reasoning", ""),
                "threshold": crit.refinement_threshold if crit else 3,
            }
        )

    weak_set = set(weak_dims)
    strong_dimensions = []
    for name, entry in scores.items():
        if name not in weak_set:
            strong_dimensions.append(
                {
                    "name": name,
                    "score": entry.get("score", 0),
                }
            )
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
        "tldr": "",
        "pathway": "",
        "named_party": "",
        "sections": {key: _empty_section(key) for key in _SECTION_KEYS},
    }


def _empty_section(key: str) -> str | list:
    """Return the empty value for a section key."""
    return [] if key in _LIST_KEYS or key == "risks" else ""


def _format_risks(risks: list) -> str:
    """Render structured risks as a named block per risk.

    Each risk becomes a bold name followed by its three labelled lines.  A risk
    missing a field renders that line empty rather than dropping it, so the gap
    is visible in the output instead of silently disappearing.
    """
    blocks = []
    for risk in risks:
        if not isinstance(risk, dict):
            blocks.append(str(risk))
            continue
        lines = [f"**{risk.get('name', 'Unnamed risk')}**"]
        lines += [f"- {_RISK_LABELS[f]}: {risk.get(f, '')}" for f in _RISK_FIELDS]
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def _parse_risks(content: str) -> list[dict]:
    """Parse a rendered risks block back into structured entries."""
    risks: list[dict] = []
    label_to_field = {v: k for k, v in _RISK_LABELS.items()}
    for line in content.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        name = re.fullmatch(r"\*\*(.+?)\*\*", line)
        if name:
            risks.append({"name": name.group(1).strip()})
            continue
        item = re.fullmatch(r"-\s*([^:]+):\s*(.*)", line)
        if item and risks:
            field = label_to_field.get(item.group(1).strip())
            if field:
                risks[-1][field] = item.group(2).strip()
    return risks


def _format_section_content(key: str, value: str | list) -> str:
    """Format a section value as a string for markdown output."""
    if key == "risks":
        return _format_risks(value) if isinstance(value, list) else str(value)
    if isinstance(value, list):
        if not value:
            return ""
        return "\n".join(f"- {item}" for item in value)
    return str(value)


def _parse_section_content(key: str, content: str) -> str | list:
    """Parse markdown section content back to the appropriate type."""
    content = content.strip()
    if key == "risks":
        return _parse_risks(content)
    if key in _LIST_KEYS:
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


def render_proposal_body(proposal: dict) -> str:
    """Render a proposal's title, TL;DR and sections as markdown.

    The visible layer runs from the TL;DR to Open Questions.  Everything in
    ``_COLLAPSED_KEYS`` is wrapped in a ``<details>`` block so it sits below the
    fold: it is provenance for a reader who wants it, not part of deciding
    whether the idea is worth taking on.

    Args:
        proposal: Proposal dict with ``title``, ``tldr`` and ``sections``.

    Returns:
        Markdown body string, without YAML frontmatter.
    """
    sections = proposal.get("sections", {})
    parts = [f"# {proposal.get('title') or 'Untitled'}"]

    tldr = (proposal.get("tldr") or "").strip()
    if tldr:
        parts.append(f"**TL;DR:** {tldr}")

    for key in _SECTION_KEYS:
        content = _format_section_content(key, sections.get(key, _empty_section(key))).strip()
        heading = _SECTION_HEADINGS[key]
        if key in _COLLAPSED_KEYS:
            # An empty provenance block is noise; an empty visible section is a
            # gap the reader should see, so only the collapsed ones are dropped.
            if not content:
                continue
            parts.append(
                f"<details>\n<summary><b>{heading}</b></summary>\n\n{content}\n\n</details>"
            )
        else:
            parts.append(f"## {heading}\n\n{content}")

    return "\n\n".join(parts) + "\n"


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

    frontmatter_str = yaml.safe_dump(frontmatter, default_flow_style=False, sort_keys=False)
    body_str = render_proposal_body(proposal)

    with open(file_path, "w") as f:
        f.write(f"---\n{frontmatter_str}---\n\n{body_str}")

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

    # Pull the TL;DR out of the title block before splitting on headings.
    tldr = re.search(r"^\*\*TL;DR:\*\*\s*(.+)$", body, re.MULTILINE)
    if tldr:
        proposal.setdefault("tldr", tldr.group(1).strip())

    # Strip the collapse wrappers so the parser sees plain headings.  Legacy
    # files have none, which is why the same path reads both formats.
    body = re.sub(r"</?details>\n?", "", body)
    body = re.sub(r"<summary><b>(.+?)</b></summary>", r"## \1", body)

    # Split on headings, accepting the current "##" and the legacy "#".
    parts = re.compile(r"^#{1,2} (.+)$", re.MULTILINE).split(body)

    # parts[0] is text before first heading (usually empty)
    # Then alternating: heading_text, content, heading_text, content, ...
    heading_to_key = {v: k for k, v in _SECTION_HEADINGS.items()}
    heading_to_key.update(_LEGACY_HEADINGS)
    sections = {}
    for i in range(1, len(parts), 2):
        heading_text = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""
        key = heading_to_key.get(heading_text)
        if key:
            sections[key] = _parse_section_content(key, content)

    # Ensure all section keys exist
    for key in _SECTION_KEYS:
        sections.setdefault(key, _empty_section(key))

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
