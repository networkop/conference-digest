<!--
conference: AutoCon 3 (Prague)
type: operator
source_url: https://networkautomation.forum/autocon3
generated: 2026-11-01
registry_key: autocon-3
written_by: ToFaRev (zai-org/GLM-5.3)
-->

# AutoCon 3 (Prague) — Digest

A network-automation operator conference. Little here is directly about DC
fabrics or identity protocols, but a strong subset is: two unusually candid
optical-transport automation stories, a BGP telemetry build, a large-scale
datacenter Terraform migration, EVPN service migration at a global telco, and
several security/identity-flavored automation sessions. The rest is a clear
field-wide shift from "automate operations" toward "design-driven,
durable-execution, trustworthy automation" — worth skimming for where the
networking discipline is heading.

## Core

### From Clicks to Code: Optical Network Automation Journey at GARR

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-MatteoColantonio-OpticalNetworkAutomation.pptx) · [Recording](https://www.youtube.com/watch?v=5ZhNN28xgmo)

Matteo Colantonio, GARR (Italian research and education network)

- **Why**: Physical-layer transport (optical circuits, transponders, ROADMs)
  is the least-automated part of most networks, and this is a rare honest
  account of why the usual automation stack fails there and what actually
  works. Directly relevant to anyone with DC/WAN interconnect
  responsibilities.
- **What**: GARR's progression from Ansible/AWX and the vendor controller's
  northbound API to a workflow-orchestrator architecture that talks directly to
  optical devices, now in early production use.
- **How**: Ansible handled basic transponder upgrades but collapsed on complex
  logic — restarting cards one-by-one and verifying service recovery required
  three nested YAMLs with `include` statements. The vendor controller API was a
  stripped-down version of the GUI: missing key features, and useless for
  circuits crossing multiple line systems (mixed-platform ROADM metro regions).
  The pivot: build abstract service models plus Python clients speaking the
  same southbound interfaces the vendor controller uses (RESTCONF, TL1 shell
  for ROADMs), separating intent from device-specific configuration.
- **Where applicable**: GARR-specific in topology (research backbone, mixed
  optical platforms), but the lessons — vendor NBIs as a bottleneck, direct
  device control, incremental automation starting with critical services —
  transfer to any optical/WAN environment. The observation that optical
  networks' GUI-centric (not CLI-centric) history changes the automation
  starting point is a genuinely useful framing.

### Coding for infrastructure is just coding, on how we moved from a script based model to an object oriented architecture

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day1_Wednesday_28May/AC3-AntonioBalmaseda-AlbertoVillegasErce-ObjectOriented.pptx) · [Recording](https://www.youtube.com/watch?v=rtzYbAPlkAs)

Antonio Balmaseda & Alberto Villegas Erce, Roche

- **Why**: The second of two talks at this conference independently reaching
  the same conclusion about optical automation (Roche's optical network uses
  the same devices as ESnet and GEANT). Together they read as a mini-postmortem
  of Ansible-and-controller-based approaches to transport automation.
- **What**: Roche Pharma's move from scattered per-engineer scripts and
  Ansible playbooks to an object-oriented, model/controller/view architecture
  built on the Workflow Orchestrator framework, expected in production by the
  conference date.
- **How**: Abstract service models with Python clients talking directly to
  devices (RESTCONF, TL1 for ROADMs); hardware changes only require adding
  implementations via Python single-dispatch, giving clean boundaries between
  abstract intent and device config. Concrete results from the slides: 6000
  backups in 20 minutes (down from 3 hours), and 200 devices patched
  unattended over a weekend with no CLI access. Massive changes now ship as a
  JSON file plus Jinja templates through a merge request.
- **Where applicable**: Roche-specific scale (worldwide multi-vendor network,
  thousands of devices), but the pattern — abandon YAML-nesting for real code
  when logic gets complex, keep Ansible only for what it's good at (backups,
  compliance, OS upgrades) — is broadly applicable.

### Going beyond show commands and screen scraping with BMP

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-BartDorlandt-BMP.pptx) · [Recording](https://www.youtube.com/watch?v=MgK2YSfTvD8)

Bart Dorlandt (freelance network automation engineer, Netherlands)

- **Why**: Verifying that BGP announcements you configured actually propagated
  and passed import policy is a classic gap; most shops do it with screen
  scraping. BMP (BGP Monitoring Protocol) is the right tool and this gives the
  architecture and the scaling numbers.
- **What**: A production pipeline for pre- and post-policy BGP data: router →
  BMP collector → Kafka → consumer → database → API, replacing screen scraping
  of `show` commands for customer-facing verification.
- **How**: The initial consumer managed 30 msg/sec — nowhere near enough for
  millions of RIB entries — and was rewritten with a pool of async Kafka
  producers, reaching 45,000 msg/sec. Hard lessons: every stage (collector,
  consumer, DB) can be crippled by too much data, so filter early, deduplicate,
  and decide what you actually need; peer-down notifications are the critical
  code path; the BMP collector implementation used was incomplete and needed
  patches (Kafka TLS, Docker).
- **Where applicable**: Broadly applicable wherever BGP policy correctness
  needs verification (peering, DC fabrics, WAN). The pipeline is
  buildable from open components but the scaling numbers are one
  implementation's — treat 30→45k msg/sec as directional, not a benchmark.

### The Road to EVPN: Automated Service Migrations

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-LukeGollan-AutomatedServiceMigrations.pptx) · [Recording](https://www.youtube.com/watch?v=dyeclGDa6yU)

Luke Gollan, Megaport

- **Why**: Migrating a live global network to EVPN with automated service
  cutover is squarely in the PM's EVPN/BGP and interconnect territory, and this
  covers the whole arc: architecture, config rollout, then customer service
  migration with minimal disruption.
- **What**: Megaport's end-to-end story of automated EVPN deployment across a
  global telco network, from design through rollout to migrating production
  services, plus customer/support-facing migration tooling.
- **How**: Object-driven database generating device configs; NETCONF
  operations to configure, log, and track changes; diversity zones to contain
  blast radius; APIs and message queuing to trigger migrations; explicit
  phased migration steps with rehearsed rollback; tooling to track network
  changes and keep business stakeholders informed. (From abstract only —
  no usable source text.)
- **Where applicable**: Megaport-specific (global NaaS/telco topology, dense
  service inventory), but the checklist — rehearsed rollback, diversity
  zones, event-driven migration triggers, stakeholder-visible risk — is a
  transferable migration methodology for any EVPN or fabric migration.

### An Epic Journey: Automating networks with Terraform

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-EduardoPozo-Terraform.pptx) · [Recording](https://www.youtube.com/watch?v=xlacAhxHQgM)

Eduardo Pozo

- **Why**: A concrete, numbers-backed account of Terraform at datacenter
  scale — including where it hurts (provider bugs, plan times, state risks) —
  which is rare and directly useful for DC automation decisions.
- **What**: Using Terraform as the primary automation tool across oil, health,
  and enterprise projects, including migrating a large multi-site datacenter to
  fully automated deployment.
- **How**: The slides quantify the pain: a 500+ leaf, 4-location, 2000+ VLAN
  fabric; a full `terraform plan` against an empty APIC (Cisco ACI, ~5334
  resources) took 45 minutes, cut to 19 minutes by moving data transformation
  (dedups via `set()`, key lookups, validation) out of Terraform into Python.
  Honest coverage of vendor provider reality: "vendors say yes yes, it just
  doesn't work," API bugs, 12+ month-old issues, no CRUD — and the mitigations
  (contribute, pressure the vendor, hybrid approach, fork the provider).
  Also state loss/locking, apply-can-destroy surprises driven by provider
  quality, and preferring pipelines straight to infrastructure over
  controller-mediated paths where possible.
- **Where applicable**: The specific numbers are ACI/APIC-specific, but the
  lessons (stateful tools at DC scale, controller API limits vs. parallelism,
  keeping computation out of your IaC layer) apply to any large fabric
  automation effort.

### Using a SONiC Abstraction API (for fun and profit)

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-JoshSaul-SONiC.pptx) · [Recording](https://www.youtube.com/watch?v=Mf6uLZZtwFs)

Josh Saul

- **Why**: SONiC fragmentation across distributions is a real operational
  problem for multi-vendor cloud and AI infrastructure provisioning — and
  AI-cluster fabric provisioning is exactly where this is biting hardest right
  now.
- **What**: A demonstration of how traditional IaC tools can drive
  abstractions that generate actual device configurations across multiple
  SONiC platforms, instead of writing per-flavor configs.
- **How**: An abstraction layer over multiple SONiC flavors, with configs
  pushed via gNMI and (where necessary) SNMP/CLI paths. (From abstract only —
  no usable source text, and it's a lightning talk, so expect a demo rather
  than deep architecture detail.)
- **Where applicable**: Directly relevant to anyone operating or evaluating
  SONiC-based DC fabrics with mixed distributions/vendors; less relevant if
  you're on a single NOS distribution.

### Pls stop exposing your... secrets

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-JohnHoward-DontExposeYourSecrets.pptx) · [Recording](https://www.youtube.com/watch?v=-_qMVdsOq8g)

John Howard

- **Why**: Hard-coded credentials and `verify=False` on REST calls are endemic
  in network automation code, and the automation toolchain itself becomes an
  attack surface — squarely a network-security concern for the PM.
- **What**: A fast tour of HashiCorp Vault's built-in secret engines, showing
  a PoC instance that removes hard-coded creds from automation scripts at
  team scale.
- **How**: Standing up a Vault PoC and using a couple of its built-in engines
  to centralize secrets consumed by automation pipelines, addressing both the
  accidental-exposure problem and the DevSecOps friction it causes. (From
  abstract only — lightning-talk depth.)
- **Where applicable**: Broadly applicable; this is a generic, adoptable
  pattern rather than an org-specific one. Watch for the usual caveat that
  Vault itself becomes Tier-0 infrastructure your automation now depends on.

### Automation Transforms $70 APs into Enterprise-Grade Networks

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-HenryHaller-70dollarAPs.pptx) · [Recording](https://www.youtube.com/watch?v=vVrjvB6QTYQ)

Henry Haller, Telecom Infrastructure Project (TIP) OpenWiFi

- **Why**: Under the WLAN packaging, this is one of the few sessions about
  device identity at fleet scale — per-device certificate generation, CA
  signing, and mutual TLS between controller and devices, i.e., the bootstrapping
  problem familiar from SPIFFE/SPIRE workload identity, applied to hardware.
- **What**: An open-source lifecycle system (TIP OpenWiFi) that takes
  commodity $70 access points from zero-touch adoption to provisioned
  enterprise WLANs, covering WPA2/3, PSK/mPSK-RADIUS, OWE, GRE tunneling, and
  multi-band configs.
- **How**: WAPs generate SSL certificates on adoption and submit them to a CA
  for signing; the certificates then authenticate the devices to the OpenWiFi
  Gateway via mutual TLS, creating a web of trust, with CA management included.
  Provisioning is driven by operator intent via JSON API transactions to the
  gateway and WebSocket transactions from gateway to APs. The source slides
  add operational lessons: immediate UI feedback and robust logging/error
  reporting matter because end-user feedback arrives late and through many
  layers.
- **Where applicable**: The software is TIP OpenWiFi-specific, but the
  onboarding pattern — device-generated keys, CA signing, mTLS control
  channel — is the template for any commodity-hardware fleet (including
  cameras, sensors, and DC out-of-band gear).

## Adjacent

### Start at the Beginning; Automating Network Design

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day1_Wednesday_28May/AC3-OpeningKeynote-ClaudiaDeLuna-StartAtTheBeginning.pptx) · [Recording](https://www.youtube.com/watch?v=PoQUA3dgmkQ)

Claudia de Luna (Opening Keynote)

- **Why**: This sets the thesis the rest of the conference keeps echoing:
  automation's next bottleneck is upstream of operations, in design. If the
  PM's teams produce monolithic diagrams and Word documents, this names the
  problem precisely.
- **What**: An argument that the fixation on "source of truth" is a symptom of
  starting midstream; the real anchor is programmatically consumable design
  data — patterns, data models, structured data — from which diagrams,
  documentation, configurations, and build guides all derive.
- **How**: Conceptual keynote, not an implementation: reframe design artifacts
  as structured data that everything else flows from, and spotlight existing
  work in that direction. (From abstract only.)
- **Where applicable**: Universal framing; pairs naturally with the
  Design-Driven Automation and Abstraction talks below.

### Building Trustworthy Network Automation, From Principles to Practice

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-DamienGarros-TrustworthyNetworkAutomation.pptx) · [Recording](https://www.youtube.com/watch?v=G3XqT-UhQ6Q)

Damien Garros

- **Why**: The trust problem is why automation adoption stalls — teams don't
  delegate critical network operations to systems whose failure behavior they
  can't predict. This is the cleanest principles-to-patterns treatment at the
  conference.
- **What**: A framework of design principles that make automation
  trustworthy, explicitly "built on mistakes, refined by experience":
  idempotency, dry-run, transactional commit/rollback, declarative over
  imperative workflows, version control, and testing.
- **How**: The slides include a useful comparison table: imperative workflows
  make idempotency, dry-run, and transactionality *hard*; declarative makes
  them easy; version control gives all three nearly free. Patterns shown:
  dry-run before apply, diff-based changes, state verification, grouping
  changes so they either all commit or all roll back, plus process advice
  (enforce business process in workflows, safe defaults, "integrate what you
  can, build what you must").
- **Where applicable**: Broadly applicable, tool-agnostic; these principles map
  onto any automation stack (Nornir, Ansible, Terraform, orchestrators).

### Transforming Network Automation with Temporal

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-NaveenAchyuta-Temporal.pptx) · [Recording](https://www.youtube.com/watch?v=1PqbtACGW80)

Naveen Achyuta

- **Why**: Durable-execution workflow engines are how other industries solved
  long-running, failure-prone, stateful orchestration — exactly what network
  change automation is. Temporal is underused in networking and this is a
  solid architectural introduction.
- **What**: An introduction of Temporal to network automation: architecture,
  why durable execution fits network use cases (provisioning, config
  management, automated remediation, human-in-the-loop), and how it compares
  to what teams hand-roll today.
- **How**: Tasks are ordinary code ("activities") whose state is persisted by
  the Temporal service (history service shards, matching service task
  queues, distributed workers) — workflows are guaranteed to run to
  completion, resuming where they left off after failures, with built-in
  tracing and audit trails. The slides show a practical trigger path
  (NetBox webhook → workflow) and per-step timing for optimization, plus a
  GitHub starter repo. Explicit caveat given: don't use it for simple tasks;
  it earns its keep at scale and resiliency requirements.
- **Where applicable**: General-purpose; the main adoption constraint is
  running another stateful service well, which small teams may find heavy.

### Mastering Network Operations: The Power of Abstraction

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-JaakkoRautanen-ThePowerOfAbstraction.pptx) · [Recording](https://www.youtube.com/watch?v=gDBvYY6pBng)

Jaakko Rautanen

- **Why**: The concrete "how do I actually build abstract services" talk the
  design-first theme needs — with a working production stack, an open-sourced
  plugin, and a demo that goes from three inputs to deployed MPLS L3VPN
  service.
- **What**: A layered automation stack in which NetBox-native data is
  detailed state, and a new top layer of "abstract services" (NetBox plugins)
  collapses daily operations to a handful of variables per service.
- **How**: An example "Virtual Network" service (VRF + customer MPLS-site
  attachments) needs dozens of correctly-allocated details (prefixes, VLANs,
  loopbacks, route-targets, ASNs); the abstract model reduces user input to
  name, template, and site attachment, with all other values allocated
  automatically from template-defined ranges. Config delivery uses NetBox
  Config Templates (Jinja), deployment varies by vendor, and a diff view
  against live state precedes a one-click push. The team open-sourced the
  Ninja NetBox plugin for generating interactive diagrams or any text output
  from Jinja. Lessons: purge arbitrary encoding rules from IP/VLAN schemes,
  go declarative (they replace entire device configs each push), keep models
  generic with templates.
- **Where applicable**: The implementation is a media-network MPLS/VPN
  environment, but the pattern (service abstraction layer over NetBox,
  template-driven allocation, full-config declarative pushes) is directly
  adoptable by anyone already running NetBox.

### The Why, What, and How about Design-Driven Automation

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-ChristianAdell-DesignDrivenAutomation.pptx) · [Recording](https://www.youtube.com/watch?v=0sQPqpohEuo)

Christian Adell Querol, Network to Code

- **Why**: The most concrete instantiation of the keynote's thesis: treat
  design as executable, versioned, decommissionable data rather than
  documentation. Includes a working open-source implementation.
- **What**: A framework where a network service catalog (minimal validated
  inputs + template logic + external context) drives a PLAN, a builder
  creates tracked/connected/rollbackable data, and that service data becomes
  the single reference for orchestration, automation (Nornir/Ansible/Terraform
  engines), and observability.
- **How**: Demonstrated with Nautobot's Design Builder (which the speaker
  contributes to): a PoP deployment created from just name + size with
  architectural validation; a second design creating a VRF, prefix from a pool,
  and a cable; design updates that understand what changes (prefix preserved,
  cable re-pointed); clean decommissioning reverting created objects; and
  every change tracked as a commit. Key argument: test the design, not just
  the implementation — if the design is deterministic, deployments don't need
  per-instance review, the way nobody reviews a PR when someone launches a
  VPC.
- **Where applicable**: The demo is Nautobot-specific, but the concepts
  (minimal input, design-as-data, traceable provenance, dry-run, full
  lifecycle through decommission) port to other SoT platforms. Speaker is
  vendor-affiliated (Network to Code) yet the talk is substantially
  technique-first.

### Taking Automation to next level: Drive your network with Microservices

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day1_Wednesday_28May/AC3-ShirishBasantRai-Microservices.pptx) · [Recording](https://www.youtube.com/watch?v=ab0QTB7xTOk)

Shirish Basant Rai, Colt Technology

- **Why**: Colt is a real carrier doing event-driven microservices for network
  automation aligned to TMF ODA NaaS standards — a useful signal of where
  operator automation architectures (and NaaS standardization) are heading.
- **What**: Colt's evolution from a simple workflow-engine architecture to an
  event-driven microservices model, and how that architecture naturally
  aligned with TMF ODA NaaS.
- **How**: Separation of concerns into microservices, asynchronous workflow
  and service-orchestration complexity hidden from consumers, code promotion
  without service disruption, and faster development cycles. (From abstract
  only — no usable source text, so expect architecture philosophy rather than
  deployment detail.)
- **Where applicable**: Colt-specific scale (global carrier, NaaS ambitions);
  the microservices event-driven pattern is heavy machinery for smaller
  estates, but the TMF ODA alignment angle matters to anyone selling or
  consuming NaaS-style interconnect.

### A Marathon and Not a Sprint: Lessons Learnt from Trying (and sometimes succeeding!) to Automate Enterprise Campus Networks

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day1_Wednesday_28May/AC3-RobertMertlingBlake-CampusNetworkAutomation.pptx) · [Recording](https://www.youtube.com/watch?v=1k-3oECPaK8)

Robert Mertling-Blake, AEG (entertainment venues worldwide)

- **Why**: An unusually honest "we are not fully automated and here's why"
  operator story — the failure-mode content the operator-program criteria
  ask for, with lessons that transfer even to non-campus environments.
- **What**: AEG's journey automating campus networks across 100+ venues
  (>800 switches, thousands of APs), including the drivers, failures, and
  what finally worked.
- **How**: Key lessons from the slides: assurance matters more than
  self-healing when the event must work (their golden rule); DCIM cable
  documentation at remote/unmanned sites dramatically improved remote-hands
  resolution; "source of record" framing gets buy-in where "source of truth"
  evangelism doesn't; doing automation perfectly became the enemy of doing
  any automation (a rushed greenfield deployment without physical
  connectivity or PNP time); buy the SoR-driven process wins — NetBox-driven
  config generation, Oxidized backups, monitoring and DDI creation that
  manual SOPs always missed. They deliberately keep DDI changes
  non-event-driven while tooling confidence grows, and deploy sacrificial
  old kit during construction to eat the dust.
- **Where applicable**: Campus/venue-specific in details, but the meta-lessons
  (pick fewer battles, alignment with site refreshes, data quality as the
  persistent constraint) transfer to any heterogeneous multi-site estate.

## Wildcard

### Teaching "old" LLMs new tricks

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day3_Friday_30May/AC3-UrsBaumann-TeachingLLMs.pptx) · [Recording](https://www.youtube.com/watch?v=X073YnquOho)

Urs Baumann

- **Why**: Not about networking per se, but a signal of where network
  automation tooling is heading: specialized models fine-tuned for automation
  tasks. Worth a look even for a skeptic of LLM-for-netops.
- **What**: A method for making general-purpose LLMs accurate on specialized
  network automation tasks without datacenter-scale training budgets, plus a
  practical fine-tuning pipeline.
- **How**: LoRA (Low-Rank Adaptation) fine-tuning — adding small trainable
  weight matrices to a frozen base model — which sharply reduces the compute
  needed to specialize an LLM, applied to network-automation tasks. (From
  abstract only — the slide text didn't extract.)
- **Where applicable**: The technique is general; the constraint is having a
  task set worth fine-tuning for and the discipline to evaluate accuracy
  claims honestly. Interesting more as a direction than a deployable today.

### Network Event Correlation. Stories to keep you awake

**Links:** [Slides](https://media.githubusercontent.com/media/Network-Automation-Forum/handyinfo/main/docs/autocon_coverage/slides/AutoCon3/Day2_Thursday_29May/AC3-JavierAntich-Correlation.pptx) · [Recording](https://www.youtube.com/watch?v=FaCafKfnQ_4)

Javier Antich

- **Why**: A refreshingly blunt "why event correlation mostly doesn't work"
  talk, with a taxonomy of where rules end and ML/neuro-symbolic approaches
  begin — relevant to anyone drowning in NOC alert noise.
- **What**: An honest dissection of operational noise-reduction approaches —
  what correlation can and cannot do today, war stories, and a proposal for
  doing better.
- **How**: The slides frame correlation as static rules (e.g., link_down +
  OSPF_Down on same device/interface → correlated) over normalized inventory
  data, and lay out a two-column map of automation vs. autonomy across
  operations: static thresholds → ML goal-deviation tracking, rules-based
  correlation → neuro-symbolic AI, rules-based closed-loop and compliance →
  goal-driven autonomous agents.
- **Where applicable**: Tool-agnostic and broadly relevant; the AI/autonomy
  roadmap is a vendor-independent framework, though the neuro-symbolic claims
  are forward-looking rather than shipped.

## Themes

- **Design is the new frontier**: The opening keynote, the abstraction talk,
  and Design-Driven Automation all argue the same thing — the next unlock is
  programmatically consumable design data (patterns, models, templates)
  upstream of operations, not better ops tooling. "Source of truth" is being
  reframed as "source of record" derived from design.
- **The Ansible/controller ceiling, twice over**: GARR and Roche hit
  independently identical walls (no idempotent modules, YAML-nesting for
  complex logic, vendor NBIs missing features) and converged on the same
  answer: real code, abstract service models, and direct device protocols
  (RESTCONF/TL1). The packet world's playbook is being rewritten for optical.
- **Durable execution enters networking**: Temporal, event-driven
  microservices at Colt, and workflow orchestrators at two research/pharma
  networks point to workflow-engine state management replacing fragile
  home-grown orchestration.
- **Trustworthiness as an engineering discipline**: Idempotency, dry-run,
  transactional rollback, and declarative models presented as a comparable
  decision matrix (declarative makes all of them easy) — adoption framed as a
  trust problem, not a tooling problem.
- **Identity and security are quietly infiltrating network automation**:
  mTLS device onboarding with per-device certificates in TIP OpenWiFi, Vault
  for automation secrets, and BMP-based verification of BGP policy —
  automated fleets are becoming PKI- and secrets-managed systems whether or
  not teams planned for it.
- **AI is present but early**: LLM fine-tuning via LoRA and neuro-symbolic
  event correlation are directionally interesting; both talks are honest that
  these are pipelines and proposals rather than proven practice.
