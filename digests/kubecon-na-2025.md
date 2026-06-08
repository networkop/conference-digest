<!--
conference: KubeCon + CloudNativeCon North America 2025
type: vendor
source_url: https://kccncna2025.sched.com/list/descriptions/
generated: 2026-06-08
registry_key: kubecon-na-2025
-->

# KubeCon + CloudNativeCon North America 2025 — Digest

A triaged set of sessions for a PM working across physical DC/WAN networking, cloud-native networking, network security, and identity. The published program provides titles, speakers, and abstracts only — no per-session paper/slide/recording links — so every write-up below is grounded in the abstract and is marked accordingly. Pure sponsor slots, 101 sessions, and content-free "we adopted X" talks were dropped. Picks are deliberately tight.

## Core

### TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned

*Giri Kuncoro & Joseph Pallamidessi, TikTok* — **Core**

- **Why**: An IPv6-only production datacenter is still rare, and Cilium's battle-testing has overwhelmingly been on IPv4 / dual-stack. This is a concrete report of what actually breaks at the datapath when you remove IPv4 entirely — directly relevant to anyone planning a v6-only fabric.
- **What**: A migration account of moving global, IPv6-only clusters to Cilium, enumerating specific failures rather than a success story. (from abstract only)
- **How**: Native routing mode was mandatory because Cilium does not tunnel over IPv6; they then hit a sequence of v6-only bugs — NDP traffic dropped by network policy due to incorrect identity resolution, DNS policy not permitting IPv6 DNS servers, debug tooling broken when IPv4 BPF maps are absent, plus a NodePort timeout issue. (from abstract only)
- **Where applicable**: IPv6-only Kubernetes on Cilium specifically; the failure modes are general to v6-only Cilium deployments, not TikTok-specific infrastructure. A practical pre-flight checklist for that migration.

### QEMU in the Fast Lane: Accelerating KubeVirt Networking With eBPF

*Daniel Borkmann & Anton Protopopov, Isovalent at Cisco* — **Core**

- **Why**: VM-on-Kubernetes convergence keeps colliding with the latency/throughput tax of the virt networking path. The usual escape hatch, SR-IOV, costs you host-side observability and policy enforcement. This is a contributor-led internals talk from the people who build the Cilium datapath.
- **What**: An architecture that puts QEMU's network path on AF_XDP to get near-line-rate KubeVirt networking while retaining host-level visibility and policy. (from abstract only)
- **How**: eBPF/AF_XDP fast path built on Cilium, `netkit`, and upstream Linux kernel enhancements, with contributions landed in both QEMU and the kernel to back KubeVirt pods with high-performance AF_XDP interfaces. (from abstract only)
- **Where applicable**: KubeVirt/QEMU-KVM on Kubernetes with a recent kernel and Cilium + netkit; general technique, but depends on the upstream kernel/QEMU work being present.

### On-Prem Load Balancing Reimagined: Serving 20 Million QPS With Gateway API and EnvoyGateway

*Isaac Wilson, The Trade Desk* — **Core**

- **Why**: One of the few talks with a real scale number (20M QPS) and an explicit "things we broke" framing — a bare-metal HAProxy to Kubernetes/Envoy migration at the high end of on-prem load balancing.
- **What**: How an established bare-metal HAProxy Community Edition load-balancing tier was rebuilt as an Envoy Gateway / Gateway API platform, including upstream Envoy contributions. (from abstract only)
- **How**: Migrated core services and refactored service discovery; extended Envoy Gateway with circuit breakers and zone-aware routing for topology-aware traffic distribution and resilience, contributing some of that work upstream. (from abstract only)
- **Where applicable**: On-prem / bare-metal load balancing at large scale; broadly applicable to Gateway API + Envoy Gateway adopters, though the 20M QPS economics are specific to The Trade Desk's ad-tech workload.

### Authenticating and Authorizing Every Connection at Uber

*Yangmin Zhu & Matt Mathew, Uber* — **Core**

- **Why**: A multi-year, production-scale SPIFFE/SPIRE zero-trust rollout across thousands of polyglot microservices, with the hard constraint of no application code changes — exactly the workload-identity territory in the PM's wheelhouse, told with operational detail.
- **What**: The design and three-year rollout of a platform-level service-to-service authn/authz system based on Envoy, SPIRE, and SPIFFE. (from abstract only)
- **How**: A "Secure Service Mesh" using Envoy as a transparent data plane and SPIRE issuing SPIFFE identities; every connection gets mTLS, workloads are authenticated by SPIFFE ID, and fine-grained policy is enforced through a unified control plane — all without service code changes. (from abstract only)
- **Where applicable**: Large multi-language, multi-cloud microservice estates. Mechanism is general (Envoy + SPIRE + SPIFFE); the scale and migration sequencing are Uber-specific.

### From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero Trust

*Mae Large & Ivy Alkhaz, State Farm* — **Core**

- **Why**: A candid SPIFFE/SPIRE operations talk — what fell over at scale and how an HA topology fixed it — which is more useful than a greenfield demo for anyone running SPIRE in anger.
- **What**: The evolution from a hand-rolled SPIFFE/SPIRE deployment that buckled under scale to an HA nested-SPIRE architecture integrated with External Secrets Operator (ESO). (from abstract only)
- **How**: Nested SPIRE configured for high availability; SPIFFE SVIDs integrated with ESO's webhook-authenticated `SecretStore` for secret retrieval and automated rotation; includes debugging detail on ESO webhook 500 errors and scaling SPIRE agents. (from abstract only)
- **Where applicable**: Multi-cluster Kubernetes (here on ROSA / OpenShift on AWS) using SPIRE + ESO; the nested-SPIRE HA pattern is general, the ROSA specifics are org-specific.

### AdminNetworkPolicy: From Alpha To Beta and Beyond

*Dan Winship & Surya Seetharaman, Red Hat; Nadia Pinaeva, NVIDIA; Bowei Du, Google* — **Core**

- **Why**: The SIG-Network policy API is where cluster-wide, admin-tier network security is actually being standardized. Knowing where AdminNetworkPolicy (ANP) and BaselineAdminNetworkPolicy are heading affects how every CNI will enforce policy.
- **What**: A working-group update on graduating ANP and BaselineANP toward beta, plus the roadmap for the Network Policy API. (from abstract only)
- **How**: Contributor-led walkthrough of the API surface for cluster-scoped, admin-defined network policy that sits above namespace-scoped NetworkPolicy. (from abstract only)
- **Where applicable**: Any Kubernetes cluster; CNI support varies (OVN-Kubernetes and others are tracking it). General standards-direction content.

### Strengthening Kubernetes Trust: SIG Auth's Latest Security Enhancements

*Anish Ramasekar, Mo Khan, Stanislav Láznička, Rita Zhang & Peter Engelbert, Microsoft* — **Core**

- **Why**: The authoritative source on where Kubernetes core authentication and authorization are moving, straight from SIG Auth chairs/leads — foundational for the identity side of the PM's remit.
- **What**: A survey of recent and upcoming SIG Auth features shaping cluster authn/authz. (from abstract only)
- **How**: Maintainer-led overview of the auth feature set landing in recent and upcoming Kubernetes releases. (from abstract only)
- **Where applicable**: All Kubernetes clusters; general, version-dependent on the releases the features ship in.

### Kubernetes IP Management: From Core Concepts To Strategic Solutions

*Ivy Zhuang & Whitney Jenkins, Google* — **Core**

- **Why**: IPAM decisions are often irreversible and IP exhaustion is a recurring production wall. A structured treatment of IPAM modes, dual-stack, and the newer Extend Service IP Range feature is squarely on-topic.
- **What**: A concepts-to-solutions tour of Kubernetes IPAM: CNI roles, IP assignment for pods/services/nodes, and current IPAM features. (from abstract only)
- **How**: Covers IPAM modes, CIDR allocation/subnetting for IP exhaustion, dual-stack (IPv4/IPv6) complexities, connectivity troubleshooting, and the Extend Service IP Range capability. (from abstract only)
- **Where applicable**: General Kubernetes networking design; broadly applicable. Leans introductory but earns a place for the strategic/irreversibility framing and the newer features.

### Navigating the AI/ML Networking Maze in Kubernetes: Lessons From the Trenches

*Antonio Ojea, Google* — **Core**

- **Why**: HPC networking primitives — RDMA, MPI, collective-communication patterns — are being dragged into Kubernetes by AI workloads. Bridging traditional networking experience into this is exactly the PM's transition, told by a SIG-Network tech lead.
- **What**: Practical lessons from building networking solutions for AI/ML workloads, including a DRA-based network driver. (from abstract only)
- **How**: Discusses integrating specialized hardware, managing out-of-band RDMA, and the collective-communication patterns of distributed training, with Dynamic Resource Allocation (DRA) exposing and managing these resources. (from abstract only)
- **Where applicable**: Kubernetes clusters running distributed AI/ML training/inference with RDMA-class hardware; the DRA network-driver approach is general but still maturing.

### Spiderpool: Dynamic Topology-Aware RDMA Allocation For GPU-Based AI Workloads

*Weizhou Lan, DaoCloud* — **Core** *(Project Lightning Talk)*

- **Why**: A precise physical-topology networking problem — aligning RDMA NICs with PCIe-affined GPUs — that the standard device-plugin/CNI split can't solve. This sits right at the DC-hardware/cloud-native seam the PM cares about.
- **What**: A mechanism in Spiderpool to allocate only the PCIe-affined RDMA NICs a pod actually needs, instead of attaching every interface and RDMA device. (from abstract only)
- **How**: Built on DRA and NRI, Spiderpool detects the GPU devices assigned at pod-creation time and allocates the matching PCIe-affined RDMA NICs and Ethernet interfaces for GPUDirect RDMA, minimizing overhead while preserving RDMA performance. (from abstract only)
- **Where applicable**: GPU nodes doing distributed inference/training where a container needs a subset of GPUs; requires RDMA NICs with discoverable PCIe affinity and DRA/NRI support. Lightning-talk depth.

### Fix First, Investigate Later: When an eBPF Rollout Brought Down Our Network

*Zain Malik, Exostellar & Grzegorz Głąb, Whatnot* — **Core**

- **Why**: A genuine incident post-mortem with hard numbers (throughput collapse from ~800 MB/s to ~250 MB/s, packet loss spikes) caused by a silently rolled-out eBPF DaemonSet — the kind of failure-mode honesty the program mostly lacks.
- **What**: An outage investigation that traced mysterious packet loss to an unannounced cloud-provider eBPF monitoring agent (Retina). (from abstract only)
- **How**: Incident narrative from alerts through diagnosis to discovery of the unfamiliar eBPF DaemonSet; emphasis on how to triage when the cause is infrastructure you didn't deploy. (from abstract only)
- **Where applicable**: Managed Kubernetes where the provider can inject eBPF agents; general cautionary lesson on eBPF programs contending on the datapath.

## Adjacent

### Lessons Applied Building a Next-generation AI Proxy

*John Howard, Solo.io* — **Adjacent**

- **Why**: From an Istio TOC/Steering member, this is the clearest articulation of why AI traffic breaks traditional proxies and what an AI-optimized data plane needs — relevant to where Envoy/Gateway data planes are heading.
- **What**: The design rationale behind a new CNCF AI proxy built as part of kgateway. (from abstract only)
- **How**: Argues that intelligent request batching, model-aware load balancing, and token-based rate limiting are now table stakes that Envoy-era proxies weren't built for, and walks through the tradeoffs of a purpose-built AI data plane. (from abstract only)
- **Where applicable**: AI/LLM inference gateways; conceptual/architectural, broadly applicable to proxy and gateway designers.

### AI Inference Without Boundaries: Dynamic Routing With Multi-Cluster Inference Gateway

*Rob Scott, Google & Daneyon Hansen, Solo.io* — **Adjacent**

- **Why**: Extends Gateway API into multi-cluster GPU scheduling — a networking-control-plane answer to GPU scarcity, from the maintainers of Gateway API and the Inference Extension.
- **What**: Multi-Cluster Inference Gateway, a new part of the Inference Gateway project that routes inference traffic to wherever GPUs are available across clusters. (from abstract only)
- **How**: Builds on existing Gateway API and multi-cluster patterns to dynamically shift traffic toward clusters with free GPU capacity, for cost optimization and availability. (from abstract only)
- **Where applicable**: Organizations with GPU capacity spread across multiple clusters; general Gateway API-based approach.

### Routing Stateful AI Workloads in Kubernetes

*Maroon Ayoub, IBM & Michey Mehta, Red Hat* — **Adjacent**

- **Why**: A layered, concrete treatment of why stateless K8s routing fails for LLM inference and how KV-cache-aware load balancing changes the picture — grounded in the multi-vendor `llm-d` effort.
- **What**: Routing strategies for stateful LLM workloads, from round-robin up to full KV-cache-aware load balancing, with guidance on when each applies. (from abstract only)
- **How**: Based on `llm-d` (Google/IBM Research/Red Hat) using the Gateway API Inference Extension; covers session-aware routing for long-context traffic and global vs local cache indices. (from abstract only)
- **Where applicable**: LLM inference platforms on Kubernetes; general technique tied to the Inference Extension.

### Gateway API: Table Stakes

*Shane Utt & Candace Holman, Red Hat; Mike Morris, Microsoft; Lior Lieberman & Kellen Swain, Google* — **Adjacent**

- **Why**: A maintainer-level status check on Gateway API as the converging standard for ingress, routing, and mesh — useful for tracking the direction of the API the PM's mesh/ingress choices now depend on.
- **What**: A consolidated update on Gateway API's maturity as a core cloud-native building block. (from abstract only)
- **How**: Maintainers from the three main vendor contributors review where the API and its conformance stand. (from abstract only)
- **Where applicable**: Anyone standardizing on Gateway API; general standards-direction content.

### Return of the Mesh: Gateway API's Epic Quest for Unity

*Henrik Rexed, Dynatrace* — **Adjacent**

- **Why**: A comparative, benchmark-driven look at how well Istio, Kuma, Linkerd, Traefik Mesh, and Ambient actually implement the Gateway API for mesh (GAMMA) — practical for mesh selection and migration.
- **What**: A community evaluation of Gateway API / GAMMA support across multiple service meshes, with performance benchmarks. (from abstract only)
- **How**: Configures each mesh using HTTPRoute and GRPCRoute, flags where custom tweaks are still needed, and benchmarks across solutions. (from abstract only)
- **Where applicable**: Teams choosing or migrating between service meshes; general. Independent benchmarking always warrants a skim of the methodology.

### Istio Project Updates: AI Inference, Ambient Multicluster & Default Deny

*Keith Mattix, Microsoft* — **Adjacent**

- **Why**: The official Istio roadmap signal — ambient multicluster, default-deny posture, and AI inference support indicate where the most-deployed mesh is investing.
- **What**: A TOC-level update on new Istio features and next-year roadmap. (from abstract only)
- **How**: Roadmap overview; depth unknown from the abstract. (from abstract only)
- **Where applicable**: Istio users; general project-direction content. Roadmap talk, so treat specifics as intentions.

### It's 2025; Why Are You OK With an Insecure Network?

*Alex Leong, Buoyant* — **Adjacent**

- **Why**: A maintainer's argument that the real blocker to in-cluster encryption/authn is operational simplicity, not technology — a useful framing for why mTLS adoption stalls, even if vendor-flavored.
- **What**: An opinion/strategy talk on the barriers to secure in-cluster communication and how to lower them. (from abstract only)
- **How**: Discusses meshes, application code, and memory safety, centering operational simplicity and observability; examples use Linkerd but framed as broadly applicable. (from abstract only)
- **Where applicable**: General; perspective rather than a technique. Note the Linkerd vendor lens.

### End-to-End Security With gRPC in Kubernetes

*Shiva & Abhishek Agrawal, Google* — **Adjacent**

- **Why**: A practical consolidation of the moving parts for securing gRPC service-to-service traffic — TLS/mTLS, JWT/OAuth2, cert lifecycle — relevant to the identity/authn remit.
- **What**: Best-practices walkthrough for end-to-end gRPC security in Kubernetes. (from abstract only)
- **How**: TLS/mTLS for transport, JWT and OAuth2 for authentication, cert-manager and Secrets for certificate management, and Istio for automating the security config. (from abstract only)
- **Where applicable**: gRPC microservices on Kubernetes; general. Likely practitioner-level rather than deep internals.

### Design Patterns for Consistent Centralized Authorization

*José Padilla, Auth0 & Alice Gibbons, Diagrid* — **Adjacent**

- **Why**: Centralized fine-grained authorization (OpenFGA / Zanzibar-style) raises a real data-consistency problem — keeping authorization data in sync with distributed app state — that the identity side eventually hits.
- **What**: Patterns for reliably synchronizing centralized authorization data (users, roles, relationships) with distributed application state. (from abstract only)
- **How**: Uses Dapr building blocks (pub/sub, state management) to coordinate consistent dual writes between apps and OpenFGA via asynchronous domain events, avoiding a shared database. (from abstract only)
- **Where applicable**: Microservices adopting OpenFGA/ReBAC with an event-driven backbone; the Dapr specifics are one implementation, the dual-write consistency problem is general.

## Wildcard

### Fast and the Furious: CICD Pipeline for eBPF Programs at Meta Scale

*Theophilus Benson (CMU) & Prankur Gupta, Meta* — **Wildcard**

- **Why**: Not a networking-design talk, but a rare look at the *release engineering* of eBPF at hyperscale — 150+ programs updated weekly across the fleet. The interesting question is how you test and roll out kernel-attached code without causing outages, which is adjacent to (and quietly underpins) everything Cilium/datapath related.
- **What**: How Meta runs CI/CD for its large eBPF program estate spanning observability, load balancing, network-stack specialization, and security. (from abstract only)
- **How**: Abstract is truncated in the program; it describes a custom, flexible in-house pipeline and the outage risk introduced by weekly eBPF updates, but specifics aren't fully stated. (from abstract only — partial)
- **Where applicable**: Hyperscale eBPF fleets; Meta-specific tooling, but the testing/rollout discipline generalizes to anyone shipping eBPF programs.

### Debugging Your Cluster When It's on Fire

*Nikola Grcevski, Grafana Labs & Tyler Yahn, Splunk* — **Wildcard**

- **Why**: The new OpenTelemetry eBPF Instrumentation project promises zero-config, on-demand distributed traces and connectivity graphs added to a live cluster without touching app config — a genuinely different operational capability worth seeing even if it's outside core networking design.
- **What**: A demonstration of adding deep, language-agnostic telemetry to a misbehaving production cluster with no application or cluster config changes, via OTel eBPF instrumentation. (from abstract only)
- **How**: Uses eBPF-based auto-instrumentation to produce on-demand distributed traces and service connectivity graphs in-situ. (from abstract only)
- **Where applicable**: Any Kubernetes cluster needing emergency observability; general, dependent on the OTel eBPF project's maturity.

### Sponsored Keynote: Anchoring Trust in the Age of AI — Identities Across Humans, Machines, and Models

*Yuan Tang & Anjali Telang, Red Hat* — **Wildcard**

- **Why**: A sponsored keynote (so discount the pitch), but it stakes out a thesis the PM's agentic-identity interest should track: extending SPIFFE/SPIRE workload identity into the AI serving path so every model and pipeline step carries a verifiable identity. The "identity for models, not just services" framing is where the field is heading.
- **What**: A proposed trust fabric where workloads, users, and AI models all carry verifiable identity for an auditable chain of trust. (from abstract only)
- **How**: SPIFFE/SPIRE issue cryptographic workload identities, Keycloak adds a user identity/access layer, and KServe extends identity into AI model serving so each model, explainer, and pipeline step runs with attested identity. (from abstract only)
- **Where applicable**: AI serving on Kubernetes; conceptual/directional. Keynote-level, vendor-framed — value is the thesis, not implementation detail.

## Themes

- **AI workloads are rewriting the networking layer.** RDMA/GPUDirect, topology-aware NIC allocation, KV-cache-aware routing, and AI-optimized proxies recur across the program — HPC networking primitives are being absorbed into Kubernetes, with Dynamic Resource Allocation (DRA) as the common plumbing.
- **Gateway API is the consolidation point.** Ingress (ingress-nginx → InGate), service mesh (GAMMA), and now inference routing are all converging on Gateway API; multiple maintainer updates and a cross-mesh benchmark reflect that gravity.
- **Workload identity is going mainstream — and stretching to AI agents.** SPIFFE/SPIRE production rollouts (Uber, State Farm), SIG Auth core work, and keynote/agentic-identity sessions show identity moving from aspiration to operations, with models and agents as the next identity-bearing entities.
- **eBPF is now infrastructure you must operate, not just adopt.** The standout talks treat eBPF as something with a release pipeline (Meta), an incident blast radius (the Retina outage), and a role accelerating virt networking (KubeVirt/AF_XDP) — a maturity shift from "eBPF is cool" to "eBPF in production has failure modes."
- **The best content is failure-honest and metric-bearing.** The picks that stood out carried real numbers or real outages (20M QPS, 800→250 MB/s collapse, three-year zero-trust rollout); most of the remaining program was product positioning or 101 material.
- **IPv6-only and on-prem/bare-metal are quietly back.** TikTok's v6-only Cilium work and The Trade Desk's bare-metal load-balancing rebuild signal that large operators are pushing cloud-native tooling into environments it wasn't originally hardened for.
