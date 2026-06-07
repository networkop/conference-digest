"""SIGCOMM fetcher.

The SIGCOMM site is static, server-rendered HTML at a predictable path:

    https://conferences.sigcomm.org/sigcomm/<year>/program/papers-info/

The accepted-papers program is a TABLE organised by day -> session. Each paper
occupies a row whose first cell holds the title (before a <br>) and the author
list (after it), followed by cells linking to the abstract toggle, the ACM DL
PDF, and a YouTube video. The very next row's cell begins "Abstract:" and holds
the full abstract.

No JS wall, no bot-block observed (unlike USENIX/Sched), so this is the most
reliable scraper of the set. We still keep the manual-fallback path for safety.

We extract, per paper: title, authors, abstract, and the video URL when present
(richer than the other fetchers). Session headings become "##" lines so the
prompt preserves SIGCOMM's own topical grouping (Datacenter, Measurements,
Hardware, NetAI, etc.).
"""

from __future__ import annotations

import re
from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

# A session header cell looks like "09:00 — 10:20 | NetAI" possibly followed by
# "Session Chair: ...". We pull the human session name after the pipe.
_SESSION_RE = re.compile(r"\|\s*([A-Za-z0-9 /&+-]+?)(?:\s*Session Chair.*)?$")


class SigcommFetcher(Fetcher):
    name = "sigcomm"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")

        if looks_blocked(resp):
            return self.manual(entry, f"SIGCOMM returned {resp.status_code} / challenge")
        if resp.status_code != 200:
            return self.manual(entry, f"unexpected status {resp.status_code}")

        text, count = self._parse(resp.text)
        if count == 0:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="page reachable but no paper rows parsed (program not up yet?)",
                source_url=url,
            )
        return FetchResult(
            status=OK,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} papers",
        )

    def _parse(self, html: str) -> tuple[str, int]:
        soup = BeautifulSoup(html, "html.parser")
        lines: list[str] = []
        count = 0

        # Walk every table row in document order. A row is one of:
        #   - a day header     (single cell, "Day N - ...")
        #   - a session header (cell with "HH:MM ... | SessionName")
        #   - a paper row      (cell with title<br>authors, + pdf/video cells)
        #   - an abstract row  (cell starting "Abstract:")
        pending_paper: dict | None = None

        for row in soup.find_all("tr"):
            cells = row.find_all(["td", "th"])
            if not cells:
                continue
            first = cells[0]
            first_text = first.get_text(" ", strip=True)

            # abstract row: attach to the paper we just emitted
            if first_text.lower().startswith("abstract:") and pending_paper is not None:
                abstract = first_text[len("abstract:"):].strip()
                if abstract:
                    lines.append(abstract)
                lines.append("")
                pending_paper = None
                continue

            # session header: contains a time range and a pipe
            if "|" in first_text and re.match(r"\s*\d{1,2}:\d{2}", first_text):
                m = _SESSION_RE.search(first_text)
                name = m.group(1).strip() if m else first_text
                lines.append(f"## Session: {name}")
                lines.append("")
                continue

            # day header: single cell, starts with "Day"
            if first_text.startswith("Day ") and len(cells) == 1:
                lines.append(f"# {first_text}")
                lines.append("")
                continue

            # paper row: title is the text before the first <br>, authors after.
            # We detect it by the presence of a <br> in the first cell AND a
            # video/pdf link somewhere in the row.
            br = first.find("br")
            row_links = [a.get("href", "") for a in row.find_all("a")]
            video = next((h for h in row_links if "youtu" in h), "")
            pdf = next((h for h in row_links if "dl.acm.org" in h), "")

            if br is not None:
                # split first cell on the <br>
                parts = first.get_text("\n", strip=True).split("\n", 1)
                title = parts[0].strip()
                authors = parts[1].strip() if len(parts) > 1 else ""
                if not title:
                    continue
                count += 1
                lines.append(f"### {title}")
                if authors:
                    lines.append(f"Authors: {authors}")
                meta = []
                if video:
                    meta.append(f"video: {video}")
                if pdf:
                    meta.append(f"pdf: {pdf}")
                if meta:
                    lines.append(" | ".join(meta))
                pending_paper = {"title": title}
                continue

        return "\n".join(lines), count
