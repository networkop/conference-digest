<!--
conference: IETF 122 (Bangkok)
type: standards
source_url: https://datatracker.ietf.org/meeting/122/agenda.json
generated: 2026-08-30
registry_key: ietf-122
-->

# IETF 122 (Bangkok) — Digest

Program source is the datatracker documents API, filtered to a curated set of 26 working groups touching cloud-native networking, network security, and identity. As with any standards meeting, the unit of work is the Internet-Draft, not the session — sessions are thin, drafts carry the substance. All write-ups below are grounded in draft abstracts only; no PDF/page links were available in the program text to enrich from, so treat "What/How" as abstract-level, not full-text analysis. `draft-ietf-*` means a working group has adopted the work (it carries real weight); a bare `draft-<author>-*` is an individual submission that may or may not go anywhere — noted per item where it matters. Datatracker links are added per draft (`https://datatracker.ietf.org/doc/<name>/`) since the program text itself carried no reference links.

The headline this cycle: **workload identity (WIMSE) has gone from architecture sketch to a nearly-complete, implementable protocol stack**, and it's flanked by matching moves in OAuth (cross-domain identity propagation), attestation (RATS), and supply-chain transparency (SCITT) — all converging on the same underlying problem of proving *what* is talking to *what*, and on whose behalf.

---

## Core

### WIMSE Architecture — `draft-ietf-wimse-arch`

- **Tier**: Core
- **Links**: [datatracker](https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/)
- **Why**: This is the frame every other WIMSE and adjacent OAuth draft below plugs into. An IETF-stream architecture for workload identity means the credential, proof-of-possession, and authentication drafts share one component model instead of each vendor inventing its own — exactly the standardization gap SPIFFE/SPIRE has been filling ad hoc.
- **What**: Defines an architecture for standardizing protocols and payloads that convey workload identity and security-context information, where a workload is software executing for a specific purpose, potentially spanning many running instances. (from abstract only)
- **How**: Scopes the problem space and the component model (identity, credentials, proof of possession, transport bindings) that the other WIMSE drafts fill in, rather than specifying wire formats itself.
- **Where applicable**: General — vendor-neutral by design, applicable to any container-orchestration or multi-service estate. Read this first before the drafts below.

### WIMSE Workload-to-Workload Authentication — `draft-ietf-wimse-s2s-protocol`, `draft-ietf-wimse-mutual-tls`, `draft-ietf-wimse-http-signature`

- **Tier**: Core
- **Links**: [s2s-protocol](https://datatracker.ietf.org/doc/draft-ietf-wimse-s2s-protocol/), [mutual-tls](https://datatracker.ietf.org/doc/draft-ietf-wimse-mutual-tls/), [http-signature](https://datatracker.ietf.org/doc/draft-ietf-wimse-http-signature/)
- **Why**: This is the atomic unit of the architecture — how two workloads actually verify each other for one HTTP request — and it directly answers the "mTLS or app-layer tokens?" question every service-mesh deployment eventually hits, by making both interoperable in the same call chain.
- **What**: `s2s-protocol` defines two compatible authentication protocols, one at the application layer and one over trusted TLS transport, that can be mixed hop-by-hop in a single call chain. `mutual-tls` profiles workload authentication using X.509 workload identity certificates over mTLS specifically. `http-signature` provides an HTTP Signatures–based alternative for end-to-end request (and optionally response) protection even when TLS is terminated at intermediate proxies or load balancers. (from abstract only)
- **How**: Workload A→B can authenticate via mTLS while the next hop B→C authenticates at the application level, with both anchored to the same Workload Identity Token — so a mesh doesn't have to pick one model estate-wide.
- **Where applicable**: General service-to-service traffic; the HTTP-signature variant is specifically useful where L7 proxies/load balancers break end-to-end TLS, i.e. most real-world meshes and API gateways.

### WIMSE Workload Credentials, Proof Token, and Identifier — `draft-ietf-wimse-workload-creds`, `draft-ietf-wimse-wpt`, `draft-ietf-wimse-identifier`

- **Tier**: Core
- **Links**: [workload-creds](https://datatracker.ietf.org/doc/draft-ietf-wimse-workload-creds/), [wpt](https://datatracker.ietf.org/doc/draft-ietf-wimse-wpt/), [identifier](https://datatracker.ietf.org/doc/draft-ietf-wimse-identifier/)
- **Why**: The concrete interop surface for anyone evaluating workload-identity tooling: a credential format, a proof-of-possession mechanism, and a canonical naming scheme — the SPIFFE-ID-shaped piece of the puzzle, now with a standards track under it.
- **What**: `workload-creds` defines the credential a workload uses to represent its identity (X.509 or token form), deliberately decoupled from proof-of-possession. `wpt` defines the Workload Proof Token, a signed JWT binding authentication to a specific HTTP request to prove possession of the key behind a Workload Identity Token. `identifier` defines the Workload Identifier as a URI unique within a trust domain, embeddable in certs and tokens. (from abstract only)
- **How**: Splitting credential from proof-of-possession lets the same credential be proven different ways depending on transport; the WPT binds to the request to resist replay.
- **Where applicable**: General; foundational for any cross-trust-domain federation or policy enforcement layered on top.

### OAuth Cross-Domain Identity Chaining & Transaction Tokens — `draft-ietf-oauth-identity-chaining`, `draft-ietf-oauth-transaction-tokens`

- **Tier**: Core
- **Links**: [identity-chaining](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/), [transaction-tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/)
- **Why**: This is the multi-hop authorization story for agentic and microservice call chains — how you carry *who originated this* and *what they're allowed to do* across service and trust-domain boundaries without re-minting broad bearer tokens at every hop.
- **What**: `identity-chaining` preserves identity and authorization context across OAuth trust domains by chaining JWT authorization grants obtained via Token Exchange (RFC 8693) each time a domain boundary is crossed. `transaction-tokens` (Txn-Tokens) propagate user identity, workload identity, and authorization context through an entire internal call chain within one trust domain for a given external request. (from abstract only)
- **How**: Identity-chaining repeats the same Token-Exchange protocol at each domain hop so the chain composes across multiple domains; Transaction Tokens scope context tightly to a single inbound request and propagate it internally so downstream services act with the originator's narrow context.
- **Where applicable**: Microservice architectures with OAuth in place; identity-chaining specifically targets requests crossing organizational or trust-domain boundaries (B2B, federated enterprise SSO).

### OAuth Attestation-Based Client Auth & Cross-App Access — `draft-ietf-oauth-attestation-based-client-auth`, `draft-ietf-oauth-identity-assertion-authz-grant`

- **Tier**: Core
- **Links**: [attestation-based-client-auth](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/), [identity-assertion-authz-grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/)
- **Why**: Two different answers to "how does an app prove who it is without a static secret" — one via hardware/platform attestation, one via an existing SSO trust relationship (informally "Cross-App Access", XAA) — both cleaner than shared-secret client auth.
- **What**: `attestation-based-client-auth` lets a client instance present a key-bound attestation, verified by a separate client attester, without revealing its target audience to that attester. `identity-assertion-authz-grant` lets an application obtain a third-party API access token by coordinating through an identity provider the downstream resource server already trusts for SSO, using Token Exchange and JWT Bearer grants. (from abstract only)
- **How**: The attestation draft's audience-blinding property means the attester can vouch for the client without learning who it's talking to; XAA reuses an existing SSO trust edge instead of requiring a new one per app pair.
- **Where applicable**: General; attestation-based auth suits mobile/device clients and workloads wanting hardware-backed identity without static secrets, XAA suits enterprise SaaS-to-SaaS integration.

### Selective-Disclosure Credentials: SD-JWT VC, Token Status List, SD-CWT — `draft-ietf-oauth-sd-jwt-vc`, `draft-ietf-oauth-status-list`, `draft-ietf-spice-sd-cwt`

- **Tier**: Core
- **Links**: [sd-jwt-vc](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/), [status-list](https://datatracker.ietf.org/doc/draft-ietf-oauth-status-list/), [sd-cwt](https://datatracker.ietf.org/doc/draft-ietf-spice-sd-cwt/)
- **Why**: The verifiable-credential stack that digital-identity-wallet and mDL implementations are actually converging on — worth tracking as the format war (JSON vs CBOR, JWT vs mdoc) settles into "two aligned formats" rather than N incompatible ones.
- **What**: `sd-jwt-vc` specifies data formats and validation rules for verifiable digital credentials as JSON payloads with selective disclosure via SD-JWT. `status-list` (TSL) defines a status mechanism and data structures for representing revocation/suspension status of tokens secured by JOSE or COSE — JWT, SD-JWT, CBOR Web Token, ISO mdoc. `sd-cwt` ports the same selective-disclosure technique to CBOR Web Tokens, aligned with COSE. (from abstract only)
- **How**: SD-JWT/SD-CWT let a holder disclose a subset of signed claims without invalidating the issuer's signature; TSL gives verifiers a compact, cacheable way to check whether a disclosed credential has since been revoked.
- **Where applicable**: General; this trio is the emerging interop baseline for digital wallets, mobile driving licenses, and any deployment needing minimal-disclosure credentials rather than all-or-nothing JWTs.

### RATS Attestation Stack: CoRIM, EAT, Attestation Results, CMW — `draft-ietf-rats-corim`, `draft-ietf-rats-eat`, `draft-ietf-rats-ear`, `draft-ietf-rats-msg-wrap`

- **Tier**: Core
- **Links**: [corim](https://datatracker.ietf.org/doc/draft-ietf-rats-corim/), [eat](https://datatracker.ietf.org/doc/draft-ietf-rats-eat/), [ear](https://datatracker.ietf.org/doc/draft-ietf-rats-ear/), [msg-wrap](https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/)
- **Why**: Remote attestation is becoming the common substrate under both workload identity (device/hardware-backed proof feeding WIMSE and OAuth attestation-based auth above) and supply-chain trust (SCITT below) — this is the plumbing layer worth understanding once rather than per-consumer.
- **What**: `corim` (Concise Reference Integrity Manifest) represents Endorsements and Reference Values a Verifier needs to appraise Evidence, in CBOR. `eat` (Entity Attestation Token) is an attested claims set describing an entity's state, as a CWT or JWT. `ear` (EAT Attestation Result) is the Verifier's output format, embedding a normalized "trustworthiness vector" for policy consumption. `msg-wrap` (CMW) is a common envelope for RATS' Evidence/Results/Endorsements messages, usable in CBOR protocols, JWTs/CWTs, and X.509 extensions alike. (from abstract only)
- **How**: An Attester produces Evidence (EAT); a Verifier appraises it against CoRIM-encoded Endorsements/Reference Values and emits an EAR; CMW gives all of these a consistent wrapper so protocols don't each reinvent the envelope.
- **Where applicable**: General — TPM/TCG DICE-based device attestation, but architecture-neutral; increasingly the trust root that ACME device-attestation and cert-issuance workflows build on (see Adjacent, below).

### SCITT Architecture & Reference APIs — `draft-ietf-scitt-architecture`, `draft-ietf-scitt-scrapi`

- **Tier**: Core
- **Links**: [architecture](https://datatracker.ietf.org/doc/draft-ietf-scitt-architecture/), [scrapi](https://datatracker.ietf.org/doc/draft-ietf-scitt-scrapi/)
- **Why**: Software supply-chain provenance keeps being solved point-by-point (certificate transparency, container image signing); SCITT is the attempt at a single, general transparency architecture instead of another bespoke ledger — directly relevant if you're evaluating supply-chain security tooling.
- **What**: `architecture` defines a general architecture for single-issuer signed-statement transparency across arbitrary supply chains, aiming for interoperability between transparency services and compliance with varied auditing regimes. `scrapi` specifies the concrete REST API — resources, request/response messages, error handling — for an interoperable SCITT Transparency Service implementation. (from abstract only)
- **How**: Issuers register signed statements to a transparency service, which returns a receipt (see COSE Receipts in Wildcard) proving inclusion in an append-only, auditable log.
- **Where applicable**: General; applicable to software artifacts, but the architecture is explicitly meant to generalize beyond software (see Traceability Claims in Adjacent).

### NVO3 Datacenter Fabric: Geneve OAM, Encapsulation Considerations, EVPN Applicability — `draft-ietf-nvo3-geneve-oam`, `draft-ietf-nvo3-encap`, `draft-ietf-nvo3-evpn-applicability`

- **Tier**: Core
- **Links**: [geneve-oam](https://datatracker.ietf.org/doc/draft-ietf-nvo3-geneve-oam/), [encap](https://datatracker.ietf.org/doc/draft-ietf-nvo3-encap/), [evpn-applicability](https://datatracker.ietf.org/doc/draft-ietf-nvo3-evpn-applicability/)
- **Why**: This is the datacenter overlay stack you work on directly — the WG has settled on Geneve as the common encapsulation, and this cycle's work fills in the two things that actually bite in production: OAM for troubleshooting overlays, and formalizing why the choice was Geneve over VXLAN-GPE/GUE in the first place.
- **What**: `geneve-oam` specifies requirements and a framework for Operations, Administration, and Maintenance in Geneve overlay networks. `encap` records the WG's encapsulation-considerations analysis and states the conclusion: Geneve, with modifications, as the common NVO3 encapsulation. `evpn-applicability` describes using EVPN as the NVO3 control plane for NVE auto-discovery and MAC/IP dissemination without requiring PIM in the underlay. (from abstract only)
- **How**: EVPN reuses BGP for the overlay control plane while keeping the underlay IP fabric independent of it; Geneve's extensible option-TLV design lets new capabilities (including OAM) ship without a new wire format.
- **Where applicable**: Multi-tenant DC fabrics. `encap` flags a genuine operational constraint worth internalizing: mixing encapsulations along a path complicates path-MTU discovery and OAM — relevant if you run heterogeneous hardware/software tunnel endpoints.

### Secure EVPN — `draft-ietf-bess-secure-evpn`

- **Tier**: Core
- **Links**: [datatracker](https://datatracker.ietf.org/doc/draft-ietf-bess-secure-evpn/)
- **Why**: EVPN underpins most modern DC and DCI fabrics; today, encrypting it usually means bolting on separate IPsec. A native security story for EVPN closes a real gap for anyone running encrypted fabric or DCI.
- **What**: A WG-adopted BESS draft presenting a solution where BGP point-to-multipoint signaling is leveraged for key and policy exchange among PE devices, creating private pairwise IPsec Security Associations without IKEv2 point-to-point signaling or direct peer-to-peer session establishment. (from abstract only)
- **How**: Reuses EVPN's existing BGP control plane to distribute IPsec keying material, avoiding a separate IKEv2 signaling mesh between every PE pair.
- **Where applicable**: DC, Service Provider, and Enterprise fabric overlays and DCI needing tenant-traffic confidentiality/integrity comparable to IPsec, without per-peer IKEv2 sessions.

### SAVNET Source Address Validation — `draft-ietf-savnet-general-sav-capabilities`, `draft-ietf-savnet-intra-domain-architecture`, `draft-ietf-savnet-inter-domain-architecture`

- **Tier**: Core
- **Links**: [general-sav-capabilities](https://datatracker.ietf.org/doc/draft-ietf-savnet-general-sav-capabilities/), [intra-domain-architecture](https://datatracker.ietf.org/doc/draft-ietf-savnet-intra-domain-architecture/), [inter-domain-architecture](https://datatracker.ietf.org/doc/draft-ietf-savnet-inter-domain-architecture/)
- **Why**: Source-address spoofing underlies reflection/amplification DDoS and is still routinely mitigated with unreliable, manually-maintained ACLs or uRPF heuristics. SAVNET is the WG working an actual generic architecture, both within and across autonomous systems.
- **What**: `general-sav-capabilities` proposes SAV as a first-class data-plane capability rather than a byproduct of FIB-based uRPF, widening deployable scenarios and traffic-handling policy. `intra-domain-architecture` gives a generic framework so a single domain's SAV mechanisms can share validation rules and improve accuracy over uRPF-only approaches. `inter-domain-architecture` extends the same idea across AS boundaries, letting ASes exchange SAV-specific information to generate more trustworthy rules than routing-table inference alone provides. (from abstract only)
- **How**: Instead of deriving filters solely from existing routing state, SAVNET routers exchange SAV-specific signaling (intra-domain) or AS-level SAV information (inter-domain) to build filters that handle asymmetric routing correctly, with graceful fallback to general routing information during partial deployment.
- **Where applicable**: General network operator deployments; inter-domain SAV is explicitly designed for incremental rollout, so partial adoption still helps.

## Adjacent

### TLS Post-Quantum Migration — `draft-ietf-tls-ecdhe-mlkem`, `draft-ietf-tls-mldsa`, `draft-ietf-tls-trust-anchor-ids`

- **Tier**: Adjacent
- **Links**: [ecdhe-mlkem](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/), [mldsa](https://datatracker.ietf.org/doc/draft-ietf-tls-mldsa/), [trust-anchor-ids](https://datatracker.ietf.org/doc/draft-ietf-tls-trust-anchor-ids/)
- **Why**: The concrete mechanics of the PQ transition landing in the protocol every service already depends on — worth tracking for when to start budgeting for larger handshakes and certificate chains.
- **What**: `ecdhe-mlkem` defines three hybrid key-agreement mechanisms combining ML-KEM with ECDHE (X25519MLKEM768, SecP256r1MLKEM768, SecP384r1MLKEM1024). `mldsa` specifies using the ML-DSA post-quantum signature scheme (FIPS 204) for TLS 1.3 authentication. `trust-anchor-ids` lets servers describe available certification paths more succinctly and lets clients select among many trusted CAs, easing the transition-era problem of bloated trust stores. (from abstract only)
- **How**: Hybrid key agreement combines classical and PQ shared secrets so an attacker must break both; trust-anchor IDs can be advertised in DNS for lower-latency negotiation.
- **Where applicable**: General TLS 1.3 deployments planning a PQ migration path; hybrid schemes are the deployment-safe default while PQ-only confidence is still building.

### MASQUE IP & Ethernet Proxying over HTTP — `draft-ietf-masque-connect-ip`, `draft-ietf-masque-connect-ethernet`

- **Tier**: Adjacent
- **Links**: [connect-ip](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/), [connect-ethernet](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ethernet/)
- **Why**: This is "VPN-as-an-HTTP-extension" maturing past UDP proxying into full IP and now Layer 2 tunneling — relevant if you're evaluating HTTP-native alternatives to classic VPN protocols for client access or overlay transport.
- **What**: `connect-ip` proxies arbitrary IP packets over HTTP, letting a client build an IP tunnel through an HTTP server acting as proxy. `connect-ethernet` does the same one layer down, tunneling Ethernet frames through an HTTP server attached to a physical or virtual Ethernet segment. (from abstract only)
- **How**: Both build on the same HTTP Datagram/Capsule Protocol machinery MASQUE established for UDP proxying, generalized to carry raw IP or L2 frames instead.
- **Where applicable**: General; useful anywhere an HTTP load balancer is the only permitted ingress and you still need L3/L2 tunnel semantics behind it.

### Post-Quantum Crypto Plumbing Across COSE/JOSE/X.509 — `draft-ietf-cose-post-quantum-signatures`, `draft-ietf-lamps-kyber-certificates`, `draft-ietf-lamps-pq-composite-kem`, `draft-ietf-jose-pq-composite-sigs`

- **Tier**: Adjacent
- **Links**: [cose-post-quantum-signatures](https://datatracker.ietf.org/doc/draft-ietf-cose-post-quantum-signatures/), [lamps-kyber-certificates](https://datatracker.ietf.org/doc/draft-ietf-lamps-kyber-certificates/), [lamps-pq-composite-kem](https://datatracker.ietf.org/doc/draft-ietf-lamps-pq-composite-kem/), [jose-pq-composite-sigs](https://datatracker.ietf.org/doc/draft-ietf-jose-pq-composite-sigs/)
- **Why**: Less exciting than the TLS story but arguably more consequential for identity infra specifically: JOSE/COSE/X.509 are what OAuth tokens, workload credentials, and CMS/S-MIME actually ride on, so PQ support here is a precondition for the identity stack above to survive the transition.
- **What**: Registers PQ signature algorithm identifiers and serializations (ML-DSA/Dilithium, Falcon, SPHINCS+) for JOSE and COSE; specifies ML-KEM conventions for X.509 PKI; defines Composite ML-KEM combining PQ and traditional algorithms (RSA-OAEP, ECDH, X25519/X448) for extra protection against a break in either component; defines equivalent composite signature schemes for JOSE/COSE. (from abstract only)
- **How**: "Composite" constructions bind multiple algorithms into one atomic key/signature/KEM object at the protocol level, so a break in the PQ or the classical component alone doesn't compromise the whole credential.
- **Where applicable**: General; this is infrastructure work — relevant to anyone issuing or verifying certificates, JWTs, or CWTs who needs a PQ migration story, not an end-user-facing feature by itself.

### IKEv2 Post-Quantum Preshared-Key Mixing — `draft-ietf-ipsecme-qr-ikev2`

- **Tier**: Adjacent
- **Links**: [datatracker](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-qr-ikev2/)
- **Why**: "Harvest now, decrypt later" is a specific concern for anyone running long-lived IPsec VPN tunnels today; this is the near-term mitigation available before full PQ key-exchange support lands in IKEv2.
- **What**: Extends IKEv2 to resist a future quantum computer by mixing preshared keys into the key derivation, without waiting for quantum-secure key-exchange algorithms to be standardized and deployed in IKEv2 itself. (from abstract only)
- **How**: A PSK, distributed out-of-band, is mixed into the IKEv2-derived key material so that breaking the classical Diffie-Hellman exchange alone isn't sufficient to recover session keys.
- **Where applicable**: General IPsec/IKEv2 deployments wanting a stopgap against harvest-now-decrypt-later before native PQ key exchange in IKEv2 matures.

### ACME Remote Attestation & Device Attestation Challenges — `draft-ietf-acme-rats`, `draft-ietf-acme-device-attest`

- **Tier**: Adjacent
- **Links**: [acme-rats](https://datatracker.ietf.org/doc/draft-ietf-acme-rats/), [device-attest](https://datatracker.ietf.org/doc/draft-ietf-acme-device-attest/)
- **Why**: Shows the RATS attestation stack (Core, above) landing in a concrete consumer: certificate issuance gated on proof of device/hardware state, not just domain-control validation. Relevant to any automated cert-issuance pipeline for devices or workloads.
- **What**: `acme-rats` lets an ACME server challenge a client to provide RATS-framework Evidence, Endorsements, or Attestation Results (via CMW) before issuing a certificate, optionally requesting specific claims. `device-attest` specifies identifiers and a challenge for validating a device's identity via attestation, with an update enabling a privacy-preserving identifier mode. (from abstract only)
- **How**: The ACME challenge-response flow is extended so "prove domain control" can be replaced or supplemented by "prove device/platform integrity" using the same Evidence/Verifier machinery RATS defines generally.
- **Where applicable**: IoT and managed-device fleets doing automated certificate issuance/renewal where hardware-backed proof of state matters more than pure domain ownership.

## Wildcard

### JSON Web Proof & JSON Proof Token — `draft-ietf-jose-json-web-proof`, `draft-ietf-jose-json-proof-token`

- **Tier**: Wildcard
- **Links**: [json-web-proof](https://datatracker.ietf.org/doc/draft-ietf-jose-json-web-proof/), [json-proof-token](https://datatracker.ietf.org/doc/draft-ietf-jose-json-proof-token/)
- **Why**: Not a direct fit for your day-to-day work, but it's a structurally different answer to selective disclosure than SD-JWT (Core, above): a new container format built for Zero-Knowledge Proof–based unlinkable presentation, not just "redact fields from a signed blob." Worth having on the radar as the more ambitious long-term direction.
- **What**: JSON Web Proof (JWP) is a new container format, parallel to JWS, that can integrity-protect *multiple* payloads in one message and supports a presentation form with selective disclosure, additional proof computation, and replay protection. JSON Proof Token (JPT) is the claims-token profile built on JWP, explicitly supporting reusability and unlinkability via Zero-Knowledge Proofs. (from abstract only, individual submissions — not yet WG-adopted at `draft-ietf-*` status for the JOSE variants shown, worth checking current adoption state before assuming momentum)
- **How**: Unlike JWS's single signed payload, JWP structures multiple payloads so a holder can selectively disclose a subset and, with ZKP-capable algorithms, prove statements about undisclosed payloads without revealing them or making separate presentations linkable to each other.
- **Where applicable**: General, but aimed squarely at privacy-sensitive credential presentation (digital ID wallets) where even SD-JWT's "redact and reveal" model still leaks presentation-linkability that ZKPs are designed to avoid.

### COSE Receipts / Merkle Tree Proofs with CCF — `draft-ietf-cose-merkle-tree-proofs`, `draft-ietf-scitt-receipts-ccf-profile`

- **Tier**: Wildcard
- **Links**: [cose-merkle-tree-proofs](https://datatracker.ietf.org/doc/draft-ietf-cose-merkle-tree-proofs/), [scitt-receipts-ccf-profile](https://datatracker.ietf.org/doc/draft-ietf-scitt-receipts-ccf-profile/)
- **Why**: A genuinely different trust primitive from certificates: instead of "a CA vouches for this key," a verifiable-ledger receipt proves "this statement was logged, at this point, tamper-evidently" — the same shape of guarantee Certificate Transparency gives certs, generalized to arbitrary signed statements.
- **What**: `cose-merkle-tree-proofs` (COSE Receipts) proves properties of a verifiable data structure to a verifier — minimal disclosure, transparency, non-equivocation — via CBOR encodings of Merkle inclusion and consistency proofs. `receipts-ccf-profile` profiles this specifically for logs produced by Microsoft's Confidential Consortium Framework (CCF), a TEE-backed ledger, for stronger tamper-evidence guarantees. (from abstract only)
- **How**: A transparency service appends a signed statement to a Merkle-tree-backed log and returns a receipt (an inclusion proof) that any relying party can verify offline against the log's published root, without trusting the service itself beyond its published commitments.
- **Where applicable**: Currently narrow (CCF-specific profile), but the underlying COSE Receipts mechanism is designed to generalize — it's the proof format underneath SCITT (Core, above) and worth understanding as transparency-ledger patterns spread beyond certificates.

### RATS Epoch Markers — `draft-ietf-rats-epoch-markers`

- **Tier**: Wildcard
- **Links**: [datatracker](https://datatracker.ietf.org/doc/draft-ietf-rats-epoch-markers/)
- **Why**: A small, elegant primitive for a problem that's usually solved badly: proving "freshness" without trusting every device's local clock. Not something you'll deploy directly, but a pattern worth recognizing when it shows up elsewhere.
- **What**: Defines Epoch Markers — "time ticks" produced and distributed by a dedicated system (the Epoch Bell) — so that receiving a specific marker establishes a shared notion of a new epoch across all recipients, without each system needing to track freshness via its own real-time clock. (from abstract only)
- **How**: Instead of timestamping and trusting clock sync, participants agree on freshness by reference to the same externally-distributed marker (CBOR time tags, RFC 3161 tokens, or nonce-like structures), embeddable as a CWT claim.
- **Where applicable**: General distributed-systems freshness problem, framed here for attestation replay-resistance but not architecturally specific to RATS — the kind of primitive that tends to get reinvented per-protocol until someone standardizes it once.

## Themes

- **Workload identity has a nearly-complete stack, not just an architecture.** WIMSE's arch, s2s-protocol, mutual-tls, http-signature, workload-creds, wpt, and identifier drafts now cover naming, credentials, proof-of-possession, and three transport bindings — this is the biggest concrete signal of the cycle for anyone building or evaluating workload-identity tooling.
- **OAuth is absorbing "propagate identity across trust domains" as core scope**, not an afterthought — transaction tokens, identity chaining, attestation-based client auth, and cross-app access are all pieces of the same multi-hop/agentic authorization problem, converging from the OAuth side rather than a clean-slate protocol.
- **Selective disclosure is now a three-way race** (SD-JWT, SD-CWT, and the more ambitious ZKP-based JSON Web Proof) rather than a single converged format — worth watching which one(s) actually get deployment traction versus staying individual submissions.
- **Post-quantum migration has moved from algorithm bake-off to wiring it into everything**: TLS, IKEv2, CMS, X.509, JOSE, and COSE all have concrete hybrid/composite drafts in flight this cycle, and composite constructions (bind PQ + classical into one atomic object) are the emerging default pattern across all of them.
- **Remote attestation (RATS) is becoming shared infrastructure**, not a niche TPM feature — it's the trust root ACME device-attestation is being built on, and conceptually adjacent to the receipt/transparency mechanisms SCITT uses for supply-chain provenance.
- **DC fabric standardization keeps converging on Geneve**, with this cycle's NVO3 work filling in the operational gap (OAM) rather than revisiting the encapsulation choice itself — the interesting risk called out by the WG's own encapsulation-considerations draft is what happens at the boundary between hardware and software tunnel endpoints running different encaps.
