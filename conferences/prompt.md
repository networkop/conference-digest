You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. They work in cloud-native networking and
infrastructure (eBPF, Cilium, Kubernetes networking, Gateway API, service
mesh, IPAM, BGP/datapath internals) and track adjacent developments in
network security and in identity/authentication (passkeys/FIDO, OAuth, OIDC,
SPIFFE/SPIRE, workload and agentic identity).

Below is the program for {CONFERENCE} ({TYPE}). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program, given its type

- academic: judge novelty, methodology, and whether results are firmly
  substantiated. Prefer work that changes how a practitioner would design or
  reason about systems over incremental benchmarks. Name the technique, not
  just the title.
- standards: these are working-group sessions and Internet-Drafts. Judge what
  is moving toward consensus, what is newly adopted, and what would affect
  implementations the PM cares about. Draft titles + abstracts carry the
  substance; sessions themselves are thin.
- vendor / community: separate genuine technical or strategic substance from
  product marketing. Down-rank pure pitches. Up-rank end-user case studies
  with real numbers and contributor-led architecture talks.
- operator: focus on operational practice, failure stories, and techniques
  that transfer across environments rather than org-specific anecdotes.
- security: judge real-world impact and technical depth. Up-rank original
  offensive/defensive research, disclosures with proof, and identity-related
  work (AD, cloud IdPs, authn/authz).

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to cloud-native networking, network security, or
  identity as the PM works on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that aren't an obvious fit but are genuinely novel or
  signal where the field is heading. Be willing to surprise.

For each selected item provide:
- Title and speaker(s)/author(s) with affiliation
- One sentence on what it ACTUALLY covers (not the marketing abstract)
- Why it matters to this PM, or why it's a wildcard
- The tier (Core / Adjacent / Wildcard)

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

Begin the output with this YAML front matter block, filled in:

---
conference: {CONFERENCE}
type: {TYPE}
source_url: {SOURCE_URL}
generated: {DATE}
registry_key: {KEY}
---

Then the digest as markdown (tiers as sections, Themes at the end).

============================ PROGRAM TEXT ============================

{PROGRAM_TEXT}
