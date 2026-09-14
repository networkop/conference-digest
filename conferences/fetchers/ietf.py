"""IETF fetcher: assembles program substance from the datatracker JSON API.

DESIGN NOTE (revised after live probing):
The meeting-wide `agenda.json` is JS-dependent and its shape is unverified, so
we DON'T rely on it. Instead we iterate our own RELEVANT_WGS list and, for each,
pull that group's active Internet-Drafts via the documents API:

    /api/v1/doc/document/?format=json&group__acronym=<wg>&type=draft

This API is open (no key), returns JSON with an `objects` array, and does not
bot-block. Each object has `name`, `title`, `abstract`, and state info. We keep
drafts that look active (filtered client-side rather than trusting an exact
state slug, which is the brittle part of the API).

We use the meeting number only to (a) label the digest and (b) confirm the
meeting exists. Whether a given WG literally met at meeting N is less important
than surfacing that WG's current drafts for the PM around that meeting's time.

Outcomes:
  OK              -> at least one relevant WG returned drafts
  NOT_PUBLISHED   -> meeting endpoint 404 / nothing came back yet
  MANUAL_FALLBACK -> transport error (API doesn't bot-block, so this is rare)
"""

from __future__ import annotations

import json
import re
from datetime import date, timedelta
from typing import Iterable, Optional

from .base import Fetcher, FetchResult, ProbeResult, http_get, OK, NOT_PUBLISHED

# WGs whose work touches cloud-native networking, network security, identity.
RELEVANT_WGS = {
    # identity / auth
    "oauth", "wimse", "scitt", "spice", "rats", "jose", "cose", "secdispatch",
    # transport / datapath / proxying
    "masque", "quic", "tls", "tsvwg", "httpbis", "tcpm",
    # routing / addressing / ops
    "idr", "grow", "savnet", "rtgwg", "6man", "v6ops", "dnsop", "add",
    # security infra
    "ipsecme", "anima", "acme", "lamps", "pquip",
    # network virtualization / service
    "nvo3", "rift", "bess",
}

API = "https://datatracker.ietf.org"
# active-ish document states we keep (slugs vary; match loosely, case-insensitive)
ACTIVE_HINTS = ("active", "wg document", "candidate", "adopted", "i-d exists")


class IetfFetcher(Fetcher):
    name = "ietf"

    # probe() asks datatracker's meeting API outright, so discovery needs no
    # second opinion. It also saves real work: fetch() walks ~30 WG endpoints,
    # and it would do so for every candidate meeting number — while returning
    # OK off the back of current WG drafts, which say nothing about whether
    # meeting 128 exists. The probe is both cheaper and more informative here.
    probe_is_sufficient = True

    def fetch(self, entry: dict) -> FetchResult:
        meeting_url = entry["program_url"]  # e.g. .../meeting/122/agenda.json

        # Confirm the meeting exists at all (cheap sanity check).
        try:
            ping = http_get(meeting_url)
        except Exception as e:
            return self.manual(entry, f"request error reaching meeting: {e}")
        if ping.status_code == 404:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="meeting endpoint 404 (not posted yet?)",
                source_url=meeting_url,
            )

        lines: list[str] = []
        count = 0
        wgs_with_content = 0

        for wg in sorted(RELEVANT_WGS):
            drafts = self._wg_active_drafts(wg)
            if not drafts:
                continue
            wgs_with_content += 1
            lines.append(f"## Working Group: {wg}")
            for d in drafts:
                count += 1
                lines.append(f"### {d['title']}  ({d['name']})")
                if d.get("abstract"):
                    lines.append(d["abstract"])
                lines.append("")

        if count == 0:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="no active drafts retrieved for relevant WGs (API shape changed?)",
                source_url=meeting_url,
            )

        return FetchResult(
            status=OK,
            program_text="\n".join(lines),
            source_url=meeting_url,
            item_count=count,
            detail=f"{wgs_with_content} WGs, {count} active drafts",
        )


    def probe(self, entry: dict, years: Optional[Iterable[int]] = None) -> ProbeResult:
        """Discovery probe via the datatracker meeting API.

        Unlike the HTML sources, IETF states its schedule outright:

            /api/v1/meeting/meeting/?number=<n>&format=json
            -> {"objects": [{"number", "date", "days", "city", ...}]}

        `date` is day one and `days` the length, so end_date is exact and the
        city gives the edition its "(Montreal)" suffix. Meetings are published
        years ahead, so a hit here is NOT "the meeting happened" — it is "this
        meeting number is real", which is precisely what discovery needs. The
        end_date then keeps the selection gate honest.
        """
        url = entry["program_url"]
        number = self._meeting_number(url)
        if not number:
            return super().probe(entry, years)

        api = f"{API}/api/v1/meeting/meeting/?number={number}&format=json"
        try:
            resp = http_get(api)
        except Exception as e:
            return ProbeResult(False, f"request error: {e}", source_url=url)
        if resp.status_code != 200:
            return ProbeResult(False, f"meeting API status {resp.status_code}", source_url=url)

        try:
            objects = resp.json().get("objects") or []
        except Exception as e:
            return ProbeResult(False, f"meeting API not JSON: {e}", source_url=url)
        if not objects:
            return ProbeResult(False, f"no meeting {number} scheduled yet", source_url=url)

        m = objects[0]
        # Only real IETF meetings; the same table also holds interims.
        if "meetingtypename/ietf" not in (m.get("type") or ""):
            return ProbeResult(False, f"meeting {number} is not a plenary IETF meeting",
                               source_url=url)

        end = None
        try:
            start = date.fromisoformat(m["date"])
            end = start + timedelta(days=max(int(m.get("days") or 1) - 1, 0))
        except Exception:
            pass

        return ProbeResult(
            True,
            f"meeting {number} scheduled" + (f", ends {end}" if end else ""),
            end_date=end,
            location=(m.get("city") or "").strip(),
            source_url=url,
        )

    @staticmethod
    def _meeting_number(url: str) -> str:
        m = re.search(r"/meeting/(\d+)/", url)
        return m.group(1) if m else ""

    def _wg_active_drafts(self, wg: str) -> list[dict]:
        url = (
            f"{API}/api/v1/doc/document/?format=json&limit=60"
            f"&group__acronym={wg}&type=draft"
        )
        try:
            resp = http_get(url)
            if resp.status_code != 200:
                return []
            data = resp.json()
        except (json.JSONDecodeError, Exception):
            return []

        out: list[dict] = []
        for obj in data.get("objects", []):
            # keep only drafts that look current; skip expired/replaced.
            states = " ".join(str(s) for s in (obj.get("states") or [])).lower()
            std_level = (obj.get("std_level") or "")
            # heuristic: if there's any active-ish hint, or no state info at all
            # (older API rows), include it; the prompt tolerates some noise.
            if states and not any(h in states for h in ACTIVE_HINTS):
                # explicitly drop clearly dead states
                if "expired" in states or "replaced" in states or "rfc" in states:
                    continue
            out.append(
                {
                    "name": obj.get("name", ""),
                    "title": (obj.get("title") or "").strip() or obj.get("name", ""),
                    "abstract": (obj.get("abstract") or "").strip(),
                }
            )
        return out
