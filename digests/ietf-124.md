<!--
conference: IETF 124 (Montreal)
type: standards
source_url: https://datatracker.ietf.org/meeting/124/agenda.json
generated: 2026-11-01
registry_key: ietf-124
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# IETF 124 (Montreal) — Digest

A working-group program, so this digest reads the drafts, not the talks: what is moving toward consensus, what changed in wire formats or security/identity mechanisms, and what is still an individual contribution. The dominant gravity this cycle is AI-fabric networking (FANTEL fast notifications, GLB in Clos fabrics, lossless RDMA over WAN) and a very active workload-identity cluster (WIMSE, SPIFFE–OAuth, transaction tokens).

## Core

### Fast Network Notifications Problem Statement

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-dong-fantel-problem-statement/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-06-network-notifications-problem-statement-00) · [Session recording](https://youtu.be/cFekE0TpHng) · [Materials](https://datatracker.ietf.org/meeting/124/session/rtgwg)

Jie Dong (Huawei), Mike McBride (Futurewei), François Clad (Cisco), Zhaohui (Jeffrey) Zhang (Juniper), with contributors from China Telecom, China Mobile, China Unicom, Tencent, Telefónica, and Turkcell

- **Why**: AI training/inference and large-scale cloud services need the network to adapt faster than today's feedback loops allow. This is the anchor problem statement for the whole FANTEL (Fast Notifications for TE and Load Balancing) cluster in RTGWG, carried forward from the IETF 123 BoF with unusual breadth of operator/vendor co-authorship.
- **What**: A structured problem statement defining what fast network notifications must carry, who must receive them, and how they get delivered — the requirements frame every other fast-notification draft at this meeting builds against.
- **How**: Tabulates four gaps in current mechanisms: (1) hop-by-hop control-plane distribution and round-trip end-to-end signaling (ECN) are too slow; (2) binary/threshold feedback is too coarse for precise adjustment; (3) decisions are made from a local view, yielding sub-optimal rerouting; (4) naive wide distribution churns the control plane. Proposes an information model (event type, location, fine-grained metrics such as utilization, queue length, delay, jitter, loss, plus path and flow 5-tuple identification), a recipient model (adjacent/non-adjacent routers, ingress nodes, end hosts, controllers/PCE/NMS), and delivery modes (unicast, multicast, hop-by-hop, scoped flooding) with subscription to suppress overhead.
- **Where applicable**: General IP fabrics — use cases span intra-DC AI/ML, cross-DC training and inference, CDN/DC interconnect, and cloud-edge. Early-stage at the meeting (individual draft `-01`), but companion drafts now cite it on the WG track as `draft-ietf-rtgwg-net-notif-ps`, so adoption momentum is real.

### Fast Notification for tunnel-based lossless RDMA transmission in WAN

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-hzh-fantel-wan-tunnel/) · [Session recording](https://youtu.be/cFekE0TpHng) · [Materials](https://datatracker.ietf.org/meeting/124/session/rtgwg)

Zehua Hu, Yongqing Zhu, Jiayuan Hu, Tanxin Pi (China Telecom)

- **Why**: Cross-AIDC LLM training and inference push RDMA through SRv6/GRE/VXLAN/MPLS tunnels over the WAN; a small number of losses collapses effective throughput, and neither ECN (end-to-end, long RTTs) nor PFC (link-local, DC-only) works there.
- **What**: A concrete Fast Network Notification (FANN) protocol: transit (P) nodes detecting failure, congestion, or state change send structured notifications to the ingress PE, which reroutes to backup paths, rebalances across available paths, and/or throttles the affected traffic and notifies the sender and controller.
- **How**: Defines a new ICMPv6 message — Code distinguishes event vs. recovery, a Hop Limit bounds propagation scope, Event Type covers link failure, congestion, performance degradation, microburst, signal degradation, and queue buildup (with sub-types, e.g., congestion severity tiers), a microsecond timestamp, the originating node's IPv6 address, and a 32-bit bitmap selecting fixed-length metadata fields (ingress/egress port IDs, link utilization, loss, latency, jitter, queue and buffer occupancy, flow 5-tuple, and a path ID carried as an SRv6 SID list or MPLS label stack). An identical structure can ride over UDP on a well-known port where ICMPv6 is filtered. Security: RFC 4443 rate limiting, length validation, and origination only from control-plane interfaces.
- **Where applicable**: Carrier inter-DC WANs carrying tunnelled RDMA (China Telecom is the driving operator — this is operator-specific in origin, general in technique). Individual draft at `-03`; the protocol encoding is draft-stage and the FANN umbrella has competing notification proposals (ARN etc.) it must converge with.

### Credit-based Flow Control Based on RSVP for RDMA transmission in WAN

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-hu-rtgwg-cbfc-rsvp/) · [Session recording](https://youtu.be/cFekE0TpHng) · [Materials](https://datatracker.ietf.org/meeting/124/session/rtgwg)

Jiayuan Hu, Zehua Hu, Tanxin Pi, Yongqing Zhu (China Telecom)

- **Why**: The other half of lossless WAN RDMA: instead of notify-and-reroute, backpressure — credit-based flow control (the InfiniBand model) extended across the WAN for cross-AIDC training with elephant flows and extreme concurrency.
- **What**: A credit-based flow control mechanism for RDMA traffic in SRv6 tunnels over the WAN, carried by an extended RSVP, aiming to provide high-throughput, zero-packet-loss transmission guarantees (from abstract only).
- **How**: Introduces credit grants into RSVP signaling so that senders transmit only against granted credits, giving precise per-flow traffic control across SRv6 tunnels rather than drop-based or ECN-based response.
- **Where applicable**: Cross-data-center AI training over SRv6 WAN — a China Telecom carrier scenario. Very early: an individual draft whose current revision (`-01`, September 2025) has actually expired on Datatracker without a replacement, so momentum is uncertain; treat as a design signal, not a trajectory, and watch whether it is revived or folded into the broader FANTEL work.

### Scheduling Network Resources for Machine Learning Clusters

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-kompella-rtgwg-mlnwsched/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-rtgwg-05-scheduling-network-resources-for-machine-learning-clusters-00) · [Session recording](https://youtu.be/cFekE0TpHng) · [Materials](https://datatracker.ietf.org/meeting/124/session/rtgwg)

Kompella (individual draft, rtgwg)

- **Why**: Everything else at this meeting reacts to congestion; this draft argues the AI network should be *scheduled* like compute — a provocative reframe from "detect and signal" to "reserve in advance," with real implications for how TE and schedulers integrate.
- **What**: A framework proposing that network resources (bandwidth, buffers, queues) be estimated, allocated, and deployed alongside compute for training/inference jobs, with contingency paths — citing SLURM and NVIDIA's KAI Scheduler as the compute-side model and the FANTEL/@Scale/OCP discussions as context.
- **How**: Scheduling happens at compute-placement time (job size/type imply communication needs) and again when a communication phase starts (CCL API invocations reveal exact endpoints and mode — broadcast, scatter, gather, all-reduce). Uses multipath TE (MPTE) with resource reservation for unicast CCL primitives and multicast TE (MCTE, companion `draft-kompella-teas-mcte`) for multicast primitives. A key argument: reservation state means transit nodes know the sources, so congestion/event signaling can be sent to the right places (ingresses), and reserved alternates give fast recovery — proactive and reactive mechanisms compose.
- **Where applicable**: Intra-DC backend networks (multipathing mandatory, unicast + multicast required), inter-DC DCI for distributed training, and metro/WAN edge inference. Early position/framework draft; broadly applicable to anyone running scheduled AI workloads, hypercaler and carrier alike.

### BGP Next-next Hop Nodes

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-next-next-hop-nodes/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-8-bgp-next-next-hop-nodes-00) · [Session recording](https://youtu.be/fFc0kGI5arw) · [Materials](https://datatracker.ietf.org/meeting/124/session/idr)

Kevin Wang, Jeff Haas, Changwang Lin, Jeff Tantsura (Juniper)

- **Why**: AI/ML Clos fabrics carry high-throughput, low-entropy flows that random ECMP hashing cannot keep drop-free; local remedies (dynamic load balancing) can't see remote-link congestion. This draft is the BGP standardization of the topology discovery that Global Load Balancing (GLB) needs.
- **What**: The NNHN characteristic for the NHC attribute, letting a leaf learn `<next-hop, next-next-hop>` tuples per route. Presented with GLB test results: on a 3-stage Clos with 100G links, a 90G flow that drops without GLB runs drop-free with it.
- **How**: The key insight is that Clos symmetry means only next-hop and next-next-hop link congestion matters — congestion beyond that is absorbed by symmetric GLB at higher tiers — so a non-link-state protocol like BGP suffices for GLB topology discovery. BGP carries next-next-hop BGP IDs in a new NHC TLV; each spine broadcasts link quality to direct neighbors (sub-millisecond, via the companion UDP router-info protocol `draft-zzhang-rtgwg-router-info`'s Neighbor Path Information TLV), and each leaf combines the two-hop link qualities to steer load. Works for 3-stage, 5-stage, and general Clos.
- **Where applicable**: IP/IPv6-routed BGP Clos fabrics — i.e., modern AI back-end networks. WG draft (`draft-ietf-idr-next-next-hop-nodes-00`) at first presentation: early on the WG track, but with working multi-party test evidence. The single most directly relevant AI-fabric item in the program.

### BGP Next Hop Dependent Characteristics Attribute

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-entropy-label/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-split-of-draft-ietf-idr-entropy-label-01) · [Session recording](https://youtu.be/fFc0kGI5arw) · [Materials](https://datatracker.ietf.org/meeting/124/session/idr)

John Scudder (Juniper) presenting the split of draft-ietf-idr-entropy-label

- **Why**: NHC is the base container for per-next-hop forwarding-plane signaling in BGP — three other WG drafts (next-next-hop-nodes, iFIT capabilities, generic metric) now define their own NHC characteristics on top of it. The session resolves a two-year stall that was blocking them.
- **What**: The NHC attribute — a transitive BGP attribute, extensible via TLVs, that conveys characteristics of the routes advertised in the UPDATE that carries it (unlike RFC 5492 capabilities). News at IETF 124: the parked `draft-ietf-idr-entropy-label` (WGLC'd November 2023, stuck "waiting for implementation") was split into `draft-ietf-idr-nhc` (the attribute plus a BGP Identifier characteristic) and `draft-ietf-idr-elc` (the Entropy Label Characteristic) — "nothing added or taken away."
- **How**: Two implementations of NHC exist; the split (chairs' consensus call, no objections) separates the twice-implemented base from ELC, which still awaits a second implementation, and unblocks the registry the dependent drafts need. Next steps: update the implementation report, reconfirm WGLC, publish.
- **Where applicable**: Any BGP deployment signaling datapath capabilities of next hops (entropy labels, GLB tuples, iFIT, metrics). Mature WG item now moving to publication; the plumbing beneath the NNHN/GLB work above.

### BGP best path next-hop selection enhancements

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-vroonen-idr-bgp-bestpath-nh-selection/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessb-1-5-bgp-best-path-next-hop-selection-enhancements-00) · [Session recording](https://youtu.be/fFc0kGI5arw) · [Materials](https://datatracker.ietf.org/meeting/124/session/idr)

Olivier Vroonen, Stéphane Litkowski (Cisco)

- **Why**: BGP's resolvability and cost rules assume the NEXT_HOP is the actual forwarding endpoint. GRE/MPLS/SR-MPLS/SRv6 tunnels break that assumption, producing real blackholes and wrong picks — shown with concrete examples of a VRF route dropped because no transport tunnel exists to the best path's next hop, and a delay-optimized (colored) path chosen by lowest IGP metric.
- **What**: Standardizes behavior vendors already implement: introduces the concept of a "forwarding address" (e.g., the tunnel endpoint) with a "forwarding context" (tunnel type and characteristics, resolution constraints such as which table to look up in); requires resolvability checks against the forwarding address, not just NEXT_HOP; makes costs from different contexts comparable via a preference notion (like RIB preference); and requires BGP to re-evaluate best paths whenever underlying reachability or cost changes (tracking).
- **How**: Builds on the partial fixes already in RFC 9012 (tunnel encapsulation) and RFC 9252 (SRv6) but addresses both resolvability and path suboptimality generically, not just for one encapsulation.
- **Where applicable**: Any tunnel-based BGP deployment, including SRv6 DC underlays — broadly applicable. Early individual draft (`-00`); value is mostly standardization of existing vendor behavior for interoperability.

### A Border Gateway Protocol 4 (BGP-4)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-idr-bgp4-rfc4271bis/) · [Materials](https://datatracker.ietf.org/meeting/124/session/idr)

Yakov Rekhter (independent), Tony Li (HPE), Susan Hares (Huawei), John Scudder, Ed. (HPE) — IDR WG document

- **Why**: The once-in-a-generation rewrite of the BGP base specification — the document every BGP implementation will eventually be coded and tested against.
- **What**: `draft-ietf-idr-bgp4-rfc4271bis-03` obsoletes RFC 4271 along with RFC 6286, 6608, 8212, and 9687, and subsumes the core of RFC 7606 (treat-as-withdraw error handling) into the base. Consolidation, not new machinery: restructured per-message and per-attribute error handling, the send-hold timer, typed NLRI parsing rules, an explicit route-resolvability condition in the decision process, and a roadmap distinguishing the "core extensions" (RFC 4760 multiprotocol, RFC 8654 extended messages) from the wider extension ecosystem.
- **How**: Full re-edit of RFC 4271 with a version-by-version change appendix and GitHub issue tracking; IDR milestone targets submission to the IESG as an Internet Standard by May 2027.
- **Where applicable**: All BGP implementations globally. Mature WG document in active revision; read it as the consolidation of two decades of errata and error-handling practice into one standard.

### EVPN Multi-Active Multihoming

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-zzhang-bess-evpn-multi-active-multihoming/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-bess-evpn-multi-active-multihoming-00) · [Session recording](https://youtu.be/4D1ZG26KiFw) · [Materials](https://datatracker.ietf.org/meeting/124/session/bess)

Jeffrey Zhang, Changwang Lin, Jorge Rabadan (individual draft, BESS)

- **Why**: EVPN offers All-Active or Single-Active multihoming today; operators want a hybrid — a subset of PEs active and load-balanced, the rest standing by for fast failover, without full active-active fanout.
- **What**: Multi-Active mode for a multihomed Ethernet Segment: PEs with higher configured preference operate All-Active (ingress PEs load-balance to them); non-preferred PEs stay Single-Active/inactive and take over on failure of the preferred set.
- **How**: Preference is signaled in the DF Election Extended Community (in ES routes); preferred PEs signal P=1/B=0 in the L2-Attribute Extended Community (in Ethernet A-D per-EVI routes) so ingress PEs load-balance to them, while non-preferred PEs signal P=0 and are excluded from DF candidacy via the AC-Influenced DF Election Capability. All PEs (including non-preferred) keep signaling All-Active in the ESI label Extended Community for backward compatibility. Strict-mode (only equal-top-preference PEs active) and loose-mode (M preferred PEs, possibly different values) variants are defined. Only the MHES's own PEs need to understand the mode; other PEs act on the P/B bits as usual.
- **Where applicable**: EVPN multihoming deployments in DC access and DCI. Early individual draft (`-00`) seeking comments; authors believe there is no backward-compatibility issue and are asking the WG to scrutinize that claim.

### More Accurate Explicit Congestion Notification (AccECN) Feedback in TCP

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-tcpm-accurate-ecn/) · [Session recording](https://youtu.be/Z1qVCrIBVqQ) · [Materials](https://datatracker.ietf.org/meeting/124/session/tcpm)

Bob Briscoe (Independent), Mirja Kühlewind (Ericsson), Richard Scheffenegger (NetApp) — TCPM

- **Why**: RFC 3168 ECN feedback allows one congestion signal per RTT; DCTCP, L4S, and ConEx need per-marking counts. This changes the TCP wire protocol itself — and it is now finished: published as **RFC 9768** (Proposed Standard, April 2026).
- **What**: AccECN replaces Classic ECN feedback: the receiver continually feeds back a count of CE-marked packets using the three TCP header flags (the former NS bit renamed AE, plus overloaded CWR/ECE) as a 3-bit ACE counter, negotiated in the three-way handshake with careful backward compatibility. An optional AccECN TCP Option (two alternative field orders, never on the SYN) supplements this with 24-bit byte counters per ECN codepoint.
- **How**: Two-part design — the essential header counter works even where middleboxes strip options; the option adds byte-accuracy and ACK-loss resilience. The receiver acts as a "generic (mechanistic) reflector" so future sender behaviors deploy unilaterally. It also feeds back the IP-ECN value received on the SYN/SYN/ACK, letting endpoints detect middleboxes that mangle the ECN/ToS field instead of blindly disabling ECN. Normative compliance requirements cover TCP proxies, normalizers, ACK filters, and offload engines.
- **Where applicable**: All TCP — public Internet and private networks including data centers; explicitly the enabler for DCTCP-style and L4S congestion control. Broadly applicable; as an RFC this is now implementation/deployment news rather than work-in-progress.

### Enhanced Encapsulating Security Payload (EESP)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-eesp-ikev2/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-ipsecme-eesp-ikev2-00) · [Session recording](https://youtu.be/ZwfypFEEcYY) · [Materials](https://datatracker.ietf.org/meeting/124/session/ipsecme)

Steffen Klassert, Antony Antony (secunet), Christian Hopps (LabN Consulting) — IPSECME WG document

- **Why**: ESP has no version field and cannot evolve transparently; everything must be IKEv2-negotiated and is invisible to intermediaries. Meanwhile high-speed deployments need an inner-flow identifier for ECMP, CPU pinning, and QoS, and selective exposure of inner headers for middleboxes. This is the network-security wire-format change of the meeting.
- **What**: EESP is a modernized ESP on a new IP protocol number: a Base Header (version, options length, 16-bit Session ID, SPI) that middleboxes can parse; a Peer Header (full 64-bit sequence number, IV) private to the peers; the ESP trailer eliminated (Next Header/Pad Length moved into a Payload Info Header); IPv6-style TLV options for future extension; and a Crypt Offset option to expose leading bytes of the inner packet for middlebox/telemetry use — covering the PSP (VNI/crypt-offset) use case, anti-replay subspaces, and shared-SA proposals in one mechanism.
- **How**: The Session ID doubles as a Sub SA ID selecting independent 64-bit anti-replay sequence-number spaces (per core, path, or QoS class), each with keys derived via KDF, creatable "on the fly" in the data plane — including hardware offload deriving per-packet sub-SA keys. Combined-mode (AEAD) algorithms only; replay-disable is negotiated (useful in DCs where upper layers handle replay); an optimized packet format elides the Payload Info Header in IPv4/IPv6 tunnel mode. Negotiable via IKEv2 but portable to other keying protocols; Linux XFRM implementation status is tracked in the draft.
- **Where applicable**: High-throughput IPsec — datacenter interconnects and large VPN fabrics where per-flow ECMP/QoS under encryption matters. WG document at `-04`, active; watch for the protocol-number allocation and PSP alignment.

### OAuth SPIFFE Client Authentication

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-schwenkschuster-oauth-spiffe-client-auth/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-oauth-spiffe-client-authentication-00) · [Session recording](https://youtu.be/lT_E5vbqAyc) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Stian Thorgersen, Scott Rose, Pieter Kasselman, Arndt Schwenkschuster (individual draft, OAuth WG venue discussion)

- **Why**: Sits exactly at the intersection of workload identity and OAuth: workloads acting as OAuth clients today authenticate with manually provisioned, long-lived client secrets; this profiles OAuth client auth to consume SPIFFE SVIDs instead.
- **What**: Profiles RFC 7521/7523 so OAuth clients authenticate to authorization servers using JWT-SVIDs or X.509-SVIDs — no client secrets — with trust established via SPIFFE Bundle Endpoints (JWKS) for key distribution, and discussion of RFC 8705 (mTLS) handling for X509-SVIDs.
- **How**: The draft explains precisely why vanilla RFC 7523 doesn't fit: its requirement that the assertion subject equal the `client_id`, and SPIFFE's subject-as-authority key-discovery model (spiffe:// URIs vs. https:// metadata). Evidence of real momentum: Keycloak 26.4 shipped a preview implementation, multiple community authenticators exist, and SPIFFE is already in production at Uber, Netflix, ByteDance, Google, and others. Open questions for the WG: venue, SPIFFE-ID vs. client-ID semantics, and registration/trust-establishment requirements.
- **Where applicable**: Any environment where SPIFFE/SPIRE infrastructure and OAuth coexist — which is most enterprise service meshes. Early individual draft, but with shipping implementation evidence rather than slideware.

### WIMSE Architecture

**Links:** [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-architecture-00) · [Session recording](https://youtu.be/0UaVPLO_9Xk) · [Materials](https://datatracker.ietf.org/meeting/124/session/wimse)

WIMSE WG presentation on draft-ietf-wimse-arch-06 (no Internet-Draft linked to the slides)

- **Why**: WIMSE is the IETF's umbrella for workload identity — the standards track that SPIFFE-adjacent interests will land on. This presentation is the WG's open-issues snapshot.
- **What**: Status of the architecture document after an interim: pending refactors of the service-to-service and identifier documents, terminology alignment, and an explicit list of topics to expand — security considerations, authorization, binding, key management, and attestation. The WG also refined its workload definition (PR#96): an independently addressable, executable software entity — microservices, containers, VMs, serverless functions — spanning fraction-of-a-second request handlers to multi-year database services and ML training jobs.
- **How**: The architecture coordinates WIMSE's credential formats (WITs), protocols, and attestation work; the "topics to expand" list is effectively the WG's current risk register — authorization and binding are where the hard problems now sit.
- **Where applicable**: Cloud-native service meshes broadly, not org-specific. WG work in progress; the interesting signal here is direction (authorization/key management next), not new mechanism.

### WIMSE Applicability for AI Agents

**Links:** [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-wimse-wimse-applicability-for-ai-agents-02) · [Session recording](https://youtu.be/0UaVPLO_9Xk) · [Materials](https://datatracker.ietf.org/meeting/124/session/wimse)

Yuan Ni, Chunchi Peter Liu (Huawei) — draft-ni-wimse-ai-agent-identity

- **Why**: Agentic identity made explicit in a standards body: AI agents blur network boundaries, exhibit unpredictable access patterns, arrive over-privileged, and escape accountability — "no identity → no access control → no accountability."
- **What**: Applies the WIMSE architecture to AI agents: an identity server issues agent credentials via an identity proxy with attestation evidence, with requirements for bootstrapping-independent trustworthy identities, automated credential management, minimal-privilege access tokens, and explicit workflows.
- **How**: The core proposal is a dual-identity credential — the agent's identity bound to its owner's (a user or an organization admin) as the input to access control — instantiated through a credential-request / user-confirmation-and-signature flow. Open questions include counter-signing design choices, credential-format extensions, whether hardware roots of trust in user devices should anchor the process, and initial trust establishment between identity server and proxy. Positioned against CHEQ's per-task double-confirmation tokens: this is per-identity credentials instead.
- **Where applicable**: Any trust domain hosting agent workloads (API agents, MCP-style clients). Huawei-driven individual contribution asking to become a WIMSE WG item — early, but agentic identity is moving from blog posts to standards requirements here.

### Transaction Tokens

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-transaction-tokens-00) · [Session recording](https://youtu.be/lT_E5vbqAyc) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Atul Tulshibagwale, George Fletcher, Pieter Kasselman — OAuth WG document, post-WGLC

- **Why**: The OAuth-side complement to WIMSE: maintaining immutable user identity, workload identity, and authorization context across a call chain inside a trust domain, enabling down-scoping at the edge and finer-grained authorization per hop.
- **What**: Txn-Tokens — tokens internal to a trust boundary that carry subject, context, and authorization details through a multi-service call chain, shared across workloads processing the request.
- **How**: Processing post-WGLC feedback: the `purp` claim became `scope`, the Txn-Token HTTP header is registered with an empty type in the HTTP fields registry, and an internal flow diagram was added. Open issues: request-context validation and replacement-token semantics (replacement process, lifetime extension, whether `tctx` can be modified). Implementations exist: Keycloak and Tokenetes (CNCF sandbox).
- **Where applicable**: Microservice/API call chains within a single trusted domain. Mature WG document close to publication.

### OAuth 2.0 Delegated Authorization

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-li-oauth-delegated-authorization/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessb-refresh-token-and-authorization-expiration-00) · [Session recording](https://youtu.be/lT_E5vbqAyc) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Ruochen Li, Haiguang Wang, Chunchi Peter Liu, Tieyan Li (Huawei) — individual draft

- **Why**: Down-scoping in OAuth today requires token exchange (RFC 8693) round-trips through the authorization server; this draft proposes client-local delegation with key-bound token chains — relevant to service chains and to how agentic clients might delegate constrained authority without AS involvement at each step.
- **What**: Delegation Tokens (DTs) issued by the AS and bound to the client's key; the client locally issues Delegated Access Tokens (DATs) bound to a delegate's key. Only DATs are accepted at resource servers — DTs are never used as access tokens. The RS validates the ordered token chain, the restrictions imposed at each delegation step, and a DPoP proof signed by the key bound to the leaf token.
- **How**: A digitally signature-linked chain analogous to PKI certificates; the explicit contrast with RFC 8693: no external STS involved, subordinate tokens tightly linked to their superior, delegation can occur at any node along the invocation chain including third-party intermediaries. Supports Rich Authorization Request details, encrypted (JWE) DTs, and sign-then-encrypt DATs; future work covers multi-layer delegation and multiple DTs per request.
- **Where applicable**: Service-to-service and delegation chains. Early individual draft from Huawei, seeking feedback. Note: the slides the agenda links to this slot actually cover a different draft (Nick Watson/Google's refresh-token and authorization-expiration parameters, also seeking adoption); the Delegated Authorization deck was presented under the OAuth 2.1 slot — the write-up above uses that deck.

### The OAuth 2.1 Authorization Framework

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-delegated-authorization-00) · [Session recording](https://youtu.be/jSC4rGzkoh8) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Dick Hardt (Hellō), Aaron Parecki, Ed. (Okta), Torsten Lodderstedt (SPRIND) — OAuth WG document

- **Why**: The consolidated successor to RFC 6749/6750 — every OAuth product roadmaps against it, and the WG milestone targets IESG submission in December 2026.
- **What**: A single standards-track specification replacing OAuth 2.0 and Bearer Token Usage, folding in OAuth for Native Apps (RFC 8252), Browser-Based Apps (RFC 10017), and the Security BCP (RFC 9700), and removing features found insecure: the implicit grant is gone, PKCE is required for the authorization-code flow, the redirect URI must be sent in token requests, sender-constrained tokens (DPoP, mTLS) are recommended over bare bearers, and refresh-token/client-credential behavior is specified in the base.
- **How**: Consolidation and normative merge of the existing document set, with an explicit "Differences from OAuth 2.0" section enumerating the removals so implementers can plan migrations.
- **Where applicable**: Every OAuth implementation, full stop. WG document at `-17` — late-stage, expect the interesting discussion to be migration timing and 2.0-mode compatibility, not design.

### Updates to OAuth 2.0 JSON Web Token (JWT) Client Authentication and Assertion-Based Authorization Grants

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc7523bis/) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Michael B. Jones (Self-Issued Consulting), Brian Campbell (Ping Identity), Chuck Mortimore (Disney), Filip Skokan (Okta) — OAuth WG, in the RFC Editor queue

- **Why**: Fixes a real, published vulnerability — "audience injection" attacks (Hosseyni, Küsters, Würtele, University of Stuttgart), found during security analysis of OpenID Federation — affecting `private_key_jwt`-style client authentication across OAuth/OIDC.
- **What**: Updates RFC 7521, 7522, 7523, and 9126: for **client authentication**, the JWT `aud` claim MUST be the authorization server's issuer identifier as its sole value — the token endpoint URL is no longer an acceptable audience — and the AS MUST reject JWTs that don't comply. Authorization *grants* may still use either issuer identifier or token endpoint URL. SAML assertions for client authentication are deprecated; a new explicit type `client-authentication+jwt` SHOULD be used as a compliance signal.
- **How**: Root cause: metadata-derived endpoint URLs used as audience values could be accepted at a different endpoint, enabling cross-endpoint token injection. The fix is deliberately asymmetric in rollout — updated clients interoperate with old servers, but not vice versa — so clients should move first; the draft documents this explicitly in its operational considerations.
- **Where applicable**: Every AS and client doing JWT client authentication or assertion grants. Mature: IETF last-call reviews complete, IESG consensus recorded, sitting in the RFC Editor queue. Plan the migration now.

### JSON Web Proof

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-jose-json-web-proofs-00) · [Session recording](https://youtu.be/WoxqyTaaI6c) · [Materials](https://datatracker.ietf.org/meeting/124/session/jose)

Mike Jones, David Waite — JOSE WG document

- **Why**: The JOSE-side container for credentials using newer selective-disclosure and unlinkability algorithms (BBS-style) — the path beyond JWS/SD-JWT for zero-knowledge-ish verifiable credentials.
- **What**: JWP: a JWS-like container that integrity-protects **multiple payloads** in one message, with a presentation form supporting selective disclosure of individual payloads, additional proof computation, and a Presentation Header to prevent replay. JPT (JSON Proof Token) constrains payloads to claims, targeting SD-JWT's problem domains with newer algorithms.
- **How**: At IETF 124 the work added a "subclaim" syntax — based on CBOR Pointer (no negative array indexing, no indexing into serialized CBOR), chosen over JSON Path, SD-JWT VC metadata paths, and OID4VP's DCQL for remote-safety, simplicity, and CBOR-readiness — so a presentation can disclose just `["address","country"]` or an `is_over_18` predicate instead of a whole claim. Motivated by common feedback from two independent digital-credential prototypes. Other open items: aligning JWP's algorithm/header registries with JWK/CWK (which don't know about them — possibly by reusing the JWS/COSE algorithm registries), BLS key representation (compressed/ZCash style per IANA early review), and JSON/CBOR example parity that has already uncovered spec bugs.
- **Where applicable**: Verifiable credentials and digital wallets. WG document in active revision; the subclaim decision is the one to track.

### SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-oauth-sessa-sd-jwt-vc-00) · [Session recording](https://youtu.be/jSC4rGzkoh8) · [Materials](https://datatracker.ietf.org/meeting/124/session/oauth)

Oliver Terbu (MATTR), Daniel Fett (Authlete), Brian Campbell (Ping Identity) — OAuth WG document

- **Why**: The leading JSON format for selectively disclosable verifiable credentials (the format behind most government/wallet pilots); this session shows it converging to working-group last call.
- **What**: Data formats plus validation and processing rules for verifiable credentials with JSON payloads, with and without selective disclosure, built on SD-JWT and the JWT extensibility model; defines issuer signature mechanisms (web-based metadata via `.well-known`/JWKs, inline `x5c`) and Type Metadata (claim schemas, rendering/display metadata).
- **How**: The `-11`/`-12` churn is stabilization: `vct#integrity` added to the non-disclosable claim list, Status List tokens must be JWTs, `lang`→`locale`, JSON schema removed from Type Metadata, `x5c` required in the protected header, `sd=always`/`sd=never` recommended to avoid ambiguity, and the relationship to Key Binding (SD-JWT+KB) clarified. The slides close with "WGLC?"
- **Where applicable**: Digital credential ecosystems — government IDs, enterprise credentials, wallets. WG document on the cusp of last call; if your identity roadmap touches credentials at all, this is the format to build against.

## Adjacent

### BMP v4: Extended TLV Support for BGP Monitoring Protocol (BMP)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-grow-bmp-tlv/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-grow-bmp-v2-tlv-support-01) · [Session recording](https://youtu.be/qkDDPaLey0Q) · [Materials](https://datatracker.ietf.org/meeting/124/session/grow)

Paolo Lucente (NTT Data), Yunan Gu (Huawei) — GROW WG document

- **Why**: BMP is how BGP is observed; Route Monitoring, Stats Reports, and Peer Down messages lack TLV extensibility, which blocks richer per-message telemetry — and the FlowSpec-feedback work below explicitly wants to export over BMP.
- **What**: Updates RFC 7854 to support optional TLVs on all BMP message types, bumps the protocol version for backward compatibility, defines essential TLVs, and adds an Enterprise (E) bit allowing per-vendor type values.
- **How**: WG-document mid-flight: post-E-bit-merge wording fixes pending, Stats messages need a container TLV to hold other optional TLVs, and an open question on merging `draft-younsi-grow-bmp-snts`.
- **Where applicable**: BGP monitoring collectors and vendor telemetry stacks; broadly applicable operational plumbing rather than a research item.

### BGP Flow Specification Extension for Feedback Binding

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-cui-idr-flowspec-feedback-binding/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-idr-sessa-2-6-bgp-flow-specification-extension-for-feedback-binding-00) · [Session recording](https://youtu.be/36tw7gGeIdA) · [Materials](https://datatracker.ietf.org/meeting/124/session/idr)

Yong Cui (Tsinghua University), Yujia Gao, Lei Zhang (Zhongguancun Laboratory) — individual draft

- **Why**: FlowSpec is one-way control today: "rule delivered ≠ rule effective." DDoS scrubbing rules fail silently on local ACL conflicts, unresolved redirect next-hops, inactive rules, or vendor gaps — and the operator has no standard way to see which nodes actually enforced the mitigation. This touches the network-security interest directly, as closed-loop visibility for a security mechanism.
- **What**: A FlowSpec extension carrying a Feedback Action as a Generic Transitive Extended Community: a Feedback Identifier (FID), a window exponent (WINC) defining the periodic reporting interval as 2^n seconds, an event flag, and a scope selector (global / inter-AS / intra-AS) — propagated across AS boundaries unchanged.
- **How**: Routers report rule lifecycle state (Received → Install → Active → Effective, or Inactive/Removed/Error) and data-plane hit statistics keyed by the FID, exported via a companion mechanism (BMP or a telemetry framework). The DDoS use case: a controller pushes scrubbing redirects and detects in real time which nodes failed to activate them. Signaling only in this draft; export is future work.
- **Where applicable**: FlowSpec-based DDoS mitigation and traffic steering across enterprise–carrier boundaries. Early academic individual draft (`-00`) explicitly seeking requirements confirmation and interest; the concept (closed-loop control for FlowSpec) is more mature than the draft.

### Proposal for Updates to Guidance on Packet Reordering

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-white-intarea-reordering/) · [Session recording](https://youtu.be/5zx9U6mxbFQ) · [Materials](https://datatracker.ietf.org/meeting/124/session/tsvwg)

Greg White (CableLabs), Ingemar Johansson (Ericsson), Dibakar Das (Intel), Chris Box

- **Why**: Several link-technology standards mandate in-order L2 delivery and implement resequencing buffers that add delay — exactly the machinery that defeats packet-spraying multipath in modern fabrics. Modern TCP and QUIC tolerate reordering far better than the L2 standards bodies assume.
- **What**: Informational guidance for layer-2 standards organizations: IETF transport protocols do not require guaranteed in-order delivery, so the resequencing requirement can be relaxed where it causes net performance degradation (from abstract only).
- **How**: Cites the modern TCP/QUIC features that improve out-of-order tolerance as the basis for updating the guidance L2 standards cite.
- **Where applicable**: Link-technology standards (link aggregation, L2 transport) — general technique, not org-specific. Maturity signal worth noting: since the meeting, the individual draft was adopted by INTAREA and replaced by WG document `draft-ietf-intarea-reordering`, so consensus is forming.

### Selective Disclosure CBOR Web Tokens (SD-CWT)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-spice-sd-cwt-update-for-ietf124-00) · [Session recording](https://youtu.be/O-wPFMHLDrI) · [Materials](https://datatracker.ietf.org/meeting/124/session/spice)

M. Prorock, O. Steele, H. Birkholz, R. Mahy, M. Jones — SPICE WG document

- **Why**: The CBOR/COSE twin of SD-JWT: selective disclosure for constrained devices and CBOR-native credential ecosystems. Watching it mature tells you where the JSON and CBOR credential formats will converge or diverge.
- **What**: A data-minimization technique for CBOR Web Tokens, inspired by SD-JWT but realigned with COSE and CWT structure; at `-05` with no major normative changes in the last cycle.
- **How**: Recent tightening: AEAD guidance (no authentication tags under 16 bytes), corrected COSE key examples, explicit rules for verifier handling of unknown claims, sorted CBOR map keys for test vectors. Open issues are CBOR-specific hygiene: encoding restrictions (forbid indeterminate length, max nesting depth 16, bstr-encoded map keys), tagged map keys, decoy-digest examples — two issues gated on early IANA registration. About 2.5 implementations (Rust, JavaScript, Python) heading into interop testing.
- **Where applicable**: Constrained-device and COSE-based credential ecosystems; WG document in the interop phase — steady, unglamorous, on track.

## Wildcard

### SCONE TCP Option

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-eddy-tcpm-scone/) · [Slides](https://datatracker.ietf.org/meeting/124/materials/slides-124-tcpm-scone-for-tcp-00) · [Session recording](https://youtu.be/Z1qVCrIBVqQ) · [Materials](https://datatracker.ietf.org/meeting/124/session/tcpm)

Wesley Eddy, Matt Joras (Meta) — individual draft in TCPM

- **Why**: A different direction of network→endpoint signaling than FANTEL: instead of telling the ingress to reroute, middleboxes tell endpoints their rate limits. Interesting precisely because it parallels the AI-fabric notification philosophy (network signals, endpoints adapt) in an entirely different problem space — and shows the SCONE WG's charter spilling beyond QUIC.
- **What**: A TCP option that network elements can insert or modify to give endpoints throughput guidance — motivated by rate-limiting of ABR video in mobile networks, where knowing the limit lets the player pick a compliant rendition instead of oscillating through losses.
- **How**: Explicitly modeled on MSS clamping — an on-path element rewrites an option the downstream stack can act on; the same network elements being built for QUIC SCONE (a new QUIC packet type carrying rate-limit encodings middleboxes can read and set) would handle the TCP option. Many details open: application interfaces, interaction with other TCP options, send timing, insertion rules.
- **Where applicable**: Rate-limited access networks (mobile) with adaptive video; the rate-signaling mechanism itself is general. Very early individual draft (`-00`) gauging whether TCPM wants this at all — a "watch the question, not the draft" item.

### Kademlia-directed ID-based Routing Architecture (KIRA)

**Links:** [Draft](https://datatracker.ietf.org/doc/draft-bless-rtgwg-kira/) · [Session recording](https://youtu.be/cFekE0TpHng) · [Materials](https://datatracker.ietf.org/meeting/124/session/rtgwg)

Roland Bless (Karlsruhe Institute of Technology) — individual draft, intended Experimental

- **Why**: A genuinely different routing architecture rather than an increment: zero-touch, ID-based control-plane routing that scales to hundreds of thousands of nodes with no hierarchy and no manual configuration. Not deployable tomorrow, but the clearest signal in the program of where autonomic-networking research is heading — and a notable data point in the "control planes shouldn't depend on the data plane they're configuring" argument.
- **What**: A two-tier architecture. The Routing Tier runs R²/Kad — a *recursive* Kademlia over self-assigned, topologically independent 112-bit NodeIDs with the XOR metric: k-bucket routing tables that grow O(log n), source routing between overlay hops, Proximity Neighbor Selection preferring short paths, overhearing of transit messages, periodic path probing, and loop-free operation even during convergence. The Forwarding Tier uses PathIDs (hashes of path-segment NodeID sequences) as label-like forwarding state, encapsulated over SRv6, IPv6-in-IPv6, or GRE — reusing existing IPv6 forwarding hardware. Add-ons include a built-in DHT for name resolution and the KeLLy topology discovery service; a domain concept provides administrative grouping; an end-system mode supports non-routing participants.
- **How**: The explicit trade is path stretch for tiny routing tables and extreme resilience — the design goal is to never lose control-plane connectivity to a reachable device, accepting stretched paths as the price. Failure recovery is error-triggered rediscovery with NotViaList exclusion of failed links, not flooding.
- **Where applicable**: Control-plane and management networks, autonomic networking, disaster-resilient infrastructure — explicitly not a data-plane replacement. Long-running individual draft (`-06`) with academic grounding; read it as architecture research with a reference protocol spec, not a deployment candidate.

## Themes

- **AI fabrics are the routing area's primary design driver now.** FANTEL problem statements, GLB-in-Clos BGP extensions, credit-based WAN flow control, and ML-cluster network scheduling all treat the AI training/inference cluster as the motivating workload — with the RTGWG fast-notification cluster (problem statement, WAN RDMA notifications, and soon-to-be-WG drafts) as this cycle's center of mass.
- **The DC/WAN boundary is dissolving in the standards.** Lossless RDMA semantics, previously confined to the DC via PFC, are being re-specified for SRv6-tunneled WAN (notifications, credit flow control), and BGP itself is being extended (NNHN) purely for fabric-internal load balancing — the PM's physical-DC and WAN interests are converging into one problem space in the IETF.
- **BGP is being modernized on two fronts at once.** Backward consolidation (rfc4271bis folding error-handling and policy RFCs into one Internet Standard) and forward-looking per-next-hop signaling (the NHC family: NNHN, iFIT, generic metric) — plus the base spec's own resolvability rules being repaired for tunnel next hops.
- **OAuth/identity is in security-incident-driven and consolidation modes simultaneously.** rfc7523bis ships an audience-injection fix through the RFC queue, OAuth 2.1 consolidates the 2012-era framework plus its security BCP, while workload identity (WIMSE, Txn-Tokens, SPIFFE client auth) and agentic identity (WIMSE AI agents, delegated token chains) form the forward edge.
- **Selective disclosure is becoming table stakes across formats.** JWP (with the new subclaim syntax), SD-JWT VC (pre-WGLC), and SD-CWT (interop phase) are all converging on the same capability in JSON and CBOR — the credential-format wars are being fought over pointer syntax and registry details now, not the core idea.
- **New wire formats are designed for middleboxes, not endpoints.** EESP's parseable Base Header and Crypt Offset, AccECN's normative middlebox/offload compliance rules, SCONE's middlebox-settable signals, and FANTEL's transit-to-ingress notifications all assume intermediaries will read, set, or rewrite protocol fields — a durable architectural shift worth tracking across every protocol the PM owns.
