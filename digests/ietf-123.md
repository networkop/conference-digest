<!--
conference: ietf-123
location: Madrid
type: standards
generated: 2026-06-08
selection_basis: program text (draft titles + abstracts); no fetchable paper links present
enrichment: none — program provided no pdf/page links beyond GitHub discussion venues; all write-ups are from abstract/draft text only
-->

# IETF 123 (Madrid) — Digest

A standards meeting, so the unit of work is the Internet-Draft, not the session. This cycle's signal is concentrated in three places that map directly onto your interests: **workload identity** finally cohering into a full WG-adopted stack (WIMSE), the **post-quantum migration** moving from algorithm definition into deployment mechanics across TLS/PKIX/COSE/JOSE, and **datacenter fabric** work in NVO3, RIFT, and SAVNET. Selection is from the program; every write-up below is grounded in the draft abstract only (no paper links were available to enrich from), and is flagged as such.

A note on maturity, since it's the whole game in a standards venue: `draft-ietf-*` means a working group has adopted the work (it carries weight); `draft-<author>-*` is an individual submission (early, may go nowhere). Where both exist for the same title, the WG copy is the one to track.

---

## Core

### Workload Identity in a Multi System Environment (WIMSE) Architecture — `draft-ietf-wimse-arch`

- **Tier**: Core
- **Why**: This is the architectural anchor for standardizing how workloads get and use identity across multi-cloud, multi-tenant, multi-service deployments — the exact problem SPIFFE/SPIRE solved proprietarily. An IETF-stream architecture means the surrounding protocol drafts (below) have a shared frame, and implementations stop being per-vendor.
- **What**: An architecture document defining how to convey workload identity and security-context information, where a workload is software running for a specific purpose, possibly across many instances. (from abstract only)
- **How**: It scopes the problem and defines the component model that the credential, token, and authentication drafts plug into, rather than specifying wire formats itself.
- **Where applicable**: Broadly applicable to any container-orchestration or microservice estate; vendor-neutral by design. This is the document to read first before the rest of the WIMSE set.

### WIMSE Workload-to-Workload Authentication — `draft-ietf-wimse-s2s-protocol`

- **Tier**: Core
- **Why**: The atomic unit of the whole architecture: how two workloads verify each other for a single HTTP request/response. It directly addresses the "do I use mTLS or app-layer tokens?" question that every service-mesh and zero-trust deployment hits.
- **What**: Defines two compatible protocols — one at the application layer, one riding trusted TLS transport — that can be mixed within a single call chain. (from abstract only)
- **How**: Workload A → B can use mutual TLS while B → C authenticates at the application level; the two are interoperable across hops, so you don't have to pick one model estate-wide.
- **Where applicable**: General; aimed at service-to-service traffic in mixed environments where some hops terminate TLS at proxies/load balancers and some are end-to-end.

### WIMSE Workload Proof Token (WPT) + Workload Credentials + HTTP Signatures — `draft-ietf-wimse-wpt`, `draft-ietf-wimse-workload-creds`, `draft-ietf-wimse-http-signature`

- **Tier**: Core
- **Why**: This trio is the concrete proof-of-possession machinery under the architecture, and it's the part that touches implementations: a credential format, a way to prove you hold the key, and an HTTP-signature option for when TLS isn't end-to-end. If you're evaluating workload-identity tooling, these define the interop surface.
- **What**: `workload-creds` defines the credential a workload uses to represent its identity (usable in X.509 or token form), deliberately separated from the PoP mechanism. `wpt` defines the Workload Proof Token — a signed JWT binding authentication to a specific HTTP request, providing application-level proof of possession of the key behind a Workload Identity Token (WIT). `http-signature` defines an HTTP Signatures–based authentication option that gives end-to-end request (and optionally response) protection even through TLS proxies and load balancers. (from abstract only)
- **How**: Credentials and proof-of-possession are split into separate documents so the same credential can be proven in different ways; WPT binds to the request to resist replay; the HTTP-signature variant protects requests across intermediaries that would otherwise break end-to-end mTLS.
- **Where applicable**: General. The HTTP-signature path is HTTP-only but specifically useful where you have L7 proxies/LBs in the path — i.e. most real service meshes and API gateways.

### Workload Identifier — `draft-ietf-wimse-identifier`

- **Tier**: Core
- **Why**: A canonical URI for naming a workload within a trust domain, embeddable in X.509 certs and security tokens. This is the SPIFFE-ID-shaped piece, and getting it standardized is what makes cross-system authorization and federation consistent.
- **What**: Defines a Workload Identifier as a URI that uniquely identifies a workload inside a specific trust domain, intended for embedding in credentials to drive authn, authz, and policy. (from abstract only)
- **How**: Standardizes the identifier format so the same identity semantics hold across certificates, tokens, and policy engines from different vendors.
- **Where applicable**: General; foundational for any federation or policy enforcement that spans trust domains.

### OAuth Identity and Authorization Chaining Across Domains + Transaction Tokens — `draft-ietf-oauth-identity-chaining`, `draft-ietf-oauth-transaction-tokens`

- **Tier**: Core
- **Why**: These two are the agentic/multi-hop authorization story. As calls fan out across services and trust-domain boundaries, you need to carry *who originated this* and *what they're allowed to do* without re-minting broad bearer tokens at every hop. This is directly the workload-and-agentic-identity space you track.
- **What**: `identity-chaining` preserves identity and authorization across OAuth trust domains by chaining context through JWT authorization grants obtained via Token Exchange (RFC 8693) and JWT Bearer (RFC 7523). `transaction-tokens` (Txn-Tokens) carry user identity, workload identity, and authorization context through an entire internal call chain within a trust domain for a given external request. (from abstract only)
- **How**: Identity-chaining repeats the same Token-Exchange-based protocol each time a domain boundary is crossed, so the chain composes across multiple domains. Transaction Tokens scope context to a single inbound request and propagate it internally, so downstream services act with the originator's narrow context rather than a reusable broad token.
- **Where applicable**: General OAuth deployments with microservice call chains; especially relevant where requests cross organizational/trust boundaries (B2B, federated enterprise SSO).

### OAuth 2.0 Attestation-Based Client Authentication — `draft-ietf-oauth-attestation-based-client-auth`

- **Tier**: Core
- **Why**: Lets a client instance present a key-bound attestation to an AS/RS without revealing its target audience to the attester. That audience-blinding property matters for privacy-preserving workload and device auth, and it's a cleaner client-authentication primitive than shared secrets.
- **What**: An OAuth extension where a client includes a key-bound attestation, verified by a separate client attester, that can serve as client authentication. (from abstract only)
- **How**: The attestation binds to the client's key and is verifiable by the AS/RS, but the attester issuing it does not learn which audience the client is talking to.
- **Where applicable**: General; useful for mobile/device clients and workloads where you want hardware- or platform-backed client identity without a static client secret.

### NVO3: Geneve + EVPN applicability + Active OAM for Geneve — `draft-ietf-nvo3-geneve`, `draft-ietf-nvo3-evpn-applicability`, `draft-ietf-nvo3-geneve-oam`

- **Tier**: Core
- **Why**: This is the datacenter overlay stack you work on directly. The WG settled on **Geneve as the common encapsulation** (over VXLAN-GPE/GUE), EVPN is the unified control plane for NVE auto-discovery and MAC/IP dissemination, and the missing piece operationally — OAM for Geneve — is being framed here. The encap choice and its OAM story affect both software and hardware tunnel-endpoint implementations.
- **What**: `geneve` specifies the flexible, extensible overlay encapsulation designed to accommodate evolving software and hardware tunnel endpoints. `evpn-applicability` describes using EVPN as the NVO3 control plane (auto-discovery, MAC mobility, multihoming, DCI) without introducing new EVPN procedures or requiring PIM in the underlay. `geneve-oam` frames the OAM functions needed to monitor and troubleshoot Geneve overlays. (from abstract only)
- **How**: Geneve uses extensible option fields so new capabilities ship without a new wire format; EVPN reuses BGP for the overlay control plane while keeping the underlay IP fabric independent; the OAM draft sets requirements for active monitoring across the overlay path.
- **Where applicable**: Multi-tenant DC fabrics. Note the encapsulation-considerations work flags a real operational constraint: mixing encapsulations along a path makes things like path-MTU discovery and OAM harder — relevant if you run heterogeneous hardware/software endpoints.

### Secure EVPN — `draft-ietf-bess-secure-evpn`

- **Tier**: Core
- **Why**: EVPN underpins most modern DC and DCI fabrics; adding a security/encryption story to it closes a gap that today usually gets papered over with separate IPsec. Worth tracking if you care about encrypted fabric and DCI.
- **What**: A WG-adopted BESS draft addressing security for EVPN. (from abstract only — the program text for this entry was limited to its title/identifier)
- **How**: Not determinable from the program text beyond that it targets EVPN; treat specifics as unconfirmed.
- **Where applicable**: EVPN-based fabrics and DCI. Flagging explicitly that this write-up is title-level only — read the draft before relying on mechanism details.

### SAVNET: Intra- and Inter-domain Source Address Validation Architecture + BAR-SAV — `draft-ietf-savnet-intra-domain-architecture`, `draft-ietf-savnet-inter-domain-architecture`, `draft-ietf-sidrops-bar-sav`

- **Tier**: Core
- **Why**: Anti-spoofing that's actually automated. uRPF and hand-maintained ACLs both fail in asymmetric-routing reality; SAVNET generates SAV rules from routing plus dedicated SAV signaling, and BAR-SAV derives filters from BGP UPDATEs + ASPA + ROA. This is the security-meets-routing intersection, and it directly affects edge/fabric filtering correctness.
- **What**: The intra-domain architecture produces accurate SAV at network edges automatically, using both local routing info and SAV-specific info exchanged between routers — more accurate than uRPF under asymmetric routing and less manual than ACLs. The inter-domain architecture does AS-level SAV by sharing SAV-specific info between ASes, falling back to general routing info during partial deployment. BAR-SAV (updates RFC 8704) derives robust SAV filters from BGP UPDATEs, ASPA, and ROA while preserving directionality and minimizing false positives. (from abstract only)
- **How**: SAVNET routers exchange purpose-built SAV information rather than inferring validity solely from the FIB, which is what kills uRPF accuracy in asymmetric paths; BAR-SAV combines three existing RPKI/BGP data sources to reduce both over-blocking and under-blocking.
- **Where applicable**: Intra-domain version applies to any operator edge; inter-domain version assumes incremental cross-AS adoption (designed to degrade gracefully when peers haven't deployed it). Broadly applicable, not vendor-specific.

### TLS PQC migration: ECDHE-MLKEM hybrid + ML-DSA auth + Trust Anchor IDs — `draft-ietf-tls-ecdhe-mlkem`, `draft-ietf-tls-mldsa`, `draft-ietf-tls-trust-anchor-ids`

- **Tier**: Core
- **Why**: This is the post-quantum transition arriving in the protocol you actually deploy. Hybrid key agreement is shipping in browsers/servers now; ML-DSA authentication and the certificate-size problems it creates are the next wave. Trust Anchor IDs is the quiet but important piece for surviving large/multiple CA sets during the migration.
- **What**: `ecdhe-mlkem` defines three hybrid groups (X25519MLKEM768, SecP256r1MLKEM768, SecP384r1MLKEM1024) combining ML-KEM with classical ECDHE. `mldsa` specifies using ML-DSA (FIPS 204) for TLS 1.3 authentication. `trust-anchor-ids` lets relying parties convey trusted CAs compactly and lets servers advertise available certification paths (including via DNS) so clients select one — addressing the bloat of carrying many trust anchors. (from abstract only)
- **How**: Hybrids run PQ and classical key exchange together so you're safe if either holds; ML-DSA replaces classical signatures for handshake auth; Trust Anchor IDs trims what has to be sent and supports path negotiation, which matters once PQ certs make chains larger.
- **Where applicable**: General TLS 1.3 deployments. Hybrid KEX is the low-risk piece to adopt first; ML-DSA auth and cert-size mitigations (see also `draft-ietf-tls-cert-abridge`, below in Adjacent) are where the operational pain concentrates.

### MASQUE: Proxying IP and Ethernet in HTTP — `draft-ietf-masque-connect-ip`, `draft-ietf-masque-connect-ethernet`

- **Tier**: Core
- **Why**: CONNECT-IP (and now CONNECT-Ethernet) turns HTTP/3 into a general-purpose tunneling substrate — VPN-like IP transport and even L2 transport over QUIC. This is increasingly relevant to cloud-native datapath and edge connectivity, and it overlaps your software-networking and WAN-interconnect interests.
- **What**: `connect-ip` defines proxying IP packets in HTTP; `connect-ethernet` extends the same model to Ethernet frames. (from abstract only)
- **How**: Both build on the HTTP Datagrams / Capsule Protocol so packets ride QUIC datagrams through an HTTP proxy, with IP- or Ethernet-level framing as the payload.
- **Where applicable**: General; useful for VPN replacement, network-to-network tunneling, and reaching workloads behind HTTP proxies. CONNECT-Ethernet is the more experimental of the two.

---

## Adjacent

### Abridged Compression for WebPKI Certificates — `draft-ietf-tls-cert-abridge`

- **Tier**: Adjacent
- **Why**: A pragmatic answer to PQ certificate bloat: a shared dictionary of root/intermediate WebPKI certs that removes them from the chain on the wire without changing trust negotiation. Smooths the PQ transition and also helps CT log storage.
- **What**: A TLS certificate-compression scheme using a shared dictionary of known CA certificates, claiming better compression than alternatives while treating CAs and operators fairly. (from abstract only)
- **How**: Roots and intermediates are referenced from a shared dictionary instead of transmitted, shrinking the chain; trust decisions are unaffected.
- **Where applicable**: General TLS, and any system storing cert chains (e.g. CT logs). Pairs naturally with the TLS PQC drafts in Core.

### COSE/JOSE Post-Quantum Signatures: ML-DSA, SLH-DSA, FN-DSA + PQ KEMs — `draft-ietf-cose-dilithium`, `draft-ietf-cose-sphincs-plus`, `draft-ietf-cose-falcon`, `draft-ietf-jose-pqc-kem`

- **Tier**: Adjacent
- **Why**: The token/credential layer's PQ story. Once your TLS is hybrid, the JWTs/CWTs and signed credentials underneath still use classical signatures; these drafts bring ML-DSA/SLH-DSA/FN-DSA and PQ KEMs to JOSE/COSE, which is what SD-JWT, CWT, and verifiable-credential formats sit on.
- **What**: Encodings for the three NIST PQ signature schemes (ML-DSA, SLH-DSA/SPHINCS+, FN-DSA/Falcon) in JOSE and COSE, plus PQ KEM registrations. (from abstract only)
- **How**: Defines the algorithm identifiers and encodings so existing JOSE/COSE-based formats can adopt PQ signatures without redesign.
- **Where applicable**: General; relevant anywhere you sign tokens or credentials (identity tokens, attestations, supply-chain receipts).

### LAMPS PQ PKI: ML-KEM and Composite KEM certificates — `draft-ietf-lamps-kyber-certificates`, `draft-ietf-lamps-pq-composite-kem`

- **Tier**: Adjacent
- **Why**: The X.509/PKI plumbing for PQ. Composite KEM (classical + PQ in one cert) is the hedging strategy most enterprises will actually deploy first, mirroring the hybrid approach in TLS.
- **What**: Algorithm identifiers for ML-KEM in X.509 PKI, and a composite ML-KEM construction combining PQ and traditional KEMs in a single certificate. (from abstract only)
- **How**: Composite binds two algorithms so a certificate remains secure if either survives, easing migration where you can't yet trust PQ alone.
- **Where applicable**: General PKI; especially conservative environments that want PQ without abandoning classical assurance.

### RATS: Remote Posture Assessment + EAT for Systems, Containers, and Applications — `draft-ietf-rats-posture-assessment`, `draft-ietf-rats-eat`

- **Tier**: Adjacent
- **Why**: Attestation is the trust root under workload identity — "is this workload running what it claims, on hardware I trust?" The posture-assessment draft explicitly extends to containers and applications at scale, which connects attestation to the WIMSE/agentic-identity world you track.
- **What**: `eat` defines the Entity Attestation Token; `posture-assessment` defines remote posture assessment for systems, containers, and applications at scale. (from abstract only)
- **How**: EAT carries signed claims about an entity's state; posture assessment frames how verifiers consume that evidence across many targets.
- **Where applicable**: General; the container/application angle is the relevant one for cloud-native estates.

### SPICE: Selective Disclosure CWT (SD-CWT) + Verifiable Digital Credentials architecture — `draft-ietf-spice-sd-cwt`, `draft-ietf-spice-vdcarch`

- **Tier**: Adjacent
- **Why**: The CBOR-native counterpart to SD-JWT, plus a reference architecture for direct credential presentation. This is the digital-credential/wallet direction of identity, adjacent to your authn interests and worth watching as it converges with OAuth's SD-JWT VC work.
- **What**: `sd-cwt` brings SD-JWT-style selective disclosure to CBOR Web Tokens, aligned with COSE; `vdcarch` defines a reference architecture introducing a "presentation mediator" for managing and selectively disclosing credentials. (from abstract only)
- **How**: SD-CWT adapts the selective-disclosure technique to CBOR/COSE encodings; the architecture centers a mediator component that handles presentation and disclosure with defined privacy properties.
- **Where applicable**: General; constrained/IoT and mdoc-adjacent ecosystems favor the CBOR path.

### ANIMA: BRSKI with Pledge in Responder Mode + Constrained BRSKI — `draft-ietf-anima-brski-prm`, `draft-ietf-anima-constrained-voucher`

- **Tier**: Adjacent
- **Why**: Zero-touch secure onboarding of devices is the bootstrap problem that precedes any workload/device identity. BRSKI's variants (responder mode, constrained/IoT) matter for how fleets of network gear and edge devices get their first trust anchor.
- **What**: `brski-prm` defines a BRSKI flow where the pledge acts in responder mode; `constrained-voucher` (cBRSKI) adapts the voucher/bootstrap flow to constrained devices. (from abstract only)
- **How**: Both adapt the BRSKI voucher exchange to deployment realities where the standard pledge-initiated, unconstrained flow doesn't fit.
- **Where applicable**: Network-equipment and IoT onboarding; constrained variant assumes limited devices.

---

## Wildcard

### RIFT: Routing in Fat Trees + RIFT Auto-EVPN — `draft-ietf-rift-rift`, `draft-ietf-rift-auto-evpn`

- **Tier**: Wildcard
- **Why**: You wouldn't go searching for a brand-new IGP, but RIFT is genuinely novel: a routing protocol *purpose-built for Clos/fat-tree DC fabrics* rather than retrofitted (like BGP-in-the-DC). It's link-state northbound and distance-vector southbound, which is an elegant fit for the topology. Auto-EVPN layering on top is a tell that it's aiming at real DC deployment, not just academic interest.
- **What**: A fat-tree-specific routing protocol; the auto-EVPN draft automates EVPN service provisioning over a RIFT underlay. (from abstract only)
- **How**: Exploits the regularity of fat-tree topologies to minimize flooding and state — flooding link-state info toward the spine, summarizing toward the leaves. (Mechanism stated from general draft framing; treat specifics as unconfirmed pending the draft.)
- **Where applicable**: Clos/fat-tree datacenter fabrics specifically — by construction it's not a general-purpose IGP. Worth a look as a contrast to the "BGP everywhere in the DC" orthodoxy (cf. `draft-ietf-rtgwg-bgp-routing-large-dc`).

### IPsec IP Traffic Flow Security (IP-TFS / AGGFRAG) — `draft-ietf-ipsecme-iptfs`

- **Tier**: Wildcard
- **Why**: Traffic-flow confidentiality is usually ignored, but IP-TFS tackles a real and under-appreciated leak: packet sizes and timing reveal information even when payloads are encrypted. The aggregation-and-fragmentation approach to hide flow characteristics is a neat technique with WAN and high-assurance relevance.
- **What**: An aggregation/fragmentation mode for ESP that provides traffic-flow security by obscuring the size and timing pattern of the original packets. (from abstract only)
- **How**: Packets are aggregated and/or fragmented into fixed-shape ESP traffic so observed flow characteristics no longer map to the underlying packets.
- **Where applicable**: IPsec tunnels where metadata leakage matters — government/high-assurance and some WAN scenarios. Has bandwidth/overhead tradeoffs inherent to padding-style schemes.

### SCITT: Architecture for Trustworthy and Transparent Digital Supply Chains — `draft-ietf-scitt-architecture`

- **Tier**: Wildcard
- **Why**: Software supply-chain integrity as an IETF-standardized transparency layer (think CT logs, generalized to any supply-chain statement). It's a signal of where "verifiable provenance" is heading, and it leans on the same COSE/receipts primitives as the identity work — a cross-pollination worth seeing even if it's not your day job.
- **What**: An architecture for registering signed supply-chain statements in append-only transparency services that issue verifiable receipts. (from abstract only)
- **How**: Statements are signed (COSE) and recorded so a verifier can later confirm inclusion via a receipt, giving tamper-evident provenance.
- **Where applicable**: General software supply-chain and artifact provenance; relevant to anyone consuming signed build/attestation metadata.

### JOSE JSON Web Proof (JWP) — `draft-ietf-jose-json-web-proof`

- **Tier**: Wildcard
- **Why**: A new container format alongside JWS/JWE built specifically for multi-message, zero-knowledge-style proofs (e.g. BBS) — i.e. selective disclosure and unlinkable presentations as a first-class primitive rather than a bolt-on. If privacy-preserving credentials go mainstream, this is plumbing you'll encounter.
- **What**: JSON Web Proof, plus its algorithms and token format, defining a JWS/JWE-sibling structure for proofs over multiple messages. (from abstract only)
- **How**: Unlike JWS (sign one payload), JWP is designed around several individually-disclosable messages and proof algorithms that support selective disclosure / ZK properties.
- **Where applicable**: General, forward-looking; verifiable-credential and privacy-preserving-identity ecosystems. Early relative to SD-JWT, but architecturally more ambitious.

---

## Themes

- **Post-quantum has moved from "which algorithm" to "how do we ship it."** The action is in hybrids (ECDHE-MLKEM, composite KEM), the second-order problems PQ creates (certificate bloat → cert-abridge, Trust Anchor IDs), and propagating PQ down into the token/PKI layers (COSE/JOSE signatures, LAMPS certs). Algorithm selection is largely settled; deployment mechanics are the work.
- **Workload identity is consolidating into a real standard.** WIMSE went from individual drafts to a WG-adopted architecture plus a full credential/proof-of-possession/authentication stack this cycle — the open-standards counterpart to what SPIFFE/SPIRE did proprietarily.
- **Authorization is going multi-hop and context-preserving.** Identity chaining, Transaction Tokens, and attestation-based client auth all converge on carrying *who and what's allowed* across service and trust-domain boundaries without minting broad reusable bearer tokens — the substrate the "agentic identity" conversation needs.
- **Datacenter fabric standards are maturing in parallel tracks.** Geneve settled as the NVO3 encapsulation with EVPN as control plane and OAM now being specified; RIFT offers a topology-native alternative to BGP-in-the-DC; SAVNET automates anti-spoofing that uRPF/ACLs handle badly.
- **HTTP/3 is becoming a general transport substrate.** MASQUE's CONNECT-IP and CONNECT-Ethernet push IP and even L2 tunneling over QUIC, blurring the line between application proxying and network connectivity.
- **Selective disclosure and transparency are recurring primitives.** SD-CWT, JSON Web Proof, SCITT receipts, and RATS attestation all build on signed-claims-plus-verifiable-proof patterns (largely COSE-based), showing privacy-preserving credentials and verifiable provenance converging on shared machinery.
