<!--
conference: DKNOG16 (Scandic Copenhagen)
type: operator
source_url: https://events.dknog.dk/event/35/
generated: 2026-11-04
registry_key: dknog-16
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# DKNOG16 — Digest

A tight operator program: two optics/transport talks, an RPKI-adjacent routing-security session, a cable-outage postmortem, and a strong run of automation/modeling talks. Note on sourcing: the DKNOG event pages mirror the program abstracts and add only session metadata (times, formats, materials), so every write-up below is grounded in the abstract plus that metadata. Skipped as out of scope: the quiz, DKNOG announcements, and the personal/career talks ("Lost in translation", "A different way to success", "Old habits die hard").

## Core

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/310/) · [Recording](https://www.youtube.com/watch?v=pLMLl6Js2vo)

Gerhard Stein (Flexoptix GmbH)

- **Why**: Transceiver power draw is a growing slice of DC and WAN opex, and this is one of the few talks showing how to extract savings from data the optics already expose — no hardware swap required. Squarely in the PM's physical-optics territory.
- **What**: An analysis of Versatile Diagnostics Monitoring (VDM) metrics in modern (>100G) optical transceivers, focused on Thermoelectric Cooler (TEC) current, correlated with temperature and cable length, to find operating conditions that minimize power while holding performance. Software prototypes were built to evaluate and visualize transceiver efficiency in Watts using real-world VDM data. (from abstract only)
- **How**: TEC current acts as a proxy for how hard the module is working to hold its temperature setpoint; correlating it with temperature and cable length across real deployment data reveals which optics and link types operate inefficiently and quantifies the per-link watts.
- **Where applicable**: Any fleet of >100G pluggables that expose VDM — the metrics come from the transceiver, not a specific switch, so the technique is broadly transferable to DC, metro, and WAN optics. Caveat: the speaker is from a transceiver vendor, so expect some product framing around a genuinely vendor-neutral technique.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/313/) · [Recording](https://www.youtube.com/watch?v=rV6xxDxmpcs)

Thomas Weible (no affiliation listed; material made with FLEXOPTIX Research)

- **Why**: Grid and spectrum planning for 800G/1.6T superchannels is a near-term, irreversible decision for anyone owning DWDM for DC/WAN interconnect; filter choices made today can lock a network out of 1.6T tomorrow.
- **What**: A case for moving DWDM channel plans to larger grids (up to 400GHz, with COTS filters) to accommodate 400G/800G/1.6T coherent superchannels, while retaining backward compatibility with legacy 50GHz services — and an argument that IP engineers must now understand coherent optics in the IPoDWDM era. (from abstract only)
- **How**: High-baud coherent superchannels need far more spectrum than legacy 50/100GHz slots; coherent detection being "blind" to anything but its own wavelength enables filterless topologies, but at the cost of flexibility. Wider COTS filters both open the growth path to 1.6T and coexist with legacy narrow-grid services.
- **Where applicable**: Operators of their own DWDM/IPoDWDM infrastructure — DC interconnect, metro, and regional transport. Networks locked into 50GHz-gridded plants face the harder migration. The content is standard transport engineering despite the FLEXOPTIX Research affiliation; discount for any product positioning around their filter/solution portfolio.

### ASPA: the new protocol for improving BGP routing security

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/311/) · [Recording](https://www.youtube.com/watch?v=ffraqoKFjPI)

Ondřej Caletka (RIPE NCC)

- **Why**: Routing security is moving from origin validation to partial path validation, and ASPA deployment decisions are landing on BGP operators now — directly within the PM's network-security scope.
- **What**: An introduction to Autonomous System Provider Authorization, the next RPKI feature being deployed after Route Origin Authorization: each AS can cryptographically declare which ASes are expected to provide it transit, and operators performing ASPA validation can drop routes arriving via unauthorized providers. (from abstract only)
- **How**: RPKI-signed provider-authorization objects let validators check a received route's propagation path against the declared transit graph, catching route leaks and hijacks propagated through unauthorized providers — complementing, not replacing, ROV.
- **Where applicable**: Any BGP operator — transit, enterprise, or DC — building on existing RPKI/ROV deployments. Deployment is early, so the practical constraints (who signs objects, which platforms validate) are the things to listen for. RIPE NCC is a registry, not a vendor, so no product-pitch risk.

### IXP+ based observations on peering and routing changes after Middle East cable outages

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/314/) · [Slides](https://events.dknog.dk/event/35/contributions/314/attachments/140/369/02%20-%20IXP%20based%20observations%20on%20peering%20and%20routing%20changes.pptx) · [Recording](https://www.youtube.com/watch?v=SKXpK6Rz_2o)

Kaj Kjellgren and Bernd Speiss (DE-CIX)

- **Why**: A physical-layer failure with measurable routing consequences — exactly the kind of concrete postmortem that transfers across environments. Relevant to anyone whose traffic depends on intercontinental cable paths.
- **What**: Observations from DE-CIX data of trends and changes in routing and traffic after the cable cuts near the shore of Yemen in September, explicitly framed as do's and don'ts for routing setup, with the authors arguing the findings hold globally. (from abstract only)
- **How**: IXP-side analysis of traffic volumes, route announcements, and peering behavior before and after the cuts — who rerouted successfully, who lacked alternate paths, and what the shifts revealed about regional routing setups.
- **Where applicable**: The specific observations are tied to the Middle East corridor and DE-CIX's vantage points (single-IX perspective), but the resilience lessons — path diversity, alternate peering, routing hygiene under failure — apply to any operator with intercontinental dependencies.

### Auto-bandwidth for SR-TE

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/315/) · [Recording](https://www.youtube.com/watch?v=RgEwds8kQRI)

Dmytro Shypovalov (Vegvisir Systems)

- **Why**: Bandwidth-aware SR-TE has been vendor-locked to date; this is an open-standard, multi-vendor prototype with an open-source component — the kind of adoptable tooling that matters for anyone running SR policies across a WAN or DC interconnect.
- **What**: A prototype auto-bandwidth solution for Segment Routing Traffic Engineering that is open-standard and multi-vendor (in contrast to existing vendor-specific mechanisms), plus an open-source "SR-TE bandwidth sampler" that collects SR policy counters via gNMI, calculates traffic rates, and converts them into BGP-LS format per RFC 9857. (from abstract only)
- **How**: Streaming telemetry of SR policy counters (gNMI) → traffic-rate computation → BGP-LS encoding per RFC 9857, so the SR-TE control plane or controller can resize policies from measured load without any vendor-proprietary signaling.
- **Where applicable**: Networks running SR policies — SP WANs and large DC-interconnect fabrics; requires gNMI-capable devices and BGP-LS support for the relevant encodings. It is explicitly a prototype, so expect a demo and roadmap rather than production tooling. Vegvisir Systems is a vendor in this space, but the open-source sampler lowers the pitch risk; evaluate the open components on their own merits.

## Adjacent

### Network Automation in the Modern Age

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/325/) · [Recording](https://www.youtube.com/watch?v=zBW63nHiia8)

Marcus Stoegbauer and Veit Heller (no affiliation listed)

- **Why**: The "source of truth / data model" problem is the current wall in netops automation — most teams past the template stage hit it. This names the next stage rather than selling a tool.
- **What**: A reflective talk tracing automation from template-pushing to variable storage in documentation systems/DCIMs, arguing the next stage demands modeling the world explicitly, unconstrained by DCIM limits — and that automation designers now need deeper data-modeling skills than the tools teach. Explicitly a conversation-opener, with a glimpse of an early draft solution. (from abstract only)
- **How**: Conceptual — decoupling the network's world-model from the documentation system that stores it; no finished tool is presented.
- **Where applicable**: Any netops team that has outgrown templates and found its DCIM's model shaping (and limiting) its automation. Conceptual rather than deployable; the value is the framing and the community discussion it opens.

### How far can you get with IX Route Servers?

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/320/) · [Slides](https://events.dknog.dk/event/35/contributions/320/attachments/145/359/How%20far%20can%20you%20go%20with%20IX%20Route%20Servers%20only_%20%5BDKNOG%5D.pptx) · [Recording](https://www.youtube.com/watch?v=3Dh1vVqNUOg)

Ben Cartwright-Cox (bgp.tools)

- **Why**: Peers rarely question whether route server routes are actually imported; this replaces that folklore with measurement across many exchanges. Evidence-based peering strategy at a large scale.
- **What**: A quantification of route server effectiveness — how relevant they are, how many participants actually import from them, and who those importers are — using the bgp.tools route collector network's deployment footprint across many internet exchanges. (from abstract only)
- **How**: Collector-based observation at many IX fabrics, comparing routes offered by route servers against what participant networks actually accept.
- **Where applicable**: IXP participants of all sizes; findings depend on bgp.tools's collector footprint (large but not exhaustive). Useful input for deciding how much to invest in bilateral peering vs. relying on the RS.

### Automate what makes sense: Data, principles and practice

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/332/) · [Slides](https://events.dknog.dk/event/35/contributions/332/attachments/149/389/DKNOG16-automate_what_makes_sense.pptx) · [Recording](https://www.youtube.com/watch?v=-245o3mEwr8)

Brian Jeggesen (no affiliation listed)

- **Why**: Diagnoses the commonest automation failure mode — tools are fine, the organization stalls — and gives a concrete starting step rather than a framework pitch.
- **What**: An explanation of why "automate what makes sense" becomes a permanent excuse to automate nothing: unclear definitions of "safe" and "correct," fragile inputs, and changes that can't be proven before shipping. Offers a pragmatic path to make automation a normal way of working, with guardrails and evidence instead of optimism, and a first step implementable immediately. (from abstract only)
- **How**: Principles-and-practice approach — pre-ship proof of correctness, guardrails, and incremental confidence-building rather than heroic one-off projects.
- **Where applicable**: Any network organization; general technique with no scale or topology dependency.

### Introduction to Design-Driven Network Automation

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/326/) · [Recording](https://www.youtube.com/watch?v=_wOCLoSAG10)

Mark Coleman (no affiliation listed)

- **Why**: The design/intent layer above config generation is where network automation platforms are converging; this gives the conceptual grounding and — usefully — covers where the approach still fails.
- **What**: Design-driven automation treats the high-level design as a first-class artifact: an explicit model of topology, roles, relationships, and constraints, independent of any device configuration. Traces the idea from early topology-aware NMS and fabric controllers to modern intent-based systems, and covers how state, drift, refactoring, and unplanned change are reasoned about from a design model. (from abstract only)
- **How**: Modeling and reasoning mechanics rather than a specific tool — how networks are represented as designs and how change over time is interpreted against them.
- **Where applicable**: Networks at the scale or complexity where per-device config models break down; relevant to DC fabrics and multi-site estates alike. Conceptual survey; judge it by the "where it still struggles" section.

### Merging Service Provider Networks

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/312/) · [Recording](https://www.youtube.com/watch?v=OKOIWvWRtLY)

Bastian Hoss and Markus Jungbluth (Xantaro Deutschland GmbH)

- **Why**: SP consolidation makes IP/MPLS integration a recurring real-world project, and this is practice-based technical content (architecture, routing, interop pitfalls) rather than a methodology pitch.
- **What**: A technical walkthrough of merging distinct IP/MPLS network infrastructures: the general project approach, key architectural considerations, and challenges in routing-protocol integration and vendor interoperability, based on past project experience. (from abstract only)
- **How**: Experience-driven — lessons from actual merge projects rather than a single mechanism.
- **Where applicable**: Service-provider mergers and acquisitions; the routing-protocol and interop pitfalls also apply to enterprises consolidating DC fabrics after acquisitions. The underlying projects are unnamed, so treat specifics as consultancy experience; the pitfall list is the transferable part.

### Command-Line to Codebase: Learning Software to Expand Your Engineering Toolkit

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/316/) · [Recording](https://www.youtube.com/watch?v=E-_K7xgPEO0)

Thomas Kjær (no affiliation listed)

- **Why**: A replicable method for network engineers building small software tools, anchored on ECMP troubleshooting — a problem anyone running DC fabrics knows is painful and manual.
- **What**: The story of building a small ECMP-aware probing tool while learning a new programming language, starting from familiar tools (traceroute, Wireshark, RFCs). The contribution is the method, not the tool: start in a domain you trust, measure everything, build in small slices, test one change at a time, explain results to yourself as you go. (from abstract only)
- **How**: Incrementally translating a manual troubleshooting workflow into code, with validation steps at each slice.
- **Where applicable**: Any network engineer; ECMP troubleshooting is universal. Light on novel technical results — the value is the low-risk method for starting and sustaining small tool projects.

## Wildcard

### Sovereignty for whom? Between digital (in)dependence and Big Tech expansionism

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/323/) · [Slides](https://events.dknog.dk/event/35/contributions/323/attachments/146/351/DKNOG%2026_1.pptx) · [Recording](https://www.youtube.com/watch?v=4m0KafbzVE8)

Signe Sophus Lai and Sofie Flensburg (University of Copenhagen)

- **Why**: Not technical, but it argues the sovereignty debate is missing the layer the PM works on — who owns the submarine cables and routing economics underneath "sovereign cloud" marketing. Strategic context for infrastructure decisions, from researchers who focus on the physical layer.
- **What**: An academic analysis of how "digital sovereignty" is deployed politically — by governments (including Denmark's "liberation" of the public sector) and by hyperscalers selling sovereignty as a service — arguing that a persistent focus on applications and services over underlying infrastructure obscures the real power structures. Illustrates with research on global submarine data cable ownership changes and the conditions around global internet routing. (from abstract only)
- **How**: Social-science research synthesis — stakeholder analysis of the sovereignty debate tied to concrete infrastructure examples.
- **Where applicable**: EU/Danish policy and procurement context; strategic framing rather than operational technique. Worth the PM's time precisely because it connects cable ownership and routing to the policy language increasingly attached to infrastructure budgets.

### Geopolitics and Digital Sovereignty in Greenland

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/319/) · [Slides](https://events.dknog.dk/event/35/contributions/319/attachments/151/364/Geopolitics%20and%20Digital%20Sovereignty%20in%20Greenland%20-%20DKNOG%202026%281%29.pptx) · [Recording](https://www.youtube.com/watch?v=qcpokehiGhg)

Signe Ravn-Højgaard (Tænketanken Digital Infrastruktur)

- **Why**: An extreme-case stress test of resilience design: an entire national ecosystem hanging off two submarine cables with routing terminating abroad. It exposes failure modes (single-corridor dependence, no traffic localization) that softer versions exist in most networks.
- **What**: An examination of Greenland's structural dependence on U.S.-controlled infrastructure across multiple layers: two submarine cables plus limited satellite links, routing and traffic flows largely terminating outside Greenland, and minimal local traffic localization — and how that constrained path diversity intersects with heightened geopolitical attention. (from abstract only)
- **How**: Case analysis of connectivity topology and traffic flows (15-minute short talk).
- **Where applicable**: Greenland-specific, but the failure patterns — path diversity below the redundancy threshold, external hosting, no local traffic retention — generalize directly to any WAN resilience review. A good forcing function for asking "what is our two-cable equivalent?"

### Who put the "inter" in internet?

**Links:** [Abstract](https://events.dknog.dk/event/35/contributions/328/) · [Recording](https://www.youtube.com/watch?v=iGRMb3-hFfc)

Poul-Henning Kamp (no affiliation listed)

- **Why**: The conference keynote (60 minutes) by Poul-Henning Kamp, a veteran of internet infrastructure and FreeBSD; his keynotes reliably challenge assumptions about how the internet's interconnection and economics actually work, and the title suggests exactly that target.
- **What**: No description was published at the time of this digest ("More to come" in the program); the title points to a critical examination of what the "inter" in internet — interconnection and its ownership — actually consists of. Slides and a recording are attached to the event page, so the content can be reviewed after the fact. This item cannot be assessed beyond title and speaker.
- **How**: Unknown — no abstract available; do not assume content from the title.
- **Where applicable**: Unknown given the missing description; keynote length (1 hour, per the event page) and speaker track record alone justify attention.

## Themes

- **The photonic layer is back on operators' desks**: two substantive optics talks — transceiver power telemetry (VDM/TEC) and DWDM grid planning for 1.6T — plus the IPoDWDM blurring of the IP/transport boundary. Power-per-bit and spectrum-per-bit are now operator planning inputs, not transport-team abstractions.
- **Measurement over folklore**: bgp.tools's route-server import study and DE-CIX's cable-outage analysis both replace peering/resilience folklore with large observational datasets — the field is increasingly answering operational questions with collector data rather than opinion.
- **Routing security's second act**: ASPA represents the post-ROV phase of RPKI — partial path validation reaching operational readiness and landing on config checklists.
- **Pushback on vendor-locked tooling**: the gNMI + BGP-LS (RFC 9857) auto-bandwidth prototype is a small but clear signal that operators want open, multi-vendor mechanisms for TE, not per-vendor silos.
- **Automation's data-model turn**: three-plus talks (Stoegbauer/Heller, Jeggesen, Coleman) converge on the same diagnosis — automation maturity is now limited by how the network is modeled and how change is proven, not by template engines or DCIM features.
- **Geopolitics entering the NOC agenda**: two sovereignty talks both anchor on submarine cables and routing dependence — physical infrastructure choices are now policy-visible, and resilience reviews increasingly need a geopolitical lens alongside the technical one.
