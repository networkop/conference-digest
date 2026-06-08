"""USENIX fetcher: NSDI, USENIX Security, SREcon.

Program pages are server-rendered HTML with a consistent structure. Each
session/paper is a node with a title (linked to its detail page), an author
line, and an abstract that may be collapsed in the markup.

USENIX bot-blocks. Strategy per the agreed plan:
  1. Try a normal GET with browser-like headers.
  2. If blocked -> return MANUAL_FALLBACK (you paste the page in yourself).
  3. If reachable but the program list is empty -> NOT_PUBLISHED (retry later).

SREcon uses /program; NSDI & Security use /technical-sessions. Both render
session nodes similarly enough for one parser; we just take whatever
title/author/abstract blocks we find.
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED


class UsenixFetcher(Fetcher):
    name = "usenix"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:  # transport failure == treat as manual fallback
            return self.manual(entry, f"request error: {e}")

        if looks_blocked(resp):
            return self.manual(
                entry,
                f"USENIX returned {resp.status_code} / bot challenge; "
                f"open the page and paste the program manually.",
            )

        if resp.status_code != 200:
            return self.manual(entry, f"unexpected status {resp.status_code}")

        text, count = self._parse(resp.text)

        if count == 0:
            # reachable but nothing to show -> artifacts likely not up yet
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="page reachable but no session nodes found (program likely not published yet)",
                source_url=url,
            )

        return FetchResult(
            status=OK,
            program_text=text,
            source_url=url,
            item_count=count,
            detail=f"parsed {count} sessions",
        )

    def _parse(self, html: str) -> tuple[str, int]:
        soup = BeautifulSoup(html, "html.parser")
        lines: list[str] = []
        count = 0

        # USENIX session nodes are typically article/div blocks whose title is
        # an <h2> within a node--paper / node--session container. We stay
        # tolerant: find heading nodes that link to a /presentation/ or
        # /conference/.../presentation page, then gather siblings.
        nodes = soup.select(
            "div.node-paper, div.node-session, article.node, "
            "div.views-row, h2.node-title"
        )

        seen_titles: set[str] = set()
        for node in nodes:
            title_el = node.find(["h2", "h3"]) or node
            title = title_el.get_text(" ", strip=True)
            if not title or title in seen_titles:
                continue

            # authors: usenix uses .field-name-field-paper-people-text or
            # a .people / .authors block; fall back to the next <p>.
            author_el = node.select_one(
                ".field-paper-people-text, .field-name-field-paper-people-text, "
                ".people, .authors, .field-pc-affiliation"
            )
            authors = author_el.get_text(" ", strip=True) if author_el else ""

            abstract_el = node.select_one(
                ".field-paper-description, .field-name-field-paper-description, "
                ".abstract, .field-session-description"
            )
            abstract = abstract_el.get_text(" ", strip=True) if abstract_el else ""

            if not (authors or abstract):
                # probably a nav/heading false positive; skip
                continue

            # Links: USENIX is open access. The title links to the paper's
            # presentation page (which carries the free PDF + slides). Capture
            # that page URL, plus any direct .pdf link in the node, so the
            # digesting session can fetch the full paper to enrich the digest.
            page_url = ""
            title_link = title_el.find("a") if hasattr(title_el, "find") else None
            if title_link is None:
                title_link = node.find("a", href=True)
            if title_link and title_link.get("href"):
                href = title_link["href"]
                page_url = href if href.startswith("http") else f"https://www.usenix.org{href}"

            pdf_url = ""
            for a in node.find_all("a", href=True):
                if a["href"].lower().endswith(".pdf"):
                    h = a["href"]
                    pdf_url = h if h.startswith("http") else f"https://www.usenix.org{h}"
                    break

            seen_titles.add(title)
            count += 1
            lines.append(f"### {title}")
            if authors:
                lines.append(f"Authors: {authors}")
            meta = []
            if pdf_url:
                meta.append(f"pdf: {pdf_url}")
            if page_url:
                meta.append(f"page: {page_url}")
            if meta:
                lines.append(" | ".join(meta))
            if abstract:
                lines.append(abstract)
            lines.append("")

        # Fallback: if structured parse found nothing, dump readable text so a
        # human at least gets *something* (and count stays 0 -> NOT_PUBLISHED).
        return "\n".join(lines), count
