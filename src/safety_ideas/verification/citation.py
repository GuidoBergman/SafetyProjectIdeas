"""Citation lookup: DOI and Semantic Scholar API queries.

These functions are *lookup tools* — they return metadata for the LLM to
inspect and judge.  They do NOT make verification decisions themselves.
"""

from __future__ import annotations

import json
import logging
import os
import urllib.error
import urllib.request
from urllib.parse import quote

logger = logging.getLogger(__name__)

_CROSSREF_BASE = "https://api.crossref.org/works"
_SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"

# Timeout for HTTP requests in seconds.
_HTTP_TIMEOUT = 10


def lookup_doi(doi: str) -> dict | None:
    """Fetch metadata for a DOI from the CrossRef API.

    Args:
        doi: DOI string (e.g. "10.1234/example").

    Returns:
        Dict with ``doi``, ``title``, ``authors``, and ``url`` if the DOI
        resolves, or None on failure.
    """
    url = f"{_CROSSREF_BASE}/{quote(doi, safe='')}"
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "SafetyIdeas/0.1 (citation-check)")
        with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT) as resp:
            data = json.loads(resp.read().decode())

        message = data.get("message", {})
        titles = message.get("title", [])
        authors_raw = message.get("author", [])
        authors = [
            " ".join(filter(None, [a.get("given", ""), a.get("family", "")]))
            for a in authors_raw
        ]
        return {
            "doi": doi,
            "title": titles[0] if titles else "",
            "authors": authors,
            "url": message.get("URL", f"https://doi.org/{doi}"),
        }
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        logger.debug("DOI lookup failed for %s: %s", doi, exc)
        return None


def search_crossref(title: str, rows: int = 3) -> list[dict]:
    """Search CrossRef by title and return candidate papers.

    Args:
        title: Paper title to search for.
        rows: Maximum number of results to return.

    Returns:
        List of dicts, each with ``doi``, ``title``, ``authors``, and ``url``.
    """
    query = quote(title)
    url = f"{_CROSSREF_BASE}?query.bibliographic={query}&rows={rows}"
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "SafetyIdeas/0.1 (citation-check)")
        with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT) as resp:
            data = json.loads(resp.read().decode())

        items = data.get("message", {}).get("items", [])
        results = []
        for item in items:
            titles = item.get("title", [])
            authors_raw = item.get("author", [])
            authors = [
                " ".join(filter(None, [a.get("given", ""), a.get("family", "")]))
                for a in authors_raw
            ]
            results.append({
                "doi": item.get("DOI", ""),
                "title": titles[0] if titles else "",
                "authors": authors,
                "url": item.get("URL", ""),
            })
        return results
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        logger.debug("CrossRef search failed for %r: %s", title, exc)
        return []


def search_semantic_scholar(title: str, limit: int = 3) -> list[dict]:
    """Search Semantic Scholar by title and return candidate papers.

    Args:
        title: Paper title to search for.
        limit: Maximum number of results to return.

    Returns:
        List of dicts, each with ``paperId``, ``title``, and ``url``.
    """
    query = quote(title)
    url = f"{_SEMANTIC_SCHOLAR_BASE}?query={query}&limit={limit}"
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "SafetyIdeas/0.1 (citation-check)")
        s2_key = os.environ.get("S2_API_KEY")
        if s2_key:
            req.add_header("x-api-key", s2_key)
        with urllib.request.urlopen(req, timeout=_HTTP_TIMEOUT) as resp:
            data = json.loads(resp.read().decode())

        papers = data.get("data", [])
        return [
            {
                "paperId": p.get("paperId", ""),
                "title": p.get("title", ""),
                "url": p.get("url", ""),
            }
            for p in papers
        ]
    except (urllib.error.HTTPError, urllib.error.URLError, OSError, json.JSONDecodeError) as exc:
        logger.debug("Semantic Scholar search failed for %r: %s", title, exc)
        return []


def lookup_citations(idea: dict) -> list[dict]:
    """Look up metadata for all citations in an idea.

    For each citation, queries CrossRef (by DOI if available, then by title)
    and Semantic Scholar (by title).  Returns all results for the LLM to judge.

    Args:
        idea: Idea dict with a ``citations`` list.  Each citation should have
            optional ``doi`` and/or ``title`` fields.

    Returns:
        List of per-citation lookup results.  Each entry is a dict with:
        - ``citation``: the original citation dict
        - ``crossref_doi``: metadata from DOI lookup (or None)
        - ``crossref_search``: list of title-search candidates from CrossRef
        - ``semantic_scholar``: list of candidates from Semantic Scholar
    """
    citations = idea.get("citations", [])
    results = []

    for citation in citations:
        doi = citation.get("doi", "")
        title = citation.get("title", "")

        entry: dict = {
            "citation": citation,
            "crossref_doi": None,
            "crossref_search": [],
            "semantic_scholar": [],
        }

        if doi:
            entry["crossref_doi"] = lookup_doi(doi)

        if title:
            entry["crossref_search"] = search_crossref(title)
            entry["semantic_scholar"] = search_semantic_scholar(title)

        results.append(entry)

    return results


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m safety_ideas.verification.citation <command> [args]")
        print("Commands:")
        print("  lookup-doi <doi>           — fetch metadata for a DOI")
        print("  search-crossref <title>    — search CrossRef by title")
        print("  search-s2 <title>          — search Semantic Scholar by title")
        print("  lookup-idea <idea_json>    — look up all citations in an idea")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "lookup-doi":
        doi = sys.argv[2]
        result = lookup_doi(doi)
        print(json.dumps(result, default=str))
    elif cmd == "search-crossref":
        title = sys.argv[2]
        results = search_crossref(title)
        print(json.dumps(results, default=str))
    elif cmd == "search-s2":
        title = sys.argv[2]
        results = search_semantic_scholar(title)
        print(json.dumps(results, default=str))
    elif cmd == "lookup-idea":
        idea_data = json.loads(sys.argv[2])
        results = lookup_citations(idea_data)
        print(json.dumps(results, default=str))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
