#!/usr/bin/env python3
"""Generate a markdown report of all surviving scored ideas, split by novelty assessment status."""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

import yaml


NOT_ASSESSED = {"not_assessed", "", None}


def find_latest_run() -> Path:
    runs = sorted(Path("data/runs").iterdir())
    if not runs:
        raise FileNotFoundError("No runs found in data/runs/")
    return runs[-1]


def parse_generate_md(path: Path) -> dict:
    """Parse a generate markdown file into frontmatter dict + body sections."""
    text = path.read_text(encoding="utf-8")
    # Split frontmatter
    parts = text.split("---", 2)
    frontmatter = {}
    body = text
    if len(parts) >= 3:
        try:
            frontmatter = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            pass
        body = parts[2].strip()

    # Remove the H1 title line (we use the scored title instead)
    body = re.sub(r"^# .+\n?", "", body).strip()

    return {"frontmatter": frontmatter, "body": body}


def render_idea(rank: int, scored: dict, generate: dict) -> str:
    """Render a single idea as a markdown section."""
    fm = generate["frontmatter"]
    body = generate["body"]

    novelty = scored.get("novelty_assessment", {})
    novelty_label = novelty.get("label") or novelty.get("classification") or "not_assessed"
    novelty_score = novelty.get("score") or novelty.get("derived_score")
    is_assessed = novelty_label not in NOT_ASSESSED

    weighted = scored.get("weighted_score", 0.0)
    conf = scored.get("confidence", 0.0)
    title = scored.get("title", fm.get("title", scored["idea_id"]))
    subfield = fm.get("subfield", "")
    strategy = fm.get("generation_strategy", "")

    lines = []

    # Header
    novelty_tag = f" | novelty: {novelty_label} ({novelty_score}/5)" if is_assessed else ""
    lines.append(f"### {rank}. [{weighted:.2f} | conf {conf:.2f}{novelty_tag}] {title}")
    lines.append("")

    if subfield:
        lines.append(f"**Subfield:** {subfield}")
    if strategy:
        lines.append(f"**Strategy:** {strategy}")
    lines.append(f"**ID:** {scored['idea_id']}")
    lines.append("")

    # Full idea body (Problem, Direction, Why it matters, Relevant context)
    lines.append(body)
    lines.append("")

    # Scores table
    scores = scored.get("scores", {})
    if scores:
        lines.append("#### Scores")
        lines.append("")
        lines.append("| Criterion | Score | Reasoning | Confidence |")
        lines.append("|-----------|-------|-----------|------------|")
        criteria_order = ["theory_of_impact", "accessible_complexity", "narrow_scope", "novelty"]
        for crit in criteria_order:
            if crit not in scores:
                continue
            s = scores[crit]
            reasoning = s.get("reasoning", "").replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {crit} | {s.get('score', '')} | {reasoning} | {s.get('confidence', '')} |")
        lines.append(f"| **weighted total** | **{weighted:.2f}** | | {conf:.2f} |")
        lines.append("")

    # Novelty assessment (assessed ideas only)
    if is_assessed:
        lines.append("#### Novelty Assessment")
        lines.append("")
        lines.append(f"**Classification:** {novelty_label}")
        reasoning = novelty.get("reasoning", "")
        if reasoning:
            lines.append(f"**Reasoning:** {reasoning}")
        existing = novelty.get("existing_work", []) or novelty.get("evidence", [])
        if existing:
            lines.append("**Existing work:**")
            for item in existing:
                if isinstance(item, dict):
                    lines.append(f"- {item.get('title', '')} — {item.get('summary', '')}")
                else:
                    lines.append(f"- {item}")
        lines.append("")

        # Citation verification
        cit_ver = scored.get("citation_verification", {})
        if isinstance(cit_ver, dict) and cit_ver:
            lines.append("#### Citation Verification")
            lines.append("")
            for cit_title, c in cit_ver.items():
                if not isinstance(c, dict):
                    continue
                status = c.get("status", "unknown")
                icon = {"verified": "✅", "corrected": "⚠️", "removed": "❌"}.get(status, "•")
                relevance = c.get("relevance_score", "")
                details = c.get("details", c.get("notes", "")).replace("\n", " ")
                lines.append(f"- {icon} **{status}** (relevance {relevance}) {cit_title} — {details}")
            lines.append("")
        elif isinstance(cit_ver, list) and cit_ver:
            lines.append("#### Citation Verification")
            lines.append("")
            for c in cit_ver:
                if not isinstance(c, dict):
                    continue
                status = c.get("status", "unknown")
                icon = {"verified": "✅", "corrected": "⚠️", "removed": "❌"}.get(status, "•")
                cit_title = c.get("title", "")
                label = c.get("relevance_label", "")
                notes = c.get("notes", c.get("details", "")).replace("\n", " ")
                lines.append(f"- {icon} **{status}** {cit_title} — {label} — {notes}")
            lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate scored ideas markdown report")
    parser.add_argument("--run-dir", type=Path, default=None, help="Run directory (default: latest)")
    args = parser.parse_args()

    run_dir = args.run_dir or find_latest_run()
    scored_dir = run_dir / "filter_score" / "scored"
    generate_dir = run_dir / "generate"
    output_path = run_dir / "filter_score" / "scored_ideas_report.md"

    print(f"Run: {run_dir.name}")
    print(f"Reading scored ideas from {scored_dir}...")

    # Load all scored ideas
    scored_files = sorted(scored_dir.glob("*.json"))
    survivors = []
    for f in scored_files:
        data = json.loads(f.read_text())
        if not data.get("eliminated", False):
            survivors.append(data)

    print(f"  Survivors: {len(survivors)}")

    # Split by novelty
    assessed = []
    not_assessed = []
    for idea in survivors:
        novelty = idea.get("novelty_assessment", {})
        label = novelty.get("label") or novelty.get("classification") or "not_assessed"
        if label not in NOT_ASSESSED:
            assessed.append(idea)
        else:
            not_assessed.append(idea)

    assessed.sort(key=lambda x: x.get("weighted_score", 0), reverse=True)
    not_assessed.sort(key=lambda x: x.get("weighted_score", 0), reverse=True)

    print(f"  Novelty assessed: {len(assessed)} | Not assessed: {len(not_assessed)}")

    # Build report
    lines = []
    lines.append("# Scored Ideas Report")
    lines.append("")
    lines.append(f"**Run:** {run_dir.name}  ")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}  ")
    lines.append(
        f"**Total survivors:** {len(survivors)} | "
        f"**Novelty assessed:** {len(assessed)} | "
        f"**Not assessed:** {len(not_assessed)}"
    )
    lines.append("")
    lines.append("---")
    lines.append("")

    def render_section(title: str, ideas: list) -> list:
        section = []
        section.append(f"## {title} ({len(ideas)} ideas)")
        section.append("")
        for rank, idea in enumerate(ideas, 1):
            idea_id = idea["idea_id"]
            md_path = generate_dir / f"{idea_id}.md"
            if md_path.exists():
                generate = parse_generate_md(md_path)
            else:
                generate = {"frontmatter": {}, "body": "*(generate file not found)*"}
            section.append(render_idea(rank, idea, generate))
        return section

    lines.extend(render_section("Part 1: Novelty Assessed", assessed))
    lines.extend(render_section("Part 2: Novelty Not Assessed", not_assessed))

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nReport written to: {output_path}")
    print(f"  Size: {output_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
