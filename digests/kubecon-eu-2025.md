<!--
conference: KubeCon + CloudNativeCon Europe 2025 (London)
type: vendor
source_url: https://kccnceu2025.sched.com/list/descriptions/
generated: 2026-08-30
registry_key: kubecon-eu-2025
-->

# KubeCon + CloudNativeCon Europe 2025 (London) — Digest

A triaged set of sessions for a PM working across physical DC/WAN networking, cloud-native networking, network security, and identity. The published program provides titles, speakers, and abstracts only — no per-session paper/slide/recording links — so every write-up below is grounded in the abstract and is marked accordingly. Sponsor pitches, cloakroom/logistics entries, DEI/community programming, and content-free "we adopted X" talks were dropped. Picks are deliberately tight given the size of the program (500+ sessions across the main conference and ~15 co-located day events).

## Core

### IAM, Agent: Identity for Autonomous AI

*Matthew Bates, Cofide* — **Core**

- **Why**: This is the session that most directly hits the PM's agentic-identity interest: applying zero-trust and workload identity principles to multi-agent AI systems, explicitly citing SPIFFE/SPIRE and the IETF's WIMSE standard.
- **What**: A talk on IAM for autonomous, multi-agent AI systems — dynamic identity provisioning, agent-to-agent authentication, and cryptographic attestation for AI agent workloads. (from abstract only)
- **How**: Applies zero-trust principles using CNCF SPIFFE/SPIRE for workload identity combined with emerging IETF standards (WIMSE) to handle the trust interplay between human and agent identities. (from abstract only)
- **Where applicable**: General; aimed at anyone building multi-agent AI architectures who needs standards-based identity rather than bespoke API keys per agent.

### Beyond Classical Cryptography: Building Quantum-Resistant Cloud Native Infrastructure With SPIFFE

*Andrés Vega, M42 & Hugo Landau, Messier42* — **Core**

- **Why**: A concrete, working demonstration of post-quantum cryptography threaded through the exact identity/networking stack the PM tracks (SPIFFE/SPIRE, Cilium, Envoy) rather than a standards-committee abstraction — a preview of what PQ migration actually touches in a real cluster.
- **What**: A live demo of end-to-end post-quantum cryptography in Kubernetes: PQC-enabled SPIRE issuing Kyber KEM / Dilithium3 X.509 certificates, quantum-resistant mTLS, and Cilium L7 policy enforcement over that identity. (from abstract only)
- **How**: Deploys PQC-enabled SPIRE, Cilium, and Envoy together — Kyber for key exchange, Dilithium3 for certificate signatures — with Cilium network policies doing L7 filtering and Envoy handling inter-node mTLS with the PQ algorithms. (from abstract only)
- **Where applicable**: General technique for any SPIFFE/SPIRE + Cilium/Envoy deployment; depends on NIST's 2024 PQC algorithm choices (ML-KEM/Kyber, ML-DSA/Dilithium) holding up, which is the same assumption the IETF PQ-migration work (see the ietf-122 digest) is built on.

### Zero Trust at Shopify Scale: Automating MTLS Across Thousands of Services

*Dani Santos & Michelle Mali, Shopify* — **Core**

- **Why**: A real production account — with failure modes, not just success framing — of the operational problem every SPIFFE/SPIRE or cert-manager deployment eventually hits: rotating certificates across thousands of services without an outage.
- **What**: How Shopify automates mTLS certificate lifecycle (issuance, rotation, cross-cluster distribution) at thousands-of-services scale, including the evolution of their approach and the failure modes they hit along the way. (from abstract only)
- **How**: Evolved from custom admission controllers to patterns that work across Kubernetes and non-Kubernetes environments — mounting CA certificates at container startup with periodic CronJob-driven renewal, plus RBAC and graceful rollover mechanisms. (from abstract only)
- **Where applicable**: General mTLS-at-scale problem; the specific CronJob-renewal pattern is one implementation choice among several, useful as a reference for anyone hitting cert-rotation pain at scale.

### SPIFFE in Practice: Universal Identity for WebAssembly Workloads

*Joonas Bergius, Cosmonic & Colin Murphy, Adobe* — **Core**

- **Why**: SPIFFE's "universal identity across any workload platform" claim gets tested against a genuinely different runtime model (WASM components, not containers) — useful signal for how far the standard actually stretches.
- **What**: The journey of adopting SPIFFE as the identity foundation for WebAssembly workloads on CNCF wasmCloud, from concept to production. (from abstract only)
- **How**: Not detailed beyond "lessons learned integrating SPIFFE with a WASM component runtime rather than a container runtime" — the abstract flags this as introducing unique challenges versus a straight lift-and-shift of container-based SPIFFE integration. (from abstract only — thin on mechanism)
- **Where applicable**: WebAssembly-based workload platforms (wasmCloud specifically); general lesson for anyone extending SPIFFE beyond containers.

### Workload Identity for Humans: A Twelve-Factor Approach

*Vish Abrams, Heroku* — **Core**

- **Why**: A useful counterpoint to the platform-level SPIFFE/SPIRE talks above: an argument that workload identity primitives are powerful but leave application developers reinventing bespoke integration per platform, and a proposal for a more opinionated developer-facing layer.
- **What**: A developer-focused workload identity approach layered on top of existing CNCF primitives (Kubernetes Service Accounts, SPIFFE/SPIRE), applying Twelve-Factor App principles to make identity integration feel natural rather than bespoke. (from abstract only)
- **How**: Not detailed mechanically in the abstract; framed as an opinionated abstraction layer over existing identity primitives rather than a new protocol. (from abstract only — thin on mechanism)
- **Where applicable**: General; relevant to anyone whose application teams treat workload identity as ops-only plumbing rather than a first-class app concern.

### Simplifying the Networking and Security Stack With Cilium, Hubble, and Tetragon

*Bill Mulligan & Anna Kapuścińska, Isovalent at Cisco; Bowei Du, Google; Amir Kheirkhahan, DBSchenker* — **Core**

- **Why**: The flagship Cilium project update, with real adopter voices (DB Schenker, Google) rather than just maintainer roadmap — worth tracking as the state of the eBPF networking/security/observability stack the PM already follows.
- **What**: Updates on Cilium's latest release covering multi-cluster networking, scaling to 65,000 nodes, service-mesh use cases, plus Hubble (network observability) and Tetragon (security observability/runtime enforcement) sub-projects. (from abstract only)
- **How**: A single eBPF-powered datapath replaces a fragmented toolchain (separate CNI, observability agent, and runtime security tools) with one unified stack. (from abstract only)
- **Where applicable**: General Kubernetes CNI/networking-security deployments; the 65,000-node scaling claim is a specific data point worth verifying against your own scale requirements rather than assuming linear applicability.

### Making the Leap: What Gateway API Needs To Support Ingress-NGINX Users

*Rob Scott, Google & James Strong, Isovalent at Cisco* — **Core**

- **Why**: Ingress-NGINX has been the de facto standard for years; its maintainers moving to a Gateway API-focused implementation is a significant ecosystem signal, and this talk is literally about the compatibility gaps blocking that migration — directly relevant to anyone planning an ingress-to-Gateway-API transition.
- **What**: An inventory of commonly-used Ingress-NGINX features not yet supported by Gateway API, and a call for community input on closing those gaps to make Gateway API a true Ingress-NGINX successor. (from abstract only)
- **How**: Not a new mechanism — a gap analysis between the mature, feature-rich Ingress-NGINX annotation surface and Gateway API's current spec coverage. (from abstract only)
- **Where applicable**: General; anyone currently on Ingress-NGINX evaluating or planning a Gateway API migration should treat this as a pre-migration checklist source.

### Uncharted Waters: Dynamic Resource Allocation for Networking

*Miguel Duarte Barroso, Red Hat & Lionel Jouin, Ericsson Software Technology* — **Core**

- **Why**: After a rejected "modify the Pod spec directly" proposal, Kubernetes networking is pivoting to Dynamic Resource Allocation (DRA) as the extensibility mechanism — this is a first-order architectural direction for how multi-network and specialized-NIC support lands in core Kubernetes.
- **What**: Introduces the DRA CNI Driver approach to bringing native multi-network and advanced networking support into Kubernetes via the DRA mechanism, rather than further Pod-spec modification. (from abstract only)
- **How**: Uses Dynamic Resource Allocation — the same Kubernetes-native mechanism being built out for GPU/TPU/NIC device management — as the plumbing for exposing and requesting specialized network resources/interfaces per pod. (from abstract only)
- **Where applicable**: General direction for Kubernetes multi-network and specialized-NIC (RDMA, SR-IOV-class) support; still an upstream-in-progress effort, so treat as a roadmap signal rather than a shipped feature to adopt today.

### Encryption, Identities, and Everything in Between; Building Secure Kubernetes Networks

*Lior Lieberman, Google & Igor Velichkovich, Stealth Startup* — **Core**

- **Why**: A rare talk that explicitly frames encryption and identity/AuthN/AuthZ as one problem for Kubernetes networking rather than separate concerns, and calls for the community to standardize and simplify it — a useful survey of where the ecosystem actually stands.
- **What**: A tour of the current encryption and AuthN/AuthZ project landscape for Kubernetes networking, framed around defense-in-depth and least-privilege, with real-world scaling scenarios. (from abstract only)
- **How**: Not a single mechanism — a synthesis across existing projects, aimed at identifying design requirements for resilient, secure networks at scale. (from abstract only)
- **Where applicable**: General; most useful as an orientation talk for evaluating the fragmented landscape of Kubernetes network encryption/identity tooling rather than a specific implementation guide.

### The Great Sidecar Debate

*William Morgan, Buoyant* — **Core**

- **Why**: The sidecar-vs-sidecarless architectural question is the central fault line in service mesh right now (Istio ambient, Cilium mesh, Kmesh below); this is a maintainer-level, engineering-tradeoffs framing rather than a vendor pitch for one side.
- **What**: A pragmatic evaluation of sidecar vs. sidecarless (ambient/eBPF) service mesh architectures across resource consumption, operational blast radius, and security threat models. (from abstract only)
- **How**: Frames every architectural choice as a tradeoff and works through concrete scenarios where sidecars still win versus where ambient/eBPF approaches are strictly better. (from abstract only)
- **Where applicable**: General service mesh architecture decisions; useful as a mental framework regardless of which mesh implementation you're evaluating.

### Revolutionizing Sidecarless Service Mesh with eBPF and Remote Gateway (Kmesh)

*Zhonghu Xu, Huawei* — **Core**

- **Why**: Concrete performance numbers for the sidecarless-mesh direction discussed above — a specific implementation (Kmesh) claiming a 90% resource-consumption reduction versus sidecar-based meshes while staying Istio-API-compatible.
- **What**: A demo of Kmesh, an eBPF-based sidecarless service mesh combining an L4 eBPF acceleration layer with an L7 control plane via remote waypoint proxies, claiming full Istio API compatibility. (from abstract only)
- **How**: eBPF hooks handle L4 traffic redirection and kernel-space connection management directly; L7 features (canary, traffic splitting, fault injection) are handled by a decoupled remote waypoint gateway rather than a per-pod sidecar proxy. (from abstract only)
- **Where applicable**: Istio-API-compatible deployments looking to cut sidecar resource overhead; vendor-reported numbers (90% resource reduction, 10x CPU improvement) should be treated as claims to verify against your own workload, not assumed universal.

### Identity-based Trust — Till Death Do We Part?

*John Kjell, ControlPlane & Kairo De Araujo, Independent* — **Core**

- **Why**: A threat-model-first look at OIDC-based "trusted publishing" (PyPI, npm, RubyGems, Homebrew, all built on Sigstore's Fulcio/Rekor) — directly relevant to identity infrastructure design, specifically the hard problem of what happens when the identity backing a signature is compromised in an append-only trust log.
- **What**: A threat model for compromise in Sigstore-based identity signing systems, and mitigation/recovery mechanisms using in-toto and The Update Framework (TUF), including a concrete implementation in in-toto's Archivista sub-project. (from abstract only)
- **How**: Sigstore's Rekor transparency log is append-only with no entry removal, so identity compromise can't simply be "erased" — the talk covers mitigation and recovery patterns that work within that constraint rather than against it. (from abstract only)
- **Where applicable**: General for OIDC-based signing/attestation systems (trusted publishing, artifact signing); specifically relevant to anyone building or relying on Sigstore-backed supply-chain identity.

## Adjacent

### CNCF Project Demos | BGP Beyond Loadbalancers with MetalLB and FRR-K8s

*(Project Pavilion demo)* — **Adjacent**

- **Why**: MetalLB's BGP engine (backed by FRR-K8s) moving beyond simple LoadBalancer-service advertisement into general BGP features on bare-metal clusters is a small but concrete signal of cloud-native networking absorbing more real routing-protocol capability.
- **What**: A demo of using MetalLB with FRR-K8s as a backend to add BGP features to Kubernetes clusters beyond basic LoadBalancer service advertisement to an on-prem fabric. (from abstract only)
- **How**: FRR-K8s (Free Range Routing wrapped for Kubernetes) backs MetalLB's evolved BGP engine, letting it speak more of BGP's feature surface to the on-prem fabric than the original simple advertisement model. (from abstract only)
- **Where applicable**: Bare-metal/on-prem Kubernetes needing BGP-based LoadBalancer integration; general for that deployment shape.

### SIG Network Intro and Updates

*Dan Winship & Nadia Pinaeva, Red Hat; Bowei Du, Google; Daman Arora, Broadcom* — **Adjacent**

- **Why**: The direct roadmap source for core Kubernetes networking (kube-proxy, EndpointSlice, Gateway API, network-policy direction) from the SIG that owns it — useful as an orientation point even without deep technical content.
- **What**: Status and progress update on SIG Network's core components and sub-projects, plus forward-looking considerations for the SIG's direction. (from abstract only)
- **How**: A maintainer panel format covering kube-proxy, ovn-kubernetes network-policy work, and other core networking component status. (from abstract only)
- **Where applicable**: General Kubernetes networking roadmap awareness; not a technical deep-dive.

### CNCF TAG Network and Cloud Native Network Landscape

*Zhonghu Xu, Huawei & Nic Jackson, Hashicorp* — **Adjacent**

- **Why**: A map of the CNCF's own networking-project taxonomy and governance — useful context for understanding how the various networking projects (Cilium, Kmesh, Istio, MetalLB, etc.) relate to each other institutionally.
- **What**: An introduction to the CNCF Network TAG, how it works with the CNCF TOC, and how to get involved. (from abstract only)
- **How**: Not a technical talk — governance and landscape orientation. (from abstract only)
- **Where applicable**: General orientation for anyone tracking the CNCF networking-project ecosystem as a whole.

### Tutorial: Mind Your Pod's Business: Network Isolation Workshop

*Surya Seetharaman & Miguel Duarte Barroso, Red Hat; Keith Burdis, Goldman Sachs* — **Adjacent**

- **Why**: A concrete, regulation-driven use case (EU NIS2 Directive) for network segmentation beyond Kubernetes' unrestricted-by-default pod networking, including the Layer 2 gap (VM/telecom workloads) that plain NetworkPolicies don't cover.
- **What**: A hands-on workshop achieving native network isolation for pods and VMs using CNI, KubeVirt, and OVN-Kubernetes, addressing both standard NetworkPolicy gaps and Layer 2 (Ethernet-level) isolation needs. (from abstract only)
- **How**: Configures CNI/OVN-Kubernetes/KubeVirt plugins on KIND clusters to create isolated networks and attach workloads (pods and VMs) to them, covering the segmentation cases plain NetworkPolicies leave open. (from abstract only)
- **Where applicable**: Regulated environments (explicitly framed around EU NIS2 compliance) and mixed VM/container workloads via KubeVirt; general technique for Layer 2 isolation gaps in Kubernetes networking.

### Debugging Envoy Tunnels: A Deep Dive

*Carlos Sanchez & Alexandra Stoica, Adobe* — **Adjacent**

- **Why**: A practitioner's account of a specific, painful operational pattern — Envoy tunnels with mTLS connecting Kubernetes pods to on-prem/customer infrastructure — with real troubleshooting scenarios rather than a theoretical overview.
- **What**: An interactive walkthrough of debugging Envoy tunnel failures in a production setup connecting Kubernetes pods to customer-dedicated on-prem infrastructure via dedicated egress IPs and mTLS. (from abstract only)
- **How**: Adobe's setup uses Envoy tunnels and mTLS to give pods dedicated egress identity/IPs and VPN-style connectivity to on-prem services; the talk works through categories of tunnel failure and how to diagnose them. (from abstract only)
- **Where applicable**: Envoy-based hybrid connectivity (Kubernetes-to-on-prem) specifically; the debugging methodology generalizes to other mTLS-tunnel troubleshooting.

### TUF-en up Your Software Supply Chain

*Marina Moore, Edera & Kairo De Araujo, Independent* — **Adjacent**

- **Why**: Complements the identity-trust talk above from the artifact-integrity side — how The Update Framework (TUF) and in-toto tie signed images to supply-chain metadata for end-to-end verifiable distribution.
- **What**: How to securely distribute container images along with supply-chain metadata (SBOMs, attestations) using TUF for update/distribution security and in-toto for attestation verification. (from abstract only)
- **How**: TUF ensures image and metadata freshness and tamper-resistance; in-toto layers on attestation verification for a combined secure-distribution pipeline, demonstrated live. (from abstract only)
- **Where applicable**: General software supply-chain security for container image distribution; relevant to anyone building or evaluating SBOM/attestation pipelines.

### Istio: The Past, Present and Future of the Project and Community

*Lin Sun & Louis Ryan, Solo.io; Raymond Wong, Forbes* — **Adjacent**

- **Why**: The state-of-the-project update from Istio's own leadership, including ambient (sidecarless) data-plane progress and Gateway API support — useful as the anchor reference point for the sidecar-debate and Kmesh talks above.
- **What**: An update on Istio's health, recent feature releases, ambient sidecar-less data plane progress, Gateway API support, and project roadmap. (from abstract only)
- **How**: Not a technical mechanism talk — a project/community status update. (from abstract only)
- **Where applicable**: General Istio-ecosystem awareness; most useful paired with the Kmesh and sidecar-debate sessions above for a fuller picture of where service mesh architecture is heading.

## Wildcard

### Using eBPF for Non-invasive, Performant, Instant Network Monitoring

*Mario Macías & Marc Tudurí, Grafana* — **Wildcard**

- **Why**: Not a design talk, but a genuinely different operational capability: getting L3–L7 network observability without redeploying network infrastructure or instrumenting applications, purely by attaching eBPF at different stack layers — worth seeing even outside core networking-design interest.
- **What**: How Grafana built plug-and-play network and service observability by attaching eBPF probes across network layers, correlating low-level packet flow with L7 request/response detail and Kubernetes metadata. (from abstract only)
- **How**: eBPF hooks into different layers of the service-infrastructure stack to extract flow and request-level data automatically, without needing SDN-provider support or invasive packet-analyzer deployments. (from abstract only)
- **Where applicable**: General; particularly useful where you don't control the underlying SDN/network infrastructure and need observability anyway.

### A Cloud Native Workflow for Hardware-in-the-Loop Software Development

*Miguel Angel Ajo, Red Hat* — **Wildcard**

- **Why**: A genuine crossover between cloud-native tooling and physical hardware testing — using Kubernetes-native CI (Tekton) to drive real firmware flashing, booting, and hardware interfaces (CAN bus, serial, video) rather than simulating them. Not a fit for the PM's networking/identity focus directly, but a "cloud-native reaches into physical hardware" pattern worth having on the radar.
- **What**: Jumpstarter, an open-source project connecting a software factory (CI/CD) to physical hardware, automating firmware testing on real devices from within Kubernetes. (from abstract only)
- **How**: Tekton Pipelines and GitLab drive device leasing and automation for tasks like firmware flashing and booting, interfacing through serial, CAN bus, audio, and video; Eclipse Che supports the dev/debug loop. (from abstract only)
- **Where applicable**: Embedded/firmware development for hardware devices (developed with an automotive manufacturer); the pattern of "Kubernetes-native CI orchestrating physical device labs" generalizes beyond automotive to any hardware-in-the-loop testing need.

### Stateful Connections in Kubernetes: The Scaling Secrets Nobody Talks About

*André Mocke & Rodrigo Fior Kuntzer, Miro* — **Wildcard**

- **Why**: Long-lived, stateful TCP/WebSocket connections are the awkward case Kubernetes' pod-churn model wasn't designed for, and this is a specific, non-networking-standards account of solving it in production for real-time collaboration at scale — a useful counterpoint to the mostly-stateless assumptions elsewhere in the program.
- **What**: How Miro built and operates a custom WebSocket connection manager in Kubernetes for real-time collaboration, handling connection rebalancing, draining, and graceful shutdown under enterprise compliance constraints. (from abstract only)
- **How**: Custom Kubernetes operators manage the WebSocket connection lifecycle — rebalancing live connections and draining them gracefully during scaling/deployment events instead of dropping them. (from abstract only)
- **Where applicable**: General for any Kubernetes workload with long-lived stateful client connections (real-time collaboration, gaming, trading); Miro-specific compliance constraints aside, the connection-lifecycle patterns generalize.

## Themes

- **Agentic and AI-agent identity is arriving as a named problem, not a hypothetical.** Multiple sessions (IAM for autonomous AI, workload identity for humans, SPIFFE for WASM) treat "how does an AI agent or non-container workload prove who it is" as current work, explicitly citing SPIFFE/SPIRE and IETF WIMSE — directly mirroring the standards work seen in the concurrent IETF 122 digest.
- **Post-quantum cryptography has reached live demos in cloud-native identity infrastructure**, not just standards documents — the SPIFFE/SPIRE + Cilium + Envoy PQC demo is a concrete preview of what a PQ migration actually touches in a running cluster.
- **Service mesh's sidecar-vs-sidecarless fight has matured into engineering tradeoffs, not tribalism** — the same cycle produced a neutral tradeoffs talk (Buoyant/Linkerd), a concrete eBPF-sidecarless implementation with performance numbers (Kmesh/Huawei), and an Istio ambient-mode project update, letting you triangulate rather than take one vendor's word for it.
- **Kubernetes networking extensibility is consolidating on Dynamic Resource Allocation** as the mechanism of choice for multi-network and specialized-NIC support, after a more invasive Pod-spec-modification approach was rejected upstream — the same DRA mechanism being built out for GPU/TPU device management.
- **Gateway API's gravity keeps increasing**: Ingress-NGINX's own maintainers moving toward it, plus a session literally cataloguing the remaining feature gaps, signals the migration pressure is now bidirectional (community push *and* maintainer pull) rather than CNCF evangelism alone.
- **Zero trust at scale is graduating from architecture talks to operations talks** — the standout identity sessions (Shopify mTLS automation, Sigstore identity-compromise threat modeling) are about the unglamorous lifecycle problems (rotation, revocation, recovery) rather than initial design, suggesting the field has moved past "should we do this" to "how do we operate this without an outage."
