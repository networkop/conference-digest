# CLAUDE.md

Guidance for Claude Code working in this repo.

## What this repo is

A pipeline that turns published conference programs into curated **digests** for
one specific reader: a PM working on physical DC networking, cloud-native
networking, network security, and identity. Automation fetches programs and
builds prompts; ToFaRev (an LLM bot, `hellt/tofarev`) drafts each digest and
opens a pull request, and a person merges it. A Claude session (or the user)
can still run a prompt by hand. Merged digests are published as a Zensical blog
on GitHub Pages. The only model calls in CI happen inside ToFaRev's reusable
workflow, with the `TOFAREV_API_KEY` secret (plus the optional
`TAVILY_API_KEY` for PDFs that block runners). The scan uses `TAVILY_API_KEY`
only for nanog.org, which blocks automated clients; reading it through Tavily
Extract was approved by the repository owner (2026-11-01). Do not route other
blocked sources around their bot protection without the same explicit approval. The
model is set by `"model"` in `digest-bot.yml`'s `trusted_config`
(`zai-org/GLM-5.3`).

## The pipeline

```
series.yaml (a recurring conference)
  -> scripts/discover_editions.py        probe for editions not in the registry
  -> registry.yaml                       new edition appended + committed by CI
registry.yaml (an edition)
  -> scripts/generate_digest_prompt.py   fetch program, compose prompt
  -> prompts/<key>.md                    committed by CI (or a local run)
  -> GitHub issue "Digest: <name>"       labeled conf:<key>
  -> digest-bot.yml                      ToFaRev drafts the digest
       (or a Claude session reads prompts/<key>.md and follows it)
  -> scripts/propose_digest.py           validate, add each pick's links row
  -> PR "digest: <key>" on tofarev/digest-<key>  -> a person merges it
  -> digests/<key>.md                    on main only via that merge (or a human/Claude commit)
  -> close-digest-issue.yml closes the issue
  -> site.yml renders digests/ with Zensical -> gh-pages
  -> links-refresh.yml (weekly, 120 days) new recordings/slides -> PR "links: <key>"
```

Five workflows: `conference-digest.yml` (weekly cron + `workflow_dispatch` with
an optional `conference` key), `digest-bot.yml` (after each scan, on a human push
to `prompts/*.md`, or `workflow_dispatch` for one key), `close-digest-issue.yml`
(push to `digests/*.md`), `site.yml` (build on PRs, build + publish on main), and
`links-refresh.yml` (Wednesdays, or `workflow_dispatch` for one key of any age).

`digest-bot.yml` calls ToFaRev's reusable `digest.yml` pinned to a full commit
SHA, exactly like containerlab calls `/tofarev review`. ToFaRev reads only
`prompts/<key>.md` at the scan's commit, runs it in its isolated container
(staged shortlist -> select -> write for big programs; `webfetch` is the writer's
only tool) and returns `digest.md` + `result.json` as an artifact. Its checks
strip links that are not in the program text and flag headings that match no
program item. The `propose` job here validates the artifact
(`scripts/propose_digest.py`, which also adds the links rows), builds the site
with it, and opens one PR per key.

**Links rows.** Every pick gets one `**Links:** [Abstract](…) · [Paper](…) ·
[Slides](…) · [Recording](…)` row under its heading, written by code
(`conferences/links.py`), never by the model. A deck in two formats keeps both
(`slides` and `slides2`, shown as `Slides (PDF)` and `Slides (PPTX)`). Sources, in order: the program
item's `page:`/`pdf:`/`slides:`/`video:`/`materials:` line (fetchers write it);
the talk's `page:`, fetched again (USENIX, Sched and netdev pages gain slides and
an embedded recording after the event; Tavily Extract reads pages that block the
runner); then, for a pick without a recording, the conference's own YouTube
channel when one is listed in `links.py`'s `UPLOAD_CHANNELS` (netnod:
@netnodix) — a channel candidate passes `channel_verify()`, where a title
shortened to its start is enough — then a YouTube search (Tavily search as
the fallback) whose candidates must pass `verify()`. Recordings appear weeks
after a conference, so `links-refresh.yml` reruns this for 120 days and opens a
`links: <key>` PR when a digest gained links. A rerun keeps every link found
before. `build_site.py` turns the row into chips and a click-to-play thumbnail.

## Invariants

These are the rules the whole thing rests on. Breaking one silently breaks the
pipeline.

1. **`digests/<key>.md` existing is the only "done" signal.** It is inferred
   from the filesystem (`is_digested()`), not recorded in state. The generator
   never writes into `digests/`. A human or a Claude session may; the Digest Bot
   writes it only on a `tofarev/digest-<key>` PR branch, so a digest reaches
   `main` only when a person merges it. `scripts/build_site.py` reads
   `digests/` and never writes it.
2. **`key` is the join key everywhere**: `registry.yaml` entry ->
   `prompts/<key>.md` -> `digests/<key>.md` -> issue label `conf:<key>` ->
   `state.json` top-level key. Renaming a key orphans the state record and the
   open issue. Don't rename a key after its first run.
3. **The scan commits only `prompts/`, `conferences/state.json` and
   `conferences/registry.yaml`.** registry.yaml is in that list *only* because
   discovery appends to it; nothing else in CI may write it. The Digest Bot
   pushes only `digests/<key>.md` to its own PR branches (`tofarev/digest-<key>`,
   and `tofarev/links-<key>` for Links Refresh), and `site.yml` pushes only the
   `gh-pages` branch. The site sources `docs/posts/`, `docs/<key>/` (talk
   pages; each holds its own `.gitignore`), `docs/companies/` and
   `docs/conferences.md` are generated at build time and gitignored.
   `run_summary.json`, `issues.json` and `discovery_summary.json` are ephemeral,
   gitignored, and passed between steps in one job — never commit them.
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
   `sched`, `sigcomm`, `netdev`, `nanog`, `autocon`, `ovscon`, `ciscolive`,
   `ripe`, `nlnog`, `denog`, `gtc`, `ocp`, plus the generic `pretalx` and
   `indico`.
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
    `type`, `source_url`, `generated`, `registry_key`, plus `written_by` on
    bot-written digests, which the site uses for attribution), then a single
    `#` heading and `##` tier sections
    (Core / Adjacent / Wildcard) and a final `## Themes`. GitHub-flavored
    markdown only. The `#` heading is the conference name alone, as the
    registry's `name` gives it, optionally followed by ` — Digest` — never an
    audience or type qualifier ("for a Networking / Identity PM", "Operator",
    "Standards", a tagline); `propose_digest.py` rewrites it to
    `# <name> — Digest` regardless. Each `###` pick heading is the program item's title, and the
    line under it is the code-built `**Links:**` row (see Links rows above);
    the writer adds no links of its own beyond exact program URLs.
12. **Discovery only ever appends, and only what it confirmed.**
    `discover_editions.py` writes new blocks at the end of `registry.yaml` and
    re-parses the file afterwards; if the result doesn't contain exactly the
    expected keys it restores the original and fails. It never edits or removes
    an existing entry, so a hand-tuned edition stays hand-tuned. An edition is
    written only after `probe()` confirmed the source has it AND `fetch()`
    returned `OK` — except where a fetcher sets `probe_is_sufficient` (IETF,
    whose probe asks datatracker's meeting API directly).
13. **A series' `key_template` must match the keys already in the registry.**
    Discovery reads it backwards to find where the series is up to
    (`ietf-{n}` -> `ietf-123` -> next is 124). A template that stops matching
    makes every edition look missing; `MAX_GAP` (5) bounds the damage, but the
    real fix is keeping template and keys in step. This is invariant 2 again:
    don't rename keys.
14. **A discovered `end_date` may be an estimate.** Discovery prefers what the
    source states (IETF's meeting API; dates scanned off the program page) and
    falls back to the series' `end_date_hint`. Entries it wrote carry
    `discovered: <date>`, and the issue body asks for a confirming glance.
    Editing that date by hand afterwards is expected and safe.
15. **Never invent program content.** If a fetch or enrichment fails, write from
    the abstract and say so ("from abstract only"). Enrichment deepens a
    write-up; it never changes selection or tier. A link that is not in the
    program text is only added by `conferences/links.py`, from the talk's own
    page or a recording that passed `verify()` (title, conference or channel,
    upload window); when in doubt it adds nothing.

## Common tasks

**Run the pipeline locally** (this is also the fix for anything bot-blocked in
CI):

```bash
pip install -r requirements.txt
python3 scripts/generate_digest_prompt.py                      # normal scan
python3 scripts/generate_digest_prompt.py --conference <key>   # force one
```

**Produce a digest:** normally ToFaRev drafts it and opens a PR; review and
merge. To redo one, close its PR and run Digest Bot with `conference: <key>`. By
hand: read `prompts/<key>.md`, follow it, write `digests/<key>.md`. Best-effort
fetch the per-item `pdf:`/`page:` links to ground the What/How sections, then run
`python3 scripts/enrich_links.py <key>` to add the links rows.

**Refresh a digest's links** (new recordings or slides): `python3
scripts/enrich_links.py <key>` locally (USENIX pages need a non-datacenter IP or
`TAVILY_API_KEY`), or run Links Refresh with `conference: <key>`. It only adds
links and rewrites nothing else.

**Build or preview the site:** `make site` (strict build into `site/`) or
`make serve-site` (live on :8001). Both run `scripts/build_site.py` first, which
turns each digest into `docs/posts/<key>.md` (front matter, excerpt, facts strip,
tier/pick markup; the digest text is unchanged except that employer names in
a pick's speaker line link to that employer's page, and each pick heading
links to its talk page), writes `docs/<key>/<slug>.md` (one page per pick at
`/<key>/<slug>/`, under the digest's `/<key>/`: its links, recording, speakers
and write-up; the folder's own `.gitignore` of `*` keeps it out of git and
marks it for cleanup on the next run, and a hand-made `docs/<key>/` stops the
build), builds `docs/companies/`
(one page per employer in `build_site.py`'s `EMPLOYER_VARIANTS` map, listing
every pick with a speaker from that employer — the Employers tab) and writes the
Conferences tracker. Style lives in `docs/stylesheets/extra.css` and `overrides/`,
adapted from containerlab.dev. Never edit `docs/posts/`, `docs/<key>/` or
`docs/companies/` — edit the digest.

**Search** indexes each pick once, from its talk page. A digest post is found
by its title, intro and facts line only: `build_site.py` marks its body and
every heading in it `data-search-exclude` (Zensical drops a section only when
its heading carries the attribute).

**Social cards:** Zensical's `social` plugin draws a 1200×630 card per page
from `layouts/night.yml` (with `layouts/assets/night.svg` behind it) and writes
the page's `og:`/`twitter:` tags. Pages from `build_site.py` pass the card's
text in a `card:` front-matter mapping (`conference`, `when`, `title`,
`presenter`); other pages fall back to their title and description. A talk's
card shows its title, presenter and conference, which is why each talk has its
own page: link previews ignore `#anchors`, so a link into a digest shows the
digest's card. The build fetches Inter from Google Fonts. In a layout a word
wider than its box is clipped rather than wrapped, and text size follows the
box height.

**Move the bot to a new ToFaRev commit:** `make pin-tofarev SHA=<full sha>`. The
SHA must be pushed to `hellt/tofarev`; GitHub resolves it when the run starts.

**Manual-paste path** (source blocks even a local fetch): open the entry's
`manual_fallback_url`, copy the program, and paste it into `prompts/<key>.md`
where `{PROGRAM_TEXT}` is — i.e. below the
`==== PROGRAM TEXT ====` separator line at the end of the prompt. That hand-built prompt is committed like a
generated one. State stays `manual`; the digest file is what closes the loop.

**Add a new conference:** follow `ADDING-A-CONFERENCE.md` (source checks, fetcher, program-text link keys, series, local trial).

**Add a conference edition:** you usually shouldn't have to — if the conference
recurs, add it to `conferences/series.yaml` once and discovery files every
future edition itself. Do it by hand (copy a block in
`conferences/registry.yaml`, setting `key`, `name`, `type`, `end_date`,
`fetcher`, `program_url`, `manual_fallback_url`, optional `run_location` and
`notes`) for a one-off event, or to correct something discovery got wrong.
Adding a new *source site* also means a new fetcher module plus a `FETCHERS`
entry.

**Add a conference series** (so next year arrives on its own): add a block to
`conferences/series.yaml` with `key_template` matching the keys already in the
registry, the URL templates, `enumerate: year|ordinal`, and an `end_date_hint`
for sources that don't state their own dates. Check it before trusting it:

```bash
python3 scripts/discover_editions.py --dry-run --series <slug>
```

`--dry-run` probes and reports without touching `registry.yaml`. A series whose
source bot-blocks CI needs `run_location: local`, and is then only discovered on
a local run.

**Commit convention:** digests commit as `digest: <key>`, with a body saying
where the program came from (auto-fetch vs manual paste) and the core signal
picked out. Bot commits are `digest run: update prompts and state (<date>)`.

## Known drift

- `digests/ietf-122.md` and `digests/ietf-123.md` were written from the old IETF
  fetcher, which listed each WG's *current* drafts rather than the meeting's
  agenda. Their prompts are now real meeting programs, so picks that were never
  on that meeting's agenda match no program item and get no links row.
- `conferences/prompt.md` is a deprecated stub; the live prompt is
  `conferences/prompt/base.md` + `types/`.
- `digests/sigcomm-2025.md` uses `---` front matter and `digests/ietf-123.md` a
  non-standard metadata set; both predate invariant 11. New digests follow 11.
- The `generate_digest_prompt.py` module docstring describes only
  pending/published; the code also writes `waiting`, `manual`, `stalled`, and
  `local_required`.
