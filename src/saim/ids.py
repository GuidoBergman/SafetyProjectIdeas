"""Idea identifier generation.

This module is the **single source of truth** for SAIM idea IDs. Every idea ID,
wherever it is created (pipeline stages, skills, ad-hoc scripts), must come from
``new_idea_id()`` or the ``python -m saim.ids`` CLI.

IDs are random short UUIDs (``gen-<8 hex chars>``) rather than sequential
counters. Sequential counters collide when ideas are generated in separate
batches or runs: two runs both start at ``gen-001`` and overwrite each other in
the shared ``data/ideas/`` directory.
"""

from __future__ import annotations

import re
from uuid import uuid4

# ``gen-`` keeps continuity with historical IDs; the suffix is random hex.
IDEA_ID_PREFIX = "gen-"
IDEA_ID_HEX_LEN = 8

IDEA_ID_PATTERN = re.compile(rf"^{re.escape(IDEA_ID_PREFIX)}[0-9a-f]{{{IDEA_ID_HEX_LEN}}}$")


def new_idea_id() -> str:
    """Return a fresh idea ID, e.g. ``gen-3f9a1c04``.

    Uses the first ``IDEA_ID_HEX_LEN`` hex characters of a UUID4, which gives
    2**32 possible IDs. At a few thousand ideas the collision probability is
    below one in a thousand, and callers that write to a shared directory can
    still guard with ``Path.exists()`` if they need certainty.
    """
    return f"{IDEA_ID_PREFIX}{uuid4().hex[:IDEA_ID_HEX_LEN]}"


def is_idea_id(value: object) -> bool:
    """Return True if *value* is an ID in the current ``gen-<hex>`` format.

    Legacy sequential IDs (``gen-001``, ``gen-0017``) return False: they are
    still valid on disk, but must not be minted again.
    """
    return isinstance(value, str) and bool(IDEA_ID_PATTERN.match(value))


def main() -> None:
    """CLI: print *count* new idea IDs, one per line (default 1)."""
    import sys

    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if count < 1:
        print("Usage: python -m saim.ids [count]", file=sys.stderr)
        sys.exit(1)
    for _ in range(count):
        print(new_idea_id())


if __name__ == "__main__":
    main()
