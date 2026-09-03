"""Netdev fetcher: netdevconf.info (Netdev 0x1A and friends).

The sessions index is static, server-rendered HTML at a predictable path:

    https://netdevconf.info/<edition>/pages/sessions.html

It lists every accepted session grouped by kind (talk / tutorial / workshop /
bof / keynote), but carries ONLY title + speakers — no abstracts. The substance
lives on each session's own page:

    https://netdevconf.info/<edition>/sessions/<kind>/<slug>.html

which has the description, the session label (track), and a "Contents" list
linking slides/papers (PDF) and the recording (YouTube). So this fetcher does
two passes: parse the index, then fetch each session page for its description
and links. 40-ish sessions per edition, so the fan-out is small.

A session page that fails to fetch degrades gracefully: the session still
appears in the program text with title + speakers, just without an abstract.
Only a failure of the INDEX page is fatal (manual fallback / not published).

No bot-blocking observed; the site is plain Jekyll-built HTML.
"""

from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

# "Speakers: A  and B" / "Speaker: A" with the newline-heavy Jekyll whitespace.
_SPEAKER_PREFIX = re.compile(r"^Speakers?:\s*", re.I)
_WS = re.compile(r"\s+")


def _clean(text: str) -> str:
    """Collapse the template's ragged whitespace into single spaces."""
    return _WS.sub(" ", text).strip()


class NetdevFetcher(Fetcher):
    name = "netdev"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")

        if looks_blocked(resp):
            return self.manual(entry, f"netdevconf returned {resp.status_code} / challenge")
        if resp.status_code != 200:
            return self.manual(entry, f"unexpected status {resp.status_code}")
        resp.encoding = "utf-8"

        sessions = self._parse_index(resp.text, url)
        if not sessions:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="sessions page reachable but no session articles found "
                       "(accepted sessions likely not posted yet)",
                source_url=url,
            )

        lines: list[str] = []
        current_kind = None
        enriched = 0
        for s in sessions:
            if s["kind"] != current_kind:
                current_kind = s["kind"]
                lines.append(f"## Session type: {current_kind}")
                lines.append("")

            detail = self._fetch_detail(s["page"])
            if detail.get("description"):
                enriched += 1

            lines.append(f"### {s['title']}")
            if s["speakers"]:
                lines.append(f"Speakers: {s['speakers']}")
            if detail.get("label"):
                lines.append(f"Track: {detail['label']}")
            meta = [f"page: {s['page']}"]
            if detail.get("pdf"):
                meta.append(f"pdf: {detail['pdf']}")
            if detail.get("video"):
                meta.append(f"video: {detail['video']}")
            lines.append(" | ".join(meta))
            if detail.get("description"):
                lines.append(detail["description"])
            lines.append("")

        return FetchResult(
            status=OK,
            program_text="\n".join(lines),
            source_url=url,
            item_count=len(sessions),
            detail=f"parsed {len(sessions)} sessions ({enriched} with descriptions)",
        )

    # --- index page -------------------------------------------------------

    def _parse_index(self, html: str, base_url: str) -> list[dict]:
        soup = BeautifulSoup(html, "html.parser")
        out: list[dict] = []

        # Each kind is a <div id="talk-sessions"> etc. holding .session-article
        # blocks. Fall back to a flat scan if the ids ever change.
        containers = soup.select('div[id$="-sessions"]')
        if not containers:
            containers = [soup]

        for container in containers:
            cid = container.get("id", "") if hasattr(container, "get") else ""
            kind = cid[: -len("-sessions")] if cid.endswith("-sessions") else "session"
            for art in container.select("div.session-article"):
                link = art.select_one("a.session-link")
                if link is None:
                    continue
                title = _clean(link.get_text(" "))
                if not title:
                    continue
                page = urljoin(base_url, link.get("href", ""))
                speaker_el = art.select_one("p.speaker")
                speakers = ""
                if speaker_el:
                    speakers = _SPEAKER_PREFIX.sub(
                        "", _clean(speaker_el.get_text(" "))
                    ).strip()
                out.append(
                    {"kind": kind, "title": title, "speakers": speakers, "page": page}
                )
        return out

    # --- per-session page -------------------------------------------------

    def _fetch_detail(self, page_url: str) -> dict:
        """Best effort. Any failure just means a thinner entry, never a hard fail."""
        try:
            resp = http_get(page_url)
            if resp.status_code != 200 or looks_blocked(resp):
                return {}
            resp.encoding = "utf-8"
        except Exception:
            return {}

        soup = BeautifulSoup(resp.text, "html.parser")
        detail: dict = {}

        desc_el = soup.select_one("section.post-excerpt")
        if desc_el:
            # Keep paragraph breaks; the description is often several paragraphs.
            paras = [_clean(p.get_text(" ")) for p in desc_el.find_all("p")]
            text = "\n".join(p for p in paras if p) or _clean(desc_el.get_text(" "))
            detail["description"] = text.strip()

        tags_el = soup.select_one("#session-tags")
        if tags_el:
            # e.g. "talk, Nuts and Bolts" -> drop the kind, keep the track label
            parts = [p.strip() for p in tags_el.get_text(strip=True).split(",")]
            label = ", ".join(p for p in parts[1:] if p)
            if label:
                detail["label"] = label

        for a in soup.select("div.session-content a[href]"):
            href = urljoin(page_url, a["href"])
            text = a.get_text(" ", strip=True).lower()
            if "video" in text or "youtu" in href:
                detail.setdefault("video", href)
            elif href.lower().endswith(".pdf"):
                detail.setdefault("pdf", href)

        return detail
