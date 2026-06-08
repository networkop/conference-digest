---
conference: ACM SIGCOMM 2025 (Coimbra)
type: academic
source_url: https://conferences.sigcomm.org/sigcomm/2025/program/papers-info/
generated: 2026-06-07
registry_key: sigcomm-2025
---

# SIGCOMM 2025 Digest

This is an AI-infrastructure-heavy cycle, and with physical DC/WAN systems treated as core, the program yields a strong Core tier: optics and topology, RDMA/lossless fabrics, hardware transports, programmable-dataplane work, and cloud-native datapath all land squarely in scope. I've pushed pure LLM-serving-algorithm and application-QoE work down or out, and reserved Wildcards for genuinely off-axis novelty.

## Core

### Mosaic: Breaking the Optics versus Copper Trade-off with a Wide-and-Slow Architecture and MicroLEDs — Kaoutar Benyahya et al. (Microsoft Research / Microsoft Azure) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750510 · video https://youtu.be/nMJuK_3_0Hw
**Why:** Link reach/power/reliability is the binding constraint on future DC fabric scaling; this directly targets the copper-vs-optics wall the PM cares about.
**What:** A new link technology that abandons the few-high-speed-channels model for hundreds of parallel low-speed channels, claiming copper-beating reach at up to 69% lower power and better reliability than current optics.
**How:** "Wide-and-slow" spatial multiplexing using directly-modulated microLEDs (not lasers) over massively multi-core imaging fibers, eliminating laser drivers and complex electronics; prototype shows 100 channels × 2Gbps scaling toward 800Gbps+ at up to 50m.
**Where applicable:** Protocol-agnostic and designed to drop in without server/switch changes — broadly applicable in principle, but still a research prototype, not a shipping transceiver.

### InfiniteHBD: Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers — Chenchen Shou et al. (Peking U. / StepFun / Lightelligence) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750468 · video https://youtu.be/d4PX36vVDX0
**Why:** HBD architecture (NVL-72 vs TPU-style) is a live topology/cost/fault-domain debate; this proposes a genuinely different point in that space.
**What:** A transceiver-centric HBD that embeds optical circuit switching into each transceiver, giving reconfigurable point-to-multipoint links and variable-size ring topologies at ~31% of NVL-72 cost with node-level fault isolation.
**How:** A silicon-photonic OCS transceiver (OCSTrx), a reconfigurable k-hop ring topology, and an HBD-DCN orchestration algorithm; evaluation claims near-zero GPU waste and 3.37x MFU vs DGX.
**Where applicable:** Aimed at LLM-training fabrics; depends on custom silicon-photonic transceivers, so it's a direction/architecture signal rather than commodity-deployable today.

### Falcon: A Reliable, Low Latency Hardware Transport — Arjun Singhvi, Nandita Dukkipati et al. (Google, with Meta/Nvidia/Microsoft) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3754353 · video https://youtu.be/nu18DsuvnlU
**Why:** RoCE's PFC/special-fabric dependence limits where hardware transport can go; a multi-vendor general-purpose alternative is strategically significant for DC NIC direction.
**What:** The first hardware transport supporting multiple Upper Layer Protocols and heterogeneous workloads on lossy, general-purpose Ethernet without special switch support.
**How:** Delay-based congestion control with multipath load balancing, a layered request-response transaction interface for multi-ULP support, hardware retransmission/error handling, and a programmable engine; first implementation hits 200 Gbps / 120 Mops/sec with op-completion up to 8x lower than CX-7 RoCE under congestion.
**Where applicable:** Broad ambition (general Ethernet DC), but it's hardware transport — realization depends on NIC silicon adoption; the cross-vendor authorship is itself the signal.

### Revisiting RDMA Reliability for Lossy Fabrics (DCP) — Wenxue Li et al. (HKUST, Huawei) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750480 · video https://youtu.be/4CgsjKMJ1Ns
**Why:** Getting RDMA off PFC/lossless is one of the cycle's central transport problems and directly relevant to lossless-fabric work.
**What:** A switch+RNIC co-designed transport that is PFC-independent, RTO-free, packet-spray-compatible, and offload-friendly, claiming 1.6x/2.1x gains over SOTA lossless/lossy RDMA.
**How:** DCP-Switch adds a simple lossless control plane that DCP-RNIC uses for header-only-based retransmission and bitmap-free packet tracking; prototyped on Tofino2 + FPGA.
**Where applicable:** General DC RDMA technique, but requires coordinated switch and RNIC changes (prototype silicon), so deployment implies a fabric+NIC co-upgrade.

### Alibaba Stellar: A New Generation RDMA Network for Cloud AI — Jie Lu et al. (Alibaba Cloud) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750539 · video https://youtu.be/eWjhga2d0uQ
**Why:** RDMA virtualization (SR-IOV) pain — slow container spin-up, resource limits, traffic steering — is exactly the multi-tenant cloud-AI networking the PM works on.
**What:** A production RDMA virtualization stack that spins up virtual devices in seconds, cuts container init time 73%, and improves LLM training speed up to 14%.
**How:** Para-Virtualized DMA (PVDMA) for on-demand memory pinning, an extended Memory Translation Table (eMTT) for GPUDirect RDMA performance, and RDMA Packet Spray for multipath.
**Where applicable:** Alibaba-specific production setup; the PVDMA/eMTT ideas generalize but the numbers are from their cluster.

### ByteDance Jakiro: Enabling RDMA and TCP over Virtual Private Cloud — Yirui Liu et al. (ByteDance) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750496 · video https://youtu.be/gh13ILZGY1s
**Why:** Carrying RDMA and TCP over one VPC overlay with real VPC semantics (security groups, QoS) is a concrete cloud-native multi-tenancy problem.
**What:** A vNIC design supporting both RDMA and TCP inside a VPC with QoS and security-group enforcement, near-physical RDMA performance, deployed a year in production.
**How:** A unified vNIC framework that applies VPC features to both stream types while staying compatible with intra-host RDMA optimizations and guaranteeing weighted-fair QoS between RDMA and TCP.
**Where applicable:** ByteDance-specific production VPC; the dual-stack-over-one-overlay pattern transfers, the deployment specifics don't.

### From ATOP to ZCube: Automated Topology Optimization Pipeline and a Cost-Effective Topology for Large Model Training — Zihan Yan, Dan Li et al. (Tsinghua, Zhongguancun Lab, ByteDance) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750503 · video https://youtu.be/7fVx3b1T_dc
**Why:** DC topology design for training clusters is core physical-networking work, and an automated search plus a concrete new topology is more useful than another hand-tuned fabric.
**What:** A pipeline that treats topology as hyperparameters to search at tens-of-thousands-of-GPU scale, yielding ZCube, which claims 3–7% faster training and 26–46% lower hardware cost vs ROFT/Rail-only/HPN.
**How:** Models topology as an optimization problem over training traffic, collective performance, fault tolerance, and cost; evaluated in build/optimize/expand scenarios and validated on a real testbed (25% cost cut vs rail-optimized).
**Where applicable:** General topology-design methodology for GPU clusters; results are simulation-heavy with a testbed check.

### Unlocking Superior Performance in Reconfigurable DCNs with Credit-Based Transport (Flare) — Federico De Marchi et al. (MPI-INF, Meta, NVIDIA) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3754342 · video https://youtu.be/l_NMFMrbRGM
**Why:** Reconfigurable (microsecond-switched) DCNs are a credible post-Moore alternative to Clos, but transport has been the gap; this closes part of it.
**What:** A credit-based transport that lets RDCNs beat Clos on throughput (up to 1.15x even under adversarial traffic) and substantially cut flow completion times vs NDP/ExpressPass/TDTCP/Bolt.
**How:** Reliable credit-based delivery that opportunistically routes over the RDCN's rapidly reconfiguring short-path circuits; testbed on programmable switches + DPDK.
**Where applicable:** Applies to reconfigurable-DCN designs specifically — relevant if/when RDCNs are on the table; mostly simulation plus a feasibility testbed.

### Hermes: Enhancing Layer-7 Cloud Load Balancers with Userspace-Directed I/O Event Notification — Tian Pan et al. (Alibaba Cloud) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750469 · video https://youtu.be/J22-2PSf04M
**Why:** eBPF on the datapath solving a real L7 LB connection-distribution problem (epoll-exclusive LIFO skew, reuseport blindness to worker health) is squarely cloud-native networking.
**What:** A framework making userspace worker status drive kernel connection dispatch, deployed on O(100K) cores across 33 Alibaba regions, cutting daily worker hangs 99.8% and L7 LB unit cost 18.9%.
**How:** Lock-free worker-status management plus eBPF overriding reuseport socket selection in a closed loop from userspace to kernel.
**Where applicable:** General Linux/eBPF technique usable in any Envoy/proxy-style fleet; the scale numbers are Alibaba-specific.

### Centralium: A Hybrid Route-Planning Framework for Large-Scale DC Network Migrations — Yikai Lin et al. (Meta, UMass) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750519 · video https://youtu.be/HMbq49xGDcg
**Why:** BGP datapath/migration pain is a real operational problem; native BGP can't express the staged, topology-aware conditions migrations need.
**What:** A Route Planning Abstraction augmenting BGP for centralized planning with distributed enforcement, with 10+ production migration use cases and a substantial reduction in migration time/risk.
**How:** RPA encodes both sequential and spatial migration conditions BGP can't, driven by a centralized controller deployed alongside existing BGP.
**Where applicable:** Meta-specific deployment but the abstraction generalizes to any large BGP-routed DC facing migrations.

### Fornax: A Hardware-Centric Session Management in Large Public Cloud Network — Heng Yu et al. (Zhongguancun Lab, Tencent, Peking U.) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750501 · video https://youtu.be/dAQuu8Oh2r8
**Why:** SmartNIC-accelerated cloud network functions live or die on their management mechanism; flow-as-unit, one-way command models don't scale to huge tables.
**What:** A shift from software-centric to hardware-centric management using session (not flow) as the unit, managing up to 16M sessions while cutting software storage 80% and CPU 77%.
**How:** A session-empowered hardware engine plus two-way hardware-driven management protocols and a lightweight software manager for scalability.
**Where applicable:** Tencent-specific SmartNIC production setup; the session-as-unit + two-way-protocol idea is a transferable design principle.

### Software-based Live Migration for RDMA (MigrRDMA) — Xiaoyu Li et al. (Tsinghua / Microsoft Research) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750487 · video https://youtu.be/_JTZhc6wYxo
**Why:** RDMA live migration has been "needs NIC support, never ships"; doing it in software on commodity RNICs unblocks host maintenance without hardware changes.
**What:** A software RDMA live-migration layer with little downtime and only 3–9% datapath overhead, adding ~3s to migrated Hadoop job completion.
**How:** A software indirection layer that keeps RDMA state identical across source and destination from the application's view, enabling transparent switchover; prototyped on Mellanox RNICs.
**Where applicable:** General technique on commodity RNICs (validated on Mellanox) — broadly relevant to anyone running RDMA workloads in VMs/containers.

### Achieving High-Speed and Robust Encrypted Traffic Anomaly Detection with Programmable Switches (Mazu) — Han Zhang et al. (Tsinghua, Peking U., Sangfor, China Telecom) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750493 · video https://youtu.be/u9a0ygqsgKs?t=1302
**Why:** Inline line-rate NIDS for encrypted traffic is a core network-security capability, and this one is production-proven across two ISPs over two years.
**What:** An inline switch-based IDS detecting malicious traffic at ~90% accuracy within minutes, having caught 10+ critical attack events protecting 10M+ servers.
**How:** A dual-plane feature-extraction model at near line speed plus a one-class classifier trained only on benign traffic, with an online update mechanism for drift.
**Where applicable:** ISP/data-center-edge deployment on programmable switches; benign-only training is a sensible general answer to label scarcity.

### SpliDT: Partitioned Decision Trees for Scalable Stateful Inference at Line Rate — Murayyiam Parvez et al. (Purdue, Michigan, UCSB, Open U. Israel, NIKSUN) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750475 · video https://youtu.be/u9a0ygqsgKs?t=356
**Why:** In-network ML for security monitoring usually assumes all features upfront; this confronts the data-plane stateful-feature constraint honestly.
**What:** A framework supporting up to 5x more stateful features and scaling to millions of flows by partitioning decision-tree inference over a sliding packet window.
**How:** Sequential subtrees each using their own top-k features, with an in-band control channel via packet recirculation managing transitions and reusing match keys/registers; a joint training/DSE workflow optimizes feature allocation, depth, and partitioning.
**Where applicable:** RMT programmable switches/SmartNICs; a general data-plane-ML technique constrained by switch resources.

### RevDNS: Reliable and Decentralized Certificate Revocation via DNS — Protick Bhowmick, Dave Levin, Taejoong Chung (Virginia Tech, U. Maryland) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3754351 · video https://youtu.be/hXASMw1JL8M
**Why:** Web-PKI revocation is broken and OCSP-over-CDN recentralizes trust (Akamai serves ~62% of revocation responses) — directly relevant to the PM's PKI/identity interest.
**What:** A DNS-based revocation scheme where resolvers answer ~99.8% of checks locally without contacting a CA, with no added latency and no extra user disclosure.
**How:** Revoked serials live in DNSSEC-signed TXT records; NSEC proofs enable aggressive negative caching; a large CA like Let's Encrypt can publish 612M certificates in a 345MB zone.
**Where applicable:** General web-PKI proposal; a concrete alternative to OCSP and short-lived certs that keeps revocation authority with CAs.

### Designing Transport-Level Encryption for Datacenter Networks (SDP) — Tianyi Gao et al. (University of Edinburgh) — Core
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750482 · video https://youtu.be/u9a0ygqsgKs?t=933
**Why:** Encryption for next-gen DC transports (NDP, Homa) is where DC transport security is heading; touches both fabric and security.
**What:** A protocol design integrating data encryption into emerging datacenter transports with TLS-style NIC offload.
**How:** Supports NIC offloading modeled on TLS-over-TCP, a native protocol number alongside TCP/UDP, and a message-based abstraction for low-latency parallel RPCs. (Short paper — abstract is thin; treat as a direction-setter, not a finished design.)
**Where applicable:** General DC-transport proposal; early-stage.

## Adjacent

### ZENITH: Towards a Formally Verified Highly-Available Control Plane — Pooria Namyar et al. (USC, Google) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750533 · video https://youtu.be/Q7zdDgZ3IKA
**Why:** The "correct-by-construction vs. periodic reconcile" argument maps directly onto Kubernetes-style controller design the PM will recognize.
**What:** A microservice SDN controller that avoids state inconsistency by design, machine-verified, resolving inconsistencies 5x faster than reconciliation-based designs.
**How:** A formally verified specification with code auto-generated from it, plus abstractions letting developers independently verify SDN apps.
**Where applicable:** SDN control planes; the design philosophy generalizes to any reconciler-based system.

### S2: A Distributed Configuration Verifier for Hyper-Scale Networks — Dan Wang et al. (Xi'an Jiaotong, Northwest U., ByteDance) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750516 · video https://youtu.be/r6Y73NGaQBw
**Why:** Config verification is operationally adjacent; single-box verifiers stall past ~10K switches / 1000M routes that large providers actually run.
**What:** A scale-out verifier reaching 10K routers and 1000M routes within 2 hours by distributing across servers.
**How:** Partitions the network model and distributes control-plane simulation + data-plane verification across machines, with prefix sharding to cut per-server memory; built on Batfish.
**Where applicable:** Large service-provider/DC networks that outgrew single-server Batfish; general approach.

### New Evolution of Hoyan: Alibaba's Global WAN Verification — Yifei Yuan et al. (Alibaba Cloud) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3754343 · video https://youtu.be/M8lJ0pIhWRY
**Why:** A multi-year production verification story with hard before/after numbers (misconfig incidents 56% → 5%) is the kind of operational evidence worth seeing.
**What:** A distributed evolution of Hoyan scaling to O(10^4) routers, millions of prefixes, billions of flows, plus a route-change-intent specification language (RCL).
**How:** Centralized-to-distributed simulation (5x faster), RCL for expressing/verifying route-change intents, and an enhanced accuracy-diagnosis framework.
**Where applicable:** Alibaba-specific WAN, but the RCL idea and the distributed-simulation approach transfer.

### PreTE: Traffic Engineering with Predictive Failures — Congcong Miao et al. (Tencent, MIT, UCSB, Meta, Tsinghua) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750508 · video https://youtu.be/nO7oHxImwiQ
**Why:** Fiber cuts are rare-but-disruptive WAN events; folding measured optical-layer degradation into TE is a fresh, physically grounded angle on availability.
**What:** A TE system that factors dynamic fiber-cut probabilities into tunnel planning, supporting up to 2x more demand at equal availability.
**How:** Per-second optical-layer measurements show failure probability jumps orders of magnitude in an ephemeral degradation state; PreTE predicts from that and proactively updates tunnels then re-optimizes allocation.
**Where applicable:** WAN operators with optical-layer telemetry; assumes access to per-second optical data.

### Confucius: Intent-Driven Network Management with Multi-Agent LLMs — Zhaodong Wang et al. (Meta, JHU, Harvard, Stony Brook) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750537 · video https://youtu.be/QpCXjseK0HQ
**Why:** First credible hyperscale report on multi-agent LLMs for network ops — useful signal on agentic operations adjacent to the PM's agentic-identity interest.
**What:** A production multi-agent framework, operational two years with 60+ apps, modeling management workflows as DAGs.
**How:** LLMs integrated with existing tools, RAG for long-term memory, human/model interaction primitives, and tight coupling to existing validation to prevent regressions.
**Where applicable:** Meta-scale ops; the architecture is a reference point for agentic network management generally.

### Understanding and Profiling CXL.mem Using PathFinder — Xiao Li et al. (UW-Madison/Beihang, Intel) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750479 · video https://youtu.be/PHqrdRGRfD4
**Why:** CXL memory pooling is becoming widely deployed and can stall co-located apps; the community lacks end-to-end profiling, which matters for DC resource disaggregation.
**What:** A utility that captures CXL.mem execution end-to-end between CPU and remote DIMM for profiling, bottleneck analysis, and anomaly diagnosis.
**How:** Models the CXL.mem data path as an execution graph from architectural performance counters and applies graph analysis to associate CXL with competing memory flows.
**Where applicable:** Servers with CXL.mem; a general diagnostic tool, increasingly relevant as memory disaggregation lands.

### Censys: A Map of Internet Hosts and Services — Zakir Durumeric et al. (Censys Inc.) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3754344 · video https://youtu.be/FnqvaE6BhuQ
**Why:** Attack-surface and security-measurement context the PM tracks adjacent to network security.
**What:** A retrospective on Censys's re-architecture for continuous Internet-wide scan data, with a visibility evaluation and lessons learned.
**How:** Operational account of redesigning collection/packaging and serving research/industry/government users; discusses unsolved problems.
**Where applicable:** Internet-measurement infrastructure; general reference.

### Formalizing Dependence of Web Infrastructure — Rumaisa Habib, Kimberly Ruth, Gautam Akiwate, Zakir Durumeric (Stanford) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750492 · video https://www.youtube.com/watch?v=JDVmpjl-u1E
**Why:** Relevant to identity/PKI via the CA-dependence lens and to resilience reasoning generally.
**What:** A rigorous statistical metric for Internet centralization that disentangles centralization from regionalization across hosting, DNS, and CAs in 150 countries.
**How:** A suite of statistical tools applied across three web-infrastructure layers.
**Where applicable:** General measurement/policy toolkit. (Note: the program text for "Hummingbird: Fast, Flexible, and Fair Inter-Domain Bandwidth Reservations" is an identical copy of this centralization abstract — Hummingbird's title is about bandwidth reservations, so its abstract appears mis-pasted in the program; flagging rather than guessing its content.)

### Threading the Ocean: Mapping Digital Routes Across Submarine Cables using Calypso — Caleb Wang et al. (Northwestern, U. Oregon) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750512 · video https://youtu.be/u9a0ygqsgKs?t=1724
**Why:** Submarine cables are the physical WAN backbone with real security/economic exposure; mapping traffic to cables is genuine DC/WAN-interconnect infrastructure work.
**What:** A framework mapping traceroutes to the submarine cables they traverse, plus "Route Stress," a metric estimating cable criticality.
**How:** Infers traceroute-to-cable mappings despite industry opacity and validates with case studies on SCN vulnerability.
**Where applicable:** Global connectivity/resilience analysis; research framework.

### Inter-domain Routing with Extensible Criteria (IREC) — Seyedali Tabaeiaghdaei et al. (Anapaya, ETH Zurich, others) — Adjacent
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750528 · video https://youtu.be/05Kfy4C3Ljc
**Why:** BGP/datapath internals and path-aware networking are in scope; extensible inter-domain criteria is a forward-looking control-plane idea.
**What:** An inter-domain routing architecture for SCION enabling path optimization on extensible, end-domain-specified criteria.
**How:** Parallel execution and real-time addition of independent route computations over SCION's stateless forwarding, with negligible global cost vs static routing in large-scale simulation.
**Where applicable:** SCION/path-aware networks specifically; not deployable on vanilla BGP.

## Wildcard

### Orderlock: A New Type of Deadlock and its Implications on HPN Protocol Design — Weihao Jiang et al. (SJTU, Nanjing U.) — Wildcard
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750497 · video https://youtu.be/LbMFusZIgZ0
**Why:** A genuine impossibility result is the kind of conceptual lever that outlasts any benchmark and reshapes how to reason about transport feature combinations.
**What:** Proves that in-order delivery + lossless transmission + out-of-order capability are jointly impossible without risking a new deadlock class ("Orderlock"), and explores Orderlock-free designs.
**How:** Formal necessary-and-sufficient-condition proof, plus a case study tuning AI-workload performance under Orderlock-free protocols.
**Where applicable:** General theory for HPN protocol/hardware co-design — a reasoning tool, not a system.

### Direct-to-Cell Satellite Network without Satellite Navigation (SN²) — Wei Liu et al. (Tsinghua) — Wildcard
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750522 · video https://youtu.be/G3KDDdRZYBE
**Why:** The failure mode is fundamentally an authn/authz-and-location problem in disguise — GNSS as an implicit trust dependency for access control is a framing the identity-minded PM will appreciate.
**What:** Shows direct-to-cell satellite networks' over-reliance on GNSS for geolocation/timing causes mis-billing, unauthorized service, and denials, and proposes self-navigation from the satellites themselves.
**How:** A "fate-sharing" approach reusing the direct-to-cell satellites for built-in navigation, trading navigation accuracy for availability; validated with commodity satellite phones on 3GPP NTN stacks.
**Where applicable:** Direct-to-cell / NTN satellite systems; the trust-dependency lesson generalizes beyond space.

### Firefly: Scalable, Ultra-Accurate Clock Synchronization for Datacenters — Pooria Namyar et al. (Google, USC, NVIDIA) — Wildcard
**Links:** pdf https://dl.acm.org/doi/10.1145/3718958.3750502 · video https://youtu.be/1dMxivswX6M
**Why:** Precise time quietly underpins distributed consistency, certificate/token validity windows, and ordering — sub-10ns in software is a striking result with security and distributed-systems reach.
**What:** A software-driven clock-sync system hitting sub-10ns device-to-device and ≤1µs device-to-UTC in a 248-machine Clos, resilient to time-server failure and unstable clocks.
**How:** Distributed consensus on a random overlay graph with gradual hardware-clock adjustment, plus "layered synchronization" decoupling internal (device-to-device) from external (to-UTC) sync.
**Where applicable:** Datacenter timing (e.g., cloud financial exchanges); software-only, broadly applicable where hardware PTP is impractical.

## Themes

- **AI training/inference infrastructure dominates the program.** Collective-communication scheduling (SyCCL, ResCCL, Hermod), MoE serving/fabric (MegaScale-Infer, MixNet), HBD/optical fabrics (InfiniteHBD, Mosaic), topology search (ZCube), and RDMA-for-AI (Stellar) — the center of gravity in systems networking has shifted to the AI datapath.
- **Optics and reconfigurable fabric are back as first-class topics.** Mosaic (microLED wide-and-slow links), InfiniteHBD (OCS-in-transceiver), MixNet (optical-electrical reconfiguration), and Flare (transport for reconfigurable DCNs) all attack the physical-layer scaling wall rather than just the protocol stack.
- **RDMA without lossless/PFC is a live front.** DCP, Falcon, and Jakiro independently push toward reliable RDMA over lossy, general-purpose, multi-tenant Ethernet — the PFC-dependence escape is this cycle's recurring transport problem.
- **In-network ML, with a built-in reality check.** Decision trees and DL on programmable switches/SmartNICs are widespread (SpliDT, Pegasus, Mazu, NPC), but "The Sweet Danger of Sugar" lands a methodological broadside on how encrypted-traffic ML is evaluated — enthusiasm and skepticism in the same program.
- **Verification and correctness-by-construction matured to production.** ZENITH (verified, code-generated control plane), S2 (scale-out config verification), and Hoyan (multi-year WAN verification with 56%→5% incident reduction) show formal methods moving from single-box tools to deployed systems.
- **LLMs/agents are entering network operations.** Confucius, BIAN, and SkyNet mark a turn toward LLM-assisted diagnosis, failure localization, and intent-driven management at hyperscale — early but production-grounded.

A caveat on what's *not* here: there's little direct passkeys/FIDO/OAuth/OIDC or SPIFFE/SPIRE workload-identity work — SIGCOMM remains a systems/datapath venue, so the identity-relevant picks (RevDNS, SN², the centralization papers) approach it from the PKI/trust-dependency angle rather than authn protocols.
