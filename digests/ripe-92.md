<!--
conference: RIPE 92 (Edinburgh)
type: operator
source_url: https://ripe92.ripe.net/programme/meeting-plan/
generated: 2026-11-03
registry_key: ripe-92
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# RIPE 92 (Edinburgh) — Digest

An operator conference: the highest-value material here is postmortems, at-scale tooling, and the IP/optical integration wave now hitting DC and WAN fabrics.

## Core

### Evolution of Meta's Edge and Backbone Networks

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/72/TBKG3W/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/TBKG3W/resources/Meta_RIPE_Z6Steot.pdf) · [Recording](https://ripe92.ripe.net/media/videos/fredrik-korsback_evolution-of-metas-edge-and-backbone-networks_main_20260519-100207.mp4)

Fredrik Korsbäck, Meta Platforms, Inc

- **Why**: The most direct window at this conference into hyperscaler physical backbone and DC fabric design — scaling strategy, ZR optics economics, and how AI traffic is reshaping both DC metro fabric and edge compute placement.
- **What**: How Meta grew the backbone >10X via two levers: scaling up (8-slot/288-port to 12-slot/432-port chassis; 288×400G to 288×800G interfaces) and scaling out (4→8 planes, multiple devices per plane). One site more than doubled platform capacity every year for 7 years (~192x cumulative). The Edge side is shifting toward an "Elastic Edge" with a global GPU footprint closer to users for uncacheable AI-generated content, plus a move away from route-server peering toward an automated bilateral peering portal.
- **How**: Two distinct backbones: EBB (DC-to-DC, IPv6-only, multi-plane, with Meta's own TE/routing software, deployed in DCs and midpoints) and CBB (DC-to-PoP, traditional IP/MPLS, single-plane). DC-metro architecture keeps paired DCs within 10km connected with 100,000s of 400G on single fiber pairs via frontend/backend switches; >10km AI backbone links run 10,000s of 800G ZR (ILA-free to 120–150km, 500km+ with ILAs) with optical protection switches. ZR pluggables (10–15W/plug) replace ~2kW transponders: a 1Pb midpoint scenario shrinks from 58 racks to 21 (400G-ZR) or 14 (800G-ZR).
- **Where applicable**: The scale numbers are Meta-specific, but the ZR rack/power math, DC-metro fiber strategy, and plane-scaling approach transfer to anyone building DC interconnect or long-haul fabric.

### Channelmania! – future proof your DWDM network topology while keeping it flexible for 1.6T

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/72/Q9YPAZ/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/Q9YPAZ/resources/Flexoptix_-_Channelm_4BcipnC.pdf) · [Recording](https://ripe92.ripe.net/media/videos/thomas-weible_channelmania-future-proof-your-dwdm-network-topology-while-keeping-it-flexibl_main_20260519-090025.mp4)

Thomas Weible, FLEXOPTIX

- **Why**: As IPoDWDM collapses the IP/transport split, IP network people now need coherent-DWDM literacy — grid planning, superchannels, and what 400GHz COTS filters mean for upgrade paths to 1.6T.
- **What**: A technical primer-plus-argument: higher-order coherent modulation (16-constellation, dual-polarization, ~425Gbps at 53.125GBd) replaces OOK; 800G/1.6T superchannels need ~400GHz grids rather than shrinking 50/25GHz grids; and coherent detection being "blind" to other wavelengths enables filterless/colorless topologies at the cost of flexibility. The practical pitch: 12×400GHz COTS channels in the C-band future-proof the plant while staying backward-compatible with legacy 50GHz services.
- **How**: Walks through coherent receiver architecture (phase- and polarization-diversity, homodyne/heterodyne/intradyne), and even a DIY superchannel approach using cheap PLC 1x4 splitters to combine TX/split RX and run subbands through regular 50GHz muxes (with a nod to Blake Willis finding 100GHz spacing optimal in practice). Closing advice: plan in THz/GHz, not nm or channel numbers; 800G coherent ZR+ in DD/OSFP is here, and ~12.8T liquid-cooled XPO is approaching.
- **Where applicable**: Anyone planning or buying DWDM capacity. Vendor-authored (FLEXOPTIX sells optics tooling), so the COTS-400GHz-filter framing is partly self-serving, but the physics and frequency-planning methodology are sound and generally applicable.

### Understanding and optimising transceiver efficiency using internal metrics for improved power savings

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/76/EAF87P/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/EAF87P/resources/Flexoptix_-_RIPE92_3WzSdf9.pdf) · [Recording](https://ripe92.ripe.net/media/videos/gerhard-stein_understanding-and-optimising-transceiver-efficiency-using-internal-metrics-for-i_main_20260519-143142.mp4)

Gerhard Stein, Flexoptix GmbH

- **Why**: Transceiver power is becoming a first-order DC design constraint; this is one of the few talks showing how to actually measure and optimize it from data already readable off modern optics.
- **What**: How to use Versatile Diagnostics Monitoring (VDM, available on >100G optics) — especially Thermoelectric Cooler (TEC) current — alongside temperature and cable length to find the efficient operating point per transceiver, in Watts, on real hardware.
- **How**: TEC power is computed as V_trc × I_TEC from VDM (vs DDM which only exposes laser current); tested across 100G QSFP28, 400G coherent ZR, and 800G QSFP-DD transceivers on Cisco Nexus 93600CD-GX, Catalyst 9500, and Juniper QFX5120. Support is patchy: QFX5120 and IOS XE expose DDM only; NX-OS reads CMIS VDM but assumes a 50°C laser target. Includes power-trend data (400G FR4: 12W→9W; 800G OSFP: 16.5→15.5W; 1.6T: 30→26W as DSP nodes shrink) and an entertaining frozen-transceiver experiment showing the laser re-warms within seconds.
- **Where applicable**: Broadly applicable to optics power budgeting; requires CMIS/VDM-capable transceivers and switch support, so check your NOS before counting on it. Vendor talk, but methodology is transferable.

### VXLAN and EVPN on Linux (with BIRD)

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/59/7JB8K9/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/7JB8K9/resources/evpn-vxlan-tutorial_WTl2IbG.pdf) · [Recording](https://ripe92.ripe.net/media/videos/maria-matejka_vxlan-and-evpn-on-linux-with-bird_main_20260518-090103.mp4)

Maria Matejka, BIRD | CZ.NIC

- **Why**: DC fabric fundamentals — VXLAN and EVPN — taught from raw Linux primitives upward, using the open-source daemon the speaker's team actually implements EVPN in, rather than a commercial stack.
- **What**: A hands-on tutorial building VXLAN tunnels manually (`ip link add ... type vxlan`, VNI, UDP 4789), VLAN-filtering bridges, and hypervisor L2 domains, then layering EVPN control-plane on top with BIRD, so attendees understand what actually happens under the hood before the abstractions arrive.
- **How**: Labs run in EduHawk (CZ.NIC's container-based network simulator, user namespaces, no root needed), starting with veths and bridges, moving to manual VXLAN links for VM mobility and traffic isolation, and progressively adding scalability layers. The setup is keepable for future fiddling.
- **Where applicable**: Anyone building or operating DC overlay fabrics on Linux/commodity hardware, or anyone who wants to debug EVPN/VXLAN rather than just configure it. Tutorial format — worth the recording if you missed it live.

### Manipulating RPKI (and more) with marquees in TLS certificates (and more)

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/65/YHQY7N/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/YHQY7N/resources/Manipulating_RPKI___1zypS0J.pdf) · [Recording](https://ripe92.ripe.net/media/videos/sasha-romijn_manipulating-rpki-and-more-with-marquees-in-tls-certificates-and-more_main_20260518-143021.mp4)

Sasha Romijn, Reliably Coded (IRRD, IRRexplorer, internet.nl)

- **Why**: A year-long, systematic XSS campaign against the tooling layer around routing infrastructure — culminating in a chain that modifies RPKI ROAs from a single clicked link. Directly relevant to network security and to anyone building tools that render protocol-derived strings.
- **What**: The author injected marquee/XSS payloads into every protocol field he controls — TLS certificate SANs, DNS version.bind/NSID/TXT, RIPE Database objects, HTTP Server headers, DHCP hostnames, wifi SSIDs, LoRa node names — and catalogued where downstream tools execute them. Findings span two RIRs, hosting providers (WHMCS on the main domain → one click adds an admin to a customer account), router firmware, and wirelessly rootable OpenWRT boxes. Most seriously: multiple paths through the RIPE NCC single sign-on session mean one click on a real ripe.net link can silently change your ROAs and take over your Database objects — you'd only notice when packets start dropping.
- **How**: The recurring pattern: tools treat protocol fields as safe data, and some of those tools share a trust boundary with critical systems. The punchline: "RPKI has HSMs and key ceremonies, but the thing that actually changes your ROAs is a web app authenticated by a cookie."
- **Where applicable**: Universal for anyone operating RPKI/IRR portals or writing tooling that displays untrusted fields; concrete guidance on what to watch for in your own tools.

### OpenPenny: Identifying Legitimate Traﬃc to Reduce Monitoring Noise

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/74/UWTWQR/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/UWTWQR/resources/openpenny-slides-rip_N1gyaTN.pdf) · [Recording](https://ripe92.ripe.net/media/videos/petros-gigis_openpenny-identifying-legitimate-traffic-to-reduce-monitoring-noise_main_20260519-113501.mp4)

Petros Gigis, UCL

- **Why**: Fills a real gap in ISP observability: packet counters and control-plane data can't tell you whether observed traffic is genuine or spoofed — which makes routing-change alerts noisy and stealthy hijacks hard to confirm.
- **What**: An open-source data-plane primitive that validates whether traffic aggregates are non-spoofed, enabling trustworthy ingress maps, fewer false routing alerts, and detection of data-plane path anomalies invisible to BGP monitoring alone (including ROV-bypassing "stealthy hijacks" where the only visible signal is an unexpected ingress point).
- **How**: Exploits a structural difference between real and spoofed TCP: legitimate connections are closed-loop (loss triggers retransmission), spoofed traffic is open-loop and cannot react. Active mode carefully drops a few packets and watches for retransmission; passive mode collects signals (e.g., per-packet load-balancing behavior) without touching traffic. Runs on commodity x86 using XDP/AF_XDP and DPDK; demonstrated on a real UCL testbed.
- **Where applicable**: ISPs and large network operators with sFlow/NetFlow telemetry; the active mode injects small, deliberate loss, so it suits telemetry/monitoring paths rather than every production link. Solidly in the eBPF/XDP space the PM tracks.

### Measuring The Impact of Post-Quantum Cryptography on Complex Applications: A Case Study on Federated Identity Management

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/112/3XVHEJ/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/3XVHEJ/resources/RIPE_92_-_FIdM_PQC-2_q0fHRKb.pdf) · [Recording](https://ripe92.ripe.net/media/videos/ginevra-fabrizio_measuring-the-impact-of-post-quantum-cryptography-on-complex-applications-a-cas_main_20260522-110043.mp4)

Ginevra Fabrizio, University of Twente

- **Why**: One of the few PQC-migration studies grounded in a real, complex identity stack (SAML + OIDC hub-and-spoke federation) rather than isolated TLS benchmarks — directly relevant to the identity side of the PM's portfolio.
- **What**: Benchmarks of the five NIST-finalized PQC algorithms against real-world load from SURF's SURFconext federation (25 days of data: authentication counts, HAProxy logs, TLS connection info, SAML request/response volumes), quantifying the computational and hardware-capacity toll of switching a production federated identity hub to PQC.
- **How**: The Hub'n'Spoke model is the worst case: the central hub (SURF.Engine) performs most cryptographic operations — each SAML flow involves validating the home IdP's response signature and signing a new response for the SP, and equivalents exist in the OIDC flow. Real authentication flows run from one second to several minutes, so added per-operation cost compounds visibly.
- **Where applicable**: Identity federation operators and anyone planning PQC migration of OAuth/OIDC/SAML infrastructure. Findings: the transition is fragmented, with many ecosystem components still unaccounted for. Specific to hub-and-spoke scale but the methodology transfers.

### Persistent unknown unicast - A peering-LAN case study

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/84/YZVWHG/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/YZVWHG/resources/ripe92-persistent-un_bP27w0R.pdf) · [Recording](https://ripe92.ripe.net/media/videos/james-rice_persistent-unknown-unicast-a-peering-lan-case-study_main_20260520-093506.mp4)

James Rice, Jump Networks Ltd

- **Why**: A textbook-quality L2 postmortem: a single MAC change can flood member traffic (including HTTPS SNI and emergency-call signalling) to hundreds of ports *indefinitely*, via a kernel-level neighbor-discovery quirk. This is the kind of hard-won operational lesson that transfers to any shared L2.
- **What**: Shows that unknown unicast on peering LANs is not always transient. RFC 4861 §7.3.1 "forward-progress confirmation" lets a stale ND entry stay REACHABLE indefinitely: when member B changes MAC, A keeps sending to the old MAC; the exchange floods those frames to all member ports; some members' devices (skipping the L2 my-station check) forward the packet onward to B; B's reply via that third-party path counts as forward progress, so no Neighbor Solicitation is ever sent. A unicast NS to the stale MAC gets flooded too, and the NA arriving from the *new* MAC without a TLLA option confirms reachability without updating the cached MAC (RFC 4861 §7.2.5) — the entry stays stale and REACHABLE.
- **How**: Kernel-level trace through `neigh_confirm()`/`neigh_timer_handler()` and `ndisc_recv_na()`/`neigh_update()`; a reproducible demo (published Nov 2024) using `ip neigh replace` with a dead MAC produces duplicate ping replies — each duplicate being a different member's device routing a packet it had no business handling. Includes a five-year timeline of reports and partial remediations at one IXP, plus a frank operator self-examination about disclosure.
- **Where applicable**: The five-year timeline is one-IXP-specific, but the mechanism is general to any Linux/BSD host on a shared L2 segment — DC fabrics, exchange LANs, any environment where MAC changes meet ND caches. Valuable for L2 design and failure-mode reasoning.

### Route Filtering at Scale

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/67/EDRJ39/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/EDRJ39/resources/RIPE_92_Route_Filter_Jl2GqKT.pdf) · [Recording](https://ripe92.ripe.net/media/videos/fedor-vompe_route-filtering-at-scale_main_20260518-163214.mp4)

Fedor Vompe, Deutsche Telekom; Sebastian Becker, Deutsche Telekom

- **Why**: Concrete, adoptable tooling for one of the hardest operational BGP problems — generating correct filters for thousands of sessions when the underlying IRR data is rotten. Up-ranks well on the "tooling others can adopt" criterion.
- **What**: A tier-1's (AS3320) account of why AS-Set documentation in RIR databases remains foundational and systematically overlooked: missing documentation, explosive AS-Set expansion, and cyclic dependencies all break filter generation, and RPKI ROV alone does not replace this layer — bogon filters, community policy, Peerlock, IRR filters, ROV, ASPA, and OTC all work together.
- **How**: Presents their toolchain, including the Route Query Specification (RQSpec) language and RIPEDiff, which compensate for poor AS-Set quality. Key framing: AS-Sets are fail-closed, so their contents and changes should be monitored — adding/removing a member set silently changes every parent set. Includes a worked route-leak prevention example (AS3320 requiring a customer's `AS-DOWNSTREAM` set before accepting prefixes).
- **Where applicable**: Large operators generating customer/peer filters from IRR; the AS-Set hygiene findings apply to anyone consuming IRR data at any scale. Deutsche Telekom's toolchain specifics are theirs, but RQSpec is worth a look.

## Adjacent

### Redefining Netflix BGP architecture

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/74/RKCTUA/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/RKCTUA/resources/Redefining_Netflix_B_2YNNG4M.pdf) · [Recording](https://ripe92.ripe.net/media/videos/elise-vennegues_redefining-netflix-bgp-architecture_main_20260519-115725.mp4)

Elise Vennegues, Netflix; Frederic Cuiller, Cisco

- **Why**: Real BGP architecture evolution at serious scale (20,000+ eBGP sessions, 2800+ peer ASNs, 400+ PoPs, ~175 countries) — the RR design questions and migration choreography are transferable even if the chosen platform is not.
- **What**: Netflix's replacement of a full iBGP mesh across edge switches, aggregation routers, and PEs with a route-reflector architecture, including the option analysis (traditional router vs VNF appliance vs integrated UCS M7 appliance), production scale figures (e.g., NA region: 38M IPv4 / 9M IPv6 paths, 300+ clients), a phased migration (staging → pilot prefixes → per-device deprefer/raise → remove the mesh), and OpenConfig YANG-based BGP telemetry with BMP activation planned.
- **How**: Validation via an early-field-trial process with Cisco; lessons include: cross-functional projects take longer than planned, and the lab is necessary but production churn/scale is unique.
- **Where applicable**: Any large edge network with full-mesh iBGP pain. Caveat: this is an openly joint Netflix–Cisco presentation and the IOS XRv9000 UCS M7 appliance gets prominent placement — treat the product comparison table as vendor-tinged and extract the architecture methodology.

### RPKI: Do we need Garbage Collection now?

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/74/HD3MND/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/HD3MND/resources/rpki-gc-merge-emoji_FTR8fda.pdf) · [Recording](https://ripe92.ripe.net/media/videos/antonios-chariton_rpki-do-we-need-garbage-collection-now_main_20260519-110128.mp4)

Antonis Chariton, AS4601 | Cisco

- **Why**: Quantifies a genuine routing-security hygiene problem: newly assigned ASNs arriving with pre-existing ROAs that make their holders' hijacks look RPKI-valid.
- **What**: Methodology-driven measurement: cross-referenced all RIPE ASN assignment dates against RPKI archives (RPKIviews) for ROAs pointing at each ASN the day before assignment — any such ROA is definitionally unintentional. Result: ~21% of new assignments in 2025 (18% in 2026) came with pre-existing ROAs, including double-digit-percentage chances of IPv4-covering ROAs; examples found in every RIR except AFRINIC. The RIPE NCC's re-assignment cleanup covers IRR but not RPKI.
- **How**: A personal anecdote (a fresh ASN with ROAs authorizing other people's IPv4) turned into a systematic study; the follow-up Address Policy WG session ("Discussion on AS Reallocation") explores fixes: longer quarantine periods, alerting on RPKI objects pointing at unassigned ASes, expanding cleanup policy.
- **Where applicable**: Anyone relying on RPKI ROV for security decisions; the data is RIPE-region-centric but the problem class exists in all RIRs.

### Why is ASPA still a draft

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/65/TDYAZY/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/TDYAZY/resources/why-is-aspa-still-a-_7WvkFjh.pdf) · [Recording](https://ripe92.ripe.net/media/videos/maria-matejka_why-is-aspa-still-a-draft_main_20260518-150332.mp4)

Maria Matejka, BIRD | CZ.NIC

- **Why**: An implementer's-eye view of why ASPA (AS Provider Authorization) keeps stalling — useful both for BGP protocol understanding and as a case study in how draft specs mislead even careful implementers.
- **What**: Clarifies what ASPA is and isn't ("ROA for the rest of the AS path": each AS signs its provider list — not whole-path authorization, not neighbor-pair authorization, not a BGPsec replacement), then walks through BIRD's implementation history: their first validation algorithm was *wrong* (assuming neighbor-pair authorization), and the wrongness survived review because the draft text suggested that reading on first pass.
- **How**: Details the RTR ASPA PDU design confusion (a redundant AS Count field questioned after the document had passed last call) and a 2024 clarification exchange that exposed deeper ambiguity in the validation algorithm.
- **Where applicable**: Anyone implementing or planning to deploy ASPA; also a good cautionary tale for anyone writing specs that will be implemented by third parties.

### DNS, Transitive Trust and How Many is Many

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/98/ATVK7Z/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/ATVK7Z/resources/DNS_Transitive_Trus_2ntoCpt.pdf) · [Recording](https://ripe92.ripe.net/media/videos/ondrej-sury_dns-transitive-trust-and-how-many-is-many_side_20260521-110213.mp4)

Ondřej Surý, ISC

- **Why**: A genuinely surprising measurement: resolving `teams.microsoft.com` on a cold cache triggers **247** outgoing queries from a single recursive resolver — with real implications for latency, load, and the transitive trust surface CDNs are building.
- **What**: A cold-cache tour through delegation types: in-domain delegations are cheap (glue mandatory, no extra cost), in-bailiwick adds 0–N×2 queries, and out-of-bailiwick delegations force the resolver to resolve each NS name from scratch — 3 + 3×N queries per name. CNAME chains make this multiplicative, not additive: each target zone may be out-of-bailiwick and each NS-set spans TLDs.
- **How**: All numbers from BIND 9, adding one complexity source at a time; notably, resolver software matters enormously — the same name cost 168 queries on BIND 9.11 but only 16 on 9.21. DNSSEC and the often-forgotten PTR case add more.
- **Where applicable**: Resolver operators, CDN/zone architects thinking about delegation hygiene, and anyone debugging cold-cache latency spikes.

### Overdoing NSEC3 Hurts

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/98/HW3LJG/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/HW3LJG/resources/presentation_dzewVOT.pdf) · [Recording](https://ripe92.ripe.net/media/videos/petr-spacek_overdoing-nsec3-hurts_side_20260521-120328.mp4)

Petr Špaček, Internet Systems Consortium

- **Why**: A crisp security nugget: NSEC3 iteration counts that operators set for "extra security" are actually a DoS amplifier and enable a poorly documented downgrade attack.
- **What**: Measured cost of extra iterations under random-subdomain attacks: ~1/3 performance loss at 5 iterations, ~2/3 at 25, across NSD, Unbound, and BIND. Worse, when iterations exceed a resolver's limit, the answer *may* be treated as insecure — and an attacker who controls any over-limit NSEC3 zone can craft a fake delegation that makes a delegation validate as insecure.
- **How**: Walks through the iteration-limit collapse over time (2500 in RFC 5155 → 150 in implementations → 0 per RFC 9276 → 50 in BIND 9.19.18 → ~20 next), then the downgrade mechanics using real records.
- **Where applicable**: Every DNSSEC-signed zone operator. Advice: use NSEC if you can, otherwise follow RFC 9276 exactly (0 iterations, no salt, no opt-out).

### The €30 attack box: inside the Android TV botnet ecosystem

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/79/7AETZG/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/7AETZG/resources/RIPE_92_-_Nokia_Deep_T2jCpjR.pdf) · [Recording](https://ripe92.ripe.net/media/videos/jerome-meyer_the-30-attack-box-inside-the-android-tv-botnet-ecosystem_side_20260519-164530.mp4)

Jérôme Meyer, Nokia

- **Why**: Documents a step-change in the DDoS and abuse landscape — botnets no longer scan for exposed IoT; they recruit via residential proxy SDKs pre-installed on consumer hardware, behind CGNAT, invisible to conventional scanning.
- **What**: Nokia Deepfield's analysis of the Oct 2025 33 Tbps attack and the ecosystem behind it: budget Android TV boxes ship with proxy software that routes requests to 0.0.0.0 — which resolves to the device's own loopback, where an unauthenticated ADB shell listens. No scanning, no CVE; the proxy SDK delivers the victim. Kimwolf alone runs ~3M active bots with ENS-based C2; the exploitable surface is estimated at 100–200M endpoints.
- **How**: Linking six botnet families via shared code, a common cryptographic fingerprint (RC4+LCG, fixed seed), and co-located infrastructure; notable capabilities include Katana compiling its rootkit on-device via a bundled C compiler and CECbot abusing HDMI-CEC to survive factory resets. Operator-facing impact: outbound attack traffic from your own subscribers causes CGNAT failures and peering congestion; C2 signals to monitor are provided.
- **Where applicable**: Any access network operator (CGNAT/peering impact), and security teams tracking proxy/botnet infrastructure. Nokia-authored but built on original lab analysis and reverse engineering.

### Detecting and Characterizing DDoS Scrubbing from Global BGP Routing: Insights from Five Leading Scrubbers

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/78/QKVKRR/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe-92/submissions/QKVKRR/resources/Detecting-scrubbing-_x1a5m3Q.pdf) · [Slides (PPTX)](https://pretalx.ripe.net/media/ripe-92/submissions/QKVKRR/resources/Detecting-scrubbing_PF3bIfl.pptx) · [Recording](https://ripe92.ripe.net/media/videos/shyam-krishna-khadka_detecting-and-characterizing-ddos-scrubbing-from-global-bgp-routing-insights_main_20260519-170727.mp4)

Shyam Krishna Khadka, University of Twente

- **Why**: Helps solve a practical monitoring problem: BGP path changes caused by DDoS scrubbing look like hijacks or leaks in your alerting, and 48% of scrubber-originated prefixes aren't properly covered by ROAs.
- **What**: A PAM 2026 paper detecting scrubbing activations/deactivations purely from public RIS BGP data (30 days, five scrubbers: Cloudflare, Akamai Prolexic, Vercara, Imperva, Radware). Always-on protection dominates (11k prefixes vs 5.6k on-demand); on-demand scrubbing splits into upstream-change (dominant) and origin-change modes.
- **How**: Inference requires at least two route-collector peers observing the AS-path change; characterization covers protection modes, session durations (median ~10h45m; 25% under 1h45m), and RPKI/IRR practice — finding 12.5% Invalid and 35.5% NotFound among temporarily-originated prefixes.
- **Where applicable**: BGP monitoring/anomaly-detection toolbuilders, and scrubbing customers who should fix their ROA coverage before an attack makes their scrubber originate their prefixes.

### The year of IPv6-only desktop

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/94/PBHCLK/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/PBHCLK/resources/RIPE_92_-_The_year_o_djkzlI7.pdf) · [Recording](https://ripe92.ripe.net/media/videos/ondrej-caletka_the-year-of-ipv6-only-desktop_main_20260521-090610.mp4)

Ondřej Caletka, RIPE NCC

- **Why**: Marks the moment IPv6-only operation crosses from mobile networks to desktops — macOS already opts out of IPv4 on IPv6-mostly networks, Windows 11 has it in preview, and NetworkManager on Linux supports it.
- **What**: The "IPv6-mostly" model: the network signals NAT64 support via DHCPv4 option 108, and devices with CLAT (or enforced IPv6 compatibility) autonomously opt out of IPv4. Framed by the RIPE meeting network's own decade-long journey (failed experiment in 2013 → working IPv6-mostly main network today), and the argument that dual stack failed as a transition mechanism: double the work, with IPv6 problems masked by the IPv4 safety net.
- **How**: NAT64 won because it's the one-box solution the industry actually chose; CLAT handles IPv4-only applications on the client. Practical pitfalls called out: IPv4-only VPNs with IPv6 killswitch features, and devices opting out even when they shouldn't.
- **Where applicable**: Enterprise/access network design; the WinCLAT arrival makes IPv6-only enterprise LANs genuinely deployable, which will change DC and edge design assumptions.

## Wildcard

### How much of BIRD is vibecoded

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/85/ANS3JF/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/ANS3JF/resources/vibecoding-bird_zChFz02.pdf) · [Recording](https://ripe92.ripe.net/media/videos/maria-matejka_how-much-of-bird-is-vibecoded_side_20260520-100918.mp4)

Maria Matejka, BIRD | CZ.NIC

- **Why**: Not a talk the PM would search for, but one of the more honest datasets available on what LLMs can and cannot do in core network software — from the maintainers of a production routing daemon.
- **What**: The answer to "how much of BIRD is vibecoded" is essentially: none of the hard parts. LLM-generated lockless multithreaded C was "pathetic." Attempts to use AI for bug fixing failed ("most of our bugs need complex thinking"), as did texts about BIRD, release notes, slide generation, and RFC review.
- **How**: Beyond the failures, it catalogs the social pressures arriving via LLM: survivor bias (nobody posts their failures), confirmation bias ("the code should do what the commit declares"), "it works, just merge it" pressure, and the emerging phenomenon of LLM-fortified forks of real projects. The uncomfortable conclusion: BIRD's problem isn't AI — it's that their documentation "sucks or is outright wrong," their future intents aren't written anywhere, and background is scattered; that's bad for humans and LLMs alike.
- **Where applicable**: Anyone maintaining open-source network infrastructure, or thinking about where AI-assisted development can safely enter their toolchain. Read alongside "Brace for Upgrades" (same conference) for the flip side — LLM-equipped security researchers flooding projects with CVE reports (~5–8% validity rates).

### BitSquatting... ...or the infinite monkeys theorem...

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/112/MFPHZ7/) · [Slides](https://pretalx.ripe.net/media/ripe-92/submissions/MFPHZ7/resources/bitsquatting-2026-ri_HV5VAoi.pdf) · [Recording](https://ripe92.ripe.net/media/videos/warren-kumari_bitsquatting-or-the-infinite-monkeys-theorem_main_20260522-113721.mp4)

Warren Kumari, Google LLC

- **Why**: A weird, memorable, and real attack class: hardware bit-flips during DNS resolution silently redirect traffic to attacker domains one binary bit away — with live capture data showing what actually leaks.
- **What**: An update on 2011-era bitsquatting research: register domains one bit-flip away from popular names (microsont.com, googneapis.com, cxase.com...) and collect the traffic that hardware errors (cosmic rays, contaminated ceramics — the talk traces this back to 1970s DRAM and cites Qantas Flight 72) accidentally send you.
- **How**: A ~1-month capture across registered variants gathered ~54,000 requests, including expanded hostnames (msdn.microsont.com), SNI of legitimate domains, cookies, OAuth-style login URLs, executables, and JavaScript — each request proving a memory error happened somewhere and leaking what the affected host was doing.
- **Where applicable**: Mostly relevant as threat-model awareness for security teams and a reminder that DNS is a hardware-reliability observation channel; the "register typos-at-the-bit-level" strategy is trivially cheap for attackers and nearly impossible to fully defend.

### IP Address space for Outer Space

**Links:** [Abstract](https://ripe92.ripe.net/programme/meeting-plan/sessions/97/RHW7DB/) · [Slides (PDF)](https://pretalx.ripe.net/media/ripe-92/submissions/RHW7DB/resources/RIPE_address_space.k_740WWva.pdf) · [Slides (Keynote)](https://pretalx.ripe.net/media/ripe-92/submissions/RHW7DB/resources/RIPE_address_space_FWRbbyo.key) · [Recording](https://ripe92.ripe.net/media/videos/tony-li_ip-address-space-for-outer-space_main_20260521-120023.mp4)

Tony Li

- **Why**: A genuinely novel addressing-policy question: there is no RIR for outer space, and the current ad-hoc practice (space agencies getting resources from their local, geography-based RIR) precludes aggregation on extremely bandwidth-constrained links.
- **What**: The IETF TIPTOP working group's proposal (draft-li-tiptop-address-space) for one RIR and one address block covering all of outer space, with one prefix each for the Moon, each planet, Lagrange points, and possibly the asteroid belt.
- **How**: The argument is aggregation economics: space links are modem-class and mission-critical, so per-planet prefixes minimize precious routing overhead; space agencies are generally cooperative (ISS precedent) and expected to interconnect in space. Notably IPv4-first pragmatism — IPv6 header overhead is a serious concern on these links, and a reclaimed /16 might suffice alongside the IPv6 block.
- **Where applicable**: Niche today, but it's a real IETF work item with ARIN in discussion for the custodian role, and an early signal of how Internet architecture extends into non-terrestrial networks.

## Themes

- **IP/optical integration is now an operator skill requirement**: Meta's ZR rack-count math, Channelmania's coherent DWDM primer for IP folks, and transceiver VDM/TEC power telemetry all point the same direction — the transponder layer is collapsing into pluggables, and DC/WAN network engineers need coherent-optics literacy to plan capacity, power, and fiber.
- **AI traffic is reshaping both fabrics and threat models**: Meta is building an AI backbone with 10,000s of 800G ZR links and pushing GPU compute to the edge, while on the security side AI companies have become the largest funders of residential proxy networks that feed 100M+ endpoint botnets — the same technology trend shows up as both a capacity driver and an attack-surface driver.
- **Routing security is operationalizing, and finding its rough edges**: ASPA deployment friction (wrong implementations, draft ambiguities), RPKI "garbage" from AS recycling, stale-ROA hijack risk, IRR/AS-Set hygiene, and — strikingly — the discovery that the security of the routing control plane ultimately rests on web apps and SSO cookies vulnerable to XSS.
- **Data-plane validation as a new observability primitive**: OpenPenny's closed-loop TCP test, BGP-inferred DDoS scrubbing detection, and SRA-based IPv6 scanning all attack the same problem — distinguishing genuine traffic and legitimate topology changes from noise, spoofing, and misconfiguration.
- **IPv6-only is finally crossing to the desktop/enterprise**: IPv6-mostly with DHCPv4 option 108 and CLAT (now including Windows) plus the 3901bis BCP for IPv6 in the DNS mark real movement after a decade of dual-stack stagnation.
- **LLMs are arriving on both sides of network software**: AI-assisted development in core routing daemons (with documented failures in hard systems code), LLM-driven CVE discovery forcing unsustainable upgrade cadences on open-source projects, and the first Practical AI BoF for ISP operations — worth tracking even at this early, mostly-hype-adjacent stage.
