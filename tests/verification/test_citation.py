"""Tests for citation verification module."""

import json
from unittest.mock import MagicMock, patch

from safety_ideas.verification.citation import (
    filter_unverified,
    verify_citations,
    verify_doi,
    verify_semantic_scholar,
)


class TestVerifyDoi:
    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_valid_doi_returns_true(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        assert verify_doi("10.1234/test") is True

    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_invalid_doi_returns_false(self, mock_urlopen):
        import urllib.error

        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="", code=404, msg="Not Found", hdrs={}, fp=None
        )

        assert verify_doi("10.9999/nonexistent") is False

    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_network_error_returns_false(self, mock_urlopen):
        import urllib.error

        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        assert verify_doi("10.1234/test") is False


class TestVerifySemanticScholar:
    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_exact_title_match(self, mock_urlopen):
        response_data = {
            "data": [
                {"paperId": "abc123", "title": "Test Paper Title", "url": "https://example.com"}
            ]
        }
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(response_data).encode()
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = verify_semantic_scholar("Test Paper Title")
        assert result is not None
        assert result["paperId"] == "abc123"
        assert result["title"] == "Test Paper Title"

    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_no_results_returns_none(self, mock_urlopen):
        response_data = {"data": []}
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(response_data).encode()
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = verify_semantic_scholar("Nonexistent Paper")
        assert result is None

    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_close_match_returns_first(self, mock_urlopen):
        response_data = {
            "data": [
                {"paperId": "abc123", "title": "Similar Paper Title", "url": "https://example.com"}
            ]
        }
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(response_data).encode()
        mock_response.__enter__ = lambda s: s
        mock_response.__exit__ = MagicMock(return_value=False)
        mock_urlopen.return_value = mock_response

        result = verify_semantic_scholar("Different Paper Title")
        assert result is not None
        assert result["title"] == "Similar Paper Title"

    @patch("safety_ideas.verification.citation.urllib.request.urlopen")
    def test_network_error_returns_none(self, mock_urlopen):
        import urllib.error

        mock_urlopen.side_effect = urllib.error.URLError("Connection refused")

        result = verify_semantic_scholar("Some Paper")
        assert result is None


class TestVerifyCitations:
    @patch("safety_ideas.verification.citation.verify_doi")
    @patch("safety_ideas.verification.citation.verify_semantic_scholar")
    def test_all_verified_via_doi(self, mock_ss, mock_doi):
        mock_doi.return_value = True
        idea = {
            "citations": [
                {"doi": "10.1234/paper1", "title": "Paper One"},
                {"doi": "10.1234/paper2", "title": "Paper Two"},
            ]
        }
        result = verify_citations(idea)
        assert len(result["verified"]) == 2
        assert len(result["failed"]) == 0
        assert len(result["removed"]) == 0
        mock_ss.assert_not_called()

    @patch("safety_ideas.verification.citation.verify_doi")
    @patch("safety_ideas.verification.citation.verify_semantic_scholar")
    def test_fallback_to_semantic_scholar(self, mock_ss, mock_doi):
        mock_doi.return_value = False
        mock_ss.return_value = {"paperId": "abc", "title": "Paper One", "url": ""}
        idea = {
            "citations": [
                {"doi": "10.1234/bad", "title": "Paper One"},
            ]
        }
        result = verify_citations(idea)
        assert len(result["verified"]) == 1
        assert len(result["failed"]) == 0

    @patch("safety_ideas.verification.citation.verify_doi")
    @patch("safety_ideas.verification.citation.verify_semantic_scholar")
    def test_unverified_goes_to_failed(self, mock_ss, mock_doi):
        mock_doi.return_value = False
        mock_ss.return_value = None
        idea = {
            "citations": [
                {"doi": "10.1234/bad", "title": "Fake Paper"},
            ]
        }
        result = verify_citations(idea)
        assert len(result["verified"]) == 0
        assert len(result["failed"]) == 1
        assert len(result["removed"]) == 1

    def test_no_citations_returns_empty(self):
        idea = {"title": "No citations idea"}
        result = verify_citations(idea)
        assert result == {"verified": [], "failed": [], "removed": []}

    @patch("safety_ideas.verification.citation.verify_doi")
    @patch("safety_ideas.verification.citation.verify_semantic_scholar")
    def test_mixed_verified_and_failed(self, mock_ss, mock_doi):
        mock_doi.side_effect = [True, False]
        mock_ss.return_value = None
        idea = {
            "citations": [
                {"doi": "10.1234/good", "title": "Good Paper"},
                {"doi": "10.1234/bad", "title": "Bad Paper"},
            ]
        }
        result = verify_citations(idea)
        assert len(result["verified"]) == 1
        assert len(result["failed"]) == 1


class TestFilterUnverified:
    def test_removes_failed_citations(self):
        idea = {
            "title": "Test",
            "citations": [
                {"doi": "10.1234/good", "title": "Good Paper"},
                {"doi": "10.1234/bad", "title": "Bad Paper"},
            ],
        }
        verification = {
            "verified": ["10.1234/good"],
            "failed": ["10.1234/bad"],
            "removed": ["10.1234/bad"],
        }
        result = filter_unverified(idea, verification)
        assert len(result["citations"]) == 1
        assert result["citations"][0]["doi"] == "10.1234/good"

    def test_no_failed_returns_same(self):
        idea = {
            "title": "Test",
            "citations": [{"doi": "10.1234/good", "title": "Good Paper"}],
        }
        verification = {"verified": ["10.1234/good"], "failed": [], "removed": []}
        result = filter_unverified(idea, verification)
        assert len(result["citations"]) == 1

    def test_all_failed_removes_all(self):
        idea = {
            "title": "Test",
            "citations": [
                {"doi": "10.1234/bad1", "title": "Bad 1"},
                {"doi": "10.1234/bad2", "title": "Bad 2"},
            ],
        }
        verification = {
            "verified": [],
            "failed": ["10.1234/bad1", "10.1234/bad2"],
            "removed": ["10.1234/bad1", "10.1234/bad2"],
        }
        result = filter_unverified(idea, verification)
        assert len(result["citations"]) == 0

    def test_does_not_mutate_original(self):
        idea = {
            "title": "Test",
            "citations": [
                {"doi": "10.1234/good", "title": "Good"},
                {"doi": "10.1234/bad", "title": "Bad"},
            ],
        }
        verification = {
            "verified": ["10.1234/good"],
            "failed": ["10.1234/bad"],
            "removed": ["10.1234/bad"],
        }
        filter_unverified(idea, verification)
        assert len(idea["citations"]) == 2  # Original unchanged
