"""Shared utility functions for SAIM."""

from __future__ import annotations

import logging
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable, TypeVar

import yaml

logger = logging.getLogger(__name__)

T = TypeVar("T")


def load_yaml(path: Path) -> dict:
    """Load a YAML file and return its contents as a dictionary.

    Args:
        path: Path to the YAML file.

    Returns:
        Parsed YAML contents.

    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If the file contains invalid YAML.
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path) as f:
        data = yaml.safe_load(f)
    if data is None:
        return {}
    return data


def retry_on_rate_limit(
    fn: Callable[[], T],
    *,
    max_retries: int = 10,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> T:
    """Call *fn* with exponential backoff on HTTP 429 responses.

    Args:
        fn: Zero-argument callable that performs the HTTP request and returns
            a result.  It should raise ``urllib.error.HTTPError`` on failure.
        max_retries: Maximum number of retry attempts after a 429.
        initial_delay: Seconds to wait before the first retry.
        backoff_factor: Multiplier applied to the delay after each retry.
        sleep_fn: Injectable sleep function (for testing).

    Returns:
        The return value of *fn* on success.

    Raises:
        urllib.error.HTTPError: Re-raised if *fn* raises a non-429 HTTP error,
            or if retries are exhausted.
    """
    delay = initial_delay
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == max_retries:
                raise
            logger.warning(
                "Rate limited (429), retrying in %.1fs (attempt %d/%d)",
                delay,
                attempt + 1,
                max_retries,
            )
            sleep_fn(delay)
            delay *= backoff_factor
    # Unreachable, but satisfies the type checker.
    raise RuntimeError("retry_on_rate_limit: unreachable")
