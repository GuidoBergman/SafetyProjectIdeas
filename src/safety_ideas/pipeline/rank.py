"""Rank stage: re-score, rank, format, and persist final proposals."""

import copy
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

import yaml

from safety_ideas.config.schemas import ScoringCriteria, TeamProfile
from safety_ideas.constants import IDEAS_DIR, OUTPUT_DIR
from safety_ideas.pipeline.filter_score import apply_weights


def rank_proposals(
    proposals: list[dict],
    criteria: list[ScoringCriteria],
    team_profile: TeamProfile,
) -> list[dict]:
    """Re-score proposals using apply_weights and sort descending by weighted_score.

    For each proposal, compute weighted_score from its 'scores' dict (re-using
    filter_score.apply_weights).  If proposal has no 'scores' dict, use
    'original_scores' converted to the expected format.  Also include novelty
    score from novelty_score field in the scores if present.

    Sort by weighted_score descending.  Add 'rank' field (1-based).

    Returns:
        Sorted list with rank and weighted_score fields added.
    """
    proposals = [copy.deepcopy(p) for p in proposals]

    for proposal in proposals:
        scores = proposal.get("scores")

        if not scores:
            # Convert original_scores (name -> int) to apply_weights format
            original = proposal.get("original_scores", {})
            scores = {
                name: {"score": val, "reasoning": "", "confidence": 0.0}
                for name, val in original.items()
            }

        # Include novelty score if present and not already in scores
        novelty_score = proposal.get("novelty_score")
        if novelty_score is not None and "novelty" not in scores:
            scores["novelty"] = {
                "score": novelty_score,
                "reasoning": "From novelty assessment",
                "confidence": 0.0,
            }

        proposal["weighted_score"] = apply_weights(scores, criteria, team_profile)

    proposals.sort(key=lambda p: p.get("weighted_score", 0.0), reverse=True)

    for i, proposal in enumerate(proposals, start=1):
        proposal["rank"] = i

    return proposals


def format_ranked_output(ranked: list[dict]) -> str:
    """Generate concise markdown for 20+ proposals scannable by a human.

    Each proposal is ~5-8 lines so a coordinator can scan quickly.

    Args:
        ranked: List of ranked proposal dicts (must have 'rank' field).

    Returns:
        Markdown string with all ranked proposals.
    """
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Ranked Research Proposals",
        "",
        f"*Generated: {now}*",
        f"*Total proposals: {len(ranked)}*",
        "",
        "---",
    ]

    for proposal in ranked:
        rank = proposal.get("rank", "?")
        title = proposal.get("title", "Untitled")
        score = proposal.get("weighted_score", 0.0)

        sections = proposal.get("sections", {})
        research_question = sections.get("research_question", "")
        if not research_question:
            # Fall back to first line of any content
            research_question = title

        approach = sections.get("approach_outline", "")
        if len(approach) > 150:
            approach = approach[:147] + "..."

        subfield = proposal.get("subfield", "N/A")
        strategy = proposal.get("generation_strategy", "N/A")
        novelty_class = proposal.get("novelty_classification", "N/A")

        # Format scores line — prefer re-scored 'scores' dict, fall back to original_scores
        scores_dict = proposal.get("scores")
        if scores_dict and isinstance(next(iter(scores_dict.values()), None), dict):
            scores_parts = [f"{k}: {v.get('score', '?')}" for k, v in scores_dict.items()]
        else:
            original_scores = proposal.get("original_scores", {})
            scores_parts = [f"{k}: {v}" for k, v in original_scores.items()]
        scores_line = ", ".join(scores_parts) if scores_parts else "N/A"

        # Provenance
        prov = proposal.get("provenance", {})
        gen_method = prov.get("generation_method", "N/A")
        kb_count = len(prov.get("kb_sources", []))
        web_count = len(prov.get("web_sources", []))

        lines.append("")
        lines.append(f"## #{rank}: {title} (Score: {score:.2f})")
        lines.append("")
        lines.append(f"**Research Question:** {research_question}")
        lines.append(f"**Approach:** {approach}")
        lines.append(
            f"**Subfield:** {subfield} | **Strategy:** {strategy} | **Novelty:** {novelty_class}"
        )
        lines.append(f"**Scores:** {scores_line}")
        lines.append(f"**Provenance:** {gen_method}, sources: {kb_count} KB, {web_count} web")
        lines.append("")
        lines.append("---")

    return "\n".join(lines) + "\n"


def persist_ideas(ranked: list[dict], ideas_dir: Path | None = None) -> list[Path]:
    """Copy final proposals to data/ideas/ for persistent accumulation.

    Each proposal is written as <idea_id>.md with YAML frontmatter and markdown
    body sections.

    Args:
        ranked: List of ranked proposal dicts.
        ideas_dir: Target directory. Uses IDEAS_DIR from constants if not provided.

    Returns:
        List of written file paths.
    """
    target = ideas_dir or IDEAS_DIR
    target.mkdir(parents=True, exist_ok=True)

    written = []
    for proposal in ranked:
        idea_id = proposal.get("idea_id", "unknown")

        # Build frontmatter metadata
        meta = {
            "idea_id": idea_id,
            "run_id": proposal.get("run_id", "unknown"),
            "stage": "rank",
            "rank": proposal.get("rank"),
            "weighted_score": round(proposal.get("weighted_score", 0.0), 4),
            "title": proposal.get("title", ""),
            "subfield": proposal.get("subfield", ""),
            "generation_strategy": proposal.get("generation_strategy", ""),
            "novelty_classification": proposal.get("novelty_classification", ""),
            "novelty_score": proposal.get("novelty_score"),
            "original_scores": proposal.get("original_scores", {}),
            "provenance": proposal.get("provenance", {}),
            "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }

        # Build markdown body from sections
        sections = proposal.get("sections", {})
        body_parts = []
        for section_name, content in sections.items():
            if isinstance(content, list):
                content = "\n".join(f"- {item}" for item in content)
            heading = section_name.replace("_", " ").title()
            body_parts.append(f"# {heading}\n\n{content}")

        frontmatter = yaml.safe_dump(meta, default_flow_style=False, sort_keys=False)
        body = "\n\n".join(body_parts)

        file_path = target / f"{idea_id}.md"
        with open(file_path, "w") as f:
            f.write("---\n")
            f.write(frontmatter)
            f.write("---\n\n")
            f.write(f"# {proposal.get('title', 'Untitled')}\n\n")
            f.write(body)
            f.write("\n")

        written.append(file_path)

    return written


def write_ranked_output(
    run_dir: Path,
    ranked: list[dict],
    markdown: str,
) -> Path:
    """Write ranked output to rank/ directory.

    Writes two files:
    - rank/ranked_proposals.md (the markdown string)
    - rank/ranked_proposals.json (the ranked list as JSON)

    Also copies markdown to data/output/ranked_proposals.md.

    Args:
        run_dir: Run directory path.
        ranked: List of ranked proposal dicts.
        markdown: Pre-formatted markdown string.

    Returns:
        Path to the markdown file in the rank/ directory.
    """
    rank_dir = run_dir / "rank"
    rank_dir.mkdir(parents=True, exist_ok=True)

    md_path = rank_dir / "ranked_proposals.md"
    json_path = rank_dir / "ranked_proposals.json"

    with open(md_path, "w") as f:
        f.write(markdown)

    with open(json_path, "w") as f:
        json.dump(ranked, f, indent=2, default=str)

    # Also copy to data/output/
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(md_path, OUTPUT_DIR / "ranked_proposals.md")

    return md_path


def main() -> None:
    """CLI: commands are rank, format, persist, write, read."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.pipeline.rank <command> <run_dir> [args]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "rank":
        run_dir = Path(sys.argv[2])
        from safety_ideas.pipeline.refine import read_refined_proposals

        proposals = read_refined_proposals(run_dir)
        if not proposals:
            print("No refined proposals found in refine/ directory", file=sys.stderr)
            sys.exit(1)
        # Minimal criteria/team for CLI usage
        print(json.dumps(proposals, indent=2, default=str))
    elif cmd == "format":
        data = json.loads(sys.argv[2])
        print(format_ranked_output(data))
    elif cmd == "persist":
        data = json.loads(sys.argv[2])
        paths = persist_ideas(data)
        print(json.dumps([str(p) for p in paths], indent=2))
    elif cmd == "write":
        run_dir = Path(sys.argv[2])
        data = json.loads(sys.argv[3])
        md = sys.argv[4] if len(sys.argv) > 4 else format_ranked_output(data)
        path = write_ranked_output(run_dir, data, md)
        print(path)
    elif cmd == "read":
        run_dir = Path(sys.argv[2])
        rank_dir = run_dir / "rank"
        json_path = rank_dir / "ranked_proposals.json"
        if json_path.exists():
            with open(json_path) as f:
                print(f.read())
        else:
            print("No ranked_proposals.json found", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
