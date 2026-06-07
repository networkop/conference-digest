#!/usr/bin/env python3
"""Render run_summary.json into a GitHub Issue title + body (markdown).

Writes issue_title.txt and issue_body.md for the workflow's github-script step
to consume. Keeps the prompt OUT of the body (prompts can be large); instead it
links to the committed prompts/<key>.md and tells you what to do.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
summary = json.loads((ROOT / "run_summary.json").read_text(encoding="utf-8"))

ready = summary.get("ready", [])
manual = summary.get("manual", [])
waiting = summary.get("waiting", [])
stalled = summary.get("stalled", [])

title = f"Conference digests ready — {date.today().isoformat()} ({len(ready)} ready)"

lines = []
lines.append(f"_Run mode: **{summary.get('mode')}** · generated {summary.get('generated')}_")
lines.append("")

if ready:
    lines.append("## ✅ Ready to digest")
    lines.append("Open the prompt file, copy it whole, paste into Claude Desktop, "
                 "then commit the result to `digests/<key>.md`.")
    lines.append("")
    for r in ready:
        lines.append(f"- **{r['name']}** — `{r['items']}` items  ")
        lines.append(f"  prompt: [`prompts/{r['key']}.md`](../blob/main/prompts/{r['key']}.md) "
                     f"→ commit to `digests/{r['key']}.md`")
    lines.append("")

if manual:
    lines.append("## ✋ Needs manual fetch (auto-fetch blocked)")
    lines.append("The site blocked automated retrieval. Open the page, copy the program, "
                 "and paste it where the prompt says `{PROGRAM_TEXT}`.")
    lines.append("")
    for r in manual:
        lines.append(f"- **{r['name']}** — attempt {r['attempts']}: {r['detail']}  ")
        if r.get("manual_url"):
            lines.append(f"  page: {r['manual_url']}")
    lines.append("")

if stalled:
    lines.append("## ⚠️ Stalled — fetcher likely needs adjusting")
    lines.append(f"These have failed {summary['counts'].get('stalled', '?')}+ times. "
                 "The site structure or URL probably changed.")
    lines.append("")
    for r in stalled:
        lines.append(f"- **{r['name']}** — {r['attempts']} attempts: {r['detail']}")
    lines.append("")

if waiting:
    lines.append("## ⏳ Waiting on publication (will retry)")
    for r in waiting:
        lines.append(f"- {r['name']} — {r['detail']}")
    lines.append("")

(ROOT / "issue_title.txt").write_text(title + "\n", encoding="utf-8")
(ROOT / "issue_body.md").write_text("\n".join(lines), encoding="utf-8")
print("issue title:", title)
