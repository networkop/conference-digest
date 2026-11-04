<!--
conference: LACNIC 45
type: operator
source_url: https://lacnic45.lacnic.net/
generated: 2026-11-03
registry_key: lacnic-45
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# LACNIC 45 — Digest

LACNIC 45 is a regional operator meeting: the technical weight this cycle sits in BGP measurement and routing security, DWDM/optical transport, GPU-fabric-driven peering economics, and adoptable open-source automation. Identity, cloud-native networking, and Kubernetes topics are essentially absent from the program — the closest adjacent signals are RPKI operational practice (a PKI in production at regional scale) and an agentic-AI-for-ops talk, both covered below. Physical/WAN work is present and taken seriously, per the picks in Core.

## Core

### Channelmania! Secure the Future of your DWDM Network Topology Remaining Flexible to 1.6T Technology

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/flexoptix-brainfuck-lacnic45.pdf) · [Recording](https://youtu.be/Ioy-GKR0NpE)

Gerhard Stein (Flexoptix; slides also credit Thomas Weible and Gert Matyasowicz, Flexoptix)

- **Why**: Physical optics and WAN transport are core to this PM, and this is the program's one deep-dive into coherent optics physics and DWDM topology planning for the 800G/1.6T era. Caveat: it is vendor-presented (Flexoptix), but the slides are engineering-heavy — constellation math, receiver architectures, spectrum planning — not a product pitch.
- **What**: A technical walkthrough of why coherent transceivers only recently became feasible, and how to design DWDM topologies that stay flexible as line rates scale. Covers on-off-keying's limits, higher-order modulation (16-constellation/4-bit patterns over two orthogonal polarizations, 425 Gbps at 53.125 GBd), and coherent receiver design (balanced/asymmetric detection, phase and polarization diversity, homo-/hetero-/intradyn detection).
- **How**: The core prescription is to stop planning in wavelengths (nm, channel numbers) and plan in spectrum (THz/GHz): contrast 96 × 50 GHz C-band channels (~2 dB insertion loss) with 12 × 400 GHz sub-bands; the authors show a DIY superchannel using cheap PLC splitters and ordinary 50 GHz DWDM mux/demux with coherent RX, and note 800G coherent ZR+ OSFP pluggables shipping today with XPO (up to 12.6T, liquid-cooled) arriving.
- **Where applicable**: Any operator or DC interconnect planning C-band capacity upgrades and topology flexibility toward 1.6T. The spectrum-planning argument is broadly applicable; the framing leans toward Flexoptix's programmable-transceiver business, so vendor-fit should be discounted.

### EVPN & VXLAN: The New Language of Modern Peering

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/weher-202605261225-peering_moderno-vxlan_evpn.pdf) · [Recording](https://youtu.be/mrgn6HbzmmY)

Ariel Weher (no affiliation listed in the program)

- **Why**: EVPN/VXLAN is the control plane / data plane pair at the center of modern DC fabric design, and applying it to peering and interconnection fabric is exactly where exchange and edge fabrics are heading — squarely a core interest of this PM.
- **What**: No description was published for this session — title, speaker, and materials only — so this write-up is limited to what the title indicates: using EVPN as the control plane and VXLAN as the overlay for modern peering/interconnection fabrics, in place of legacy VLAN-based designs. The same speaker runs a companion hands-on **VxLAN Configuration Lab** at the same meeting (recording available), which signals the talk is practical and configuration-level rather than conceptual.
- **How**: Cannot be characterized further without the slides; the PM should review the deck and lab recording directly (links are attached below each heading by the pipeline).
- **Where applicable**: IXP/peering-fabric operators and DC interconnect designs. Flagged as title-and-materials-only; no claims here go beyond the session's own title.

### Impacts of LLM Traffic on Peering Strategies

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/llm-traffic-implications-for-peering-strategy.pdf) · [Recording](https://youtu.be/kSSug2XqAxc)

Tomás Lynch (AS20473 — presents from his own network's experience)

- **Why**: GPU/LLM clusters create a new traffic-profile class that changes both DC fabric architecture and external interconnect economics — directly relevant to the PM's DC fabric and DC/WAN interconnect work, and a rare first-person operator account rather than a projection.
- **What**: How LLM traffic actually lands on a network. GPU clusters are built as two fabrics: a converged frontend leaf-spine (north-south inference and dataset-ingestion traffic, usually oversubscribed, 100GE/400GE at the edge) and a non-blocking backend leaf-spine (east-west training only), plus high-performance storage. The two LLM traffic classes behave oppositely: inference is low-volume, constant, bidirectional, geographically dispersed ("looks like traditional traffic" → latency-driven peering via IXPs and PNIs); dataset ingestion is massive, bursty, mostly inbound, concentrated — and it drives the 95th-percentile transit bill (→ cost-driven strategy: rate-limit/schedule ingestion with customers, raise minimum commitments, add/rebalance transit, direct connects to GPU customers). GPU frontend traffic itself breaks the classic compute sinusoid: spiky outbound vs near-constant inbound.
- **How**: 24-hour traffic-graph comparisons of GPU vs traditional compute frontend patterns from the presenter's own network, then derived peering tactics per traffic class. Side observations: ingestion bursts can trip DDoS-detection thresholds (validate them), and mixed flow sizes make congestion management critical.
- **Where applicable**: Operators serving GPU/AI customers and DC providers designing frontend/backend fabric separation. The traffic-profile taxonomy generalizes; the numbers are one operator's network, so scale-dependence should be assumed.

### Towards detecting DoS attacks in the server's NIC

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/lara-botero-lacnic45-v3.pdf) · [Recording](https://youtu.be/hQe2kLWE_Ew)

Adrián Lara (Universidad de Costa Rica), Juan Felipe Botero (Universidad de Antioquia)

- **Why**: Sits at the intersection of two of the PM's core interests — network security and datapath internals — by moving DoS detection off CPUs and IDS appliances into the server's NIC dataplane, with an eBPF/XDP variant that is broadly deployable.
- **What**: Research on embedding ML-based DoS detection in SmartNICs to eliminate the two classic IDS deployment problems: traffic duplication (mirroring) and bottlenecks. Measured results on a Netronome SmartNIC show the ML model adds only a slight shift to the detection-delay distribution with low dispersion — inference at line rate with near-negligible overhead. A companion case applies the same idea with XDP + eBPF and model quantization (16/8/4/2-bit): all quantized models show median inference latency around 0.2 μs.
- **How**: Strict role split — the CPU/control plane manages global policy, model updates and exceptions; the SmartNIC dataplane does per-packet feature extraction, filtering and inference. Simple models (decision trees) are compiled into P4 match-action tables (each branch becomes a table entry over feature ranges); quantization fits models into NIC memory; the NIC exports features so the CPU can (re)train. Malicious traffic is dropped before it reaches the OS.
- **Where applicable**: Host-granularity DoS defense and edge microsegmentation. The P4 path requires programmable SmartNICs (demonstrated on Netronome); the eBPF/XDP variant runs on ordinary Linux hosts. Research-stage, but the architecture and quantization findings transfer directly.

### Automation and Telemetry applied to BGP Routing Policies

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/automatizacion-y-telemetria-aplicada-a-politicas-de-enrutamiento-bgp.pdf) · [Recording](https://youtu.be/FA_p-IipxqM)

Henri Alves de Godoy (Universidade Estadual de Campinas), Ernesto Sánchez (Universidad Católica de Salta); slides also credit William Sánchez (Celsia Internet, Colombia)

- **Why**: A concrete, fully reproducible open-source stack for BGP policy automation plus link-quality-driven failover — exactly the adoptable tooling an operator program should surface, and squarely in the PM's BGP-internals/automation interest. The topology is even published on GitHub.
- **What**: A Containerlab-replicated model of Colombian ISP Celsia's BGP infrastructure with automated failover: link quality to each provider is scored every 30 seconds from MTR measurements (latency, jitter, loss); thresholds trigger automatic BGP policy updates (AS-path prepend / local preference) through the NetBox API — no manual intervention, full change traceability via version control, Grafana dashboards. Reported results: complete deployment in the test environment, reduced failover time, elimination of manual configuration, and an open, multi-vendor, auditable pipeline.
- **How**: NetBox as single source of truth (netbox-bgp plugin; custom fields for local ASN, prepend count, local preference) → webhook fires a GitLab CI/CD pipeline → Nornir (Netmiko over SSHv2) renders and pushes config to multi-vendor nodes (Huawei VRP core, Nokia SR Linux providers, Cisco IOL switch) → MTR JSON output lands in Elasticsearch → Grafana visualizes and alerts. Scoring: weighted latency (direct-to-peer 70% / public-DNS hop-by-hop 30%) plus penalties for loss and jitter, with configurable warning/critical thresholds (e.g., peer latency 12/25 ms, loss 0%/20%, 3-point change margin).
- **Where applicable**: Any multi-provider ISP or enterprise WAN; the entire stack is open source and the lab topology is on GitHub, so it is directly adoptable. Constraints: validated in Containerlab against Celsia's design, not yet a production-at-scale report, and the failover logic assumes broadly comparable service quality between providers.

### Case Study: Route Hijacking, RPKI, and Social Engineering

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/secuestros-de-rutas-en-bgp-el-extrano-caso-del-pdf-falso-lacnic45.pdf) · [Recording](https://youtu.be/jDwbvmqJZpY)

Carlos Martínez (LACNIC), Guillermo Cicileo (LACNIC)

- **Why**: A fully investigated postmortem of a deliberate BGP hijack against an RIR itself, combining routing security with social engineering of the transit-provisioning trust chain. Concrete postmortems with real attribution are exactly what this operator program should up-rank.
- **What**: In July 2025, LACNIC's AS28001 and its São Paulo prefixes were hijacked intermittently in three windows (20, 15, and 5 minutes across July 9–12), degrading access to LACNIC's services from the rest of the Internet. The attacker — an Indonesian AS (142395) — impersonated both LACNIC's prefixes *and* its ASN, which is why RPKI/ROA origin validation did not help: the forged announcements carried the authorized origin AS. The enabling mechanism was a forged Letter of Authorization (a fake PDF with a scanned signature) accepted by an international transit provider; the Indonesian ISP involved was itself partly a victim. Resolution ran through APNIC's security team and APJII in Indonesia.
- **How**: Interactive walkthrough of how peering/transit agreements are verified in practice today — LoAs checked against WHOIS/IRR, which the deck describes as "as precarious as it looks" — why prefix+ASN impersonation cannot be accidental (vs. common accidental prefix mis-origination), the cross-RIR coordination path, and why this attack class is precisely what ASPA is designed to catch.
- **Where applicable**: Every operator that accepts customer announcements on the basis of LoA documents — i.e., nearly all transit providers — and anyone treating RPKI ROV as sufficient protection. Broadly applicable; the defensive lesson (treat PDF authorization letters as untrusted; anchor verification in cryptographic objects) is universal.

### Hands-on ASPA: Configuration and Lessons Learned

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-aspa-fundamentos.pdf) · [Recording](https://youtu.be/jDwbvmqJZpY?si=AINliImhXzawKGQU&t=1347)

Carlos Martínez (LACNIC), Guillermo Cicileo (LACNIC)

- **Why**: ASPA is the next deployment wave in routing security — LACNIC's own member-assembly report lists ASPA object support as its 2026 RPKI roadmap item, and the NRO's 2026 RPKI program explicitly aims to deploy ASPA — and this hands-on session connects directly to the hijack case above.
- **What**: A fundamentals-plus-practice session on ASPA (Autonomous System Provider Authorization, IETF sidrops drafts): a new RPKI object in which an ASN cryptographically declares its authorized upstream providers (an AS0 ASPA declares "no providers," e.g., Tier-1s or route-server-only clients). It detects forged-AS-path/origin hijacks and mitigates global route-leak propagation, reusing the existing RPKI architecture (validators, repositories, rpki-rtr) without adding router-side cryptography.
- **How**: ASPA formalizes valley-free routing: for each adjacent AS pair in an AS_PATH, the validator checks the customer's attestation — P (declared provider), nP (AS exists in the attestation but this neighbor is not a provider → lateral/customer hop), nA (no attestation published) — enabling both upstream and downstream path verification.
- **Where applicable**: Any operator already running RPKI can adopt ASPA on the same infrastructure; benefits scale with ecosystem-wide adoption, which is still early (IETF draft stage). Pairs with the case study: RPKI origin validation alone would not have stopped the AS28001 impersonation; path verification is the missing half.

### Routing under siege: how traffic engineering decisions facilitate prefix hijackings

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/enrutamiento-bajo-presion-como-las-decisiones-de-ingenieria-de-trafico-facilitan-el-secuestro-de-prefijos-lacnic45.pdf) · [Recording](https://youtu.be/pRq5GjlLnUI)

Renan Paredes Barreto (Universidade Federal do Rio Grande — FURG; slides also credit Leandro Bertholdo and Pedro Marcos)

- **Why**: Controlled, real-Internet experiments that quantify how operators' own traffic engineering choices change hijack exposure — turning received wisdom ("prepends are harmless") into measured numbers with direct configuration implications.
- **What**: Using the PEERING testbed (real BGP announcements from five PoPs: Amsterdam, UFMG, Seoul, Johannesburg, and a Northeast-US site), the authors ran type-0 hijack experiments in controlled windows (Nov 2024–Feb 2025) against 127,421 responsive data-plane targets across 45,462 ASes, measuring both control-plane reach (RIS Live monitors) and data-plane impact (ping responses). Key results: increasing AS-path prepends by the victim increases hijack impact; ASes can be significantly impacted even without prepending; more-specific-prefix hijacks affect even well-connected ASes with fairly uniform impact; and impact varies materially by PoP/location.
- **How**: Victim and hijacker announce the same prefix from different PEERING sites; impact percentage = monitors/hosts selecting the hijacker's path vs. the victim's; each iteration varies TE technique (prepend count, prefix length, selective announcements), AS locations, and connectivity.
- **Where applicable**: Any operator using prepends or managing announcement granularity — the practical lesson (heavy prepending measurably increases sub-prefix hijack exposure) is broadly applicable. Constraints: IPv4 only, type-0 hijacks only, no ROAs created — findings are scenario-specific rather than universal.

## Adjacent

### Behind the Routes: Measuring BGP Instability on the Internet

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic-45-behind-the-routes-measuring-bgp-instability-on-the-internet.pdf) · [Recording](https://youtu.be/c51phXoslpM)

Milena Bueno Rocha (FURG, Brazil; slides co-authored with Pedro Marcos)

- **Why**: Systematic baseline data on how much BGP churn is real change versus noise — directly useful to anyone building BGP monitoring, anomaly detection, or dashboards, and a good calibration against "BGP is melting" narratives.
- **What**: Fifteen days (April 2026) of RIBs plus updates from RRC00 (Amsterdam) and RRC24 (Montevideo), filtered to full-table monitors, analyzed across Global / LACNIC / Panama scopes. Findings: over 60% of updates globally are effective routing changes (LACNIC-region announcements reach 81.7% — the highest of the three scopes); AS_PATH and COMMUNITIES dominate attribute changes (~95% of effective updates); over 96% of effective updates modify at most 2 attributes; MED and NEXT_HOP changes are negligible; and propagation is mostly local — 50% of IPv4 changes are seen by fewer than 10 monitors, while IPv6 changes propagate more widely (80% of changes reach ≤26 monitors).
- **How**: Updates classified as effective changes / redundant / withdrawals; per-update attribute diffs; propagation measured by counting how many full-table monitors observe the same per-prefix change within a 120-second window, aggregated into CDFs. Regional scoping uses LACNIC delegated files.
- **Where applicable**: BGP monitoring and anomaly-detection design generally; fully reproducible from public RIS/RouteViews data. The authors flag the open next question: who is causing the instability.

### The Internet ASN graph

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/el-grafo-de-los-asns-de-internet-lacnic45.pdf) · [Recording](https://youtu.be/EBa1wEFbnKs)

Claudio Risso (Universidad de la República, Uruguay), Carlos Martínez (LACNIC)

- **Why**: A framework for building structural models of the Internet's AS-level graph — relevant to the PM's BGP-internals interest for policy simulation (RPKI/ASPA/ROA scenarios), topology reasoning, and understanding measurement vantage-point bias.
- **What**: A methodology plus first results: reconstruct the AS-level graph from a full month of MRT data (24 RIPE RIS + 4 RouteViews collectors, April 2025). Raw graph: ~86,400 ASes / ~750,000 edges, 36.8% degree-1 leaves, mean degree 16.6 — Internet transit is only ~0.02% as dense as a full mesh. After reducing to the transit-only graph (84,497 nodes / 389,442 adjacencies) and homeomorphic reduction, the "backbone" is a 2-connected component of ~29,923 nodes, with dense cliques of 31 and 35 ASes (disconnecting one member of the 35-clique requires 34 simultaneous failures). The work also classifies node lifecycles (stable, born, dying, flapping, sporadic, reborn) and explicitly studies the probe-distribution problem: how many and which collectors are needed to reconstruct the topology.
- **How**: All ASPATHs from MRT full + update dumps parsed with BGPStream; each ASPATH hop becomes an edge; bogons and prepends discarded; then combinatorial-optimization analysis (biconnected components, articulation points, n-connectivity) to identify core structure.
- **Where applicable**: Routing-policy simulation, topology research, and data-informed peering/deployment decisions. Built from public collector data with the usual vantage-point bias; the probe-placement question is open, which itself matters for anyone consuming collector-derived "Internet views."

### What Is My RPKI Validator Doing Right Now?

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/que-estara-haciendo-mi-validador-rpki-en-este-momento-lacnic45.pdf) · [Recording](https://youtu.be/k263dzMIiI4)

Santiago Aggio (CONICET BB / UTN-FRBB, Argentina)

- **Why**: RPKI validators are quietly becoming production-critical infrastructure for anyone doing ROV — this gives a concrete measurement plus an ops playbook for running and monitoring them, which the PM can treat as a case study in operating a PKI at scale.
- **What**: An operator-oriented examination of relying-party software (FORT, Routinator 3000, rpki-client, StayRTR, rpki-prover) and the synchronization layer: RRDP (RFC 8182) vs rsync, where RRDP's snapshot/delta model substantially reduces data transferred per validation cycle (one publication point shows ~4,425 RRDP vs ~135 rsync fetches). Includes measured sync latencies from 20 RIPE Atlas probes in Argentina showing that the geographic location of publication points influences synchronization times, and notes 26 active IETF drafts in the RPKI space (publication-server BCP, ERIK sync protocol, decentralized repository architecture).
- **How**: Routinator's Prometheus exporter + Grafana for VRP and session metrics; validator metrics pages; RIPE Atlas ping/traceroute to publication points. Operational recommendations: size the validator VM (memory, tmpfs, CPU); run more than one validator implementation for redundancy; use different IPv4/IPv6 source addresses toward repositories (to survive DDoS filtering); run DNS resolvers with parallel resolution; monitor both sides of the validator (RRDP/rsync toward publication points, RTR toward routers); consider RTRTR as an RTR proxy for mid/large operators.
- **Where applicable**: Any operator running RPKI ROV — broadly applicable and immediately adoptable. The latency measurements are Argentina-specific; the practices are general.

### BGP ORIGIN in Practice: Inconsistencies Observed in LACNIC Prefixes

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/bgp-origin-v3-lacnic45.pdf) · [Recording](https://youtu.be/t4qf4JM5GGQ)

Celsa Sánchez (NIC Chile)

- **Why**: A surprising result about a "boring" attribute: ORIGIN no longer means what RFC 4271 says it means — operators deliberately rewrite it as a policy tool, which breaks any analytics, teaching material, or tooling that assumes documented semantics.
- **What**: Twelve months (2025) of RIBs from four RouteViews collectors (Chile, Mexico, Fortaleza, Rio), filtered to LACNIC prefixes. Expected ORIGIN distribution is ~90% IGP / 9% INCOMPLETE / 1% EGP; reality diverges wildly by collector. Rio shows 90% of prefixes with MIXED origins (different peers at the same collector see different ORIGIN values for the same prefix + origin AS), including 12% triple inconsistency (IGP+EGP+INCOMPLETE); Fortaleza — same country, similar peer count — shows only ~11% mixed. EGP usage in Fortaleza jumped abruptly from August 2023.
- **How**: Monthly RIBs converted to text, filtered with monthly LACNIC delegated files, grouped per unique prefix and classified by ORIGIN. The anomaly resolves through an operator case study: that operator deliberately re-marks routes learned from remote peers as EGP, because ORIGIN is evaluated before next-hop distance in best-path selection — using the attribute as a policy lever rather than a provenance descriptor. Corroborated by an independent RIPE 91 talk on BGP ORIGIN rewriting (James Bensley).
- **Where applicable**: Anyone consuming BGP data — analytics, path-prediction tools, policy engines — or teaching BGP. Measurement is LACNIC-scoped, but the deck explicitly notes the phenomenon is not regional; the closing question ("change the attribute, or change how we interpret it?") is an IETF-shaped problem.

### The annoying Noisy BGP Speakers

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/BGP-Noisy-speakers-ElisaP-AleA-v2.pdf) · [Recording](https://youtu.be/9j1Nb7MN5ew)

Alejandro Acosta and Elisa Peirano (both LACNIC, per slide contact addresses)

- **Why**: Quantifies BGP update noise with a simple, reproducible per-ASN metric — useful for NOC hygiene, route-server operations, and for grounding "BGP churn" conversations with peers in data.
- **What**: Processing 2.2M+ BGP messages from RRC24 (Montevideo) and RRC15 (São Paulo), covering 86,398 ASNs and ~1.44M IPv4/IPv6 prefixes: the mean noise index is ~1,547 updates per announced prefix versus a median of 234 — noise is heavily concentrated in a small set of participants; IPv6 is measurably noisier than IPv4; and most of the noisiest ASNs belong to organizations outside the LAC region. Causes cited: software bugs, misconfigurations (notably missing `update-source`), and hardware/DoS-induced session instability. Mitigations: route filtering, correct `update-source`, prefix limits on peers, dampening, and moderate timer tuning.
- **How**: A per-ASN noise factor (updates per announced prefix) following the SIDN Labs "Noisy Neighbours" methodology (CNSM 2025), computed with Python (mrtparser, pandas, numpy) against NRO delegated-extended files for country mapping.
- **Where applicable**: IXP/route-server operators and any NOG doing BGP hygiene; methodology is reproducible from public collectors. Country-level conclusions are vantage-point-specific (two LAC collectors).

### BGP Optimization for Medium-Sized ISPs: Technical and Financial Decisions Using Open-Source Tools

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/fernando-tipiani-lacnic45-ftl-optimizacion-bgp-para-isps.pdf) · [Recording](https://youtu.be/cuiku_FkTPI)

Fernando Tipiani (no affiliation listed in the program)

- **Why**: A worked, adoptable playbook that connects per-prefix flow data to BGP announcement decisions to the transit bill — the technical-financial bridge the PM's stakeholders constantly ask for, built entirely on open-source tools.
- **What**: A method for balancing inbound traffic across two (or more) transit providers with different tariffs and percentile-95 commitments: measure per-provider consumption (Observium or LibreNMS SNMP/billing modules), rank traffic per /24 (Akvorado for sFlow/NetFlow/IPFIX — NFSen noted as obsolete), then regroup which prefixes are announced toward which provider to minimize overage. Worked example: a 55 Gbps ISP with 20/10 Gbps commits and $1/$2 per-Mbps tariffs cuts monthly overage from $25,000 to $16,000 — a 36% saving — by shifting traffic groups to the cheaper provider.
- **How**: Open-source monitoring stack → per-prefix traffic ranking → iterative prefix grouping to hit target consumptions per provider → update BGP announcements and verify. Final recommendations: secure commits without rate-limiting but with burstable capacity; avoid concentrating more than 60% of traffic on a single provider; use IXPs and peering as the primary cost lever.
- **Where applicable**: Multi-transit ISPs and enterprises on percentile-95 billing. Assumes comparable service quality across providers and stable enough traffic patterns for prefix-level grouping to stick over a billing cycle. Tooling is fully open source and broadly adoptable.

### LightScope: Turning Unused Production Ports into Global Network Telescopes and Honeypots

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic-45-lightscope-v2.pdf) · [Recording](https://youtu.be/zr7wZqv1MwY)

Eric Kapitanski (USC Information Sciences Institute; advisor Jelena Mirkovic)

- **Why**: A genuinely new measurement vantage point for the network-security side of the PM's portfolio: as IPv4 dark space shrinks, this turns closed ports on live production hosts into telescope/honeypot sensors, with evidence it sees attackers that dark-space telescopes and honeynets miss entirely.
- **What**: A lightweight sensor (median 7.5% of one core / 191 MB RAM; 295+ nodes) deployed across 27 domains and 243 internet-reachable endpoints (UCSD 57, Internet2 46, SDSC 35, Nebraska 28, Amazon 15, plus DFN, SURF, Verizon, Deutsche Telekom and others). It answers TCP SYN attempts to unused ports on in-use IPs — addresses attackers already know about — forwarding sessions to an ISI honeypot with the adopter's IP anonymized (IRB-approved). Findings: scanning behavior clusters by Jaccard similarity of port sets (broad multi-domain scanners vs targeted single-domain scanning); LightScope observes scanner IPs exclusive to any passive telescope or residential honeynet, and exclusivity increases down the attack funnel (scanners → attackers that log in and run commands). Cross-check against commercial intel: of 13,667 IPs that logged into honeypot ports and ran commands, GreyNoise classed 74% as malicious and AbuseIPDB recommended blocking 58%.
- **How**: Agent on production hosts captures connection attempts to unused ports; analysis quantifies per-endpoint visibility and overlap with telescopes/honeynets using exclusivity and Jaccard metrics.
- **Where applicable**: Research and CSIRT measurement programs; any network can adopt the sensor. Limitations: TCP SYN only, no UDP or backscatter, deliberately capped resource use. The broader implication matters to anyone reasoning from telescope data alone: dark-space-only visibility is increasingly incomplete.

## Wildcard

### Automating Technical Support at ISPs Using AI Agents and TR-369 (USP)

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/LACNIC_FTL_2026_Jaris_Aizprua.pdf) · [Recording](https://youtu.be/vwqoQCrLgFk)

Jaris Aizprúa Barrios (no affiliation listed in the program)

- **Why**: Not a DC/cloud-native/security/identity talk, but a concrete signal of where network operations is heading: LLM agents with real device-telemetry authority autonomously resolving L1 support — and a preview of exactly the "how much authority do autonomous agents get over infrastructure" question the PM tracks on the agentic-identity side.
- **What**: An architecture plus demo pairing TR-369/USP (Broadband Forum's User Services Platform — bidirectional, TLS/mTLS-secured CPE management with continuous push telemetry and MQTT/WebSockets/STOMP transports, succeeding TR-069/CWMP) with LLM agents: an n8n-orchestrated agent that reads live CPE state and resolves the 60–70% of L1 tickets that are repetitive (no signal ~25%, forgotten WiFi password ~18%, speed complaints ~15%), answering from the ISP's own documentation via RAG instead of hallucinating.
- **How**: LLM selection with cost framing (Gemini 2.5 Flash ~$0.75/1M tokens, GPT-4o mini, Claude Haiku 3, or Gemma 4 fully on-prem via Ollama/vLLM for data sovereignty); RAG over equipment manuals and internal procedures; n8n/Make/Zapier automation glue; TR-369 provides ground-truth telemetry (signal levels, reboots, push alerts) so the agent acts on measured device state rather than customer description.
- **Where applicable**: Consumer ISPs with managed CPE fleets; requires TR-369-capable CPEs and a USP controller (ecosystem adoption still growing; large TR-069 fleets need migration). The agentic-ops pattern — autonomous agents combining device control, retrieval, and action — generalizes well beyond support desks.

### IP Geolocation Update

**Links:** [Slides](https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic4-ipgeo-v2.pdf) · [Recording](https://youtu.be/VaxG99ELJB0)

Lee Howard (presenting the IAB workshop report)

- **Why**: The IAB just ran a dedicated workshop because IP geolocation is breaking under CGNAT, satellite networks, and privacy proxies — and the remediation path runs through RPKI-signed geofeeds (RFC 9632), tying into the routing-PKI world the PM already follows.
- **What**: A report on the IAB's December 2025 IP Geolocation Workshop (30 accepted submissions, 67 participants): why geolocation is used (CDN/edge selection, content licensing, fraud, compliance), current mechanisms (RFC 8805 CSV geofeeds plus RFC 9632 RPKI-based discovery and authentication), and the gaps: no ontology for what a location claim even means (user vs. egress vs. infrastructure vs. jurisdiction); >95% accuracy at country level but sharp degradation at city/coordinate level; CGNAT/mobile/satellite mapping users to gateway locations; "digital sinkholes"; stale data persisting after IPv4 block transfers; no feedback loop for ISPs to correct third-party databases; and privacy tension (IP-as-PII, VPN/proxy interactions).
- **How**: Workshop-report format — use cases, current mechanisms, gaps, and future directions (richer geofeed expressiveness; new mechanisms that don't rely on implicit signals, e.g., authenticated and consent-based HTTP headers) — intended to seed future IETF/IRTF work.
- **Where applicable**: Anyone whose services, compliance, or CDN/edge logic depend on IP geolocation, and operators who should be publishing accurate geofeeds. This is direction-setting standardization content, not deployable tech today.

### Towards the Age of IPv6-Only

**Links:** [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/05/redes-mayoritariamente-ipv6v4.pdf) · [Slides (PDF)](https://apievt.lacnic.net/wp-content/uploads/2026/05/lacnic45-dnsrecursivodetrasdenat64.pdf) · [Recording](https://youtu.be/zHTjt1dLqYI)

Speakers not listed on the program item; the LACNIC 45 tutorial overview identifies José Cotúa and Alejandro Acosta (LACNIC tutorial team)

- **Why**: IPv6-mostly (RFC 8925) is quietly becoming the pragmatic end-state for campus, enterprise, and access networks — the PM may not be tracking it, and this tutorial carries real configurations and an OS-support matrix that de-risk a decision they will likely face.
- **What**: A hands-on tutorial on IPv6-only and IPv6-mostly operation: NAT64/DNS64 mechanics and header translation; 464XLAT for IPv4 literals, legacy IPv4-socket software, and broken dual-stack servers; and the IPv6-mostly model (RFC 8925 §1.2) where one segment simultaneously serves IPv6-only, dual-stack, and IPv4-only hosts — hosts that request DHCPv4 option 108 simply do not get an IPv4 address. Claimed benefits: >2/3 savings in IPv4 addresses, less NAT, and a simpler network than dual stack. Companion decks cover an IPv6-only recursive DNS resolver behind NAT64, RFC 8950 (extended-nexthop encoding for routing IPv4 packets over IPv6-only links), and DHCPv6 prefix delegation.
- **How**: DHCP option 108 signaling (client requests it; a configured server offers an IPv4 lease of "none for 30 minutes"; the client aborts and retries later), with host-side CLAT — native on Android 12+, iOS 15+, and macOS 12.0.1+ (CLAT activates on seeing the PREF64 router-advertisement option); Windows 11 support in recent releases; Linux via the clatd script or NetworkManager 1.52+.
- **Where applicable**: Enterprise/campus/access networks with NAT64 in place and IPv4 pool pressure; DC relevance is narrower but real (RFC 8950 for IPv6-only fabrics). The OS-support matrix is the gating constraint — older client fleets simply keep dual stack on the same segment, which is precisely what the model is designed to allow.

## Themes

- **From origin validation to path validation.** The program's routing-security arc runs RPKI/ROA → a real forged-LoA hijack of LACNIC's own ASN (which ROV could not stop because the attacker impersonated the authorized origin AS too) → ASPA as the fix, with both LACNIC and the NRO committing to ASPA deployment in 2026. The exposed weak link is procedural: PDF letters of authorization in transit provisioning.
- **BGP measurement is maturing into an operational discipline.** Multiple independent works quantify instability (effective vs. redundant updates), noise (heavy-tailed, concentrated in few ASes, IPv6 noisier than IPv4), attribute semantics (ORIGIN rewritten as a policy lever), and AS-graph structure — all from public RIS/RouteViews collectors with reproducible Python pipelines.
- **LLM/GPU workloads are reshaping fabric architecture and interconnect economics.** Split frontend/backend leaf-spine designs, and inference vs. dataset-ingestion traffic profiles that demand opposite peering strategies (latency-driven IXPs/PNIs vs. cost-driven transit management and 95th-percentile exposure).
- **Physical-layer future-proofing reaches even regional operators.** Coherent-pluggable physics, spectrum-based planning (THz/GHz rather than nm/channel numbers), and 400 GHz channelization as the flexibility mechanism toward 800G/1.6T.
- **A consolidated open-source automation stack.** NetBox as source of truth + GitLab CI/CD + Nornir + telemetry (MTR/Elasticsearch/Grafana), reproducible in Containerlab, with flow analytics (Akvorado) feeding BGP decisions — the same pattern recurs across multiple talks.
- **Security is moving into the dataplane and the host.** ML inference pushed into SmartNICs (P4 match-action tables) and eBPF/XDP dataplanes to eliminate IDS mirroring and bottlenecks, running at line rate with sub-microsecond inference overhead.
