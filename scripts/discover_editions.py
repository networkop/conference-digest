#!/usr/bin/env python3
"""Find editions that ought to exist and add them to the registry.

registry.yaml lists editions; series.yaml lists the recurring conferences
behind them. Almost every conference here runs at least once a year, so the
next edition's key and URLs are derivable — this script derives them, checks
the source really has that edition, and appends it to registry.yaml. From then
on it is an ordinary registry entry and the rest of the pipeline treats it like
any hand-written one.

Where a series is up to is read from the registry itself (highest year, or
highest ordinal, matching the series' key_template), so this stays correct
whether the last edition was added by hand or by a previous run, and it closes
gaps if the repo sits untouched for a couple of years.

Each candidate must clear two gates before it is written:

  probe()   the source serves that edition at all (not a 404, not a bot
            challenge) — and, where the source states them, its real dates
  fetch()   there is a program we could actually digest today

Requiring the second gate is what keeps placeholder pages ("SIGCOMM 2027 —
call for papers") out of the registry: the entry appears the run after the
program goes up, not a year early.

end_date decides when the digest is due, so it is taken, in order, from:
  1. what the source says (IETF's meeting API; dates scanned off the page)
  2. the series' end_date_hint, as <year>-<MM-DD>
A discovered entry carries `discovered: <date>`, which the issue body turns
into a "confirm the end_date" note when the date was only a hint.

Writes: conferences/registry.yaml (append-only), discovery_summary.json
(ephemeral, read by scripts/build_issue.py in the same job).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from conferences.fetchers import get_fetcher  # noqa: E402
from conferences.fetchers.base import OK  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "conferences" / "registry.yaml"
SERIES = ROOT / "conferences" / "series.yaml"
DISCOVERY_SUMMARY = ROOT / "discovery_summary.json"

DEFAULT_LOOKAHEAD = 2
# Don't chase a series more than this far past where the registry sits. Bounds
# the damage if a key_template stops matching and every edition looks missing.
MAX_GAP = 5

AUTO_SECTION = (
    "\n  # --------------------------------------------------------------------- #\n"
    "  # Auto-discovered editions (scripts/discover_editions.py).\n"
    "  # Appended by the scheduled run once the source confirmed the edition\n"
    "  # exists AND its program was fetchable. Edit or re-order these freely —\n"
    "  # discovery only ever appends keys that are not in this file yet.\n"
    "  # --------------------------------------------------------------------- #\n"
)


# --------------------------------------------------------------------------- #
# templates
# --------------------------------------------------------------------------- #

def fill(template: str, ident: int, mode: str) -> str:
    """Render one edition's key/name/url from a template."""
    if mode == "year":
        return template.replace("{year}", str(ident)).replace("{yy}", f"{ident % 100:02d}")
    return (
        template.replace("{n}", str(ident))
        .replace("{hex}", format(ident, "x"))
        .replace("{HEX}", format(ident, "X"))
    )


def ident_pattern(key_template: str, mode: str, ordinal_format: str) -> re.Pattern:
    """A regex that reads an edition's number back out of an existing key."""
    if mode == "year":
        body = re.escape(key_template).replace(re.escape("{year}"), r"(?P<id>\d{4})")
        body = body.replace(re.escape("{yy}"), r"\d{2}")
    elif ordinal_format == "hex":
        body = re.escape(key_template)
        for slot in ("{hex}", "{HEX}"):
            body = body.replace(re.escape(slot), r"(?P<id>[0-9a-fA-F]+)")
        body = body.replace(re.escape("{n}"), r"\d+")
    else:
        body = re.escape(key_template).replace(re.escape("{n}"), r"(?P<id>\d+)")
    return re.compile(f"^{body}$")


def parse_ident(text: str, mode: str, ordinal_format: str) -> int:
    return int(text, 16 if (mode == "ordinal" and ordinal_format == "hex") else 10)


def latest_ident(keys: list[str], spec: dict) -> int | None:
    """Where this series has got to in the registry, by its own key pattern."""
    mode = spec.get("enumerate", "year")
    fmt = spec.get("ordinal_format", "dec")
    pat = ident_pattern(spec["key_template"], mode, fmt)
    found = [parse_ident(m.group("id"), mode, fmt) for k in keys if (m := pat.match(k))]
    return max(found) if found else None


def candidates(spec: dict, known_keys: list[str], today: date) -> list[int]:
    """Edition numbers this series ought to have but the registry doesn't."""
    mode = spec.get("enumerate", "year")
    lookahead = int(spec.get("lookahead", DEFAULT_LOOKAHEAD))
    latest = latest_ident(known_keys, spec)

    if latest is None:
        start = spec.get("start")
        if start is None:
            return []
        latest = parse_ident(str(start), mode, spec.get("ordinal_format", "dec")) - 1

    if mode == "year":
        # Everything from the year after the last known edition up to next year,
        # so a repo left alone for two years still catches up.
        upper = max(today.year + 1, latest + 1)
        ids = list(range(latest + 1, min(upper, latest + MAX_GAP) + 1))
    else:
        ids = list(range(latest + 1, latest + 1 + min(lookahead, MAX_GAP)))

    return ids[:MAX_GAP]


# --------------------------------------------------------------------------- #
# registry writing
# --------------------------------------------------------------------------- #

def yaml_str(value: str) -> str:
    """Quote a scalar the way the hand-written entries are quoted."""
    return json.dumps(value, ensure_ascii=False)


def render_entry(entry: dict) -> str:
    lines = [
        f"  - key: {entry['key']}",
        f"    name: {yaml_str(entry['name'])}",
        f"    type: {entry['type']}",
        f"    end_date: {entry['end_date']}",
        f"    fetcher: {entry['fetcher']}",
    ]
    if entry.get("run_location"):
        lines.append(f"    run_location: {entry['run_location']}")
    lines += [
        f"    program_url: {yaml_str(entry['program_url'])}",
        f"    manual_fallback_url: {yaml_str(entry['manual_fallback_url'])}",
        f"    discovered: {entry['discovered']}",
    ]
    if entry.get("notes"):
        lines.append(f"    notes: {yaml_str(entry['notes'])}")
    return "\n".join(lines) + "\n"


def append_entries(new_entries: list[dict]) -> None:
    """Append blocks to registry.yaml, then re-parse to prove we didn't break it.

    `conferences:` is the file's only top-level key and runs to EOF, so
    appending is safe and leaves every existing comment untouched. If the
    result doesn't parse, or doesn't contain exactly the editions we expect,
    the original file is put back and the run fails loudly.
    """
    original = REGISTRY.read_text(encoding="utf-8")
    before = {e["key"] for e in yaml.safe_load(original)["conferences"]}

    text = original if original.endswith("\n") else original + "\n"
    if "# Auto-discovered editions" not in text:
        text += AUTO_SECTION
    for entry in new_entries:
        text += "\n" + render_entry(entry)

    REGISTRY.write_text(text, encoding="utf-8")
    try:
        after = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]
        keys = [e["key"] for e in after]
        expected = before | {e["key"] for e in new_entries}
        if set(keys) != expected or len(keys) != len(set(keys)):
            raise ValueError(f"registry keys after write: {sorted(set(keys) ^ expected)}")
    except Exception as e:
        REGISTRY.write_text(original, encoding="utf-8")
        raise SystemExit(f"discovery: refusing to corrupt registry.yaml ({e}); reverted")


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def in_ci() -> bool:
    return os.environ.get("GITHUB_ACTIONS") == "true" or os.environ.get("CI") == "true"


def resolve_end_date(spec: dict, ident: int, probe_end: date | None,
                     prev_end: date | None, today: date) -> tuple[str, bool]:
    """(ISO end_date, was_estimated). Source first, series hint second."""
    if probe_end:
        return probe_end.isoformat(), False

    hint = spec.get("end_date_hint")
    if not hint:
        return "", True

    if spec.get("enumerate", "year") == "year":
        year = ident
    elif prev_end:
        # Ordinal series carry no year in their number, so date the edition one
        # year after the last one we know about — which is how IETF's numbering
        # and netdev's hex editions have always run.
        year = prev_end.year + 1
    else:
        year = today.year
    return f"{year}-{hint}", True


def latest_end_date(registry: list[dict], spec: dict) -> date | None:
    """end_date of the newest edition of this series already in the registry."""
    mode = spec.get("enumerate", "year")
    fmt = spec.get("ordinal_format", "dec")
    pat = ident_pattern(spec["key_template"], mode, fmt)
    ends = []
    for e in registry:
        if not pat.match(e["key"]):
            continue
        raw = e.get("end_date")
        ends.append(raw if isinstance(raw, date)
                    else datetime.strptime(str(raw), "%Y-%m-%d").date())
    return max(ends) if ends else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", help="only probe this series slug")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be added; don't touch registry.yaml")
    args = ap.parse_args()

    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["conferences"]
    known_keys = [e["key"] for e in registry]
    specs = yaml.safe_load(SERIES.read_text(encoding="utf-8"))["series"]
    if args.series:
        specs = [s for s in specs if s["series"] == args.series]
        if not specs:
            raise SystemExit(f"no series '{args.series}' in {SERIES.name}")

    today = date.today()
    ci = in_ci()
    added: list[dict] = []
    reports: list[dict] = []

    for spec in specs:
        slug = spec["series"]
        mode = spec.get("enumerate", "year")
        run_location = spec.get("run_location", "auto")

        # Same rule as the orchestrator: a source that bot-blocks CI is not
        # probed from CI. Reported, not skipped silently — a local run gets it.
        if run_location == "local" and ci:
            reports.append({"series": slug, "status": "local_required",
                            "detail": "source bot-blocks CI; run discovery locally"})
            continue

        for ident in candidates(spec, known_keys, today):
            key = fill(spec["key_template"], ident, mode)
            if key in known_keys:
                continue

            candidate = {
                "key": key,
                "name": fill(spec["name_template"], ident, mode),
                "type": spec["type"],
                "fetcher": spec["fetcher"],
                "program_url": fill(spec["program_url_template"], ident, mode),
                "manual_fallback_url": fill(spec["manual_fallback_url_template"], ident, mode),
            }
            fetcher = get_fetcher(spec["fetcher"])
            years = [ident] if mode == "year" else None

            try:
                pr = fetcher.probe(candidate, years)
            except Exception as e:  # a probe must never kill the run
                reports.append({"series": slug, "key": key, "status": "probe_error",
                                "detail": f"{e}"})
                continue

            if not pr.exists:
                reports.append({"series": slug, "key": key, "status": "absent",
                                "detail": pr.detail})
                # Editions come in order; if this one isn't up, later ones
                # certainly aren't. Stop probing this series.
                break

            # Gate 2: is there really a program behind that URL? Skipped when
            # the fetcher says its probe already settled the question.
            fetch_detail = "probe is authoritative; fetch skipped"
            item_count = 0
            if not getattr(fetcher, "probe_is_sufficient", False):
                try:
                    fr = fetcher.fetch(candidate)
                except Exception as e:
                    reports.append({"series": slug, "key": key, "status": "fetch_error",
                                    "detail": f"fetcher crashed: {e}"})
                    continue

                if fr.status != OK:
                    reports.append({"series": slug, "key": key, "status": "no_program",
                                    "detail": f"{fr.status}: {fr.detail}"})
                    continue
                fetch_detail, item_count = fr.detail, fr.item_count

            end_date, estimated = resolve_end_date(
                spec, ident, pr.end_date, latest_end_date(registry, spec), today
            )
            if not end_date:
                reports.append({"series": slug, "key": key, "status": "no_end_date",
                                "detail": "source gave no dates and series has no "
                                          "end_date_hint; add one to series.yaml"})
                continue

            name = candidate["name"]
            if pr.location:
                name = f"{name} ({pr.location})"

            note = spec.get("notes", "")
            provenance = (
                f"Auto-discovered {today.isoformat()} from series '{slug}'. "
                + ("end_date is an ESTIMATE from the series hint — confirm it against "
                   "the event page." if estimated else "end_date taken from the source.")
            )

            entry = {
                **candidate,
                "name": name,
                "end_date": end_date,
                "run_location": spec.get("run_location", ""),
                "discovered": today.isoformat(),
                "notes": f"{note} {provenance}".strip(),
                "_estimated": estimated,
            }
            added.append(entry)
            known_keys.append(key)
            reports.append({"series": slug, "key": key, "status": "added",
                            "end_date": end_date, "estimated": estimated,
                            "items": item_count,
                            "detail": f"{pr.detail}; {fetch_detail}"})

    if added and not args.dry_run:
        append_entries(added)

    summary = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "in_ci": ci,
        "dry_run": args.dry_run,
        "added": [
            {"key": e["key"], "name": e["name"], "end_date": e["end_date"],
             "estimated": e["_estimated"]}
            for e in added
        ],
        "reports": reports,
    }
    DISCOVERY_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    verb = "would add" if args.dry_run else "added"
    print(f"[discovery{' / ci' if ci else ''}] {verb} {len(added)} edition(s)")
    for r in reports:
        key = r.get("key", "-")
        print(f"  {r['status'].upper():14} {r['series']:16} {key:24} {r.get('detail', '')}")

    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"discovered={'true' if added else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
