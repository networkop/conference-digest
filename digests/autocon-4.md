<!--
conference: AutoCon 4 (Austin)
type: operator
source_url: https://networkautomation.forum/autocon4
generated: 2026-11-01
registry_key: autocon-4
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AutoCon 4 (Austin) — Digest

An operator-focused network automation program. Note up front: this cycle is heavy on automation practice, Day-2 operations, and the first wave of agentic-AI-in-production stories — lighter on the deep datapath/optics/identity material than a SIGCOMM or OSNA program, but the DC-fabric and WAN operator case studies below are directly on-target.

## Core

### Spectron: network orchestration in practice at scale; what works, what hurts

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-KatarzynaKurowska-AldrinIsaac-Spectron.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-KatarzynaKurowska-AldrinIsaac-Spectron.pptx) · [Recording](https://www.youtube.com/watch?v=RbBlNKj2IW8)

Katarzyna Kurowska & Aldrin Isaac — eBay (Senior Software Engineer; Director, Site Network Engineering & Security)

- **Why**: The single most relevant talk for physical DC fabric work: how a hyperscale-adjacent operator designs, provisions, and validates diverse DC topologies with an in-house intent-based system — including a candid "what hurts" section, which is rarer and more useful than the wins.
- **What**: Spectron is eBay's spec-driven, intent-based fabric orchestration covering the ZTP lifecycle: fabric planning, spec generation, rack/TOR power-on, and deployment. Engineers write JSON topology specs (site, IP spec, node/interface specs for spines/leaves); the system renders device config, validates against a digital twin, and deploys. Multi-vendor, with explicit SONiC support. The "what hurts" half is the real value: abstractions that came out too generic or too limiting, prototypes that silently became production code, and SONiC's promise of a unified software stack across interchangeable hardware colliding with per-vendor functionality and API discrepancies.
- **How**: Layered, composable abstractions — Layout (NodeSpec + InterfaceSpec), IP addressing (IPSpec + IPAllocationSpec), routing (RoutingSpec), and fungible hardware via PlatformSpec + NodeProfile — with rendering decoupled from generation and renderers composed from reusable blocks. GNS3-based topology emulation verifies before production deploy. A custom schema language and model generator keep it extensible; an adapter principle absorbs multi-vendor SONiC differences.
- **Where applicable**: eBay-specific build, but the architecture lessons (define your domain early, design around primitives, embed NetEng in the dev cycle, early verification at every lifecycle stage) transfer to any operator building or buying fabric automation. Future work listed: EVPN/VXLAN overlay, test/Day-2 framework, traffic filters, HA/scalability — worth tracking if you have adjacency with the team.

### Kubernetes Network Emulation, a standard interface to design and validate networks

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ManodiptoGhose-RyanElliott-KubernetesNetworkEmulation.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ManodiptoGhose-RyanElliott-KubernetesNetworkEmulation.pptx)

Manodipto Ghose & Ryan Elliott (no affiliation given in program)

- **Why**: Sits exactly at the intersection of the PM's cloud-native and physical-network interests: it uses Kubernetes as the substrate for emulating real multi-vendor network OSes, enabling shift-left validation without lab hardware.
- **What**: KNE (openconfig/KNE) is a vendor-neutral network device emulation framework: containerized vendor NOS images wired into arbitrary topologies on Kubernetes, with lifecycle management provided by k8s. Paired with the OpenConfig Feature Profiles repo and the ONDATRA test framework, it enables "write test once, run anywhere" — the same tests against a virtual KNE testbed and a physical one. Claimed outcomes: weeks/months saved over waiting for testbed procurement, and at least 50% savings in testbed build costs.
- **How**: Topology defined as nodes (vendor NOS containers, e.g. Arista cEOS, with bootstrap config and certs) plus A-to-Z links; Ixia-c (containerized Open Traffic Generator, OTG model-based API with Snappir/GoSnappi SDKs) injects traffic and emulates control planes (e.g. BGP peers) at points in the topology. OTG scales from containers to hardware generators via the same API.
- **Where applicable**: Open-source and broadly applicable, with one hard dependency: your NOS must have a container image (major vendors do). Best fit for feature/compliance testing and CI; not a performance- or optics-fidelity tool — control-plane and functional behavior only. The "compliance as code" angle (shared test suites in featureprofiles) is a genuine standardization play worth watching.

### Overhauling Data Center Network Automation: Intel's Data-Centric Journey

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-GregBotts-IntelsDataCentricJourney.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-GregBotts-IntelsDataCentricJourney.pptx) · [Recording](https://www.youtube.com/watch?v=wl1STXalmEQ)

Greg Botts — Intel (Senior Network Engineer)

- **Why**: A rare full-journey DC automation case study at real scale (global, 5k+ devices, new network platform + new automation system simultaneously), with a clear architectural position: data first, everything else is a by-product.
- **What**: Intel IT replaced a turnkey vendor automation solution (inflection point: roadmap, scale, and cost limits) with a data-centric system built on Nautobot as the network source of truth, plus open-source components, DBaaS, and config generation. Timelines are concrete: 6-month prototype, 8-month pilot, 1-year migrations — delivered on time and under budget. Results: provisioning time reduced ~75%, 100% standardized configs.
- **How**: Foundation is modeled, centralized, programmatically accessible network data (device inventory, device data, jobs, golden config → intended config). Key learnings: model for scale, right-size and enable log-cleaner (hosting matters), and "relentlessly standardize" — eliminate one-offs. The modeled data is explicitly positioned as the on-ramp for AI ("table is set for AI") and self-service for partners and customers.
- **Where applicable**: Intel-internal, but the methodology (data-first, NSoT as foundation, staged rollout) is general and vendor-neutral — Nautobot is open source. Most useful if you run a large multi-site DC estate and are weighing build-vs-buy on automation; the talk includes their actual build/buy criteria list.

### ESnet's new Micro-Service based Discovery Service

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-MarcKoerner-ESnetDiscoveryService.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-MarcKoerner-ESnetDiscoveryService.pptx) · [Recording](https://www.youtube.com/watch?v=AxSFCr7zo40)

Marc Koerner — ESnet

- **Why**: ESnet operates a national science WAN with optical line systems — the closest thing in this program to the PM's DC/WAN interconnect and optics interests. This is a production (since June 2025) redesign of how bulk network data is collected and normalized, born from real operational pain.
- **What**: A Kafka-based, notification-driven discovery and document-repository architecture replacing per-application polling. Previously, multiple tools independently queried devices for overlapping purposes (optical circuit sync with the config DB, L2/L3 topology for the OSCARS L2VPN tool), causing redundant collection, inconsistent data across apps, and unnecessary device/network load. The Discovery Service centralizes this into one low-friction mechanism with pluggable normalizers.
- **How**: Agent Controller (scheduler, dedup of discovery requests) distributes work via Kafka to Discovery Agents, which pull data from sources — NETCONF from devices, RESTCONF from the TNMS management system, or even spreadsheets. Documents (up to 80MB, compressed) land in the "Andy Lake Service" repository with metadata and history; stacked/parallel normalizers (implementing the TOWL equipment ontology) generate normalized views and compute change notifications. Fine-grained controls: configurable audit intervals, namespace-level gets, regex filters to strip counters and sensitive data before storage. Deployed as microservices on Kubernetes (two prod clusters plus staging) with GitLab/Argo CD/Rancher.
- **Where applicable**: ESnet-specific stack (Kafka, TOWL, k8s), but the design pattern — notification-driven bulk data management with normalized views — generalizes to any multi-tool operator drowning in redundant polling. The honesty about equipment is valuable: vendor NETCONF/YANG standard violations, devices that lock up under discovery, models so large the device times out, and NSO being slow at non-config retrieval. Budget for these if you attempt the same.

### Scaling Network Operations with Modular Ansible: A Multi-Environment Automation Framework

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-JosephNicholson-ScalingNetOpsWithModularAnsible.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-JosephNicholson-ScalingNetOpsWithModularAnsible.pptx) · [Recording](https://www.youtube.com/watch?v=mVq5bdkiskg)

Joseph Nicholson — NTT DATA, Global IP Network (AS2914)

- **Why**: A Tier-1 transit backbone operator's playbook for scaling Ansible across a multi-vendor WAN including DWDM — backbone routers across three vendors, optical across two — which matches the PM's WAN and interconnect focus.
- **What**: Six years of evolving an Ansible repository into a modular, multi-environment automation framework serving GIN's 800+ network elements (250+ backbone routers, 100+ DWDM elements across 5 continents, 40+ countries, 90+ PoPs), covering software upgrades, maintenance snapshots, traffic updates, and circuit testing — run from CLI and AWX.
- **How**: Dynamic inventory is a Python script pulling all device data (platform, vendor, OS, location, monitoring status) from GUMS, their in-house change-management system with 25+ years of lineage (started as Verio tooling in the late 1990s) — groups are built per vendor/platform/device-type on every playbook run. CI/CD pipeline gates merges on `#FIXME` tags and syncs revision vars to AWX hourly; task files are shared across playbooks with a careful include (dynamic) vs import (static) discipline; folder structure is per-playbook, subdivided per NOS.
- **Where applicable**: NTT GIN-specific in its dependence on GUMS and org history, but the transferable lessons are explicit: adopt pipeline and AWX APIs earlier, enforce repository naming policy, use dynamic inventory from your existing change system rather than maintaining static files, and understand include/import semantics before sharing task files. Honest about the trade-off: shared task files update many playbooks at once — and break many at once.

### From Band-Aids to Best Practices: USAA's Network Automation Journey

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-BrandonCavett-BestPracticesAtUSAA.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-BrandonCavett-BestPracticesAtUSAA.pptx) · [Recording](https://www.youtube.com/watch?v=MEDwtGy99jQ)

Brandon Cavett — USAA (Senior Infrastructure Engineer)

- **Why**: A concrete, Arista-centric DC story of the pattern most enterprises actually live: Day-1 rack provisioning automated early, Day-2 becoming the real problem, and config-as-code (AVD) as the resolution — including retrofit difficulty and engineer-training costs.
- **What**: USAA built end-to-end automated rack provisioning (CloudVision config builders via API, switch provisioning in under an hour hands-off), then hit Day-2 reality: CLI-first changes, drift between designed and running config in CloudVision when standalone Ansible playbooks pushed directly to switches, and heavy per-playbook testing. They adopted Arista AVD (Architect, Validate, Deploy), which standardized config fabric-wide, enabled sweeping changes quickly, and let them use CloudVision's change-control process to pre-stage and review changes. Most recent environments are 100% config-as-code; the Day-1 provisioning pipeline was replaced by AVD entirely.
- **How**: AVD (Ansible collection) generates config from structured intent and deploys via eAPI or CloudVision; pre-provisioning pipelines export the data needed to add new switches into AVD. Next steps: wrap the whole process in CI/CD with Arista Cloud Test (ACT) for pre-deployment testing and ANTA for post-validation, plus retrofitting legacy environments.
- **Where applicable**: USAA/Arista-specific (AVD, CloudVision, ACT/ANTA are Arista tooling), so directly applicable only to EOS/CVP estates — but the drift problem from out-of-band playbook changes, the change-control-integration pattern, and the "training traditional network engineers on Git/CI/Ansible is the hard part" observation generalize broadly.

### The Secret to Network Config & Security Compliance at Scale

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-VincentPhelan-Compliance.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-VincentPhelan-Compliance.pptx) · [Recording](https://www.youtube.com/watch?v=nSlSDb8B2Ks)

Vincent Phelan — Head of Network Architecture & Automation (financial sector)

- **Why**: The PM's network-security interest gets its strongest entry here: a working, scaled config-compliance system at a bank, with real numbers, built on open components (OPA, TextFSM, GitOps) rather than a compliance product.
- **What**: A config/security compliance pipeline that runs compliance for 7,000 devices against 70 policies in about one minute, treating architecture (constraints, standardization, cutting the product count) and automation as one discipline rather than two teams. Includes five anti-patterns from 20 years of war stories — premature optimization, snowflake-tolerant design, manual data massaging, imaginary scaling fears, and forcing formats (YAML/Jinja2) on engineers who don't natively speak them.
- **How**: Collect generic data from any source via device command output, parse with TextFSM ("yet to find something more generic and not AI"), filter junk before processing, and keep everything with a "not yet" adage. Compliance rules are expressed as Open Policy Agent (Rego) policies — and, in the "write programs that write programs" spirit, the OPA policies themselves are auto-generated with expected/actual/allow fields and control-mapping metadata (control ID, description) baked into each evaluation, producing per-device, per-control, per-evaluation overviews. The GitOps repo scales to 3.5M objects / ~20GB. Drift detection and remediation close the loop.
- **Where applicable**: Technique is org-agnostic and built on open source; the control-mapping metadata pattern is especially transferable to any regulated environment (financial, healthcare) where compliance evidence must tie to specific controls. The architecture-first stance (reduce product count before automating) is a prerequisite, not an option — the speaker is explicit that automation bolted onto a patchwork fails.

### Is MCP just an API Abstraction?

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-WilliamCollins-MCP.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-WilliamCollins-MCP.pptx) · [Recording](https://www.youtube.com/watch?v=-SKWJhKseEE)

William Collins — Director, Technical Evangelism

- **Why**: MCP is the emerging protocol substrate for agentic systems interacting with infrastructure — directly relevant to the PM's workload/agentic identity and protocol interests (how agents authenticate, discover capabilities, and get scoped access is the same problem class as OAuth/OIDC/SPIFFE, one layer up). This is the sharpest protocol-level dissection in the program.
- **What**: A point-by-point architectural comparison of MCP against REST APIs, concluding MCP is not merely an API wrapper: REST is stateless, URL-routed, and built for human developers; MCP is a stateful, session-based JSON-RPC protocol with dynamic capability discovery, built for AI models to interact with external systems safely. The framing of the N×M integration problem (N models × M tools = N×M custom integrations, with quadratic maintenance and vendor lock-in) collapsing to N+M (N clients + M servers) is the clearest articulation of why the protocol matters.
- **How**: MCP's three primitives — Resources (read data/context), Prompts (templates), Tools (execute actions) — plus context (semantically-tagged data loaded into the model's window) and logs (diagnostics pushed back). Decorators auto-generate tool schemas from docstrings, eliminating the glue code and agent-loop plumbing of hand-rolled function calling. The talk's best design guidance is intention-based tool design (`run_compliance_check(device_group, policy)` rather than endpoint-mapped getters), role-based capability filtering via tags to prevent decision paralysis, and MCP gateway patterns as evolution paths. It also cleanly separates intelligence (understanding intent) from scale (concurrency, multi-tenancy).
- **Where applicable**: Protocol-general, vendor-neutral, with working code (github.com/wcollins/talks). Caveat: the speaker is a technical evangelist, but the content is architecture analysis, not a product pitch. Directly applicable to anyone designing agent-to-infrastructure access — and the role-based tool-exposure idea is effectively least-privilege scoping for agents, a live question in agentic identity.

## Adjacent

### From Manual to Marathon: My Automation Journey at HEB

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ErichCrosswhite-ManualToMarathonAtHEB.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ErichCrosswhite-ManualToMarathonAtHEB.pptx) · [Recording](https://www.youtube.com/watch?v=jhxgJNrWeY0)

Erich Crosswhite — H-E-B

- **Why**: The best near-miss postmortem in the program: a change that nearly removed DNS servers from the production config chain, what guardrail failed, and how the pipeline was hardened afterward.
- **What**: An IaC journey for a new Arista environment at a 400+ store retailer: AVD-based config generation, GitLab MRs with peer review, AWX webhooks, CloudVision (CVaaS) change controls, auto-generated Confluence docs, and — after the near-miss — Nautobot integration for access-port config that was subsequently removed, not because the product failed, but because the author's scripting lacked controls.
- **How**: The DNS incident: a Nautobot data cleanup (logical cables disconnected) propagated through CI/CD and the generated config dropped DNS servers; luck (`execute_tasks: false` in CloudVision) prevented an outage. The fix: build stage generating config from both main and feature branches, a validate stage diffing them plus Batfish verification, results reported directly into the merge request for review before deploy. Also includes a lab cautionary tale (a `state: absent` that wiped the lab fabric to ZTP) and future work toward Container Lab digital twins with ANTA validation.
- **Where applicable**: H-E-B/enterprise-specific and Arista-stack-specific, but the pipeline design (MR-integrated diff + Batfish gates, guardrails around SoT-driven generation) is adoptable by anyone. The core lesson — the SoT product was fine; the unguarded integration was the risk — generalizes completely.

### Toward Autonomy

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ScottRobohn-TowardAutonomy.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_General-Session/AC4-ScottRobohn-TowardAutonomy.pptx) · [Recording](https://www.youtube.com/watch?v=esVkHChgSg8)

Scott Robohn — NAF | Solutional

- **Why**: The best framing talk of the cycle for where closed-loop network operations is heading — useful context for any PM whose roadmap touches autonomous remediation.
- **What**: "Control Plane 3.0": autonomy as a continuum (scripted automation → goal-driven adaptive behavior), not a feature you turn on. Argues we already run autonomous systems — BGP being the exemplary model (distributed, convergent, bounded impact) — and enumerates the necessary ingredients: control loops fed by telemetry, fail-safe error handling for states you didn't anticipate, incremental workflow-by-workflow development, and people and trust built through measurable experiments and gated rollouts.
- **How**: Phased rollout per use case (experiment → PoC → limited prod → scale), with a difficulty tiering that rings true (easy: device OS upgrade, branch CPE turn-up; medium: SP edge turn-up, multi-tenant segmentation; hard: global failover orchestration, brownout mitigation, intent-drift remediation). AI is positioned as a "how, not a what" — one tool among several, with hybrids of AI and traditional mechanisms called the most likely effective path. Reference scaffolds: TM Forum autonomy models, ETSI ENI, IBN — "models as scaffolding, not doctrine."
- **Where applicable**: Conceptual rather than a case study, but the difficulty tiers and cross-domain orchestration framing (LAN + DC + WAN + cloud + security, and IP/optical alignment as an opportunity) are directly relevant to DC/WAN planning. No org-specific dependencies.

### 2025 State of Network Automation Survey Results

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-ChrisGrundemann-2025NetworkAutomationSurveyResults.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day1_Wed_19Nov_Single-Track/AC4-ChrisGrundemann-2025NetworkAutomationSurveyResults.pptx) · [Recording](https://www.youtube.com/watch?v=DihuRAAXA0A)

Chris Grundemann — Network Automation Forum

- **Why**: Field-wide data every PM in this space should have on hand: 681 responses (352 complete) across 58 countries and 34 industries — an order of magnitude larger than prior years (106 in 2024, 78 in 2023).
- **What**: The headline findings paint a less rosy picture than conference hallways suggest. Mean self-assessed automation is 37.5% (down from ~42% the prior two years — plausibly a sampling effect from more early-stage and enterprise respondents), 73% of orgs are at or below 50% automated. The "half-nots": half of organizations have less than 30% automation, no LLM plans (only 3% have LLMs deployed with production network access; ~45% have no plans), zero dedicated automation staff, don't measure automation success, and are misaligned with leadership. 44% of reported barriers are "people" problems (skills 27%, organizational 20%, cultural 14%); technical is only 10%.
- **How**: Survey methodology with year-over-year comparability caveats the presenter himself flags ("Caveat Emptor" — sample composition shifted notably: 39% USA vs 58% in 2023, enterprise share up to 42%). Tooling data: 82% homebrew, Ansible dominates OSS (53%), Python at 93% of scripting; top automated tasks are backups and device deployment; the largest gaps between current and desired automation are troubleshooting (+223), capacity planning (+167), and traffic engineering (+156).
- **Where applicable**: Globally sourced and broadly indicative rather than statistically pure — use the directional findings (people barriers, the troubleshooting gap, minimal production AI) to calibrate roadmap assumptions, not as precise benchmarks.

### HAWAT: An AI Assistant for Network Troubleshooting

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-KarlNewell-HAWAT.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_PM_General-Session/AC4-KarlNewell-HAWAT.pptx) · [Recording](https://www.youtube.com/watch?v=nEWnIYK3koI)

Karl Newell & Matt Mullins — Internet2

- **Why**: A working agentic AI assistant interfacing directly with network hardware at a national research network — one of the few demos in the program where an LLM-driven agent reasons through real protocol failure modes.
- **What**: HAWAT (Heuristic Analysis With Adaptive Troubleshooting): an agentic chatbot that interprets network conditions and executes commands on infrastructure. Demonstrated on both a lab topology and Internet2's 88-device production-scale national network (aggregation routers, core routers, global exchange points), including live latency tests (NY–LA, ~69ms) and BGP route-origin analysis per neighbor/VRF.
- **How**: LLM + RAG (over network documentation) + ReAct agentic framework. The demos shown are the convincing kind: diagnosing an OSPF adjacency failure to a hello-interval mismatch (10s vs 20s) with the specific log lines, explaining adjacency flapping from "inactivity timer expired" / "nbr did not list our router ID", and drawing ASCII topology with data-plane vs management-plane distinction. Next steps are MCP and agent-to-agent protocols.
- **Where applicable**: Internet2 research-network context, and the demos include pre-recorded sessions — evaluate the failure-diagnosis patterns rather than production readiness. The approach (LLM as reasoning front-end over a bounded command set, with RAG grounding in topology and docs) is replicable in any environment; the risk profile of letting it execute commands is yours to scope.

### The NetDevOps Journey: Manual Firefighting to Agentic Autonomy

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-ClosingKeynote-GregFreeman.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-ClosingKeynote-GregFreeman.pptx) · [Recording](https://www.youtube.com/watch?v=woGsjPS7cro)

Greg Freeman — Lumen (VP Network & Customer Transformation) — Closing Keynote

- **Why**: Scale and candor from one of the world's largest networks — ~340,000 fiber route miles, 350+ Tbps backbone, AS1 — on both what large-scale automation achieved and a sober reading of AI's failure statistics.
- **What**: Lumen's operational transformation: 80% "hands out of the network" via machine-to-machine communication, 350+ workflows developed, running at a pace of ~10 workflows per minute 24×7, built on Itential orchestration with an integration layer spanning ticketing, alarming (Splunk, RFM), CMDB, and dozens of system adapters. The second half pivots to AI: an MCP architecture with an MCP service layer (Ollama in DDC, Databricks/Claude) exposing internal tools to agents, plus a "Supervisor Agent" above them — and an AI use case for pinpointing fiber-cut GPS locations.
- **How**: The automation strategy is standards-plus-process ("no shortcuts": PDDs, SDDs, training, "upscaling employees" rather than replacing them). The AI section is notable for citing both Wharton's optimistic outlook and MIT's cautionary one (of $30–40B invested in custom AI projects, ~95% see zero return; organizational readiness, not technology, is the limiter), plus clear "what AI is not" caveats: non-deterministic outputs need human oversight, it is not a universal replacement, and it requires continual upkeep.
- **Where applicable**: Lumen-specific scale and Itential-based stack — the workflow counts and mediation architecture are their topology. Transferable: the tiered support-culture shift, the supervisor-agent-over-MCP-services pattern, and the discipline of treating AI adoption as an organizational-readiness problem. Treat the ROI claims as directional; the cited MIT/Wharton tension is the honest part.

### From CLI to Model: Building a Foundational Source of Truth for Brownfield Networks

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MunachimsoNwaiwu-FromCLItoModel.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MunachimsoNwaiwu-FromCLItoModel.pptx) · [Recording](https://www.youtube.com/watch?v=5iIx-PYqbBI)

Munachimso Nwaiwu — Revelo (open-source project)

- **Why**: Addresses the barrier that stops most brownfield automation: no source of truth on a legacy network with no budget — with an open-source methodology and working code rather than advice.
- **What**: A three-step pipeline ("Revelo"): bootstrap an inventory (either explicit IP/credentials/platform, or discovered via `nmap -O` including hidden subnet devices), build a structured SOT by parsing live state into JSON, and validate state with automated diffs. Demonstrated on a multi-vendor lab (Cisco IOS/IOS-XE/NX-OS, Junos).
- **How**: NAPALM for vendor-neutral getters (facts, interfaces IPs, LLDP neighbors), Netmiko as the "truck" for CLI commands NAPALM doesn't cover, and Genie (pyATS) as the parser. The versioning design is the clever part: `inventory/1/`, `sot/1_2/` (snapshot 2 under inventory 1), `diff/1_2/` — producing an auditable history and two validation modes: live compliance ("is the network compliant right now?") and offline audit ("what changed last night?") with clean structured diffs instead of config noise.
- **Where applicable**: Broadly applicable to any brownfield network with programmatic CLI/API access — no greenfield or budget required, and the components are all mainstream open source. Limits: it captures operational state as the baseline, so your "intended state" is initially defined by whatever is actually running — a starting point, not a governance model.

### Bridging Infrastructure and Data

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MarcoMartinez-BridgingInfrastructureAndData.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day2_Thurs_20Nov_AM_Advanced-Track/AC4-MarcoMartinez-BridgingInfrastructureAndData.pptx) · [Recording](https://www.youtube.com/watch?v=eU6-fYqch8Y)

Marco Martinez — Swisscom (Infrastructure Automation Architect)

- **Why**: An IPAM-relevant engineering talk: dynamic, SoT-driven resource allocation (e.g. "give me an unused IP") pushed directly into Terraform, solving the impedance mismatch between dynamic schemas and static provider definitions.
- **What**: A proof-of-concept custom Terraform provider for Infrahub, powered by GraphQL, that eliminates static `.tfvars` files and makes infrastructure data (unused IPs, standard vSwitch configs, cloud-provider IP reservations) directly available — read-only and read-write — inside IaC workflows, with an automated pipeline that builds and publishes the provider.
- **How**: The core problem is that Infrahub has a dynamic schema (no default schema; it changes per instance and branch) while Terraform providers expect static schemas in Go — and no Go SDK existed for Infrahub. The solution: a generator that takes your GraphQL queries, uses genqlient to produce a typed Go SDK, and templates a provider from them — schema baked in per version, published to a private registry, `make all` to build. Documented honestly: the design choices brought significant complexity, and self-built providers are not the norm.
- **Where applicable**: PoC-stage and Swisscom-context; the pattern (dynamically generating a provider from queries rather than hand-maintaining one) generalizes to any GraphQL-backed SoT/IPAM system (Infrahub, or similar). Directly relevant to anyone who wants IPAM allocation to happen inside Terraform plans instead of spreadsheets.

## Wildcard

### A Harmonized, Standards-based Ontology for Telco-grade Agents

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-DaveDuggal-Graphs.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-DaveDuggal-Graphs.pptx) · [Recording](https://www.youtube.com/watch?v=LydZQboIm5E)

Dave Duggal — EnterpriseWeb (founder/CEO)

- **Why**: Not a fit for the PM's core stack, but it is the most idea-dense 30 minutes in the program: a serious architectural argument for why LLM agents can't be telco-grade without formal knowledge engineering — and a critique of the industry's current GraphRAG/RAG direction.
- **What**: The argument: statistical pattern matching (GenAI/agentic AI) is not good enough for reliable, available networks — backed by cited benchmarks (best-performing models at 25% full-sequence-match accuracy on nested API-call tasks; "context rot" research; Apple's "illusion of thinking"). The proposal: knowledge graphs with formal ontologies (harmonizing 3GPP, O-RAN, TMF, ETSI NFV, TOSCA, MPLIFY LSO) as the deterministic layer, with the KG as a "control language" over language models — low-token, low-latency, energy-efficient, deterministically validating inferences — and as a secure blackboard providing shared memory, domain knowledge, temporal history, and tools to agents under strong governance.
- **How**: The technical meat is a "ladder of abstraction" from relational tables through labeled-property graphs and RDF triplestores to hypergraphs supporting multi-dimensional, conditional, n-ary relationships — with pointed analysis of why each lower rung fails (joins are expensive; LPGs can't model n-ary object relationships; RDF triples explode with complexity). The KG sits behind an MCP server as "Context-as-a-Service."
- **Where applicable**: Telco-centric (3GPP/TMF framing, 6G "AI-native" vision) and vendor-originated (EnterpriseWeb CEO), so discount accordingly — but the underlying critique and the hypergraph-over-RDF/LPG reasoning apply to anyone building agent governance for infrastructure where determinism matters. Pairs naturally with the PM's identity interest: this is effectively an argument for formal, governable agent context and permissions.

### Battle of the Bots: Which AI Models Actually Work for Network Engineering Tasks

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-EricChou-BattleOfAIBots.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon4/Day3_Fri_21Nov_Single-Track/AC4-EricChou-BattleOfAIBots.pptx) · [Recording](https://www.youtube.com/watch?v=77doPhGapwE)

Eric Chou — Network to Code

- **Why**: A genuinely reusable decision framework rather than another AI demo — and the methodology (expected-value analysis plus task-specific evaluation) transfers to any AI adoption decision, including agent/identity tooling.
- **What**: The premise: "which model is best?" is the wrong question; the right one is "what is the expected value of using AI for *this* task with *this* model?" A lightning talk with a decision-tree method: map decision points, calculate probabilities of success, and derive expected value per option — illustrated with a worked RCA example (AI root-cause platform at 75% success rate, 30-minute resolution vs 4-hour manual, $4k/hr downtime cost, $10k SLA penalty — EV of AI-powered RCA $11,000 vs -$26,000 for manual).
- **How**: Three practical evaluation methods to establish the probability inputs: expert review (human in the loop), automated code evaluation (digital twin for pass/fail), and AI-as-judge. The takeaway: build your own evaluation system and iterate — with a sensible default (Claude) as the starting point, not the conclusion.
- **Where applicable**: Task- and org-specific by construction — the whole point is that you run it on your tasks with your cost/downtime numbers. Broadly applicable wherever AI tooling is being considered for repeatable technical work; the evaluation-system pattern (expert + code + AI judge) is the durable part.

## Themes

- **Data-first is the settled consensus**: Intel (Nautobot NSoT as foundation), ESnet (centralized discovery + normalization), the brownfield SOT talk, and Swisscom's Infrahub integration all independently converged on "model the data first; everything else is a by-product." Source-of-truth design is where the architectural effort now goes.
- **Agentic AI crossed from demos into operator practice — but production reality is thin**: HAWAT, Lumen's supervisor-agent-over-MCP architecture, and constrained-accuracy pipelines (Building AI with AI) show real systems; the survey shows only 3% of orgs with LLMs deployed against production network data and ~45% with no plans. The gap between conference content and field adoption is the widest it's been.
- **MCP specifically, not "AI" generally, is the concrete protocol story**: the MCP dissection talk, Lumen's MCP service layer, HAWAT's roadmap, and the telco-ontology talk (MCP as context server) all treat MCP as the integration substrate — with intention-based tool design and role-based capability filtering emerging as the de-facto scoping model for agent access.
- **Validation shift-left went mainstream**: digital twins (Spectron/GNS3, KNE, Container Lab), pre-merge config diffs with Batfish, ONDATRA "write once, run anywhere" against virtual and physical testbeds — verify-before-deploy is now assumed practice, not novelty.
- **Day-2 is the honest battleground**: USAA's drift-and-retrofit story, HEB's near-miss, NTT's upgrade workflows, and the lifecycle-automation material all describe the same arc — provisioning gets automated first, then Day-2 maintainability (guardrails, change control, training) is where programs succeed or stall.
- **The constraints are organizational, not technical**: the survey's 44% "people" barriers, Lumen's MIT citation (95% of custom AI projects see zero return for readiness reasons), and the leadership track's sociotechnical framing all point the same direction — skills, trust, and sponsorship, not tooling, are the rate limiters this cycle.
