# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this repo is

A pipeline that turns published conference programs into curated **digests** for
one specific reader: a PM working on physical DC networking, cloud-native
networking, network security, and identity. Automation fetches programs and
builds prompts; a Claude session (or the user) runs the prompt and writes the
digest. There are no API keys and no model calls in CI — CI only fetches, writes
prompts, and files issues.

## The pipeline

```
registry.yaml (an edition)
  -> scripts/generate_digest_prompt.py   fetch program, compose prompt
  -> prompts/<key>.md                    committed by CI (or a local run)
  -> GitHub issue "Digest: <name>"       labeled conf:<key>
  -> [Claude session reads prompts/<key>.md and follows it]
  -> digests/<key>.md                    committed by a human/Claude, never CI
  -> close-digest-issue.yml closes the issue
```

Two workflows: `conference-digest.yml` (weekly cron + `workflow_dispatch` with an
optional `conference` key) and `close-digest-issue.yml` (push to `digests/*.md`).

## Invariants

These are the rules the whole thing rests on. Breaking one silently breaks the
pipeline.

1. **`digests/<key>.md` existing is the only "done" signal.** It is inferred
   from the filesystem (`is_digested()`), not recorded in state. The generator
   never writes into `digests/`; only a human or a Claude session does.
2. **`key` is the join key everywhere**: `registry.yaml` entry ->
   `prompts/<key>.md` -> `digests/<key>.md` -> issue label `conf:<key>` ->
   `state.json` top-level key. Renaming a key orphans the state record and the
   open issue. Don't rename a key after its first run.
3. **CI commits only `prompts/` and `conferences/state.json`.**
   `run_summary.json` and `issues.json` are ephemeral, gitignored, and passed
   between steps in one job — never commit them.
4. **`state.json` is bookkeeping, not truth.** It tracks
   `status`/`attempts`/`last_attempt`/`last_error` only. A record can say
   `manual` while the digest is already committed (that's normal — see
   `usenix-security-2025`); the digest file wins.
5. **Selection gate:** `end_date <= today` AND no digest yet. `--conference
   <key>` bypasses both gates and forces one edition.
6. **A fetcher never fails the run.** Any exception is caught and downgraded to
   `manual_fallback`. Fetchers return one of `OK` / `NOT_PUBLISHED` /
   `MANUAL_FALLBACK` and must prefer returning zero items over returning wrong
   items — `attempts >= STALL_THRESHOLD` (4) then flags `stalled` so a broken
   selector surfaces instead of producing a bad digest.
7. **Every conference `type` needs `conferences/prompt/types/<type>.md`.**
   `build_prompt()` raises if it's missing. Types today: `academic`,
   `standards`, `vendor`, `operator`, `security`.
8. **Every `fetcher` value must be registered** in
   `conferences/fetchers/__init__.py::FETCHERS`. Today: `usenix`, `ietf`,
   `sched`, `sigcomm`, `netdev`.
9. **`run_location: local`** means the source bot-blocks datacenter IPs. In CI
   that edition is skipped without a fetch attempt (status `local_required`) and
   the issue tells the user to run it from their own machine. `--conference`
   overrides this, so a local forced run does fetch.
10. **The prompt is composed, not stored.** `prompts/<key>.md` =
    run-note header + `prompt/base.md` with `{TYPE_GUIDANCE}` and the
    `{CONFERENCE} {TYPE} {SOURCE_URL} {KEY} {DATE} {PROGRAM_TEXT}` slots filled.
    Edit `base.md` / `types/*.md`, never a generated `prompts/*.md` — except in
    the manual-paste path (below).
11. **Digests start with the HTML-comment metadata block** (`conference`,
    `type`, `source_url`, `generated`, `registry_key`), then `##` tier sections
    (Core / Adjacent / Wildcard) and a final `## Themes`. GitHub-flavored
    markdown only; links as `[text](url)` using the exact URLs from the program
    text.
12. **Never invent program content.** If a fetch or enrichment fails, write from
    the abstract and say so ("from abstract only"). Enrichment deepens a
    write-up; it never changes selection or tier.

## Common tasks

**Run the pipeline locally** (this is also the fix for anything bot-blocked in
CI):

```bash
pip install -r requirements.txt
python3 scripts/generate_digest_prompt.py                      # normal scan
python3 scripts/generate_digest_prompt.py --conference <key>   # force one
```

**Produce a digest:** read `prompts/<key>.md`, follow it, write
`digests/<key>.md`. Best-effort fetch the per-item `pdf:`/`page:` links to
ground the What/How sections.

**Manual-paste path** (source blocks even a local fetch): open the entry's
`manual_fallback_url`, copy the program, and paste it into `prompts/<key>.md`
where `{PROGRAM_TEXT}` is — i.e. below the
`==== PROGRAM TEXT ====` separator line at the end of the prompt. That hand-built prompt is committed like a
generated one. State stays `manual`; the digest file is what closes the loop.

**Add a conference edition:** copy a block in `conferences/registry.yaml` and set
`key`, `name`, `type`, `end_date`, `fetcher`, `program_url`,
`manual_fallback_url`, optional `run_location` and `notes`. Adding a new *source
site* also means a new fetcher module plus a `FETCHERS` entry.

**Commit convention:** digests commit as `digest: <key>`, with a body saying
where the program came from (auto-fetch vs manual paste) and the core signal
picked out. Bot commits are `digest run: update prompts and state (<date>)`.

## Known drift

- `conferences/prompt.md` is a deprecated stub; the live prompt is
  `conferences/prompt/base.md` + `types/`.
- `digests/sigcomm-2025.md` uses `---` front matter and `digests/ietf-123.md` a
  non-standard metadata set; both predate invariant 11. New digests follow 11.
- The `generate_digest_prompt.py` module docstring describes only
  pending/published; the code also writes `waiting`, `manual`, `stalled`, and
  `local_required`.
