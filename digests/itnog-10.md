<!--
conference: ITNOG10
type: operator
source_url: https://www.itnog.it/itnog10
generated: 2026-11-04
registry_key: itnog-10
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# ITNOG10 — Digest

**Source depth note:** ITNOG10 published no abstracts — the program lists only titles, speakers, and slide links, and slide content was not retrievable in this run. Every write-up below is therefore grounded in the session title (and slide-link filename) alone; items are marked *(title only)*. Where a mechanism is described with "presumably" or "expect," it is an inference about what the talk likely covers, not a claim about its contents — verify against the linked decks before acting on it.

## Core

### Integration of Security Functions in EVPN/VXLAN Using Group-Based Policy

**Links:** [Slides](https://www.itnog.it/files/1-4_202604-nmodena-EVPN-VXLAN-Group-Based-Policy-ITNOG10.pdf)

Nicola Modena

- **Why**: Sits exactly at this PM's intersection of DC fabric and network security: enforcing policy inside the EVPN/VXLAN overlay rather than bolting on perimeter appliances.
- **What**: An approach to integrating security functions into EVPN/VXLAN fabrics using Group-Based Policy. *(title only)*
- **How**: GBP as a technology tags traffic with policy-group identifiers carried in the VXLAN header so the fabric itself enforces segmentation; expect the talk to cover where security functions hook into that model — the deck has the specifics.
- **Where applicable**: EVPN/VXLAN DC fabrics. GBP support is uneven across NOS/silicon (strongest on Cisco platforms), so check which parts are portable before assuming multi-vendor applicability.

### National Layer-2 wholesale FWA leveraging VxLAN

**Links:** [Slides](https://www.itnog.it/files/1-3_202604-cbiasibetti-L2FWA-ITNOG10-Public.pdf)

Christian Biasibetti

- **Why**: A rare case study of applying DC overlay tech (VXLAN) to a national wholesale FWA backhaul — a transferable pattern for L2 service delivery over an IP core, which is squarely in the PM's fabric/interconnect space.
- **What**: Design and operation of a national layer-2 wholesale service for Fixed Wireless Access, built on VXLAN. *(title only)*
- **How**: Presumably VXLAN tunnels extending L2 domains from aggregation points toward FWA endpoints across an IP core; the deck carries the actual architecture.
- **Where applicable**: Telco wholesale/FWA context, so scale numbers may be footprint-specific; the L2-service-over-VXLAN pattern itself is broadly reusable.

### BGP nell'underlay multi-cloud: resilienza e simmetria tra on-prem e public cloud

**Links:** [Slides](https://www.itnog.it/files/1-17_ITNOG10-BGPunderlayMultiCloud-CPLC-20260421.pdf)

Carlo Pio Luigi Ciciriello

- **Why**: Directly the PM's cloud-native networking and DC/WAN-interconnect territory: BGP design for hybrid underlays, where resilience and return-path symmetry are the genuinely hard parts.
- **What**: A BGP underlay design spanning on-prem DCs and public clouds, targeting failover resilience and traffic symmetry between the two. *(title only)*
- **How**: Expect session/policy design and path selection across dedicated cloud interconnects to keep flows symmetric on both failover and normal operation — the classic pitfall this class of talk addresses.
- **Where applicable**: Broadly applicable to any hybrid/multi-cloud design using dedicated interconnects (Direct Connect/ExpressRoute-style), operator or enterprise.

### Open Networking and IPoDWDM in Production: Operational Lessons from European Networks

**Links:** [Slides](https://www.itnog.it/files/2-17_IPoDWDM%20400G%20ZR+%20ITNOG10%20v1.pdf)

Alessandro Giudice

- **Why**: IPoDWDM with 400G ZR+ pluggables (per the slides filename) is the current frontier of router-integrated coherent optics for DCI/WAN interconnect — and production lessons from real European networks, not vendor spec sheets, are the valuable part.
- **What**: Operational experience running open networking / IPoDWDM (400G ZR+) in production across multiple European networks. *(title only)*
- **How**: Coherent 400G ZR/ZR+ pluggables terminated in router ports, collapsing the transponder layer; expect real-world issues around optical budgets, multivendor interoperability, and troubleshooting.
- **Where applicable**: DCI and WAN interconnect generally. The multi-network framing suggests lessons transfer beyond a single operator's setup.

### Hollow Core Fibre - Nothing is better than glass for guiding light

**Links:** [Slides](https://www.itnog.it/files/1-11_ITNOG_hollowcorefiber.pdf)

Steve Jones

- **Why**: Hollow-core fiber is the most-watched optics disruption (ultra-low latency, low nonlinearity), and the title reads as a deliberately contrarian, pro-solid-glass take — exactly the skeptical operator perspective worth hearing before buying into the hype. Pure PM optics territory.
- **What**: An assessment of hollow-core fiber versus conventional solid glass fiber for guiding light. *(title only)*
- **How**: Presumably a physics-and-operations comparison — latency, attenuation, nonlinearity, cost, and deployment maturity; verify the framing in the deck.
- **Where applicable**: Long-haul, subsea, and latency-sensitive DCI routes; the practical constraints are reach, cost, and maturity of supply.

### SRv6 uSID: Deterministic AI Backend Networking and Unified DC Frontend Design

**Links:** [Slides](https://www.itnog.it/files/1-13_2026_ITNOG_adonzell_Cisco-final.pdf)

Alberto Donzelli — the slides filename ("Cisco-final") indicates a Cisco-affiliated session; treat as a vendor-informed design pattern, not a neutral case study

- **Why**: AI backend networks are the hottest fabric-design problem right now (deterministic, lossless behavior for collective/parallel traffic) — squarely in the PM's RDMA/lossless-fabric interest.
- **What**: A design combining SRv6 micro-segment (uSID) networking for AI backend traffic with a unified frontend/DC architecture. *(title only)*
- **How**: uSID compresses many segments into a single IPv6 address for fine-grained steering; the claim to verify in the deck is how SRv6 delivers "deterministic" backend behavior and how frontend and backend unify under one addressing scheme.
- **Where applicable**: Requires SRv6/uSID-capable silicon and NOS, so the mechanism is partially vendor/silicon-bound; the AI-backend problem framing transfers across the industry.

### MIX DC3

Mauro Magrassi — MIX (Milan Internet exchange)

- **Why**: A buildout talk for an IXP's third datacenter — pure physical-DC territory (space, power, topology, fabric, inter-site connectivity) at a facility whose uptime matters to the Italian internet.
- **What**: Presentation of MIX's new DC3 facility. *(title only — no abstract; likely design and service roadmap for the new site)*
- **How**: Unknown from the program; expect site selection, fabric/topology design, and how DC3 interconnects with the existing MIX estate.
- **Where applicable**: IXP/colo context; DC buildout lessons (power density, topology, inter-DC links) are broadly relevant.

### Inside Seabone: experiences of a Tier-1 Backbone

**Links:** [Slides](https://www.itnog.it/files/1-9_ITNOG_%20Inside%20Seabone%20-%20Experiences%20of%20a%20Tier-1%20Backbone.pdf)

Gabriele Laghi, Patrizia Rossi, Antonio Ferretti

- **Why**: A Tier-1 operational tell-all is exactly the "failure stories and hard-won lessons" category this PM up-ranks — Tier-1 backbones see failure modes no one else does.
- **What**: Behind-the-scenes operational experiences running the Seabone Tier-1 IP backbone. *(title only)*
- **How**: Unknown; expect scale, peering, capacity engineering, and incident practice from the deck.
- **Where applicable**: Tier-1/transit scale — some lessons are inherently scale-dependent, but the operational patterns (maintenance, convergence, tooling) transfer.

### Migrazione del nostro Backbone a SR-MPLS perdendo pochi ping...

**Links:** [Slides](https://www.itnog.it/files/1-2_Il%20nostro%20Backbone%20-%20ITNOG10.pdf)

Denis Corradini

- **Why**: A migration story with the packet-loss count right in the title — the most transferable kind of operator talk: how to move a live backbone to SR-MPLS while (nearly) not dropping traffic.
- **What**: Migration of an operator backbone to SR-MPLS, with impact quantified by ping loss during cutover. *(title only)*
- **How**: Expect an SR-MPLS underlay with TI-LFA fast reroute and a phased cutover; the durable value is the cutover method and the measured loss, not the product choice.
- **Where applicable**: Any MPLS-capable backbone — a broadly applicable migration pattern, not org-specific.

### Transforming BGP operations to serve the best prefix out of 26 million

**Links:** [Slides](https://www.itnog.it/files/1-5_Transforming%20BGP%20Operations.pdf)

Alessandro D'Eliseo, Antonio Prado

- **Why**: BGP operations at 26-million-prefix scale is the extreme end of BGP tooling and datapath internals — exactly what the PM tracks in software networking.
- **What**: How BGP operations were reworked to select and serve the "best" prefix out of a 26-million-prefix table. *(title only)*
- **How**: Unknown; at that scale this is necessarily automation and policy engineering around massive tables — the deck has the architecture.
- **Where applicable**: The 26M figure signals a very large content/anycast or transit platform, so the scale is org-specific; the tooling and automation patterns partially transfer.

### Splitting ottico passivo per ridundanza link

Mirko Mosca

- **Why**: A physical-optics technique for link redundancy using passive splitters — cheap, unpowered redundancy directly in the PM's optics/cabling territory, and the kind of low-tech trick high-end roadmaps overlook.
- **What**: Using passive optical splitting to provide link redundancy. *(title only)*
- **How**: Presumably a splitter feeds two paths/receivers so a failure on one path does not drop the link; the design constraint to check is the splitter's insertion loss (roughly 3 dB per branch) eating into the loss budget.
- **Where applicable**: Short-reach/DCI links and cost- or power-constrained sites; loss-budget math limits reach, so it does not scale to long spans without amplification.

## Adjacent

### Building the longest SR-TE lsp in the world

**Links:** [Slides](https://www.itnog.it/files/1-12_longesttunnel-itnog_26_um_2.pdf)

Umberto M

- **Why**: A boundary-pushing SR-TE experiment — useful mainly for understanding SR datapath scaling limits (SID-stack depth, MTU, resilience) even if you never build one.
- **What**: Construction of a claimed record-length SR-TE LSP. *(title only)*
- **How**: Presumably an intercontinental path stitched across cooperating networks; the engineering constraints hit along the way are the transferable content.
- **Where applicable**: Depends on participating ASes; the limits discovered are general to SR-TE deployments.

### OTN oltre il trasporto: reti programmabili, latenze garantite e architetture quantum-safe

OPNET — vendor session (OPNET listed as the speaker)

- **Why**: Signals where optical transport is heading: programmable OTN, guaranteed-latency services, and post-quantum crypto in transport — the last item touching the PM's security interest.
- **What**: A vendor vision for OTN "beyond transport": programmability, latency guarantees, and quantum-safe architectures. *(title only)*
- **How**: Unknown; expect a roadmap rather than operator practice.
- **Where applicable**: Treat as a directional market signal with a pitch component, not an adoptable technique.

### Open Lab: A collaborative multi-vendor platform for experimentation and validation of next-generation networking technologies

**Links:** [Slides](https://www.itnog.it/files/1-18_A%20collaborative%20multi-vendor%20platform%20for%20experimentation%20and%20validation%20of%20next-generation%20networking%20technologies.pdf)

Flavio Luciani

- **Why**: A community-run, multi-vendor validation lab is infrastructure other operators can actually use — pre-production validation is a persistent gap, and shared labs are one of the few real answers.
- **What**: A collaborative platform for experimenting with and validating next-generation networking technologies across vendors. *(title only)*
- **How**: Multi-vendor lab environment; the access/participation model is presumably described in the deck.
- **Where applicable**: Broadly adoptable by operators; community-run, so watch for Italy/EU scoping.

### AS/IXP Traffic Observability / Osservabilità del traffico AS/IXP

**Links:** [Slides](https://www.itnog.it/files/2-13_trafficobservabilityITNOG_0426_FINALE.pdf)

Luca Deri, Federico Santulli

- **Why**: Traffic observability at AS and IXP scope — tooling others can adopt, feeding capacity planning, peering decisions, and abuse/anomaly detection.
- **What**: Approaches and tools for observing traffic at AS and IXP level. *(title only)*
- **How**: Unknown; expect flow-based analysis and open tooling in the deck.
- **Where applicable**: Any AS or IXP operator; broadly applicable.

### Semplificare l'automazione multi-vendor: Client RESTCONF auto-generati dai moduli YANG

**Links:** [Slides](https://www.itnog.it/files/2-14_Matteo%20Colantonio%20semplificare%20automazione%20multivendor%20ITNOG10.pdf)

Matteo Colantonio

- **Why**: Auto-generating RESTCONF clients from YANG models is a concrete, adoptable automation technique that attacks multi-vendor fragmentation at its root — exactly the kind of tooling others can pick up.
- **What**: A pipeline that generates RESTCONF client code from YANG modules, simplifying multi-vendor automation. *(title only)*
- **How**: YANG modules parsed into generated, typed client APIs per device/vendor, abstracting RESTCONF differences behind generated drivers.
- **Where applicable**: Any environment with YANG/RESTCONF-capable devices; vendor-neutral by construction, so broadly applicable.

## Wildcard

### Antares: Multi-Agent AI for Automated Network Analysis and Troubleshooting in GARR Data Centers

**Links:** [Slides](https://www.itnog.it/files/2-12_Antares-ITNOG10.pdf)

Francesco Lombardo — GARR (Italian research and education network)

- **Why**: Agentic AI performing diagnosis on production datacenter networks is an emerging subfield — and it raises exactly the authorization and trust questions around autonomous agents acting on infrastructure that the PM's identity and security work cares about.
- **What**: Antares, a multi-agent AI system for automated network analysis and troubleshooting in GARR data centers. *(title only)*
- **How**: Presumably cooperating specialized agents (telemetry collection, hypothesis generation, remediation); the deck has the actual architecture and scope.
- **Where applicable**: R&E-network DCs today; the multi-agent ops pattern generalizes, and the guard-railing questions (what may an agent do, unattended, to a production fabric?) apply anywhere.

### Measuring the public Internet

**Links:** [Slides](https://www.itnog.it/files/2-15_APNIC%20ITNOG%2010.pdf)

João Damas — APNIC (per slides filename)

- **Why**: Not a technical advance, but the measurement infrastructure behind most public claims about Internet health, routing, and deployment — knowing how those numbers are produced (and where they're blind) is quietly valuable to anyone reasoning about the public Internet.
- **What**: How the public Internet is measured at global scale. *(title only)*
- **How**: Unknown; expect measurement methodology and data platforms rather than a deployable technique.
- **Where applicable**: General context; no environment-specific constraints.

*Not selected: sponsor/community slots (HaliveOS, IXP updates, ITNOG updates, PeeringDB news), 101-level sessions (Improve IPv6 Peering), and off-domain talks (telephony KPIs/fraud analytics, telco edge computing local break, HERABIT interprovider VPN, the NAF automation map, and the "Reimagining Networking in the Age of AI" keynote, which looked like a perspective talk rather than a technical one). NAF and HERABIT were the closest near-misses if you want one more automation-framework and one more inter-AS service case study.*

## Themes

- **Optics is the center of gravity at this operator event**: hollow-core fiber, 400G ZR+ IPoDWDM in production, passive optical splitting for redundancy, and programmable/quantum-safe OTN — even a small operator conference is dominated by the physical layer this cycle.
- **Segment routing as the universal dataplane**: an SR-MPLS backbone migration, a record-length SR-TE LSP, and SRv6 uSID in the datacenter — SR now spans WAN transport and AI-fabric design in the same program.
- **AI appears on both sides of the network**: AI backends drive deterministic fabric design (SRv6 uSID), while AI enters operations as multi-agent troubleshooting (Antares) and as a theme reshaping the engineer's role.
- **The overlay abstraction has escaped the datacenter**: EVPN/VXLAN with Group-Based Policy for security, and national L2 wholesale FWA over VXLAN — DC overlay tech is now the substrate for telco wholesale services too.
- **Automation is consolidating around standards and shared infrastructure**: YANG-generated RESTCONF clients, the NAF framework, and a community multi-vendor Open Lab — moving from per-box scripts toward generated code and collective validation.
- **Hybrid multi-cloud BGP is table stakes**: an operator-context talk on resilient, symmetric on-prem-to-cloud underlays signals that multi-cloud connectivity is now routine operator work, not enterprise-only.
