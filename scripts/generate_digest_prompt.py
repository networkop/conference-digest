#!/usr/bin/env python3
"""Conference digest orchestrator.

State machine over conference editions:

  pending  --(fetch ok)-->  published  --(digests/<key>.md committed)--> digested
     |                          ^
     |  (not_published /        |
     |   manual_fallback)       |
     +--------- retry ----------+   ... until attempts >= STALL_THRESHOLD -> stalled

Run modes:
  - scheduled (default): consider every edition whose end_date is in the past
    and which is not yet digested; (re)attempt fetch.
  - --conference <key>: force just that one (manual workflow_dispatch).

"digested" is INFERRED from the presence of digests/<key>.md, so the only
state this script writes is pending/published/attempts/errors. The repo is the
source of truth for what's done.

Outputs:
  prompts/<key>.md           ready-to-paste prompt (universal prompt + program)
  conferences/state.json     bookkeeping
  run_summary.json           what happened this run (the workflow reads this to
                             decide whether to open an issue, and what to say)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from conferences.fetchers import get_fetcher  # noqa: E402
from conferences.fetchers.base import OK, NOT_PUBLISHED, MANUAL_FALLBACK  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "conferences" / "registry.yaml"
STATE = ROOT / "conferences" / "state.json"
PROMPT_DIR = ROOT / "conferences" / "prompt"
PROMPT_BASE = PROMPT_DIR / "base.md"
PROMPT_TYPES = PROMPT_DIR / "types"
PROMPTS_DIR = ROOT / "prompts"
DIGESTS_DIR = ROOT / "digests"
RUN_SUMMARY = ROOT / "run_summary.json"

STALL_THRESHOLD = 4  # ~2 months of fortnightly retries before flagging


def load_registry() -> list[dict]:
    with open(REGISTRY, encoding="utf-8") as f:
        return yaml.safe_load(f)["conferences"]


def load_state() -> dict:
    if STATE.exists():
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state: dict) -> None:
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.write("\n")


def is_digested(key: str) -> bool:
    return (DIGESTS_DIR / f"{key}.md").exists()


def parse_date(s) -> date:
    # PyYAML auto-parses unquoted ISO dates into date objects; tolerate both.
    return s if isinstance(s, date) else datetime.strptime(str(s), "%Y-%m-%d").date()


def build_prompt(entry: dict, program_text: str, source_url: str) -> str:
    # Compose base.md with the one type-block relevant to this conference.
    # Each conference type (academic/standards/vendor/operator/security) has its
    # own reading-guidance file under prompt/types/; only the relevant one is
    # injected, keeping the prompt focused instead of carrying all five blocks.
    conf_type = entry["type"]
    type_file = PROMPT_TYPES / f"{conf_type}.md"
    if not type_file.exists():
        available = sorted(p.stem for p in PROMPT_TYPES.glob("*.md"))
        raise FileNotFoundError(
            f"no prompt type-block for type '{conf_type}' "
            f"(entry '{entry['key']}'); expected {type_file}. "
            f"Available types: {available}"
        )
    type_guidance = type_file.read_text(encoding="utf-8").strip()

    template = PROMPT_BASE.read_text(encoding="utf-8")
    body = (
        template.replace("{TYPE_GUIDANCE}", type_guidance)
        .replace("{CONFERENCE}", entry["name"])
        .replace("{TYPE}", conf_type)
        .replace("{SOURCE_URL}", source_url)
        .replace("{KEY}", entry["key"])
        .replace("{DATE}", date.today().isoformat())
        .replace("{PROGRAM_TEXT}", program_text)
    )
    # Run-note prepended for whoever executes this prompt. Kept separate from
    # the prompt proper so the triage instructions stay portable.
    key = entry["key"]
    sep = "=" * 64
    run_note = (
        ">>> HOW TO RUN THIS <<<\n"
        f"This is the digest prompt for {key}. If you are a Claude session with\n"
        "filesystem access to the conference-digest repo, you can read this same\n"
        f"file directly from `prompts/{key}.md` instead of having it pasted.\n"
        "Produce the digest below and SAVE IT as a markdown file at exactly:\n"
        f"    digests/{key}.md\n"
        "Write the file into the repo directly if you can; otherwise output the\n"
        "file contents so it can be saved to that path. Use that exact filename —\n"
        "it is how the pipeline marks this conference done. If you wrote the file,\n"
        "a brief confirmation is enough; don't also paste the whole digest.\n"
        f"{sep}\n\n"
    )
    return run_note + body


def in_ci() -> bool:
    # GitHub Actions (and most CI) set these. Used to decide whether to skip
    # fetching run_location:local sources that bot-block datacenter IPs.
    return os.environ.get("GITHUB_ACTIONS") == "true" or os.environ.get("CI") == "true"


def select(registry: list[dict], only_key: str | None) -> list[dict]:
    today = date.today()
    out = []
    for entry in registry:
        if only_key:
            if entry["key"] == only_key:
                out.append(entry)
            continue
        if is_digested(entry["key"]):
            continue
        if parse_date(entry["end_date"]) <= today:
            out.append(entry)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", help="force a single registry key")
    args = ap.parse_args()

    PROMPTS_DIR.mkdir(exist_ok=True)
    DIGESTS_DIR.mkdir(exist_ok=True)

    registry = load_registry()
    state = load_state()
    now = datetime.now(timezone.utc).isoformat()
    ci = in_ci()
    forced = bool(args.conference)

    selected = select(registry, args.conference)

    # Every selected conference is an OPEN WORK ITEM and gets a status record,
    # regardless of whether fetch succeeds. The issue layer ensures an issue
    # exists for each and updates its body from this status. status is one of:
    #   ready          prompt written, ready to run
    #   waiting        fetch reached the source but nothing to parse yet
    #   local_required run_location:local and we're in CI -> must fetch locally
    #   manual         fetch blocked (bot challenge); paste the page in by hand
    #   stalled        too many failed attempts; fetcher likely needs fixing
    items = []

    for entry in selected:
        key = entry["key"]
        run_location = entry.get("run_location", "auto")
        st = state.setdefault(
            key, {"status": "pending", "attempts": 0, "last_attempt": None, "last_error": ""}
        )

        base_rec = {
            "key": key,
            "name": entry["name"],
            "type": entry["type"],
            "run_location": run_location,
            "program_url": entry.get("program_url", ""),
            "manual_url": entry.get("manual_fallback_url", ""),
        }

        # local-only source in CI: don't even attempt the fetch (it will 403).
        # The work item still exists; the issue will carry local instructions.
        if run_location == "local" and ci and not forced:
            st["last_attempt"] = now
            st["status"] = "local_required"
            items.append({**base_rec, "status": "local_required",
                          "attempts": st.get("attempts", 0),
                          "detail": "source bot-blocks CI; fetch locally"})
            continue

        fetcher = get_fetcher(entry["fetcher"])
        try:
            res = fetcher.fetch(entry)
        except Exception as e:  # never let one fetcher kill the run
            res = type("R", (), {})()
            res.status, res.detail, res.program_text, res.source_url, res.item_count = (
                MANUAL_FALLBACK, f"fetcher crashed: {e}", "", entry.get("program_url", ""), 0,
            )

        st["last_attempt"] = now

        if res.status == OK:
            prompt = build_prompt(entry, res.program_text, res.source_url)
            (PROMPTS_DIR / f"{key}.md").write_text(prompt, encoding="utf-8")
            st["status"] = "published"
            st["attempts"] = 0
            st["last_error"] = ""
            items.append({**base_rec, "status": "ready",
                          "items": res.item_count, "attempts": 0,
                          "detail": res.detail})
        else:
            st["attempts"] += 1
            st["last_error"] = res.detail
            stalled = st["attempts"] >= STALL_THRESHOLD
            if stalled:
                status = "stalled"
            elif res.status == MANUAL_FALLBACK:
                status = "manual"
            else:
                status = "waiting"
            st["status"] = status
            items.append({**base_rec, "status": status,
                          "attempts": st["attempts"], "detail": res.detail})

    save_state(state)

    by_status: dict[str, int] = {}
    for it in items:
        by_status[it["status"]] = by_status.get(it["status"], 0) + 1

    summary = {
        "generated": now,
        "mode": "manual" if forced else "scheduled",
        "in_ci": ci,
        "counts": by_status,
        "items": items,
    }
    RUN_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    # human-readable log
    print(f"[{summary['mode']}{' / ci' if ci else ''}] {len(items)} open item(s): {by_status}")
    for it in items:
        extra = f" ({it['items']} items)" if it.get("items") else ""
        print(f"  {it['status'].upper():14} {it['key']}{extra} - {it['detail']}")

    # The issue layer always runs when there is at least one open work item.
    notify = bool(items)
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"notify={'true' if notify else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
