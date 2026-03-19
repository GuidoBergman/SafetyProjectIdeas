"""Citation verification: DOI and Semantic Scholar API lookups."""

from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
from urllib.parse import quote

logger = logging.getLogger(__name__)

_CROSSREF_BASE = "https://api.crossref.org/works"
_SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"

# Timeout for HTTP requests in seconds.
_HTTP_TIMEOUT = 10


def verify_doi(doi: str) -> bool:
    """Check whether a DOI resolves via the CrossRef API.

    Args:
        doi: DOI string (e.g. "10.1234/example").

    Returns:
        True if the DOI resolves (HTTP 200), False otherwise.
    """
    url = f"{_CROSSREF_BASE}/{quote(doi, safe='')}"
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "SafetyIdeas/0.1 (citation-check)")
        with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT) as resp:
            return resp.status == 200
    except (urllib.error.HTTPError, urllib.error.URLError, OSError) as exc:
        logger.debug("DOI verification failed for %s: %s", doi, exc)
        return False


def verify_semantic_scholar(title: str) -> dict | None:
    """Look up a paper by title via the Semantic Scholar API.

    Args:
        title: Paper title to search for.

    Returns:
        Dict with paper metadata (paperId, title, url) if a match is found,
        or None if no match.
    """
    query = quote(title)
    url = f"{_SEMANTIC_SCHOLAR_BASE}?query={query}&limit=3"
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "SafetyIdeas/0.1 (citation-check)")
        with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT) as resp:
            data = json.loads(resp.read().decode())

        papers = data.get("data", [])
        if not papers:
            return None

        # Check for a title match (case-insensitive).
        title_lower = title.lower().strip()
        for paper in papers:
            paper_title = (paper.get("title") or "").lower().strip()
            if paper_title == title_lower:
                return {
                    "paperId": paper.get("paperId"),
                    "title": paper.get("title"),
                    "url": paper.get("url", ""),
                }

        # Return first result as a close match if no exact match found.
        first = papers[0]
        return {
            "paperId": first.get("paperId"),
            "title": first.get("title"),
            "url": first.get("url", ""),
        }
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        logger.debug("Semantic Scholar lookup failed for %r: %s", title, exc)
        return None


def verify_citations(idea: dict) -> dict:
    """Verify all citations in an idea dict.

    Expects the idea to have a ``citations`` key containing a list of dicts,
    each with optional ``doi`` and/or ``title`` fields.

    Args:
        idea: Idea dict with a ``citations`` list.

    Returns:
        Dict with ``verified``, ``failed``, and ``removed`` lists.
    """
    citations = idea.get("citations", [])
    verified: list[str] = []
    failed: list[str] = []

    for citation in citations:
        doi = citation.get("doi", "")
        title = citation.get("title", "")
        identifier = doi or title or "unknown"

        is_verified = False

        # Try DOI first (cheapest).
        if doi:
            if verify_doi(doi):
                is_verified = True

        # Fall back to Semantic Scholar title search.
        if not is_verified and title:
            result = verify_semantic_scholar(title)
            if result is not None:
                is_verified = True

        if is_verified:
            verified.append(identifier)
        else:
            failed.append(identifier)

    return {
        "verified": verified,
        "failed": failed,
        "removed": list(failed),  # Failed citations will be removed.
    }


def filter_unverified(idea: dict, verification: dict) -> dict:
    """Remove unverified citations from an idea dict.

    Args:
        idea: Idea dict with a ``citations`` list.
        verification: Verification results from ``verify_citations()``.

    Returns:
        New idea dict with unverified citations removed.
    """
    failed_set = set(verification.get("failed", []))
    if not failed_set:
        return idea

    filtered = dict(idea)
    original_citations = idea.get("citations", [])
    filtered["citations"] = [
        c
        for c in original_citations
        if (c.get("doi") or c.get("title") or "unknown") not in failed_set
    ]
    return filtered


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.verification.citation <command> [args]")
        print("Commands:")
        print("  verify-doi <doi>           — verify a single DOI")
        print("  verify-title <title>       — search Semantic Scholar by title")
        print("  verify-idea <idea_json>    — verify all citations in an idea")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "verify-doi":
        doi = sys.argv[2]
        result = verify_doi(doi)
        print(json.dumps({"doi": doi, "verified": result}))
    elif cmd == "verify-title":
        title = sys.argv[2]
        result = verify_semantic_scholar(title)
        print(json.dumps(result, default=str))
    elif cmd == "verify-idea":
        idea_data = json.loads(sys.argv[2])
        result = verify_citations(idea_data)
        print(json.dumps(result))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
