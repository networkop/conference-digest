<!--
conference: SREcon25 Americas
type: operator
source_url: https://www.usenix.org/conference/srecon25americas/program
generated: 2026-08-30
registry_key: srecon-2025-americas
-->

# SREcon25 Americas — Digest

Program source is the expanded schedule (titles, speakers, and abstracts; no PDF/slide/recording links were present in the pasted program text, so no Links field is included below — every write-up is grounded in the abstract only). This cycle's program skews heavily toward observability tooling, incident-response process, and organizational/human-factors content, plus a large AI/ML-infrastructure-operations cluster (safe model rollout, ML training governance, AI-assisted ops) — none of which is core to the PM's stated interests. The pick count below is intentionally small: it reflects genuinely thin coverage of DC/WAN networking, cloud-native networking, network security, and identity this cycle, not aggressive filtering of a networking-heavy program.

## Core

### Improving the SRE Experience for 10 Years as a Free, Open, and Automated Certificate Authority

*Matthew McPherrin, Internet Security Research Group (Opening Plenary)* — **Core**

- **Why**: A decade of operational history from the team running Let's Encrypt — now securing 500M+ websites — on what it actually takes to run free, automated PKI issuance reliably at Internet scale, plus a preview of upcoming changes to the ecosystem every TLS operator depends on.
- **What**: A retrospective on ten years of Let's Encrypt's certificate authority and Certificate Transparency log operations, covering lessons for anyone managing TLS certificates and guidance on upcoming changes to the CA. (from abstract only)
- **How**: Not detailed mechanically in the abstract; framed as historical/operational context plus forward guidance rather than a single technique. (from abstract only — thin on mechanism)
- **Where applicable**: General; directly relevant to the same certificate-lifecycle/crypto-agility theme surfaced in the Netflix Enigma talk at USENIX Security '25 this cycle (see that digest) — shortening cert lifetimes make automated issuance like Let's Encrypt's the operational baseline, not an option.

### Please Give Me Back My Network Cables! On Networking Limits in AWS

*Steffen Gebert and Miklos Tirpak, emnify* — **Core**

- **Why**: A specific, hard-won account of where "the cloud network" abstraction breaks down — running a mobile core network's packet-processing functions on EC2 and hitting undocumented and semi-documented AWS networking limits (packets-per-second, connection tracking) directly relevant to anyone building network-function or high-PPS workloads on public cloud.
- **What**: A catalog of AWS EC2 networking limits (bandwidth caps, packet-per-second ceilings, connection tracking limits) discovered the hard way while running a mobile virtual network operator's custom mobile core network functions on AWS, including which limits are documented versus not, and how to monitor remaining quota. (from abstract only)
- **How**: Explains how limits like PPS and connection tracking affect network traffic once exceeded, and diagnostic approaches for identifying when an incident is actually an undocumented cloud networking-limit rather than an application bug. (from abstract only)
- **Where applicable**: Network-function/packet-processing workloads on AWS EC2 specifically; the underlying lesson (cloud "unlimited" networking has real, sometimes-undocumented ceilings) generalizes to any high-PPS or connection-dense workload on public cloud.

### Securing Distributed Cache: Achieving Secure-by-Default with Key Challenges & Insights

*Akashdeep Goel, Sriram Rangarajan, and Samuel Fu, Netflix* — **Core**

- **Why**: A concrete account of retrofitting security (cert lifecycle management, secured proxy calls for polyglot clients) onto an already-massive production system — 400M requests/sec, 14PB of data — rather than designing it in from day one, which is the situation most real security-hardening projects actually face.
- **What**: How Netflix secured its multi-region distributed caching system (used for both streaming and gaming workloads) after the fact, covering certificate lifecycle management, eliminating spurious policy lookup calls, and securing proxy calls across clients written in different languages. (from abstract only)
- **How**: Debugged and validated using CPU profiling and memory dumps to find the performance/correctness cost of retrofitted security controls, then executed a global-scale rollout. (from abstract only)
- **Where applicable**: General for retrofitting security/mTLS-style controls onto an existing high-throughput distributed system; the polyglot-client proxy-securing pattern is broadly applicable beyond caching specifically.

### Network Flow Data in the Cloud

*Steve Dodd, Slack* — **Core**

- **Why**: An argument that classical network-engineering techniques (graph theory, the discrete math underlying traditional routing/traffic-engineering work) are directly applicable to modern cloud service-oriented architecture — and a concrete method for per-service traffic attribution without paying for vendor flow-logging products.
- **What**: A framework for building per-service network traffic attribution in cloud infrastructure using network-graph analysis techniques borrowed from traditional network engineering (the kind of work "manual OSPF metric tuning" represents), without relying on expensive vendor logging solutions. (from abstract only)
- **How**: Applies graph-theoretic analysis of network topology/flow to optimize data flow, routing, and resilience visibility at the service level — essentially traffic engineering applied to service-mesh-era cloud infrastructure. (from abstract only)
- **Where applicable**: General for large-scale cloud service infrastructure wanting traffic/dependency visibility; the technique is explicitly framed as reviving under-used traditional networking analysis for cloud-native environments.

### Chaos Experiments - Datacenter Stress Testing

*Clayton Krueger, USAA* — **Core**

- **Why**: Most chaos-engineering practice targets individual applications or services; this is chaos testing applied to an entire datacenter as the blast-radius unit, which is a meaningfully different (and harder) failure-domain scope directly relevant to physical DC operations.
- **What**: An account of building a comprehensive, automated, leadership-backed chaos engineering program at a financial services provider, elevated from individual-application testing to whole-datacenter stress testing. (from abstract only)
- **How**: Not detailed mechanically in the abstract; framed around the organizational and technical stages of scaling chaos testing to datacenter scope, including overcoming fear/uncertainty/doubt as an adoption barrier. (from abstract only — thin on mechanism)
- **Where applicable**: General for organizations with the operational maturity to test at datacenter-wide blast radius; financial-services-specific framing but the scaling journey generalizes.

## Adjacent

### Handling the Largest Domains Migration, Ever!

*Franklin Angulo and Divya Kamat, Squarespace* — **Adjacent**

- **Why**: A concrete account of migrating 10M+ domains (the assets behind Google Domains, acquired by Squarespace in 2023) at a scale not previously seen in the domain-registrar industry — a rare data point on DNS/registrar infrastructure operations at extreme scale.
- **What**: The challenges of executing a domain-registrar migration involving more than 10 million domains following Squarespace's acquisition of the Google Domains business. (from abstract only)
- **How**: Not detailed mechanically in the abstract. (from abstract only — thin on mechanism)
- **Where applicable**: Domain registrar/registry operations specifically; general lessons on very-large-scale record migration likely apply more broadly.

### Taming the Beast: Understanding and Harnessing the Power of HTTP Proxies

*Guillaume Quintard, Varnish Software* — **Adjacent**

- **Why**: A practitioner deep-dive on reverse proxies as active operational tooling (debugging, traffic manipulation, incident mitigation) rather than passive infrastructure — relevant datapath/operational context for anyone running proxy-fronted services.
- **What**: How reverse proxies enhance observability, performance, and resilience in modern SRE/DevOps workflows, with a focus on using proxies as active tools during production incidents rather than just static traffic routers. (from abstract only)
- **How**: Combines HTTP fundamentals with reverse-proxy traffic manipulation techniques and OpenTelemetry integration for debugging and active mitigation. (from abstract only)
- **Where applicable**: General for any proxy-fronted (Varnish, Envoy, nginx-class) service architecture.

### Hijacking Service Discovery to Simulate Dependency Degradation

*Abdulrahman Alhamali, Shopify* — **Adjacent**

- **Why**: A cleaner alternative to proxy-based dependency-degradation simulation (circuit breaking, bulkheading, graceful degradation testing) — directly relevant to anyone testing resilience patterns in a service-mesh or service-discovery-based architecture.
- **What**: Techniques for simulating dependency degradation (slowdowns, bandwidth limits, outages) by hijacking service discovery rather than requiring all traffic to route through a dedicated simulation proxy. (from abstract only)
- **How**: Streamlines traffic-forwarding for degradation simulation by manipulating what service discovery returns, avoiding the overhead of a full proxy-based simulation layer. (from abstract only)
- **Where applicable**: General for service-discovery-based architectures (Kubernetes, service mesh, or custom) wanting to test resiliency mechanisms without waiting for a real incident.

### Maturing Your Data Architecture in a Week: How Bluesky Survived

*Jaz Volpert, Bluesky PBC* — **Adjacent**

- **Why**: A real account of a small team (~6 engineers) rapidly scaling physical infrastructure under a genuine viral-growth event (1,200% DAU increase in a week) — notable specifically because Bluesky runs its own physical infrastructure rather than purely cloud-native services.
- **What**: How Bluesky's backend team matured its data architecture in 11 days of intense effort to handle a surge to 1M+ new users/day and 1,600+ events/sec, while running core infrastructure on owned physical hardware. (from abstract only)
- **How**: Not detailed mechanically in the abstract beyond "rapidly matured data architecture." (from abstract only — thin on mechanism)
- **Where applicable**: Physical/self-hosted infrastructure under sudden extreme load; a useful contrast case to cloud-elastic scaling stories since Bluesky couldn't simply autoscale.

### Is the S in SRE for "Security"?

*John Benninghoff, Security Differently* — **Adjacent**

- **Why**: A structured argument for the operational and organizational overlap between SRE and security practice (patching/attack-surface management, observability, incident response, postmortems) — useful framing for anyone trying to align SRE and security teams.
- **What**: An argument that SRE and Security teams share enough operational DNA (attack-surface management, observability, incident response, testing) that organizations most effectively reduce cybersecurity risk by improving general technology/operational performance rather than treating security as a separate discipline. (from abstract only)
- **How**: Draws on safety-science and DevOps research linking organizational performance across development, operations, SRE, and security; proposes Security Level Objectives as an SLO-style mechanism for prioritizing security work. (from abstract only)
- **Where applicable**: General organizational-design question for any org with separate SRE and security functions.

### Lies Programmers Believe About Memory

*Chris Down, Meta (Linux kernel memory management maintainer)* — **Adjacent**

- **Why**: A from-the-source explanation of Linux kernel memory internals (TLBs, page tables, cgroup memory classes) from an actual kernel memory-management maintainer — low-level systems knowledge that underlies performance/reliability work on any Linux-hosted infrastructure, DC or cloud.
- **What**: A tour of kernel memory management internals — CPU memory hardware abstractions (TLBs, page tables) and Linux's own internal memory classes and their often-misunderstood properties — aimed at helping SREs reason correctly about application memory behavior. (from abstract only)
- **How**: Explains the actual mechanics of virtual memory, page tables, and cgroup-based memory accounting rather than treating them as opaque abstractions. (from abstract only)
- **Where applicable**: General for anyone debugging memory-related performance or reliability issues on Linux, DC or cloud; particularly relevant to cgroups-based container/Kubernetes memory limits.

## Wildcard

### AIOps: Prove It! An Open Letter to Vendors Selling AI for SREs

*Charity Majors and Fred Hebert, Honeycomb.io (Closing Plenary)* — **Wildcard**

- **Why**: Not a networking or identity talk, but a pointed, credible-source (Honeycomb's own co-founder) counter-narrative to the AI-for-ops hype dominating this cycle's program by sheer volume — worth having as a calibration point against the many AI/ML-infra-ops talks elsewhere in the schedule.
- **What**: A critical framework for evaluating vendor claims about AI-powered SRE/ops tooling, arguing that skeptical operators need to engage with genAI rather than dismiss it, while vendors need to demonstrate good-faith engagement with real SRE problems rather than hype. (from abstract only)
- **How**: Not a technical mechanism talk — an argued position piece from two well-known observability practitioners. (from abstract only)
- **Where applicable**: General; useful as a lens for evaluating any AIOps/AI-for-reliability vendor pitch.

### Systems Thinking with Poisoned Systems

*Hazel Weakly, Nivenly Foundation; Sandeep Kanabar, Gen* — **Wildcard**

- **Why**: An unusual framing — applying "garbage in, garbage out" and data-poisoning concepts not to ML training data but to the practice of operating carefully-tuned production systems with AI assistance layered on top — a genuinely different angle on AI-ops risk than the typical "AI will help SREs" pitch.
- **What**: A discussion of drawbacks (data poisoning, bias, inaccessibility, de-skilling) that emerge when AI assistance is introduced into carefully-tuned operational systems, plus strategies for keeping AI transparent and reliable rather than an inscrutable black box. (from abstract only)
- **How**: Draws on the speakers' personal experience working around biased/broken AI-assisted systems. (from abstract only — thin on mechanism)
- **Where applicable**: General for any org introducing AI-assisted tooling into existing operational systems.

### Fully Automated HW SKU Selection System to Optimize Apache Pinot's Cost-to-Serve at LinkedIn

*Jia Guo and Dino Occhialini, LinkedIn; Yifan (Sabrina) Zhao, Netflix* — **Wildcard**

- **Why**: Not a networking or identity fit, but a genuinely novel operational capability — automatically recommending optimal hardware SKUs across a ~14,000-machine fleet based on live workload profiling — that touches the PM's "physical" interest from an unusual angle (hardware selection as an automated, continuous optimization problem rather than a one-time procurement decision).
- **What**: A fully automated system that recommends optimal hardware SKU profiles for Apache Pinot's production OLAP database fleet (~14K machines) at LinkedIn, cutting cost-to-serve by nearly 50% across highly varied workload, cost, and dataset-size characteristics. (from abstract only)
- **How**: Low-overhead profiling collects high-cardinality resource-usage data (CPU, memory, IO) from production clusters across multiple SKU profiles, feeding a cost-optimization algorithm that recommends SKU allocation with minimal operational overhead. (from abstract only)
- **Where applicable**: Large heterogeneous-hardware fleets running variable workloads; the general pattern (continuous, profiling-driven hardware-fit optimization rather than static procurement) generalizes beyond Pinot/OLAP specifically.

## Themes

- **Certificate lifecycle management keeps surfacing as unglamorous but critical infrastructure.** Let's Encrypt's decade of free automated CA operations and Netflix's cert-lifecycle-hardening of a 400M req/s cache both treat certs as load-bearing infrastructure requiring dedicated engineering — echoing the same crypto-agility theme from the Netflix Enigma talk at this cycle's USENIX Security (see that digest).
- **The cloud networking abstraction keeps leaking at scale.** emnify's AWS networking-limits war stories and Slack's revival of classical network-graph-theory traffic attribution both argue that treating "the cloud network" as an infinite, opaque resource stops working once you're pushing real packet/connection volume.
- **Datacenter-scale chaos engineering is a maturity signal.** USAA's whole-datacenter (not single-service) chaos testing suggests some organizations are moving failure-domain testing to match actual production blast radius rather than testing individual services in isolation.
- **AI/ML infrastructure operations dominated this cycle's program by sheer volume** — safe model rollout, ML training governance, AI-assisted ops, AIOps vendor skepticism — but almost none of it intersects the PM's stated core interests; flagged here as a program-wide trend rather than pulled into the picks above.
- **This cycle's program is genuinely thin on networking and identity architecture specifically.** Most content is observability tooling, incident-response process, and organizational/human-factors material — worth noting as a property of this program, not a sign that relevant content was filtered out.
