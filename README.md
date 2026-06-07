# conference-digest

Generates ready-to-paste **digest prompts** for conferences relevant to
cloud-native networking, network security, and identity. A GitHub Actions
workflow fetches each conference's published program, wraps it in a universal
triage prompt, commits the prompt, and opens a GitHub Issue telling you what's
ready. You paste the prompt into Claude Desktop, generate the digest, and
commit it to `digests/`.

No API keys. No SMTP. The only credential used is the workflow's built-in
`GITHUB_TOKEN` (for committing and opening issues).

## How it works

```
trigger (fortnightly cron, or manual workflow_dispatch)
  -> orchestrator reads registry + state
  -> for each past, not-yet-digested conference: run its fetcher
       OK            -> write prompts/<key>.md, mark published
       not_published -> retry next run (event past but artifacts not up yet)
       manual         -> auto-fetch blocked; you paste the program in yourself
  -> commit prompts/ + state.json
  -> open ONE GitHub Issue summarising what's ready / needs you / stalled
  -> [you] paste prompt into Claude Desktop -> commit digests/<key>.md
```

A conference is considered **done** when `digests/<key>.md` exists — that's the
only "done" signal; the script never writes it, you do (by committing the
digest). State (`conferences/state.json`) only tracks pending/published and
retry bookkeeping.

### Selection rule

On each run, the orchestrator selects every conference whose `end_date` is in
the past and which has no digest yet, then (re)attempts the fetch. Artifacts
(papers, videos) are usually published *after* the event, so a past conference
that isn't fetchable yet stays `pending` and is retried until it succeeds — or,
after `STALL_THRESHOLD` (4) failed attempts, is flagged **stalled** so you know
a site changed and a fetcher needs adjusting.

## Layout

```
conferences/
  registry.yaml      # the conferences (one entry per edition/year)
  prompt.md          # the universal digest prompt (slots: {CONFERENCE} {TYPE} ...)
  state.json         # auto-managed bookkeeping (created on first run)
  fetchers/
    base.py          # shared fetch + result types + bot-block heuristic
    usenix.py        # NSDI / USENIX Security / SREcon (static HTML)
    ietf.py          # datatracker documents API (per-WG active drafts)
    sched.py         # KubeCon / CNCF public Sched schedule (HTML)
scripts/
  generate_digest_prompt.py   # orchestrator (state machine)
  build_issue.py              # renders run_summary.json -> issue body
prompts/             # generated, committed by the workflow
digests/             # YOU commit digests here; presence = done
.github/workflows/
  conference-digest.yml
```

## Running it

- **Manual, one conference:** Actions tab -> Conference Digest -> Run workflow,
  set `conference` to a registry key (e.g. `nsdi-2025`). Ignores the date and
  digested gates — forces that one.
- **Scheduled:** runs weekly; the state machine no-ops when nothing is new, so
  you only get an issue when there's something to digest.
- **Locally:** `pip install -r requirements.txt && python scripts/generate_digest_prompt.py`

## Adding a conference

Copy a block in `registry.yaml`, set:

- `key` — unique slug, also the prompt/digest filename
- `type` — `academic | standards | vendor | operator | security` (drives how
  the prompt tells Claude to read the program)
- `end_date` — `YYYY-MM-DD` (selection is based on this)
- `fetcher` — `usenix | ietf | sched`
- `program_url` — the machine/human-readable program endpoint
- `manual_fallback_url` — page for you to open if auto-fetch is blocked

## Fetcher notes & known fragilities

- **USENIX** and **Sched** are HTML scrapers using browser-like headers. Both
  sites can bot-block (USENIX confirmed to do so). On a block they return
  `manual` and the issue gives you the URL to copy from by hand. The HTML class
  selectors are best-effort; if a site restyles, the fetcher returns zero items
  (`not_published`) and eventually trips the stall flag rather than producing
  wrong output. **The first live run is the real test of these selectors.**
- **IETF** uses the open datatracker documents API (no key, no bot-block). It
  iterates a curated `RELEVANT_WGS` list (edit in `ietf.py` as interests shift)
  and pulls each WG's active drafts. Draft "active" filtering is intentionally
  permissive — when the API returns state as opaque URIs it keeps the draft;
  worst case is a few extra drafts in the prompt, which Claude filters anyway.
- The `*.sched.com` subdomains and exact `end_date`s in the registry should be
  verified close to each event; they're flagged in registry `notes`.

## Dependencies

`requests`, `beautifulsoup4`, `PyYAML`. Installed fresh in the workflow runner.
