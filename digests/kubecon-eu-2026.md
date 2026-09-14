<!--
conference: KubeCon + CloudNativeCon Europe 2026
type: vendor
source_url: https://kccnceu2026.sched.com/list/descriptions/
generated: 2026-09-14
registry_key: kubecon-eu-2026
-->

# KubeCon + CloudNativeCon Europe 2026 — Digest

23 picks from a 569-session program (Amsterdam, 22–27 March 2026).

*Sourcing note: the Sched program exposes titles, speakers and descriptions but no
paper, slide or recording links, so every write-up below is from the session
abstract only and no links are given. Where an abstract promises a demo or
numbers without stating them, that is called out rather than guessed at.*

## Core

### Multi-Network Step-by-Step: Enabling SR-IOV Support From Kubernetes Network (DRA) Drivers

*Masaharu Kanda, NTT, Inc. & Lionel Jouin, Red Hat*

- **Why**: This is the session where physical NICs stop being a bolt-on. Multus has
  been the de facto answer for multi-network pods for years, and it sits beside
  Kubernetes rather than inside it. SIG-Network is replacing that with a first-class
  path, and if it lands, the way you attach a VF to a pod changes.
- **What**: Official multi-network support in Kubernetes built on Dynamic Resource
  Allocation and a new `PodNetwork` resource, with the CNI DRA Driver as the
  reference implementation bridging DRA and CNI.
- **How**: NIC allocation and management move into the DRA machinery instead of
  annotation-driven side channels. The claimed payoff is transparent NIC usage
  visibility and fine-grained control — the specific example given is bandwidth
  allocation per Virtual Function of a physical NIC.
- **Where applicable**: Aimed squarely at high-bandwidth AI/ML, telco and HPC
  workloads — anywhere you are already running SR-IOV. Broadly applicable in
  principle, but this is upstream work in motion: treat it as the direction of
  travel and check what has actually merged before planning against it.

### Kubernetes Network Driver Unpacked: Modularity, Trade-offs and the Road Ahead

*Lionel Jouin & Sebastian Scheinkman, Red Hat; Antonio Ojea, Google; Sunyanan Choochotkaew, IBM*

- **Why**: The companion strategy session to the SR-IOV talk, and the more important
  one for anyone deciding where to place bets. The people building the competing
  implementations are on one panel arguing about the shape of the ecosystem.
- **What**: A panel across several Kubernetes Network (DRA) Drivers — the
  CNI-DRA-Driver and DraNet named explicitly — on how DRA is reshaping Kubernetes
  networking into modular, composable components.
- **How**: The central trade-off is stated plainly: one single complete network
  driver versus an ecosystem of smaller purpose-built ones. Secondary axes are
  balancing imperative against declarative models, and keeping simplicity while
  staying extensible.
- **Where applicable**: Vendor- and operator-facing rather than hands-on. Most
  valuable if you are choosing a CNI strategy for the next few years, since the
  answer determines whether interoperability across projects is realistic.

### The Latest in GPU, TPU, NIC and Other Device Support — WG Device Management

*John Belamaric, Google & Patrick Ohly, Intel*

- **Why**: DRA is the substrate under both talks above, and this is its status
  report from the working-group co-chairs. NICs are named as a first-class device
  type alongside GPUs and TPUs, which is the part that matters for fabric work.
- **What**: DRA reached General Availability in 1.34; this covers what shipped in
  1.35 and what is targeted for 1.36.
- **How**: The named post-GA workstreams are managing device failures, groups of
  devices that work together *across nodes*, and controlled sharing of devices.
  Cross-node device groups are the notable one — that is a topology-aware
  allocation problem, not a node-local one.
- **Where applicable**: Anyone on 1.34+. The cross-node grouping work is most
  relevant if you are building multi-node accelerator or NIC pools.

### Bridging Islands: EVPN Overlays for Multi-Cluster KubeVirt

*Miguel Duarte, Red Hat* — Cloud Native Theater | KubeVirt Summit

- **Why**: Real datacenter networking at a Kubernetes conference. BGP-EVPN, VXLAN
  and VRFs applied to the stretched-L2 problem, rather than another overlay
  reinvented in userspace.
- **What**: An integration of OpenPERouter giving EVPN-based VXLAN overlays so
  Layer 2 stretches transparently between clusters, keeping VM MAC/IP consistent
  across migration and disaster recovery.
- **How**: Declarative APIs over a dynamic BGP-EVPN control plane. Two consequences
  worth noting: deterministic cross-cluster live migration, and VRF-aware overlays
  that provide direct routed ingress to VMs — removing the need to expose ports
  through Kubernetes Services at all.
- **Where applicable**: Multi-site KubeVirt estates, and legacy workloads that
  genuinely need broadcast/multicast. Assumes you can run BGP-EVPN between sites,
  so this is for operators who control the underlay — not a public-cloud pattern.

### Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery to Simulation at Scale

*Weizhou Lan, Daocloud*

- **Why**: Names the physical fabric explicitly — scale-up interconnect *and* RDMA
  spine–leaf — as the thing the scheduler has to understand. This is where DC
  topology and Kubernetes scheduling actually meet.
- **What**: A practical approach to multi-level topology discovery feeding
  topology-aware scheduling in Kueue, plus a way to validate it without buying the
  hardware.
- **How**: Three stated parts: dynamic topology discovery and health detection
  across scale-up, RDMA spine and RDMA leaf layers; topology-aware scheduling with
  priority-based placement so GPUs get optimal communication paths; and Kwok
  simulating thousands of virtual nodes with multi-level topologies for
  zero-hardware-cost validation at scale.
- **Where applicable**: Multi-tenant AI inference clusters with heterogeneous GPU
  interconnect. The Kwok simulation trick generalizes to any large-topology
  scheduling validation, independent of the GPU specifics.

### Gateway API: Bridging the Gap from Ingress to the Future

*Nick Young & James Strong, Isovalent at Cisco; Katarzyna Łach & Rostislav Bobrovsky, Google; Norwin Schnyder, Airlock*

- **Why**: ingress-nginx is being archived, and that is pushing a large population
  of Ingress users toward Gateway API on a deadline. This session is about the
  friction of that migration specifically.
- **What**: Six months of Gateway API changes plus upcoming features, framed around
  the incoming Ingress refugees.
- **How**: The concrete items are the `ingress2gateway` migration tool, better
  integration with cert-manager and external-dns, improvements to TLS handling, and
  `ListenerSet` moving to Standard — the last intended to give Ingress users a
  familiar experience while keeping Gateway API's stronger security model.
- **Where applicable**: Anyone still on Ingress, which is still most people. The
  migration tooling is generic; how much you gain depends on which implementation
  you land on — see the next pick.

### Navigating the Gateway API Maze: 40+ Implementations, 55+ Features, and a Path to Portability

*Beka Modebadze, Google & Christine Kim, Isovalent at Cisco*

- **Why**: The honest counterweight to the previous talk. "Use Gateway API" is not
  a decision; 40+ implementations and 55+ features is a procurement problem, and
  feature support varies enough that portability is a claim worth testing.
- **What**: Tooling and a method for picking an implementation, plus what
  "supports a feature" actually guarantees.
- **How**: A new set of tools to discover and compare implementations by feature
  name, and an examination of how the conformance test suite underwrites
  portability — including how to tell whether features you already depend on are
  genuinely supported by your implementation.
- **Where applicable**: Directly useful to anyone selecting or auditing a Gateway
  API implementation. Vendor-neutral by construction, though both speakers work for
  implementers.

### When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infrastructure

*Yong Tang, Ivanti & John Belamaric, Google*

- **Why**: Framed against the recent DNS disruptions at major cloud providers. The
  argument is that DNS is critical infrastructure and brief degradation cascades —
  which is exactly the failure mode that makes DNS a networking problem rather than
  an application one.
- **What**: How CoreDNS is evolving for large-scale critical environments, covering
  both scale and security.
- **How**: New CoreDNS plugins that improve multi-core scalability and reduce
  contention under high query load; operational lessons on tuning, deployment
  patterns and limiting blast radius during failure. The security half covers
  spoofing, cache abuse and amplification attacks, reviews recently fixed CoreDNS
  vulnerabilities, and gives hardening strategies.
- **Where applicable**: Any cluster running CoreDNS at load, which is nearly all of
  them. The contention work matters most on high-core-count nodes.

### Smart Routing at Scale: How Spotify's xDS Control Plane Cut 75% of Cross-Zone Traffic

*Yannick Epstein & Anya Hristova, Spotify*

- **Why**: One of the few talks in the program with a hard, sustained production
  number attached to a specific architecture. Cross-zone traffic cost is a
  universal tax on multi-AZ deployment, and this quantifies what closing the
  control loop is worth.
- **What**: A sustained 75% reduction in cross-zone traffic across Spotify's compute
  infrastructure, stated as achieved without impacting reliability.
- **How**: They extended an in-house xDS control plane to do dynamic, data-driven
  zone-aware routing across a proxyless service mesh spanning two million nodes.
  The mechanism is Envoy's routing principles combined with real-time load
  telemetry: the control plane continuously recalculates optimal per-zone weights
  and pushes routing state in real time. The stated contrast is with their previous
  client-side routing, which optimized on each service's limited local view and so
  could not optimize globally.
- **Where applicable**: Spotify-specific in implementation — in-house control plane,
  proxyless mesh, two million nodes — but the speakers claim the design principles
  generalize to any large-scale mesh trading cost against availability, and the
  local-view-versus-global-view argument clearly does.

### From NLB Sprawl to Mesh Efficiency: How Skyscanner Handles 60M Requests Per Minute With Istio

*John Clark, Skyscanner & Steven Thwaites, Solo.io*

- **Why**: The other cost-with-numbers talk, from the opposite direction: removing
  load balancers rather than routing around them. Also a rare case study that says
  what it gave up, not just what it saved.
- **What**: A network rebuild across dozens of clusters at >60M req/min, saving
  "millions" on AWS while preserving resilience and compliance.
- **How**: Four changes: east-west NLBs removed in favour of pod-to-pod multicluster
  traffic; gateways added for controlled ingress/egress while using Spot instances;
  Istio Ambient Mesh deployed for zero-trust without sidecars; OpenTelemetry-based
  observability built alongside. The abstract is unusually candid about the risks —
  NLB sprawl, multicluster operational drag, sidecar overhead, coordinated rollout
  across many clusters, and holding peak-time performance while shifting traffic.
- **Where applicable**: AWS-specific in its cost model (NLB pricing is what makes
  the arithmetic work), but the ambient-mesh and multicluster patterns are general.
  Most relevant if you are running many clusters with east-west load balancers
  between them.

### WIT Happens: Exploring the Latest Evolution of the SPIFFE and WIMSE Workload Identity Standards

*Noah Stride, Teleport & Arndt Schwenkschuster, Defakto Security*

- **Why**: A concrete standards milestone rather than a survey: the IETF WIMSE
  Working Group's Workload Identity Token is being adopted natively by SPIFFE and
  SPIRE in 2026. If you have a workload identity strategy, this changes the
  credential menu.
- **What**: What WIT is and how it differs from the credential types SPIFFE already
  issues, with SPIFFE/WIMSE context for how the two efforts fit together.
- **How**: A recap of the existing JWT and X.509 SVID types, then WIT's structure,
  security properties and presentation methods, compared directly against both. The
  abstract hedges on a demo of workload-to-workload authentication with WIT
  ("with any luck"), so treat that as unconfirmed.
- **Where applicable**: Anyone running SPIRE or planning workload identity.
  Standards-track work, so vendor-neutral, but adoption timing is the open question.

### From Static Tokens to Attestation: The Evolution of Secure Node Joining

*Ciprian Hacman & Jack Francis, Microsoft; Michael McCune & Josephine Pfeiffer, Red Hat; Justin Santa Barbara, Google*

- **Why**: The framing is the right one: when Karpenter creates capacity in seconds
  and users plug custom nodes into managed control planes, "if the kubelet
  connects, it's in" is no longer a defensible trust model. This is the identity
  problem at the infrastructure layer.
- **What**: A cross-vendor panel — kOps and Cluster API maintainers plus engineers
  from the major cloud providers — on how node joining works today and how it
  should work.
- **How**: The stated scope is defining a root of trust, validating node identities
  with metadata and attestation, locking down CSR approval, binding joins to
  declarative objects, and post-join controls to limit privilege creep —
  NodeRestriction, scoped RBAC, admission, and drift detection.
- **Where applicable**: Broadly applicable, and unusually so for a security talk:
  the panel spans kOps, Cluster API and the managed offerings, so the answers should
  not be single-vendor. Most urgent for anyone letting nodes join from outside their
  own provisioning path.

## Adjacent

### SIG Network: The State of Networking for AI on Kubernetes

*David Martin, Red Hat; Haiyan Meng, Bowei Du & Kellen Swain, Google; Nadia Pinaeva, NVIDIA*

- **Why**: The best single session for mapping where upstream networking effort is
  actually going, from the people setting the agenda. Also stakes out a position
  worth hearing argued: which parts of "AI networking" are just networking.
- **What**: A presentation-plus-panel covering SIG Network's AI-driven work, from
  Gateway API through the Gateway API Inference Extension to networking for agentic
  systems.
- **How**: Highlights and key projects first, then guided discussion and audience
  questions. Explicitly includes the claim that AI networking is in large part
  ordinary networking, with specific exceptions.
- **Where applicable**: Roadmap-level rather than implementable. Useful for
  anticipating what lands upstream over the next few releases.

### SPIFFE Meets OAuth: Federated Identity for Cloud Native Workloads

*Yoshiyuki Tabata, Hitachi, Ltd.*

- **Why**: Addresses the multi-hop authorization problem across trust domains, which
  is where mTLS-only designs tend to run out of road. Cites specific drafts and RFCs
  rather than gesturing at "zero trust".
- **What**: Federated identity patterns combining SPIFFE with emerging OAuth
  extensions, for propagating identity and authorization across trust domains.
- **How**: SPIFFE JWT-SVID plus OAuth Identity Chaining
  (`draft-ietf-oauth-identity-chaining`) and the Assertion Framework (RFC 7521 /
  7523), enabling multi-hop authorization and identity propagation without relying
  solely on mTLS. Demo integrates Keycloak, SPIRE and OAuth flows.
- **Where applicable**: Multi-cluster and multi-trust-domain estates. General
  technique built on public standards; the demo stack is one instantiation.

### When an Agent Acts on Your Behalf, Who Holds the Keys?

*Mariusz Sabath & Maia Iyer, IBM Research*

- **Why**: The delegation problem stated precisely — when an agent commits code or
  triggers a workload, static API keys cannot express who actually authorized it,
  which makes both fine-grained authorization and audit impossible. That is an
  identity architecture question, not an AI one.
- **What**: An architecture that cryptographically binds agent identity to delegated
  user identity, so every action traces to both the code that executed it and the
  person who approved it.
- **How**: SPIRE's workload attestation extended to produce a verifiable agent
  identity; Keycloak acting as an OAuth 2.0 server manages the delegated user
  identity and preserves context across long, nested transactions; an open-source
  MCP Gateway enforces policy and audit at a single trusted point between agents and
  tools.
- **Where applicable**: Enterprise agent deployments. Research-origin, and the
  delegation-chain pattern is the transferable part regardless of whether you adopt
  this particular gateway.

### Let Your Network Speak!

*Nadia Pinaeva, NVIDIA & Joel Takvorian, Red Hat*

- **Why**: Targets a specific and familiar failure: with a non-trivial number of
  network policies in a cluster, telling *why* a connection was allowed or denied is
  genuinely hard. Existing tooling shows what happened, not the reason.
- **What**: An observability approach where the agent receives and understands
  messages from the network explaining why a packet met its fate.
- **How**: Demo walks the path from the Linux kernel to the netobserv GUI via OVS,
  OVN and OVN-Kubernetes.
- **Where applicable**: OVN-Kubernetes specifically — the mechanism runs through the
  OVS/OVN stack, so this is not portable to other CNIs as-is. Directly useful if
  that is your datapath.

### Evolving Baremetal-as-a-Service: Secure Multi-Cluster Networking and Service Identity Automation

*Yushiro Furukawa & Mitsuhiro Tanino, LY Corporation*

- **Why**: A hyperscale operator describing how physical and virtual machines are
  operated through one consistent set of cloud-native patterns — with certificate
  issuance wired into baremetal provisioning, which is the detail worth stealing.
- **What**: A BMaaS platform rebuilt on Kubernetes custom controllers, OpenStack Nova
  extensions and AthenZ-based automation.
- **How**: Nova extended with Kubernetes custom controllers so baremetal provisioning
  and lifecycle run through declarative APIs; ACL-based access control between
  multiple in-house clusters, applied automatically to new pods; AthenZ issuing
  certificates during baremetal instance creation so inter-service communication is
  trusted and encrypted from birth.
- **Where applicable**: Explicitly org-specific — LY Corporation's private cloud, and
  AthenZ is not widely deployed elsewhere. The pattern of binding identity issuance
  to provisioning generalizes; the stack does not.

### KubeVirt on GB200: Virtualizing a Rack-Scale Supercomputer

*Fan Zhang, Kevin Klues & Alay Patel, NVIDIA* — Cloud Native Theater | KubeVirt Summit

- **Why**: The clearest statement in the program of how rack-scale hardware breaks
  existing software assumptions. When the rack behaves as one logical system, the
  PCIe-shaped abstractions in the VFIO/QEMU/Kubernetes stack stop describing
  reality.
- **What**: The practical enablement path for running KubeVirt on GB200 (Grace
  Blackwell), where CPU and GPU are coupled through a cache-coherent interconnect
  with unified memory rather than discrete devices on PCIe.
- **How**: VFIO and kernel requirements, QEMU/libvirt requirements, Topology Manager
  requirements for device plugins or DRA, and two rack-scale pieces: Compute Domains
  as the unit of allocation for multi-node GPU fabrics, with IMEX domain
  bring-up/teardown orchestrated by a daemon integrated into the KubeVirt lifecycle;
  and guest topology pass-through mirroring host CPU/memory/GPU topology so the
  guest driver can online memory correctly.
- **Where applicable**: Requires GB200-class hardware, so narrow today. Worth the
  time anyway for the general lesson about fabric-coupled racks — the same
  assumptions break on any similar architecture.

### Virtualizing Large Scale GPU Cluster for Sovereign AI: Petasus AI Cloud Journey with Kubernetes

*Jian Li, SK Telecom*

- **Why**: Carries the number that matters for the virtualize-or-not argument on
  accelerated infrastructure: under 5% overhead versus bare metal, on a real
  1000+ Blackwell GPU cluster.
- **What**: How the Haein Supercluster — described as Korea's largest AI cluster and
  part of its Sovereign AI initiative — was virtualized on Kubernetes and KubeVirt.
- **How**: The sub-5% figure is attributed to NVLink/NVSwitch and GPUDirect RDMA
  virtualization, explicitly contrasted with traditional PCIe- and TCP-based
  virtualization. Resources are partitioned via namespaces for on-demand tenant GPU
  clusters; automation cuts provisioning from days or weeks to roughly 10 minutes;
  DCGM and Prometheus provide observability.
- **Where applicable**: Requires NVLink/NVSwitch-class hardware and GPUDirect RDMA —
  the performance claim depends entirely on those paths, and would not hold on
  PCIe/TCP. Multi-tenancy approach is broadly instructive.

### Why Is It So Hard to Run a 5G Core on Kubernetes — And What Needs to Change for 6G

*Joel Studler, Swisscom & Ashan Senevirathne, Telstra*

- **Why**: The sharpest critique in the program, from two operators rather than a
  vendor: most "cloud-native Network Functions" are merely containerized ones. For
  anyone watching telco-DC convergence, this names precisely where the abstraction
  is being faked.
- **What**: Why CNFs remain box-centric, illustrated with the argument that a User
  Plane Function is not inherently cloud-native, and what 6G would need to change.
- **How**: The specific indictment is that Helm install mimics hardware mounts,
  Multus wires up virtual cables, and NETCONF configures boxes — so these designs
  bypass Kubernetes' own IPAM, networking and high-availability strengths while
  being marketed as telco-grade. The forward-looking half argues for Kubernetes-first
  patterns and for exposing APIs so the network can be treated as a product.
- **Where applicable**: Telco-specific in its examples, but the underlying pattern —
  lift-and-shift dressed as cloud-native, bypassing the platform's strengths — is
  general and recognizable well outside telco.

## Wildcard

### Beyond the Edge: Cloud Native Application Management Under Extreme Network Conditions

*Tobias Nöthlich & Maximilian Nitsch, D3TN GmbH*

- **Why**: Kubernetes assumes a network that mostly works. This asks what remains
  when you remove that assumption entirely — not high latency, but links where
  end-to-end IP connectivity may never exist at any instant. A genuinely different
  set of constraints, and a useful stress test of which cloud-native assumptions are
  fundamental versus incidental.
- **What**: How containerized applications can be deployed, updated and managed
  through Kubernetes while communicating over Delay-/Disruption-Tolerant Networking
  protocols.
- **How**: Integration points, the networking abstractions required, and practical
  considerations for operating DTN-enabled workloads.
- **Where applicable**: Satellites, deep-space probes, remote research stations,
  air-gapped systems. Nobody's datacenter — but the store-and-forward discipline is
  the interesting export.

### Keeping the Cloud Afloat with Deterministic Simulation Testing

*Marcus Hodgson, Antithesis & Marek Siarkowicz, Google*

- **Why**: etcd's v3.5 consistency errors are a known scar in the ecosystem, and the
  honest admission here is that the robustness testing framework built in response
  demands unsustainable effort and expertise to maintain. The proposed replacement
  is a technique, not more labour.
- **What**: Deterministic simulation testing as a way to validate entire distributed
  systems, now applied to etcd through a CNCF-sponsored collaboration with
  Antithesis.
- **How**: Deterministic execution plus fault injection, which together reproduce
  elusive bugs exactly rather than probabilistically.
- **Where applicable**: General technique for distributed systems. The etcd
  deployment is the proof point; the reason to watch it is whether this becomes the
  default expectation for critical CNCF infrastructure.

### The Hyperscale Uncertainty Principle: Debugging Tail Latency in a Trillion-Object System

*Yashraj Kakkad, Google*

- **Why**: A well-told debugging story with a counterintuitive result: the system was
  partitioned into perfectly balanced shards to minimize variance, and tail latency
  became the problem anyway. The conclusion — that predictability, not average
  performance, is the binding constraint — transfers directly to fabric and queueing
  work.
- **What**: The hunt for tail latency in the Google Photos integrity pipeline at
  trillion-object, exabyte scale, where data skew was ruled out and the real
  bottleneck proved to be the non-linear way P99 latency governs overall throughput.
- **How**: Three competing solutions are compared — traffic shaping as the standard
  fix, request hedging as the high-cost trade-off, and a novel architectural pattern
  the speaker calls the "Partition Alignment Principle". The abstract does not say
  which won or by how much.
- **Where applicable**: Google-specific system, and the specifics are unlikely to
  port. The analysis method and the P99-governs-throughput argument are the general
  parts.

## Themes

- **DRA is becoming the universal device abstraction, and NICs are now inside it.**
  Three separate Core sessions — SR-IOV multi-network, the network-driver panel, and
  the WG Device Management update — all route through Dynamic Resource Allocation.
  The direction is clear: Multus-style side channels give way to first-class
  Kubernetes resources, and cross-node device groups mean the scheduler must start
  understanding fabric topology rather than just node inventory.

- **Cross-zone and east-west traffic cost has become a first-order architecture
  driver.** Spotify's 75% cross-zone reduction and Skyscanner's removal of east-west
  NLBs are the same story told twice: at scale the network bill, not the compute
  bill, forces the redesign. Both answers converge on moving routing decisions into
  a control plane with a global view.

- **Physical reality is reasserting itself against the abstraction.** GB200's
  cache-coherent racks break the PCIe assumptions in VFIO/QEMU; RDMA spine–leaf
  topology has to be discovered and scheduled against; SK Telecom's sub-5%
  virtualization overhead exists only because of NVLink and GPUDirect RDMA; and two
  operators argue that telco CNFs fake cloud-native by wiring virtual cables. The
  hardware is no longer something the platform can abstract away.

- **Workload identity is consolidating on standards, and being pushed down the
  stack.** WIMSE's Workload Identity Token being adopted natively by SPIFFE/SPIRE,
  SPIFFE composed with OAuth identity chaining for multi-hop authorization, node
  joining moving from static tokens to attestation, and agent actions bound
  cryptographically to the user who approved them — all four extend the same
  credential model outward to new principals rather than inventing new ones.

- **Gateway API has won the interface and is now fighting the portability war.**
  ingress-nginx's archival is pushing migration on a deadline, while 40+
  implementations and 55+ features make "supports Gateway API" an insufficient
  answer. Conformance testing is doing the load-bearing work here, and it is where
  the interesting arguments now are.

- **AI traffic is being absorbed into existing networking primitives, not given new
  ones.** The Gateway API Inference Extension, an AI Gateway working group, agentic
  traffic governed through Gateway API, adaptive inference routing on queue depth
  and cache state — the consistent bet across SIG Network and the Envoy/Istio
  ecosystem is that this is a routing problem, and mostly the routing machinery that
  already exists.
