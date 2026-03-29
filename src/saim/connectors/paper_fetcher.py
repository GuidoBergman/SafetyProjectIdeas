"""Paper content fetcher for targeted deep reading during novelty assessment.

Supports multiple sources:
- ArXiv HTML pages: section extraction (discussion, limitations, future work, etc.)
- ArXiv API + PDF: fallback for papers without HTML versions
- LessWrong / Alignment Forum: GraphQL API (no auth required)
- Blog posts: trafilatura extraction
- Any URL: trafilatura fallback
"""

from __future__ import annotations

import io
import logging
import re
from urllib.parse import urlparse

import arxiv
import httpx
import pypdf
import trafilatura

from saim.constants import (
    ARXIV_HTML_BASE,
    DEEP_READ_CONTENT_LIMIT,
    DEEP_READ_SECTION_LIMIT,
    DEEP_READ_TIMEOUT,
    KNOWN_BLOG_DOMAINS,
)

logger = logging.getLogger(__name__)

# Section headings we look for in papers.
_TARGET_SECTIONS = [
    "discussion",
    "limitations",
    "future work",
    "conclusion",
    "related work",
]

_TAG_RE = re.compile(r"<[^>]+>")

# Match h2/h3 headings with their level for ArXiv HTML parsing.
_HEADING_WITH_LEVEL_RE = re.compile(
    r"<h([2-3])[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL
)

# LessWrong/AF GraphQL endpoints.
# AF shares its database with LW, so we use LW's endpoint for both
# (AF's endpoint sometimes returns 429 security checkpoint).
_GRAPHQL_ENDPOINTS = {
    "lesswrong.com": "https://www.lesswrong.com/graphql",
    "alignmentforum.org": "https://www.lesswrong.com/graphql",
}

# GraphQL query to fetch post content by ID.
_POST_QUERY = """
query PostById($id: String) {
  post(input: {selector: {_id: $id}}) {
    result {
      title
      htmlBody
    }
  }
}
"""

# Regex to extract post ID from LW/AF URLs (the segment after /posts/).
_LW_POST_ID_RE = re.compile(r"/posts/([^/]+)")

# Regex to find section headers in PDF text.
_PDF_SECTION_RE = re.compile(
    r"^(\d+\.?\s+)?(discussion|limitations|future work|"
    r"conclusion|related work)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def _strip_tags(html: str) -> str:
    """Remove HTML tags and collapse whitespace."""
    text = _TAG_RE.sub(" ", html)
    return re.sub(r"\s+", " ", text).strip()


def _extract_arxiv_id(url: str) -> str | None:
    """Extract ArXiv paper ID from a URL."""
    parsed = urlparse(url)
    if not parsed.hostname or "arxiv.org" not in parsed.hostname:
        return None
    path = parsed.path.strip("/")
    for prefix in ("abs/", "html/", "pdf/"):
        if path.startswith(prefix):
            return path[len(prefix):]
    return None


def _is_known_blog(url: str) -> bool:
    """Check if a URL is from a known blog domain."""
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    return any(domain in hostname for domain in KNOWN_BLOG_DOMAINS)


def _get_lw_endpoint(url: str) -> str | None:
    """Get the GraphQL endpoint for a LessWrong/AF URL."""
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    for domain, endpoint in _GRAPHQL_ENDPOINTS.items():
        if domain in hostname:
            return endpoint
    return None


def _extract_lw_post_id(url: str) -> str | None:
    """Extract post ID from a LessWrong/AF URL."""
    match = _LW_POST_ID_RE.search(url)
    return match.group(1) if match else None


# --- ArXiv HTML ---


def _parse_sections_from_html(html: str) -> dict[str, str]:
    """Parse ArXiv HTML and extract content under target section headings."""
    sections: dict[str, str] = {}

    headings: list[tuple[int, int, str, int]] = []
    for match in _HEADING_WITH_LEVEL_RE.finditer(html):
        level = int(match.group(1))
        text = _strip_tags(match.group(2)).lower().strip()
        text_clean = re.sub(r"^\d+(\.\d+)*\s*", "", text)
        headings.append((match.start(), level, text_clean, match.end()))

    for i, (pos, level, heading_text, content_start) in enumerate(headings):
        for target in _TARGET_SECTIONS:
            if target in heading_text and target not in sections:
                content_end = len(html)
                for j in range(i + 1, len(headings)):
                    if headings[j][1] <= level:
                        content_end = headings[j][0]
                        break
                raw = html[content_start:content_end]
                clean = _strip_tags(raw)
                if clean:
                    sections[target] = clean[:DEEP_READ_SECTION_LIMIT]
                break

    return sections


def fetch_arxiv_sections(arxiv_id: str) -> dict | None:
    """Fetch an ArXiv paper and extract target sections.

    Tries HTML first, falls back to PDF extraction, then abstract-only.
    """
    # Try HTML version first (cheapest, best structured).
    html_result = _fetch_arxiv_html(arxiv_id)
    if html_result is not None:
        return html_result

    # Fall back to PDF extraction.
    pdf_result = _fetch_arxiv_pdf(arxiv_id)
    if pdf_result is not None:
        return pdf_result

    # Last resort: abstract via ArXiv API.
    return _fetch_arxiv_abstract(arxiv_id)


def _fetch_arxiv_html(arxiv_id: str) -> dict | None:
    """Try to fetch and parse ArXiv HTML version."""
    url = f"{ARXIV_HTML_BASE}/{arxiv_id}"
    try:
        response = httpx.get(
            url, timeout=DEEP_READ_TIMEOUT, follow_redirects=True
        )
        if response.status_code != 200:
            return None
    except httpx.HTTPError:
        return None

    sections = _parse_sections_from_html(response.text)
    if not sections:
        return None
    return {"url": url, "sections": sections}


def _fetch_arxiv_pdf(arxiv_id: str) -> dict | None:
    """Download ArXiv PDF and extract sections via pypdf + regex."""
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    try:
        response = httpx.get(
            pdf_url, timeout=30, follow_redirects=True
        )
        if response.status_code != 200:
            return None
    except httpx.HTTPError:
        return None

    try:
        reader = pypdf.PdfReader(io.BytesIO(response.content))
        full_text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )
    except Exception as e:
        logger.warning("Failed to parse PDF for %s: %s", arxiv_id, e)
        return None

    sections = _extract_sections_from_text(full_text)
    if not sections:
        return None
    return {"url": pdf_url, "sections": sections}


def _fetch_arxiv_abstract(arxiv_id: str) -> dict | None:
    """Fetch paper abstract and metadata via ArXiv API."""
    try:
        client = arxiv.Client()
        # Strip version suffix like "v2" but keep the paper ID digits.
        clean_id = re.sub(r"v\d+$", "", arxiv_id)
        search = arxiv.Search(id_list=[clean_id])
        results = list(client.results(search))
        if not results:
            return None
        paper = results[0]
        return {
            "url": paper.entry_id,
            "sections": {
                "abstract": paper.summary[:DEEP_READ_SECTION_LIMIT],
            },
        }
    except Exception as e:
        logger.warning("ArXiv API failed for %s: %s", arxiv_id, e)
        return None


def _extract_sections_from_text(text: str) -> dict[str, str]:
    """Extract sections from plain text (e.g. from PDF) using regex."""
    sections: dict[str, str] = {}
    matches = list(_PDF_SECTION_RE.finditer(text))

    for i, match in enumerate(matches):
        section_name = match.group(2).lower().strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[start:end].strip()

        for target in _TARGET_SECTIONS:
            if target in section_name and target not in sections:
                if content:
                    sections[target] = content[:DEEP_READ_SECTION_LIMIT]
                break

    return sections


# --- LessWrong / Alignment Forum ---


def fetch_lw_content(url: str) -> dict | None:
    """Fetch post content from LessWrong or Alignment Forum via GraphQL.

    No authentication required for public posts.
    """
    endpoint = _get_lw_endpoint(url)
    post_id = _extract_lw_post_id(url)
    if not endpoint or not post_id:
        return None

    try:
        response = httpx.post(
            endpoint,
            json={"query": _POST_QUERY, "variables": {"id": post_id}},
            timeout=DEEP_READ_TIMEOUT,
            headers={"Content-Type": "application/json"},
        )
        if response.status_code != 200:
            logger.info("LW/AF GraphQL returned %d for %s", response.status_code, url)
            return None

        data = response.json()
        post = data.get("data", {}).get("post", {}).get("result")
        if not post or not post.get("htmlBody"):
            return None

        content = _strip_tags(post["htmlBody"])
        return {"url": url, "content": content[:DEEP_READ_CONTENT_LIMIT]}
    except Exception as e:
        logger.warning("Failed to fetch LW/AF content from %s: %s", url, e)
        return None


# --- Blog posts ---

_BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _fetch_html_with_httpx(url: str) -> str | None:
    """Fetch a URL with httpx and a browser User-Agent."""
    try:
        resp = httpx.get(
            url,
            timeout=DEEP_READ_TIMEOUT,
            follow_redirects=True,
            headers={"User-Agent": _BROWSER_UA},
        )
        return resp.text if resp.text else None
    except httpx.HTTPError:
        return None


def fetch_blog_content(url: str) -> dict | None:
    """Fetch and extract clean text from a blog post URL.

    Tries trafilatura's built-in fetcher first, falls back to httpx
    with a browser User-Agent if that fails (some sites block bots).
    """
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded is None:
            downloaded = _fetch_html_with_httpx(url)
        if downloaded is None:
            logger.info("Could not download blog content from %s", url)
            return None
        content = trafilatura.extract(
            downloaded, include_tables=False, include_comments=False
        )
        if not content:
            logger.info("No content extracted from %s", url)
            return None
        return {"url": url, "content": content[:DEEP_READ_CONTENT_LIMIT]}
    except Exception as e:
        logger.warning("Failed to extract blog content from %s: %s", url, e)
        return None


# --- Main dispatcher ---


def fetch_deep_content(url: str) -> dict | None:
    """Fetch deeper content from a URL for novelty assessment.

    Dispatches to the appropriate fetcher:
    - ArXiv URLs -> HTML sections, then PDF fallback, then abstract
    - LessWrong/AF -> GraphQL API
    - Known blog domains -> trafilatura
    - Other URLs -> trafilatura fallback
    """
    # ArXiv papers.
    arxiv_id = _extract_arxiv_id(url)
    if arxiv_id is not None:
        return fetch_arxiv_sections(arxiv_id)

    # LessWrong / Alignment Forum posts.
    if _get_lw_endpoint(url) is not None:
        return fetch_lw_content(url)

    # Blogs and everything else via trafilatura.
    return fetch_blog_content(url)


def main() -> None:
    import json
    import sys

    if len(sys.argv) < 3:
        print(
            "Usage: python -m saim.connectors.paper_fetcher"
            " <command> <url_or_json>"
        )
        print("Commands:")
        print("  fetch <url>              — fetch deep content from a URL")
        print("  fetch-batch '<json>'     — fetch from multiple URLs")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "fetch":
        url = sys.argv[2]
        result = fetch_deep_content(url)
        print(json.dumps(result, indent=2, default=str))
    elif cmd == "fetch-batch":
        urls = json.loads(sys.argv[2])
        results = [fetch_deep_content(u) for u in urls]
        print(json.dumps(results, indent=2, default=str))
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
