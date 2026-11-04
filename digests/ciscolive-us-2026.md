<!--
conference: Cisco Live US 2026 (Las Vegas)
type: vendor
source_url: https://www.ciscolive.com/on-demand/on-demand-library.html?search.event=1769534158486002QYqy
generated: 2026-11-03
registry_key: ciscolive-us-2026
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# Cisco Live US 2026 (Las Vegas) — Digest

A note on sources: the Cisco Live on-demand library is a login-gated SPA — page fetches return only a shell with no session content, and the program carries no paper or slide links. Every write-up below is therefore grounded in the session abstract only. Cisco Live is a vendor conference: `BRK`/`TAC`/`CENETI` breakouts usually carry real technical depth, while `PSO` (Product Session Overview) sessions are product marketing and are down-ranked accordingly — though several signal genuine technology shifts worth tracking.

## Core

### Building AI/ML Fabrics at Hyperscale: Architecture Evolutions, Challenges, Open Standards, Performance Characterization and Validation on Cisco SiliconOne-based Platforms. - BRKMSI-2014

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362746189001qPdj)

Masiuddin Mohammed (Cisco), Evan Knipp (Cisco)

- **Why**: The single densest architectural map of where AI-scale DC fabrics are going — cluster size, topology generations, and DCI constraints are exactly the design questions a physical-networking PM needs answered.
- **What**: A trace of AI fabric evolution from 4K/16K-GPU leaf-spine, to 64K-GPU Disaggregated Scheduled Fabric (DSF) two-tier with super-spines, to >200K-GPU three-tier scale-out, plus multi-DC DCI interconnect; paired with a benchmarking methodology for validating these fabrics (from abstract only).
- **How**: Addresses scale-out concerns (fat flows, ECMP polarization, asymmetric failures, fault resilience) separately from scale-up concerns (~8x per-accelerator bandwidth for tensor-parallel, e.g. NVL72), and DCI demands of high-speed buffering and encryption over ~100 km / 1 ms RTT. Validation is done in production-like environments using open, standards-aligned test practices to minimize test drift.
- **Where applicable**: Cisco-specific (Silicon One platforms) and hyperscaler-derived, but the topology taxonomy, failure-mode catalog, and benchmark methodology generalize to any large AI fabric build.

### Designing RoCEv2 Networks for Distributed AI Training with Cisco Nexus 9000 - BRKDCN-2688

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362706030001qxos)

Praveen Poojary (Cisco)

- **Why**: Lossless/low-loss RDMA fabric tuning is the hardest operational problem in AI clusters today; this is the session that actually walks the PFC/ECN/congestion-control knobs.
- **What**: A design-and-operate guide for RoCE fabrics purpose-built for training jobs of thousands to tens of thousands of GPUs running days-to-weeks, targeting near-lossless behavior and predictable AllReduce/AllGather throughput (from abstract only).
- **How**: Covers the frontend/backend network separation common at hyperscalers and its implications for leaf-spine topology, routing, and failure domains; then congestion control, PFC/ECN, and QoS tuning for bursty, low-entropy AI flows.
- **Where applicable**: Nexus 9000-specific in tooling, but the lossless-fabric design principles (entropy, incast, ECN thresholds) apply to any RoCEv2 backend fabric.

### Real World Deployments: Architectural lessons learnt from a 100+ Node AI Factory Deployment - BRKXAR-2039

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362792577001qwKT)

Dave Lucas (Cisco), Nandu Shankar (Cisco)

- **Why**: The closest thing in this program to an end-user case study with failure discussion — a real integration bring-up, not a clean-room reference architecture.
- **What**: Lessons from standing up a 100+ node "AI factory" spanning compute, network, and storage, with dual GPU vendors, virtual and containerized workloads, RDMA-accelerated storage with GPUDirect, multi-tenant security, and a scalable RoCE front and back-end fabric (from abstract only).
- **How**: Explicitly covers the failure modes that don't appear in config guides: multi-OS GPU driver inconsistencies, RoCE fabric optimization, cross-vendor GPU networking quirks, shared-services dependencies, cabling/topology missteps, and typical bottlenecks.
- **Where applicable**: Deployment-specific (one environment, Cisco-built), but the cross-vendor integration pitfalls are broadly instructive for anyone running mixed-GPU AI infrastructure.

### Cisco Nexus 9000 Architecture - BRKDCN-3939

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362712723001qA8P)

Faraz Taifehesmatian (Cisco)

- **Why**: Switching silicon and forwarding mechanics are core to this PM; this is the internals session for Cisco's workhorse DC switch line.
- **What**: An in-depth architecture study of the latest-generation Nexus 9000 modular and top-of-rack switches — ASIC architecture, forwarding mechanics, and physical design (from abstract only).
- **How**: Walks the packet path through the ASIC and the hardware-enabled features that produce high-performance DC network services.
- **Where applicable**: Nexus 9000-specific; useful as a concrete datapoint on merchant/custom silicon trade-offs and what a modern DC ASIC feature set looks like.

### Silicon One Unveiled: Diving into the power of Cisco silicon - BRKNWT-2624

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362749382001qqAi)

Ramesh Sivakolundu (Cisco), Dave Zacks (Cisco)

- **Why**: Silicon One is the unifying silicon across Cisco's enterprise, SP, and AI portfolios; understanding its design rationale is directly relevant to physical DC networking decisions.
- **What**: A deep-dive into how Silicon One is architected and why — the design choices, distinguishing features, and how its capabilities map to different network roles. Caveat: the abstract is noticeably hype-toned ("fast-paced... you will be glad you did!") and carries no specific technical claims, so depth must be verified in the room or on the recording (from abstract only).
- **How**: Presented as silicon design-and-engineering rationale — not just feature lists but the why behind implementation choices, and how those translate into deployable designs.
- **Where applicable**: Cisco silicon-specific; valuable mainly as the architectural underpinning for the AI-fabric and routing sessions above.

### 400G, 800G, and Terabit Pluggable Optics: What You Need to Know - BRKOPT-2699

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362762541001qNLj)

Mark Nowell (Cisco), Errol Roberts (Cisco)

- **Why**: Optics is a listed core interest, and this is the standards-and-roadmap session covering the full 400G→1.6T transition.
- **What**: Current 400G pluggable technologies and applications, next-gen form factors for 800G and 1.6T (including breakout use cases), the new 800Gb/s and 1.6Tb/s Ethernet standardization work, and optical co-packaging developments for integrating optics into ASICs (from abstract only).
- **How**: Covers both coherent and non-coherent optics, what's driving each development, and the system/network implications of adopting them.
- **Where applicable**: Broadly applicable industry roadmap rather than a Cisco product pitch (Mark Nowell is a long-time IEEE 802.3 participant); co-packaging and LPO/LRO implications matter to any high-density DC design.

### VXLAN EVPN: A Deep Dive into Packet Forwarding - BRKDCN-3966

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362712951001q1X6)

Lukas Krattiger (Cisco)

- **Why**: EVPN/VXLAN datapath internals are a core interest — this is the "follow the packet" internals session, not a feature overview.
- **What**: A day-in-the-life walkthrough of a VXLAN EVPN packet: routing and bridging behavior, and multi-destination (BUM) traffic handling, from ingress VTEP to egress VTEP and beyond (from abstract only).
- **How**: Step-by-step datapath trace of encap/decap, ARP suppression, and multicast replication mechanics on the fabric.
- **Where applicable**: Any VXLAN EVPN fabric; mechanism-focused rather than product-specific.

### Modern Multi-Homing in VXLAN EVPN: Enabling vPC and ESI+ in Today's Data Centers - BRKDCN-2940

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362708226001qwAw)

Parth Patel (Cisco)

- **Why**: EVPN ESI multihoming landing in NX-OS 10.6.1 is a real control-plane shift for Cisco fabrics; the vPC-vs-ESI trade-off is a live design decision.
- **What**: A comparison of classic vPC and the new EVPN ESI multihoming (ESI+), covering how each works, what changes with ESI+, and when to choose one over the other (from abstract only).
- **How**: Real design examples and packet-flow comparisons, framed around fabric scale, resiliency requirements, and operational model. Assumes prior vPC-VTEP knowledge.
- **Where applicable**: NX-OS fabrics specifically; the ESI-MH model itself is the IETF standard mechanism also used by other vendors and SONiC, so the concepts travel well.

### Troubleshooting SONIC on Cisco 8000: Learn how to Troubleshoot BGP, ACL, VxLAN on SONIC - TACMSI-2001

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780412385626001HBEq)

VASU Thatipalli (Cisco)

- **Why**: SONiC is where open-source NOS development is actually happening; a TAC-lead troubleshooting session is a good signal of how production-mature SONiC on Cisco silicon has become.
- **What**: Operational and control-plane debugging of BGP, ACLs, and VXLAN in SONiC environments, plus a structured troubleshooting framework covering data plane, control plane, and root-cause analysis (from abstract only).
- **How**: SONiC CLI techniques and log analysis to isolate faults in production-scale deployments.
- **Where applicable**: Cisco 8000 + SONiC deployments; the framework and CLI methods apply to SONiC generally, and the session doubles as a maturity readout for disaggregated switching.

### Beyond the (Switch)-Port: Exploring the World of Host Networking - BRKNWT-2620

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362748487001q3zR)

Bruce McDougall (Cisco), Chris Lapp (Cisco)

- **Why**: Host-side networking is where this PM's physical and cloud-native interests converge — kernel bypass, eBPF datapaths, CNI performance, and SmartNICs in one arc.
- **What**: A tour from the ToR switch port down into the host: native OS packet paths, hypervisor networking, the Kubernetes CNI ecosystem, and emerging sub-100µs host-networking techniques (from abstract only).
- **How**: Compares virtio/SR-IOV and vSwitch options (OVS, VPP), benchmarks CNI choices — Calico "just routes," Cilium's eBPF policy datapaths, VPP-backed CNIs for terabit throughput — and looks ahead at XDP/AF_XDP kernel bypass, eBPF congestion control, and SmartNICs fusing packet processing with AI inference.
- **Where applicable**: Broadly applicable to Linux host networking and K8s; the real-world benchmark claims (terabit VPP CNIs, sub-100µs paths) should be probed for environment specifics.

### Life of a Packet in Kubernetes: A Network Engineer's Guide - BRKCLD-3734

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362683763001qJVv)

Nico Vibert (Cisco)

- **Why**: A datapath-internals walkthrough of Kubernetes networking using Isovalent Cilium — squarely on this PM's core cloud-native interests (eBPF, Gateway API, overlays, BGP).
- **What**: A full trace of a packet through a Kubernetes cluster — across nodes, overlays, policy, and egress — using Cilium as the dataplane, with live demos (from abstract only).
- **How**: Unpacks VXLAN/Geneve overlays, Gateway API, Egress Gateway, BGP routing, IPsec encryption, Direct Server Return, multi-cluster Cluster Mesh, plus performance features BIG TCP and topology-aware traffic engineering; observability via Hubble, Cilium CLI, and Wireshark.
- **Where applicable**: Cilium/Isovalent-centric but the K8s networking constructs (Gateway API, CNI, multicluster) are vendor-neutral; advanced session, assumes routing/overlay/LB fluency.

### Unifying Kubernetes and the Data Center: Isovalent Private Networks over EVPN/VXLAN - BRKDCN-3668

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362712043001qDWG)

Marcos Hernández (Cisco)

- **Why**: Bridges this PM's two worlds — K8s networking and DC EVPN fabric — with concrete control-plane and datapath mechanisms rather than hand-waving about "integration."
- **What**: A blueprint for integrating Isovalent Private Networks (Cilium-based K8s) with external EVPN/VXLAN fabrics, including underlay/overlay connectivity, BGP control-plane setup, EVPN route-type advertisements, VRF instantiation, and VTEP configuration on both sides (from abstract only).
- **How**: Details the specific route advertisements and datapath programming needed to stretch logical L2/L3 networks between Kubernetes and the Cisco fabric, and how the result supports distributed AI/ML application designs.
- **Where applicable**: Isovalent + Cisco NX-OS/ACI-style fabrics specifically; the EVPN-into-K8s pattern is generalizable to any CNI that can speak BGP/EVPN.

### Hijacking Trust: Weaponizing Stolen Cookies and Tokens - BRKSEC-2132

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362774923001qPab)

Stefan Duernberger (Cisco)

- **Why**: Session/token theft is the dominant real-world auth attack vector, and this session covers the modern defensive stack — passkeys, token binding, shared signals — directly on this PM's identity interests.
- **What**: How stolen cookies and tokens are weaponized, and the countermeasures: passkeys (FIDO/WebAuthn), OAuth 2.0 and OIDC flows, Google's Device-Bound Session Credentials (DBSC), Cisco Duo Passport, and the Shared Signals and Events (SSE) framework (from abstract only).
- **How**: Walks implementation of each mechanism and how they combine in a Zero Trust architecture to kill replayable bearer credentials.
- **Where applicable**: Standards-based and broadly applicable (DBSC is a browser standard-in-progress, SSE is OpenID Foundation work); the Duo Passport portion is product-specific.

### Reclaiming Your Agency: MCP, OAuth 2.1 and the Power to Automate Anything - BRKSEC-2065

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362772709001qwMt)

Jeremiah Williams (Cisco)

- **Why**: Agentic identity is an emerging core interest, and this is the standards-level session — MCP authorization, OAuth 2.1, fine-grained authorization — rather than a product pitch.
- **What**: How the emerging agentic-AI security stack works: Model Context Protocol (MCP), OAuth 2.1, fine-grained authorization, and related mechanisms for controlling what autonomous agents can access and do (from abstract only).
- **How**: Explores how these standards combine to give agents delegated, scoped, auditable access to business applications — and notes the same machinery applies to human identity.
- **Where applicable**: Standards-track and vendor-neutral (MCP, OAuth 2.1, fine-grained authz are IETF/OpenAI-ecosystem work); product agnosticism should be verified in the deck.

### Hunting the Invisible Army: Visibility for AI Agents & Non-human Identities - BRKSEC-2067

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362773161001qnZd)

Tal Kronrod (Cisco)

- **Why**: NHI explosion is the identity story of the cycle; traditional ITDR built for humans misses machine-speed, broad-permission identities.
- **What**: A framework and product demonstration (Cisco Identity Intelligence) for unified visibility and threat detection/response across service accounts, workloads, and autonomous AI agents in cloud, on-prem, and SaaS (from abstract only).
- **How**: Applies identity intelligence — correlating inherited permissions, credential usage, and behavior — to detect threats from NHIs that never trip human-focused anomaly detection.
- **Where applicable**: The NHI problem is universal, but the demo is Cisco's Identity Intelligence product; the framework's portability to other ITDR tooling should be probed.

### Your AI Agents Don't Talk to My AI Agents - Let's Fix That! - BRKETI-1009

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362727697001qJqy)

Sabitha Krishnamurthy (Cisco)

- **Why**: AGNTCY is a Linux Foundation open-source project defining agent interoperability infrastructure including *agent identity* — the federation/identity layer this PM tracks (analogous to SPIFFE's role for workloads).
- **What**: An introduction to the Internet of Agents and AGNTCY.org's four core technologies: agent directory, agent identity, SLIM messaging, and observability — the shared substrate for cross-environment agent discovery, trust, and communication (from abstract only).
- **How**: Technical overview plus practical multi-agent use cases demonstrated with shared code.
- **Where applicable**: Open-source (Linux Foundation) and cross-vendor by design; early-stage, so expect evolving specs rather than settled interfaces.

### Pig-in-the-Middle - TLS Decryption and Encrypted Visibility Engine Deep Dive on Cisco Secure Firewall - BRKSEC-3320

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362784581001qETL)

Carol Trincia Dsouza (Cisco)

- **Why**: Encrypted Client Hello plus post-quantum crypto is about to break passive TLS interception — a network-security sea change this PM needs to plan for.
- **What**: A deep dive on the modern encryption stack as seen from the firewall: ECH, domain fronting, evasive VPNs, fake TLS, QUIC decryption, and how the Encrypted Visibility Engine fingerprints the source process of an encrypted connection without decrypting anything (from abstract only).
- **How**: Live demos of decryption configuration (TLS and QUIC) and of encrypted-traffic analysis, including how a free CDN account can stack QUIC + ECH + encrypted DNS + post-quantum crypto into an opaque connection, and what that means for decryption policy.
- **Where applicable**: Cisco Secure Firewall product context, but the threat/visibility analysis (ECH, PQ, QUIC obfuscation) is broadly relevant to any TLS-inspecting security stack.

### Safeguarding the Internet's Backbone: Unleashing the Power of RPKI for Unbreakable IPv4 and IPv6 BGP Security - BRKENT-2179

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362724287001qciQ)

Jeffry Handal (Cisco), John Shea (Cisco)

- **Why**: RPKI deployment is the practical, deployable answer to BGP hijacking — core internet-routing security with direct DC/WAN interconnect relevance.
- **What**: Real-world BGP hijack incidents (criminal and nation-state) analyzed against what RPKI and related BGP capabilities would have prevented, plus deployment strategies and working configuration examples to start an RPKI rollout (from abstract only).
- **How**: Route Origin Validation mechanics, deployment patterns (full vs partial ROV), and complementary BGP security capabilities.
- **Where applicable**: Any organization operating BGP and announcing prefixes — vendor tooling is Cisco IOS-XR/IOS-XE but RPKI/RFC 6811 is standards-based and cross-vendor.

## Adjacent

### Control your destiny in the token-based AI economy with pluggable optics innovations - PSOMSI-1005

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362837016001q73e)

Ray Nering (Cisco), Yoav Schreiber (Cisco)

- **Why**: Down-ranked as a `PSO` product session, but it carries the substantive technology story behind Cisco's optics roadmap: silicon photonics, 1.6T pluggables, and Linear Pluggable Optics.
- **What**: How Cisco's 1.6T pluggable optics and Silicon Photonics serve AI back-end/front-end networks, and how LPO moves the DSP power draw from the module into the switch silicon (from abstract only).
- **How**: Details the power-efficiency mechanics of LPO on Silicon One G300 platforms (liquid- and air-cooled) and Cisco's field-reliability approach: qualification, test, and over-the-wire firmware updates across deployed optics fleets.
- **Where applicable**: Cisco-optics-specific; the LPO power trade-off (and its reach/reliability constraints) is an industry-wide decision point for anyone building 1.6T back-ends.

### AI Gave Every Attacker a Kubernetes Playbook. Isovalent Takes It Away - PSOSEC-2345

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362841100001qyhe)

Duffie Cooley (Cisco)

- **Why**: A `PSO` product pitch, but the underlying pattern — identity-aware (not IP-aware) network policy in K8s — is core to where this PM's cloud-native-security interests are heading.
- **What**: Demonstration of replacing IP-based K8s network policy with identity-aware enforcement via Cilium, plus process-level visibility and nano-segmentation via Isovalent Runtime Security, integrated with Splunk ES for ATT&CK-mapped detections (from abstract only).
- **How**: eBPF-based enforcement keyed to workload identity rather than IP/pod-label matching, catching east-west traffic that IP policies miss in ephemeral environments.
- **Where applicable**: Cilium/Isovalent-specific; the identity-based-policy concept generalizes, but the specific enforcement is tied to this stack.

### Zero Trust for Agents - PSOSEC-2344

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362840881001q8vP)

Tsailing Merrem (Cisco), Prabhu Barathi (Cisco)

- **Why**: Down-ranked from core: this is product-positioning for Cisco's Zero Trust portfolio applied to agents, and the more substantive agentic-identity coverage is in BRKSEC-2065 and BRKSEC-2067.
- **What**: The argument that autonomous agents become the "ultimate insider" without fine-grained authorization, and how Cisco is extending its Zero Trust access architecture to enforce scope, access control, and data security for an agentic workforce (from abstract only).
- **How**: Extends existing Zero Trust enforcement points (identity-aware proxy/access) to agent identities and their permitted actions rather than just access.
- **Where applicable**: Cisco Zero Trust portfolio-specific; useful mainly as a readout of how a major vendor plans to operationalize agent authorization.

### The New, QUIC Based Encrypted Protocol Stack Taking over the Internet and How to Deal with It - BRKSPM-2024

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362786699001qfwe)

Andreas Enotiadis (Cisco), Bart Van de Velde (Cisco)

- **Why**: Adjacent rather than core because of its service-provider framing, but the QUIC/HTTP-3/DoH/ECH stack it describes is the same visibility threat covered in BRKSEC-3320, with protocol-internals depth.
- **What**: How the QUIC-based stack (QUIC + HTTP/3 + DoH + eSNI/ECH) is constructed and evolving — already claimed at ~50% of traffic and doubling every 18 months — and why it obsoletes the assumptions SP networks are built on: encryption kills application visibility, and congestion management moves into the application (from abstract only).
- **How**: Analysis of the stack's visibility and flow-control behavior plus SP-side countermeasures for traffic visibility, QoE monitoring, and efficient use of scarce resources like 5G spectrum.
- **Where applicable**: SP networks primarily; the protocol analysis applies to any operator of middleboxes and QoS infrastructure facing QUIC traffic.

## Wildcard

### A Quantum Leap in Networking: Cisco's Blueprint for Tomorrow's Infrastructure - CENETI-1281

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780412374240001Hi1c)

Ramana Kompella (Cisco)

- **Why**: Not a fit for daily work, but a credible roadmap signal: Cisco is committing to quantum networking on a ~5-year horizon, with named artifacts and partners.
- **What**: Cisco's quantum networking vision and concrete pieces: the Quantum Network Entanglement Chip and a Network-Aware Quantum Compiler, plus how quantum capabilities augment classical systems today and the IBM partnership (from abstract only).
- **How**: Entanglement distribution hardware plus a compiler that maps quantum programs onto network topology — the beginning of a distributed-quantum-systems networking stack.
- **Where applicable**: Early research/vendor-vision stage; treat as strategic sensing, not deployable technology.

### The Network Capability AI Has Been Waiting For - BRKPAR-1026

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362764339001q4nI)

Nikhil Handigol (Forward)

- **Why**: A partner session, but it points at a genuinely novel operational pattern: a mathematically accurate network digital twin as the *reasoning layer* for both human changes and autonomous AI agents.
- **What**: Demonstration of pre-deployment verification of routing and firewall changes on a formal network model, catching regressions before production, and automated end-to-end impact assessment replacing manual approval cycles (from abstract only).
- **How**: Formal verification of network state and behavior (the Forward Networks model-checking lineage) applied as the guardrail that lets AI agents act on production networks with verified-before-risk confidence.
- **Where applicable**: Formal-model based, vendor- and device-neutral in principle (Forward ingests multi-vendor configs); the AI-agent-trust framing is early but directly relevant to where network automation is heading.

### Failure Patterns in Modern Distributed Systems: Lessons from Major Internet Outages - BRKOPS-2000

**Links:** [Abstract](https://www.ciscolive.com/on-demand/on-demand-library.html#/session/1780362756585001qYP0)

Mike Hicks (Cisco)

- **Why**: Outside the core interests, but a 90-minute analysis of real major outages (cloud providers, collaboration platforms, CDNs) with repeatable forensic patterns is high-value for anyone designing resilient distributed infrastructure.
- **What**: Three failure patterns distilled from major incidents: coordination features becoming failure-distribution mechanisms, systems that look healthy while core functions silently break, and config changes cascading across interconnected systems (from abstract only).
- **How**: Case-study walkthroughs using the ThousandEyes MCP server and its analytical framework to surface, interrogate, and codify patterns from real incident data — turning raw telemetry into repeatable forensic methodology. Led by the Principal Analyst behind The Internet Report.
- **Where applicable**: Pattern-level and broadly applicable; the MCP-server-driven analysis is itself an early example of AI-tooling-assisted incident forensics.

## Themes

- **AI fabrics dominate the physical-networking agenda**: Nearly every DC session is now framed around AI training/inference — RoCEv2 lossless back-ends, 64K–200K+ GPU topologies (leaf-spine → DSF → three-tier), scale-up vs. scale-out split, and DCI at 1 ms RTT. "Regular" DC fabric sessions (VXLAN EVPN internals, multihoming) persist but are the legacy track.
- **Optics is the next capacity battleground**: 800G/1.6T pluggables, new Ethernet speeds standardization, LPO moving DSPs into switch silicon, and co-packaged optics all appear — power per bit is the binding constraint on AI cluster economics.
- **eBPF/Cilium is now Cisco's cloud-native wedge**: Isovalent-derived sessions span datapath internals, EVPN fabric integration, and security, signaling that host-networking and the DC fabric are being re-converged at the K8s layer.
- **Agentic identity is the breakout topic of the cycle**: Four sessions cover it from different angles — standards (MCP/OAuth 2.1), NHI visibility/ITDR, zero-trust enforcement, and open-source federation (AGNTCY agent identity). The workload-identity problem is being re-litigated for agents.
- **Encryption is winning against the middlebox**: ECH, QUIC, encrypted DNS, and post-quantum crypto are forcing a shift from bulk decryption toward metadata fingerprinting and identity-based controls — two sessions confront this directly.
- **SONiC and open standards are the credibility markers**: Even at a vendor conference, sessions foreground SONiC troubleshooting, AGNTCY/Linux Foundation work, and "open, standards-aligned" AI fabric benchmarking — open-ecosystem positioning is now expected, not exceptional.
