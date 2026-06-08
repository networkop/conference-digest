#!/usr/bin/env python3
"""Render run_summary.json into per-conference GitHub issue specs.

Writes issues.json: a list of {key, title, body, labels} objects, one per open
work item (every conference past its end_date and not yet digested). The
workflow's github-script step UPSERTS these: if an open issue with the matching
"conf:<key>" label exists, it updates the body; otherwise it creates one.

The issue exists for the whole window between "event is past" and "digest
merged", independent of whether automated fetch succeeded. Its body states the
current status and the exact next action (run locally / run the prompt / fix
the fetcher / wait). The close-workflow closes it when digests/<key>.md lands.
"""

import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
summary = json.loads((ROOT / "run_summary.json").read_text(encoding="utf-8"))
today = date.today().isoformat()


def conf_label(key: str) -> str:
    return f"conf:{key}"


def run_prompt_instructions(key: str) -> str:
    return (
        "Run the digest:\n\n"
        "- In a Claude session with filesystem access to this repo, tell it:\n"
        f"  \"Read `prompts/{key}.md` and follow its instructions.\"\n"
        f"- Or open `prompts/{key}.md`, paste it into Claude, and run it.\n\n"
        f"The result must be committed as `digests/{key}.md` (that auto-closes "
        "this issue)."
    )


def local_fetch_instructions(key: str, program_url: str) -> str:
    return (
        "This source blocks automated fetches from CI (datacenter IPs get a "
        "403), so generate the prompt **from your own machine**:\n\n"
        "1. Fetch the program and build the prompt:\n"
        "   ```bash\n"
        "   cd conference-digest\n"
        f"   python3 scripts/generate_digest_prompt.py --conference {key}\n"
        "   ```\n"
        f"   This writes `prompts/{key}.md`.\n"
        "2. Run the digest: in a Claude session with filesystem access to this "
        f"repo, tell it: \"Read `prompts/{key}.md` and follow its instructions.\"\n"
        f"3. Commit the result as `digests/{key}.md` (that auto-closes this issue).\n\n"
        f"_Fallback, only if your machine is also blocked: open {program_url}, copy "
        f"the program, and paste it into `prompts/{key}.md` where it says "
        "`{PROGRAM_TEXT}` before running step 2._"
    )


def manual_paste_instructions(key: str, manual_url: str) -> str:
    return (
        "Automated fetch reached the site but returned nothing parseable. Try a "
        "local run first — it usually works from a non-datacenter IP:\n\n"
        "1. Fetch and build the prompt locally:\n"
        "   ```bash\n"
        "   cd conference-digest\n"
        f"   python3 scripts/generate_digest_prompt.py --conference {key}\n"
        "   ```\n"
        f"   If that writes `prompts/{key}.md` with real content, continue.\n"
        "2. Run the digest: tell a repo-connected Claude session: "
        f"\"Read `prompts/{key}.md` and follow its instructions.\"\n"
        f"3. Commit the result as `digests/{key}.md`.\n\n"
        f"_Fallback, if the local run also comes back empty: open {manual_url}, "
        f"copy the program, paste it into `prompts/{key}.md` where it says "
        "`{PROGRAM_TEXT}`, then do step 2._"
    )


def body_for(item: dict) -> str:
    key = item["key"]
    status = item["status"]
    header = f"**{item['name']}**  \n`type: {item['type']}` · `status: {status}`\n\n"

    if status == "ready":
        n = item.get("items", "?")
        action = (
            f"The program was fetched ({n} items) and the prompt is ready at "
            f"[`prompts/{key}.md`](../blob/main/prompts/{key}.md).\n\n"
            + run_prompt_instructions(key)
        )
    elif status == "local_required":
        action = local_fetch_instructions(key, item.get("program_url", ""))
    elif status == "manual":
        action = manual_paste_instructions(key, item.get("manual_url", "") or item.get("program_url", ""))
    elif status == "stalled":
        action = (
            f"Automated fetch has failed {item.get('attempts', '?')} times "
            f"(`{item.get('detail', '')}`). The site structure or URL has "
            "probably changed and the fetcher needs adjusting. Until then you "
            "can fetch locally / by hand:\n\n"
            + local_fetch_instructions(key, item.get("program_url", ""))
        )
    elif status == "waiting":
        action = (
            "The event is over but the program/artifacts aren't published yet "
            f"(`{item.get('detail', '')}`). Nothing to do — this will retry "
            "automatically. You can also force a local run once the program is "
            f"up: `python3 scripts/generate_digest_prompt.py --conference {key}`."
        )
    else:
        action = f"Status `{status}`: {item.get('detail', '')}"

    footer = (
        "\n\n---\n"
        f"_Updated {today}. This issue auto-closes when `digests/{key}.md` is "
        "committed to `main`._"
    )
    return header + action + footer


def title_for(item: dict) -> str:
    return f"Digest: {item['name']}"


issues = []
for item in summary.get("items", []):
    key = item["key"]
    issues.append(
        {
            "key": key,
            "title": title_for(item),
            "body": body_for(item),
            "labels": ["digest", f"status:{item['status']}", conf_label(key)],
        }
    )

(ROOT / "issues.json").write_text(json.dumps(issues, indent=2) + "\n", encoding="utf-8")
print(f"prepared {len(issues)} issue spec(s): {[(i['key']) for i in issues]}")
