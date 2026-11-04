<!--
conference: SwiNOG #42
type: operator
source_url: https://www.swinog.ch/meetings/swinog42/
generated: 2026-11-02
registry_key: swinog-42
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# SwiNOG #42 — Digest

## Core

### Networking for AI

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/20261020_SwiNOG-Networking-for-AI_v2.pdf)

Remi Locherer - Arista Networks

- **Why**: AI training/inference clusters are the hardest physical datacenter networking problem of the moment, and this is a dense technical walkthrough of the fabric design decisions: lossless Ethernet, load balancing, topology, optics, and power. Directly in the PM's physical-DC wheelhouse (RoCE/lossless fabrics, optics, topology).
- **What**: A structured treatment of why AI traffic breaks traditional DC design — few, large, long-lived, highly synchronized flows; bursts at 100% of link rate with no stat-muxing; a single loss or XPU failure halts the whole job — followed by concrete scale-out designs, congestion control, load balancing evolution, and the Ultra Ethernet / MRC trends, plus the optics and cooling consequences.
- **How**: Covers RoCEv2 framing and why "converged Ethernet" means lossless Ethernet (PFC hop-by-hop on ingress, ECN end-to-end, DCQCN). Explains why ECMP fails on low-entropy XPU-to-XPU flows (collisions, out-of-order delivery on link flap) and the progression from RDMA-aware hashing to dynamic and cluster-aware load balancing. Compares fat-tree vs planar/rail topologies (flexibility vs fiber cost and 1:1 bandwidth), gives per-tier XPU-count design tables up to ~660k hosts on multi-planar 7060XE7 fabrics, and covers UET packet spraying, packet trimming (64B trimmed frames as fast congestion signals), and the OpenAI-led Multipath Reliable Connection (MRC) OCP transport spec. Finishes with the physical layer: LPO transceivers (≤8W vs 14-16W, ~50% power reduction, 9x lower latency), liquid cooling, and XPO extra-dense pluggable optics for 204.8T in 1OU.
- **Where applicable**: AI backend/scale-out fabric design generally; the concepts (lossless forwarding, entropy, oversubscription, power-as-constraint) transfer to any DC operator. Note it is an Arista session and the design tables are Arista-platform-specific (7060X6/7800R4/7060XE7), but the vast majority of the content is protocol- and silicon-generic, not a disguised pitch.

### Beyond RPKI Origin Validation, what do we gain with RFC9234 (BGP roles) and ASPA

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/OpenBGPD-SWINOG-42-2026.pdf) · [Recording](https://youtu.be/ECjCo7pNnyg)

Claudio Jeker - RSSF (OpenBGPD lead developer, rpki-client co-maintainer)

- **Why**: BGP security is a core interest, and this is the rare talk that grounds the RFCs in real 2025–2026 incidents and gives a concrete, ordered deployment checklist. The Hetzner forged-origin hijack case alone is worth the read: it shows exactly where ROV stops protecting you.
- **What**: An argument that ROV is necessary but insufficient — it does nothing against path leaks (Voxility/Lumen April 2025, Cloudflare January 2026, both with intact origins) and nothing against forged-origin hijacks — and that RFC 9234 (BGP roles + OTC) plus ASPA close those gaps. Includes a sharp section on ROA `maxLength` as an attack surface: a /16 with maxLength /24 authorizes an attacker to forge your origin for any unannounced more-specific.
- **How**: RFC 9234 exchanges role information (provider/peer/customer/RS/RS-client) in the BGP OPEN, rejects role-mismatched sessions, and adds the transitive Only-To-Customer attribute so routes learned from providers/peers/RS are marked and rejected when re-exported upward — catching type 1–4 leaks at the source even with a broken export filter. ASPA publishes a signed provider list in the RPKI; routers check AS_PATHs for valley-free propagation, so even partial deployment rejects provably Invalid paths while leaving Unknown paths usable. The Hetzner case (162.55.80.0/24, forged AS_PATH `... 6204 62390 24940`, ROV result "Valid") was later invalidated by AS24940's post-attack ASPA record, which doesn't authorize AS62390. Call to action: reject ROV invalids, publish minimal ROAs, configure roles/OTC, publish complete ASPA provider lists (including backup and DDoS-mitigation transit).
- **Where applicable**: Any ISP, transit provider, or IXP route server; vendor support is the practical constraint — OpenBGPD/BIRD/FRR and (recently) JunOS 25.2R1 and MikroTik RouterOS 7.21 support RFC 9234; ASPA is available in OpenBGPD and BIRD now, with FRR/JunOS/XR planned or in field trial. Broadly applicable; publishing ROAs/ASPA works even before your routers validate.

### The Cloud-Native Advantage: Intent-based Network Automation

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG-42-%E2%80%93-The-Cloud-Native-Advantage.pdf) · [Recording](https://youtu.be/WmebR1Lf5lE)

Alexander North - Swisscom (with Markus Vahlenkamp - Nokia)

- **Why**: Bridges the PM's two worlds in one talk — Kubernetes resource-model tooling applied to YANG/NETCONF/gNMI device configuration. The core problem is one anyone running CNFs or telco functions has hit: Helm deploys the pod, but the running config is still set with imperative per-instance NETCONF RPCs, outside any reconcile loop.
- **What**: Schema Driven Configuration (SDC), an open-source (initiated by Nokia, CNCF Sandbox since 2026) Kubernetes Operator that models device configuration as Config custom resources with priorities, and reconciles them against the device via NETCONF or gNMI. In production at Swisscom for the 5G mobile core — roughly 2000 pods, 5000 interdependent parameters, 14 network functions.
- **How**: Config CRs declare only their slice of the YANG tree, tagged with a target and a priority. SDC merges all Configs (priority resolves overlaps — a temporary ops override at prio 50 beats the platform baseline at prio 100, and deleting the override restores the baseline), validates the merged tree against YANG, diffs against the device's running config, and translates only the delta to NETCONF/gNMI with per-NOS rules. Drift is surfaced as Deviation CRs with typed reasons (`NOT_APPLIED`, `OVERRULED`, `UNHANDLED` brownfield config); `revertive: true` re-applies automatically. A `kubectl sdc blame` command shows, for every leaf, whether it came from which Config or from brownfield running config — "Config Blame is to Config apply what Git Blame is to commit."
- **Where applicable**: Anything with a YANG model — physical routers, VMs, containers. Note the abstract oversells "self-healing": default behavior reports drift rather than fixing it (revertive is opt-in), and RESTCONF is not yet supported. The Swisscom deployment is a large-scale telco core, but the mechanism itself is general and adoptable at docs.sdcio.dev.

### Managing IP Allocation with an Open-Source DDI

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/Managing-IP-Allocation-with-an-Open-Source-DDI-2.pdf) · [Recording](https://youtu.be/70M_GdX4QBA)

Marco Martinez - Swisscom

- **Why**: IPAM is an explicit core interest, and this is a practitioner's build report: no open-source DDI exists today, so the speaker assembled one from three proven components rather than building DNS/DHCP/IPAM from scratch.
- **What**: A composable DDI built on Infrahub (IPAM/source of truth), Kea (DHCP), and PowerDNS (DNS), orchestrated by Event-Driven Ansible into a single event-driven configuration plane. The IPAM layer is authoritative: DNS entries and DHCP reservation pools are generated dynamically from the modeled dependencies in Infrahub.
- **How**: An earlier attempt (a "configuration plane" over the three products with separate automation tooling) failed on consistency; the working design makes Infrahub the source of truth, and events from it drive Ansible workflows that apply only the defined properties to Kea and PowerDNS — which keep their production-grade secure configuration for everything else. Reconciliation is built in. The result and code are published (github.com/marcom4rtinez/ddi).
- **Where applicable**: Environments priced out of commercial DDI (the stated motivation: cost, transparency, source of truth, moving out of silos). Honest limitations: HA and the "one vendor supports the whole stack" property of commercial DDI are what you give up; everything runs on containers/Linux and the integration complexity is higher than a monolithic product. Operator-specific in architecture choices, but the pattern (SoT generates DNS/DHCP, event-driven push, reconcile) is broadly reusable.

### Automating Target Discovery in the gNMIc Operator

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/BA-gNMIc-operator-swinog42.pdf)

Daniel Schatzmann

- **Why**: Streaming telemetry (gNMI) moving into Kubernetes, plus automatic synchronization with a source of truth — squarely in the PM's cloud-native networking and network-automation space. It's also a nice example of upstream-able operator work from a bachelor thesis at OST.
- **What**: An extension to the gNMIc Operator (open-source, started 2026) that removes the last manual step in gNMI telemetry: keeping the monitored-target list current. Targets are synchronized from an external source of truth (NetBox in the demo), closing the gap where the monitoring stack and the inventory drift apart.
- **How**: Two complementary mechanisms: periodic pull from NetBox via an export template, and event-driven push from NetBox via webhook — so inventory changes propagate to the collectors without human edits. The demo runs targets in Containerlab with a Prometheus/Grafana monitoring stack; the export template and webhook receiver have both been contributed as examples in the gNMIc Operator docs, and the mechanism is extensible to other sources of truth. (The work is a BSc thesis by Valentino Diller and Roman Weber at OST, supervised by Daniel Schatzmann.)
- **Where applicable**: Any team running gNMI/gNMIc — the operator itself is upstream and open, and the NetBox integration patterns ship in its documentation. General technique, not org-specific.

### From Lab to Production: The Hard Parts of Agentic NetOps

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG_42_NetFabric_v3.pdf) · [Recording](https://youtu.be/MTVdgd6WK_8)

Tobias Bühler - NetFabric

- **Why**: The follow-up to SwiNOG #41's agentic-AI-in-network-ops talk, now with real production deployment scars. For a PM thinking about agentic identity and AI safely operating production networks, this is the most concrete failure-mode catalog available — all drawn from Swiss ISP/MSP deployments on 1000+ devices.
- **What**: The three hard problems of production agentic NetOps — correctness, security, and model/paradigm churn — with real failure cases and code-level fixes. The core thesis: rely on code wherever it matters, and run continuous evaluation, because prompt and skill changes alone do not reliably change agent behavior.
- **How**: Correctness: agents analyzing firewall policies checked only the PREROUTING chain or the first 50 of 950 rules, ignored default-drop policies, and mis-evaluated subnet membership — fixed with a dedicated, multi-vendor firewall logic module in code (given rules and a flow, does it pass: yes/no). Security: agent-written SQL against a multi-tenant metrics DB is wrapped in guardrails that rewrite queries at the AST level to enforce tenant isolation, cap analyzed rows, block modifications, and reject oversized results before they blow the context window; CLI access is mediated by a grammar of available commands scraped from lab devices, categorized with operator approval, so production lookups only pass approved commands (a DMVPN troubleshooting example drops from ~25 blind failed commands to one-shot success). Evaluation: pitfalls include a TODO-list prompt change that tripled run time (3→10 min), synthetic test traces without production noise, and unit-style tests that don't predict long agentic investigations. Reported results: ticket root cause and proposed fix in 2–3 minutes in multiple deployments, early hardware-degradation detection, config-vs-source-of-truth drift detection.
- **Where applicable**: Any operator considering AI agents on production networks. The patterns (guardrails in code, approved command grammars, eval harnesses fed by production incidents) are general; the specifics reflect NetFabric's own deployments and products.

### On-prem LLM cluster for network and security analyses

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/swinog42-on-prem-llm-network-security.pdf) · [Recording](https://youtu.be/KHmfNnx535U)

Mischa Diehm - narrowin

- **Why**: A reference architecture for running AI over network data entirely on-prem — and, unusually, it takes the identity and security model seriously (scoped agent credentials, RBAC, MCP authorization, audit trails linking user → tool call → device change), which maps directly onto the PM's workload and agentic identity interests. It also includes real small-cluster physical networking detail.
- **What**: A four-layer sovereign stack: interaction (chat/web/API + a planning agent), AI (open-weight models — GLM, Qwen, Nemotron, DeepSeek — on a local GPU cluster served by vLLM behind an OpenAI-compatible API), integration (MCP servers exposing purpose-built tools plus skills, not raw data), and context (topology, configs, syslog, CMDB/IPAM, ticketing, or a single device via SSH/REST/SNMP). Evaluated on a multi-vendor IT/OT Containerlab lab network and agent-driven assessments of production data from real networks.
- **How**: Hardware is 4× NVIDIA DGX Spark (512 GB pooled memory for weights/KV cache when sharded across nodes) behind a MikroTik CRS804-4DDQ 400G switch — about 25K CHF. Notable networking finding: internal PCIe limits mean each Spark gets 2×200G, not 400G, so one 200G link carries data plane and management moves to a separate interface; the nodes are memory-rich but bandwidth-poor (~273 GB/s), so MoE models run best. The interesting operational lessons are in data fusion: combine state, signals, inventory, and intent (from a system of record like Infrahub), pair tools with skills instead of exposing raw data, and make every finding verifiable by linking it to source evidence. Security model covers RBAC per role/device/action, MCP Enterprise-Managed Authorization via the identity provider, scoped SSH/API identities for the agent, prompt injection (a malicious ticket can steer tool calls even with a local model), model-trust limits of open weights, audit trails, and human approval gates with rollback.
- **Where applicable**: Operators with privacy, sovereignty (CLOUD Act / AI Act), or cost constraints on shipping network data to cloud LLMs — particularly IT/OT and critical infrastructure. The honest trade-offs are stated: you need staff who can run it, the model market moves monthly, and without clear goals it becomes a time sink. Reproducible as a reference architecture; scale is deliberately small (desk-sized), not hyperscaler.

## Adjacent

### From Connectivity to Cyber Resilience : Defense in Depth for the connected Enterprise

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/Defense-in-depth-for-connected-enterprises-Gautier_Nokia_Swinog_42_Oct20ed1f.pdf) · [Recording](https://youtu.be/xQJpbnAkCK0)

Yannick Gautier - NI ION NOKIA

- **Why**: PQC migration is a real, dated obligation for network security programs (harvest-now-decrypt-later), and the slides contain useful framing — cryptographic debt, discovery→assess→prioritize, migration timelines of 5–15+ years by organization size, and the argument that symmetric crypto survives quantum with larger keys while asymmetric is broken (Shor vs Grover).
- **What**: Nokia's Quantum-Safe Networks pitch: layered, multi-technology key establishment (PQC ML-KEM/ML-DSA per FIPS 203–205, symmetric key infrastructure, optional QKD per ETSI GS 014) with centralized key management (1830 SMS), line-rate encryption at multiple layers, crypto-agility, and sovereignty over entropy. Interesting data point: the estimated qubits needed to break RSA-2048 dropped from ~1 billion (2012) to under 100,000 (2026) across three papers in twelve months.
- **How**: Defense in depth across application/IP/MPLS/L2/physical layers with different key-establishment architectures (PQC-only via PKI, QKD+symmetric, hybrid PKI+PSK), coordinated key rotation, and certified entropy; ends with four telco monetization models for quantum-safe connectivity.
- **Where applicable**: Enterprises and carriers with long-lived confidential data and regulated critical-infrastructure obligations. Caveat: the second half is a Nokia portfolio and services pitch (1830 optical line, SMS key management, QSN service models) — take the threat framing and migration methodology, discount the product push.

### Small BNGs

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/202610xx_FW_Small-BNGs.pdf) · [Recording](https://youtu.be/hnC82wCm0mY)

Fiona Weber - WDZ GmbH // Wobcom GmbH

- **Why**: A contrarian architecture decision with a completed migration to show for it: instead of the industry trend of terminating subscribers on a few huge central routers, AS9136 pushed small white-box BNGs to the edge. A genuine postmortem-flavored operator story — exactly the kind of hard-won, transferable lesson the PM's field values.
- **What**: Migration from 2 central to 25 distributed BNGs on RtBrick software on UfiSpace and EdgeCore hardware (MPLS/IS-IS + SR, BGP, PPPoE/IPoE, QinQ, RADIUS, CGNAT, L2/L3VPN), plus the migration experience: the topology change turned into a major fiber and infrastructure cleanup, strange CPEs in the field, "bugs, bugs, bugs," and subscriber migration pain.
- **How**: Distributed termination removes centralized failure points, simplifies backbone/fiber planning, enables direct routing and service flexibility, and avoids "major vendor tax" with pay-as-you-grow boxes. The costs: IP pool management and config automation get harder, and you're running more complex hardware deep in the field with a new software vendor. The speaker's guidance on fit: it depends on physical footprint and org structure, and is especially attractive for medium-sized networks — but even if decentralization isn't right for you, shrink your failure domains ("huge chassis routers need to die").
- **Where applicable**: The migration specifics are AS9136/WDZ-specific; the failure-domain reasoning and the honest challenge list are broadly applicable to any access-network operator.

### The Accidental Platform Team: Kubernetes Operators at Swisscom

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/2026-10-21-swinog-accidental-platform-team.pdf) · [Recording](https://youtu.be/7kWNTz5mPek)

Fabian Schulz - Swisscom (with Lea Brühwiler)

- **Why**: The organizational counterpart to the SDC and gNMIc talks: what happens when Kubernetes operators for network automation (IPAM, inventory, NETCONF router config — the same Swisscom stack) get adopted beyond their original 5G-core scope and become "Operators as a Service" for a platform team running Kubernetes-as-a-Service.
- **What**: An adoption story, not an architecture story. The honest middle section is the value: a wall of real user objections ("I don't understand Kubernetes", "we were faster the old way", "there will always be manual changes on the box", "I just did it myself with a Gitlab pipeline, it's easier") and the incremental answers that overcame them.
- **How**: Gradual adoption (pick one easy use case, ship a prototype early, iterate on feedback), then four countermeasures: a graphical UI for people who won't use kubectl; observability and traceability (commit history, provenance of every change) to answer "how do I know where this change came from"; knowledge-sharing initiatives and regular check-ins to build trust. The before/after numbers are striking: 5G-core network provisioning dropped from multi-week sequences (change requests 5–10 days, IP tables 2 days, integration 5–10 days) to minutes-to-hours of intent creation with continuous automated testing. Reference architecture published at architecture.cncf.io.
- **Where applicable**: Teams building internal platform/operator tooling — the human-side lessons are the transferable part and generalize well beyond telco. Scale numbers are Swisscom-specific.

### Internet Domain Blocking: Current Legal Situation and Outlook on the Current Revision of the Telecommunications Act

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/20261020-Schlauri-Netzsperren-Swinog42.pdf) · [Recording](https://youtu.be/bsemYuiTfz4)

Simon Schlauri - Ronzani Schlauri Attorneys

- **Why**: Not technical, but directly operationally relevant to any Swiss ISP: prosecutors are ordering access providers to block domains, and the talk documents the actual cases, the technical-refutation expert opinion, and the draft legislation. For a PM whose products sit on Swiss networks, this is where content-blocking obligations are heading.
- **What**: A case history from 2025–2026: Vaud and Valais prosecutors ordered providers to "seize" domains (reinterpreted as blocking after the fact), imposed a CHF 6,000 fine on a non-compliant provider, and ordered blocking of a climate-activist group's URLs — even though the site was hosted in Switzerland and the prosecutor never asked the host to take it down. The Vaud Cantonal Court lifted that block in May 2026 but dodged the core legality question; a Federal Supreme Court appeal is pending.
- **How**: Legal analysis plus a decisive technical contribution: a Switch expert opinion establishing that individual URLs cannot be blocked via DNS at all, and that the only practicable ISP measure is blocking an entire domain on their resolver — which over-blocks (all services under the domain, including email) and violates net neutrality. The proposed new Art. 6a Telecoms Act would mandate blocking of fraud-related second-level domains on fedpol notification — narrow, but still without judicial review or a hearing for site operators. The speaker's position: "delete, don't block" — go after the hosting source, and if blocking exists at all, only by statute with a court weighing interests.
- **Where applicable**: Swiss access providers and anyone operating DNS resolvers there. Jurisdiction-specific, but the pattern — courts accepting "the other providers comply" as proof of feasibility — is a caution for operators everywhere.

### FRRouting Open Discussion

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/FRRouting-%E2%80%93-Open-Discussion-%C2%B7-SwiNOG-42.pdf) · [Recording](https://youtu.be/ivgjZ7B6Xo8)

Martin Winter - NetDEF / FRRouting

- **Why**: Light on content by design (it was an interactive feedback session), but worth a note for a PM with BGP/datapath interests: it's a deliberately vendor-free channel to the maintainers of the open-source routing suite that underpins SONiC, white-box NOSes, and much of the leaf-spine world.
- **What**: An experiment in format — no product pitch, just community Q&A on FRR's state (forked from Quagga 2017, ~30 maintainers, BGP/OSPF/IS-IS/LDP/BFD and more, 10.7.1 current) and what's missing for operator use cases.
- **How**: Structured prompts (who uses it, who tried and stopped and why, what's missing), with NetDEF — which runs FRR's community CI and has three employees in Switzerland — explicitly inviting feature requests, bug reports, and contributions.
- **Where applicable**: Relevant to anyone evaluating open-source control planes for routers, route servers, or container-networking BGP; the session itself is a one-off, but the contact channel is durable. Skippable if you weren't in the room.

## Wildcard

### Retro Networks

**Links:** [Slides](https://www.swinog.ch/wp-content/uploads/2026/11/SwiNOG-Oct.-2026-V3.pdf) · [Recording](https://youtu.be/L4rc3l15crM)

Gianpaolo Del Matto - THE PHINTAGE COLLECTOR

- **Why**: Looks like a nostalgia talk and is, for two-thirds of it (10BASE5 vampire taps, PhoneNet, Token Ring developed in Zurich, DOS memory limits) — but it pivots into one of the most honest available case studies of LLM-assisted development in a deeply constrained environment, and the lessons are unusually sharp.
- **What**: The speaker reimplemented the 3Com 3C509B configuration utility (3CCFGCLI) in 16-bit real-mode 8086 assembly, because the original needs a 286+ and 232 KB on disk. The result: 0.8.3 is feature-complete and runs on a real 8086 in ≤256 KB RAM, with the binary refactored from 40 KB down to 26 KB.
- **How**: Used an LLM as "a very fast, sometimes hallucinating developer" — not an oracle. Concrete episodes: the LLM correctly suggested a full hardware mock early, the speaker refused, and paid for it with an entire 0.6 refactoring branch; separately, the LLM burned three hours chasing a "mysterious" 1-byte offset down into disassembling Turbo Assembler itself when the root cause was that 8086 short jumps can only reach ±127 bytes and the routine had simply outgrown them. Discipline: the ~180-case test harness was human-built, all output reviewed, and continuous refactoring kept the bloat down.
- **Where applicable**: As engineering-method takeaways, broadly — "AI can help you build it, but you still need to understand it, review it, and prove that it works." Published at github.com/gpdm/TPC-3CCFGCLI. Only the LLM-methods half generalizes; the vintage-hardware half is for fun (and the ENTER Technikwelt exhibit).

### Reality, Rewritten: AI as Forger and Investigator

Dominik Haenni - Zurich Forensic Science Institute

- **Why**: The opening keynote frames the question the three agentic-AI talks later dance around: when the same technology fabricates evidence and analyzes it, what happens to expert judgment and trust in organizations — which is, in the end, the same question as trusting an agent's root-cause analysis on a production network.
- **What**: An exploration of generative AI's dual role — producing convincing fake images, cloned voices, and plausible documents, while also accelerating forensic analysis, research, and software development — with current examples from the Institute's casework, and a look beyond the tool at responsibility and how organizations work when AI compresses timelines.
- **How**: Case-example driven (the abstract does not describe a method); the argument is that when AI "changes the rules," business as usual in evidence handling — and by extension, any function that certifies truth — is not affordable.
- **Where applicable**: Not a networking talk, but its trust-in-automated-findings framing transfers directly to anyone shipping AI-generated analysis into operational workflows. (from abstract only)

## Themes

- **Agentic AI meets production networks — with a converging answer.** Three talks (Agentic NetOps, on-prem LLM, Retro Networks) independently land on the same discipline: correctness and security belong in code (AST-level query guardrails, approved command grammars, dedicated logic modules), not in prompts; findings must be verifiable against evidence; and continuous evaluation against production data, not synthetic unit tests, is what keeps agents working long-term.
- **The Kubernetes resource model is reaching into network devices.** SDC (Config CRs reconciled to YANG/NETCONF/gNMI), the gNMIc Operator (telemetry targets as reconciled state), and Swisscom's platform-team story are the same pattern at three layers: watch → compare → act, with sources of truth (NetBox, Infrahub) feeding declarative intent.
- **BGP security is moving past ROV, pushed by fresh incidents.** The Cloudflare leak (origin intact, ROV useless) and the Hetzner forged-origin hijack (ROV said Valid) are this cycle's motivating cases; RFC 9234 roles/OTC and ASPA are the deployable response, and minimal ROA maxLength is the cheap hygiene fix available today.
- **AI fabrics made power and optics the binding constraint.** Lossless Ethernet, entropy-aware load balancing, and topology (planar vs fat-tree) were all framed as consequences of XPU economics; LPO, XPO, and liquid cooling are the physical-layer response — optics and power, not switching capacity, dominate AI-cluster CapEx/OpEx.
- **Sovereignty and self-hosting as a Swiss operator theme.** On-prem AI (data never leaves the building), CommunityRack's "knowledge stays in the community" positioning, open-source DDI replacing priced-out commercial products, and the domain-blocking legal fight all argue the same case from different directions: control over stack, data, and know-how.
- **Composable open-source stacks displacing monolithic vendor products.** Infrahub+Kea+PowerDNS as a DDI, RtBrick on white-box UfiSpace/EdgeCore hardware as distributed BNGs, open-weight models on vLLM with MCP, and FRR's quiet ubiquity — the pattern across talks is assembling proven components around a source of truth, and the recurring cost is integration complexity and self-managed HA.
