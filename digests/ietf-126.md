<!--
conference: IETF 126 (Vienna)
type: standards
source_url: https://datatracker.ietf.org/meeting/126/agenda.json
generated: 2026-11-01
registry_key: ietf-126
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 126 (Vienna) — Digest

A standards meeting, so the unit of value is the draft, not the talk. Maturity matters: below, WG-adopted / WGLC documents (BGP-LS BGP-only fabric, EVPN First Hop Security, WIMSE credentials, Merkle Tree Certificates, OAuth-SPIFFE) are the ones closest to changing implementations; the AI-fabric drafts from IDR/RTG/SPRING are mostly early individual drafts but backed by unusually broad operator/vendor coalitions. Two clusters dominate this cycle: AI backend networking (adaptive routing, entropy, lossless WAN) and workload/agentic identity (WIMSE maturing, agent delegation exploding).

## Core

### Fully Adaptive Routing Ethernet using BGP

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xu-idr-fare/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-5-1-fully-adaptive-routing-ethernet-fare-00) · [Session recording](https://youtu.be/csKXfIQpUXs) · [Materials](https://datatracker.ietf.org/meeting/126/session/idr)

Qingliang Zhang (H3C), with co-authors from Tencent, Baidu, China Mobile, Yandex, HPE, Arrcus, Broadcom, Ruijie, Centec, Huawei and IEIT SYSTEMS.

- **Why**: AI training on 3–5 stage Clos fabrics needs non-blocking behavior; static per-flow ECMP collapses when a few large flows hash-collide onto one path. This is the most implementation-backed routing draft at the meeting.
- **What**: FARE-BGP — a BGP extension (path-bandwidth extended community) that lets switches do *weighted* ECMP based on real residual path capacity rather than uniform hashing. Version -05 adds handling for multiple BGP sessions per switch pair (bandwidth computed at node granularity, not session granularity) and packet forwarding over tunnels (WECMP applies to tunneled packets with loopback endpoints). The authors state the draft is ready for a WG adoption call.
- **How**: The prefix-originating node (e.g., leaf) attaches a maximum path-bandwidth value; each node computes `path bandwidth = min(aggregate parallel-link bandwidth, advertised value)` and either spreads the weight across ECMP paths or prunes the ECMP set so remaining links match the computed bandwidth.
- **Where applicable**: BGP-only AI/DC fabrics. Implemented by at least two cloud providers (China Mobile Cloud, Baidu Cloud) and six vendors, and adapted to 6+ switch ASIC generations — Broadcom Tomahawk 5 (51.2T) and Tomahawk 6 (102.4T), Nvidia Spectrum-4, Huawei SD58XX, Centec Arctic, Clounix CLX86. Explicitly multi-vendor, not org-specific.

### Fully Adaptive Routing Ethernet in Multi-Plane Scale-Out Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-xu-idr-fare-in-mpson/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-sessa-1-5-2-fully-adaptive-routing-ethernet-in-multi-plane-scale-out-networks-fare-in-mpson-00) · [Session recording](https://youtu.be/csKXfIQpUXs) · [Materials](https://datatracker.ietf.org/meeting/126/session/idr)

Yinben Xia, Weifeng Zhang (Tencent), Peilong Wang (Baidu), Haibo Wang (Huawei), and a large RNIC/switch author group (Broadcom, Intel, Ruijie, Yandex, China Mobile, GPU vendors).

- **Why**: ~100K-GPU clusters are moving to multi-plane scale-out topologies (RNIC multi-homed across disjoint planes, no inter-plane links) — which pushes path selection into the NIC. Route scale is the blocker: 4 planes × 100K host routes ≈ 400K routes, impractical on an RNIC.
- **What**: FARE-in-MPSON extends FARE-BGP from switches to RoCE NICs for multi-plane scale-out (complementing FARE-in-SUN for scale-up). It contributes two route-table suppression techniques: route aggregation with unreachability notification (zero-bandwidth community, or unreachable-prefix advertisement) and selective route filtering via Prefix ORF (RFC 5292), plus a transitive FIB-Suppress extended community so switches can omit RNIC host routes from FIB.
- **How**: BGP sessions terminate on RNICs; the RNIC evaluates per-plane reachability and path bandwidth for weighted ECMP. Because collectives mean each GPU talks to a limited peer set, RNICs can request only needed host routes; on unreachability they install a host route from the aggregate's remaining next-hops.
- **Where applicable**: Hyperscale multi-plane AI scale-out with RNIC-resident BGP — relies on predictable collective-communication peer sets. Version -00, very early, but the author list signals real industry intent.

### SRv6 for Deterministic Path Placement in AI Backends

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-filsfils-srv6ops-srv6-ai-backend/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-srv6ops-34-srv6-in-ai-backend-01) · [Session recording](https://youtu.be/kxTId7do_y4) · [Materials](https://datatracker.ietf.org/meeting/126/session/srv6ops)

Ahmed Abdelsalam (Cisco), on behalf of co-authors from Cisco, Microsoft, Oracle Cloud, IBM Cloud, NVIDIA and Arrcus.

- **Why**: This is the hyperscaler reference design for AI backends — the draft the SRv6/srv6ops community is rallying around, and it is requesting WG adoption at this meeting.
- **What**: Describes how SRv6 NEXT-CSID enables deterministic path placement: the NIC's transport stack encodes each path as an ordered segment list in the packet header, and the fabric forwards statelessly. It documents the MRC (Multipath Reliable Connection) design: packet spraying, ECN-based adaptive load balancing, out-of-order memory placement, selective retransmission, and packet trimming for incast — reaching 131,000 GPUs with only two tiers of switches (8×100Gb/s per host instead of 1×800Gb/s).
- **How**: Switches carry no per-flow state, no resilient-ECMP hashing, no BGP convergence logic; the end host steers deterministically and can recover from failures within one RTT. Loopback SRv6 probes allow path probing without a peer.
- **Where applicable**: Hyperscale production deployments (the deck cites OpenAI, Microsoft, and Oracle MRC+SRv6 deployments; rev04 adds Microsoft and Oracle as co-authors). Not directly transplantable to smaller estates, but it defines the pattern NICs and switches will be asked to support.

### BGP Link-State Extensions for BGP-only Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp-ls-bgp-only-fabric/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-idr-bgp-link-state-extensions-for-bgp-only-networks-00) · [Session recording](https://youtu.be/XclSKFBYC18) · [Materials](https://datatracker.ietf.org/meeting/126/session/idr)

Ketan Talaulikar, Aravind Babu MahendraBabu, Clarence Filsfils, Krishna Swamy (Cisco), Shawn Zandi (LinkedIn), Gaurav Dawra, Muhammad Durrani (Oracle).

- **Why**: BGP-only fabrics (increasingly the default in AI/ML DCs) lose the topology visibility that link-state IGPs give to FRR and TE computation. This WG document supplies it — and its new use cases tie directly into the two AI-backend drafts above.
- **What**: BGP-LS extensions (Protocol-ID 7) to advertise topology in BGP-only networks. Since IETF 125 it has added an IPFRR use case (LFA/TI-LFA/ERP in loss-sensitive AI Clos fabrics with strict convergence requirements) and SRv6 scenarios: unified SRv6 domain across DC frontend + WAN eliminating DCI gateway translation, and SR Policy computation for deterministic AI backend paths. Simplified procedures now reference RFC 9857/9514 directly.
- **How**: Standard BGP-LS address-family advertisement of nodes/links from the BGP-only fabric, consumed by controllers or local PCEs for path computation.
- **Where applicable**: Any BGP-only DC or WAN. Implemented in SONiC-FRR (merged FRR PR); IANA early allocation for the BGP Route Type TLV is done. Requesting WG review — mature and moving.

### A RoCEv2 Flow-Level Load Balancing Method Based on the IPv6 Flow Label

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-hu-6man-ipv6-flowlabel-load-balancing-rdma/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-6man-slides-126-6man-ipv6-flowlabel-load-balancing-rdma-01-00) · [Session recording](https://youtu.be/MR_SV1EFB6Y) · [Materials](https://datatracker.ietf.org/meeting/126/session/6man)

Jiayuan Hu (presenter), Jie Dong, Xia Gong.

- **Why**: The classic RoCEv2 load-balancing flaw: many parallel RDMA sessions from one host share an identical 5-tuple, so ECMP hashes them all to one path — elephant flows, congestion, loss in AI/HPC clusters.
- **What**: A 6man proposal to recover per-session entropy: the ingress network device parses the Queue Pair numbers (24-bit Source/Destination QP) from the RoCEv2 BTH/DETH headers, hashes them with the low 16 bits of each IPv6 address using CRC32, and writes the low 20 bits into the IPv6 Flow Label. Downstream devices then hash "5-tuple + Flow Label".
- **How**: CRC32 with init 0xFFFFFFFF — deliberately hardware/ASIC-friendly; only the Flow Label field is modified, so firewalls and NAT behavior are untouched and hosts are fully transparent to the mechanism.
- **Where applicable**: RoCEv2-over-IPv6 AI/HPC fabrics; requires ingress switch parsing capability. Early individual draft; the authors are asking for review, so expect evolution.

### Enhanced ECMP for AI Cluster

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cheng-rtgwg-enhanced-ecmp/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-08-enhanced-ecmp-for-ai-cluster-00) · [Session recording](https://youtu.be/0lOx_vRs1no) · [Materials](https://datatracker.ietf.org/meeting/126/session/rtgwg)

Weiqiang Cheng (China Mobile), Changwang Lin (New H3C Technologies).

- **Why**: In AI training the flow count is small, so per-flow ECMP hash collisions are proportionally more damaging; per-packet ECMP balances perfectly but reorders — unacceptable for RDMA without reordering support.
- **What**: Two complementary methods: (1) ingress-interface-group ECMP — group ingress interfaces and hash by in-group index so traffic from different ports lands on different ECMP egress ports; (2) egress-group ECMP — the egress leaf advertises a Group ID in a new BGP extended community (Router-ID + Group-ID, 6 bytes), and the ingress leaf maps flows to matching ECMP subgroups.
- **How**: Purely control-plane/local hashing changes; no datapath encapsulation. Method 1 suits balanced GPU ingress traffic, method 2 suits balanced egress traffic.
- **Where applicable**: Leaf-spine AI Clos. Individual draft -01 soliciting RTGWG feedback — with an explicit open question whether the BGP extended community should move to IDR. Overlaps in problem space with FARE and the flow-label draft but is a simpler, narrower fix.

### GSE architecture for AIDC

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-zhuang-rtgwg-aidc-gse-architecture/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-07-gse-architecture-for-aidc-00) · [Session recording](https://youtu.be/0lOx_vRs1no) · [Materials](https://datatracker.ietf.org/meeting/126/session/rtgwg)

Rui Zhuang (China Mobile), Sandy Zhang (ZTE).

- **Why**: A fundamentally different answer to AI-cluster congestion: instead of reactive ECN/PFC, schedule everything before sending. China Mobile/ZTE are fielding this, so it will surface in AIDC requirements even if it doesn't win in IETF.
- **What**: Global Scheduling Ethernet: credit-based authorization (a sender must get a bandwidth grant from the receiver-side last hop before transmitting), packet aggregation into uniform-size segments for forwarding, improved ECMP that sprays packets while preserving receiver-side ordering, and interworking with PFC/ECN. The draft presents intra-PoD (GPU-to-GPU credit negotiation) and inter-PoD (Leaf-to-Super-Spine) scenarios, with port IDs advertised via BGP (draft-zhang-idr-portid-ec).
- **How**: New Ethernet packet types carry a GSE header for uniform-size segments and for credit request/grant messages; switches recognize and forward GSE-framed traffic. PoDs from different vendors can interoperate by restoring original packets at the Core.
- **Where applicable**: AI data centers. Implemented in prototype hardware/software with "early performance data [showing] significant gains over traditional RoCE" — no numbers published yet. China Mobile-driven; treat as one contender for the post-RoCE AIDC architecture rather than a settled standard.

### PFC PAUSE Frame Forwarded Transparently in Wide Area Networks

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-he-rtgwg-wan-pfc/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-rtgwg-pfc-pause-frame-forwarded-transparently-in-wide-area-networks-00) · [Session recording](https://youtu.be/0lOx_vRs1no) · [Materials](https://datatracker.ietf.org/meeting/126/session/rtgwg)

Xiaoming He (China Telecom), Lijie Deng (China Telecom).

- **Why**: AI and distributed-storage workloads now run RDMA across metro/wide-area links between data centers; the draft's argument is that AIDC interconnect needs lossless WAN transmission, and hop-by-hop PFC in the WAN is both costly and amplifies head-of-line blocking, deadlock and congestion diffusion.
- **What**: China Telecom's proposal to carry PFC PAUSE frames *transparently* across the WAN: the egress PE validates the PFC frame (destination MAC must be 01-80-C2-00-00-01, source must be the directly-connected DC gateway port), encapsulates it in the DCI tunnel (SRv6, SR-MPLS, or VXLAN), and transit nodes forward it untouched; the ingress PE decapsulates, rewrites the source MAC to its own port, and delivers it to the source DC gateway. End-to-end flow control with zero PFC capability required in WAN nodes.
- **How**: The price is buffering: the destination DC gateway must reserve `Buffer > (R − T) × D` per priority queue, where D is the PFC propagation delay across the WAN — the draft's key engineering constraint.
- **Where applicable**: DCI/MAN interconnect of two AIDCs under one administrative intent. Individual draft -00; competing with the SRv6 approach below for the same problem.

### SRv6 behavior extention for Flow Control in WAN

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ruan-spring-priority-flow-control-sid/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-spring-srv6-behavior-extension-for-flow-control-in-wan-00) · [Session recording](https://youtu.be/3ui3EfTTLkA) · [Materials](https://datatracker.ietf.org/meeting/126/session/spring)

Zhengxin Han (China Unicom, presenter), Zheng Ruan, Yao Liu, MengYao Han, Ying Liu (China Unicom/ZTE).

- **Why**: The SRv6-flavored answer to the same lossless-WAN problem — with two advantages over transparent PFC: backpressure can traverse legacy non-PFC devices, and it can be scoped to per-tenant/slice queues instead of coarse port-level pausing. The SPRING list already reached consensus (June–July 2025) that a new SRv6 behavior is the preferred approach.
- **What**: A new `End.X.PFC` behavior that flags PFC-capable interfaces along an SRv6 path. PFC frames are encapsulated into *reverse* SRv6 tunnels whose final segment is the `End.X.PFC` SID of the target upstream interface, delivering backpressure precisely to the right node even across non-PFC legacy transit devices.
- **How**: Capability flooded via IGP (OSPF/IS-IS) and BGP-LS to a controller, which provisions reverse tunnels (E→C, C→A) before congestion; the data-plane pseudocode strips the outer IPv6/SRH on Ethernet next-header (143) and applies flow control when the PFC multicast MAC is seen.
- **Where applicable**: Inter-DC RDMA over L2VPN/L3VPN SRv6 policies in mixed PFC/legacy infrastructure; multi-tenant isolation via NRP/slice queues. Draft -03, actively seeking operator co-review.

### TCP Packet Trimming Extension

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-mazilu-tcpm-packet-trimming/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-tcpm-tcp-packet-trimming-slides-126-tcpm-packet-trimming-00) · [Session recording](https://youtu.be/pS7dKMeaHeE) · [Materials](https://datatracker.ietf.org/meeting/126/session/tcpm)

Flavius Mazilu, Valentin Bobaru, Costin Raiciu (University Politehnica of Bucharest).

- **Why**: Modern datacenter switch silicon (Arista, Broadcom Tomahawk 5, Nvidia, Juniper are all cited) already supports packet trimming — discard payload, keep the header, mark it — but TCP has no way to consume the signal. This is the host-side counterpart to a shipping hardware feature, and it mirrors the trimming used in the MRC/SRv6 AI-backend design above.
- **What**: A TCP extension: a "Trimming Permitted" option negotiated in the 3WHS; data packets then carry `DSCP_TRIMMABLE`; when a switch trims, the receiver gets the header (with `DSCP_TRIMMED` and updated IP checksum — TCP checksum is intentionally invalid) and returns a NACK option carrying the trimmed packet's sequence number. The sender treats the NACK as an explicit loss/congestion signal and enters fast recovery — deterministic loss recovery instead of SACK/RACK inference.
- **How**: Optional two-queues-per-port scheme puts trimmed packets on a higher-priority queue so NACKs return quickly; NACKs could get their own DSCP (Ultra Ethernet's UET proposes `DSCP_CONTROL` for exactly this).
- **Where applicable**: Data centers and controlled administrative domains only — explicitly not for the open Internet. Draft -00 with open questions (checksum handling, congestion-control response) posed to TCPM; watch whether the WG picks it up.

### EVPN First Hop Security

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-first-hop-security/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-bess-evpn-first-hop-security-00) · [Session recording](https://youtu.be/3lzjKPn9HdE) · [Materials](https://datatracker.ietf.org/meeting/126/session/bess)

Ali Sajassi, Lukas Krattiger, Krishna Ananthamurthy (Cisco), Jorge Rabadan (Nokia), Wen Lin (Juniper).

- **Why**: First Hop Security functions (DHCP snooping, DAI, ND Inspection, Source Guard) depend on a local DHCP snoop binding database — which silently breaks in EVPN fabrics where hosts move and multi-home across PEs, causing legitimate traffic to be dropped or spoofed traffic to pass.
- **What**: A WG-adopted BESS draft defining a new EVPN BGP route to distribute and synchronize DHCP snooping bindings (IPv4/IPv6-to-MAC, binding state, lease/create time) among all PEs in an EVI, covering host mobility, multi-homing, and distributed IRB.
- **How**: Straightforward BGP route distribution with binding attributes; major technical issues are resolved and the authors consider the document ready for Working Group Last Call.
- **Where applicable**: Any EVPN datacenter or campus fabric running FHS — broadly applicable, multi-vendor co-authored, and the most mature item in the DC-security space at this meeting.

### Merkle Tree Certificates

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) · [Session recording](https://youtu.be/0DOjvhF7VgU) · [Materials](https://datatracker.ietf.org/meeting/126/session/acme)

David Benjamin (Google), Devon O'Brien (Apple), Bas Westerbaan, Luke Valenta (Cloudflare), Filippo Valsorda (Geomys).

- **Why**: The PKI arithmetic problem: post-quantum signatures are huge (ML-DSA-44: 2,420 bytes/sig; ML-DSA-65: 3,309) and certificate lifetimes are shrinking — two SCTs plus a leaf signature adds ~7,260–9,927 bytes of authentication overhead, and CT log storage scales with entry size and issuance rate. MTCs redesign the certificate to survive both trends.
- **What**: A new X.509-adjacent certificate form where the CA *certifies by logging*: it appends TBSCertificate entries to append-only issuance logs, signs checkpoints and subtrees, and independent cosigners attest correct (optionally mirrored) operation. A certificate is the tbscert + a Merkle inclusion proof + cosignatures — log entries contain hashes instead of public keys and no signatures, so they don't scale with PQ key/sig size. An optional "landmark-relative" certificate eliminates signatures entirely for up-to-date relying parties, and "revoked ranges" let RPs bulk-discard long-expired log entries so monitoring infrastructure scales by retention policy, not log lifetime.
- **How**: Uses a "subtree" Merkle primitive (inclusion and consistency proofs) so proofs stay small; ACME extensions (Section 9, the part presented in Vienna) define issuance; TLS use covers both standalone and landmark-relative forms.
- **Where applicable**: Public web PKI first, but the mechanism is general. This is a WG document (PLANTS) now at -07 — the most mature PKI redesign on the IETF's table, with the browser/CDN ecosystem already at the table.

### OAuth SPIFFE Client Authentication

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-spiffe-client-auth/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-sessa-oauth-spiffe-client-authentication-00) · [Session recording](https://youtu.be/yhE1FL8VW7E) · [Materials](https://datatracker.ietf.org/meeting/126/session/oauth)

Stian Thorgersen, Scott Rose, Nancy Cam-Winget, Pieter Kasselman, Arndt Schwenkschuster.

- **Why**: Workloads acting as OAuth clients today authenticate with static, long-lived client secrets — exactly the secret-sprawl problem SPIFFE/SPIRE exists to eliminate. This WG draft bridges the two worlds.
- **What**: Profiles RFC 7521/7523, RFC 8705 (mTLS), and the attestation-based client-auth draft so JWT-SVIDs, X.509-SVIDs and WIT-SVIDs work as OAuth client credentials with no client secrets. Crucially it *removes* the "assertion subject == client_id" restriction of RFC 7521, since SPIFFE IDs are infrastructure-opinionated (`spiffe://example.org/us-east-1/cluster-A/service-Z/instance-1`) while OAuth client IDs are service-scoped and many workloads share one client.
- **How**: The open problem is SPIFFE-ID → client-ID mapping, with three contending approaches: direct list, open-ended prefix wildcards, or path-segment wildcards — described as the last big remaining item.
- **Where applicable**: Any shop running SPIRE/SPIFFE alongside an OAuth authorization server (the deck cites Entra, Google managed workload identity, Uber, Netflix, ByteDance deployments of SVIDs). WG document; blocked mainly on the WIT dependency (in WGLC) and mapping semantics.

### Workload Identifier Origin Hint for TLS ClientHello

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-rosomakho-tls-wimse-cert-hint/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-tls-sessa-workload-identifier-scope-hint-00) · [Session recording](https://youtu.be/RO-Drvzquc4) · [Materials](https://datatracker.ietf.org/meeting/126/session/tls)

Yaroslav Rosomakho, Jonathan Hoyland.

- **Why**: mTLS between workloads has an awkward bootstrap: a client can't know which cert/trust domain a server will accept, and servers can't enumerate acceptable trust domains — so deployments burn separate TLS endpoints. This fixes that with a small wire-format change.
- **What**: A TLS ClientHello extension carrying one or more workload identifier *origins* (URI scheme + trust domain, drawn from the WIMSE identifier format). Presence of the extension signals the client won't choke on a CertificateRequest and can produce a certificate for a listed scope; the server uses the hint to decide whether client auth is required and which trust anchors apply.
- **How**: An empty list is valid and degenerates into a "request mTLS" flag; for privacy, combine with ECH — empty list in the Outer ClientHello, real scopes in the Inner.
- **Where applicable**: Cross-organization workload mTLS (the motivating case: a server with trust relationships with thousands of customer trust domains). Individual draft -02, with the authors asking whether there's appetite for an adoption call — this is the piece that makes WIMSE credentials usable in the TLS handshake.

### WIMSE Workload Credentials

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-workload-credentials-witwic-01) · [Session recording](https://youtu.be/0a4HZRJ5d9c) · [Materials](https://datatracker.ietf.org/meeting/126/session/wimse)

Brian Campbell (Ping Identity), Joe Salowey (CyberArk), Arndt Schwenkschuster (Defakto Security), Yaron Sheffer (Intuit), Yaroslav Rosomakho (Zscaler).

- **Why**: The credential layer of the workload-identity stack that OAuth-SPIFFE, the TLS hint, and the agent drafts all build on — and it was in Working Group Last Call at this meeting.
- **What**: Defines the Workload Identity Token (WIT, a JWT) and Workload Identity Certificate (WIC, X.509) that bind a key to a workload's WIMSE identifier, usable across protocols; proof-of-possession mechanisms are deliberately out of scope and defined in companion documents.
- **How**: Credential formats only — the separation of "what the credential is" from "how you prove possession" is the draft's main design contribution, letting the same credential work over mTLS, HTTP signatures, and proof tokens.
- **Where applicable**: Any runtime in the WIMSE architecture, from basic single-service to multi-cloud multi-tenant. WG document past WGLC; the presentation indicated the road likely ends (i.e., publication) before the next meeting.

### WIMSE Trust Domain Discovery

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-schwenkschuster-wimse-trust-domain-discovery/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-wimse-trust-domain-discovery-00) · [Session recording](https://youtu.be/0a4HZRJ5d9c) · [Materials](https://datatracker.ietf.org/meeting/126/session/wimse)

Arndt Schwenkschuster, Yaroslav Rosomakho.

- **Why**: WIMSE scopes identifiers to a trust domain but leaves *how a relying party obtains that domain's trust anchors* undefined — the exact gap SPIFFE fills with the Bundle Endpoint. In open environments with no prior relationship, that gap blocks any cross-org WIMSE deployment.
- **What**: Defines the WIMSE Trust Bundle (JWKS-formatted, with `use` values distinguishing `wimse-jwt` and `wimse-x509` signing material for both credential types) and a Trust Domain Metadata document at `/.well-known/wimse-trust-domain` (redirects allowed) that resolves a trust-domain name to its bundle endpoint.
- **How**: A domain owner serves metadata and bundle publicly over HTTPS, mirroring the OIDC metadata/SPIFFE bundle patterns; private deployments can serve them privately or use `.internal` TLDs with different distribution.
- **Where applicable**: Open federation-style workload identity. Individual draft asking "do we agree on the problem space?" — early, but it's the missing interoperability piece for the mature WIMSE credential docs.

### AI Agent Authentication and Authorization

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-aims-00) · [Session recording](https://youtu.be/0a4HZRJ5d9c) · [Materials](https://datatracker.ietf.org/meeting/126/session/wimse)

Nick Steele (OpenAI), Aaron Parecki (Okta), Jeff Lombardo (AWS), Brian Campbell (Ping Identity), Yaroslav Rosomakho (Zscaler), Pieter Kasselman (Defakto Security).

- **Why**: The strongest single framework document in the agent-identity land rush: deliberately anti-"invent a new AI protocol," it maps existing standards onto agent communications and surgically identifies what's missing. The author list (OpenAI, Okta, AWS) signals real platform intent.
- **What**: An informational draft ("AIMS") covering the full stack: exactly one WIMSE identifier per agent (may be a SPIFFE ID); primary credentials as WIMSE WIC/WIT or SPIFFE SVIDs, secondary via OAuth token exchange and Transaction Tokens; authentication at transport (mTLS with workload X.509) or application layer (WIMSE proof tokens, RFC 9421 HTTP signatures over WIT); OAuth for delegated authorization including human-in-the-loop (noting CIBA doesn't fit mid-execution pauses); SSF/CAEP for continuous posture signals; policy and compliance explicitly out of scope.
- **How**: Composition of existing specs with gaps named — the value is the map, not new mechanics.
- **Where applicable**: Agent-to-LLM/tool/service/agent interactions generally. Requesting chairs consider WG adoption as a work item; expect it to become the umbrella the other agent drafts hang from.

### Agent Authorization use cases and gap analysis

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-chen-oauth-agent-authz-use-cases/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-agent-authorization-use-cases-and-gap-analysis-00) · [Session recording](https://youtu.be/yhE1FL8VW7E) · [Materials](https://datatracker.ietf.org/meeting/126/session/oauth)

Meiling Chen (China Mobile).

- **Why**: The requirements document that justifies (and scopes) the OAuth WG's agent work — read it to understand *why* AIMS, PEDIGREE and delegate SD-JWT all exist.
- **What**: Ten use cases across consumer, enterprise and security scenarios, each with authorization requirements and gaps: intent-to-permission mapping and interactive consent loops for personal assistants; scope explosion and missing conditional context in smart homes; the confused-deputy/agent-flagging problem when agents hit human-facing services (the "agent downloads 400 papers and gets the user's account banned" example); multi-hop delegation chains and group authorization for agent teams; and global/bulk revocation gaps (RFC 7009 revokes one token at a time — useless in an incident).
- **How**: Gap analysis against RAR (too static), DPoP (fixed keys break agent migration), Transaction Tokens (internal-only), and CIMD (no agent metadata, no delegation traceability), each with proposed optimizations like attenuating agent tokens and `parent_agent_id` claims.
- **Where applicable**: Vendor-neutral; informational individual draft -01 with biweekly open meetings — the input document for whatever OAuth extensions follow.

### PEDIGREE: Verifiable Delegation Identity for Agentic AI Systems

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-rampalli-pedigree/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-karthikrampalli-pedigree-deck-00) · [Session recording](https://youtu.be/0a4HZRJ5d9c) · [Materials](https://datatracker.ietf.org/meeting/126/session/wimse)

Karthik Rampalli.

- **Why**: The sharpest statement of the agentic-authorization failure mode: an orchestrator takes one human consent and spawns sub-agents that all inherit its ambient credentials — so a relying party cannot tell which agent acted, on whose authority, or within what limits. A bad charge can't be attributed.
- **What**: A delegation-identity layer *above* workload credentials (WIT/WIC or X.509 SVID, unmodified). The SIT is a signed JWT (`typ pedigree+jwt`, EdDSA) with a parent chain, scopes, a Cedar-encoded mandate, an operator ceiling reference, consent chain and delegation depth. Its three claimed advances over AAuth and AIP: monotonic scope attenuation enforced at mint and verify (AAuth explicitly rejects attenuation), dual-layer authority enforcement (per-parent mandate AND operator ceiling — a single-layer guard fails when the orchestrator is compromised), and strict cryptographic re-verification of every parent SIT, catching parent-swap attacks that append-only token chains miss.
- **How**: Relying parties evaluate three inputs — workload credential, SIT chain, local policy + operator ceiling — with Cedar static-analysis proofs of narrowing; revocation is bounded-staleness and fail-closed, explicitly not real-time.
- **Where applicable**: Any multi-agent orchestration where sub-agents act under delegated human authority. Very early individual draft — the deck is candid that wire details still belong on the mailing list — but the three-tests framing (attribution, attenuation, enforcement) is the right vocabulary for this problem space.

### Delegate SD-JWT

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-gco-oauth-delegate-sd-jwt/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-oauth-delegate-sd-jwts-00) · [Session recording](https://youtu.be/XxkhXxInz3k) · [Materials](https://datatracker.ietf.org/meeting/126/session/oauth)

Gareth Oliver (Google).

- **Why**: Delegation of verifiable credentials with selective disclosure — the exact mechanism agentic payments need (user authorizes an agent to spend, merchant/bank sees only the delegated slice) and that plain SD-JWTs can't express.
- **What**: An extension letting a Holder delegate to a Delegate Holder by making the Key Binding JWT itself an SD-JWT with its own disclosures and its own key binding: `<issuer-jwt>~<disclosures>~~<kb-sd-jwt>~<disclosures>~<kb-jwt>`. The whole design fits in that one line — the delegation is a holder-signed SD-JWT whose payload hashes and binds the issuer's original (`sd_hash`, `cnf` for the delegate's key).
- **How**: Standard SD-JWT disclosure machinery at each layer; the verifier sees the issuer credential, the holder's delegation statement with narrowed/selective claims, and the delegate's proof of possession.
- **Where applicable**: Agentic systems and digital-credential delegation (power-of-attorney and vehicle-registration examples given). Individual draft; open questions include a common delegation policy language (aud, exp-style) and where revocation status lists are hosted.

## Adjacent

### WIMSE Workload-to-Workload Authentication with HTTP Signatures

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-wimse-http-signatures-00) · [Session recording](https://youtu.be/0a4HZRJ5d9c) · [Materials](https://datatracker.ietf.org/meeting/126/session/wimse)

Joe Salowey (CyberArk), Yaron Sheffer (Intuit).

- **Why**: The application-layer leg of WIMSE — authentication that survives the TLS-terminating proxies and load balancers that dominate real service topologies, which the PM's mesh/ingress world knows well.
- **What**: WG draft -04 requesting WGLC. Two changes since -02: the audience indicator moved from a bespoke `Wimse-Audience` header to a `wimse-aud` HTTP Signatures parameter (still URI-shaped), letting a recipient confirm the signed message targets it; and a `wimse-req-nonce` parameter copies the request's random nonce into the signed response, closing a cut-and-paste attack where an on-path malicious proxy splices a valid response into the wrong request — RFC 9421 signs request and response but doesn't bind them.
- **How**: RFC 9421 signatures over the Workload Identity Token and request components; response signing optional but recommended given the assumed-malicious-proxy threat model.
- **Where applicable**: HTTP-based workload-to-workload traffic only (other protocols use other WIMSE proof mechanisms); needs updating of the draft's examples for the new parameters.

### Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-acme-rats/) · [Session recording](https://youtu.be/0DOjvhF7VgU) · [Materials](https://datatracker.ietf.org/meeting/126/session/acme)

Peter Chunchi Liu (Huawei), Mike Ounsworth (Cryptic Forest Software), Michael Richardson (Sandelman Software Works), Ganesh Mallaya (AppViewX), Sven Rajala (Keyfactor).

- **Why**: Where device attestation meets automated certificate issuance: enterprises increasingly want to issue client (and server) certificates only to devices that can *prove* their posture — measured boot, HSM-held keys, MDM registration — and ACME had no standardized way to ask.
- **What**: A WG document (-03) defining a `remote-attestation` identifier type whose value is a property hint (`measured-boot`, `hsm`, …) rather than a real identifier, plus a `remote-attest-01` challenge answered with a RATS Conceptual Message Wrapper (CMW) in any supported format (EAT, WebAuthn, TPM). The challenge object carries a `freshnessNonce`, an optional `attestClaimsHint` listing claims the server wants attested, and a `verifierEncryptionCredential` (JWK) so sensitive evidence can be JWE-encrypted in transit. The design supports both the RATS Passport model (attestation-result-01, mandatory to implement) and Background Check model (encrypted evidence), and is explicitly supplemental — the client still satisfies DNS-01/HTTP-01 for the identifiers that go into the certificate.
- **How**: A pseudo-identifier plus challenge/response in the existing ACME order flow; verification and appraisal policy remain the CA's business.
- **Where applicable**: Enterprise client certs, WiFi/EAP-TLS onboarding, BYOD S/MIME, code-signing keys in HSMs. Complementary to (broader than) the WebAuthn-based ACME Device Attestation extension; also worth reading alongside V-PEA below, which generalizes the same WHAT+environment idea.

## Wildcard

### IS-IS Support For The Power Conserving Path Placement Strategy (PCPPS)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-many-lsr-power-group/) · [Session recording](https://youtu.be/ExzDVs2e4o0) · [Materials](https://datatracker.ietf.org/meeting/126/session/lsr)

Colby Barth (Juniper), Tony Li, Vishnu Pavan Beeram, Ron Bonica (HPE).

- **Why**: Not AI, not identity — but the signal that *energy* is entering the IGP standards track. PCPPS inverts usual traffic engineering: concentrate traffic onto a small set of links so the rest can be powered down until needed.
- **What**: The IS-IS encoding for the power-state information that I-D.many-teas-power-steering's Power Conserving Path Placement Strategy needs distributed by an IGP. Notably, this individual draft has since been replaced by `draft-ietf-lsr-pcpps` with a call for WG adoption issued — i.e., LSR picked it up right after this meeting.
- **How**: IGP advertisement of the information a PCPPS computation needs to know which resources can be safely idled. (Write-up from the abstract and datatracker status; no slides were available.)
- **Where applicable**: WAN/operator networks where energy cost is a first-order routing input. Interesting tension with the AI-fabric work elsewhere in this digest, which wants maximum parallelism, not consolidation — expect the two objectives to collide in DC design discussions.

### Reverso for the QUIC protocol

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-frochet-quicwg-reverso-for-quic/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-quic-reverso-for-quic-00) · [Session recording](https://youtu.be/Pzy_4svJ4vY) · [Materials](https://datatracker.ietf.org/meeting/126/session/quic)

Florentin Rochet (University of Namur).

- **Why**: A genuinely surprising transport result: QUIC v1's wire layout — encrypted data potentially surrounded by encrypted control — makes *contiguous zero-copy at the receiver impossible* in a conforming implementation. This draft proposes a QUIC version that fixes it, and it's grounded in a published paper (ACM SIGCOMM CCR, Jan 2026).
- **What**: vReverso changes three things from v1: a few more bytes in the short header (worst case 13 vs 5 — a stream ID and offset), a stream frame must be first in the packet, and frame element ordering is *reversed on the wire*. That's enough to drive data reassembly using decryption's hidden copy, so a receiver can expose a whole HTTP/3 data frame of arbitrary size in zero-copy.
- **How**: Reversed frame ordering minimizes added header info (no need to locate where control begins), and a bidirectional buffer abstraction means the same code parses both v1 and vReverso. Loopback microbenchmarks show ~15.4 Gb/s for the prototype vs ~15.2 Gb/s QUIC v1 on comparable stacks — the author himself flags these numbers as "to be taken with a grain of salt."
- **Where applicable**: Receiver-side throughput optimization for QUIC and derivatives (QMux is called out). Early individual draft with real maintenance-cost questions, but a rare case of wire-format research feeding directly into a standards venue.

### Verifiable Proof of Environment Attestation Profile

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-lkspa-rats-verifiable-geo-fence/) · [Slides](https://datatracker.ietf.org/meeting/126/materials/slides-126-rats-verifiable-proof-of-environment-attestation-profile-v-pea-00) · [Session recording](https://youtu.be/IhxaSHCwdv0) · [Materials](https://datatracker.ietf.org/meeting/126/session/rats)

Michael Richardson (presenter), with R. Krishnan (JPMorgan Chase), N. Smith, D. Lopez (Telefonica), A. Prasad (Oracle), S. Addepalli (Aryaka), H. Birkholz (Fraunhofer SIT).

- **Why**: Sovereignty and regulated-deployment requirements (RBI India, Korea's spatial-data act, GDPR) are demanding *provable* geographic residency — and nothing today cryptographically links a workload's identity, its execution integrity, and its location. This draft fuses them.
- **What**: V-PEA (formerly the verifiable geofencing draft) is a profile of the RATS architecture (RFC 9334) that binds two hardware-rooted dimensions into one TPM-sealed Evidence object: WHAT (TPM provenance, platform/boot integrity, workload-agent binary digest) and WHERE (physical residency per GNSS/MNO/timing location sources, with Galileo OSNMA and multi-constellation cross-checks against spoofing added since IETF 125). Neither dimension can be forged or transplanted without invalidating the other, and the credential is issued only if both pass. The WHERE dimension supports transparent zero-knowledge proofs so an Attester can prove in-boundary compliance without disclosing coordinates. A WIMSE Integration appendix ties the Attestation Result to credential issuance.
- **How**: Location sources produce signed claims; a TPM quote seal binds them to the platform's integrity Evidence; a Verifier appraises, and the result can be embedded in standard X.509 so downstream consumers never need to understand RATS. Running code exists (LF Edge AegisSovereignAI: TPM 2.0, SPIRE, Keylime, Plonky2 ZKP).
- **Where applicable**: Regulated, sovereign, high-assurance deployments rather than general web workloads — but as hardware-rooted identity meets workload identity (see AIMS/OAuth-SPIFFE above), this is where attestation-gated credential issuance is heading. The draft was presented as a call for RATS WG adoption.

## Themes

- **AI fabrics have captured the routing area.** IDR, RTG, SPRING and srv6ops sessions are dominated by one problem: making 100K-GPU Clos/multi-plane fabrics non-blocking. Adaptive routing (FARE, FARE-in-MPSON), entropy recovery (flow-label, enhanced ECMP), and scheduling (GSE) are competing answers, and the unusually broad operator/ASIC-vendor author lists (Tomahawk 5/6, Spectrum-4 ports already done) say this is deployment-driven, not academic.
- **Lossless is escaping the datacenter.** Three drafts attack the same new requirement — RDMA over WAN/DCI — with different mechanics: transparently tunneled PFC PAUSE frames (rtgwg), PFC backpressure in reverse SRv6 tunnels with per-tenant granularity (spring), and multi-DC fabrics via BGP-LS/SRv6. The industry has decided cross-DC AI training is a WAN problem; the mechanism is unsettled.
- **Switches are becoming signal emitters, and host stacks must listen.** Packet trimming is shipping in Arista/Broadcom/Nvidia/Juniper silicon, and now TCP (TCPM draft) and transport designs (MRC, UET's DSCP_CONTROL) are being extended to consume in-band congestion/trim signals — a real host/network contract shift worth tracking for NIC and OS roadmaps.
- **Workload identity has crossed into standards maturity.** WIMSE credentials passed WGLC, HTTP signatures are requesting it, OAuth-SPIFFE is one mapping decision from done, and the TLS ClientHello hint plus trust-domain discovery fill the remaining handshake and federation gaps. The SPIFFE/SPIRE world is being standardized piece by piece, and the pieces now reference each other.
- **Agentic identity is the new land rush — early, overlapping, unresolved.** AIMS (use existing standards, don't invent), PEDIGREE (per-hop attenuating delegation), delegate SD-JWT, and the OAuth use-case gap analysis all attack delegation/attribution/revocation from different angles, with AAuth and AIP outside this selection. Watch adoption calls: whichever framework the OAuth/WIMSE WGs bless will define interop for agent platforms.
- **PQ pressure is forcing PKI redesign, and energy is entering the IGP.** Merkle Tree Certificates at -07 (log-size-free entries, signature-free landmark certs) is the concrete response to ML-DSA sizes plus short-lived certs; meanwhile PCPPS — concentrating traffic so links can be powered down — has been adopted by LSR, adding an objective (energy) that runs directly against the AI fabric's maximize-parallelism instinct.
