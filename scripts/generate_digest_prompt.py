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
PROMPT_TEMPLATE = ROOT / "conferences" / "prompt.md"
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
    template = PROMPT_TEMPLATE.read_text(encoding="utf-8")
    body = (
        template.replace("{CONFERENCE}", entry["name"])
        .replace("{TYPE}", entry["type"])
        .replace("{SOURCE_URL}", source_url)
        .replace("{KEY}", entry["key"])
        .replace("{DATE}", date.today().isoformat())
        .replace("{PROGRAM_TEXT}", program_text)
    )
    # Run-note prepended for whoever executes this prompt. Kept separate from
    # the prompt proper so the triage instructions stay portable. When pasted
    # into a Claude session with filesystem/repo access, this tells it to write
    # the result to the right path; in a plain chat it's a harmless instruction
    # to output a file with that name.
    key = entry["key"]
    sep = "=" * 64
    run_note = (
        ">>> HOW TO RUN THIS <<<\n"
        "Produce the digest below and SAVE IT as a markdown file at exactly:\n"
        f"    digests/{key}.md\n"
        "If you have access to the conference-digest repository (e.g. via a\n"
        "filesystem connector), write the file there directly. Otherwise, output\n"
        "the file contents so it can be saved to that path. Use that exact\n"
        "filename — it is how the pipeline marks this conference done.\n"
        "Do not also paste the digest into chat if you wrote the file; a brief\n"
        "confirmation is enough.\n"
        f"{sep}\n\n"
    )
    return run_note + body


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

    selected = select(registry, args.conference)
    results = {"ready": [], "waiting": [], "manual": [], "stalled": []}

    for entry in selected:
        key = entry["key"]
        st = state.setdefault(
            key, {"status": "pending", "attempts": 0, "last_attempt": None, "last_error": ""}
        )

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
            results["ready"].append(
                {"key": key, "name": entry["name"], "items": res.item_count, "detail": res.detail}
            )
        else:
            st["attempts"] += 1
            st["last_error"] = res.detail
            stalled = st["attempts"] >= STALL_THRESHOLD
            st["status"] = "stalled" if stalled else "pending"
            bucket = "stalled" if stalled else ("manual" if res.status == MANUAL_FALLBACK else "waiting")
            results[bucket].append(
                {
                    "key": key,
                    "name": entry["name"],
                    "attempts": st["attempts"],
                    "detail": res.detail,
                    "manual_url": entry.get("manual_fallback_url", ""),
                }
            )

    save_state(state)

    summary = {
        "generated": now,
        "mode": "manual" if args.conference else "scheduled",
        "counts": {k: len(v) for k, v in results.items()},
        **results,
    }
    RUN_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    # human-readable log
    print(f"[{summary['mode']}] ready={len(results['ready'])} "
          f"waiting={len(results['waiting'])} manual={len(results['manual'])} "
          f"stalled={len(results['stalled'])}")
    for r in results["ready"]:
        print(f"  READY    {r['key']}: {r['items']} items")
    for r in results["manual"]:
        print(f"  MANUAL   {r['key']}: {r['detail']}")
    for r in results["stalled"]:
        print(f"  STALLED  {r['key']}: {r['attempts']} attempts - {r['detail']}")

    # signal for the workflow: open an issue only if there's something to say
    notify = bool(results["ready"] or results["manual"] or results["stalled"])
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"notify={'true' if notify else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
