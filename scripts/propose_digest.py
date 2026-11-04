#!/usr/bin/env python3
"""Install one ToFaRev digest artifact and describe it for review.

  propose_digest.py KEY ARTIFACT_DIR --message FILE --body FILE
                    [--run-url URL] [--issue N]

ARTIFACT_DIR is the downloaded `tofarev-digest-<key>` artifact: digest.md plus
result.json (stats and check notes). The digest is validated and written to
digests/<key>.md, and every pick gets its links row (conferences/links.py:
abstract, paper, slides, recording; TAVILY_API_KEY is the search fallback).
The commit message follows the repo convention (`digest: <key>`, where the
program came from, the core signal) and the PR body lists the automatic checks
and link counts for the human who merges it. Exits non-zero, writing nothing,
if the artifact does not belong to KEY or has no `###` picks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from conferences.links import context_for, enrich  # noqa: E402

REGISTRY = ROOT / "conferences" / "registry.yaml"
STATE = ROOT / "conferences" / "state.json"
MAX_BYTES = 400_000


def fail(message: str) -> int:
    print(f"error: {message}", file=sys.stderr)
    return 1


def normalize_title(markdown: str, name: str) -> tuple[str, str | None]:
    """Return (markdown, note): the `#` heading becomes `# <name> -- Digest`.

    The writer sometimes qualifies the title with an audience or type
    ("Digest for a Networking / Identity PM", "Operator Digest", a tagline);
    the title is the conference name alone, decided here by code - like the
    links rows, never by the model.
    """
    title = f"# {name} — Digest"
    meta_end = markdown.find("-->")
    head, tail = ("", markdown) if meta_end == -1 else (markdown[: meta_end + 3], markdown[meta_end + 3:])
    m = re.search(r"^# +(.+)$", tail, re.M)
    if m:
        old = m.group(1).strip()
        if old == f"{name} — Digest":
            return markdown, None
        tail = re.sub(r"^# +.+$", title, tail, count=1, flags=re.M)
        return head + tail, f"Title normalized to '{name} — Digest' (writer had: '{old}')."
    return head + "\n\n" + title + "\n" + tail.lstrip("\n"), f"No `#` heading found; inserted '{name} — Digest'."


def themes(markdown: str, limit: int = 3) -> list[str]:
    m = re.search(r"^## +Themes\b.*?$(.*)", markdown, re.M | re.S | re.I)
    bullets = re.findall(r"^[-*] +(.+)$", m.group(1), re.M) if m else []
    out = []
    for b in bullets[:limit]:
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", b).replace("**", "").strip()
        out.append(text if len(text) <= 160 else text[:159].rsplit(" ", 1)[0] + "…")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("key")
    ap.add_argument("artifact", type=Path)
    ap.add_argument("--message", type=Path, required=True)
    ap.add_argument("--body", type=Path, required=True)
    ap.add_argument("--run-url", default="")
    ap.add_argument("--issue", default="")
    ap.add_argument("--no-links", action="store_true", help="skip the links rows (offline use)")
    args = ap.parse_args()
    key = args.key

    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,99}", key):
        return fail(f"invalid key {key!r}")
    registry = {e["key"]: e for e in yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]}
    if key not in registry:
        return fail(f"{key} is not in the registry")
    entry = registry[key]
    digest_file = args.artifact / "digest.md"
    result_file = args.artifact / "result.json"
    if not digest_file.is_file() or not result_file.is_file():
        return fail(f"{args.artifact} has no digest.md and result.json")
    if digest_file.stat().st_size > MAX_BYTES:
        return fail("digest.md is too large")
    result = json.loads(result_file.read_text(encoding="utf-8"))
    markdown = digest_file.read_text(encoding="utf-8")
    if result.get("failed") or result.get("key") not in (None, key):
        return fail(f"result.json is failed or belongs to {result.get('key')!r}")
    meta = re.match(r"<!--\n(.*?)\n-->", markdown, re.S)
    if not meta or not re.search(rf"^registry_key: {re.escape(key)}$", meta.group(1), re.M):
        return fail(f"digest.md does not start with the metadata block for {key}")
    written_by = re.search(r"^written_by: *(.+)$", meta.group(1), re.M)
    written_by = written_by.group(1).strip() if written_by else "ToFaRev"
    if not re.search(r"^### +\S", markdown, re.M):
        return fail("digest.md has no ### pick headings (the writer used another layout); "
                    "no PR is opened, so the next Digest Bot run drafts it again")
    markdown, title_note = normalize_title(markdown, entry["name"])

    links = None
    if not args.no_links:
        prompt = ROOT / "prompts" / f"{key}.md"
        markdown, links = enrich(markdown, prompt.read_text(encoding="utf-8") if prompt.is_file() else "",
                                 context_for(entry))
    (ROOT / "digests" / f"{key}.md").write_text(markdown, encoding="utf-8")

    state = json.loads(STATE.read_text(encoding="utf-8")).get(key, {}) if STATE.exists() else {}
    if state.get("status") == "manual":
        source = f"a program pasted into prompts/{key}.md by hand"
    else:
        source = f"a program auto-fetched by the {entry.get('fetcher', '?')} fetcher"
    stats = result.get("stats", {})
    notes = result.get("notes", [])
    if title_note:
        notes = [title_note, *notes]
    signal = themes(markdown)

    message = [f"digest: {key}", "", f"Written by {written_by} from prompts/{key}.md, built from {source}."]
    message.append(
        f"{stats.get('picks', '?')} picks from {stats.get('items', '?')} program items "
        f"({stats.get('mode', '?')} run, {stats.get('calls', '?')} model calls)."
    )
    if signal:
        message += ["", "Themes:"] + [f"- {t}" for t in signal]
    if args.run_url:
        message += ["", f"Workflow run: {args.run_url}"]
    args.message.write_text("\n".join(message) + "\n", encoding="utf-8")

    staged = stats.get("mode") == "staged"
    rows = [
        ("Program", f"{stats.get('items', '?')} items from {source}"),
        ("Selection", f"{stats.get('batches', 0)} shortlist batches → {stats.get('shortlisted', 0)} shortlisted → "
                      f"{stats.get('selected', 0)} sent to the writer" if staged else "whole program sent to the writer"),
        ("Picks", str(stats.get("picks", "?"))),
        *([("Links", f"{links['page']} abstract pages, {links['pdf']} papers, {links['slides']} slides, "
                     f"{links['video']} recordings ({links['video_from_search']} found by a verified search)")]
          if links else []),
        ("Model", f"{written_by}, {stats.get('calls', '?')} calls in {stats.get('seconds', '?')} s"),
    ]
    if args.run_url:
        rows.append(("Workflow run", f"[logs]({args.run_url})"))
    body = [
        f"ToFaRev drafted the digest for **{entry['name']}**.",
        "",
        f"Merging publishes it to the site and closes the conference issue{f' (closes #{args.issue})' if args.issue else ''}.",
        "",
        "| | |",
        "|---|---|",
        *[f"| {k} | {v} |" for k, v in rows],
        "",
        "### Automatic checks",
        "",
        *([f"- {n}" for n in notes] or ["- Nothing to flag. Every heading matches a program item."]),
        *([f"- No program links for: {h}" for h in links["unmatched"][:10]] if links else []),
        "",
        "### Before merging",
        "",
        "- [ ] Picks and tiers make sense for this program.",
        "- [ ] Spot-check two or three write-ups against their abstracts.",
        "- [ ] Any heading flagged above is a real program item.",
        *(["- [ ] Open two or three recordings found by search: right talk, right event."]
          if links and links["video_from_search"] else []),
        "",
        "Edit the digest on this branch if needed. To redo it, close this PR and run **Digest Bot** with this key.",
    ]
    args.body.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"installed digests/{key}.md ({len(markdown)} bytes, {len(notes)} note(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
