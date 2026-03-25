"""Fix truncated idea files by rebuilding from complete pipeline sources.

Due to a bug where create_batches() did not enrich stage 2+ survivors with
original idea data, the refine stage produced truncated content. This script
rebuilds data/ideas/ files and refine/ markdown from the complete sources:
- generate/<id>.md for the original idea text
- filter_score/scored/<id>.json for complete scoring reasoning

Usage:
    uv run python scripts/fix_truncated_ideas.py <run_dir>
    uv run python scripts/fix_truncated_ideas.py data/runs/2026-03-19T19-58-40
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

from safety_ideas.constants import IDEAS_DIR, OUTPUT_DIR
from safety_ideas.pipeline.generate import read_idea_sketches
from safety_ideas.pipeline.rank import format_ranked_output
from safety_ideas.pipeline.refine import (
    _SECTION_HEADINGS,
    _SECTION_KEYS,
    _format_section_content,
    _parse_proposal_markdown,
    write_refined_proposal,
)


def _parse_generate_body(body: str) -> dict:
    """Extract structured fields from a generate-stage markdown body.

    Returns dict with keys: title, problem, direction, why_it_matters,
    relevant_context.
    """
    result = {}
    title_match = re.match(r"^# (.+)", body)
    if title_match:
        result["title"] = title_match.group(1).strip()

    for field, pattern in [
        ("problem", r"\*\*Problem:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)"),
        ("direction", r"\*\*Direction:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)"),
        ("why_it_matters", r"\*\*Why it matters:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)"),
        ("relevant_context", r"\*\*Relevant context:\*\*\s*(.+?)(?=\n\n|\n\*\*|\Z)"),
    ]:
        match = re.search(pattern, body, re.DOTALL)
        if match:
            result[field] = match.group(1).strip()

    return result


def _build_strength_rationale(scores: dict) -> str:
    """Build strength rationale from complete filter_score scoring reasoning."""
    parts = []
    for name, entry in scores.items():
        if not isinstance(entry, dict):
            continue
        score = entry.get("score", 0)
        reasoning = entry.get("reasoning", "")
        if reasoning:
            parts.append(f"{name} ({score}/5): {reasoning}")
    return "\n\n".join(parts)


def _build_cited_sources(scored: dict, generate_fields: dict) -> list[str]:
    """Build cited sources from filter_score and generate data."""
    sources = []

    # From citation_verification (may be a dict or a list)
    cv = scored.get("citation_verification", {})
    if isinstance(cv, dict):
        citations = cv.get("citations", [])
    else:
        citations = []
    for cite in citations:
        title = cite.get("title", "")
        notes = cite.get("notes", "")
        status = cite.get("status", "")
        if title:
            entry = title
            if notes:
                entry += f" - {notes}"
            elif status:
                entry += f" ({status})"
            sources.append(entry)

    # From novelty_assessment evidence
    if not sources:
        novelty = scored.get("novelty_assessment", {})
        evidence = novelty.get("evidence", [])
        sources.extend(evidence)

    # Fallback to generate-stage relevant context
    if not sources:
        ctx = generate_fields.get("relevant_context", "")
        if ctx:
            for item in re.split(r"\.\s+", ctx):
                item = item.strip().rstrip(".")
                if item:
                    sources.append(item)

    return sources


def fix_idea(
    idea_id: str,
    generate_data: dict,
    scored_path: Path | None,
    refine_proposal: dict | None,
    run_dir: Path,
) -> dict:
    """Rebuild a single idea from complete sources.

    Returns a summary dict with what was fixed.
    """
    changes = []

    # Parse the original generate body
    body = generate_data.get("body", "")
    gen_fields = _parse_generate_body(body)

    # Load scored data if available
    scored = {}
    if scored_path and scored_path.exists():
        with open(scored_path) as f:
            scored = json.load(f)

    # Start from the refine proposal if it exists, otherwise build fresh
    if refine_proposal:
        proposal = dict(refine_proposal)
    else:
        proposal = {
            "idea_id": idea_id,
            "run_id": generate_data.get("run_id", "unknown"),
            "stage": "refine",
            "title": gen_fields.get("title", generate_data.get("title", "")),
            "sections": {},
        }

    sections = proposal.get("sections", {})

    # Fix research_question if it looks malformed
    rq = sections.get("research_question", "")
    if not rq or "Reframed for" in rq or len(rq) < 20:
        problem = gen_fields.get("problem", "")
        if problem:
            sections["research_question"] = problem
            changes.append("research_question")

    # Fix approach_outline if truncated (ends mid-sentence or has refinement text appended)
    ao = sections.get("approach_outline", "")
    if not ao or "Refined:" in ao or "Refine " in ao or (ao and not ao.rstrip().endswith(".")):
        direction = gen_fields.get("direction", "")
        if direction:
            sections["approach_outline"] = direction
            changes.append("approach_outline")

    # Fix theory_of_impact_chain if empty or very short
    tic = sections.get("theory_of_impact_chain", "")
    if not tic or len(tic) < 20:
        wim = gen_fields.get("why_it_matters", "")
        if wim:
            sections["theory_of_impact_chain"] = wim
            changes.append("theory_of_impact_chain")

    # Fix strength_rationale if truncated
    sr = sections.get("strength_rationale", "")
    if not sr or (sr and not sr.rstrip().endswith((".", "!", ")"))):
        scores = scored.get("scores", {})
        if scores:
            sections["strength_rationale"] = _build_strength_rationale(scores)
            changes.append("strength_rationale")

    # Fix cited_sources if empty
    cs = sections.get("cited_sources", [])
    if not cs:
        sections["cited_sources"] = _build_cited_sources(scored, gen_fields)
        if sections["cited_sources"]:
            changes.append("cited_sources")

    # Fix alternative_framings with truncated titles
    af = sections.get("alternative_framings", [])
    if af:
        fixed_af = []
        any_truncated = False
        for framing in af:
            if isinstance(framing, str) and "Evaluati:" in framing:
                any_truncated = True
            fixed_af.append(framing)
        if any_truncated:
            # Can't recover truncated framing titles; clear them rather than
            # keeping garbled text
            sections["alternative_framings"] = []
            changes.append("alternative_framings (cleared truncated)")

    proposal["sections"] = sections
    return {"proposal": proposal, "changes": changes}


def _update_sections_in_dict(idea_dict: dict, fixed_sections: dict) -> bool:
    """Update sections in a JSON idea dict. Returns True if changed."""
    sections = idea_dict.get("sections", {})
    changed = False
    for key, value in fixed_sections.items():
        if sections.get(key) != value:
            sections[key] = value
            changed = True
    return changed


def _fix_ranked_proposals(
    run_dir: Path, fixed_ideas: dict[str, dict]
) -> int:
    """Fix sections in rank/ranked_proposals.json and regenerate .md files.

    Returns count of files updated.
    """
    rank_json = run_dir / "rank" / "ranked_proposals.json"
    if not rank_json.exists():
        return 0

    with open(rank_json) as f:
        ranked = json.load(f)

    any_changed = False
    for proposal in ranked:
        idea_id = proposal.get("idea_id", "")
        if idea_id in fixed_ideas:
            if _update_sections_in_dict(proposal, fixed_ideas[idea_id]):
                any_changed = True

    if not any_changed:
        return 0

    # Write updated JSON
    with open(rank_json, "w") as f:
        json.dump(ranked, f, indent=2, default=str)

    # Regenerate markdown from updated JSON
    md_content = format_ranked_output(ranked)

    rank_md = run_dir / "rank" / "ranked_proposals.md"
    with open(rank_md, "w") as f:
        f.write(md_content)

    # Also update data/output/ copy
    output_md = OUTPUT_DIR / "ranked_proposals.md"
    if output_md.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(output_md, "w") as f:
            f.write(md_content)

    return 3  # json + rank md + output md


def fix_run(run_dir: Path) -> None:
    """Fix all truncated ideas in a pipeline run."""
    run_dir = Path(run_dir)

    # Load all generate-stage ideas
    originals = {i["idea_id"]: i for i in read_idea_sketches(run_dir)}
    if not originals:
        print(f"No generate-stage ideas found in {run_dir}/generate/", file=sys.stderr)
        sys.exit(1)

    # Load existing refine proposals
    refine_dir = run_dir / "refine"
    refine_proposals = {}
    if refine_dir.exists():
        for md_file in refine_dir.glob("*.md"):
            text = md_file.read_text()
            proposal = _parse_proposal_markdown(text)
            if proposal:
                refine_proposals[proposal["idea_id"]] = proposal

    scored_dir = run_dir / "filter_score" / "scored"
    total_fixed = 0
    total_unchanged = 0
    # Collect fixed sections keyed by idea_id for batch updates
    fixed_ideas: dict[str, dict] = {}

    for idea_id, gen_data in sorted(originals.items()):
        scored_path = scored_dir / f"{idea_id}.json" if scored_dir.exists() else None
        refine_proposal = refine_proposals.get(idea_id)

        # Skip ideas that weren't refined (eliminated earlier)
        if not refine_proposal and not (scored_path and scored_path.exists()):
            continue

        result = fix_idea(idea_id, gen_data, scored_path, refine_proposal, run_dir)
        changes = result["changes"]
        proposal = result["proposal"]

        if not changes:
            total_unchanged += 1
            continue

        total_fixed += 1
        fixed_ideas[idea_id] = proposal["sections"]
        print(f"  {idea_id}: fixed {', '.join(changes)}")

        # Write back to refine directory (.md files)
        if refine_proposal:
            write_refined_proposal(run_dir, proposal)

        # Write back to data/ideas/ if the file exists there
        ideas_file = IDEAS_DIR / f"{idea_id}.md"
        if ideas_file.exists():
            _write_ideas_file(ideas_file, proposal)

    print(f"\n  Ideas: {total_fixed} fixed, {total_unchanged} unchanged")

    # For batch/ranked updates, use ALL current refine proposal sections
    # (not just newly fixed ones) since prior runs may have fixed refine MDs
    # without updating these files.
    all_sections: dict[str, dict] = {}
    if refine_dir.exists():
        for md_file in refine_dir.glob("*.md"):
            text = md_file.read_text()
            proposal = _parse_proposal_markdown(text)
            if proposal:
                all_sections[proposal["idea_id"]] = proposal.get("sections", {})

    if all_sections:
        rank_count = _fix_ranked_proposals(run_dir, all_sections)
        print(f"  Ranked proposals: {rank_count} files updated")

    print("\nDone.")


def _write_ideas_file(file_path: Path, proposal: dict) -> None:
    """Write a proposal to data/ideas/ in the same format as rank.persist_ideas."""
    sections = proposal.get("sections", {})

    # Build frontmatter from proposal metadata (exclude sections)
    meta = {k: v for k, v in proposal.items() if k != "sections"}

    # Build markdown body from sections
    body_parts = []
    for key in _SECTION_KEYS:
        heading = _SECTION_HEADINGS[key]
        content = _format_section_content(sections.get(key, ""))
        body_parts.append(f"# {heading}\n\n{content}")

    frontmatter = yaml.safe_dump(meta, default_flow_style=False, sort_keys=False)
    body = "\n\n".join(body_parts)

    title = proposal.get("title", "Untitled")
    with open(file_path, "w") as f:
        f.write("---\n")
        f.write(frontmatter)
        f.write("---\n\n")
        f.write(f"# {title}\n\n")
        f.write(body)
        f.write("\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run python scripts/fix_truncated_ideas.py <run_dir>")
        print("Example: uv run python scripts/fix_truncated_ideas.py data/runs/2026-03-19T19-58-40")
        sys.exit(1)

    run_path = Path(sys.argv[1])
    if not run_path.exists():
        print(f"Run directory not found: {run_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Fixing truncated ideas in {run_path}...")
    fix_run(run_path)
