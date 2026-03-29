"""Tests for citation lookup module."""

import json
from unittest.mock import MagicMock, patch

from saim.verification.citation import (
    lookup_citations,
    lookup_doi,
    search_crossref,
    search_semantic_scholar,
)


def _mock_urlopen(response_data: dict | str) -> MagicMock:
    """Create a mock urlopen context manager returning the given data."""
    if isinstance(response_data, dict):
        body = json.dumps(response_data).encode()
    else:
        body = response_data.encode()
    mock_response = MagicMock()
    mock_response.read.return_value = body
    mock_response.status = 200
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)
    return mock_response


class TestLookupDoi:
    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_metadata_on_success(self, mock_urlopen_fn):
        crossref_response = {
            "message": {
                "title": ["Attention Is All You Need"],
                "author": [
                    {"given": "Ashish", "family": "Vaswani"},
                    {"given": "Noam", "family": "Shazeer"},
                ],
                "URL": "https://doi.org/10.1234/test",
            }
        }
        mock_urlopen_fn.return_value = _mock_urlopen(crossref_response)

        result = lookup_doi("10.1234/test")
        assert result is not None
        assert result["doi"] == "10.1234/test"
        assert result["title"] == "Attention Is All You Need"
        assert result["authors"] == ["Ashish Vaswani", "Noam Shazeer"]
        assert result["url"] == "https://doi.org/10.1234/test"

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_none_on_404(self, mock_urlopen_fn):
        import urllib.error

        mock_urlopen_fn.side_effect = urllib.error.HTTPError(
            url="", code=404, msg="Not Found", hdrs={}, fp=None
        )
        assert lookup_doi("10.9999/nonexistent") is None

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_none_on_network_error(self, mock_urlopen_fn):
        import urllib.error

        mock_urlopen_fn.side_effect = urllib.error.URLError("Connection refused")
        assert lookup_doi("10.1234/test") is None

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_handles_missing_fields(self, mock_urlopen_fn):
        crossref_response = {"message": {}}
        mock_urlopen_fn.return_value = _mock_urlopen(crossref_response)

        result = lookup_doi("10.1234/test")
        assert result is not None
        assert result["title"] == ""
        assert result["authors"] == []


class TestSearchCrossref:
    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_candidates(self, mock_urlopen_fn):
        crossref_response = {
            "message": {
                "items": [
                    {
                        "DOI": "10.1234/paper1",
                        "title": ["Paper One"],
                        "author": [{"given": "Alice", "family": "Smith"}],
                        "URL": "https://doi.org/10.1234/paper1",
                    },
                    {
                        "DOI": "10.1234/paper2",
                        "title": ["Paper Two"],
                        "author": [],
                        "URL": "https://doi.org/10.1234/paper2",
                    },
                ]
            }
        }
        mock_urlopen_fn.return_value = _mock_urlopen(crossref_response)

        results = search_crossref("Paper One")
        assert len(results) == 2
        assert results[0]["doi"] == "10.1234/paper1"
        assert results[0]["title"] == "Paper One"
        assert results[0]["authors"] == ["Alice Smith"]
        assert results[1]["doi"] == "10.1234/paper2"

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_empty_on_no_results(self, mock_urlopen_fn):
        crossref_response = {"message": {"items": []}}
        mock_urlopen_fn.return_value = _mock_urlopen(crossref_response)

        results = search_crossref("Nonexistent Paper")
        assert results == []

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_empty_on_network_error(self, mock_urlopen_fn):
        import urllib.error

        mock_urlopen_fn.side_effect = urllib.error.URLError("Connection refused")
        assert search_crossref("Some Paper") == []


class TestSearchSemanticScholar:
    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_candidates(self, mock_urlopen_fn):
        response_data = {
            "data": [
                {"paperId": "abc123", "title": "Test Paper Title", "url": "https://example.com"},
                {"paperId": "def456", "title": "Related Paper", "url": "https://example.com/2"},
            ]
        }
        mock_urlopen_fn.return_value = _mock_urlopen(response_data)

        results = search_semantic_scholar("Test Paper Title")
        assert len(results) == 2
        assert results[0]["paperId"] == "abc123"
        assert results[0]["title"] == "Test Paper Title"

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_empty_on_no_results(self, mock_urlopen_fn):
        response_data = {"data": []}
        mock_urlopen_fn.return_value = _mock_urlopen(response_data)

        results = search_semantic_scholar("Nonexistent Paper")
        assert results == []

    @patch("saim.verification.citation.urllib.request.urlopen")
    def test_returns_empty_on_network_error(self, mock_urlopen_fn):
        import urllib.error

        mock_urlopen_fn.side_effect = urllib.error.URLError("Connection refused")
        assert search_semantic_scholar("Some Paper") == []

    @patch("saim.verification.citation.urllib.request.urlopen")
    @patch.dict("os.environ", {"S2_API_KEY": "test-key-123"})
    def test_sends_api_key_header_when_set(self, mock_urlopen_fn):
        response_data = {"data": []}
        mock_urlopen_fn.return_value = _mock_urlopen(response_data)

        search_semantic_scholar("Some Paper")

        req = mock_urlopen_fn.call_args[0][0]
        assert req.get_header("X-api-key") == "test-key-123"

    @patch("saim.verification.citation.urllib.request.urlopen")
    @patch.dict("os.environ", {}, clear=True)
    def test_no_api_key_header_when_unset(self, mock_urlopen_fn):
        response_data = {"data": []}
        mock_urlopen_fn.return_value = _mock_urlopen(response_data)

        search_semantic_scholar("Some Paper")

        req = mock_urlopen_fn.call_args[0][0]
        assert req.get_header("X-api-key") is None


class TestLookupCitations:
    @patch("saim.verification.citation.lookup_doi")
    @patch("saim.verification.citation.search_crossref")
    @patch("saim.verification.citation.search_semantic_scholar")
    def test_looks_up_doi_and_title(self, mock_s2, mock_crossref, mock_doi):
        mock_doi.return_value = {"doi": "10.1234/p1", "title": "Paper", "authors": [], "url": ""}
        mock_crossref.return_value = [{"doi": "10.1234/p1", "title": "Paper", "authors": []}]
        mock_s2.return_value = [{"paperId": "abc", "title": "Paper", "url": ""}]

        idea = {"citations": [{"doi": "10.1234/p1", "title": "Paper"}]}
        results = lookup_citations(idea)

        assert len(results) == 1
        assert results[0]["crossref_doi"] is not None
        assert len(results[0]["crossref_search"]) == 1
        assert len(results[0]["semantic_scholar"]) == 1

    @patch("saim.verification.citation.lookup_doi")
    @patch("saim.verification.citation.search_crossref")
    @patch("saim.verification.citation.search_semantic_scholar")
    def test_title_only_skips_doi_lookup(self, mock_s2, mock_crossref, mock_doi):
        mock_crossref.return_value = []
        mock_s2.return_value = []

        idea = {"citations": [{"title": "Some Paper"}]}
        results = lookup_citations(idea)

        assert len(results) == 1
        mock_doi.assert_not_called()
        assert results[0]["crossref_doi"] is None

    @patch("saim.verification.citation.lookup_doi")
    @patch("saim.verification.citation.search_crossref")
    @patch("saim.verification.citation.search_semantic_scholar")
    def test_doi_only_skips_title_searches(self, mock_s2, mock_crossref, mock_doi):
        mock_doi.return_value = {"doi": "10.1234/p1", "title": "Paper", "authors": [], "url": ""}

        idea = {"citations": [{"doi": "10.1234/p1"}]}
        results = lookup_citations(idea)

        assert len(results) == 1
        assert results[0]["crossref_doi"] is not None
        mock_crossref.assert_not_called()
        mock_s2.assert_not_called()

    def test_no_citations_returns_empty(self):
        assert lookup_citations({"title": "No citations"}) == []

    @patch("saim.verification.citation.lookup_doi")
    @patch("saim.verification.citation.search_crossref")
    @patch("saim.verification.citation.search_semantic_scholar")
    def test_multiple_citations(self, mock_s2, mock_crossref, mock_doi):
        mock_doi.return_value = None
        mock_crossref.return_value = []
        mock_s2.return_value = []

        idea = {
            "citations": [
                {"doi": "10.1/a", "title": "Paper A"},
                {"doi": "10.1/b", "title": "Paper B"},
            ]
        }
        results = lookup_citations(idea)
        assert len(results) == 2
        assert results[0]["citation"]["title"] == "Paper A"
        assert results[1]["citation"]["title"] == "Paper B"
