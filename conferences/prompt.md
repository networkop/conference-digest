You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

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

- Core: directly relevant to the PM's core interests as listed above
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title** and speaker(s)/author(s) with affiliation, and the tier.
- **Links**: reference links to the paper, slides, and recording where the
  program provides them (the program text below includes pdf:/video: links per
  item when available — use those exact URLs; omit a link if not present rather
  than guessing).
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

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
