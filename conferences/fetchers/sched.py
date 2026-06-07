"""Sched fetcher: KubeCon / CNCF and other Sched-hosted events.

The Sched *management* API needs an organizer key we don't have. But the
public schedule is plain HTML and needs no key. The cleanest public surface is
the "list with descriptions" view:

    https://<event>.sched.com/list/descriptions/

which renders every session's title, time, speakers, and full description in
one long page. We parse that. Same bot-block risk as USENIX -> same
manual-fallback escape hatch.

If the event's Sched is set Private, the descriptions view won't expose
content -> NOT_PUBLISHED (or MANUAL_FALLBACK on an outright block).
"""

from __future__ import annotations

from bs4 import BeautifulSoup

from .base import Fetcher, FetchResult, http_get, looks_blocked, OK, NOT_PUBLISHED


class SchedFetcher(Fetcher):
    name = "sched"

    def fetch(self, entry: dict) -> FetchResult:
        url = entry["program_url"]
        try:
            resp = http_get(url)
        except Exception as e:
            return self.manual(entry, f"request error: {e}")

        if looks_blocked(resp):
            return self.manual(
                entry,
                f"Sched returned {resp.status_code} / challenge; "
                f"open the schedule and paste it manually.",
            )
        if resp.status_code != 200:
            return self.manual(entry, f"unexpected status {resp.status_code}")

        text, count = self._parse(resp.text)
        if count == 0:
            return FetchResult(
                status=NOT_PUBLISHED,
                detail="schedule reachable but no sessions parsed (not published / private?)",
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

        # In the descriptions list view each session is an article/row with an
        # event title link and a description block. Sched markup uses
        # .sched-container / .event classes; we stay tolerant.
        rows = soup.select(
            "div.sched-container, article.sched-event, div.event, "
            "div.list-simple .sched-container-inner"
        )

        for row in rows:
            title_el = row.select_one("h2, h3, a.name, span.event-name, .sched-event-name")
            title = title_el.get_text(" ", strip=True) if title_el else ""
            if not title:
                continue

            speakers_el = row.select_one(".sched-event-details-roles, .speakers, .sched-person")
            speakers = speakers_el.get_text(" ", strip=True) if speakers_el else ""

            desc_el = row.select_one(".tip-description, .sched-event-description, .description")
            desc = desc_el.get_text(" ", strip=True) if desc_el else ""

            if not (speakers or desc):
                continue

            count += 1
            lines.append(f"### {title}")
            if speakers:
                lines.append(f"Speakers: {speakers}")
            if desc:
                lines.append(desc)
            lines.append("")

        return "\n".join(lines), count
