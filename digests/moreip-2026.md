<!--
conference: MORE-IP 2026
type: operator
source_url: https://more-ip-event.net/more-ip-2026/agenda/
generated: 2026-11-03
registry_key: moreip-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# MORE-IP 2026 — Digest

A note on depth: this program is unusually thin on abstracts — most sessions list only a title and speakers, and no `page:` or `pdf:` links were available for enrichment. Every write-up below is therefore grounded in the title, the speaker's affiliation, and (where available) the one-line abstract, and is marked accordingly. Where the talk content is unknown, I say so rather than guess.

## Core

### SCION

Adrian Perrig — ETH Zurich

- **Why**: SCION is the most serious sustained attempt at a clean-slate, security-first internet architecture that has reached actual deployment discussions, and it speaks directly to the PM's network-security and interdomain-routing interests. Having its chief architect present at an operator event means the talk is aimed at people who run networks, not academics.
- **What**: SCION (Scalability, Control, and Isolation on Next-Generation Networks) is a path-aware internetworking architecture: instead of letting BGP's path selection decide transit opaque to endpoints, receivers and senders hold visible, cryptographically authenticated path choices. The program publishes no description for this session, so the specific content (architecture overview vs. deployment status vs. operator onboarding) is unknown — but any of those would be valuable. *(from abstract only; no description published)*
- **How**: SCION organizes the internet into Isolation Domains containing ASes, and lets endpoints select among authenticated AS-level path segments — enabling path failure isolation, protection against route hijacks, and control-plane attacks that today's BGP can't defend against. The Swiss financial sector has run SCION pilots over an exchange infrastructure, making this relevant to IX/peering operators like the host.
- **Where applicable**: Interdomain/WAN transit and any environment with strict integrity or availability guarantees (finance, critical infrastructure). Not a DC-fabric or LAN technique — it's about the internet core and inter-AS paths. Deployment is still early; treat it as a signal of where interdomain security is heading rather than something to adopt next quarter.

### IPv4-with-IPv6 Next-Hop: Towards an IPv4-Free Internet Core

Tobias Fiebig — Vienna University of Technology

- **Why**: For anyone who cares about BGP/datapath internals and the long, slow IPv6 transition, this is one of the sharpest technical titles on the program. The question it names — can we carry IPv4 reachability with IPv6-only transport in the core, so the core stops speaking IPv4 entirely — is one of the few genuinely structural changes still available to the internet without a flag day.
- **What**: The title indicates a proposal or evaluation of running the core network IPv6-only: advertising IPv4 prefixes while using IPv6 next-hop addresses (the mechanism standardised in RFC 8950), eliminating the need for IPv4 addresses on core-facing interfaces and shrinking the core's IPv4 configuration surface. No abstract was published, so the exact contribution — measurement of current adoption, an operator how-to, or a transition proposal — cannot be confirmed. *(from abstract only; no description published)*
- **How**: Presumably by combining extended-nexthop BGP encoding (IPv4 NLRI, IPv6 next hop) with v6-only core links, so IPv4 survives only as payload/edge reachability. Fiebig's group is known for large-scale BGP measurement, so expect deployment data or adoption obstacles rather than a purely theoretical argument.
- **Where applicable**: Transit providers, IXs, and large DC/WAN interconnect operators — exactly the environments this event's audience runs. The main constraints are real-world ones: hardware/daemon support for extended nexthops on all core routers, and the operational discipline to keep v4 out once it's out. Treat the specifics as unverified until the paper or slides are published.

### DDoS Threatscape and Mitigation Strategies

Kevin Richardson — NTT DATA

- **Why**: DDoS is the most operationally concrete part of the PM's network-security interest, and this is the only dedicated DDoS session on the program. NTT's global network sits in the middle of a large share of internet attack traffic, so an update on the current threatscape is worth the time.
- **What**: An overview of the current DDoS landscape and mitigation practice, from a provider with global visibility. The title and the one-word framing are all the program provides; there is no abstract, so the balance between attack trends (volumetric, protocol, application-layer, and the recurring amplification vectors) versus mitigation tactics (scrubbing, flow-spec, anycast absorption) is unknown. *(from abstract only; no description published)*
- **How**: Unknown in detail from the program. Talks in this genre typically combine attack telemetry with tiered mitigation: upstream flow control (BGP Flowspec, RTBH), dedicated scrubbing centers, and edge rate/application filtering.
- **Where applicable**: Broadly applicable — DDoS threatscape and mitigation patterns transfer across any operator facing the public internet. Mitigation economics scale with provider size; NTT-scale scrubbing capacity is not replicable by a small operator, but the defensive taxonomy is.

### Automation & Orchestration

Steven Bakker — AMS-IX

- **Why**: This is part of the AMS-IX technical track — the host exchange explaining how it automates its own production platform. Operator-run tooling talks at an IX are exactly the "automation others can adopt" category that transfers well, and for a PM whose interests span software-native networking, exchange automation is a useful benchmark of the state of the practice.
- **What**: Unknown in content — the program lists only the title and the AMS-IX Technical Track tag. Expect it to cover configuration generation, provisioning, and change management for exchange fabric and service infrastructure (member ports, route servers, service lifecycles). *(from abstract only; no description published)*
- **How**: Unknown from the program; historically AMS-IX has discussed pipeline-driven configuration from a single source of truth and test-driven change validation for its switching and service platforms.
- **Where applicable**: Directly relevant to anyone operating shared switching infrastructure (IXPs, meetpoint fabrics) or running network automation programs generally. The specifics will be AMS-IX-specific in tooling but the workflow patterns are broadly portable.

### NOC Update

**Links:** [Recording](https://www.youtube.com/watch?v=zb_cZxyVLwY)

Konstantinos Prantzos — AMS-IX

- **Why**: NOC updates are the purest postmortem-and-operations genre at operator events: what broke, what was learned, what changed. For a PM in DC/fabric work, an exchange NOC's year in review is a compact source of failure modes in shared-layer-2 fabric at carrier scale.
- **What**: The AMS-IX NOC's update on operational events, incidents, and infrastructure work over the preceding period. The program gives only the title and the AMS-IX Technical Track tag; whether it includes incident postmortems or is limited to maintenance and statistics is not stated. *(from abstract only; no description published)*
- **How**: N/A — this is an operational report rather than a technique talk.
- **Where applicable**: Broadly instructive for anyone running always-on layer-2 fabrics and peering platforms; the specific incidents are AMS-IX's, but the failure classes (optics, port flaps, maintenance risk, member-side mayhem) are universal in exchange and DC fabrics.

## Adjacent

### Time dissemination in the Netherlands

Miguel Regalado Querol — AMS-IX; Reindert Hommes — Tallgrass

- **Why**: Time is silent critical infrastructure: everything from BGP session stability to log forensics to (increasingly) financial and telemetry correctness depends on NTP/PTP and GNSS-derived time. A joint talk by AMS-IX and Tallgrass on national time dissemination suggests this is about building a sovereign, verifiable time service in the Netherlands — a topic with direct operational resonance for DC operators.
- **What**: Per the title, the current state and direction of time distribution across NL, likely including existing NTP infrastructure, GNSS dependency, and what a more resilient national time service would look like. No abstract was published. *(from abstract only; no description published)*
- **How**: Unknown from the program; talks in this space typically cover hierarchical NTP/PTP distribution, GNSS vulnerability and spoofing countermeasures, and traceable time sources.
- **Where applicable**: Any operator of DC or interconnect infrastructure whose correctness depends on clock sync. Netherlands-specific in deployment, but the GNSS-dependency problem is universal.

### Migration in Curaçao

**Links:** [Recording](https://www.youtube.com/watch?v=ruWd92r3XdY)

Marianny Vallejo — AMS-IX

- **Why**: A migration story from an operator actually doing it — AMS-IX runs AMS-IX Caribbean in Curaçao, so this is likely a platform or infrastructure migration executed in a smaller, resource-constrained environment. Migration war stories are among the most transferable operator talks.
- **What**: Unknown — the program lists only the title and the AMS-IX Technical Track tag. The subject is presumably the migration of AMS-IX's Caribbean exchange operations (platform, connectivity, or services) and the lessons from executing it. *(from abstract only; no description published)*
- **How**: Unknown from the program text.
- **Where applicable**: Operators planning platform migrations, especially in small-market/low-redundancy environments where the usual "do it in parallel over six months" playbook doesn't fit. Scale and topology are specific; the migration discipline is general.

### European Network update

**Links:** [Recording](https://www.youtube.com/watch?v=pvj4XUIppec)

Patrick Christian — TeleGeography

- **Why**: The PM's DC/WAN interconnect interest includes knowing where capacity, cables, and traffic are moving. TeleGeography is the standard reference for exactly this, and an annual European update compresses a year of cable, capacity, and resilience developments into one session.
- **What**: Connectivity and resilience developments across European networks, per the one-line abstract — expect capacity and pricing trends, new subsea/terrestrial routes, and concentration/resilience analysis of European interconnect. *(from abstract only)*
- **How**: N/A — a landscape/market intelligence talk rather than a mechanism talk.
- **Where applicable**: Useful context for anyone doing DC siting, interconnect strategy, or peering in Europe; not a technique to adopt, but input to strategy.

### An overview of the services offered for free to the community by Team Cymru

Massimiliano Stucchi — Team Cymru

- **Why**: Security telemetry is expensive; free, reputable, community-funded services are an easy adoption decision, and an inventory talk is precisely the kind of immediately actionable content operator digests should surface. For the PM's security remit, this is a shortcut to knowing what's available without procurement.
- **What**: Exactly what the abstract says: a survey of Team Cymru's no-cost community services. Team Cymru is well known for free offerings to the operator community — historically including bogon filtering/route-server projects, ASN/IP ownership lookups, and DDoS-response assistance — though the specific set covered in this talk is not enumerated in the program. *(from abstract only)*
- **How**: N/A — this is a services overview, not a research contribution.
- **Where applicable**: Any network operator, of any scale. The main caveat is verifying current service terms; "free to the community" services have their own qualification and fair-use processes.

### Panel: Digital backbone or national risk?

**Links:** [Recording](https://www.youtube.com/watch?v=sv8Z3oxkM1s)

Stijn Grove — Dutch Data Center Association; Elina Gansetska — Ministry of Digital Transformation of Ukraine; Taras Stetsenko — Ministry of Digital Transformation of Ukraine

- **Why**: For a PM whose core work is physical datacenter networking, the policy layer increasingly shapes what can be built: siting, power, sustainability mandates, and sovereignty requirements. The Ukrainian participation is what elevates this — first-hand perspective on keeping digital infrastructure running under physical attack is among the hardest-won operational lessons available anywhere.
- **What**: A policy panel on organizing data and data centres "smartly, sovereignly, and sustainably" — i.e., how national digital infrastructure should be planned, with the contrast between the Netherlands' DC market and Ukraine's wartime digital-continuity experience. *(from abstract only)*
- **How**: N/A — panel format; expect policy framing with some operational color from the Ukrainian side.
- **Where applicable**: Relevant to DC siting/strategy in Europe generally; the Ukrainian resilience lessons are distinctive and broadly instructive for continuity planning.

## Wildcard

### From AI to Quantum in Space: Why Now?

Melchior Aelmans — IonQ

- **Why**: Not a fit for any of the PM's core areas — included because quantum networking is one of the few technologies that could restructure secure interconnect and key distribution over the next decade, and a "quantum in space" framing signals where serious money is being spent. The PM should know the shape of the pitch even if they don't act on it.
- **What**: Unknown — the program publishes only the title. From the title and the speaker's employer, expect a case for near-term satellite-based quantum communication and its entanglement with AI-era compute demands. No abstract was published. *(from abstract only; no description published)*
- **How**: Unknown from the program text.
- **Where applicable**: Caveat: this is a keynote from a quantum-computing vendor, so treat it as a signal of vendor direction and hype temperature rather than an engineering assessment. Watch, don't budget.

### The infrastructure you don't see is the infrastructure we could lose

**Links:** [Recording](https://www.youtube.com/watch?v=2auSpnKdrOw)

Gijs Tuinman

- **Why**: The title points at hidden dependencies — the substrate of fiber, exchanges, power, and time that nobody notices until it fails — which is a framing that tends to produce genuinely uncomfortable lists of single points of failure. That's the kind of talk a PM with DC-fabric responsibility benefits from precisely because it's not their daily vocabulary.
- **What**: Unknown — the program publishes only the title and speaker, with no abstract or affiliation. From the title alone, expect an essay-style talk on invisible critical infrastructure and its fragility. *(from abstract only; no description published)*
- **How**: N/A.
- **Where applicable**: Unverifiable from the program; attend for perspective, not technique.

## Themes

- **The internet core is back on the table.** Two of the strongest technical sessions — SCION and IPv4-with-IPv6 next-hops — both attack the interdomain layer. Path-aware security and v6-only cores are moving from papers into operator-venue talks, a sign these transitions are entering deployment discussions rather than research agendas.
- **Foundational services get renewed attention.** Time dissemination, routing hygiene, and free community security services form a quiet cluster: the boring-but-critical substrate layer that operators are re-investing in after years of taking it for granted.
- **Resilience and sovereignty dominate the policy track.** Between the digital-backbone panel, strategic-autonomy talks, and Ukrainian ministry participation, the policy spine of this event is clearly national-infrastructure resilience — with wartime continuity as the extreme case study.
- **The host's operational track is the technical core.** AMS-IX's NOC update, automation talk, and Curaçao migration are the only sessions where production practice is presented directly — thin on abstracts but the most transferable content in the program.
- **Notably low program transparency.** Most sessions publish no description at all, which is itself a signal about how this event positions itself: relationship-driven and operator-attended rather than content-browseable. Plan attendance by speaker and track rather than by abstract.
