"""Load previously generated ideas to avoid duplication."""

import logging
from pathlib import Path

from safety_ideas.constants import IDEAS_DIR

logger = logging.getLogger(__name__)


def load_previous_ideas(ideas_dir: Path | None = None) -> list[str]:
    """Extract H1 titles from markdown files in the ideas directory.

    Args:
        ideas_dir: Directory containing idea markdown files.
            Defaults to IDEAS_DIR from constants.

    Returns:
        List of title strings extracted from H1 headings.
    """
    if ideas_dir is None:
        ideas_dir = IDEAS_DIR

    if not ideas_dir.is_dir():
        logger.info("Ideas directory does not exist: %s", ideas_dir)
        return []

    titles: list[str] = []
    for md_file in sorted(ideas_dir.glob("*.md")):
        for line in md_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                titles.append(line[2:].strip())
                break

    logger.info("Loaded %d previous ideas from %s", len(titles), ideas_dir)
    return titles


def main() -> None:
    import json
    import sys

    ideas_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    titles = load_previous_ideas(ideas_dir)
    print(json.dumps(titles))


if __name__ == "__main__":
    main()
