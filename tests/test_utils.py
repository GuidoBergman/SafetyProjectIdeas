"""Tests for shared utility functions."""

import urllib.error

import pytest

from saim.utils import retry_on_rate_limit


class TestRetryOnRateLimit:
    def test_returns_immediately_on_success(self):
        result = retry_on_rate_limit(lambda: "ok")
        assert result == "ok"

    def test_retries_on_429_then_succeeds(self):
        calls = {"count": 0}
        delays = []

        def fake_sleep(seconds):
            delays.append(seconds)

        def flaky():
            calls["count"] += 1
            if calls["count"] < 3:
                raise urllib.error.HTTPError(
                    url="", code=429, msg="Too Many Requests", hdrs={}, fp=None
                )
            return "recovered"

        result = retry_on_rate_limit(flaky, initial_delay=0.5, sleep_fn=fake_sleep)
        assert result == "recovered"
        assert calls["count"] == 3
        assert delays == [0.5, 1.0]

    def test_raises_after_max_retries_exhausted(self):
        delays = []

        def fake_sleep(seconds):
            delays.append(seconds)

        def always_429():
            raise urllib.error.HTTPError(
                url="", code=429, msg="Too Many Requests", hdrs={}, fp=None
            )

        with pytest.raises(urllib.error.HTTPError) as exc_info:
            retry_on_rate_limit(
                always_429, max_retries=2, initial_delay=1.0, sleep_fn=fake_sleep
            )
        assert exc_info.value.code == 429
        assert len(delays) == 2

    def test_non_429_error_raises_immediately(self):
        delays = []

        def fake_sleep(seconds):
            delays.append(seconds)

        def server_error():
            raise urllib.error.HTTPError(
                url="", code=500, msg="Internal Server Error", hdrs={}, fp=None
            )

        with pytest.raises(urllib.error.HTTPError) as exc_info:
            retry_on_rate_limit(server_error, sleep_fn=fake_sleep)
        assert exc_info.value.code == 500
        assert delays == []

    def test_exponential_backoff_delays(self):
        delays = []

        def fake_sleep(seconds):
            delays.append(seconds)

        calls = {"count": 0}

        def flaky():
            calls["count"] += 1
            if calls["count"] <= 4:
                raise urllib.error.HTTPError(
                    url="", code=429, msg="Too Many Requests", hdrs={}, fp=None
                )
            return "done"

        result = retry_on_rate_limit(
            flaky,
            max_retries=4,
            initial_delay=1.0,
            backoff_factor=2.0,
            sleep_fn=fake_sleep,
        )
        assert result == "done"
        assert delays == [1.0, 2.0, 4.0, 8.0]
