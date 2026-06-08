DEPRECATED — this monolithic prompt has been split into:
  conferences/prompt/base.md         (persona, tiers, item format, rules, output)
  conferences/prompt/types/*.md      (per-type reading guidance)

The orchestrator (scripts/generate_digest_prompt.py) now composes base.md with
the one relevant types/<type>.md. This file is no longer read by anything and
should be removed from the repo:  git rm conferences/prompt.md
