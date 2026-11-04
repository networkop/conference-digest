<!--
conference: Capacity Europe 2026
type: vendor
source_url: https://www.capacityeurope.com/agenda/
generated: 2026-11-02
registry_key: capacity-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Capacity Europe 2026 — Digest

A note on this program: Capacity Europe is a wholesale-carrier and digital-infrastructure market event, not a technical conference. There are no papers or engineering deep-dives; the substance is in executive panels, market-data presentations, and a few vendor sessions. The picks below are the items with genuine technical or strategic content for someone whose core work is physical DC/WAN networking, network security, and identity — and the digest flags where a session is likely a product pitch or a pure boardroom discussion. All `page:` links returned 404 when fetched (the agenda pages are no longer live), so **every write-up below is from the abstract only**.

## Core

### Presentation: Data Center Interconnect for the AI Era: Enabling Distributed AI Infrastructure

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-pays-europes-digital-ambition-policys-real-price-tag)

Nino Shaptoshvili, VP of Sales - PacketLight Networks Ltd

- **Why**: DCI is squarely in the PM's core territory — optical transport between data centres is becoming the fabric that binds distributed GPU clusters into one AI system. This is the one session in the program that directly addresses the DC/WAN interconnect problem for AI workloads.
- **What**: An argument that as AI infrastructure spreads across multiple sites, the network (not the compute) becomes the gating factor, and that high-performance DCI is what turns scattered GPU clusters, storage, and compute into a "unified AI fabric" (from abstract only).
- **How**: Optical transport delivering high bandwidth, deterministic low latency, and security for moving large datasets and synchronising AI workloads across sites — i.e. the classic coherent-optics DCI playbook applied to training/inference traffic patterns.
- **Where applicable**: Multi-site AI clusters, campus-scale and metro/regional DCI. Caveat: the speaker is a VP of Sales at a DCI vendor (PacketLight), so expect a product-adjacent framing rather than an operator case study; no scale, latency, or cost figures are published. Treat as a vendor's view of the problem, useful for the requirements it articulates (deterministic latency, bulk dataset movement) rather than for evidence.

### Panel: Beyond Copper: Fibre, Hollow Core & What's Next

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-switch-done-right-lessons-europes-front-runners)

Christoph Glingener (CEO, ADTRAN), Danny Preston (Co-founder & CEO, Network Planning Solutions), Jussi Tolvanen (CEO, DNA), Colin Bannon (CTO BT Business, BT), Lee Myall (CEO, Neos Networks), Daniel Rowan (Independent)

- **Why**: Hollow-core fibre is the most consequential optical-physical-layer development on the horizon for anyone working DC interconnects — ultra-low latency and nonlinearity advantages that matter for sync-sensitive workloads (including distributed training). This is the only session at the event engaging with it.
- **What**: A panel on what European operators invest in next as copper is retired: fibre expansion, migration strategy, and next-generation physical media including hollow-core fibre and advanced optical networks (from abstract only).
- **How**: Not a single technique — a strategy discussion spanning copper-switch-off migration economics, fibre modernisation, and emerging fibre types. Expect the hollow-core discussion to be at the roadmap/adoption level, not waveguide physics.
- **Where applicable**: Broadly applicable to European access and core networks; the PM's interest is specifically in whether hollow core reaches DCI and long-haul routes. Panel composition (mostly CEOs/CTOs of operators and vendors) signals strategy, not implementation detail.

### Keynote Panel: Wiring the AI Boom: Building Fibre Corridors for Training, Inference and Scale

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/keynote-panel-wiring-ai-boom-building-fibre-corridors-training-inference-scale)

Nicholas Collins (O2 Business Holdings), Marisa Trisolino (eUnity/EUNEtWORKS), Jim Fagan (EXA Infrastructure UK), Jorge Alvarez (Retelit Digital Services), Jeff Hulse (Verizon), Amjad Arab (Salam)

- **Why**: The physical-build side of AI: which corridors get fibre, how fast, and on what commercial terms. For a PM whose core work includes DC/WAN interconnect and fibre capacity planning, this is where the supply-side decisions are being described.
- **What**: How AI is reshaping fibre demand across training hubs, inference, and edge — and how operators respond with fast-track corridor builds, dark-fibre strategies, investment choices, and network design, including early customer engagement (from abstract only).
- **How**: Panel discussion covering build strategy and commercial models (dark fibre vs lit service, pre-commitments from AI customers) rather than engineering.
- **Where applicable**: European long-haul and inter-DC corridors. The training-vs-inference geography split it implies (training in power-rich hubs, inference near users) is broadly applicable to European capacity planning, though specifics will be operator-specific.

### Presentation: Boom or Bottleneck? An Update on Global Subsea Connectivity

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-subsea-bottleneck-europes-cables-cap-ai-boom-) · [Recording](https://www.youtube.com/watch?v=GOOoLs5gDlA)

Stacey Parker, Research Analyst - TeleGeography

- **Why**: TeleGeography is the one source in this program that brings actual data — bandwidth deployment, pricing, and supply/demand by route — rather than opinion. For anyone whose WAN planning depends on transatlantic/Mediterranean capacity economics, this is the highest signal-density session listed.
- **What**: A data-driven counterpoint to "capacity squeeze" headlines: unprecedented investment is driving massive network growth and route diversity, and the session gives a realistic supply/demand and pricing outlook for Europe, including current constraints (from abstract only).
- **How**: Market analysis built on TeleGeography's bandwidth, infrastructure, and pricing datasets — deployment pipelines, route diversity metrics, and price trends.
- **Where applicable**: Global subsea capacity planning with a European focus; broadly applicable, not org-specific. No figures are in the abstract, but this format reliably delivers real numbers on stage.

### Panel: The New Rules of Network Design

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-new-rules-network-design)

Rajesh Sennik (Roland Berger), Vilas Thawale (Tata Communications, Subsea Networks), Tony O'Sullivan (RETN), John Fitzgibbon (AWS), Younès Stouky (Orange Wholesale)

- **Why**: This addresses a real shift in the PM's core domain: network topology and interconnect decisions increasingly driven by security mandates, sovereignty, and geopolitical risk rather than pure efficiency. The panellist mix (AWS network planning + Tata subsea + Orange wholesale + RETN) spans both sides of that tension.
- **What**: How security, resilience, and sovereignty requirements are changing where networks are routed, where facilities are located, and how networks interconnect — and the cost/trade-off consequences across fibre, datacentres, and subsea (from abstract only).
- **Why it matters / What it implies for design**: routing and peering decisions now carry a threat model, not just a latency model — directly relevant to network-security-informed design.
- **Where applicable**: European and global carrier networks; the sovereignty constraints discussed are EU-specific, the routing/resilience logic is general. Executive-level discussion; expect direction, not design methodology.

### Panel 2: Fibre, Routes & the Fragility of Global Connectivity

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-2-fibre-routes-fragility-global-connectivity)

Marc Halbfinger (Red HMH), Steve Roberts (EXA Infrastructure), Andy Palmer-Felgate (Submarine Cable Engineer, Meta), Paul Gabla (Alcatel Submarine Networks)

- **Why**: Route diversity has become a first-class design constraint in WAN/DC interconnect, and this panel includes both a hyperscaler's cable engineer (Meta) and a subsea vendor — the closest this program gets to people who actually design cable systems.
- **What**: How the industry builds resilient fibre and subsea networks — route diversity as a strategic imperative driven by AI adoption, cloud growth, and digital sovereignty (from abstract only).
- **How**: Discussion-level: route-diversification practice, "resilience by design" principles, and how sovereignty moves change route economics.
- **Where applicable**: Subsea and long-haul route planning globally with a European lens. Meta's presence suggests a hyperscaler buyer's perspective on route diversity, which is the most transferable content for DC/WAN interconnect planning.

### Panel: From Best Practice to Critical Infrastructure: Rethinking Fibre Resilience

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-best-practice-critical-infrastructure-rethinking-fibre-resilience)

Felix Seda (NJFX), Gilles Calligaro (Arteria), Tom Ronan (Senior Director, Fiber Systems, VIAVI), Salman Alomiri (Mobily), Dave Ferry (ITS)

- **Why**: Network resilience engineering with an actual measurement/monitoring angle — VIAVI's Tom Ronan is the one panellist across the program likely to discuss fibre monitoring, OTDR-based visibility, and fault localisation rather than pure commercial resilience.
- **What**: How operators strengthen reliability, improve visibility across their networks, and minimise disruption as resilience becomes a competitive differentiator for business customers (from abstract only).
- **How**: Panel discussion spanning monitoring/visibility tooling, restoration practice, and commercial framing of resilience.
- **Where applicable**: Carrier fibre networks broadly; NJFX's cable-landing-exchange model is US-specific but the monitoring and visibility discussion is general. No metrics published; the abstract is thin, so value depends heavily on the VIAVI contribution.

## Adjacent

### Opening Keynote: Protecting Critical Infrastructure in an Era of Hybrid Threats

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-resilience-imperative)

Laurie Walker, Team Lead, Critical Undersea Infrastructure Coordination Cell - NATO

- **Why**: Network security at the geopolitical layer: this is the NATO cell specifically stood up after the Baltic Sea cable incidents, and it is shaping the government expectations that will land on network operators as security requirements.
- **What**: The evolving threat landscape for critical networks (hybrid threats combining cyber, physical, and climate exposure), the Alliance's role in infrastructure protection, and required actions from governments and industry (from abstract only).
- **How**: Policy/strategy keynote, not technical; expect attribution-free threat framing and resilience doctrine.
- **Where applicable**: European critical-infrastructure operators, subsea and backbone networks. Adjacent rather than core because it sets requirements rather than techniques — but it is a useful leading indicator of coming mandates.

### Panel: Chokepoints & Shockwaves: Protecting the Cables Europe Can't Lose

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-chokepoints-shockwaves-protecting-cables-europe-t-lose)

Martin Prins (Dutch Subsea Cable Coalition), Ugne Kleinauskaite (Meta), Martin Dowling (CTO, Midgard Infra), Andy Bax (EXA Infrastructure)

- **Why**: A complement to Panel 2 above: the protection and partnership side of subsea resilience, including hyperscaler-driven reshaping of cable ownership. A second Meta speaker at the event signals how much of Europe's subsea build is now hyperscaler-financed.
- **What**: How hyperscaler investment and global crises are reshaping Europe's subsea connectivity, exposing fragilities, and how diversified routes, new partnership models, and sovereignty moves can protect capacity (from abstract only).
- **How**: Panel discussion — chokepoint analysis, route diversification, cable-partnership models.
- **Where applicable**: European subsea capacity and cable-partnership structures; policy-tinged but with operator participants.

### Opening Keynote Panel: Beyond Silos: Building Europe's Converged Digital Infrastructure

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/opening-keynote-panel-beyond-silos-building-europes-converged-digital-infrastructure)

Joe Scattareggia (Colt), Paula Cogan (Digital Realty), Brenden Rawle (Equinix), Michael Wheeler (NTT Data), Twinkle Singh (Google), Anna Klaft (KLF Management)

- **Why**: Market structure, but structure that directly affects DC interconnect product decisions: colocation, carriers, and IXPs converging into joint builds and shared models. Useful context for anyone whose DC fabric work depends on carrier/colo/IX interfaces.
- **What**: A first-of-its-kind stage sharing between Europe's colocation providers, carriers, and internet exchanges, debating joint ventures, shared models, network convergence, and revenue models across the stack (from abstract only).
- **How**: Executive debate; expect announcement-adjacent content on colo-carrier partnerships.
- **Where applicable**: European colo/carrier/IX market; strategic rather than technical.

### Presentation: The Automation Gap: Why Networks Outpace the Organisations Running Them

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-automation-gap-networks-outpace-organisations-running)

Frank McDermott, CEO & Co-Founder - CARMA

- **Why**: The automation/digital-twin theme is adjacent to the PM's cloud-native networking world, and the framing here is honest about a real failure mode — visibility without control. Caution: CEO of a digital-twin vendor, so treat as a product-adjacent pitch.
- **What**: The claim that networks are increasingly intelligent but organisations struggle to convert visibility into control, and that digital twins and operational data can drive automation, faster scaling decisions, and cost reduction (from abstract only).
- **How**: Digital-twin and operational-data approaches to moving from monitoring to automated action.
- **Where applicable**: Carrier network operations broadly; no metrics or case evidence in the abstract, so apply the standard skepticism to "we adopted digital twins and it was great" claims until numbers appear.

### Panel: From FLAP to Frontier: Rethinking Europe's footprint for AI

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-flap-frontier-rethinking-europes-footprint-ai)

Dawn Childs (nLighten), Ivo Ivanov (DE-CIX), Amar Khan (Meta), Falk Weinreich (Portus Data Centers), Giancarlo Giacomello (Aruba)

- **Why**: Where AI compute physically sits — the latency/power/sovereignty trade-off that determines future DC fabric demand. The IXP perspective (DE-CIX) on traffic redistribution is directly relevant to interconnect planning.
- **What**: Europe's DC landscape is decentralising beyond the FLAP-DASH metros; the panel covers emerging AI hubs, edge growth, and how policy, sovereignty, and latency shape siting decisions (from abstract only).
- **How**: Panel discussion on siting drivers — power price vs latency, sovereignty requirements, inference-at-edge economics.
- **Where applicable**: European DC market planning; directional rather than quantitative.

### Presentation: The Deployment Gap: What's Holding Fibre Back?

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/presentation-networks-built-profits-missing)

Andrew Black, Technical Director - Fujikura Europe Ltd

- **Why**: The only speaker in the program from an actual fibre/cable component manufacturer in a technical-director role — likely the closest thing to a physical-layer talk on offer. The topic is deployment friction (cost, labour, modernisation) rather than DC-specific fibre, but the constraints discussed shape every build the PM touches.
- **What**: As operators move from rollout plans to large-scale delivery, the emerging problems are cost, complexity, labour availability, and network modernisation; the talk covers practical deployment realities and lessons across European markets (from abstract only).
- **How**: Practitioner overview of deployment practice — likely splicing/cabling logistics, labour scaling, and modernisation trade-offs, given the speaker's background.
- **Where applicable**: European fibre deployment generally; the abstract does not specify DC or long-haul focus, so applicability to DC-specific cabling is uncertain.

## Wildcard

### Presentation: New control points, new telco value in an AI world

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-presentation)

Amy Cameron, MD, Research - STL Partners

- **Why**: Not about the PM's core domains, but it names a thesis worth stress-testing: that AI agents — not APIs — are the real catalysts that will make NaaS work, and that new control points (observability data, voice records, network sensing) become monetisable assets. That is a direct early signal for anyone tracking how automation and agentic systems reshape network service interfaces.
- **What**: Analysis of how AI agents change customer relationships, what the true catalysts of NaaS adoption are, and which new network control points (observability, voice records, sensing) can be captured (from abstract only).
- **How**: Analyst framework discussion, not a technical mechanism.
- **Where applicable**: Telco/wholesale product strategy broadly; the "AI agents as the NaaS demand signal" claim is the transferable idea.

### GrowthX Dragons Den Pitch 5

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/growthx-dragons-den-pitch-5)

Inthujan Rasalingam, CEO & Co-Founder - Capacity Connect

- **Why**: A concrete early specimen of agentic transaction infrastructure: AI agents turning a buyer requirement into an RFP, matching to verified operators, drafting proposals, and running capacity deals to close. The PM tracks agentic identity and workload identity — this is where that pattern shows up in the wholesale world, including the obvious unsolved question of how agents authenticate to counterparties.
- **What**: A five-minute startup pitch: "agentic transaction infrastructure for data center capacity," compressing the manual DC capacity procurement process into an agent-driven pipeline (from abstract only).
- **How**: One buyer requirement → auto-generated RFP → matching against a verified operator database → agent-drafted proposals → deal execution.
- **Where applicable**: Datacenter capacity marketplace transactions; early-stage startup pitch, so no evidence of traction — the value is as a signal of agent-mediated B2B commerce arriving in infrastructure procurement.

### Panel: Reclaiming the voice opportunity with voice AI

**Links:** [Abstract](https://www.capacityeurope.com/agenda/capacity-europe-2026/panel-reclaiming-voice-opportunity-voice-ai)

Isabelle Paradis (Hot Telecom), Burak Enseren (Telnyx), Yogesh Lulla, John Kennedy (Enea), Guillaume Klein (iBasis)

- **Why**: Outside the PM's core, but it is the only session at the event touching identity as a monetisation and security axis in real traffic: how operators integrate identity signals into voice services while AI-driven fraud accelerates. Fraud is becoming the forcing function for stronger caller/user identity in carrier networks.
- **What**: Voice as an AI-driven, high-value service alongside accelerating voice fraud; the panel covers integrating identity, analytics, and CX data to monetise voice beyond minutes while protecting customers (from abstract only).
- **How**: Panel discussion on identity and analytics integration in voice/messaging services.
- **Where applicable**: Carrier voice and messaging businesses; the identity-technology specifics are not stated, so treat as directional.

## Themes

- **AI is the new traffic engine, and it is being wired for**: nearly every Core Infrastructure session frames capacity decisions (fibre corridors, subsea, DCI) around training hubs vs inference-at-edge geography — the training/inference split is now the standard analytical lens for physical build planning.
- **Resilience and route diversity have moved from afterthought to design constraint**: multiple sessions (Panel 2, Chokepoints, Rethinking Fibre Resilience, the NATO keynote) treat physical route fragility, chokepoints, and hybrid threats as first-order inputs to network design, driven by real cable incidents and geopolitics.
- **Sovereignty and security now dictate topology**: "The End of Neutral Infrastructure" framing and "The New Rules of Network Design" capture a genuine shift — routing, siting, and interconnect choices increasingly follow trust and jurisdiction, not just efficiency, with real cost consequences.
- **Carrier/colo/IX/hyperscaler convergence**: the Beyond Silos panel, hyperscaler speakers at Meta appearing across three subsea/DC sessions, and the neocloud-carrier case study all point to blurring value-chain roles in who builds and who pays for interconnect.
- **Automation remains an organisational gap, not a technology gap**: the Automation Gap and Legacy-vs-Scale sessions repeat a familiar theme — visibility exists, control doesn't — with NaaS still unresolved; the STL wildcard adds the twist that agentic AI may finally be the demand-side catalyst.
- **Notable absence for this PM**: there is essentially no cloud-native networking (no eBPF/Cilium/Kubernetes content), no workload identity (SPIFFE/SPIRE, passkeys), and no switching/optics internals at this event — Capacity Europe is a market and infrastructure conference, so the value here is supply-side context for DC/WAN capacity, not datapath depth; those interests are better served elsewhere this cycle.
