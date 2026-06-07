#!/usr/bin/env python3
"""Render run_summary.json into a set of per-conference GitHub issues.

Writes issues.json: a list of {key, title, body, labels} objects, one per
conference that needs attention (ready / manual / stalled). The workflow's
github-script step loops over this and opens one issue each, idempotently
(it skips a conference that already has an open issue with the same conf label).

Each issue carries a label "conf:<key>" so the close-workflow can find and
close it when digests/<key>.md lands on main.

"waiting" conferences get NO issue (they're just silently retried next run).
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
summary = json.loads((ROOT / "run_summary.json").read_text(encoding="utf-8"))

today = date.today().isoformat()
issues = []


def conf_label(key: str) -> str:
    return f"conf:{key}"


for r in summary.get("ready", []):
    key = r["key"]
    body = (
        f"**{r['name']}** — {r['items']} items parsed.\n\n"
        "Ready to digest. Open the prompt, run it (in Claude Desktop with repo "
        "access, or paste it), and commit the result to "
        f"`digests/{key}.md`.\n\n"
        f"Prompt: [`prompts/{key}.md`](../blob/main/prompts/{key}.md)\n\n"
        f"This issue closes automatically once `digests/{key}.md` is committed "
        "to `main`."
    )
    issues.append(
        {
            "key": key,
            "title": f"Digest ready: {r['name']}",
            "body": body,
            "labels": ["digest", conf_label(key)],
        }
    )

for r in summary.get("manual", []):
    key = r["key"]
    body = (
        f"**{r['name']}** — auto-fetch blocked (attempt {r['attempts']}).\n\n"
        f"{r['detail']}\n\n"
        "Open the page below, copy the program, and paste it where the prompt "
        f"says `{{PROGRAM_TEXT}}`, then run and commit to `digests/{key}.md`.\n\n"
    )
    if r.get("manual_url"):
        body += f"Page: {r['manual_url']}\n"
    issues.append(
        {
            "key": key,
            "title": f"Manual fetch needed: {r['name']}",
            "body": body,
            "labels": ["digest", "manual", conf_label(key)],
        }
    )

for r in summary.get("stalled", []):
    key = r["key"]
    body = (
        f"**{r['name']}** — {r['attempts']} failed fetch attempts.\n\n"
        f"{r['detail']}\n\n"
        "The site structure or URL has probably changed; the fetcher likely "
        "needs adjusting. (This issue will not auto-close until a digest is "
        "committed.)"
    )
    issues.append(
        {
            "key": key,
            "title": f"Fetcher stalled: {r['name']}",
            "body": body,
            "labels": ["digest", "stalled", conf_label(key)],
        }
    )

(ROOT / "issues.json").write_text(json.dumps(issues, indent=2) + "\n", encoding="utf-8")
print(f"prepared {len(issues)} issue(s): {[i['key'] for i in issues]}")
