"""Tests for the paper_fetcher module. All HTTP/API calls are mocked."""

from unittest.mock import MagicMock, patch

from safety_ideas.connectors.paper_fetcher import (
    _extract_arxiv_id,
    _extract_lw_post_id,
    _extract_sections_from_text,
    _get_lw_endpoint,
    _is_known_blog,
    _parse_sections_from_html,
    fetch_arxiv_sections,
    fetch_blog_content,
    fetch_deep_content,
    fetch_lw_content,
)


class TestExtractArxivId:
    def test_abs_url(self):
        assert _extract_arxiv_id("https://arxiv.org/abs/2401.12345") == "2401.12345"

    def test_html_url(self):
        assert _extract_arxiv_id("https://arxiv.org/html/2401.12345") == "2401.12345"

    def test_pdf_url(self):
        assert _extract_arxiv_id("https://arxiv.org/pdf/2401.12345") == "2401.12345"

    def test_versioned_url(self):
        assert _extract_arxiv_id("https://arxiv.org/abs/2401.12345v2") == "2401.12345v2"

    def test_non_arxiv_url(self):
        assert _extract_arxiv_id("https://example.com/paper") is None

    def test_arxiv_no_prefix(self):
        assert _extract_arxiv_id("https://arxiv.org/2401.12345") is None


class TestIsKnownBlog:
    def test_alignment_forum(self):
        assert _is_known_blog("https://www.alignmentforum.org/posts/abc") is True

    def test_lesswrong(self):
        assert _is_known_blog("https://www.lesswrong.com/posts/abc") is True

    def test_anthropic(self):
        assert _is_known_blog("https://anthropic.com/research/x") is True

    def test_unknown_domain(self):
        assert _is_known_blog("https://example.com/blog/post") is False


class TestLwHelpers:
    def test_get_lw_endpoint_lesswrong(self):
        url = "https://www.lesswrong.com/posts/abc/my-post"
        assert _get_lw_endpoint(url) == "https://www.lesswrong.com/graphql"

    def test_get_lw_endpoint_af(self):
        url = "https://www.alignmentforum.org/posts/abc/my-post"
        endpoint = _get_lw_endpoint(url)
        # AF routes through LW's GraphQL (AF's endpoint returns 429).
        assert endpoint == "https://www.lesswrong.com/graphql"

    def test_get_lw_endpoint_other(self):
        assert _get_lw_endpoint("https://example.com") is None

    def test_extract_post_id(self):
        url = "https://www.lesswrong.com/posts/abc123/my-cool-post"
        assert _extract_lw_post_id(url) == "abc123"

    def test_extract_post_id_no_match(self):
        assert _extract_lw_post_id("https://example.com") is None


class TestParseSectionsFromHtml:
    def test_extracts_numbered_headings(self):
        html = (
            "<h2>4 Related Work</h2><p>Related text</p>"
            "<h2>5 Discussion</h2><p>Discussion text</p>"
            "<h2>6 Conclusion</h2><p>Conclusion text</p>"
        )
        sections = _parse_sections_from_html(html)
        assert "related work" in sections
        assert "discussion" in sections
        assert "conclusion" in sections

    def test_collects_subsections(self):
        html = (
            "<h2>5 Discussion</h2><p>Main discussion.</p>"
            "<h3>5.1 Limitations</h3><p>Limitation details.</p>"
            "<h2>6 Conclusion</h2><p>Done.</p>"
        )
        sections = _parse_sections_from_html(html)
        assert "discussion" in sections
        assert "Limitation details" in sections["discussion"]
        assert "limitations" in sections

    def test_no_target_sections(self):
        html = "<h2>Methods</h2><p>Methods text</p>"
        assert _parse_sections_from_html(html) == {}

    def test_truncates_long_sections(self):
        html = f"<h2>Discussion</h2><p>{'x' * 5000}</p>"
        sections = _parse_sections_from_html(html)
        assert len(sections["discussion"]) == 3000

    def test_empty_html(self):
        assert _parse_sections_from_html("") == {}


class TestExtractSectionsFromText:
    def test_extracts_discussion(self):
        text = (
            "3 Results\nSome results here.\n"
            "4 Discussion\nThis is the discussion section.\n"
            "5 Conclusion\nWe conclude.\n"
        )
        sections = _extract_sections_from_text(text)
        assert "discussion" in sections
        assert "discussion section" in sections["discussion"]

    def test_extracts_multiple(self):
        text = (
            "5 Discussion\nDisc text.\n"
            "6 Limitations\nLimit text.\n"
            "7 Conclusion\nConc text.\n"
        )
        sections = _extract_sections_from_text(text)
        assert len(sections) == 3

    def test_no_sections(self):
        text = "Just some random text without section headers."
        assert _extract_sections_from_text(text) == {}

    def test_truncates(self):
        text = f"5 Discussion\n{'x' * 5000}\n6 Conclusion\nDone.\n"
        sections = _extract_sections_from_text(text)
        assert len(sections["discussion"]) == 3000


class TestFetchArxivSections:
    @patch(
        "safety_ideas.connectors.paper_fetcher._fetch_arxiv_abstract",
        return_value=None,
    )
    @patch(
        "safety_ideas.connectors.paper_fetcher._fetch_arxiv_pdf",
        return_value=None,
    )
    @patch("safety_ideas.connectors.paper_fetcher._fetch_arxiv_html")
    def test_html_success(self, mock_html, mock_pdf, mock_abstract):
        mock_html.return_value = {
            "url": "https://arxiv.org/html/2401.12345",
            "sections": {"discussion": "text"},
        }
        result = fetch_arxiv_sections("2401.12345")
        assert result is not None
        assert "discussion" in result["sections"]
        mock_pdf.assert_not_called()

    @patch("safety_ideas.connectors.paper_fetcher._fetch_arxiv_abstract")
    @patch("safety_ideas.connectors.paper_fetcher._fetch_arxiv_pdf")
    @patch(
        "safety_ideas.connectors.paper_fetcher._fetch_arxiv_html",
        return_value=None,
    )
    def test_falls_back_to_pdf(self, mock_html, mock_pdf, mock_abstract):
        mock_pdf.return_value = {
            "url": "https://arxiv.org/pdf/2401.12345",
            "sections": {"conclusion": "text"},
        }
        result = fetch_arxiv_sections("2401.12345")
        assert result is not None
        mock_pdf.assert_called_once()

    @patch("safety_ideas.connectors.paper_fetcher._fetch_arxiv_abstract")
    @patch(
        "safety_ideas.connectors.paper_fetcher._fetch_arxiv_pdf",
        return_value=None,
    )
    @patch(
        "safety_ideas.connectors.paper_fetcher._fetch_arxiv_html",
        return_value=None,
    )
    def test_falls_back_to_abstract(self, mock_html, mock_pdf, mock_abs):
        mock_abs.return_value = {
            "url": "https://arxiv.org/abs/2401.12345",
            "sections": {"abstract": "Summary of the paper."},
        }
        result = fetch_arxiv_sections("2401.12345")
        assert result is not None
        assert "abstract" in result["sections"]


class TestFetchLwContent:
    @patch("safety_ideas.connectors.paper_fetcher.httpx.post")
    def test_successful_fetch(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {
                "post": {
                    "result": {
                        "title": "AI Safety Post",
                        "htmlBody": "<p>This is about AI safety.</p>",
                    }
                }
            }
        }
        mock_post.return_value = mock_response

        url = "https://www.lesswrong.com/posts/abc123/my-post"
        result = fetch_lw_content(url)
        assert result is not None
        assert "AI safety" in result["content"]

    @patch("safety_ideas.connectors.paper_fetcher.httpx.post")
    def test_empty_response(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": {"post": {"result": None}}
        }
        mock_post.return_value = mock_response

        url = "https://www.lesswrong.com/posts/abc123/my-post"
        assert fetch_lw_content(url) is None

    def test_invalid_url(self):
        assert fetch_lw_content("https://example.com/post") is None


class TestFetchBlogContent:
    @patch("safety_ideas.connectors.paper_fetcher.trafilatura.extract")
    @patch("safety_ideas.connectors.paper_fetcher.trafilatura.fetch_url")
    def test_successful_fetch(self, mock_fetch, mock_extract):
        mock_fetch.return_value = "<html><body>Blog content</body></html>"
        mock_extract.return_value = "Clean blog post about AI safety"

        result = fetch_blog_content("https://anthropic.com/research/x")
        assert result is not None
        assert result["content"] == "Clean blog post about AI safety"

    @patch("safety_ideas.connectors.paper_fetcher._fetch_html_with_httpx")
    @patch("safety_ideas.connectors.paper_fetcher.trafilatura.fetch_url")
    def test_download_failure(self, mock_fetch, mock_httpx):
        mock_fetch.return_value = None
        mock_httpx.return_value = None
        assert fetch_blog_content("https://anthropic.com/x") is None


class TestFetchDeepContent:
    @patch("safety_ideas.connectors.paper_fetcher.fetch_arxiv_sections")
    def test_dispatches_arxiv(self, mock_arxiv):
        mock_arxiv.return_value = {"url": "...", "sections": {"discussion": "t"}}
        result = fetch_deep_content("https://arxiv.org/abs/2401.12345")
        mock_arxiv.assert_called_once_with("2401.12345")
        assert result is not None

    @patch("safety_ideas.connectors.paper_fetcher.fetch_lw_content")
    def test_dispatches_lesswrong(self, mock_lw):
        mock_lw.return_value = {"url": "...", "content": "text"}
        url = "https://www.lesswrong.com/posts/abc/my-post"
        result = fetch_deep_content(url)
        mock_lw.assert_called_once_with(url)
        assert result is not None

    @patch("safety_ideas.connectors.paper_fetcher.fetch_lw_content")
    def test_dispatches_af(self, mock_lw):
        mock_lw.return_value = {"url": "...", "content": "text"}
        url = "https://www.alignmentforum.org/posts/abc/my-post"
        fetch_deep_content(url)
        mock_lw.assert_called_once_with(url)

    @patch("safety_ideas.connectors.paper_fetcher.fetch_blog_content")
    def test_dispatches_blog(self, mock_blog):
        mock_blog.return_value = {"url": "...", "content": "text"}
        url = "https://anthropic.com/research/x"
        fetch_deep_content(url)
        mock_blog.assert_called_once_with(url)

    @patch("safety_ideas.connectors.paper_fetcher.fetch_blog_content")
    def test_unknown_domain_uses_trafilatura(self, mock_blog):
        mock_blog.return_value = {"url": "...", "content": "text"}
        fetch_deep_content("https://example.com/some-page")
        mock_blog.assert_called_once()
