"""Shared fetcher machinery.

A fetcher has two jobs.

FETCH (the pipeline): given a registry entry, retrieve clean program text.
It returns a FetchResult with one of three outcomes:

  ok              -> got real content; orchestrator emits a prompt
  not_published   -> event is past but artifacts aren't up yet; retry next run
  manual_fallback -> auto-fetch blocked (bot detection); the human should open
                     manual_fallback_url, copy the program, and paste it in

The distinction between not_published and manual_fallback matters:
  - not_published is expected and silent (just try again in two weeks).
  - manual_fallback / repeated failure is what eventually trips the stall flag
    and tells you a site changed and the fetcher needs adjusting.

PROBE (discovery): given a *candidate* entry for an edition that is not in the
registry yet, cheaply answer "does this edition exist, and when does it end?"
scripts/discover_editions.py uses this to add next year's edition by itself.
The default probe is a single GET plus a date scan of the page, which is enough
for every HTML source we have; IETF overrides it with the datatracker API,
which states the dates outright.

A probe must never be trusted to *prove* an edition is digestible — discovery
confirms that by running the real fetch() afterwards and requiring OK.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Optional

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


@dataclass
class ProbeResult:
    """Does a candidate edition exist, and what do we know about it?

    exists    the URL served real content (not 404, not a bot challenge)
    end_date  the last day of the event, when the source states it. None means
              "couldn't tell" and the caller falls back to the series hint.
    location  city/venue, when the source states it; used to enrich the name.
    """

    exists: bool
    detail: str = ""
    end_date: Optional[date] = None
    location: str = ""
    source_url: str = ""


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


# --------------------------------------------------------------------------- #
# Date scanning (discovery only)
#
# Conference pages state their dates over and over — once per session row, per
# day header, in the footer. We exploit that: collect every date on the page,
# keep the ones in a plausible year, and let the MOST REPEATED month win. A
# stray "submissions close 15 January 2027" in one abstract can't outvote the
# 500 rows that all say March 2026. Within the winning month we take the latest
# day, which is the end of the event (co-located days included, deliberately —
# an end_date that is a day or two late only delays a digest, whereas one that
# is early can select an edition whose program is still half-empty).
# --------------------------------------------------------------------------- #

_MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
_MONTH_RE = (
    r"(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|"
    r"jul(?:y)?|aug(?:ust)?|sep(?:t)?(?:ember)?|oct(?:ober)?|"
    r"nov(?:ember)?|dec(?:ember)?)"
)
# "March 26, 2026" / "Mar 26 2026"
_MDY = re.compile(rf"\b{_MONTH_RE}\.?\s+(\d{{1,2}})(?:st|nd|rd|th)?,?\s+(\d{{4}})\b", re.I)
# "26 March 2026" / "26th Mar, 2026"
_DMY = re.compile(rf"\b(\d{{1,2}})(?:st|nd|rd|th)?\s+{_MONTH_RE}\.?,?\s+(\d{{4}})\b", re.I)
# "2026-03-26"
_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")


def _month_num(word: str) -> Optional[int]:
    return _MONTHS.get(word.lower().rstrip(".")[:4]) or _MONTHS.get(word.lower()[:3])


def find_dates(text: str) -> list[date]:
    """Every parseable calendar date in the text, duplicates kept."""
    out: list[date] = []

    def add(y: int, m: int, d: int) -> None:
        try:
            out.append(date(y, m, d))
        except ValueError:
            pass  # 31 February and friends

    for mon, day, year in _MDY.findall(text):
        m = _month_num(mon)
        if m:
            add(int(year), m, int(day))
    for day, mon, year in _DMY.findall(text):
        m = _month_num(mon)
        if m:
            add(int(year), m, int(day))
    for year, mon, day in _ISO.findall(text):
        add(int(year), int(mon), int(day))
    return out


def scan_end_date(text: str, years: Optional[Iterable[int]] = None) -> Optional[date]:
    """Best guess at the last day of the event described by this page.

    `years` restricts which dates count (the candidate edition's year, or a
    small window for ordinal-numbered series). Returns None when the page
    doesn't say anything usable — the caller then falls back to the series hint.
    """
    allowed = set(years) if years is not None else None
    dates = [d for d in find_dates(text) if allowed is None or d.year in allowed]
    if not dates:
        return None
    # Most-repeated (year, month) wins; ties break toward the earlier month so a
    # trailing "save the date for next year" block can't hijack the result.
    counts = Counter((d.year, d.month) for d in dates)
    top = max(counts.items(), key=lambda kv: (kv[1], -kv[0][0], -kv[0][1]))[0]
    return max(d for d in dates if (d.year, d.month) == top)


class Fetcher:
    """Base class. Subclasses implement fetch(); probe() is optional."""

    name = "base"

    # Does probe() alone prove an edition is real? False by default: an HTML
    # page can 200 with nothing but a "call for papers" on it, so discovery
    # confirms with a real fetch() before writing the edition to the registry.
    # Set True only when probe() hits an authoritative endpoint that answers
    # "does this edition exist" directly — it spares discovery a full fetch.
    probe_is_sufficient = False

    def fetch(self, entry: dict) -> FetchResult:  # pragma: no cover
        raise NotImplementedError

    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """Default discovery probe: one GET, then read the dates off the page.

        Works for every plain-HTML source (Sched, SIGCOMM, netdev, USENIX).
        Override when the source has an endpoint that states its dates.
        """
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)

        # 404 first: a site's "no such event" page often carries the same words
        # looks_blocked() keys on, and reporting "blocked" for what is really
        # "next year isn't up yet" sends you debugging the wrong thing.
        if resp.status_code == 404:
            return ProbeResult(False, "404 (no such edition yet)", source_url=url)
        if looks_blocked(resp):
            return ProbeResult(
                False, f"blocked ({resp.status_code} / challenge)", source_url=url
            )
        if resp.status_code != 200:
            return ProbeResult(False, f"unexpected status {resp.status_code}", source_url=url)

        resp.encoding = resp.encoding or "utf-8"
        end = scan_end_date(resp.text, years)
        return ProbeResult(
            True,
            f"200; dates {'scanned' if end else 'not found on page'}",
            end_date=end,
            source_url=url,
        )

    # convenience for subclasses
    @staticmethod
    def manual(entry: dict, detail: str) -> FetchResult:
        return FetchResult(
            status=MANUAL_FALLBACK,
            detail=detail,
            source_url=entry.get("manual_fallback_url", entry.get("program_url", "")),
        )
