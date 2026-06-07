"""Shared fetcher machinery.

A fetcher's job: given a registry entry, try to retrieve clean program text.
It returns a FetchResult with one of three outcomes:

  ok              -> got real content; orchestrator emits a prompt
  not_published   -> event is past but artifacts aren't up yet; retry next run
  manual_fallback -> auto-fetch blocked (bot detection); the human should open
                     manual_fallback_url, copy the program, and paste it in

The distinction between not_published and manual_fallback matters:
  - not_published is expected and silent (just try again in two weeks).
  - manual_fallback / repeated failure is what eventually trips the stall flag
    and tells you a site changed and the fetcher needs adjusting.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
import requests

# A realistic desktop-browser UA. USENIX and Sched challenge obvious bots.
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    ),
    "Accept-Language": "en-GB,en;q=0.9",
}

OK = "ok"
NOT_PUBLISHED = "not_published"
MANUAL_FALLBACK = "manual_fallback"


@dataclass
class FetchResult:
    status: str                      # OK | NOT_PUBLISHED | MANUAL_FALLBACK
    program_text: str = ""           # cleaned text, when status == OK
    detail: str = ""                 # human-readable note / error reason
    source_url: str = ""             # the URL actually used
    item_count: int = 0              # rough count of sessions parsed (sanity)
    meta: dict = field(default_factory=dict)


def http_get(url: str, timeout: int = 30) -> requests.Response:
    """GET with browser-like headers. Raises on transport errors."""
    return requests.get(url, headers=BROWSER_HEADERS, timeout=timeout)


def looks_blocked(resp: requests.Response) -> bool:
    """Heuristic: did we hit bot detection rather than real content?"""
    if resp.status_code in (403, 429, 503):
        return True
    body = resp.text.lower()
    markers = (
        "access denied",
        "are you a robot",
        "captcha",
        "cf-challenge",
        "request unsuccessful",
        "enable javascript and cookies",
    )
    return any(m in body for m in markers)


class Fetcher:
    """Base class. Subclasses implement fetch()."""

    name = "base"

    def fetch(self, entry: dict) -> FetchResult:  # pragma: no cover
        raise NotImplementedError

    # convenience for subclasses
    @staticmethod
    def manual(entry: dict, detail: str) -> FetchResult:
        return FetchResult(
            status=MANUAL_FALLBACK,
            detail=detail,
            source_url=entry.get("manual_fallback_url", entry.get("program_url", "")),
        )
