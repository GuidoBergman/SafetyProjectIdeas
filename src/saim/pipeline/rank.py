"""Rank stage: re-score, rank, format, and persist final proposals."""

import copy
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

import yaml

from saim.config.schemas import ScoringCriteria, TeamProfile
from saim.constants import IDEAS_DIR, OUTPUT_DIR
from saim.pipeline.filter_score import apply_weights


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


def _scores_for_weighting(proposal: dict) -> dict:
    """Build an apply_weights-compatible scores dict from a proposal.

    Uses the proposal's ``scores`` dict if present, otherwise reconstructs one
    from ``original_scores`` (name -> int).  Mirrors the logic in
    ``rank_proposals`` so re-ranking stays consistent with first-pass ranking.
    """
    scores = proposal.get("scores")
    if not scores:
        original = proposal.get("original_scores", {})
        scores = {
            name: {"score": val, "reasoning": "", "confidence": 0.0}
            for name, val in original.items()
        }
    novelty_score = proposal.get("novelty_score")
    if novelty_score is not None and "novelty" not in scores:
        scores["novelty"] = {
            "score": novelty_score,
            "reasoning": "From novelty assessment",
            "confidence": 0.0,
        }
    return scores


def _apply_novelty_update(proposal: dict, update: dict) -> None:
    """Write a calculated novelty assessment onto a proposal in place."""
    classification = update["classification"]
    derived = update.get("derived_score")
    confidence = update.get("confidence", 0.0)
    reasoning = update.get("reasoning", "")

    proposal["novelty_classification"] = classification
    proposal["novelty_score"] = derived
    proposal["novelty_method"] = "novelty_assessed"
    proposal["novelty_evidence"] = update.get("evidence", [])

    # Reconstruct a full scores dict from original_scores when absent so the
    # novelty update never drops the other criteria.
    scores = proposal.get("scores")
    if not isinstance(scores, dict) or not scores:
        original = proposal.get("original_scores", {})
        scores = {
            name: {"score": val, "reasoning": "", "confidence": 0.0}
            for name, val in original.items()
        }
    scores["novelty"] = {
        "score": derived,
        "reasoning": reasoning,
        "confidence": confidence,
    }
    proposal["scores"] = scores

    original_scores = proposal.get("original_scores")
    if isinstance(original_scores, dict):
        original_scores["novelty"] = derived


def rerank_with_novelty(
    run_dir: Path,
    updates: dict[str, dict],
    top_n: int,
    criteria: list[ScoringCriteria],
    team_profile: TeamProfile,
    persist: bool = False,
    ideas_dir: Path | None = None,
) -> dict:
    """Re-rank the top-N proposals after a calculated-novelty pass (rank #2).

    Reads the rank #1 output (``rank/ranked_proposals.json``), applies the
    calculated novelty ``updates`` to the top-``top_n`` proposals, drops any whose
    final classification is ``already_solved`` (the novelty hard gate), recomputes
    their weighted scores with the real novelty, and re-sorts **only** that top
    block.  The remaining proposals (ranked below the cutoff) keep their estimated
    novelty and original order and are appended underneath.  The merged list is
    re-numbered and written back over ``rank/ranked_proposals.{json,md}``.

    The original rank #1 ordering is preserved once at
    ``rank/ranked_proposals.rank1.json`` (written only if it does not yet exist,
    so repeated re-runs never clobber the true first ranking).

    Args:
        run_dir: Run directory containing ``rank/ranked_proposals.json``.
        updates: Mapping of idea_id -> novelty update dict with keys
            ``classification``, ``derived_score``, ``confidence``, ``reasoning``,
            ``evidence``, and optional ``eliminated``.
        top_n: Number of top-ranked proposals to re-assess and re-rank.
        criteria: Scoring criteria (for weighted-score recomputation).
        team_profile: Team profile (for weight overrides).
        persist: When True, persist the assessed top survivors to ``ideas_dir``.
        ideas_dir: Override for the persist target (defaults to IDEAS_DIR).

    Returns:
        Dict of counts: assessed, eliminated, survivors_top, rest, total, persisted.
    """
    rank_dir = run_dir / "rank"
    ranked_path = rank_dir / "ranked_proposals.json"
    if not ranked_path.exists():
        raise FileNotFoundError(f"No rank #1 output found at {ranked_path}")

    with open(ranked_path) as f:
        proposals = json.load(f)

    # Preserve the original rank #1 ordering exactly once.
    backup_path = rank_dir / "ranked_proposals.rank1.json"
    if not backup_path.exists():
        with open(backup_path, "w") as f:
            json.dump(proposals, f, indent=2, default=str)

    proposals.sort(key=lambda p: p.get("rank", len(proposals) + 1))
    top = proposals[:top_n]
    rest = proposals[top_n:]

    assessed = 0
    eliminated = 0
    survivors_top: list[dict] = []
    for proposal in top:
        update = updates.get(proposal.get("idea_id", ""))
        if update is None:
            # No calculated novelty for this one — keep as-is in the top block.
            survivors_top.append(proposal)
            continue

        assessed += 1
        gated = update.get("eliminated") or update.get("classification") == "already_solved"
        _apply_novelty_update(proposal, update)
        if gated:
            eliminated += 1
            continue

        proposal["weighted_score"] = apply_weights(
            _scores_for_weighting(proposal), criteria, team_profile
        )
        survivors_top.append(proposal)

    survivors_top.sort(key=lambda p: p.get("weighted_score", 0.0), reverse=True)

    final = survivors_top + rest
    for i, proposal in enumerate(final, start=1):
        proposal["rank"] = i

    write_ranked_output(run_dir, final, format_ranked_output(final))

    persisted = 0
    if persist:
        # Only the freshly-assessed survivors are eligible (persist_ideas also
        # guards on novelty_method, so estimated-only `rest` is never written).
        persisted = len(persist_ideas(survivors_top, ideas_dir=ideas_dir))

    return {
        "assessed": assessed,
        "eliminated": eliminated,
        "survivors_top": len(survivors_top),
        "rest": len(rest),
        "total": len(final),
        "persisted": persisted,
    }


def format_ranked_output(ranked: list[dict]) -> str:
    """Generate human-scannable markdown with full proposal details.

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
        idea_id = proposal.get("idea_id", "unknown")
        title = proposal.get("title", "Untitled")
        score = proposal.get("weighted_score", 0.0)

        sections = proposal.get("sections", {})
        research_question = sections.get("research_question", "")
        if not research_question:
            research_question = title

        approach = sections.get("approach_outline", "")
        experiments = sections.get("proposed_first_experiments", "")
        impact_chain = sections.get("theory_of_impact_chain", "")
        strength_rationale = sections.get("strength_rationale", "")
        alternative_framings = sections.get("alternative_framings", [])
        cited_sources = sections.get("cited_sources", [])

        subfield = proposal.get("subfield", "N/A")
        strategy = proposal.get("generation_strategy", "N/A")
        novelty_class = proposal.get("novelty_classification", "N/A")
        novelty_method = proposal.get("novelty_method", "N/A")

        # Format scores with reasoning and confidence
        scores_dict = proposal.get("scores")
        score_detail_lines: list[str] = []
        if scores_dict and isinstance(next(iter(scores_dict.values()), None), dict):
            for k, v in scores_dict.items():
                s = v.get("score", "?")
                reasoning = v.get("reasoning", "")
                confidence = v.get("confidence")
                conf_str = f", confidence: {confidence}" if confidence is not None else ""
                if reasoning:
                    score_detail_lines.append(f"  - **{k}:** {s}{conf_str} — {reasoning}")
                else:
                    score_detail_lines.append(f"  - **{k}:** {s}{conf_str}")
        else:
            original_scores = proposal.get("original_scores", {})
            for k, v in original_scores.items():
                score_detail_lines.append(f"  - **{k}:** {v}")

        # Provenance
        prov = proposal.get("provenance", {})
        gen_method = prov.get("generation_method", "N/A")
        kb_count = len(prov.get("kb_sources", []))
        web_count = len(prov.get("web_sources", []))

        lines.append("")
        lines.append(f"## #{rank}: {title} (Score: {score:.2f})")
        lines.append("")
        lines.append(f"**ID:** {idea_id}")
        lines.append("")
        lines.append(f"**Research Question:** {research_question}")
        lines.append("")
        lines.append(f"**Approach:** {approach}")
        lines.append("")
        if experiments:
            lines.append(f"**Experiments:** {experiments}")
            lines.append("")
        if impact_chain:
            lines.append(f"**Impact Chain:** {impact_chain}")
            lines.append("")
        if strength_rationale:
            lines.append(f"**Strength Rationale:** {strength_rationale}")
            lines.append("")
        if alternative_framings:
            framings_text = "; ".join(
                item if isinstance(item, str) else str(item) for item in alternative_framings
            )
            lines.append(f"**Alternative Framings:** {framings_text}")
            lines.append("")
        if cited_sources:
            sources_text = "; ".join(
                item if isinstance(item, str) else str(item) for item in cited_sources
            )
            lines.append(f"**Cited Sources:** {sources_text}")
            lines.append("")
        lines.append(
            f"**Subfield:** {subfield} | **Strategy:** {strategy}"
            f" | **Novelty:** {novelty_class} ({novelty_method})"
        )
        lines.append("**Scores:**")
        lines.extend(score_detail_lines)
        lines.append(f"**Provenance:** {gen_method}, sources: {kb_count} KB, {web_count} web")
        lines.append("")
        lines.append("---")

    return "\n".join(lines) + "\n"


def persist_ideas(
    ranked: list[dict],
    ideas_dir: Path | None = None,
    require_assessed: bool = True,
) -> list[Path]:
    """Copy final proposals to data/ideas/ for persistent accumulation.

    Each proposal is written as <idea_id>.md with YAML frontmatter and markdown
    body sections.

    Proposals whose novelty is only *estimated* (``novelty_method`` is anything
    other than ``"novelty_assessed"``) are skipped when ``require_assessed`` is
    True.  This mechanically enforces the project rule that ideas must not be
    persisted with only estimated novelty — a real novelty check must run first.

    Args:
        ranked: List of ranked proposal dicts.
        ideas_dir: Target directory. Uses IDEAS_DIR from constants if not provided.
        require_assessed: When True (default), skip proposals without a
            calculated (``"novelty_assessed"``) novelty assessment.

    Returns:
        List of written file paths (excludes any skipped proposals).
    """
    target = ideas_dir or IDEAS_DIR
    target.mkdir(parents=True, exist_ok=True)

    written = []
    for proposal in ranked:
        idea_id = proposal.get("idea_id", "unknown")

        if require_assessed and proposal.get("novelty_method") != "novelty_assessed":
            # Estimated-only novelty: do not persist (project rule).
            continue

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
            "novelty_method": proposal.get("novelty_method"),
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
        print("Usage: python -m saim.pipeline.rank <command> <run_dir> [args]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "rank":
        run_dir = Path(sys.argv[2])
        from saim.pipeline.refine import read_refined_proposals

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
    elif cmd == "rerank":
        # rerank <run_dir> <updates_dir> <top_n> <persist:true|false>
        from saim.config.loader import load_config

        run_dir = Path(sys.argv[2])
        updates_dir = Path(sys.argv[3])
        top_n = int(sys.argv[4])
        persist = len(sys.argv) > 5 and sys.argv[5].lower() in ("true", "1", "yes")

        updates: dict[str, dict] = {}
        if updates_dir.exists():
            for jf in sorted(updates_dir.glob("*.json")):
                with open(jf) as f:
                    u = json.load(f)
                idea_id = u.get("idea_id") or jf.stem
                updates[idea_id] = u

        config = load_config(load_env=False)
        team = config.teams.get(config.default_team)
        result = rerank_with_novelty(
            run_dir, updates, top_n, config.criteria, team, persist=persist
        )
        print(json.dumps(result, indent=2))
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
