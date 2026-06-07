---
conference: ACM SIGCOMM 2025 (Coimbra)
type: academic
source_url: https://conferences.sigcomm.org/sigcomm/2025/program/papers-info/
generated: 2026-06-07
registry_key: sigcomm-2025
---

# SIGCOMM 2025 Digest

A note up front: this is a heavily AI-infrastructure and datacenter-transport cycle. For a PM in cloud-native networking, security, and identity, the program is thinner on direct hits (eBPF/Cilium/Kubernetes/service mesh/identity) than on adjacent datacenter and WAN systems work. I've prioritized accordingly — picks that touch the datapath, programmable switches, eBPF, service mesh, verification, and PKI/identity rank highest, and I've been willing to reach into satellite/measurement work for genuine novelty rather than pad the Core tier.

## Core

**Hermes: Enhancing Layer-7 Cloud Load Balancers with Userspace-Directed I/O Event Notification** — Tian Pan et al. (Alibaba Cloud)
Uses eBPF to override kernel reuseport socket selection so userspace worker health drives kernel connection dispatch, fixing epoll-exclusive LIFO skew and reuseport's unawareness of worker liveness. Directly relevant: this is eBPF-on-the-datapath solving an L7 LB load-distribution problem at 33-region scale, with real production deltas (99.8% fewer worker hangs). The reuseport-steering technique transfers to anyone building Envoy/proxy fleets.
Tier: Core

**HardMesh: Enabling High-performance Service Mesh Ingress Processing with SmartNICs** — Myoungsung You et al. (U. Seoul, Dankook, ETRI, Chonnam, KAIST)
Offloads service-mesh ingress-gateway traffic analysis and routing to a SmartNIC with a thin CPU proxy for management, claiming ~4.4x throughput. The ingress gateway as the mesh's CPU bottleneck is a problem the PM lives with; this is a concrete hardware-offload data point even if the SmartNIC dependency limits portability.
Tier: Core

**Scallop: Scalable Video Conferencing Using SDN Principles** — Oliver Michel et al. (Princeton, UVA)
Splits an SFU into a Tofino/BlueField-3 hardware data plane for frequent media forwarding/dropping and a software control plane for session logic, claiming 7-422x scaling. The SDN-style control/data-plane decomposition on programmable switches and SmartNICs is the transferable idea, applicable well beyond WebRTC to any high-fan-out packet relay.
Tier: Core

**SpliDT: Partitioned Decision Trees for Scalable Stateful Inference at Line Rate** — Murayyiam Parvez et al. (Purdue, Michigan, UCSB, Open U. Israel, NIKSUN)
Partitions decision-tree inference into sequential subtrees over a sliding packet window using packet recirculation, supporting stateful per-flow features without blowing RMT resource limits. For in-network security monitoring at line rate this is the most architecturally honest of the data-plane-ML papers — it confronts the feature-state constraint head-on rather than assuming all features upfront.
Tier: Core

**Achieving High-Speed and Robust Encrypted Traffic Anomaly Detection with Programmable Switches (Mazu)** — Han Zhang et al. (Tsinghua, Peking U., Sangfor, China Telecom)
Inline NIDS on programmable switches using dual-plane feature extraction plus a one-class model trained only on benign traffic, with online model updates, deployed two years across two ISPs. A real production line-rate detection system for encrypted traffic — directly relevant to network security, and the benign-only one-class framing is a sensible answer to label scarcity.
Tier: Core

**The Sweet Danger of Sugar: Debunking Representation Learning for Encrypted Traffic Classification** — Yuqi Zhao et al. (Politecnico di Torino)
Shows that BERT-style encrypted-traffic classifiers hit ~98% accuracy mostly via dataset shortcuts/spurious correlations that vanish in realistic settings, and proposes a correct evaluation methodology. Essential skepticism for anyone evaluating ML-based traffic classification or security tooling — it tells the PM which vendor accuracy claims to distrust and why.
Tier: Core

**SDP: Designing Transport-Level Encryption for Datacenter Networks** — Tianyi Gao et al. (U. Edinburgh)
A short proposing transport-level encryption for next-gen DC transports (NDP, Homa) with TLS-style NIC offload, a native protocol number, and message-based abstraction for low-latency RPC. Relevant to where datacenter transport security is heading; the abstract is thin (it's a short paper), so treat as a direction-setter rather than a finished design.
Tier: Core

**RevDNS: Reliable and Decentralized Certificate Revocation via DNS** — Protick Bhowmick, Dave Levin, Taejoong Chung (Virginia Tech, U. Maryland)
Publishes revoked serials in DNSSEC-signed TXT records with NSEC negative caching so resolvers answer ~99.8% of revocation checks without hitting a CA, countering the Akamai-serves-62%-of-OCSP recentralization. Direct PKI/identity relevance: a concrete alternative to OCSP and short-lived certs that touches web-PKI trust assumptions the PM tracks.
Tier: Core

## Adjacent

**Falcon: A Reliable, Low Latency Hardware Transport** — Arjun Singhvi, Nandita Dukkipati et al. (Google, with Meta/Nvidia/Microsoft co-authors)
A multi-ULP hardware transport for general-purpose lossy Ethernet (delay-based CC, multipath, hardware retransmit), positioned against RoCE's PFC dependence. Matters as a likely-influential industry transport standard-in-waiting; the multi-vendor authorship signals ecosystem direction for datacenter NIC transport.
Tier: Adjacent

**Revisiting RDMA Reliability for Lossy Fabrics (DCP)** — Wenxue Li et al. (HKUST, Huawei)
Co-designs switch and RNIC for PFC-independent, RTO-free, packet-spray-compatible RDMA reliability via header-only retransmission and bitmap-free tracking. The broader theme — making RDMA work without lossless/PFC — is the one to track; this is one of several strong entries in it.
Tier: Adjacent

**ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud** — Yirui Liu et al. (ByteDance)
A vNIC design carrying both RDMA and TCP inside a VPC overlay with QoS and security-group support, deployed a year in production. Relevant to cloud-native networking: it shows how VPC abstractions (security groups, QoS) extend to RDMA tenants — an overlay/multi-tenancy concern the PM will recognize.
Tier: Adjacent

**Confucius: Intent-Driven Network Management with Multi-Agent LLMs** — Zhaodong Wang et al. (Meta, Johns Hopkins, Harvard, Stony Brook)
Production multi-agent LLM framework modeling network-management workflows as DAGs with RAG memory and tight integration to existing validation, 60+ apps over two years at Meta. The first credible hyperscale report on multi-agent LLMs for network ops — useful signal on agentic operations, an area adjacent to the PM's agentic-identity interest.
Tier: Adjacent

**Centralium: A Hybrid Route-Planning Framework for Large-Scale Data Center Network Migrations** — Yikai Lin et al. (Meta, UMass)
Augments BGP with a Route Planning Abstraction enabling centralized planning with distributed enforcement for staged DC migrations. For anyone living in BGP datapath/migration pain, the abstraction (encoding sequential + spatial migration conditions BGP can't express) is the takeaway.
Tier: Adjacent

**ZENITH: Towards A Formally Verified Highly-Available Control Plane** — Pooria Namyar et al. (USC, Google)
A microservice SDN controller that avoids state inconsistency by design, with a machine-verified spec and code generated from it, resolving inconsistencies 5x faster than reconciliation-based designs. Relevant to Kubernetes-style reconciliation thinking — the "correct by construction vs. periodic reconcile" argument maps directly onto controller design debates the PM will know.
Tier: Adjacent

**S2: A Distributed Configuration Verifier for Hyper-Scale Networks** — Dan Wang et al. (Xi'an Jiaotong, Northwest U., ByteDance)
Scales config verification beyond a single server by partitioning the network model across machines (built on Batfish), reaching 10K routers / 1000M routes. Config verification is operationally adjacent; the scale-out approach matters if the PM's environment outgrew single-box Batfish.
Tier: Adjacent

**Formalizing Dependence of Web Infrastructure** — Rumaisa Habib, Kimberly Ruth, Gautam Akiwate, Zakir Durumeric (Stanford)
A rigorous statistical metric for Internet centralization that disentangles centralization from regionalization across hosting, DNS, and CAs in 150 countries. Relevant to identity/PKI through the CA-dependence lens, and to resilience reasoning generally. (Note: program text for this paper and the "Hummingbird" entry is identical to this centralization abstract — Hummingbird's listed title is about bandwidth reservations, so its abstract appears mis-pasted; flagging rather than guessing.)
Tier: Adjacent

**Censys: A Map of Internet Hosts and Services** — Zakir Durumeric et al. (Censys Inc.)
A retrospective on Censys's re-architecture for continuous Internet-wide scan data collection, with visibility evaluation and lessons. Useful infrastructure context for attack-surface and security-measurement work the PM tracks adjacent to network security.
Tier: Adjacent

## Wildcard

**Orderlock: A New Type of Deadlock and its Implications on High Performance Network Protocol Design** — Weihao Jiang et al. (SJTU, Nanjing U.)
Proves that in-order delivery + lossless transmission + out-of-order capability are jointly impossible without risking a new deadlock class ("Orderlock"), and explores Orderlock-free protocol designs. A genuine impossibility result that reshapes how to reason about HPN protocol/hardware co-design — the kind of conceptual lever that outlasts any single benchmark.
Tier: Wildcard

**Direct-to-Cell Satellite Network without Satellite Navigation (SN²)** — Wei Liu et al. (Tsinghua)
Shows direct-to-cell satellite networks' over-reliance on GNSS for geolocation/timing causes mis-billing, unauthorized service, and denials, and proposes self-navigation from the satellites themselves. Wildcard because the failure mode is fundamentally an authn/authz-and-location problem in disguise — GNSS as an implicit trust dependency for access control is a framing the identity-minded PM will appreciate.
Tier: Wildcard

**TinyLEO: Small-scale LEO Satellite Networking for Global-scale Demands** — Yuanjie Li et al. (Tsinghua)
Argues mega-constellations massively over-provision relative to uneven real demand, and uses spatiotemporal supply-demand matching to shrink the needed constellation 2-7.9x. Wildcard for the contrarian thesis — a supply-demand-matching argument against brute-force scaling that's intellectually transferable to capacity planning well beyond space.
Tier: Wildcard

**Firefly: Scalable, Ultra-Accurate Clock Synchronization for Datacenters** — Pooria Namyar et al. (Google, USC, NVIDIA)
Software-driven distributed-consensus clock sync hitting sub-10ns device-to-device and ≤1µs-to-UTC, with "layered synchronization" decoupling internal and external sync. Wildcard because precise time is quietly foundational — for distributed consistency, certificate/token validity windows, and ordering — and sub-10ns in software is a striking result with reach into security and distributed systems.
Tier: Wildcard

## Themes

- **AI training/inference infrastructure dominates.** A large share of the program is GPU-cluster networking: collective-communication scheduling (SyCCL, ResCCL, Hermod), MoE serving (MegaScale-Infer, MixNet), HBD/optical fabrics (InfiniteHBD, Mosaic), and RDMA for AI (Stellar). The center of gravity in systems networking has clearly shifted to the AI datapath.

- **RDMA without lossless/PFC is a live front.** Multiple independent teams (DCP, Falcon, Jakiro) are converging on making RDMA reliable over lossy, general-purpose Ethernet and across multi-tenant VPCs — the PFC-dependence escape is this cycle's recurring transport problem.

- **In-network ML, with a reality check.** Pushing decision trees and DL onto programmable switches/SmartNICs is widespread (SpliDT, Pegasus, Mazu, NPC), but "Sugar" lands a needed methodological broadside on how these models are evaluated — enthusiasm and skepticism arriving in the same program.

- **LLMs for operating networks.** Confucius, BIAN, and SkyNet mark a turn toward LLM/agentic assistance for diagnosis, failure localization, and intent-driven management at hyperscale — early but production-grounded.

- **Verification and correctness-by-construction.** ZENITH, S2, and Hoyan show formal/verification methods maturing from single-box tools to distributed, production-deployed systems — a quiet but consequential trend for reliability.

- **Satellites grew up.** LEO networking moved from feasibility to economics, security, and architecture (TinyLEO, SN², StarCDN, SaTE, LeoCC), including the recognition that satellite access control inherits GNSS's trust and failure properties.

A caveat on what's *not* here: there's little direct passkeys/FIDO/OAuth/OIDC or SPIFFE/SPIRE work — SIGCOMM remains a systems/datapath venue, so the identity-relevant picks (RevDNS, SN², the centralization papers) come at it from the PKI/trust-dependency angle rather than authn protocols.
