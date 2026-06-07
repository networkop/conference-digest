"""SIGCOMM fetcher.

The SIGCOMM site is static, server-rendered HTML at a predictable path:

    https://conferences.sigcomm.org/sigcomm/<year>/program/papers-info/

The accepted-papers program is a real <table> organised by day -> session.
Row shapes (confirmed against the live 2025 page):

  session header row:
    <td id="session-xxx">
      <p><span class="text-color-primary">09:00 — 10:20 | NetAI</span></p>
      <p class="style_italic"><span ...>Session Chair:</span> Name</p>
    </td> ...
  paper row:
    <td>
      <p><span class="text-color-primary">PAPER TITLE</span></p>
      <p class="style_italic">Author A (Aff); Author B (Aff); ...</p>
    </td>
    <td>...abstract toggle...</td>
    <td><a href="https://dl.acm.org/doi/...">PDF</a></td>
    <td><a href="https://youtu.be/...">video</a></td>
  abstract row:
    <td> ... Abstract: <full text> ... </td>

So: title and authors are SEPARATE <p> elements (no <br>). We detect a paper
row as one whose first cell has a title <p> AND the row carries a PDF/video
link or is immediately followed by an "Abstract:" row. Session headers are
detected by the "HH:MM ... | Name" text (and/or the td id="session-").

Encoding: the server doesn't always advertise UTF-8, so we force it to avoid
mojibake in dashes/abstracts.
"""

from __future__ import annotations

import re
from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED

_SESSION_RE = re.compile(r"\d{1,2}:\d{2}.*\|\s*(.+)$")


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

        # Force UTF-8: the page contains em-dashes and accented author names
        # that arrive garbled if requests guesses latin-1.
        resp.encoding = "utf-8"

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

        for row in soup.find_all("tr"):
            cells = row.find_all("td")
            if not cells:
                continue
            first = cells[0]

            # --- abstract row: first cell text starts with "Abstract:" ---
            cell_text = first.get_text(" ", strip=True)
            if cell_text.lower().startswith("abstract:"):
                abstract = cell_text[len("abstract:"):].strip()
                if abstract:
                    lines.append(abstract)
                    lines.append("")
                continue

            # --- session header: td#session-* OR "HH:MM ... | Name" text ---
            td_id = first.get("id", "")
            if td_id.startswith("session-") or _SESSION_RE.search(cell_text):
                m = _SESSION_RE.search(cell_text)
                name = m.group(1).strip() if m else cell_text
                # drop any trailing "Session Chair: ..." that shares the cell
                name = re.split(r"Session Chair", name)[0].strip(" |")
                if name:
                    lines.append(f"## Session: {name}")
                    lines.append("")
                continue

            # --- paper row: title in first <p>, authors in <p.style_italic> ---
            ps = first.find_all("p")
            if not ps:
                continue
            title = ps[0].get_text(" ", strip=True)
            if not title:
                continue
            # authors: the italic <p> if present, else the second <p>
            author_p = first.find("p", class_="style_italic")
            if author_p is None and len(ps) > 1:
                author_p = ps[1]
            authors = author_p.get_text(" ", strip=True) if author_p else ""

            # require some signal this is really a paper: an author line, or a
            # PDF/video link in the row. Otherwise skip (stray <p> cell).
            row_links = [a.get("href", "") for a in row.find_all("a")]
            video = next((h for h in row_links if "youtu" in h), "")
            pdf = next((h for h in row_links if "dl.acm.org" in h), "")
            if not (authors or video or pdf):
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

        return "\n".join(lines), count
