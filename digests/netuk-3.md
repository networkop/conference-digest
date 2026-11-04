<!--
conference: NetUK3 (The Brewery)
type: operator
source_url: https://indico.netuk.org/event/3/
generated: 2026-11-03
registry_key: netuk-3
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# NetUK3 (The Brewery) — Digest

A compact UK operator event (~24 sessions). The program skews heavily toward exactly this reader's core interests this cycle: physical-layer optics and fibre, routing security, and source-of-truth/automation tooling. Picks below are grouped by relevance; sponsor sessions with pitch-like abstracts (Infoblox "Protocol-as-a-Service", Megaport agentic NaaS) were skipped as picks, though Megaport's topic is noted in Themes.

## Core

### LON2 Network Refresh

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/58/) · [Slides](https://indico.netuk.org/event/3/contributions/58/attachments/58/222/LON2_V12.pptx) · [Recording](https://www.youtube.com/watch?v=_4ZZImbGu6g)

Jan Kayser (LINX)

- **Why**: The rarest commodity at an operator conference — a public postmortem-flavored account of refreshing a production fabric with live members on it. LINX ran the world's first disaggregated EVPN IXP LAN (2018) with hardware and software from different vendors, so their refresh story is a directly transferable lesson in multi-vendor fabric migration risk.
- **What**: How LINX refreshed LON2, their second-biggest London LAN, while roughly a third of LINX membership remained connected — and the title's pointed "or was there?" promises the parts that went wrong, not just the happy path (from abstract only).
- **How**: Per the abstract: an in-house, redundant dual-LAN design (LON1/LON2 since 2002, deliberately avoiding a single point of failure for UK connectivity), EVPN control plane on disaggregated hardware/software, migrated around end-of-life equipment. The talk is short (10 min + Q&A); expect the migration sequencing and failure detail rather than deep architecture.
- **Where applicable**: The dual-LAN IXP resilience model is LINX-specific, but the underlying problem — refresh an EVPN fabric in place without evacuating tenants — is universal for anyone running a DC or exchange fabric. Watch for what the multi-vendor sourcing actually cost them operationally.

### Hollow Core Fibre - Nothing is better than glass for guiding light

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/47/) · [Slides](https://indico.netuk.org/event/3/contributions/47/attachments/50/196/260626%20H+S%20Hollow-Core%20Fiber.pptx) · [Recording](https://www.youtube.com/watch?v=-xVyeopGlp4)

Steve Jones (Huber+Suhner)

- **Why**: Hollow-core fibre is the first genuine step-change in transmission medium in decades — guidance through air rather than glass — and it is being positioned specifically for datacentre interconnect and AI compute-cluster links, which are core DC/WAN interconnect territory.
- **What**: A technology primer on HCF: how it works, the performance benefits, the application space (the event page summary confirms explicit coverage of DCI and AI compute cluster usage), and — crucially — the constraints of deploying it into a market dominated by singlemode fibre and LC/APC connectors, including a proposed solution to the HCF-to-LC/APC interop conundrum.
- **How**: Physics-level: light guided in an air core rather than solid glass, which changes latency, nonlinearity, and loss characteristics; the talk covers what that buys operationally and where the connector/splicing ecosystem still fights the installed SMF base.
- **Where applicable**: DCI, low-latency backhaul, AI cluster interconnects. Vendor talk (Huber+Suhner, a connectivity supplier), but the abstract is about the technology category and its constraints rather than a product. The practical constraint — splicing, patching, and connector maturity against a singlemode-dominated plant — is the part that matters for anyone scoping an HCO deployment.

### Which in my switch? LPO, CPO, XPO optics. What are they, when to use

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/61/) · [Slides](https://indico.netuk.org/event/3/contributions/61/attachments/61/212/2026-06-18%20LPO%20CPO%20optics%20for%20NetUK3%20v4.pptx) · [Recording](https://www.youtube.com/watch?v=OiJrMbJSNhI)

Dr Robert Friskney (Arista)

- **Why**: Optics format choice is now a switch-architecture decision, not a line-item: LPO, CPO, and XPO change power, latency, port density, and the vendor lock-in surface of a fabric. Anyone planning 800G/1.6T generations needs this decision framework.
- **What**: An explainer and decision guide: what linear-drive pluggable optics (LPO) are versus traditional DSP-based pluggables; how co-packaged optics (CPO) differs; the practical cost/latency/power trade-offs; which switch and routing use-cases LPO wins today and which it loses; how the answer shifts as port rates rise; and the future evolution toward CPO's density versus the alternative "extra-dense pluggable" (XPO) approach (from abstract only — the event page confirms it is a reprise of a well-received community talk at Net.Ldn with the Q&A topics folded in).
- **How**: LPO removes the DSP for short-reach links (trading reach and interoperability margin for power and latency savings); CPO integrates optics into the switch package; XPO keeps pluggability while pushing density — the talk maps each onto switch/routing use-cases.
- **Where applicable**: Short-reach in-fabric and backplane-adjacent links are the LPO sweet spot; CPO/XPO are next-generation switch design questions. Arista-led, so expect some roadmap framing from a switch vendor's perspective, but the material is a category primer, not a product pitch.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/48/) · [Recording](https://www.youtube.com/watch?v=LcyrmUooBoA)

Dr Gerhard Stein (Flexoptix)

- **Why**: Power per port is becoming a first-order datacenter constraint and transceivers are a large, controllable share of it. This is one of the few talks showing a concrete, measurable method for cutting optical power without performance loss.
- **What**: A data-driven method using Versatile Diagnostics Monitoring (VDM) — internal transceiver telemetry available in modern >100G optics — to find operating conditions that minimise wattage. The event page summary confirms the analysis focuses on Thermoelectric Cooler (TEC) current and laser current, correlated against temperature and total power draw. The authors built software prototypes and analyse real-world VDM data to evaluate and visualise transceiver efficiency in Watts.
- **How**: Correlation analysis of TEC/laser current against temperature (and cable length) to identify optimal operating points — essentially treating existing per-transceiver telemetry as a power-optimisation sensor rather than just a health alarm.
- **Where applicable**: Broadly applicable to any operator of >100G optics — the metrics are standard transceiver telemetry, not vendor-proprietary, so the method is replicable with any VDM-capable fleet. Caveat: results are prototype-stage from a transceiver vendor, so treat the savings claims as directional until reproduced on your own hardware.

### Data Signal-Based Distributed Fibre Optic Sensing

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/62/) · [Slides](https://indico.netuk.org/event/3/contributions/62/attachments/62/173/netuk2026v2.pptx) · [Recording](https://www.youtube.com/watch?v=Dzgv73Z_q1Y)

Jasmine Parkes (Comtek Network Systems and Bangor University)

- **Why**: Physical fibre plant causes roughly a third of network outages, and conventional distributed fibre sensing (DAS) requires dedicated fibre pairs and extra lasers — capex that blocks most operators. This is the physical-infrastructure talk of the program.
- **What**: A "Data-Driven Sensing" architecture from a joint R&D initiative (Bangor University's DSP Centre of Excellence, Sorrento, and Comtek Networks) in which the live, revenue-carrying data signal itself acts as the sensor. Validated to classify and localise fibre faults with ~98% claimed accuracy, with no extra fibre assets, no additional lasers, and no downtime — eliminating the standalone-DAS capital overhead. The talk closes with a research roadmap toward simultaneously monitoring physical infrastructure running alongside fibre routes.
- **How**: DSP-based analysis of the active data signal's own impairments/reflections to detect, classify, and locate faults on the in-service fibre, instead of injecting a separate sensing signal on a dark pair.
- **Where applicable**: Operators of backbone or critical leased routes without spare fibre to dedicate to sensing. This is R&D-stage output from an academic/industry collaboration, not a shipping product — treat it as a strong signal of where fibre monitoring is heading rather than something to procure this quarter.

### When UK Traffic Takes an Unplanned Detour: Routing Security for the UK Peering Community

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/46/) · [Slides](https://indico.netuk.org/event/3/contributions/46/attachments/49/217/Ritesh%20NetUK%202026.pptx) · [Recording](https://www.youtube.com/watch?v=dXdWl9ZkpS0)

Ritesh Mukherjee (Nokia)

- **Why**: Routing security is core network security, and this is the program's substantive treatment: it moves past RPKI-ROV checklists to the attack classes ROV cannot see, grounded in real incidents (the 2019 Swiss leak of 70,000 routes via China Telecom Frankfurt; the 2025 BGP hijack disrupting DNS root infrastructure; documented "stealthy" hijacks that pass all RPKI checks).
- **What**: A practical, prioritised roadmap for UK peering networks: what LINX and LONAP route-server RPKI filtering already protects against; where bilateral (non-route-server) peers remain exposed; an introduction to ASPA, which all five RIRs have committed to supporting by end-2026; and the case for BMP as the missing observability layer that turns silently discarded invalid routes into active threat intelligence (from abstract only — the event page reproduces the abstract).
- **How**: A layered defence model: ROV on route servers (deployed), ROV on bilateral sessions (gap), ASPA for path-manipulation and valley-free enforcement (emerging), BMP-driven route monitoring for anomalies invisible to both ROV and ASPA (observability gap).
- **Where applicable**: Any network that peers. The framing is UK/LINX-specific but the ROV → ASPA → BMP maturity ladder is universally applicable, and the "quick wins this quarter" structure makes it actionable. Speaker is from Nokia, but the content is standards-based rather than product-based.

### Autonomous System Provider Authorisation

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/52/) · [Recording](https://www.youtube.com/watch?v=JMM7HZjbgpY)

Ralph Smit (RIPE NCC)

- **Why**: The natural companion to the talk above: ASPA is the concrete next step in RPKI path validation, and this is the operator-facing how-to from the registry that runs hosted RPKI for most of Europe.
- **What**: An introduction to ASPA objects — a relatively new RPKI object type signed by AS owners that declares an AS's authorised upstream providers, preventing route leaks, BGP path spoofing, and valley-free violations. Covers how to create ASPA objects (hosted RPKI at ARIN/RIPE NCC, or delegated CA software such as Krill) and the current state of uptake, including support in some software routers (from abstract only).
- **How**: An AS signs an ASPA listing its providers; validators can then reject paths in which the AS appears to route via an unauthorised upstream — enforcing a signed, valley-free provider relationship.
- **Where applicable**: Any AS owner; ASPA creation is available today through the mainstream hosted and delegated RPKI paths, so this is directly actionable rather than speculative. Expect a short talk (25 min) — intro-and-summary depth.

### SCION: Secure Path-Aware Internet Routing for Critical Infrastructures

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/45/) · [Slides](https://indico.netuk.org/event/3/contributions/45/attachments/48/183/SCION%20%28NetUK%203%29%20for%20presentation.pptx) · [Recording](https://www.youtube.com/watch?v=sEyzLrl_LIs)

Kevin Meynell (SCION Association)

- **Why**: SCION is the most mature "beyond BGP" routing architecture with real production deployment, and its trust model — cryptographic path validation with a standalone trust root rather than third-party CAs — sits right at the intersection of network security and the PM's identity/trust interests.
- **What**: SCION as an answer to BGP's fundamental limitation that operators have little control over where traffic transits: high resilience to routing attacks, explicit path selection, fast failover, geofencing (with a post-quantum angle), and comparison against RPKI, MPLS, SD-WAN, Segment Routing, and BGPSEC. The event page adds that it is supported by several UK-based ISPs including BT and Colt, and is in production in Swiss financial services, healthcare, and power utilities, with a vendor-neutral IETF specification in progress.
- **How**: A trust model built on logical groupings of networks ("trust domains"/ISDs) sharing a common jurisdiction and agreed trust policies, with a standalone trust root; traffic is exchanged only within a trust domain unless explicitly permitted, enabling sovereign networks and user/operator path selection.
- **Where applicable**: Initially critical infrastructure and regulated sectors (finance, healthcare, energy, defence) that need provable path control; requires SCION-capable connectivity, which in the UK is emerging via BT and Colt. Not a drop-in for commodity Internet operations, but relevant to any strategy discussion about trustworthy interconnect for critical workloads.

## Adjacent

### Edge Network Evolution

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/60/) · [Recording](https://www.youtube.com/watch?v=Gf_BOJN9roQ)

Ben Ryall, Ian Cleary (Meta)

- **Why**: A hyperscaler reshaping its edge topology for AI workloads changes the peering and traffic landscape for every operator downstream — directly relevant to DC/WAN interconnect thinking.
- **What**: How Meta's edge infrastructure is evolving from traditional content delivery to AI-driven experiences, reshaping topology to balance efficiency and quality of experience while preserving direct 1:1 peering relationships for networks of all sizes, with optimisations intended to help operators defer or avoid capex (from abstract only; the event page adds nothing beyond it).
- **How**: Architectural shifts at Meta's edge — the talk is short (10 min + Q&A) and the slides/recording will not be published, so this is attend-live-or-miss-it.
- **Where applicable**: Meta-specific scale and workload mix; useful as directional input on how AI traffic changes edge/peering economics, not as a transferable design.

### Rethinking Network Monitoring

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/55/) · [Slides](https://indico.netuk.org/event/3/contributions/55/attachments/55/182/Rethinking%20Network%20Monitoring%20%28NetUK%29.pptx) · [Recording](https://www.youtube.com/watch?v=jKhIKkGqRq8)

Mr David Flores

- **Why**: Monitoring modernisation is the flip side of automation — every session on source-of-truth and automation at this event depends on telemetry you can actually act on.
- **What**: A reframe of monitoring as observability: a modular open-source stack spanning collection, processing, storage, visualisation, and alerting, enriched with a network source of truth, correlating metrics/logs/flows, with event-driven automation and AI-assisted root cause analysis. The event page summary adds the honest trade-off framing: scale, operational overhead, and expertise costs of building your own stack, with modularity as the mitigation.
- **How**: Pair telemetry with a source of truth so data becomes queryable and context-rich, then layer automation and AI-assisted RCA on top; the speaker positions this as a pilotable blueprint.
- **Where applicable**: General technique, vendor-neutral (independent speaker), applicable to any size of network — though the "build vs buy" trade-offs the summary flags are the real decision content.

### The Network Automation Forum Framework: A vendor-neutral reference model for building automation at scale

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/63/)

Pete Crocker (OpsMill)

- **Why**: A shared vocabulary and reference architecture for network automation is the missing layer that makes automation conversations between engineers, vendors, and consultants coherent — useful for anyone mapping their own automation estate.
- **What**: A walkthrough of the Network Automation Forum's reference architecture, developed over a year by a multi-stakeholder community: why standardised language around network automation was needed and how to apply the framework both starting from scratch and retro-fitting it to what you already built (from abstract only).
- **How**: A layered reference model (published at reference.networkautomation.forum) that names the components of an automation architecture so tooling choices can be positioned against it.
- **Where applicable**: Broadly applicable — the framework is deliberately vendor-neutral even though the speaker is from OpsMill; it is a mapping tool, not a stack you deploy.

### Workshop: Open Source Data Management Platform - Infrahub

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/54/)

Alex Gittings (OpsMill), Pete Crocker (OpsMill)

- **Why**: Source of truth is the foundation every other automation talk at this event assumes; this is a hands-on evaluation opportunity for the leading open-source SoT platform rather than a slide deck about it.
- **What**: A two-hour hands-on workshop on Infrahub, an open-source infrastructure data-management platform combining Git-like version control on top of a graph database, with three pillars: flexible schema, native version control, and unified storage. Structured as two modules/labs: foundation and network source-of-truth setup (devices, IPAM, CSV/API imports), then config generation via GraphQL queries and Jinja2 templating, with a GraphQL lab using the built-in GraphiQL explorer.
- **How**: Version-controlled graph data with a flexible schema as the SoT, queried via GraphQL, feeding Jinja2 templating for config generation and integration with existing automation tools.
- **Where applicable**: Teams evaluating open-source SoT/IPAM options. Vendor-led (OpsMill builds Infrahub) but the format is working directly with the actual open-source product in a sandbox — a genuine evaluation, not a pitch.

### Telecoms Inventory for GPON using Kuwaiba

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/59/) · [Slides](https://indico.netuk.org/event/3/contributions/59/attachments/59/202/Netuk-Inventory-gpon-kuwaiba_v_1.0.pptx) · [Recording](https://www.youtube.com/watch?v=gyK6saFGk-c)

Corey Maltby (Solent University), Craig Gallen (Entimoss and Solent University)

- **Why**: Physical/logical inventory is the unglamorous prerequisite for fibre operations; Kuwaiba is a credible open-source alternative to commercial telecoms inventory systems and this is a grounded evaluation of it, including failure modes.
- **What**: An introduction to Kuwaiba (open-source telecoms inventory, originating in South America, modelling physical and logical network resources and services at significantly lower cost than commercial systems) via a student industrial consulting project: modelling a city-wide GPON network in Kuwaiba populated from UK UPRNs and OpenStreetMap GIS data. The event page summary adds discussion of the issues with populating the system from UK public GIS data sources, plus an offered demo.
- **How**: GIS data import (UPRNs, OpenStreetMap) into Kuwaiba's resource model to design and document a citywide GPON deployment — testing how practical the tool and data pipeline are.
- **Where applicable**: ISPs and service providers, especially UK altnets building fibre; the GIS-data-quality findings are UK-specific, but the Kuwaiba evaluation is relevant to any operator weighing open-source inventory.

### Everything is Fine and Our Automation Works Perfectly

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/67/) · [Recording](https://www.youtube.com/watch?v=IBur_6W_8rE)

Stefan Funke (Inter.link)

- **Why**: A wry counterpoint to the automation track: automation is only as good as the data counterparties feed it (IRR records, RTBH fields, survey data), which ties directly back to the routing-security sessions.
- **What**: Per the title and one-line abstract, an operator's account of what their "working perfectly" automation actually requires from others — updated IRR, RTBH fields, and survey compliance (from abstract only — the program text gives just the punchline).
- **How**: Unknown from the abstract; expect a short lightning-format talk on the human/data prerequisites of inter-operator automation.
- **Where applicable**: Peering and transport automation; content cannot be verified in advance from the thin abstract, so treat as a low-commitment slot filler between the LON2 and SCION talks.

## Wildcard

### Data Centers in Space - The Big Picture

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/57/) · [Slides](https://indico.netuk.org/event/3/contributions/57/attachments/57/163/2026-04%20Data%20Centers%20in%20Space%20-%20NetUK3%20.pptx) · [Recording](https://www.youtube.com/watch?v=kWVAEDEfPEQ)

Geoff Bennett (Nokia)

- **Why**: Not a core interest, but a rigorous reality-check on the extreme extrapolation of the PM's daily constraints — space, power, water, permitting — from a respected industry explainer. If multi-gigawatt AI campuses are colliding with those limits on the ground, this is the "what if we simply left" scenario, with the failure modes taken seriously.
- **What**: A critical assessment of orbital data centers: what problems the idea is actually trying to solve, the technologies that must be developed, the scale that would be required, and the unavoidable consequences — anchored in real signals: SpaceX's January FCC filing for up to one million "orbital data center" satellites, Google's Project Suncatcher suggesting viability as soon as 2027, and funded startups. The speaker explicitly asks which problems are simply insoluble, and what damage filling orbit this way inflicts (from abstract only).
- **How**: Structured as problem-first analysis rather than hype: constraints (launch mass, radiation, thermal rejection, serviceability, debris) versus the terrestrial pain (power, water, land, community backlash) the idea claims to escape.
- **Where applicable**: Strategic/forward-looking context rather than actionable practice — useful for anyone calibrating where compute placement could plausibly go over the next decade, and a well-informed sceptic's set of questions to hold vendor narratives against.

### Evaluation of BGP Roles (RFC 9234) with the aid of an AI Assistant

**Links:** [Abstract](https://indico.netuk.org/event/3/contributions/51/) · [Slides](https://indico.netuk.org/event/3/contributions/51/attachments/52/174/NETUK-July26-JLUCEK-v3.pptx) · [Recording](https://www.youtube.com/watch?v=yRt_72zC9EA)

Dr Julian Lucek (HPE)

- **Why**: The clearest signal in this program of where the network operations toolchain is heading — LLMs driving device configuration through MCP servers — demonstrated on a routing-security feature (RFC 9234 BGP Roles, itself a route-leak mitigation) by one of networking's best-known educators.
- **What**: Three parts: benchmarking results showing a general-purpose reasoning LLM (Opus 4.7, per the event page summary) achieving solid scores across three tiers of a network certification exam track; a retrospective analysis of a real past network outage showing LLMs would have found the root cause significantly faster; and the main demo — an LLM driving a Junos MCP server to configure, test, and document BGP Roles from just a few, deliberately vague prompts, with the LLM filling in missing details in an intent-based manner and proving a substantial time-saver over manual work.
- **How**: LLM + Model Context Protocol server pattern: the model discovers device capabilities and state through the MCP tool interface, plans the configuration, executes and validates it, and generates the documentation — the human supplies intent, not commands.
- **Where applicable**: Junos-specific in the demo (Junos MCP server), and a single-operator workflow at demo scale — but the pattern (LLM agent over an MCP tool surface, applied to a security-relevant protocol feature) is the transferable idea, and directly relevant to how network engineering work changes in the near term.

## Themes

- **Routing security's centre of gravity is shifting from ROV to ASPA + observability.** Three sessions (Mukherjee's roadmap, Smit's ASPA how-to, Lucek's RFC 9234 demo) converge on the same point: route-server RPKI filtering is table stakes, and the frontier is signed path validation (ASPA, with all five RIRs committing by end-2026) plus BMP-based detection of hijacks that pass every RPKI check.
- **The physical layer is the hot topic again, driven by AI-cluster economics.** Four sessions — hollow-core fibre, LPO/CPO/XPO, VDM transceiver power telemetry, and data-signal DFOS — cover fibre, optics, and power. The common driver is AI compute: latency budgets for cluster interconnects and watt budgets per port.
- **Power is the new latency.** Transceiver watt optimisation, LPO's DSP elimination, Meta's edge efficiency work, and orbital datacenters (framed as an escape valve for power/water/permitting limits) all treat energy as the binding constraint on next-generation infrastructure.
- **Open-source source-of-truth tooling is consolidating.** Infrahub (SoT with Git-like versioning), Kuwaiba (telecoms inventory), the NAF automation framework, and the monitoring-as-observability blueprint all push credible OSS alternatives to commercial NMS/inventory stacks — the operator community is standardising its data layer before its automation layer.
- **Agentic AI has reached the network toolchain.** Lucek's LLM-over-MCP configuration demo, Flores' AI-assisted root cause analysis, and even the Megaport sponsor slot on MCP-driven NaaS all point the same direction; expect MCP servers for network devices to become standard vendor surface area.
- **Postmortems and operational honesty remain the currency of operator events.** LINX's refresh story ("...or was there?"), Lucek's retrospective outage analysis, and Inter.link's automation punchline are the sessions designed to transfer hard-won lessons rather than roadmaps.
