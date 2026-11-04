<!--
conference: AutoCon 5 (Munich)
type: operator
source_url: https://networkautomation.forum/autocon5
generated: 2026-11-01
registry_key: autocon-5
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AutoCon 5 (Munich) — Digest

AutoCon 5 is a network-automation operator conference, so nothing here touches optics, RDMA/lossless fabrics, eBPF/Cilium, or FIDO/SPIFFE directly. The value for this PM is in the physical-fabric and WAN automation war stories (EVPN/VXLAN, SRv6 backbones, an 800G pan-European migration), one genuinely strong network-security automation case, and the agentic-AI governance debate that dominated the leadership track. Picks below are grouped accordingly.

## Core

### Network Operations Automation at DE-CIX

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Lucas%20Immanuel%20Nickel%20-%20Network%20Operations%20Automation%20at%20DE-CIX.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Lucas%20Immanuel%20Nickel%20-%20Network%20Operations%20Automation%20at%20DE-CIX.pptx) · [Recording](https://www.youtube.com/watch?v=k1TMAgNROh8)

Lucas Immanuel Nickel · Network Operations Engineer — DE-CIX

- **Why**: One of the few talks treating network automation itself as production infrastructure with SRE discipline — reliable delivery, observability, safe failure — at an interconnection platform whose fabric is the product.
- **What**: DE-CIX (3,700+ connected networks, 100+ routers, hundreds of circuits) runs 15+ production web services, 20+ cron jobs and 500+ executions/day from one shared library. Two shipped patterns: a gNMIc config-generation job driven from Zabbix + NetBox, and a geospatial network view service; both deploy via GitOps in under 10 minutes.
- **How**: All workloads (cron jobs and web services) run in Kubernetes behind a single standardized CI/CD path (Kaniko → Harbor → Helm → K8s, Renovate for deps). The gNMIc generator turns Zabbix host/proxy and NetBox device data into proxy configs exposing device telemetry as Prometheus metrics. "Geo" correlates NetBox + Zabbix into a live geographic view, inferring relationships from imperfect data and preferring "incomplete but honest output" over silent success. 1 in 3 deploys is rejected before production — failure moved deliberately left.
- **Where applicable**: The GitOps delivery and defensive-automation patterns are broadly applicable; the scale and IXP workflows (route servers, FPU fiber switching) are DE-CIX-specific. The Kubernetes investment assumes you already run a container platform for network tooling.

### Rethinking Network Monitoring

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Christian%20Adell%20-%09David%20Flores%20-%20Rethinking%20Network%20Monitoring.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Christian%20Adell%20-%09David%20Flores%20-%20Rethinking%20Network%20Monitoring.pptx) · [Recording](https://www.youtube.com/watch?v=F6_f1piv0LI)

Christian Adell & David Flores · CoreWeave

- **Why**: The clearest architectural statement at the conference that monitoring is the feedback signal for automation, not a dashboard problem — from a GPU-cloud operator running hyperscale DC fabrics.
- **What**: The argument is that the gap isn't tooling but architecture: observability is a pipeline (collector → processor → distribution → persistence → visualization) that must be *diverse* (metrics, logs, flows, state, config), *integrable* (tied to the SoT and the orchestrator so the loop closes), and *scalable* (federated, cardinality-aware). The stated goal: a device added to the SoT starts being monitored automatically; a 3am interface degradation is verified and remediated by a workflow, no human.
- **How**: Normalize multi-vendor telemetry (gNMI vs SNMP schemas) into a common shape; enrich with SoT context (role, location, owner, maintenance status) — but only with labels that drive decisions, since every label multiplies time series. SoT decides what gets monitored (push/webhook over periodic sync); "an alert is a contract, not a notification" — alerts must be machine-consumable by the orchestrator.
- **Where applicable**: The pipeline pattern is vendor-agnostic and transfers to any fleet. The "hundreds of thousands of devices" framing is CoreWeave-scale; smaller operators can adopt the architecture without the federation complexity.

### Reaching Fully Automated Backbone Networks: A Network Developer's Journey

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Eugen%20Serban%20-%20Bartek%20Bacal%20-%20Reaching%20fully%20automated%20backbone%20networks%2C%20a%20Network%20Developer%27s%20journey.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Eugen%20Serban%20-%20Bartek%20Bacal%20-%20Reaching%20fully%20automated%20backbone%20networks%2C%20a%20Network%20Developer%27s%20journey.pptx) · [Recording](https://www.youtube.com/watch?v=d4yRszRS6FI)

Eugen Serban & Bartek Bacal · Swisscom

- **Why**: A production SRv6 backbone at carrier scale, with the honest four-year delta between architecture PowerPoints and reality — squarely in this PM's WAN/protocol territory.
- **What**: Today: >3,000 devices (~10k target) running SRv6 orchestrated by NSO with zero manual CLI, >25k public-facing service instances (>150k target), and zero escalated major incidents. The candid part: standardization struggles, early engineering choices that hurt, toolkit woes, organizational and cultural hurdles (Dev vs Ops, Network Engineer vs Developer), and northbound processes that didn't adapt.
- **How**: A virtual dev stage with repeatable testing superseded earlier tooling; automatic documentation; a deliberately small standardized service catalog (L2VPN/EVPN, L3VPN, SRv6) so each component is replaceable. Open challenges named explicitly: true CI/CD, scale testing (YANG leafrefs and "for loops" causing exponential runtime growth), and closed-loop self-healing split into awareness → analysis → decision → execution.
- **Where applicable**: Swisscom-specific SP environment, NSO-centric. The org lessons (the hardest problems were not the network) and the scale-testing pitfalls transfer to any backbone automation program.

### Automation at Scale Across Domains: DC, Campus, and WAN

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Christian%20Breunig%20-%20Automation%20at%20scale%20across%20domains%20%28DC-Campus-WAN%29.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Christian%20Breunig%20-%20Automation%20at%20scale%20across%20domains%20%28DC-Campus-WAN%29.pptx) · [Recording](https://www.youtube.com/watch?v=seiputEwZVg)

Christian Breunig · Network Architect — Rohde & Schwarz

- **Why**: A full EVPN-VXLAN fabric program — dual DCs, campus, WAN — with a quantitative answer to "how much Day-2 work will there really be?" (much more than you think).
- **What**: 500+ devices under unified Git/Ansible/GitLab CI. Change volume grew from 109 (2021) to 1,060 (2025) as the network became a service-provider-like internal backbone — the "few VLANs a year" assumption died quickly. They maintain a 100% EVE-NG replica of the network at all times and spend ~80% of their time in the QA environment.
- **How**: Declarative, data-driven model: NetBox as SoT, data determines what gets rendered (VLANs on port-channels, VLAN database, VNIs). One inventory per domain (DC/LAN/WAN) with domain-specific inheritance (DC.yml/LAN.yml/WAN.yml); ANTA for post-change validation (e.g., detecting decommissioned endpoint ports); ansible-lint/yamllint enforced. Scaling tips include 2-byte vs 4-byte ASN pitfalls (the RD is only 32-bit) and careful MLAG peer-link addressing to avoid customer-VRF conflicts.
- **Where applicable**: Single-vendor (Arista + AVD + CloudVision) — that's the constraint. The QA-digital-twin discipline, the change-rate data, and the MLAG/ASN gotchas transfer to any EVPN fabric program.

### Ten Years of Network Automation at LINX

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Riccardo%20Verzeni%20-%20Ten%20Years%20of%20Network%20Automation%20at%20LINX.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Riccardo%20Verzeni%20-%20Ten%20Years%20of%20Network%20Automation%20at%20LINX.pptx) · [Recording](https://www.youtube.com/watch?v=MRyNX4gDSfI)

Riccardo Verzeni · Director of Software Engineering — LINX

- **Why**: A decade-long incremental journey at a large IXP — customer port provisioning, MAC ACL port security, rate limiting, quarantine testing, thousands of route-server BGP sessions — the physical interconnect + BGP combination this PM lives in.
- **What**: Three phases: NCA (config-as-code from structured data, Jinja2/Ansible/NAPALM, reviewable diffs, git audit trails), NCA 2.0 (unsupervised, asynchronous member self-service via API → message queue → worker), and OMS-based service orchestration plus route-server automation. A bespoke SoT (TSI) was built because nothing on the market fit an IXP with a telco's workflows but not its scale — today they'd probably use NetBox.
- **How**: The standout pattern is the pause–resume hybrid model: the OMS workflow pauses when external action is required (member validates config in quarantine VLAN, invited member accepts a private VLAN, NOC patches a physical port) and resumes automatically once satisfied. Explicit guardrails: locking, serialized deploys, hash-verification of pushed files, defaulting to humans for corner cases.
- **Where applicable**: IXP workflows are LINX-specific, but the pause-resume pattern, the phase-by-phase trust building, and the DO/DON'T list (don't build bespoke by default; don't over-engineer error handling) are broadly transferable.

### GitOps the Hard Way: Rebuilding a Source of Truth (Three Times)

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Radim%20Ro%C5%A1ka%20-%20GitOps%20the%20Hard%20Way%3A%20Rebuilding%20a%20Source%20of%20Truth%20for%20an%20EVPN%20Fabric%20%28Three%20Times%29.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Radim%20Ro%C5%A1ka%20-%20GitOps%20the%20Hard%20Way%3A%20Rebuilding%20a%20Source%20of%20Truth%20for%20an%20EVPN%20Fabric%20%28Three%20Times%29.pptx) · [Recording](https://www.youtube.com/watch?v=Bv5WSaNfblE)

Radim Roška · ALTEPRO solutions (per slides)

- **Why**: The hardest problem in EVPN fabric automation is the data model, not the tooling — demonstrated by rebuilding the schema three times before it survived production. Directly relevant DC-fabric territory.
- **What**: A dual-DC EVPN/VXLAN fabric, ~40 Arista switches, automated from day one with AVD, Git and GitLab CI. The real work: extracting a coherent service model from a network that had no source of truth, discovering vendor-provided data models (AVD's) didn't fit their operational requirements, and building operator tooling (a CLI editor, validator, and search) so junior engineers could actually use the SOT. One year on, the ops team uses it daily; the biggest shift was in how they think about configuration, not speed.
- **How**: Two layers: a CRA service SOT capturing service intent, and a translator to the AVD data model — service identity is global while VLAN/VNI mapping is POD-local, which forced the separate abstraction. Day-2 pipeline: edit → commit → MR → validate → translate → build → deploy, with avd-editor/avd-validator/avd-finder as operator-facing tools.
- **Where applicable**: Arista/AVD-specific implementation at small-mid scale (40 switches, 2 DCs). The core lesson — service intent needs its own abstraction above the vendor model — generalizes to any fabric program.

### Automating firewall rule deployment in a highly regulated environment

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Jo%C3%A3o%20Soares%20-%20Automating%20firewall%20rule%20deployment%20in%20a%20highly%20regulated%20environment.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Jo%C3%A3o%20Soares%20-%20Automating%20firewall%20rule%20deployment%20in%20a%20highly%20regulated%20environment.pptx) · [Recording](https://www.youtube.com/watch?v=PZUpC_SVAsk)

João Soares · Ørsted (per talk content)

- **Why**: The strongest network-security item in the program: policy-as-code firewall automation with hard production numbers, in a highly regulated energy company.
- **What**: DRAGØN, Ørsted's self-service firewall platform: internal customers define, validate and deploy their own rules via a request form or full GitOps workflow, with no firewall team involvement. Results as of 2026: 40+ teams, 150+ users, 3,500+ successful deployments, 3,000+ rejected-by-validation attempts, automated requests 0% → 80%, human-handled lead time down 88% — and total request volume up ~250%, exposing the hidden cost of the old slow process.
- **How**: Security principles were moved out of SharePoint/Word/gut-feeling into policy-as-code: custom Nautobot models abstracting business/security concepts, related to real network constructs, connected by policy, exposed to humans via GUI and machines via API. Validation runs automatically against those policies; security is pulled in automatically when a rule requires it; Terraform deploys to the firewall management platform and Ansible commits to the firewalls. Compliant-by-design, fully versioned and revertable.
- **Where applicable**: Regulated-enterprise specific (Danish critical energy infrastructure), but the pattern — security policy as queryable models rather than documents, plus treating the automation as a real product with versioning/changelog/support — transfers to any security-governed org.

### Migrating the GÉANT Network to a new vendor

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Simone%20Spinelli%20-%20Migrating%20the%20G%C3%89ANT%20Network%20to%20a%20new%20vendor%20using%20WFO%20and%20Ansible.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Simone%20Spinelli%20-%20Migrating%20the%20G%C3%89ANT%20Network%20to%20a%20new%20vendor%20using%20WFO%20and%20Ansible.pptx) · [Recording](https://www.youtube.com/watch?v=UlbrvLODuNg)

Simone Spinelli · GÉANT (per talk content)

- **Why**: A two-year, zero-major-disruption Juniper → Nokia migration of a pan-European IP/MPLS WAN at 800G — physical backbone and interconnection work at continental scale, exactly this PM's core.
- **What**: GÉANT (31 PoPs, 44 nodes, >1,000 services: BGP-based L3, L2 circuits, directly attached servers) migrated to Nokia 7750-SR (SR-OS, not SR-Linux) between June 2024 and February 2026, while simultaneously building the in-house GÉANT Automation Platform (GAP) on open-source Workflow Orchestrator and Ansible.
- **How**: Top-down modeling: every config line exists because it belongs to the node or to a service; one network construct = one Ansible role, with lifecycle management embedded. Peering is modeled org-centrically with lifecycle states (provisioned/active/disabled), covering IX peering, private peering, and upstreams. Concrete migration example: moving an IX port where GAP finds all peers, Moodi starts monitoring, Ansible generates config, operator confirms — AMS-IX with ~120 peers took 30 minutes.
- **Where applicable**: GÉANT/NREN scale, but WFO is a genuinely open, joinable community (SURF, ESnet as partners; public money, public code). The "design as the primary source of truth" and per-construct role patterns transfer to any multi-vendor WAN.

## Adjacent

### Modernizing Workflows as Old as the Railways: Operationalizing Network Automation

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Leo%20Fleskes%09-%20Gerasimos%20Tzakis%20-%20Modernizing%20Workflows%20as%20old%20as%20the%20Railways%3A%20Operationalizing%20Network%20Automation.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%201%20-%20Wednesday/AC5%20-%20Leo%20Fleskes%09-%20Gerasimos%20Tzakis%20-%20Modernizing%20Workflows%20as%20old%20as%20the%20Railways%3A%20Operationalizing%20Network%20Automation.pptx) · [Recording](https://www.youtube.com/watch?v=49j4WqMxm98)

Leo Fleskes · Network Automation Architect — DB Systel GmbH (with Gerasimos Tzakis, Network to Code)

- **Why**: The best data-quality war story in the program — two years of IPAM/inventory cleanup before any automation was possible at a 2,500+-router railway WAN. IPAM data hygiene is directly in this PM's wheelhouse.
- **What**: Building a Single Source of Truth uncovered the brownfield mess: empty locations, "Düsseldorf" vs "Dusseldorf", VRF mismatches, DNS misconfigurations, missing or mis-attributed prefixes. A dedicated cleanup team plus daily issue reports produced +25% documented IP addresses and, crucially, organizational momentum. A VPN rollout that took 70 minutes across four teams now takes 25 across one.
- **How**: Stage-by-stage: SoR interaction through small Nautobot jobs (allocation 25 → 5 min), configuration through an NSO service fed by the Nautobot job (30 → 1 min), documentation still manual. Platform scaling follows Conway: weekly integration meetings, shared responsibility split between platform team and device-owner teams, PRs reviewed from both sides.
- **Where applicable**: Deutsche Bahn-scale brownfield WAN; the sequencing (data first, MVP workflows, blameless cleanup culture) and the "give us a 'let's fix it' mentality" tactic transfer to any brownfield IPAM/SoT effort.

### Lessons Learned Testing Network Automation Solutions

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Ivan%20Pepelnjak%20-%20Lessons%20Learned%20Testing%20Network%20Automation%20Solutions.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Ivan%20Pepelnjak%20-%20Lessons%20Learned%20Testing%20Network%20Automation%20Solutions.pptx) · [Recording](https://www.youtube.com/watch?v=JuLozEjA45U)

Ivan Pepelnjak · ipSpace.net

- **Why**: The most transferable engineering talk of the conference — the testing methodology behind netlab, plus a multi-vendor NOS bug catalog that anyone testing across platforms will hit.
- **What**: ~100 transformation tests plus ~100 error tests comparing against YAML-stored expected results (diffs reviewed in PRs); 25+ integration suites, 250+ individual tests across ~30 device types, requiring 3,700+ lab instances and days of runtime. Hard lessons: testing distributed systems takes longer than planned and vendor implementations will surprise you.
- **How**: Multi-platform testing is solved by *not* parsing show output on ~20 platforms — instead, FRRouting probe containers attached to the device under test run JSON show commands and validate protocol behavior indirectly. Tiered CI: pre-commit (linting, some tests) → push → PR (all transformations) → dedicated server (full integration before release).
- **Where applicable**: Broadly applicable to anyone building or testing multi-vendor automation. The quirks list is directly useful: Junos advertising wide IS-IS metrics as 63, Aruba CX invalid VXLAN IP checksums, mostly-broken OSPF NSSA implementations, divergent EVPN/ARP defaults, unresolved VRRPv3 checksum and MPLS entropy-label disagreements.

### How Workflow-Driven Automation Becomes Operable Under Air Gap & Compliance Constraints

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Henry%20%C3%96lsner%20-%20Christian%20Miene%20-%20How%20Workflow%20Driven%20Automation%20Becomes%20Operable%20Under%20Air%20Gap%20and%20Compliance%20Constraints.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20General%20Session/AC5%20-%20Henry%20%C3%96lsner%20-%20Christian%20Miene%20-%20How%20Workflow%20Driven%20Automation%20Becomes%20Operable%20Under%20Air%20Gap%20and%20Compliance%20Constraints.pptx) · [Recording](https://www.youtube.com/watch?v=zBvGy34XRUI)

Henry Ölsner · NTT Germany & Christian Miene · 50Hertz

- **Why**: Automation under German critical-infrastructure rules where always-on connectivity is not a given — and the use-case list includes an 802.1X migration (the only identity-adjacent item in the whole program) and MPLS VRF WAN segmentation.
- **What**: A transmission-system operator's journey from unmanaged Python scripts, regex parsing and undocumented cron jobs on a backup server to a platform (DINA) run by a 5-person team: 106,654 workflow executions and 719 sub-process executions, covering CMDB sync, 802.1X migration, MPLS VRF rollout, a DC self-service portal, and VM network provisioning across ~4,000 devices in 6 network zones.
- **How**: The Workflow Definition Document (WDD) is the centerpiece: one formal, auditable contract per use case containing goal/KPI, BPMN workflow, UI design, data models, constraints, and external dependencies — reviewed by stakeholders on a fixed cadence. Platform principles: air-gapped by design, build once/deploy unchanged, develop without live-system access, workload distributed via Django + Celery.
- **Where applicable**: Specific to air-gapped, compliance-heavy critical infrastructure (dependency wheels chains, no GitLab connectivity), but the WDD-as-contract pattern is a strong fit for any change-managed environment, regulated or not.

### Practical Network Reliability Engineering

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20Leadership%20Track/AC5%20-%20John%20Howard%20-%20Practical%20Network%20Reliability%20Engineering.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20Leadership%20Track/AC5%20-%20John%20Howard%20-%20Practical%20Network%20Reliability%20Engineering.pptx) · [Recording](https://www.youtube.com/watch?v=I2thHjtCXzM)

John Howard · Head of Network Infrastructure — Proton AG

- **Why**: Four years of applying NRE (SLI/SLO discipline) to a real network, with outcomes: 10x capacity since 2021, -40% per-port cost, zero extra headcount, zero out-of-hours change windows.
- **What**: A reframing from device health to capabilities and services: a 100G wavelength is a *service*; "packets DC1→DC2 within 8–10ms with N+1 redundancy" is a *capability* — and capabilities map cleanly to SLIs. Notably, "we missed targets early on. That was a feature not a bug — it surfaced which layer needed attention."
- **How**: Design contracts between layers (Edge ↔ Core ↔ Fabric ↔ OOBM) and between network and applications — e.g., apps never exceed 50% of assigned capacity (p99), the network never reduces capacity >50%, anycast instead of VRRP, default-deny VRF egress. SLIs composed in Prometheus recording rules (port state + MACsec CA + IS-IS adjacency + BGP session = DCI health); a gNMIc/NATS/Prometheus/Grafana/Alertmanager stack with Sloth for SLO burn-downs; canary rollouts and auto-isolation for residual risk.
- **Where applicable**: Proton-specific design (EVPN fabrics, MACsec-protected DCI wavelengths), but the capability→SLI method and the bilateral contract framing are generally applicable. Includes a hot take worth arguing with: you cannot be a network engineer and a software engineer concurrently — pick one.

### From Data to Decisions: Real-Time Network Context

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20V%C3%ADctor%20Fern%C3%A1ndez%20-%20From%20Data%20to%20Decisions%3A%20Real%E2%80%91Time%20Network%20Context.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20V%C3%ADctor%20Fern%C3%A1ndez%20-%20From%20Data%20to%20Decisions%3A%20Real%E2%80%91Time%20Network%20Context.pptx) · [Recording](https://www.youtube.com/watch?v=GvZjayObzWQ)

Víctor Fernández · Senior Network & Systems Architect — Colt Technology Services

- **Why**: The data-layer talk that underpins both safer automation and the agentic-AI direction: unifying configs, telemetry, BGP data, service relationships, and change history into one live model.
- **What**: A real-time context platform (ingest → normalize → relate → expose) that answers, when an interface goes down: which services are affected, which customers, whether redundancy exists, and whether there was a recent change. Exposed via API, MCP, and web UI to three consumer types — engineers, automation, and agents.
- **How**: The core scenario: a change in New York and a degradation in Paris — independent events or a hidden dependency? Lessons from applying it at scale: data quality over everything, "same thing, same id" identifiers, relationships expose hidden risks, semantics over links. Framing: "automation scales actions, context speeds up decision-making."
- **Where applicable**: Colt-scale carrier environment; requires serious data-quality discipline first. The MCP exposure makes it a concrete early example of the agent-context plumbing several other talks gesture at.

### NAF Framework — Deep Dive (Parts 1 & 2)

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20NAF%20Framework%20Track/AC5%20-%20Damien%20Garros%20-%20Christian%20Adell%20-%20The%20Network%20Automation%20Map.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20NAF%20Framework%20Track/AC5%20-%20Damien%20Garros%20-%20Christian%20Adell%20-%20The%20Network%20Automation%20Map.pptx) · [Recording](https://www.youtube.com/watch?v=d-kjSJxJVKk)

Christian Adell & Damien Garros · CoreWeave / NAF

- **Why**: The shared vocabulary the rest of the conference keeps mapping to (LINX explicitly, CoreWeave's monitoring talk, the anti-patterns talk). For a PM, it's a vendor-neutral yardstick to assess automation claims against.
- **What**: A tool-agnostic decomposition of any automation system into functional blocks — Intent, Orchestration, Executor, Collector, Observability, Presentation, Infrastructure — each with MUST/SHOULD/MAY capabilities, boundaries, and responsibilities. Explicitly not a protocol or reference architecture; any tool can map to one or more blocks, and you implement only what your use case needs.
- **How**: Worked example: deploy a subnet across 50 mixed-vendor NETCONF branch sites — Infrahub (intent) → AAP (orchestration) → Ansible (executor via NETCONF) → gNMIc/SuzieQ/Kentik (collection) → Prometheus/SuzieQ/Kentik (drift detection) → orchestrated re-run on the failing site → Grafana compliance dashboard, closing a 5→6→3→4→5 remediation loop.
- **Where applicable**: Generally applicable as a vocabulary and scoping tool; no ordering imposed and no requirement for completeness. Useful as the mental model that ties together the LINX, DE-CIX and Colt architectures in this digest.

## Wildcard

### How NetOps Can Embrace AI to Lead Enterprise Innovation

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Chris%20Wade%20-%20Closing%20Keynote%20-%20How%20NetOps%20can%20embrace%20AI%20to%20lead%20innovation.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Chris%20Wade%20-%20Closing%20Keynote%20-%20How%20NetOps%20can%20embrace%20AI%20to%20lead%20innovation.pptx) · [Recording](https://www.youtube.com/watch?v=KmXwu7354os)

Chris Wade · CTO — Itential

- **Why**: The closing keynote and the clearest articulation of where the field believes it's heading: agents, skills, and MCP as complementary layers of an operating model. Vendor vantage point (Itential CTO), so read it as direction-setting rather than deployed practice.
- **What**: Agents decide WHEN (orchestrators with observe→think→act loops), Skills encode HOW (procedural knowledge in ~100-token SKILL.md files — "runbooks turned into agent-consumable procedures"), MCP provides WHAT (a "USB-C for AI" connector to databases, APIs, tools). An honest capability map for 2026: LLMs are strong on protocols, RFCs and general reasoning; weak on vendor specifics behind paywalls, unpublished APIs, and TAC-ticket knowledge.
- **How**: A build/execute/operate arc: build agents doing spec-driven development of deterministic automations (LLMs have vastly more training data for native code than Ansible YAML); centrally-run "execute" agent fleets with tools fixed and limited at build time (a read-only device-health agent literally lacks the tool to change config); and "operate" agents managed by engineers like team members, picking tools at runtime. A worked NOC connectivity-troubleshooting agent shows restricted tools, skills, and policies in action. Notably, customer conversations put AI governance and guardrails above the question of whether agents functionally work.
- **Where applicable**: Vision-stage. The NAF-block framing appears throughout (down to musing "Network Agentic Forum? — can we consider agents as users?"), which is a strong signal the framework intends to absorb the agentic wave.

### Architecting Network Automation with Software Engineering Principles

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Leandro%20Lerena%20-%20Paradigms%20of%20Trust%3A%20Architecting%20Network%20Automation%20with%20Software%20Engineering%20Principles.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%203%20-%20Friday/AC5%20-%20Leandro%20Lerena%20-%20Paradigms%20of%20Trust%3A%20Architecting%20Network%20Automation%20with%20Software%20Engineering%20Principles.pptx) · [Recording](https://www.youtube.com/watch?v=HI1SM9RBLJU)

Leandro Lerena · zebbra AG (per slides)

- **Why**: The most genuinely novel technical idea in the program: applying database-transaction semantics and typed safety profiles to network operations — and deriving a principled safety model for agentic AI from it.
- **What**: A response to scripts reaching their structural limits (no versioning, unknown safety profiles, undetectable race conditions, weak auditability). The replacement: "function blocks" with declared properties (pure / idempotent / reversible), pessimistic locking, and a workflow state machine distinguishing FAILED_SAFE (pure steps only, or rollback succeeded) from FAILED_UNSAFE (side effects may have occurred; resources stay locked to prevent more workflows from touching unknown state).
- **How**: Race conditions are treated as the read-modify-write problem relational databases already solved — a central orchestrator locks context, executes blocks transactionally, rolls back reversible ones, and escalates unsafe ones. Vendor plugins (Cisco IOS via Scrapli, SR Linux via Netmiko, etc.) implement capability interfaces so business logic stays vendor-agnostic; every block is tested against netlab virtual labs via pytest fixtures (remote-lab developer preview on GitHub). The agentic tiers fall out naturally: autonomous read-only agents (pure blocks only), autonomous allow-list (pre-approved idempotent/reversible blocks), and supervised everything else — agents never touch device credentials.
- **Where applicable**: Greenfield framework thinking from a consultancy, not a hyperscaler postmortem — but the safety-tier model is directly reusable by anyone designing the agent-to-network boundary, which this PM will likely have to opine on soon.

### "A Computer Must Never Make a Management Decision." Can We Let AI Run Our Infrastructure?

**Links:** [Slides (PDF)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20Leadership%20Track/AC5%20-%20Marc%20Stadtherr%20-%20%E2%80%9CA%20Computer%20Must%20Never%20Make%20a%20Management%20Decision.%E2%80%9D%20Can%20We%20Let%20AI%20Run%20Our%20Infrastructure%3F.pdf) · [Slides (PPTX)](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon5/Day%202%20-%20Leadership%20Track/AC5%20-%20Marc%20Stadtherr%20-%20%E2%80%9CA%20Computer%20Must%20Never%20Make%20a%20Management%20Decision.%E2%80%9D%20Can%20We%20Let%20AI%20Run%20Our%20Infrastructure%3F.pptx)

Marc Stadtherr · Kumorai Inc.

- **Why**: The governance counterpart to the AI enthusiasm: the binding constraint on safe AI adoption is *systemic legibility* — can your organization even explain what its infrastructure is, who owns it, and what intent governs it? This framing has obvious resonance with identity and ownership models.
- **What**: The claim is we have an "execution surplus and an understanding deficit": more tools, less coherence. Four recurring symptoms — operational drag, fragmented automation, broken governance, and an AI readiness gap — all traced to the same root: no unified model reconciling Source of Truth (what infrastructure should look like) with System of Record (what it looks like now). The proposed fix is an "Infrastructure Intent Control Plane" that renders, encodes, and reconciles both.
- **How**: An advise-versus-act boundary: AI may act only when intent, ownership, and reconciliation are explicit *and continuous*; it must explain itself whenever any of the three is missing. Three grounding scenarios show the failure modes: a 300-site SD-WAN migration stalled on unknown owners and dependencies; an MSP outage with fragmented accountability; a 15k-rule firewall cleanup impossible without explicit intent ("maintain until Q2 decommissioning" vs "delete this rule").
- **Where applicable**: Conceptual, with vendor framing (Kumorai) rather than a deployed system. Still, the 30-second test it implies — can you explain what happens when the AI is wrong? — is a useful gate for any agentic-ops roadmap, and it converges with the supervision tiers in the Lerena talk.

## Themes

- **The data model is the hard part, not the tooling.** DB Systel's two years of IPAM cleanup, Roška's three schema rebuilds, Ørsted's policy-as-code conversion, and LINX's bespoke SoT all say the same thing: pipelines are easy, coherent intent models that survive production contact are the actual work.
- **A shared vocabulary is consolidating.** The NAF functional-block map was invoked across the program (LINX mapped its decade-old architecture onto it; the anti-patterns talk recommends it as the recovery path). Tool-agnostic blocks are becoming the industry's common language for scoping and comparing automation stacks.
- **Testing and guardrails are the new default posture.** netlab's 3,700-lab multi-vendor test matrix, pytest/pyATS pre/post-test layers, 50Hertz's auditable Workflow Definition Documents, DE-CIX's "1 in 3 deploys rejected before production," and Lerena's transactional safety profiles all treat validation as architecture, not afterthought.
- **Observability is becoming the actuator signal.** CoreWeave's monitoring-as-feedback-loop, Colt's real-time context platform, Proton's SLI/SLO composition, and the Kentik self-healing narrative converge on closed loops where telemetry drives orchestrated action — with human gates at the risky end.
- **Agentic ops arrived in the discourse, cautiously.** The closing keynote (agents/skills/MCP), the governance talks (Stadtherr's legibility gate, the "digital intern" framing), and MCP-based context exposure at Colt sketch a supervised, tool-limited, auditable adoption path — nobody credible is proposing unsupervised agents touching devices.
- **Physical fabric and WAN scale is back on the agenda — as automation substrate.** SRv6 at Swisscom, GÉANT's 800G vendor migration, dual-DC EVPN fabrics at Rohde & Schwarz and Roška's project: the automation conversation now spans backbone hardware lifecycle and fabric topology, not just enterprise campus tooling. Notably absent: anything on optics/RDMA specifics, cloud-native dataplanes (eBPF/Cilium), or digital identity beyond 50Hertz's 802.1X migration — none of this PM's deepest specialties had dedicated sessions.
