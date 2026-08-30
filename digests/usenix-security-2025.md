<!--
conference: USENIX Security '25 (34th USENIX Security Symposium)
type: academic
source_url: https://www.usenix.org/conference/usenixsecurity25/technical-sessions
generated: 2026-08-30
registry_key: usenix-security-2025
-->

# USENIX Security '25 (34th USENIX Security Symposium) — Digest

Program source is the expanded technical-sessions schedule (titles, authors, and full abstracts; no PDF/slide/recording links were present in the pasted program text, so no Links field is included below — every write-up is grounded in the abstract only). USENIX Security is enormous (380+ accepted papers plus Enigma industry talks across three days); this is a tight cut toward the PM's stated interests — physical DC/WAN networking, cloud-native networking, network security, and identity/authentication — with most of the program (ML/AI privacy, blockchain internals, mobile-app privacy measurement, hardware fault injection unrelated to networking) left out.

## Core

### Trust Agility in an Era of Transient Ties: Rethinking TLS Trust in a Rapidly Evolving Ecosystem

*Hoss Shafagh, Netflix (Enigma track)* — **Core**

- **Why**: A practitioner-level look at the most consequential near-term shift in the Web PKI — root programs shortening server certificate lifetimes to a maximum of 47 days by 2029 — from someone who runs PKI and workload-identity infrastructure at Netflix scale, not a standards document.
- **What**: An argument for "trust agility" — the ability to rapidly and securely update trust relationships as certificate authorities, cryptographic standards, and threat models evolve — as the operational response to shortening cert lifetimes, slower-upgrading consumer devices, and growing non-browser (machine-to-machine, workload identity) use cases that fall outside traditional browser trust models. (from abstract only)
- **How**: Draws on real-world PKI operations at Netflix to describe automation and lifecycle-aware certificate management strategies across diverse endpoints, including preparing for post-quantum cryptographic transitions. (from abstract only)
- **Where applicable**: Anyone operating PKI/TLS infrastructure at scale, workload-identity systems, or IoT/embedded fleets with slow upgrade cycles; general but grounded in a large-scale production environment.

### BGP Vortex: Update Message Floods Can Create Internet Instabilities

*Felix Stöger, ETH Zurich; Henry Birge-Lee, Princeton University; Giacomo Giuliari, Mysten Labs; Jordi Subira-Nieto and Adrian Perrig, ETH Zurich* — **Core**

- **Why**: A new BGP instability attack that neither BGPSEC nor RPKI can prevent, because every message involved is a legitimate, standards-compliant BGP UPDATE — a reminder that route-origin validation alone doesn't close the routing-security gap.
- **What**: Discovery of the "BGP Vortex," a configuration where just three legitimate BGP UPDATE messages trigger persistent instability, weaponizable to cause router overload and forwarding loops across the Internet. All major router implementations tested were susceptible. (from abstract only)
- **How**: Exploits standards-compliant BGP Communities extensions (used for traffic engineering) that allow route-preference modification; the paper proposes a framework for classifying which BGP extensions are similarly dangerous versus safe to deploy. (from abstract only)
- **Where applicable**: General for any BGP-speaking network; the mitigation framework is for router vendors and operators using BGP Communities-based traffic engineering.

### Ares: Comprehensive Path Hijacking Detection via Routing Tree

*Yinxiang Tao et al., Tsinghua University / Zhongguancun Laboratory / Quan Cheng Laboratory; Congcong Miao, Tencent* — **Core**

- **Why**: Path hijacking (manipulating AS-path attributes rather than just the origin) is the stealthier successor to origin hijacking specifically designed to evade existing detection — this is a system that closes that gap with real-event validation, not just simulation.
- **What**: Ares, a system detecting path hijacking by tracking changes to an AS's "observed prefix routing tree" (OPRT), validated against 12 real-world hijacking events (detected within 5 minutes each) and large-scale simulation (97.2%–99.3% detection rate, 1.06% false-positive rate). (from abstract only)
- **How**: Uses weighted edit distance between routing trees to quantify anomalous change, combined with clustering to accelerate detection and heuristics to reduce false positives; generates ~2.31 alerts/hour across the entire Internet. (from abstract only)
- **Where applicable**: General BGP route-hijacking detection for network operators and Tier-1/content ASes; a deployable detection system rather than a protocol change.

### Haunted by Legacy: Discovering and Exploiting Vulnerable Tunnelling Hosts

*Angelos Beitis and Mathy Vanhoef, DistriNet, KU Leuven* — **Core**

- **Why**: The same tunneling encapsulation families underlying datacenter and WAN overlay networking — GRE, IPIP, and IPv4/IPv6 translation tunnels — turn out to have over 4 million open, unauthenticated hosts on the public Internet, directly relevant to anyone running or securing tunnel endpoints.
- **What**: An Internet-wide scan finding 4M+ hosts that accept unauthenticated IPIP, GRE, 4in6, or 6in4 tunneling traffic, exploitable as one-way proxies, for source-address spoofing, or for access into private networks — plus two new amplification-based DoS attacks (16x and 75x amplification) and an Economic DoS attack that drains a host's outgoing bandwidth. (from abstract only)
- **How**: Seven distinct IPv4/IPv6 scan methods identify hosts accepting unauthenticated tunneling traffic; the amplification attacks work by concentrating traffic in time or looping packets between vulnerable hosts. (from abstract only)
- **Where applicable**: General for any network exposing GRE/IPIP/4in6/6in4 tunnel endpoints to the Internet without authentication — directly applicable to DC/WAN overlay and legacy IPv6-transition tunnel deployments specifically, not just an academic curiosity.

### Lemon: Network-Wide DDoS Detection with Routing-Oblivious Per-Flow Measurement

*Wenhao Wu et al., Institute of Computing Technology / Chinese Academy of Sciences* — **Core**

- **Why**: A DDoS-detection system implemented and evaluated on real programmable switch hardware (Tofino), directly relevant to datapath/programmable-networking work, that solves a genuine correctness problem (over-counting from unpredictable routing) rather than just adding another ML classifier.
- **What**: Lemon, a network-wide DDoS detection system that stays accurate even when traffic routing is unpredictable and invalidates the operator's assumed network topology — a failure mode that breaks existing sketch-based measurement systems. (from abstract only)
- **How**: A novel "Lemon sketch" data structure in the data plane avoids over-counting and mis-allocation across measurement points; a control plane aggregates sketches for network-wide, per-flow DDoS detection and victim identification. Implemented in both software (Bmv2) and programmable hardware (Tofino) switches. (from abstract only)
- **Where applicable**: General DDoS-detection deployments on programmable data-plane hardware (P4/Tofino-class switches); the routing-obliviousness is specifically valuable for networks with dynamic or asymmetric routing.

### Exposing and Circumventing SNI-based QUIC Censorship of the Great Firewall of China

*Ali Zohaib et al., University of Massachusetts Amherst / GFW Report / University of Colorado Boulder / Stanford University* — **Core**

- **Why**: A rigorous measurement of a nation-state QUIC-blocking system reveals a real architectural weakness (decryption overhead collapses effectiveness under load) and a real weaponization risk (it can be triggered to block arbitrary UDP traffic between third parties) — directly relevant to anyone reasoning about QUIC/UDP behavior at the network edge.
- **What**: The GFW decrypts QUIC Initial packets at scale to apply SNI-based blocking, using a blocklist distinct from its other censorship mechanisms; the paper finds this decryption is computationally expensive enough to fail under moderate traffic and can be weaponized to block unrelated UDP traffic. Circumvention strategies were integrated into Firefox, quic-go, and major circumvention tools. (from abstract only)
- **How**: Active measurement characterizes what triggers GFW QUIC blocking; the weaponization angle exploits the same decryption-at-scale mechanism against arbitrary third-party UDP flows. (from abstract only)
- **Where applicable**: General for QUIC/UDP traffic traversing state-level middleboxes; the weaponization finding is a general lesson about any inline-decryption censorship/inspection architecture, not GFW-specific.

### Universal Cross-app Attacks: Exploiting and Securing OAuth 2.0 in Integration Platforms

*Kaixuan Luo et al., The Chinese University of Hong Kong; Samsung Research America* — **Core**

- **Why**: A platform-wide OAuth account-linking design flaw affecting Microsoft, Google, and Amazon integration platforms — a concrete, high-severity (CVSS 9.6) example of exactly the kind of OAuth/identity-integration failure that matters at the architecture level, not the implementation level.
- **What**: Two new attacks — Cross-app OAuth Account Takeover (COAT) and Request Forgery (CORF) — exploiting the lack of app differentiation in multi-app OAuth account-linking on integration platforms (Workflow Automation, Virtual Assistants, Smart Homes). 11 of 18 tested platforms were vulnerable to COAT and 5 to CORF. (from abstract only)
- **How**: Built COVScan, a semi-automated black-box tool that profiles OAuth designs across platforms to find cross-app vulnerabilities; a victim risks account takeover simply by linking any single malicious app, or even clicking a crafted link. (from abstract only)
- **Where applicable**: General for any platform supporting third-party app marketplaces with OAuth-based account linking; the architectural lesson (differentiate apps, not just users, in the OAuth trust model) generalizes beyond the specific platforms tested.

### Detecting Compromise of Passkey Storage on the Cloud (CASPER)

*Mazharul Islam et al., University of Wisconsin–Madison; Visa Research* — **Core**

- **Why**: Directly addresses a real gap in FIDO2 passkey deployments: cloud-synced passkeys solve the account-recovery problem but reintroduce a breach surface (the passkey management service's cloud storage) that today's defenses can't close without breaking recovery or login UX.
- **What**: CASPER, the first framework letting web service providers detect abuse of passkeys leaked from a passkey management service (PMS), even against attackers who strategically adapt to evade detection. (from abstract only)
- **How**: Integrates into existing passkey backup/sync/authentication flows with minimal UX impact, negligible performance overhead, and low deployment complexity for participating services. (from abstract only — detection mechanism specifics not given)
- **Where applicable**: General for any relying party accepting FIDO2 synced passkeys; directly actionable for services already on the passkey adoption path.

### Towards Practical, End-to-End Formally Verified X.509 Certificate Validators (Verdict)

*Zhengyao Lin et al., Carnegie Mellon University; Northeastern University* — **Core**

- **Why**: X.509 validation bugs have a long history of real security vulnerabilities precisely because the standards are ambiguous and every validator deviates idiosyncratically — this is the first end-to-end formally verified validator, proven to match Chrome/Firefox/OpenSSL's actual (not just documented) behavior at scale.
- **What**: Verdict, a formally verified X.509 certificate validator (parsing, path building, path validation) with customizable, formally-specified validation policies compiled to efficient Rust code; validated against Chrome, Firefox, and OpenSSL policies on over ten million real Certificate Transparency certificates. (from abstract only)
- **How**: Validation policy is specified in first-order logic; a proof-producing compiler generates Rust code proven to conform to a subset of RFC requirements, and Verdict is shown to match each baseline's actual behavior and performance. (from abstract only)
- **Where applicable**: General; directly relevant to anyone building or auditing a TLS/PKI stack who wants provable conformance rather than "matches OpenSSL's quirks by accident."

### STEK Sharing is Not Caring: Bypassing TLS Authentication in Web Servers Using Session Tickets

*Sven Hebrok et al., Paderborn University* — **Core**

- **Why**: A concrete, large-scale-confirmed TLS authentication bypass in virtual hosting — exactly the multi-tenant TLS-termination pattern common in cloud/CDN infrastructure — affecting Apache, nginx, (Open)LiteSpeed, and Caddy, plus real providers including Fastly.
- **What**: Session ticket confusion vulnerabilities in TLS session resumption under virtual hosting, where a shared Session Ticket Encryption Key (STEK) across virtual hosts on one physical server breaks isolation, enabling bypass of client and server authentication. All four tested server implementations were vulnerable to client-auth bypass; a large-scale scan found six clusters of providers vulnerable to server-auth bypass. (from abstract only)
- **How**: Exploits inconsistent STEK handling across virtual hosts sharing one physical server during TLS session resumption to confuse which host a resumed session actually authenticates. (from abstract only)
- **Where applicable**: General for any TLS termination point serving multiple virtual hosts/tenants from shared infrastructure with session-ticket resumption enabled — a direct operational risk for multi-tenant edge/CDN/load-balancer deployments.

### Robustifying ML-powered Network Classifiers with PANTS

*Minhao Jin and Maria Apostolaki, Princeton University* — **Core**

- **Why**: ML-based traffic classification is increasingly load-bearing for resource allocation and intrusion detection in cloud-native networking, and this is a practical, white-box framework for finding and fixing adversarial blind spots in exactly that class of system.
- **What**: PANTS, a white-box framework combining adversarial ML with SMT solvers to generate realizable adversarial inputs against ML-based network traffic classifiers (MNCs), plus an iterative adversarial-training process that hardens MNCs against them. Outperforms prior baselines (Amoeba, BAP) by 70%–2x in finding adversarial inputs and improves target-model robustness by 52.7% without sacrificing accuracy. (from abstract only)
- **How**: Integrates SMT solving to handle MNC-specific challenges — non-differentiable components like traffic engineering, and semantic/reliability constraints on realizable inputs — that block direct use of standard gradient-based adversarial ML methods. (from abstract only)
- **Where applicable**: General for network operators deploying ML-based traffic classification (intrusion detection, resource allocation); a practical robustness-testing and hardening tool, not just an attack demonstration.

### X.509DoS: Exploiting and Detecting Denial-of-Service Vulnerabilities in Cryptographic Libraries Using Crafted X.509 Certificates

*Bing Shi et al., Alibaba Group; Luyi Xing, Indiana University Bloomington* — **Core**

- **Why**: A systematic study of an underexplored class of cryptographic-library vulnerability — availability, not confidentiality/integrity — finding 18 new and 12 previously known CVEs across seven mainstream crypto libraries, all reachable via crafted certificates rather than exotic inputs.
- **What**: X.509DoS, a class of denial-of-service attacks against cryptographic library implementations, launched via specially crafted X.509 certificates; a tool for rapidly generating such certificates and detecting the underlying DoS vulnerabilities. (from abstract only)
- **How**: Systematically probes implementations handling X.509 certificates for availability-impacting bugs, showing that spec/standard compliance alone does not guarantee resistance to resource-exhaustion attacks. (from abstract only)
- **Where applicable**: General for any service parsing/validating X.509 certificates from untrusted input (TLS servers, mTLS endpoints); the finding that standards-compliance ≠ DoS-safety generalizes beyond the seven libraries tested.

## Adjacent

### Assessing the Aftermath: The Effects of a Global Takedown Against DDoS-for-hire Services

*Anh V. Vu et al., University of Cambridge; University of Edinburgh; University of Strathclyde; University of Illinois Chicago* — **Adjacent**

- **Why**: A rare quantitative, multi-year measurement of whether law-enforcement disruption actually works against the DDoS-for-hire ecosystem — useful context for anyone evaluating DDoS threat trends rather than just technical mitigation.
- **What**: An assessment of the largest booter takedown effort to date (since December 2022), finding over half of seized sites returned within a day, traffic to re-emerged domains dropped 80–90%, and the first takedown wave cut global DDoS volume 20–40% (with a significant effect specifically on UDP-based attacks) — but the overall market proved resilient, with effects lasting at most ~6 weeks. (from abstract only)
- **How**: Combines web traffic data, ground-truth visits to seized sites, millions of DDoS attack records, and underground-forum/Telegram chat analysis. (from abstract only)
- **Where applicable**: General threat-intelligence context for DDoS trend forecasting; policy-relevant more than technically actionable for network defenders directly.

### S/MINE: Collecting and Analyzing S/MIME Certificates at Scale

*Gurur Öndarö et al., Münster University of Applied Sciences; Fraunhofer SIT / ATHENE* — **Adjacent**

- **Why**: The first broad empirical look at S/MIME's real-world PKI health (41M+ certificates), complementing the Verdict/X.509DoS/Trust-Agility picks above with a specific-but-large PKI ecosystem case study.
- **What**: Analysis of 41M+ real-world S/MIME certificates collected from public LDAP address books, finding the trust-chain and cryptographic health of the S/MIME PKI is generally improving (weak keys expiring, weak algorithms phasing out) but many certificates are issued by non-publicly-trusted CAs, and RFCs/clients should be more stringent about what counts as a valid S/MIME cert. (from abstract only)
- **How**: Large-scale collection and trust-chain construction from public LDAP directories, cross-referenced against CA/Browser Forum S/MIME Baseline Requirements. (from abstract only)
- **Where applicable**: General email security / S/MIME PKI ecosystem health; most directly useful to CAs and email client implementers.

### 5G and Cellular Network Security

*Multiple papers/teams — see below* — **Adjacent**

- **Why**: A dense cluster of 5G/cellular protocol-security papers this cycle — worth a combined mention as a vertical, even though cellular/RAN isn't explicitly named in the PM's core interests, because the architectural patterns (control/data-plane separation, standardized network functions) echo cloud-native networking design.
- **What**: `AKMA+` (Singapore Management University et al.) finds and fixes vulnerabilities in 5G's Authentication and Key Management for Applications protocol while preserving standards compatibility. `SNI5GECT` (SUTD) sniffs and injects into pre-authentication 5G NR messages without a rogue base station, achieving 70–90% attack success within 20m. `CoreCrisis` (Penn State) is a stateful fuzzer that found 13 crashing and 7 spec-deviation vulnerabilities across three open-source and one commercial 5G core implementation. `GLaDoS` (ETH Zurich / Oxford) is a full-scale deployed system for geofenced cellular denial-of-service in sensitive areas, neutralizing 99.3% of connections across 100+ commercial cells. (from abstract only)
- **How**: Varies by paper — protocol formal analysis (AKMA+), pre-auth sniff-and-inject (SNI5GECT), stateful black-box fuzzing with FSM learning (CoreCrisis), and combined overshadowing + localization (GLaDoS). (from abstract only)
- **Where applicable**: 5G core/RAN operators and equipment vendors specifically; GLaDoS is also relevant to physical-security/sensitive-facility contexts wanting legal, geofenced cellular control.

### Towards Internet-Based State Learning of TLS State Machines

*Marcel Maehren et al., Ruhr University Bochum; Paderborn University* — **Adjacent**

- **Why**: Extends TLS state-machine learning (previously only usable in controlled local environments) to work across the real, noisy Internet at scale — a methodology advance more than a single vulnerability finding, though it did surface a real Citrix NetScaler integrity bug and new CBC padding oracles.
- **What**: The first large-scale (7,337 domains, 1,304 extracted models) study of TLS implementation state machines learned directly over the Internet, handling jitter, load balancers, and non-determinism that previously confined this technique to lab settings. Found a handshake transcript integrity vulnerability in Citrix NetScaler and new CBC padding oracle vulnerabilities. (from abstract only)
- **How**: Extends Mealy-machine state-learning techniques with new handling for large protocol alphabets and automated analysis of the resulting automata, plus support for session resumption, renegotiation, and CBC padding-oracle-relevant features previously excluded. (from abstract only)
- **Where applicable**: General TLS implementation testing methodology; directly useful to anyone auditing TLS stacks at scale rather than one implementation at a time.

### An Industry Interview Study of Software Signing for Supply Chain Security

*Kelechi G. Kalu et al., Purdue University* — **Adjacent**

- **Why**: Software signing is widely recommended by supply-chain security frameworks but adoption remains low — this is the first in-depth practitioner account of why, complementing the technical PKI/cert-validation picks above with the human/organizational side.
- **What**: Interviews with 18 experienced security practitioners across 13 organizations on software-signing adoption, surfacing technical, organizational, and human barriers; finds experts disagree on signing's importance and documents how internal/external events (breaches, new regulation) drive adoption. (from abstract only)
- **How**: Qualitative interview study producing a refined software-supply-chain factory model highlighting where and why signing practices break down. (from abstract only)
- **Where applicable**: General for organizations evaluating or mandating software signing as part of supply-chain security policy.

### A Framework for Abusability Analysis: The Case of Passkeys in Interpersonal Threat Models

*Alaa Daffalla et al., Cornell University / Cornell Tech; University of Wisconsin–Madison; New York University* — **Adjacent**

- **Why**: The first analysis of how passkeys — the largest current push toward passwordless authentication — interact with interpersonal threat models (intimate partner violence, elder abuse), a threat class that's easy to overlook when passkey security is evaluated only against remote attackers.
- **What**: An abusability-analysis framework applied to 19 passkey-supporting services, finding abuse vectors including flawed implementations that let an abuser maintain ongoing illicit access with no recovery path for the victim, and vectors that let attackers lock victims out or gaslight them. (from abstract only)
- **How**: A general framework for identifying how new authentication features can be exploited by an adversary with routine physical device access and partial credential knowledge — applied specifically to passkey account-recovery and device-management flows. (from abstract only)
- **Where applicable**: General framework applicable beyond passkeys; the passkey-specific findings are directly relevant to anyone implementing or evaluating passkey account-recovery UX.

### Post-Quantum Secure Messaging: Signal, MLS, and iMessage PQ3

*Multiple papers/teams — see below* — **Adjacent**

- **Why**: A cluster of formal-methods papers rigorously analyzing post-quantum secure-messaging protocols already in production (Signal's PQXDH, Apple's iMessage PQ3, IETF-standardized MLS) — the identity/crypto-agility theme from the Netflix Enigma talk playing out at the protocol-design layer.
- **What**: `Bundled Authenticated Key Exchange` (AIST/PQShield) formally shows Signal's X3DH and PQXDH don't achieve "optimal" security under a new unified model, and introduces RingXKEM, a fully post-quantum handshake that does. A companion paper does the same for deniability guarantees specifically, building an efficient deniable ring-signature scheme from NIST-standardized Falcon. A third paper machine-verifies Apple's iMessage PQ3 protocol in the TAMARIN prover, including previously-thought-infeasible unbounded-loop ratchet analysis. A fourth explores more efficient post-quantum authentication modes for IETF-standardized MLS group messaging, trading some security for up to 75x lower post-quantum communication overhead. (from abstract only)
- **How**: Formal/symbolic verification (TAMARIN) and unified concrete-security models applied to already-deployed or standardized PQ messaging handshakes, rather than proposing yet another new protocol from scratch. (from abstract only)
- **Where applicable**: General for anyone implementing or evaluating post-quantum secure messaging; directly relevant given Signal, Apple, and IETF (MLS) are all production deployments, not research prototypes.

## Wildcard

### Catch-22: Uncovering Compromised Hosts Using SSH Public Keys

*Cristian Munteanu et al., Max Planck Institute for Informatics; Delft University of Technology (Distinguished Paper Award Winner)* — **Wildcard**

- **Why**: A clever, minimally-invasive Internet-scale detection technique — using SSH's own public-key-authentication challenge behavior to fingerprint compromise without ever needing valid credentials or touching the compromised system — that found state-actor-associated keys inside sensitive ASes.
- **What**: A method identifying 21,700+ compromised SSH servers across 1,649 ASes and 144 countries by checking for the presence of known-malicious attacker public keys, without needing to log in or test passwords; surfaced new context on botnets (fritzfrog), threat actors (teamtnt), and state-actor-linked keys in sensitive networks. (from abstract only)
- **How**: Exploits the fact that SSH only sends a public-key-authentication challenge if the corresponding key is actually present on the server — letting a scanner test for known malicious keys' presence with zero access and zero risk of triggering an actual login. (from abstract only)
- **Where applicable**: General Internet-scale compromise detection; the technique's elegance (a side effect of protocol behavior, not a vulnerability) is the interesting part, applicable anywhere an authentication protocol leaks presence information.

### LEO-Range: Physical Layer Design for Secure Ranging with Low Earth Orbiting Satellites

*Daniele Coppola et al., ETH Zurich; CISPA Helmholtz Center for Information Security* — **Wildcard**

- **Why**: Not a fit for the PM's terrestrial DC/WAN focus directly, but LEO satellite constellations are an increasingly real backhaul/connectivity layer, and this is provably-secure physical-layer ranging design for exactly that emerging infrastructure — the kind of "where the physical network is heading" signal worth having on the radar.
- **What**: A physical-layer design for secure distance ranging between LEO satellites and ground devices, compatible with OFDM (used by high-bandwidth satellite links), with a formal security proof bounding an attacker's probability of a distance-reduction attack. Tested with a hardware satellite-channel emulator, limiting spoofing to under a 2⁻²⁰ success probability for a 117m distance-reduction attempt in realistic channel conditions. (from abstract only)
- **How**: A novel frequency-domain verification scheme provides provable security against arbitrary physical-layer attack strategies, rather than relying on a specific attacker model. (from abstract only)
- **Where applicable**: LEO satellite communication systems specifically; general technique for physical-layer secure ranging that could generalize to other wireless ranging contexts.

### Red Bleed: A Pragmatic Near-Infrared Presentation Attack on Facial Biometric Authentication Systems

*Bowen Hu, Kuo Wang, and Chip Hong Chang, Nanyang Technological University* — **Wildcard**

- **Why**: A practical, sub-$400 hardware attack defeating a widely-deployed commercial biometric authentication system (Windows Hello, confirmed by Microsoft's own security response center) — a concrete demonstration that "commercial-off-the-shelf NIR biometric = secure" is no longer a safe assumption.
- **What**: Red Bleed, a presentation attack against near-infrared (NIR) facial biometric authentication (e.g., Windows Hello, Apple Face ID) using a custom-built consumer LCD display costing under $400, converting ordinary visible-light face images/video into convincing NIR spoofs. Confirmed against a commercial Windows Hello module with a CVE scheduled for disclosure. (from abstract only)
- **How**: A generative framework (VAE-based) converts RGB/visible-spectrum face images or video into the NIR domain, combined with face-swapping, so attackers can use easily-obtainable RGB material (social media photos, video calls) rather than needing rare NIR footage of the target. (from abstract only)
- **Where applicable**: NIR-based facial biometric authentication specifically (a widely deployed modality); a hardware/software technique that generalizes to any NIR liveness-detection system relying on the assumption that commodity displays can't emit convincing NIR.

### Deanonymizing Ethereum Validators: The P2P Network Has a Privacy Issue

*Lioba Heimbach et al., ETH Zurich; University of Bern; IMDEA Networks* — **Wildcard**

- **Why**: Not a blockchain-economics paper — a peer-to-peer network privacy/deanonymization finding (any node can link validator identities to peer IP addresses) that's really a P2P protocol design lesson wearing blockchain clothing, relevant to anyone reasoning about identity-unlinkability guarantees in P2P systems generally.
- **What**: Demonstrates the Ethereum P2P network fails to provide its intended validator anonymity — any participating node can link a validator's identifier to a peer's IP address. Using data from just four nodes over three days, the authors located 15%+ of all Ethereum validators, including geographic location and hosting organization. Awarded a bug bounty by the Ethereum Foundation. (from abstract only)
- **How**: A methodology for any P2P node to correlate validator identifiers with connected peers' network-level metadata, empirically validated at scale rather than theorized. (from abstract only)
- **Where applicable**: Directly Ethereum-specific in its finding, but the underlying lesson — that P2P protocols claiming participant anonymity need explicit defenses against peer-correlation attacks, not just identifier obfuscation — generalizes to any P2P system with an unlinkability goal.

## Themes

- **BGP/routing security keeps finding fresh, standards-compliant attack surface.** BGP Vortex (legitimate UPDATE messages triggering instability) and Ares (stealthy path hijacking bypassing origin-only defenses) both show that RPKI/ROV-class defenses, while necessary, don't close the routing-security gap — the protocol's own legitimate extensibility is the remaining attack surface.
- **Tunnel and overlay endpoints are under-defended at Internet scale.** "Haunted by Legacy" found 4M+ open GRE/IPIP/4in6/6in4 hosts — the same encapsulation families underlying DC/WAN overlay networking — a concrete reminder that tunnel endpoints need the same perimeter discipline as any other network boundary, not an implicit trust assumption.
- **Identity infrastructure is being stress-tested at the integration layer, not just the crypto layer.** Passkey cloud-backup compromise (CASPER), OAuth account-linking takedown (Universal Cross-app Attacks), and formally verified X.509 validation (Verdict) all target where standards meet real deployment — the place bugs actually live.
- **Crypto-agility has gone from aspiration to forcing function.** The Netflix Enigma talk on 47-day certificate lifetimes by 2029 sets the operational stakes; the post-quantum secure-messaging cluster (Signal, iMessage PQ3, MLS) shows the same agility pressure playing out at the protocol-design layer for already-deployed systems, not hypothetical future ones.
- **5G/cellular core and RAN security remains a rich, mostly-unsolved vertical.** Multiple independent groups this cycle found fundamental protocol-level gaps (AKMA linkability, pre-auth message injection, core-network fuzzing crashes, geofenced DoS) — worth periodic monitoring even outside a primary cloud-native/DC focus, since the control/data-plane separation patterns echo modern network function design.
- **The most memorable findings this cycle are cheap, elegant techniques, not brute-force ones.** A sub-$400 LCD spoofing commercial biometric hardware, an SSH protocol side-effect fingerprinting 21,700+ compromised hosts with zero access, and three legitimate BGP messages destabilizing routers all make the same point: novel low-cost techniques against deployed systems remain more interesting than incremental ML-classifier papers.
