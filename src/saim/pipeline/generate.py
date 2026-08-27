"""Generate stage: write and read idea sketch markdown files with YAML frontmatter."""

from datetime import UTC, datetime
from pathlib import Path

import yaml

from saim.ids import is_idea_id, new_idea_id

_REQUIRED_IDEA_KEYS = [
    "run_id",
    "subfield",
    "generation_strategy",
    "confidence",
    "title",
    "problem",
    "direction",
    "why_it_matters",
    "relevant_context",
]


def write_idea_sketch(run_dir: Path, idea: dict) -> Path:
    """Write an idea sketch as a markdown file with YAML frontmatter.

    ``idea_id`` is optional: when absent or empty it is minted with
    ``saim.ids.new_idea_id()``. When present it must already be in that format,
    so IDs are always generated the same way and never collide across batches.

    Returns the path to the created file.

    Raises:
        ValueError: If required keys are missing, or ``idea_id`` is set to
            something other than a ``saim.ids`` ID.
    """
    missing = [k for k in _REQUIRED_IDEA_KEYS if k not in idea]
    if missing:
        raise ValueError(f"Idea dict missing required keys: {missing}")

    idea_id = idea.get("idea_id") or new_idea_id()
    if not is_idea_id(idea_id):
        raise ValueError(
            f"Invalid idea_id {idea_id!r}. Idea IDs must come from saim.ids "
            "(uv run python -m saim.ids), which returns e.g. 'gen-3f9a1c04'. "
            "Hand-written or sequential IDs collide across batches and runs. "
            "Omit idea_id to have one minted here."
        )

    generate_dir = run_dir / "generate"
    generate_dir.mkdir(parents=True, exist_ok=True)

    frontmatter = {
        "idea_id": idea_id,
        "run_id": idea["run_id"],
        "stage": "generate",
        "timestamp": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "subfield": idea["subfield"],
        "generation_strategy": idea["generation_strategy"],
        "confidence": idea["confidence"],
    }

    body_lines = [
        f"# {idea['title']}",
        "",
        f"**Problem:** {idea['problem']}",
        "",
        f"**Direction:** {idea['direction']}",
        "",
        f"**Why it matters:** {idea['why_it_matters']}",
        "",
        f"**Relevant context:** {idea['relevant_context']}",
    ]

    fm_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    content = f"---\n{fm_str}---\n\n" + "\n".join(body_lines) + "\n"

    file_path = generate_dir / f"{idea_id}.md"
    file_path.write_text(content)
    return file_path


def read_idea_sketches(run_dir: Path) -> list[dict]:
    """Read all idea sketch markdown files from the generate directory.

    Returns a list of dicts with frontmatter fields plus a 'body' key.
    """
    generate_dir = run_dir / "generate"
    if not generate_dir.exists():
        return []

    results = []
    for md_file in sorted(generate_dir.glob("*.md")):
        text = md_file.read_text()
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1])
        body = parts[2].strip()
        entry = {**fm, "body": body}
        results.append(entry)

    return results


def list_idea_files(run_dir: Path) -> list[Path]:
    """Return a sorted list of .md file paths in the generate directory."""
    generate_dir = run_dir / "generate"
    if not generate_dir.exists():
        return []
    return sorted(generate_dir.glob("*.md"))


def main() -> None:
    import json
    import sys

    if len(sys.argv) < 3:
        print("Usage: python -m saim.pipeline.generate <command> <run_dir> [json_data]")
        sys.exit(1)
    cmd = sys.argv[1]
    run_dir = Path(sys.argv[2])
    if cmd == "write":
        idea_data = json.loads(sys.argv[3])
        path = write_idea_sketch(run_dir, idea_data)
        print(path)
    elif cmd == "list":
        for f in list_idea_files(run_dir):
            print(f)
    elif cmd == "read":
        ideas = read_idea_sketches(run_dir)
        print(json.dumps(ideas, indent=2, default=str))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
