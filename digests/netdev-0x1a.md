<!--
conference: Netdev 0x1A (Rome)
type: vendor
source_url: https://netdevconf.info/0x1A/pages/sessions.html
generated: 2026-09-03
registry_key: netdev-0x1a
-->

# Netdev 0x1A Digest (Rome, 13-16 July 2026)

Netdev is the Linux kernel networking community's own conference, so the "vendor pitch" problem barely exists here — the filter instead is between mainline-relevant engineering and one-off experiments. This cycle is dominated by the AI backend fabric: RDMA multipathing in production at OpenAI/Microsoft scale, SRv6 as the host-controlled path primitive, pluggable congestion control, and encryption sliding down the stack into hardware (PSP in v6.18, MACsec under RoCE, kTLS on DPUs). The second big thread is the DPU/host split becoming a Linux `netdev` contract problem, including how Kubernetes learns to schedule on it.

Write-ups are grounded in the session abstracts; three (MRC/SRv6, PSP, MACsec-on-DPU) are additionally grounded in the published slide decks, which is noted per item.

## Core

### Resilient AI Supercomputer Networking using MRC and SRv6 — Christoph Paasch (OpenAI) and others — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/resilient-ai-supercomputer-networking-using-mrc-and-srv6.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper45-talk-slides/2026_MRC_netdevconf.pdf) · [video](https://youtu.be/qlVweM7rLx4)

**Why:** This is the single most load-bearing talk of the program: production experience of running RDMA over a 75K-GPU fabric at OpenAI and Microsoft, and the clearest public statement yet of how frontier training clusters actually do path selection and failure recovery.

**What:** Three coupled pieces — MRC, an RDMA transport that sprays a single QP's packets across all fabric paths and actively load-balances; two-tier multi-plane Clos topologies (4 x 200G or 8 x 100G planes) that let >100K-GPU clusters stay two-tier; and static SRv6 source routing so the endpoint, not the fabric, decides the path.

**How:** Regular RoCE pins a QP to one hash-selected path, so flow collisions leave links idle while collided flows drive tail latency — and tail latency directly sets step time in synchronous training. MRC keeps one logical QP for the application but sprays across path selectors, each PS resolving to a complete SRv6 destination address that names plane/NIC port and T0 uplink. Loss is treated as path feedback: bad PSs are swapped from a backup set, converging to <1 loss/s/NIC within minutes with no pre-populated denylist. Switches stay dumb — static config, no resilient ECMP hashing, no BGP convergence — and a `clustermapper` loopback SRv6 probe feeds a denylist without needing a peer. Production incidents shown: a T1 that stopped forwarding hit ~25% of QPs and ~580K dropped packets before MRC routed around it; four flapping 200G links cost ~25% throughput for about a minute, with QPs staying alive.

**How much is deployed:** MRC is implemented by three NIC vendors — NVIDIA (ConnectX-8/9), AMD (Pollara, Vulcano), Broadcom (Thor Ultra) — on 400/800G RDMA NICs.

**Where applicable:** Explicitly a large-operator design: it assumes a purpose-built multi-plane Clos, source-routing-capable NICs, and MRC silicon. The transferable ideas — endpoint-driven path selection, treating loss as path health, keeping switches static — apply well below that scale. Packet trimming and ECN load-balancing were mentioned but not covered.

### SRv6 Workshop — Chair: Stefano Salsano (Univ. of Rome Tor Vergata), with Cisco, Ericsson contributors — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/workshop/srv6-workshop.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper48-talk-slides/netdev-0x1A-srv6-l2-services.pdf) · [video](https://youtu.be/VWlH9D7FSCU) · [workshop page with all decks](https://netgroup.github.io/netdev-0x1A-srv6-workshop/)

**Why:** The counterpart to the MRC talk, and the more actionable one: SRv6 is the mechanism by which host-decided pathing and VXLAN replacement both become possible in mainline Linux, and this session covers exactly the gaps that still block that.

**What:** Three threads — source-routed AI backends (deterministic, congestion-aware path placement decided at host/NIC rather than by ECMP hashing); SRv6 L2 services beyond the current `End.DX2` cross-connect; and a provider-grade end-to-end design on Linux + FRR with a new observability tool.

**How:** On L2: RFC 8986 defines `End.DX2`/`DT2U`/`DT2M` and RFC 9252 the EVPN-over-SRv6 overlay, but the kernel only implements the `End.DX2` cross-connect with no native L2 endpoint netdevice; a recent netdev RFC series adds `End.DT2U` plus an `sr6` Ethernet pseudowire device, which is what would make a VXLAN-like deployment model (and therefore replacing VXLAN in Kubernetes CNIs, OVN, Neutron) viable. The provider thread adds `tablesnoop`, a lookup-level tracer sitting between tcpdump and pwru/retis that traces PBR, v4/v6 route lookups, SRv6 head-end/endpoint behaviors and MPLS label ops, plus SRv6 Redundancy Protection (a new R-SID format from `draft-ietf-spring-sr-redundancy-protection`) with 802.1CB FRER extended to SRv6 encapsulation via XDP. (From abstract and agenda.)

**Where applicable:** Broadly applicable and mostly upstream-track: Linux has had SRv6 for 9 years, FRR 5 years, with SONiC/Cilium/VPP in the ecosystem. The L2 pseudowire work is RFC-series-stage, so treat the VXLAN-replacement story as a direction, not a shipping option.

### What's next for the PSP Security Protocol (workshop) — Chair: Willem de Bruijn — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/workshop/whats-next-for-the-psp-security-protocol.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper19-talk-slides/Netdevconf%202026%20Panel_%20What's%20next%20for%20the%20PSP%20Security%20Protocol.pdf) · [video](https://youtu.be/7rA3roMcrDg)

**Why:** PSP is now in mainline (v6.18), has silicon from Broadcom, Intel and NVIDIA, and became an Open Compute Project v1 spec in June 2026. That combination makes it the most credible datacenter alternative to IPsec for intra- and inter-DC and AI-fabric encryption — and this session is where v2 scope gets set.

**What:** A panel on where PSP goes next, with the OCP standardization move as the backdrop: v1 is essentially Google's existing spec plus clarifications, v2+ is where feature gaps and new capabilities land.

**How:** PSP's design points, per the deck: scalable (10M+ flows, 100K+ flow changes/sec; all Rx keys derived from one device key, so O(1) key storage), deliberately minimal (no AH, only AES-GCM/AES-GMAC, no replay protection because L4 already has it), and datacenter-shaped (UDP encapsulation so existing load balancers hash it, plaintext headers so telemetry still works under AEAD, HW-timestamp-derived IV for latency measurement). Candidate v2 work named on the panel slide: multi-user security, cluster-mode key derivation, key exchange, confidential compute, SR-IOV, FIPS 140-3, ChaCha20-Poly1305, optional wire-format fields. Kernel-side work in flight includes netkit and packetdrill support, with packetdrill gaining PSP encap and netlink ops in the `.pkt` language and a wireserver that does a real key exchange against the stack under test.

**Where applicable:** Datacenter and cloud-tunnel scenarios with PSP-capable NICs; deployed at scale at Google today. The OCP move is the signal to watch — it's what would make PSP a multi-vendor baseline rather than one operator's protocol.

### MACsec-Protected RDMA on DPUs: From Linux Netdev State to Workload Scheduling — Alkama Hasan and Vijay Ram Inavolu — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/macsec-protected-rdma-on-dpus-from-linux-netdev-state-to-workload-scheduling.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper38-talk-slides/DRANET_SEC_NetDev0x1A.pdf) · [video](https://youtu.be/uetdaP9m11s)

**Why:** It sits exactly on the intersection this PM cares about — physical fabric encryption, DPU offload, and Kubernetes scheduling — and it names a real gap: RDMA verbs bypass the kernel, so kTLS and in-kernel IPsec cannot protect the path that KV-cache, gradients and model weights actually cross.

**What:** Carry DPU-side MACsec datapath state up into the host-visible RDMA netdev, then let a Kubernetes DRA network driver (DRANet) publish "MACsec-capable" as a schedulable property alongside RDMA, SR-IOV and NUMA locality in the node's ResourceSlice.

**How:** MACsec (802.1AE) sits at L2, below the RDMA transport, so a hardware-offloaded MACsec engine encrypts egress under RoCE with no host CPU crypto cost; the kernel already has the plumbing (`macsec_ops`, `NETIF_F_HW_MACSEC`, `ip macsec offload mac`). The hard part is the split: the host sees an RDMA-capable PCIe function while the MACsec engine, egress port and control plane live on the DPU. DRANet-Sec turns the resulting netdev feature advertisement into a ResourceSlice entry, so a pod requests placement on nodes where RDMA egress is genuinely protected — MACsec becomes a second offload stacked under RDMA, invisible to the workload. The talk's stated focus is keeping the advertised capability aligned with the real protected datapath, a problem that recurs for any DPU-resident offload exposed to the scheduler.

**Where applicable:** Multi-tenant AI/HPC clusters with DPU-based RDMA; demonstrated on a DPU testbed with the Red Hat DPU Operator / OpenShift + Cilium offload stack as context. The capability-advertisement-vs-reality problem generalizes to every DRA-scheduled hardware feature.

### Toward Host-Pluggable Congestion Control for RDMA/IP Datacenter Transports — Vivek Kashyap — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/toward-host-pluggable-congestion-control-for-rdmaip-datacenter-transports.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper35-talk-slides/pluggable_congestion_management_netdev.pdf) · [video](https://youtu.be/cCkRoczzgrM)

**Why:** RDMA congestion control is stuck in NIC firmware, which means every algorithm change is a vendor release. Breaking that open is the difference between DCQCN/PFC-shaped fabrics and fabrics you can actually tune per workload.

**What:** A working implementation of host-driven RDMA congestion control that runs with NIC-embedded congestion control disabled and without relying on DCQCN/PFC behaviour.

**How:** A host component (userspace or kernel) periodically sends probe packets, uses hardware timestamping to get path RTT, converts that into a per-path congestion estimate, then distributes the resulting control value across the active Queue Pairs for that peer via a driver-mediated QP update interface. The author is explicit that probe RTT is a deployable starting signal rather than the right one, and that the same framework could take ECN counts, ACK/progress counters, retransmit events and path-health indicators. (From abstract only.)

**Where applicable:** RDMA/IP datacenter fabrics carrying mixed traffic — AI collectives, storage, KV-cache movement, HPC, front-end — where one fixed firmware algorithm is a poor fit for all of them. Needs driver support for the QP update interface, so vendor cooperation is still on the critical path.

### Can Homa and TCP Get Along? — John Ousterhout — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/can-homa-and-tcp-get-along.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper23-talk-slides/TCPHoma.pdf) · [video](https://youtu.be/K9NZL_2qm4g)

**Why:** Coexistence is the actual adoption blocker for any new datacenter transport. Nobody gets a greenfield fabric, so "what happens when it shares a NIC with TCP" decides whether Homa is deployable at all.

**What:** Measurements of TCP and Homa running concurrently, plus `homa_qdisc`, a new queuing discipline that fixes the resulting unfairness — and, notably, improves plain TCP too.

**How:** Baseline finding: running together, TCP gets slightly *better* (Homa reduces buffer utilization) while Homa degrades badly (TCP still overloads buffers). `homa_qdisc` paces output for both protocols to prevent NIC queue buildup, implements Homa's SRPT policy plus a limited SRPT for TCP, and balances output between the two under congestion. With it, Homa suffers only slight degradation alongside TCP, TCP latency improves over the no-qdisc case, and TCP-only short-message tail latency improves by nearly 2x versus `fq_codel`. (From abstract only.)

**Where applicable:** General Linux hosts — this is a qdisc, not a fabric requirement. Homa itself still wants switch priority queues; the `fq_codel` tail-latency result is interesting independently of whether you ever run Homa.

### Linux QUIC: Bringing a Modern Secure Transport into the Kernel — Xin Long — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/linux-quic-bringing-a-modern-secure-transport-into-the-kernel.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper15-talk-slides/Netdev%200x1A%20Slides%20-%20Linux%20QUIC.pdf) · [video](https://youtu.be/0opE9rssasw)

**Why:** QUIC in the kernel changes what kernel subsystems (SMB, NFS) can use as a secure transport, and it puts a POSIX-shaped API on a protocol that has so far been userspace-library-only. That has knock-on effects for anything doing per-connection identity and crypto offload.

**What:** A kernel QUIC implementation exposing a new `IPPROTO_QUIC` socket type, described as already past prototype stage.

**How:** The kernel owns the full transport — stream management, congestion control, loss recovery, packet handling, connection migration, flow control — while the TLS handshake stays in userspace, coordinated for kernel consumers through the existing `net/handshake` framework and the `tlshd` service. The socket API keeps `connect()`/`accept()`/`sendmsg()`/`recvmsg()` and extends it with ALPN-based dispatching, transport-parameter configuration and stream lifecycle control. Validation covers interop against major QUIC implementations, syzkaller fuzzing and high-speed benchmarking; consumers so far include Samba, in-progress NFS work, curl HTTP/3 and NetPerfMeter. Future work: upstreaming across kernel and GnuTLS, and NIC crypto offload. (From abstract only.)

**Where applicable:** Broad, once upstream — but note the split trust model (handshake in userspace via `tlshd`) and that NIC crypto offload is still future work.

### Accelerating Software RDMA (RXE) with Netkit and Devmem — Yanjun Zhu — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/accelerating-software-rdma-rxe-with-netkit-and-devmem.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper1-talk-slides/rxe_netkit_devmem_ebpf.pdf) · [video](https://youtu.be/kYTYzvWC-wc)

**Why:** It wires together three things this PM tracks separately — netkit (the Cilium-era container device), devmem TCP/dma-buf, and software RDMA — into one datapath, and it targets the container/namespace case rather than bare metal.

**What:** A shortened RXE (Soft-RoCE) datapath that uses netkit as a fast-path transport hook, plus devmem TCP integration for true end-to-end zero copy and an eBPF-based visibility layer.

**How:** Today RXE encapsulates RoCEv2 in UDP/IP, so same-host inter-namespace traffic traverses routing lookups, Netfilter and redundant copies. Hooking netkit's native TX/RX bypasses the IP layer entirely, giving a claimed 10-20% same-host latency reduction in namespace environments (proportional to how much routing/firewall complexity is skipped). Layering devmem TCP and dma-buf on top — with hardware queue leasing/splitting from the physical NIC (e.g. ConnectX-6) — lands payloads directly in device (GPU) memory. For observability, instead of kprobes or driver patches, an eBPF program on netkit's tcx hook parses RDMA headers (BTH etc.) into a ring buffer for PCAP dumping. Presented with a live demo across namespaces based on kernel selftests. (From abstract only.)

**Where applicable:** Containerized RDMA, particularly where zero-copy hardware RXE support is absent. The devmem half needs a NIC supporting queue leasing and a dma-buf provider, so treat the "100% zero copy" claim as hardware-conditional.

### Thrice the charm: an skb extension for BPF metadata — Jakub Sitnicki and Andrej Stender — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/thrice-the-charm-an-skb-extension-for-bpf-metadata.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper31-talk-slides/Netdev%200x1A%20-%20Thrice%20the%20charm%20-%20an%20skb%20extension%20for%20BPF%20metadata.pdf) · [video](https://youtu.be/ot2K4-PFQDc)

**Why:** Carrying custom per-packet metadata between BPF hooks is a recurring blocker for anything building policy or identity into the datapath (service mesh, per-connection labels, tenant tags). This is the third attempt at solving it and the write-up includes why the previous designs failed.

**What:** A proposal to give BPF programs a place to store data whose lifetime is the skb's, outside the narrow scope where XDP/skb metadata works today.

**How:** Two candidate mechanisms are compared — one available today, one still on the drawing board — from the point of view of the BPF networking hooks and their overhead, along with the rejected alternatives (extending skb metadata lifetime guarantees, BPF local storage) and why they didn't work. The skb-extension mechanics get the most attention: compiling out unused extensions, and the extra hot-path allocation that skb extensions currently imply. Ends on open user-API questions. (From abstract only.)

**Where applicable:** Anything BPF-based in the kernel datapath; this is upstream design discussion, so the value is in knowing which way the API is likely to land before building on the current workarounds.

### One Layer Deeper: The 10-Layer Cake Under a Linux Network Interface — Jesse Brandeburg (Cloudflare) — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/one-layer-deeper-the-10-layer-cake-under-a-linux-network-interface.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper17-talk-slides/10%20layer%20cake%20of%20networking%20%281%29.pdf) · [video](https://youtu.be/Bd7ct9pPWTg)

**Why:** The most useful non-feature talk of the program: a production-performance mental model from someone who wrote Intel Ethernet drivers and now runs performance at Cloudflare, framed around the observability gap rather than a knob list.

**What:** A tour of the ten layers hidden under the "interface, socket, queue" abstraction — NIC hardware, drivers, CPU placement, packet hooks, traffic control, firewalls, socket buffers, application runtimes, microarchitecture, observability — and how to reason about which one is spending your budget.

**How:** The framing is that the old playbook ("turn everything off and go fast") no longer applies, because firewalls, observability and multi-tenant isolation are production requirements. Packets can vanish at the NIC, XDP, tc, conntrack, qdisc, softnet backlog, socket receive queue or the application runtime queue — and a service can honestly report it processed everything it received while the kernel drops packets it never saw. Concrete examples: why `sendmmsg()`/`recvmmsg()` still matter, why treating the socket receive queue as a warehouse causes loss and latency, where UDP loses segmentation offload behaviour, where VLAN acceleration hides metadata userspace needs, and the real cost of stacked XDP/tc/netfilter/conntrack/BPF hooks. Ends below the packet path at cache efficiency, code size and TLB misses. (From abstract only.)

**Where applicable:** Universal. Cloudflare's 31.4 Tbps attack-mitigation scale is context, not a prerequisite.

### DPU-Offloaded TLS Termination and Session Routing for Stateful MCP Traffic — Balakrishna Bhamidipati and Vijay Ram Inavolu — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/dpu-offloaded-tls-termination-and-session-routing-for-stateful-mcp-traffic.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper39-talk-slides/netdev-39.pdf) · [video](https://youtu.be/peHxKX72H7U)

**Why:** Agentic traffic is starting to generate its own infrastructure requirements, and this one is squarely identity-shaped: OAuth2/JWT validation moved onto the DPU, which relocates the authentication trust boundary off the inference host.

**What:** A DPU-resident reverse proxy, built only from stock Linux mechanisms, that does TLS termination, OAuth2/JWT validation and MCP session-aware L7 routing.

**How:** MCP sessions are pinned to a backend by an application-layer `Mcp-Session-Id` that the backend assigns in the initialization response — so affinity is invisible at connection time and only readable after TLS termination. On the DPU, the proxy does the OpenSSL handshake in userspace then enables kernel TLS via `SSL_OP_ENABLE_KTLS`, handing record processing to the kernel `tls` subsystem where cipher and kernel support allow. It extracts the session id from decrypted headers into an in-process affinity table (round-robin for new sessions), and a single-process epoll state machine multiplexes handshakes, forwarding, long-lived SSE relay and teardown. JWT validation on the DPU rejects unauthorized requests before they reach inference hosts. Evaluation covers session affinity correctness, backend balance, stale-session handling and kTLS stability over long-lived streams. (From abstract only.)

**Where applicable:** Explicitly framed as a reusable architecture on commodity DPUs with no kernel modifications, rather than a new protocol — so the pattern (identity checks at the DPU boundary, kTLS fallback path) transfers even if MCP doesn't.

### Tempesta xFW: open-source eBPF-based volumetric DDoS protection — Alexander Krizhanovsky — Core

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/tempesta-xfw-open-source-ebpf-based-volumetric-ddos-protection.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper26-talk-slides/slides.pdf) · [video](https://youtu.be/aTq9v_9CYVM)

**Why:** A rare open-source, architecture-level treatment of volumetric DDoS filtering in XDP/tc, including the parts that usually stay proprietary: rate-limiter design trade-offs, and what current eBPF API limits actually prevent.

**What:** An open-source eBPF DDoS mitigation stack covering both host-based deployment (CDN edge, on-prem ADC, where the host terminates TCP) and router-based deployment (ISP/hosting/IaaS, where the host may only ever see attack traffic or one direction of it, as in DSR and scrubbing).

**How:** A multi-layer filter — source port/address filtering, reputation and GeoIP, IP/UDP/TCP anomaly checks, destination-IP rate limiting as last resort — with XDP and tc programs arranged for multi-NIC nodes. The talk compares leaky buckets, sliding windows and probabilistic rate limiting and the configuration hazards of each; covers TCP authentication for ACK/RST floods and SYN-flood protection across host, router and scrubbing scenarios; DNS-specific parsing and acceleration; Prometheus metrics with per-CPU high-throughput incident logging to ClickHouse (sampled under overload); and an evaluation mode for safe deployment. Notes that most filtering logic turns out to be shared across the deployment architectures. (From abstract only.)

**Where applicable:** Broadly deployable open source ([repo](https://github.com/tempesta-tech/xFW), full release scheduled June 2026), from single hosts to scrubbing centres. It is the vendor's own project, so treat performance claims accordingly.

## Adjacent

### io_uring ZCRX: Progress and Next Steps — Pavel Begunkov — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/io_uring-zcrx-progress-and-next-steps.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper41-talk-slides/zcrx.pdf) · [video](https://youtu.be/oXyAF_xfdUw)

**Why:** Zero-copy receive that keeps the normal stack (and its tooling and observability) is the pragmatic alternative to kernel bypass; since 6.15 it has been real, and this is the honest status report.

**What:** Recent ZCRX developments, API additions, and the open questions blocking broader adoption. **How:** The named problems are refill-queue exhaustion when buffers can't be recycled, sharing a NIC queue between multiple processes, and letting applications detect memory pressure before allocation failures bite. (From abstract only.)

**Where applicable:** Linux 6.15+ hosts with supported NICs; general-purpose high-throughput services rather than specialist bypass workloads.

### AF_XDP copy mode needs more love — Jason Xing — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/af_xdp-copy-mode-needs-more-love.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper7-talk-slides/netdev-0x1a-paper7.pdf) · [video](https://youtu.be/nmyuxyIxddU)

**Why:** Zero-copy AF_XDP only works on a handful of drivers (ice, bnxt, mlx5) — for VMs on virtio-net, containers on veth, and the long tail of NICs, copy mode *is* the datapath, and it has been under-optimized.

**What:** Correctness fixes already merged (multi-buffer TX buffer leaks, continuation descriptor handling, a metadata TOCTOU) plus in-flight optimizations totalling close to 2x TX throughput.

**How:** No single fix — cycle-level perf analysis, lock-contention tracing, cache-line bouncing detection and structure layout heat-mapping applied across the copy-mode TX path. (From abstract only.)

**Where applicable:** Directly relevant to container and VM datapaths, which is where the copy path actually lives.

### TCP State of the union (2026) — Eric Dumazet — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/tcp-state-of-the-union-2026.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper40-talk-slides/State%20of%20the%20union%20in%20TCP%20land%20in%202026%20-%20Google%20Slides.pdf) · [video](https://youtu.be/OJnu6Pts-eo)

**Why:** The annual baseline on where kernel TCP performance work is going, from its principal author. **What/How:** Recent and upcoming TCP changes with a focus on performance on modern platforms — the abstract is one line, so the slides are the content. (From abstract only.)

**Where applicable:** Universal; worth skimming the deck rather than reading the abstract.

### Rakaia: Scalable In-Kernel Scheduling for TCP-Based RPCs — Rui Yang, Konstantinos Prasopoulos, Edouard Bugnion — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/rakaia-scalable-in-kernel-scheduling-for-tcp-based-rpcs.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper27-talk-slides/rakaia-netdev-talk.pdf) · [video](https://youtu.be/buZifwSNREM)

**Why:** Every service-mesh and RPC stack pays for the same thing: POSIX exposes byte streams, so userspace rebuilds message semantics with I/O threads, work queues and thread pools. This attacks that at the source.

**What:** A kernel module exposing a purely message-oriented API that hides TCP from userspace, with gRPC adapted to use it.

**How:** Message parsing and work-conserving scheduling happen directly in the kernel's TCP receive path, at the earliest possible point, eliminating head-of-line blocking within and across connections. Compatible with existing RPC protocols, TLS (via kTLS) and the normal TCP stack. Reported: HOL blocking eliminated across connection counts, up to 5x higher throughput-under-SLO than KCM, and 1.56x for gRPC with 23% less userspace CPU for 2% more kernel time. (From abstract only.)

**Where applicable:** Research prototype as an out-of-tree module; the numbers are the argument for pushing message semantics down, not something to deploy now.

### The CXL Fabric End-Game: Bandwidth Realities and Networked Memory for AI Scale — PJ Waskiewicz — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/the-cxl-fabric-end-game-bandwidth-realities-and-networked-memory-for-ai-scale.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper21-talk-slides/CXL%20Memory%20Fabrics%20Coherency%20-%20Netdev%200x1A.pdf) · [video](https://youtu.be/idStzK7MPTc)

**Why:** A useful corrective to the "CXL memory is just a far NUMA node" framing that keeps showing up in AI infrastructure planning.

**What:** An argument that bandwidth, not latency, is the binding constraint on network-attached CXL memory pools, and a sketch of what memory-coherent cluster execution would actually require.

**How:** CXL link bandwidth can be orders of magnitude below native multi-channel DDR, so the bandwidth-to-core ratio changes the economics of scaling models across pooled memory even though the latency is manageable; CXL 2.0 has only just introduced hardware memory pooling. The talk outlines the required work across switching infrastructure, firmware, and Linux networking and memory subsystems. (From abstract only.)

**Where applicable:** Forward-looking ("moonshot" track) — treat as a constraint map for CXL-based memory disaggregation plans, not a deployment guide.

### Securing IOAM in the Linux Kernel: Toward Trustworthy In Situ Network Telemetry — Maxime Goffart, Emilien Wansart, Benoit Donnet — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/securing-ioam-in-the-linux-kernel-toward-trustworthy-in-situ-network-telemetry.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper18-talk-slides/slides_ioam.pdf) · [video](https://youtu.be/TEM1JAgpYbg)

**Why:** IOAM's security model is "assume the domain boundary holds" — one misconfigured filter and in-band telemetry leaks or, worse, can be forged by an on-path adversary.

**What:** Encryption and authentication for IOAM data fields, implemented in the Linux kernel with a userspace configuration interface, released open source.

**How:** An AEAD scheme supporting AES-GCM and ChaCha20-Poly1305 applied to the telemetry carried in IPv6 extension headers, evaluated for its impact on IPv6 forwarding performance. (From abstract only.)

**Where applicable:** Limited domains that actually run IOAM (ISP or datacenter); the general lesson — boundary-filtering as the only control is a single point of failure — is broader.

### Line-Rate Cybersecurity: Modern DPI and Encrypted Traffic Fingerprinting at 100 Gbps — Luca Deri, Alfredo Cardigliano — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/line-rate-cybersecurity-modern-dpi-and-encrypted-traffic-fingerprinting-at-100-gbps.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper29-talk-slides/Netdev_0x1A_slides_deri_cardigliano_v2.pdf) · [video](https://youtu.be/OrL_jLspYUc)

**Why:** The claim that JA3/JA4 have structural flaws against ephemeral TLS extensions is worth knowing if you rely on TLS fingerprints for detection or bot management.

**What:** Recent nDPI work: cryptographic fingerprinting to classify encrypted traffic, the JA3/JA4 weaknesses, and integration with the kernel firewall path.

**How:** Beyond payload parsing, using cryptographic fingerprints for actor identification; integrating nDPI with the Linux firewall architecture for real-time optimization; architectures using PF_RING and SmartNIC flow managers for deterministic 100 Gbps monitoring with hardware-accelerated enforcement. (From abstract only.)

**Where applicable:** Monitoring and enforcement points that can see the traffic; the SmartNIC/PF_RING blueprint is the scale-out path, the fingerprinting critique applies to anyone consuming JA3/JA4.

### Performance Comparison of Transport Mechanisms for LLM Inference KVCache Transfers — Jamal Hadi Salim, Nabil Bitar, Pedro Tammela, Victor Nogueira — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/performance-comparison-of-transport-mechanisms-for-llm-inference-kvcache-transfers.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper14-talk-slides/0x1A-kvcache-Presentation.pdf) · [video](https://youtu.be/0_ZREgPkJbY)

**Why:** The methodology is the contribution: evaluating AI-fabric transports without owning GPUs, which makes transport comparison accessible to anyone with switches and NICs.

**What:** A GPU-free emulation approach that reproduces LLM inference KV-cache traffic patterns on real NICs and fabrics, used to compare latency and throughput across existing transports.

**How:** Model GPU and model-execution behaviour with equations to estimate processing capacity, generate the resulting real-time traffic onto standard network infrastructure, and make the transport pluggable — the point being that different models produce different traffic patterns, so `iperf`-style generators can't express them. (From abstract only.)

**Where applicable:** Any lab evaluating fabric or transport options for AI infrastructure without GPU budget; fidelity depends entirely on how well the emulation model matches the real workload.

### LLMs and the kernel security process (keynote) — Greg Kroah-Hartman — Adjacent

**Links:** [session](https://netdevconf.info/0x1A/sessions/keynote/llms-and-the-kernel-security-process.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper47-talk-slides/gregkh_netdev.pdf) · [video](https://youtu.be/w71JusTenBw)

**Why:** Networking is taking the brunt of the LLM-generated "security" report flood, and how the kernel security team absorbs it affects how fast real network security fixes move.

**What:** A history of the flood, what the kernel security team has tried, and what might reduce the load. (From abstract only.)

**Where applicable:** Anyone maintaining a project with a security-report intake, not just kernel developers. Pairs with the New Age Tooling BoF below.

## Wildcard

### Promise Networks: Why a Bilateral Link Layer Solves Congestion Control at the Source — Anjali Singhai-Jain, Chihjen Chang, Paul Borrill, David Zage — Wildcard

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/promise-networks-why-a-bilateral-link-layer-solves-congestion-control-at-the-source.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper46-talk-slides/promise-networks-talk.pdf) · [video](https://youtu.be/AzSCfNtXfJE)

**Why:** A deliberately foundational challenge to the entire congestion-control framing, presented for community critique — and the kind of argument that either goes nowhere or reshapes the debate in five years.

**What:** The proposal that packet drops are not necessary at datacenter scale, and that congestion control belongs in the link layer as an admission discipline rather than above it as a feedback loop.

**How:** Open Æthernet generalizes the "end-dally" bilateral closure from Metcalfe and Boggs's 1976 EFTP into a link-layer primitive where every frame is gated on a peer-issued token — a sender without a token cannot transmit, so uninvited frames never enter the fabric. Framed via Promise Theory, with a sketch of the Linux kernel surface it would need. Same authors' companion talk applies the identical argument to the syscall boundary. (From abstract only.)

**Where applicable:** Nothing deployable — an explicit moonshot needing new link-layer hardware semantics. Read it for the framing of drops-as-design-choice at million-node scale.

### Networking Headless CXL Devices for AI Memory Services — Vijay Inavolu, Gaurav Agarwal — Wildcard

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/networking-headless-cxl-devices-for-ai-memory-services.html) · [video](https://youtu.be/JaqEdCahElA)

**Why:** A genuinely surprising construction: giving a CXL memory device — which exposes a memory window, not a NIC — a cluster-facing service identity, using nothing but stock kernel pieces.

**What:** A virtual L3 interface that carries IP over a shared CXL memory window, so services running on a CXL Type-2 device (Redis, KV-cache managers, Milvus query nodes) get IP-reachable endpoints and Kubernetes service identity.

**How:** Host and device daemons each open `/dev/net/tun`, configure a virtual L3 interface and `mmap` the same CXL HDM-H window as a shared packet ring, with ordering rules to carry packets reliably over memory; a host-pod bridge pattern gives the device-side Linux a service IP so clients never see the memory window. ping, ssh, Redis and TCP services work end to end with no new module. Reported: 60x less host-link traffic than a host-side compute path, and 2.56x FAISS vector-search throughput scaling across four cards. (From abstract only.)

**Where applicable:** CXL Type-2 "smart memory" hardware, which is rare today — but the pattern (network identity for a device that has no network) is the interesting part.

### Scripting Netfilter with Lua: A Cooperative Kernel-Userspace Pipeline — Lourival Vieira Neto, Md. Shehar Yaar Tausif, Firas Shaari, Marcel S. A. de Moura, Arif Alam — Wildcard

**Links:** [session](https://netdevconf.info/0x1A/sessions/talk/scripting-netfilter-with-lua-a-cooperative-kernel-userspace-pipeline.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper34-talk-slides/netdev-0x1a.pdf) · [video](https://youtu.be/TRETKtPAWck)

**Why:** An L7 filtering design that deliberately does *not* intercept TLS — no CA on every client, no per-connection termination — and still ships in production on Wi-Fi access-point hardware. That trade-off is worth understanding even if you never write kernel Lua.

**What:** A kernel/userspace pipeline that classifies flows from DNS queries, HTTP requests and TLS handshake metadata instead of decrypting them, built on the Lunatik kernel-scripting framework.

**How:** A userspace Lua agent generates an nftables bridge ruleset that dispatches each new flow to a Netfilter hook for classification; nftables then caches the verdict in a set so subsequent packets bypass Lua entirely. Three new bindings: `luanetfilter` (Netfilter hooks), `luaskb` (socket-buffer access and reply synthesis), `luanftables` (libnftables wrapper). Sustains 1.4 Gbps at parity with a plain Linux bridge on a Wi-Fi 6 AP under mixed Ethernet/Wi-Fi HTTPS load; shipping as the in-kernel engine of a commercial secure wireless gateway on OpenWiFi APs. (From abstract only.)

**Where applicable:** Constrained gateway hardware that can't sustain DPI-by-interception; the classify-once-then-cache-the-verdict structure generalizes well beyond Lua.

### New Age Tooling BoF — Chair: Jamal Hadi Salim — Wildcard

**Links:** [session](https://netdevconf.info/0x1A/sessions/bof/new-age-tooling-bof.html) · [slides](https://netdevconf.info/0x1A/docs/netdev-0x1a-paper28-talk-slides/Yuan%20Tan.pdf) · [video](https://youtu.be/w-fGQuNK3pU)

**Why:** The most concrete public accounting so far of what AI-assisted kernel work actually produces — bugs found, patches rejected, and the review machinery being built in response. Read alongside the Greg KH keynote.

**What:** Six short segments: fuzzing past transport-security crypto gates; a proposed gate framework for filtering AI-generated security submissions; a postmortem of an AI-generated SRv6 patchset; an LLM bug-finding agent; and the Sashiko AI code-review tool's adoption story.

**How:** The fuzzing work extends BRF (a Syzkaller fork) for MPTCP because stateless fuzzers can't get past the kernel's token-lookup-then-HMAC chain — it reports two upstream-mergeable bugs in `net/mptcp/` (a userspace-PM alloc-during-teardown race, and a kernel-PM-reachable divide-by-zero in `tcp_tso_segs` that re-emerges a 2021 bug class), with honest limits stated (N=2, no controlled baseline). The submission-filter proposal is four gates, three fully automatable in CI, aimed at the ~80% of submissions where the bug doesn't exist, the root-cause analysis is hallucinated, or the patch was never tested. Sashiko, introduced mid-March 2026, is reported as adopted by most major subsystems. (From abstract only.)

**Where applicable:** Any maintainer-side process facing AI-generated contributions; the gate framework is explicitly proposed as useful regardless of whether AI was involved.

## Themes

- **The AI backend fabric is now production Linux, not a proposal.** MRC + static SRv6 at 75K GPUs, three NIC vendors shipping MRC silicon, source-routed AI backends in the SRv6 workshop, host-pluggable RDMA congestion control, and a GPU-free way to benchmark the transports — the whole stack showed up at once, with incident graphs attached.

- **Encryption is descending the stack and moving off the host CPU.** PSP in mainline v6.18 with an OCP v1 spec, MACsec offloaded beneath RoCE, kTLS terminated on a DPU, AEAD-protected IOAM. The pattern is inline hardware crypto below the transport, with the host increasingly outside the trust boundary rather than inside it.

- **The DPU/host split has become a Linux `netdev` contract problem.** Two talks turn on the same question: when the datapath, the crypto engine and the egress port live on the DPU, how does the host-visible netdev honestly advertise what's protected — and how does Kubernetes (via DRA/ResourceSlices) schedule on that without lying to the workload?

- **Zero-copy is converging from several directions at once.** devmem TCP and dma-buf, io_uring ZCRX, netkit as a fast-path hook, shared-memory socket transport, and a renewed push on AF_XDP copy mode for the container/VM long tail that zero-copy will never reach.

- **The kernel is reclaiming transports that drifted to userspace.** QUIC as `IPPROTO_QUIC`, message-oriented RPC scheduling in the TCP receive path, and a qdisc to make a new transport coexist with TCP — all arguing that the abstraction boundary moved too far up.

- **AI-generated patches are now an operational load on the subsystem, and the response is tooling.** A keynote on the security-report flood, a BoF on gate frameworks, verification-driven LLM bug finding, an SRv6 patchset postmortem, and Sashiko adopted across most major subsystems within four months.

- **Observability gaps keep being named as the real production problem** — packets disappearing between NIC, XDP, tc, conntrack, qdisc and socket queues; RPC latency that no single subsystem can attribute; SRv6 lookups invisible between tcpdump and pwru. Several talks are ultimately about closing attribution gaps rather than adding speed.
