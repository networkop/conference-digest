>>> HOW TO RUN THIS <<<
This is the digest prompt for netdev-0x1a. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/netdev-0x1a.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/netdev-0x1a.md
Write the file into the repo directly if you can; otherwise output the
file contents so it can be saved to that path. Use that exact filename —
it is how the pipeline marks this conference done. If you wrote the file,
a brief confirmation is enough; don't also paste the whole digest.
================================================================

You are helping a product manager triage conference talks. The PM has 15+
years of experience spanning physical and software networking, network
security, and digital identity. Their core interests are: physical datacenter
networking (optics, switching, topology, RDMA/lossless fabrics, cabling,
DC/WAN interconnect), software and cloud-native networking (eBPF, Cilium,
Kubernetes networking, Gateway API, service mesh, IPAM, BGP/datapath
internals), network security, and identity/authentication (passkeys/FIDO,
OAuth, OIDC, SPIFFE/SPIRE, workload and agentic identity). Physical DC and WAN
systems work is CORE to this PM, not adjacent — do not down-rank a paper for
being about hardware, optics, or datacenter fabric.

Below is the program for Netdev 0x1A (Rome) (vendor). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a vendor / community program (e.g. a CNCF or vendor conference).
Separate genuine technical or strategic substance from product marketing.
Down-rank pure product pitches and sponsor slots. Up-rank end-user case studies
with real numbers (scale, latency, cost, incident detail), contributor-led
architecture and internals talks, and sessions that reveal where an open-source
project is actually heading. Be skeptical of "we adopted X and it was great"
talks with no metrics or failure discussion.

## Enriching from the source material (best effort)

The program text gives you a title, authors, and an abstract per item, and
often links (`pdf:`, `page:`, `video:`). The abstract alone is thin — the full
paper has the methodology, real results, and limitations that make the What /
How / Where-applicable sections accurate instead of guessed.

If you have a tool to fetch URLs, then for EACH selected item (Core, Adjacent,
and Wildcard) try to retrieve the fuller source before writing it up:

- Prefer a `pdf:` link; else fetch the `page:` link (often has the full text or
  a longer description); a `video:` link is a last resort, don't transcribe it.
- Use what you retrieve to ground What/How/Where-applicable in the paper's
  actual contributions, evaluation, and stated constraints.

This is strictly best-effort. Many links fail or are paywalled:

- If a fetch fails, is paywalled, returns only an abstract, or you have no fetch
  tool, just fall back to the abstract already in the program text. That is
  fine and expected — do not stall or skip the item.
- NEVER invent paper contents, numbers, or findings from a failed or partial
  fetch. If you only had the abstract, write from the abstract.
- Note when an item's write-up is based only on the abstract, e.g. end its
  What line with "(from abstract only)", so the reader knows the depth.
- Do not let enrichment change which items you select or their tier; selection
  is from the program. Enrichment only deepens the write-up.

## What to produce

Group selected items into three relevance tiers:

- Core: directly relevant to the PM's core interests as listed above
  (physical DC networking, cloud-native networking, network security, or
  identity) as they work on them today.
- Adjacent: relevant to the broader field; useful context or near-term
  influence.
- Wildcard: 2-4 items that are NOT a direct fit for the PM's core interests
  but are worth their attention anyway because the work is genuinely novel or
  signals where the field is heading (a new technique, a surprising result, an
  emerging subfield). A Wildcard should make the PM think "I wouldn't have
  searched for this, but I'm glad I saw it." Do not pad this tier — if there
  are only two true wildcards, list two.

For each selected item provide, in this structure:
- **Title** and speaker(s)/author(s) with affiliation, and the tier.
- **Links**: reference links to the paper, slides, and recording where the
  program provides them (the program text below includes pdf:/video: links per
  item when available — use those exact URLs; omit a link if not present rather
  than guessing).
- **Why**: why this matters — the problem it addresses and why it's worth the
  PM's time.
- **What**: what the work actually is — the core contribution or finding, in
  plain terms (not the marketing abstract).
- **How**: how it works — the key technical approach or mechanism.
- **Where applicable**: the environment this applies to, and any specifics that
  constrain it. Explicitly flag if it is org-specific (e.g. "Alibaba-specific
  production setup", "requires Broadcom Tomahawk silicon", "assumes a
  single-operator WAN") versus broadly applicable. If it's a general technique,
  say so.

Then a short "Themes" section (3-6 bullets) naming patterns across the
program: what the field is collectively paying attention to this cycle.

## Rules

- Prioritize ruthlessly. 15 sharp picks beat 60 hedged ones. A large program
  should still yield a tight list.
- Skip pure product pitches, sponsor slots with no substance, and
  beginner/101 sessions unless they signal a real shift.
- If the program text is incomplete or an abstract is missing, say so for that
  item rather than inventing content.
- Do not invent talks, authors, or affiliations. Use only what's in the
  program text below.

## Output format

Target renderer is GitHub (GitHub-Flavored Markdown viewed in a repo). Use only
syntax GitHub renders reliably, and follow these rules:

- Headings with `#`/`##`/`###`; bold with `**...**`; italics with `*...*`.
- Bullet lists with `-`. Put a blank line before every list and before every
  heading, or GitHub won't render them correctly.
- Keep nested-list indentation at two spaces per level; avoid deeper nesting.
- All links as `[text](url)` — never bare URLs. Use the exact pdf:/video: URLs
  from the program text.
- No raw HTML except the metadata comment below. Do not use heading IDs,
  footnotes, definition lists, or other non-GFM extensions.
- You may use tables and `code spans` where they genuinely help, since GitHub
  supports them; don't force them.

Begin the output with this metadata, wrapped in an HTML comment so it does not
show in the rendered view but stays in the source:

<!--
conference: Netdev 0x1A (Rome)
type: vendor
source_url: https://netdevconf.info/0x1A/pages/sessions.html
generated: 2026-09-03
registry_key: netdev-0x1a
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Session type: talk

### Why Syscalls Fail: Bilateral Commit at the Linux Kernel/Userspace Boundary
Speakers: Manav Singhai and Paul Borrill
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/why-syscalls-fail-bilateral-commit-at-the-linux-kerneluserspace-boundary.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper4-talk-slides/why-syscalls-fail-deck.pdf | video: https://youtu.be/JtbfJen0zeg
Just like conventional Ethernet, system calls are fire-and-forget.
The Unix syscall interface—the boundary between userspace and kernel—operates as a unilateral protocol. The caller transmits a request into the kernel and assumes the operation will complete correctly, the result will be delivered to userspace, and the application will consume it. No bilateral commit protocol governs this boundary. When the assumption fails—through OOM kills, signal delivery during I/O, page cache eviction, completion queue races, or power loss—the failure is typically silent.
This paper introduces the Kernel Acknowledgment Spectrum: a formal framework for classifying kernel-userspace interactions by the highest level of bilateral confirmation they provide. We identify five levels—from Level 0 (fire-and-forget write() to page cache) through Level 4 (bilateral semantic commit with application verification)—and show that the vast majority of syscall interfaces terminate at Level 1 or below.
We connect syscall failure to the Forward-In-Time-Only (FITO) projection error and demonstrate that the same structural absence identified in email (SMTP), messaging (SMS/iMessage), and conventional Ethernet—no commit protocol—is present at the kernel-userspace boundary. Every syscall encodes the FITO assumption: the caller presumes forward progress through the kernel, through the hardware, and back to userspace, with no mechanism to detect or recover from violations of this assumption.
We present forensic case studies including the PostgreSQL fsync catastrophe, io_uring completion queue races, signal coalescing failures, and the Linux memory overcommit design. We survey existing bilateral mechanisms—seL4 synchronous IPC, POSIX fsync(), userfaultfd(), and the failed Windows Transactional NTFS—and propose a taxonomy of bilateral commit strategies at the syscall boundary, drawing on the bilateral link protocol of Open Atomic Ethernet (OAE).

### AF_XDP copy mode needs more love
Speakers: Jason Xing
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/af_xdp-copy-mode-needs-more-love.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper7-talk-slides/netdev-0x1a-paper7.pdf | video: https://youtu.be/nmyuxyIxddU
In practice, only a handful of drivers (e.g., ice, bnxt, mlx5) benefit from AF_XDP’s zero-copy mode. For the vast majority of deployments — virtual machines on virtio-net, containers interconnected via veth, and the long tail of hardware without dedicated XSK support — zero-copy is simply not an option. Copy mode thus serves as the de facto universal data path, yet it has received far less attention than its zero-copy counterpart. This talk covers both the correctness fixes recently merged into mainline (multi-buffer TX buffer leaks, continuation descriptor handling, TOCTOU in metadata) and a set of ongoing performance optimizations that, taken together, deliver close to a 2× throughput improvement. These gains did not come from a single silver bullet. They are the result of methodical, fine-grained profiling — cycle-level perf analysis, lock contention tracing, cache-line bouncing detection, and structure layout heat-mapping — applied across every layer of the copy-mode TX path. The optimizations include:

### RPC Latency Breaker: Where Did My RPC Time Go?
Speakers: Satish Kumar and Fam Zheng
Track: Hands On
page: https://netdevconf.info/0x1A/sessions/talk/rpc-latency-breaker-where-did-my-rpc-time-go.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper9-talk-slides/netdev-0x1a-paper9.pdf | video: https://youtu.be/DHvogOQ8S-g
RPC latency in datacenter environments is difficult to diagnose because a single RPC spans multiple subsystems: the kernel receive stack on each host, application scheduling delays, business logic, and the physical network. Service mesh frameworks record end-to-end latency but cannot attribute it to a specific component.
SO_TIMESTAMPING provides kernel timestamps but retrieving them from the socket error queue is slow and carries performance overhead, forcing most deployments to rely on sampling rather than per-RPC coverage. It also requires application changes to consume the data and correlate timestamps with the RPC identifier. Recent eBPF-based developments solve the slow retrieval problem by collecting these timestamps directly in BPF and can correlate them with the originating system call, but cannot correlate them with the RPC.
Furthermore, current solutions emphasize TX-path, per-packet tracing, capturing time windows such as qdisc scheduling delays and ACK RTT. We argue that TX-path delays are rarely the source of problems — they occur within the application’s own execution context and are typically fast. Network RTT windows are already well-served by existing tools like BCC’s tcprtt.
We present RPC Latency Breaker, which decomposes every RPC into four components: (1) full RPC time, from the requester’s sendmsg to its recvmsg of the response; (2) NIC-to-softirq delay on both sides, capturing NIC processing and softirq scheduling latency; (3) softirq-to-application-read delay on both sides, capturing softirq processing and application scheduling delays; and (4) network RTT, reflecting physical network latency. All of this is derived solely from syscall-level hooks and SO_TIMESTAMPING RX timestamps — no per-packet tracing, no application changes, and no clock synchronization required, and provides this breakdown for every RPC.
Correlating timestamps with individual RPCs — without application-level RPC identifiers — is solved by exploiting the ping-pong pattern inherent in RPC traffic: on a given TCP flow, sendmsg and recvmsg events strictly alternate between requester and responder. We detect this pattern by analyzing time gaps between consecutive events and pair timestamps across the two endpoints using TCP socket sequence numbers: a sender’s write_seq at sendmsg precisely matches the receiver’s copied_seq at the corresponding recvmsg, establishing a per-RPC mapping without any application cooperation.
Clock synchronization across the two hosts is not required because timestamps from different clock sources are never directly compared. Each latency component is computed by differencing timestamps from the same host: NIC-to-softirq and softirq-to-read delays are purely local measurements, and full RPC time is derived from the requester’s own clock alone. Socket sequence number alignment identifies which events correspond across hosts but carries no timing information from the remote clock. As a result, even large inter-host clock skews do not affect the accuracy of the breakdown.
We will present case studies from our production environment demonstrating how the tool has identified a range of RPC latency problems. Using this breakdown, we can readily categorize issues as slow physical network, application scheduling delays, or longer business logic — and once categorized, it becomes immediately clear where to focus the investigation.

### Accelerating Software RDMA (RXE) with Netkit and Devmem
Speakers: Yanjun.Zhu
Track: Hands On
page: https://netdevconf.info/0x1A/sessions/talk/accelerating-software-rdma-rxe-with-netkit-and-devmem.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper1-talk-slides/rxe_netkit_devmem_ebpf.pdf | video: https://youtu.be/kYTYzvWC-wc
Software RDMA (Soft-RoCE/RXE) traditionally encapsulates RoCE v2 traffic within standard UDP/IP packets. While functional, this design forces same-host inter-namespace or container communication to traverse the entire Linux networking subsystem , incurring severe performance penalties from routing table lookups, Netfilter/iptables rules, and redundant memory copies. We propose and demonstrate an optimized, shortened data path for RXE that leverages netkit as a high-performance fast-path transport hook. By interfacing directly with netkit’s native transmit and receive mechanisms, RXE entirely bypasses the traditional IP layer. Our evaluation demonstrates a 10% to 20% reduction in same-host latency within network namespace environments, highly dependent on the complexity of the bypassed host routing and firewall rules. To push the boundaries of zero-copy software RDMA, we integrate Device Memory TCP (devmem TCP) and dma-buf into this architecture via netkit. By utilizing hardware queue leasing and splitting from a physical NIC (e.g., NVIDIA ConnectX-6), data payloads bypass host RAM and land directly into bound device memory (e.g., GPU). This hardware-software co-design achieves absolute 100% zero-copy data transfers across network boundaries , completely mitigating CPU-bound memory copy overhead under massive workloads. Furthermore, this architecture addresses a long-standing challenge in software RDMA: non-intrusive, low-overhead observability. Unlike kprobes or driver-specific modifications that degrade performance or break portability , we leverage netkit’s native integration with eBPF (tcx/ingress). We implement a programmable visibility layer that executes kernel-level packet parsing , extracts RDMA headers (Base Transport Header/BTH, etc.) into an eBPF ring buffer , and streams them to user space for standard PCAP dumping with negligible overhead. Live Demonstration: We will present a fully functional, unified RXE-Netkit prototype operating across isolated Linux network namespaces. The live demonstration will showcase:
This talk will feature a comprehensive, deep-dive architectural analysis along with an end-to-end live demo based on Linux kernel selftests.

### Performance Comparison of Transport Mechanisms for LLM Inference KVCache Transfers
Speakers: Jamal Hadi Salim and Nabil Bitar and Pedro Tammela and Victor Nogueira
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/performance-comparison-of-transport-mechanisms-for-llm-inference-kvcache-transfers.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper14-talk-slides/0x1A-kvcache-Presentation.pdf | video: https://youtu.be/0_ZREgPkJbY
The AI/ML infrastructure landscape is evolving at an unprecedented pace, driven by continuous innovation across AI accelerators, networking technologies, and software stacks. In networking specifically, the industry is rapidly advancing fabric architectures, switch capabilities, NIC technologies, and transport protocols.
Leading LLM models roughly doubling in size every 6 to 10 months. Current state of the art is in the range of 1-3 trillion parameters. At 1 byte per parameter that requires 1-3 TB of GPU RAM. There is no way to fit that on 1 or 8 GPUs. You need networking to interconnect many GPUS !
To evaluate networking technologies one would need to keep up with:
Networking plays a pivotal role for interconnecting the GPUs and many proposals exist on how to transport the inter-cluster traffic - which is of interest to us.
There is a challenge: If you want to keep up and evaluate how evolving networking technologies handle these fast moving variables or if you are trying to innovate a new network transport you would need to constantly invest in GPUs and associated hardware which is not cheap.
Our approach overcomes the challenge by:
1) Coming up with a technique which emulates the GPU + model processing using mathematical equations to estimate the processing capacity of GPUs and specific model behavior to generate real time traffic that would use standard network infrastructure. Real NICs and switch fabrics can be used without needing any GPUs (which are many factors more expensive than network gear).
2) Allowing plugging in of different transports into the emulated GPUs. We will demonstrate that approaches used in different LLM models exhibit different traffic patterns, so using a tool like classical tools like iperf will be insufficient to express traffic patterns. This approach also allows creating and testing new transports in a more realistic environment.
In this talk we use our approach to generate traffic to evaluate and compare the performance characteristics—latency and throughput—of the several existing transport mechanisms by emulating inference KV cache transfers across a set of existing LLM models and GPU configurations:

### Kernel shared memory socket transport
Speakers: David Wei
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/kernel-shared-memory-socket-transport.html | video: https://youtu.be/BCI6itT8_Hc
The fastest way to do IPC is to use shared memory allowing for zero copy on both the sender AND the receiver. The kernel does not provide primitives that allow for zero copy on both sides; features such as splice, sendfile and vmsplice only avoid copying on the sender side.
This has typically been a problem the kernel left to userspace to handle, with libraries such as boost::interprocess that build on top of shared memory. However it requires both the sender and the receiver to use the same library to do shared memory IPC. This makes it hard for foundational libraries such as HTTP clients and servers to integrate zero copy IPC, instead needing the final service using the HTTP client to make their own modifications to the client, using the same shared memory IPC library as the HTTP server.
This proposal is about adding kernel support for fast, same host shared memory IPC, built on top of AF_UNIX SOCK_SEQPACKET and io_uring with UDP-like message based semantics. io_uring is chosen to take advantage of features such as registered buffers to pre-pin the shared memory once and flexibility in extending uAPI instead of existing socket based APIs. The goal is that once this is upstream, then any userspace library can add support knowing that it will work with any other sender/receiver process that use the same kernel feature.
There is a working prototype ready for RFC which will be sent to the list prior to the conference. The goal is to seek community feedback on the uAPI and implementation design choices.

### Linux QUIC: Bringing a Modern Secure Transport into the Kernel
Speakers: Xin Long
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/linux-quic-bringing-a-modern-secure-transport-into-the-kernel.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper15-talk-slides/Netdev 0x1A Slides - Linux QUIC.pdf | video: https://youtu.be/0opE9rssasw
QUIC (RFC 9000) is now widely used for modern secure networking, combining encrypted transport, multiplexed streams, and low-latency connection setup over UDP. While it has become the default transport for many user-space applications, QUIC is still not part of the Linux kernel networking stack. This limits its integration with kernel subsystems and reduces opportunities for reuse in components such as SMB and NFS.
This talk presents a Linux kernel implementation of QUIC that introduces it as a native transport using a new IPPROTO_QUIC socket type. It starts with the motivation for moving QUIC into the kernel and the practical benefits this enables, including direct use by kernel subsystems, POSIX-style socket APIs, ALPN-based connection dispatching, and reduced overhead through in-kernel processing.
The design and architecture of the implementation are covered in detail. The kernel handles the full QUIC transport logic, including stream management, congestion control, loss recovery, packet handling, connection migration, and flow control. TLS handshake processing remains in user space. For kernel consumers, the existing net/handshake framework together with the tlshd user-space service is used to coordinate handshake processing while keeping a clear and minimal boundary between kernel and user space.
The socket API follows familiar POSIX patterns, exposing connect(), accept(), sendmsg(), and recvmsg() for both applications and kernel consumers. In addition, the API is extended to support a broader set of use cases, including ALPN-based routing, transport parameter configuration, stream life cycle control, and connection-level operations needed by in-kernel and user-space consumers. Real-world usage examples include Samba integration, ongoing NFS work, curl HTTP/3 support, and performance tooling such as NetPerfMeter.
Testing and validation include interoperability testing against major QUIC implementations, syzkaller fuzzing, and performance benchmarking on high-speed networks, showing that the implementation is already usable beyond a prototype stage.
The talk concludes with future work, including upstreaming efforts across the kernel and GnuTLS ecosystems, NIC crypto offloading support, and continued evolution of the API to cover additional deployment scenarios and workload requirements.

### Validation and Evaluation of HyStart++ for Linux
Speakers: Maryam Ataei Kachooei and Zimraan Ahmad and Joshua Solomon and Clive Thompson and Jae Won Chung and Benjamin Peters and Feng Li and Mark Claypool
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/validation-and-evaluation-of-hystart-for-linux.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper16-talk-slides/netdev2026_v2.pdf | video: https://youtu.be/ndMJnAJc79I
Linux TCP CUBIC defaults to using HyStart to exit slow start and transition to congestion avoidance, but HyStart can perform poorly over networks with delay variation by exiting slow start prematurely. HyStart++ was designed to improve HyStart by adding Conservative Slow Start, an intermediate phase between slow start and congestion avoidance that reduces the exponential growth until either confirming a transition to congestion avoidance or going back to slow start. Our work validates an implementation of HyStart++ for Linux, confirming adherence of the code base to the Request for Comments (RFC 9406) and demonstrating functionality through case studies under known conditions. Then, we evaluate HyStart++ over several network paths, focusing on networks with high delay variation, including satellite links. Our results show that HyStart++ improves upon HyStart by continuing to grow after HyStart would have exited slow start, leading to a higher congestion window and better early goodput in some cases. However, HyStart++’s reaction to delay variation restricts utilization, motivating further adjustments to HyStart++ and other slow start mechanisms to improve slow start for wireless access networks.

### One Layer Deeper: The 10-Layer Cake Under a Linux Network Interface
Speakers: Jesse Brandeburg
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/one-layer-deeper-the-10-layer-cake-under-a-linux-network-interface.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper17-talk-slides/10 layer cake of networking (1).pdf | video: https://youtu.be/Bd7ct9pPWTg
Queues are not Ethernet NICs, Ethernet interfaces are not single Ethernet ports, and having fast hardware doesn’t automatically make software fast.
Linux networking presents a clean abstraction: an interface, a socket, a queue. Production systems are less polite. Under that abstraction is a 10-layer cake of NIC hardware, drivers, CPU placement, packet hooks, traffic control, firewalls, socket buffers, application runtimes, microarchitecture, and observability. The frosting on the outside hides the complexity inside.
This talk is a tour of those hidden layers from the perspective of a kernel developer who spent years writing Intel Ethernet drivers and now works on production performance at Cloudflare. The old performance playbook was often “turn everything off and go fast.” Modern production is different: everything is on because it (usually) has to be. Firewalls, observability, and multi-tenant isolation are critical production features. Cloudflare has publicly described mitigating attacks as large as 31.4 Tbps , but the hard problem is no longer making one machine’s performance scream; it is understanding which layer is quietly spending the budget, hiding the drop, or adding the delay (often stacked problems).
A frequently occurring challenge in modern production performance is the observability gap. Linux has counters, but not always the correlation you want at 03:00 from Prometheus. Packets can disappear at the NIC, XDP, tc, conntrack, qdisc, softnet backlog, socket receive queue, or application runtime queue. A service can honestly report “I processed everything I received” while the kernel is dropping packets before the application ever sees them.
We will walk through concrete examples from Linux networking and production systems: why sendmmsg() and recvmmsg() still matter, and why treating the socket receive queue as a packet warehouse causes loss and latency. Why UDP is great until you lose automatic segmentation/offload behavior, and why VLAN acceleration is helpful until userspace needs the metadata. Why security hooks such as XDP, tc, netfilter, conntrack, socket filters, and eBPF programs are powerful but not free.
Finally, we will look below the packet path at CPU behavior: cache efficiency, code size, and TLB misses. “Less code is faster” and “bigger assembly instructions are faster” are both true — it depends on whether you’re bound by instructions, frontend bandwidth, or translations.
The goal is not to memorize every knob. The goal is to build the intuition to ask better questions when fast hardware becomes slow software. Knowing one layer deeper than the abstraction you develop on makes you a better network developer, a better production engineer, and a better architect.
The 10 Layers

### improving debuggability of nommu code with UML
Speakers: Hajime Tazaki
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/improving-debuggability-of-nommu-code-with-uml.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper8-talk-slides/netdev0x1a-nommu-uml.pdf | video: https://youtu.be/5S1WDdxl06s
Userspace network stack can be implemented as a port of kernel network stack to userspace (e.g., Linux kernel library). At the cost of less generality, and lack of memory protection/isolation within a single network stack, the performance is a primary benefit of the mechanism. This performance benefit is mainly derived from the single-address space nature of its internal because the send/receive code path can reduce the cost of program/memory context transitions, resulting the improvement of system calls overhead.
In Linux kernel, the single-address space of memory management subsystem can be configured by disabling memory management unit (MMU), CONFIG_MMU=n (or nommu). Historically the configuration is mainly used for embedded devices which does not have an MMU in their processors, but recently it is revisited to support specialized case of virtualization, which a guest only requires a single address space, like the case of userspace network stack.
Although nommu has a unique and an important bit of kernel, several maintainers recently raised a concern that it is hard to maintain the feature because it is hard to test. Linux test project (LTP) dropped NOMMU (uclinux) test cases, which had been broken and not fixed due to lack of maintainers ( 1). mm subsystem had several regressions with CONFIG_MMU=n which might also be caused due to lack of tests during feature introduction ( 2*3). Testing platform is available via buildroot image of nommu platforms, even you do not have a real hardware, but it is also hard to maintain toolchains to build code and test images.
We are trying to fix this situation by adding nommu mode to user-mode linux (UML). nommu UML is currently under v14 patchset (*4) and runs with Alpine Linux with additional busybox/musl packages, which we also plan to upstream once kernel inclusion.
Supporting nommu to UML has an several meanings:
Here are the summary of what we have done.
We will briefly highlight above in this talk, and showcases what we can do to more debug-friendly nommu kernel. We will also share several facts gained from local benchmark, bug reproduciblity with KASAN. In addition to that, we will discuss the possible extensions that we plan to do in the future.
*1 https://lore.kernel.org/ltp/20240103015240.1065284-1-pvorel@suse.cz/ *2 https://lore.kernel.org/linux-mm/20241108222834.3625217-1-thehajime@gmail.com/ *3 https://lore.kernel.org/linux-mm/20251218083200.2435789-1-joshua.hahnjy@gmail.com/ *4 https://lore.kernel.org/all/cover.1770170302.git.thehajime@gmail.com/

### Securing IOAM in the Linux Kernel: Toward Trustworthy In Situ Network Telemetry
Speakers: Maxime Goffart and Emilien Wansart and Benoit Donnet
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/securing-ioam-in-the-linux-kernel-toward-trustworthy-in-situ-network-telemetry.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper18-talk-slides/slides_ioam.pdf | video: https://youtu.be/TEM1JAgpYbg
In Situ Operations, Administration, and Maintenance (IOAM) is an IETF-standardized in-band network telemetry protocol that enables routers to collect and embed operational telemetry data directly into IPv6 Extension Headers of in-transit packets. IOAM is designed to operate within a Limited Domain - such as an Internet Service Provider (ISP) or a datacenter network - where boundary filtering is assumed to prevent telemetry data from leaking outside the domain. However, IOAM provides no built-in confidentiality or integrity protection: telemetry fields are transmitted in plaintext and are not authenticated, leaving them vulnerable to interception and forgery by on-path adversaries in the event of a misconfiguration or boundary enforcement failure. To address this gap, we propose a security mechanism providing encryption and authentication for IOAM based on an AEAD scheme, supporting both AES-GCM and ChaCha20-Poly1305. We implement this solution directly in the Linux kernel, with a user-space configuration interface, and evaluate its impact on IPv6 packet forwarding performance. Both the kernel-space and user-space code are released as open source.

### The CXL Fabric End-Game: Bandwidth Realities and Networked Memory for AI Scale
Speakers: PJ Waskiewicz
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/the-cxl-fabric-end-game-bandwidth-realities-and-networked-memory-for-ai-scale.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper21-talk-slides/CXL Memory Fabrics Coherency - Netdev 0x1A.pdf | video: https://youtu.be/idStzK7MPTc
Compute Express Link, or CXL, has seen significant industry focus surrounding memory expansion devices, specifically utilizing CXL.mem to add capacity. As large-scale AI models continue to demand massive, distributed memory footprints, the conversation has naturally shifted toward using CXL.mem to architect network-attached memory pools.
However, current implementations gloss over a severe architectural bottleneck: bandwidth. The common industry assumption is that CXL memory access can simply be treated as a “far” NUMA node, implying that latency is the primary hurdle. While the latency is manageable, CXL link bandwidth can be orders of magnitude slower than native, multi-channel DDR speeds. This massive bandwidth-to-core disparity completely changes the economics and execution realities of scaling large AI models across distributed memory.
With CXL 2.0 implementations only recently introducing initial support for hardware-level memory pooling, much of the work to realize true memory-coherent clusters remains ahead of us. The focus of this talk is to look past simple memory expansion and evaluate what is required to achieve native cluster execution across fully memory-coherent CXL fabrics. The presentation will outline the “moonshot” requirements necessary to bridge this gap, detailing the critical architectural work and future integration needed across switching infrastructure, firmware, and the Linux kernel networking and memory subsystems.

### Can Homa and TCP Get Along?
Speakers: John Ousterhout
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/can-homa-and-tcp-get-along.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper23-talk-slides/TCPHoma.pdf | video: https://youtu.be/K9NZL_2qm4g
The Homa transport protocol differs significantly from TCP: for example, it uses receiver-driven congestion control instead of sender-driven, it is message-based rather than stream-oriented, and it takes advantage of priority queues in network switches. This raises concerns about what happens when both protocols are used simultaneously: do the protocols interfere with each other?
This talk will consist of three parts. In the first part I will discuss initial performance measurements of TCP and Homa running concurrently, which show that TCP performance actually improves slightly when running with Homa (because Homa reduces buffer utilization) but Homa’s performance degrades drastically (because TCP still overloads buffers). In the second part of the talk I will describe homa_qdisc, a new queuing discipline that paces output traffic for both Homa and TCP to prevent queue buildup in the NIC; homa_qdisc also implements Homa’s SRPT policy and implements a limited form of SRPT for TCP as well. When output congestion occurs, homa_qdisc balances output traffic between Homa and TCP. In the third part of the talk I will present performance measurements of TCP and Homa running with homa_disc. When TCP and Homa run concurrently, homa_qdisc improves performance for both protocols: Homa now suffers only slight degradation in the face of competing TCP traffic, and TCP latency is even better with homa_qdisc than without. In addition, when TCP runs without Homa, homa_qdisc improves tail latency for short messages by almost a factor of 2 relative to fq_codel.

### Tempesta xFW: open-source eBPF-based volumetric DDoS protection
Speakers: Alexander Krizhanovsky
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/tempesta-xfw-open-source-ebpf-based-volumetric-ddos-protection.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper26-talk-slides/slides.pdf | video: https://youtu.be/aTq9v_9CYVM
In this talk we present Tempesta xFW - an open source [1][2] eBPF-based solution for mitigating volumetric DDoS attacks.
Tempesta xFW targets different protection architectures: host-based protection, such as CDN edge or on-premises application delivery controller cases, where a host is a TCP connection endpoint; and router-based protection, such as an ISP, hosting, or IaaS provider cases, where a host routes IP packets to protected servers or networks. In the latter case, the host may not “see” normal clean traffic and may receive only traffic containing a DDoS attack. Also, the node may receive only client-to-server traffic, as in direct server return or some traffic scrubbing scenarios.
Moreover, there are always-on, redirection, and hybrid deployment scenarios, and modern “hit-and-run” DDoS attacks, such as Aisuru-Kimwolf, challenge the architectures.
In this talk we discuss:
DDoS protection architectures - surprisingly, most filtering logic is shared across them
What makes DDoS protection logic unique - which protection logic requires specific eBPF programming with extensive map usage and interaction with the kernel, and which can be implemented with traditional firewall rules
XDP and TC programs architecture for multi-NIC nodes
Multi-layer filtering architecture and simple protection logic: source port and address filtering, reputation and GeoIP filtering, IP, UDP and TCP anomalies, destination IP rate limiting as the last resort.
Different approaches to rate limiting: leaky buckets, sliding windows, probabilistic rate limiting, and issues with proper configuration
TCP authentication approach for ACK and RST flood protection
TCP SYN flood protection for host, router and scrubbing scenarios
DNS protection - from basic parsing to advanced techniques accelerating protected DNS servers
Prometheus monitoring and high-throughput per-CPU incident logging to ClickHouse with sampling under overload
Safe deployment with evaluation mode
Performance evaluation and challenges with current eBPF API limitations
References:
[1]. Tempesta xFW public repository; full open-source release scheduled for June 2026, https://github.com/tempesta-tech/xFW
[2]. Tempesta xFW wiki page, https://tempesta-tech.com/tempesta-escudo/knowledge-base/XFW/

### Thrice the charm: an skb extension for BPF metadata
Speakers: Jakub Sitnicki and Andrej Stender
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/thrice-the-charm-an-skb-extension-for-bpf-metadata.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper31-talk-slides/Netdev 0x1A - Thrice the charm - an skb extension for BPF metadata.pdf | video: https://youtu.be/ot2K4-PFQDc
After a few months of pause, we’re taking another stab at giving BPF users a place to store custom data that lives and dies with the skb.
We’ll start with a recap of what we’ve established about the existing XDP/skb metadata feature:
From there we’ll look at two ways to store skb-associated BPF metadata outside of where XDP/skb metadata is supported, one available today and one still on the drawing board:
We’ll compare what the interface looks like from the PoV of BPF networking hooks, and what overhead users can expect from each approach.
To round out the picture, we’ll also cover the alternatives that didn’t pan out, like extending skb metadata lifetime guarantees and adding BPF local storage, and explain where those designs failed.
Next we’ll focus on skb extensions themselves and two aspects of their current implementation that affect how well they can carry BPF metadata, along with how we might improve the status quo: the challenges of compiling out unneeded extensions, and every network stack developer’s worst nightmare, the extra memory allocation on the hot path.
We’ll wrap up with considerations for the user API for BPF metadata access, going over questions like:

### Rakaia: Scalable In-Kernel Scheduling for TCP-Based RPCs
Speakers: Rui Yang and Konstantinos Prasopoulos and Edouard Bugnion
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/rakaia-scalable-in-kernel-scheduling-for-tcp-based-rpcs.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper27-talk-slides/rakaia-netdev-talk.pdf | video: https://youtu.be/buZifwSNREM
Delivering RPCs with high throughput and low latency demands work-conserving scheduling across many CPU cores and eliminating head-of-line (HOL) blocking across all messages. By exposing per-connection byte streams rather than messages to userspace, the POSIX TCP API inherently induces HOL blocking both within and across connections. To mitigate HOL blocking, RPC frameworks such as gRPC must reconstruct message semantics in userspace through additional abstractions including dedicated I/O threads, work queues, and worker thread pools, introducing significant context switching and synchronization overheads.
This paper presents Rakaia, a framework that hides all TCP-level abstractions from userspace and exposes a purely message-oriented API. By performing message parsing and work-conserving scheduling directly in the kernel’s TCP receive path, at the earliest possible point, Rakaia efficiently eliminates HOL blocking and avoids the heavy userspace machinery imposed by stream-based APIs.
Rakaia is compatible with existing RPC protocols, TLS, and the kernel’s TCP stack. Rakaia is implemented as a Linux kernel module and relies on kTLS. We also adapt gRPC to use Rakaia’s API and assess its practical impact. Our evaluation shows Rakaia: (i) consistently eliminates HOL blocking across a wide range of connection counts; (ii) achieves up to 5× higher throughput-under-SLO than KCM, Linux’s current in-kernel message API over TCP; (iii) improves gRPC’s throughput-under-SLO by up to 1.56×, reducing the userlevel CPU time needed by 23% while increasing the kernel time only by 2%.

### Scripting Netfilter with Lua: A Cooperative Kernel-Userspace Pipeline
Speakers: Lourival Vieira Neto and Md. Shehar Yaar Tausif and Firas Shaari and Marcel S. A. de Moura and Arif Alam
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/scripting-netfilter-with-lua-a-cooperative-kernel-userspace-pipeline.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper34-talk-slides/netdev-0x1a.pdf | video: https://youtu.be/TRETKtPAWck
Secure Web Gateways protect outbound HTTPS traffic, but their deep packet inspection intercepts TLS by terminating each connection through a CA installed on every client, an approach that the commodity hardware of Wi-Fi access points typically cannot sustain. This paper presents a kernel- userspace datapath pipeline that filters L7 traffic by inspect- ing DNS queries, HTTP requests, and TLS handshake meta- data rather than intercepting the connection. Both halves run in Lua: a userspace agent generates an nftables bridge rule- set that dispatches each new flow to a Netfilter hook for clas- sification. Then, nftables caches the verdict in a set, and subsequent packets bypass Lua entirely. The pipeline builds on Lunatik, our Linux kernel-scripting framework presented at Netdev 0x14 and 0x17, and contributes three new bind- ings: luanetfilter for direct Netfilter hooks, luaskb for socket-buffer access and reply synthesis, and luanftables, a userspace libnftables wrapper. On a Wi-Fi 6 access point under a combined Ethernet and Wi-Fi HTTPS work- load, the pipeline sustains 1.4 Gbps at parity with a plain Linux bridge in throughput and latency. The pipeline ships in production as Ring Zero Dome, the in-kernel engine of the NetExperience Secure Wireless Gateway on OpenWiFi access points.

### MACsec-Protected RDMA on DPUs: From Linux Netdev State to Workload Scheduling
Speakers: Alkama hasan and Vijay Ram Inavolu
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/macsec-protected-rdma-on-dpus-from-linux-netdev-state-to-workload-scheduling.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper38-talk-slides/DRANET_SEC_NetDev0x1A.pdf | video: https://youtu.be/uetdaP9m11s
Large-scale AI and HPC jobs depend on RDMA to move data between nodes with low latency and high throughput. RDMA commonly relies on userspace verbs and NIC hardware offload, with DPU-based datapaths becoming increasingly common in clustered deployments. Since that datapath often bypasses the normal host networking stack, encryption that protects ordinary host networking, such as TLS, kTLS, or in-kernel IPsec, can leave RDMA flows outside the intended protection boundary. This matters in multi-tenant clusters where model weights, inference data, parameters, and intermediate tensors cross the fabric as the industry increasingly looks to secure this layer.
MACsec (IEEE 802.1AE) operates at Layer 2, below the RDMA transport, and when offloaded to hardware, encrypts egress traffic inline below RoCE and other RDMA transports without host CPU crypto cost. The Linux kernel’s MACsec HW offload infrastructure (macsec_ops, NETIF_F_HW_MACSEC, ip macsec offload mac) already supports this, but cloud deployments also need a way to turn MACsec capability into a schedulable property, so workloads land on nodes where RDMA egress can actually be protected. DPU-based RDMA offloads add another split to the model. The host may see an RDMA-capable PCIe function, while the MACsec engine, egress port, and control plane live on the DPU side.
We build on this netdev contract by carrying DPU-side MACsec datapath state into the host-visible RDMA netdev, then showing how that state can be consumed by DRANet, a Kubernetes Dynamic Resource Allocation network driver. DRANet-Sec publishes MACsec capability alongside RDMA, SR-IOV, and NUMA locality in the node ResourceSlice. This enables a workload to request placement on nodes where RDMA egress is eligible for hardware MACsec protection without application changes. In effect, MACsec becomes a second hardware offload stacked beneath RDMA and invisible to the workload above it. On a DPU-based RDMA testbed, we show how the pieces fit together end to end, from MACsec datapath state to host netdev feature advertisement, DRANet-Sec resource publication, and scheduler-visible placement. The talk focuses on the kernel and netdev mechanics needed to keep the advertised capability aligned with the real protected datapath, a challenge that recurs for any DPU-resident offload exposed to workload scheduling

### DPU-Offloaded TLS Termination and Session Routing for Stateful MCP Traffic
Speakers: Balakrishna Bhamidipati and Vijay Ram Inavolu
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/dpu-offloaded-tls-termination-and-session-routing-for-stateful-mcp-traffic.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper39-talk-slides/netdev-39.pdf | video: https://youtu.be/peHxKX72H7U
Model Context Protocol (MCP) is fast becoming how AI agents reach tools, data, and models, increasingly deployed at scale where connection counts, compute-intensive authentication, and session affinity become infrastructure concerns. A session, once initialized, is pinned to a backend, and subsequent requests must return to it using an application-layer session identifier assigned by the backend in the initialization response and visible only after TLS termination. This affinity cannot be determined from packet fields at connection time, and today TLS termination, authentication, and routing execute on inference hosts, competing for the CPU and memory bandwidth needed by MCP servers and their backends to serve requests.
We present a DPU-offload reverse-proxy solution, built entirely from stock Linux mechanisms, that moves TLS termination, OAuth2/JWT validation, and session-aware L7 routing off the host. On the DPU the proxy performs the OpenSSL handshake in userspace and enables kernel TLS with SSL_OP_ENABLE_KTLS, delegating record processing to the Linux tls subsystem when cipher and kernel support allow it. It extracts the Mcp-Session-Id from decrypted headers and maintains an in-process session-to-backend affinity table. New sessions are assigned round-robin, while subsequent requests follow the recorded session-to-backend mapping, ensuring consistent L7 session affinity. A single-process, epoll-driven state machine multiplexes handshakes, forwarding, long-lived Server-Sent Events (SSE) relay, and teardown on client DELETE or backend 404. JWT validation on the DPU rejects unauthorized requests before they reach inference hosts, shifting the TLS and authentication trust boundary to the DPU.
Evaluation demonstrates correct session affinity, balanced backend utilization, stale-session handling, and stable kernel-TLS operation across long-lived streaming connections. The contribution is a reusable Linux-based architecture rather than a new protocol or kernel primitive. We walk through the packet path, kTLS activation and fallback, session lifecycle, backend affinity, and SSE relay, showing how the design can be reproduced on commodity DPUs without kernel modifications.

### TCP State of the union (2026)
Speakers: Eric Dumazet
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/tcp-state-of-the-union-2026.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper40-talk-slides/State of the union in TCP land in 2026 - Google Slides.pdf | video: https://youtu.be/OJnu6Pts-eo
I will present recent and upcoming TCP changes, with a focus on performance on modern platforms.

### io_uring ZCRX: Progress and Next Steps
Speakers: Pavel Begunkov
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/io_uring-zcrx-progress-and-next-steps.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper41-talk-slides/zcrx.pdf | video: https://youtu.be/oXyAF_xfdUw
io_uring ZCRX: Progress and Next Steps
Since its introduction in Linux 6.15, io_uring zero-copy receive (ZCRX) has proved to be a compelling solution for applications requiring high-performance networking without sacrificing the Linux networking stack or the existing infrastructure, tooling, and observability built around it. However, to make it a truly reliable solution for a broader set of workloads, we first need to answer a number of important questions. What happens when the refill queue is exhausted and we can’t recycle buffers back to the kernel? How can a NIC queue be shared between multiple processes? How can applications detect memory pressure before allocation failures impact performance, and what mitigation options are available?
In this talk I’ll be walking through the latest developments in ZCRX and how they address these challenges. We’ll dive into recent API additions and the motivation behind them, new features, and performance improvements. Finally, I’ll touch on future directions and what’s next for zero-copy receive in Linux.

### Networking Headless CXL Devices for AI Memory Services
Speakers: Vijay Inavolu and Gaurav Agarwal
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/networking-headless-cxl-devices-for-ai-memory-services.html | video: https://youtu.be/JaqEdCahElA
AI serving workloads are pushing past host memory hierarchies. Long-context KV caches, embedding stores, and vector databases for RAG need large capacity, high bandwidth, and low random-access latency. Composable memory fabrics based on fabric-attached CXL memory move compute close to data, where smart memory devices run search, cache lookup, compression, and quantization near device-local DDR. This wins on data movement, latency, and memory scaling, but it creates a Linux networking problem. In deployment these functions become cloud native services such as Redis, KV-cache managers and Milvus QueryNodes. Those services need IP-reachable endpoints. The CXL Type-2 device that runs them exposes a memory window, not a NIC.
In this talk, we present the Linux virtual-interface path we built for that gap, using only stock kernel pieces. A host daemon and device daemon open /dev/net/tun, configure a virtual L3 interface, and mmap the same CXL HDM-H window as a shared packet ring. ping, ssh, Redis, and TCP services work end-to-end with no new module on either side. We walk through the shared-ring design and the ordering rules needed to carry packets reliably over CXL memory and also the new host-pod bridge pattern created for this which gives device-side Linux a cluster-facing service identity over the CXL-backed virtual link, so the service is discovered, scaled, and reached by service IP while clients stay unaware of the memory window underneath. We then run those services over this path without application changes. Data-intensive work stays on device-local DDR while Linux-native networking carries only control and result traffic where our measurements which show 60x less host-link traffic than a host-side compute path, and 2.56x FAISS vector-search throughput scaling across four cards.
Networking composable memory for AI is moving fast, and the design space is wide open. Getting it right in Linux will shape how AI services scale. We bring this deliberately simple path, with the data behind it, to Netdev to spark collaboration on Linux networking mechanisms for composable memory fabrics serving AI workloads.

### Line-Rate Cybersecurity: Modern DPI and Encrypted Traffic Fingerprinting at 100 Gbps
Speakers: Luca Deri and Alfredo Cardigliano
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/line-rate-cybersecurity-modern-dpi-and-encrypted-traffic-fingerprinting-at-100-gbps.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper29-talk-slides/Netdev_0x1A_slides_deri_cardigliano_v2.pdf | video: https://youtu.be/OrL_jLspYUc
Modern network visibility and security are heavily based on understanding the behavior of the application-layer. However, ubiquitous encryption and stealthy evasion protocols have severely degraded the effectiveness of legacy firewalls. This talk proposal introduces the latest advancements in nDPI, an open-source Deep Packet Inspection (DPI) toolkit. We explore how modern DPI transcends simple payload parsing by leveraging cryptographic fingerprints to identify malicious actors despite encryption.
Furthermore, we expose structural flaws in industry-standard fingerprinting methodologies like JA3 and JA4 when confronted with ephemeral TLS extensions. Finally, we present the practical integration of nDPI within the Linux kernel firewall architecture for real-time traffic optimization, alongside architectural blueprints utilizing PF_RING and SmartNIC flow managers to achieve deterministic 100 Gbps traffic monitoring and hardware-accelerated enforcement.

### Network Precision Time with Data-plane Timestamping and Hardware-backed Scheduling
Speakers: David Zage and Srinivasan S Iyengar and Hector Blanco Alcaine and Christopher S Hall and Sreedevi Joshi and Priyalee Kushwaha
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/network-precision-time-with-data-plane-timestamping-and-hardware-backed-scheduling.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper36-talk-slides/netdev-0x1a-paper36-slides.pdf | video: https://youtu.be/DZCQGfVY7w8
Precision timing in Linux networking has largely been limited to control-plane timestamping, where timing is observed but not directly controlled, typically at rates below modern line speeds. Bringing timestamping into the data plane at line rate is challenging because driver behavior introduces variability that can undermine timestamp fidelity even with hardware assistance. We examine a hardware-centric approach that relocates clock synchronization functions from the control plane to the data plane within a \SNIC architecture. The design applies real-time clock corrections using packet-derived timestamps and a lightweight two-bit synchronization protocol.
However, timestamp accuracy is not sufficient on its own. Linux can measure time, but it does not yet reliably enforce timing in the transmit path. We explore how SO_TXTIME shifts timing from observation to control by allowing applications to explicitly schedule packet transmission. While powerful, software-based scheduling struggles to scale to modern link rates and tight jitter bounds. To complete the model, we propose hardware-timed pause semantics can be used for low-jitter transmit control. Together, data-plane timestamping, explicit transmit scheduling, and hardware-backed timing control move Linux networking toward deterministic, time-aware data planes.

### Toward Host-Pluggable Congestion Control for RDMA/IP Datacenter Transports
Speakers: Vivek Kashyap
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/talk/toward-host-pluggable-congestion-control-for-rdmaip-datacenter-transports.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper35-talk-slides/pluggable_congestion_management_netdev.pdf | video: https://youtu.be/cCkRoczzgrM
Building on the Netdev 0x19 talk on congestion control in AI/ML datacenter networks, this talk presents a concrete step toward host-pluggable congestion control for RDMA/IP datacenter transports. The previous talk surveyed modern datacenter congestion-control approaches, the limitations of fixed endpoint behavior, and the need for congestion-control algorithms to become more programmable and adaptable as workloads evolve.
This follow-up focuses on a practical implementation model that moves congestion-control policy out of fixed firmware or hardware implementations and into a host/hybrid control framework. A host component running in userspace, or alternatively in the kernel, periodically issues probe packets and uses hardware timestamping to obtain path RTT measurements. These measurements are converted into a congestion estimate for the path. The resulting control value is then distributed across the active Queue Pairs associated with that peer or path and applied through a driver-mediated QP update interface. The talk will share results from this implementation running with NIC-embedded congestion control disabled, without relying on DCQCN/PFC behavior, to demonstrate that a host-driven control loop can manage RDMA congestion.
The intent is not to claim that probe RTT is the only useful congestion signal. Rather, probe-driven feedback provides a deployable starting point for separating congestion-control policy from device-specific implementation. By commoditizing the control loop through a host-accessible framework, new algorithms can be prototyped, tuned, compared, and modified without requiring every change to be embedded directly in NIC firmware/hardware. The same host/driver framework can also be extended to incorporate additional endpoint signals such as ECN counts, ACK or progress counters, retransmit and retry events, selective-recovery information, and path-health indicators.
This flexibility matters because modern datacenter workloads are heterogeneous. AI/ML collectives, storage transfers, kv-cache movement, HPC messages, and front-end traffic may share Ethernet/IP infrastructure but have different latency, throughput, and burst behavior. A host-pluggable substrate allows congestion behavior to be adapted by workload, path, and policy rather than being constrained to a single fixed transport or firmware mechanism.
The talk will describe the probe-driven control loop, the interaction between the host congestion-control component and active QPs, early implementation results, the tradeoffs between userspace, kernel, firmware, and hardware placement, and the minimal endpoint interfaces needed to make RDMA congestion-control algorithms easier to deploy and evolve in datacenter environments.

### Promise Networks: Why a Bilateral Link Layer Solves Congestion Control at the Source
Speakers: Anjali Singhai-Jain and Chihjen Chang and Paul Borrill and David Zage
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/promise-networks-why-a-bilateral-link-layer-solves-congestion-control-at-the-source.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper46-talk-slides/promise-networks-talk.pdf | video: https://youtu.be/AzSCfNtXfJE
We are going to walk Linux Networking Humans through how to build Compassionate Networks that work for AI use cases, using Human Networks as examples to draw parallels. Our observation is that Linux Networking in general, with switches in between, is not very compassionate: it floods the network with packets, without any network resource reservations. Based on our experiments we believe there are fundamental flaws and semantic errors in the way we think about communication. Network packet drops, it turns out, are the mother of TAR (Timeout And Retry) and cause timeout storms, reconstruction storms, and metastable datacenters. So we go back to the fundamentals and ask: are packet drops necessary? As we scale the datacenter to millions of nodes, it turns out they are not – they cause congestion, transaction loss, and coherence problems in distributed systems and AI/ML infrastructures. Compassionate networks are the opposite of imposition networks, and most of our networks are imposition networks as of now. The opposite of an imposition network is a Promise Network.
The technical substance: Modern congestion control treats the network as a substrate onto which packets are imposed, and from which loss, latency, and Explicit Congestion Notification (ECN) marks must be reactively interpreted. We argue for an alternative approach that was visible in the 1976 Ethernet paper but never pushed from the transport layer down to the link layer. Metcalfe and Boggs’s end-dally in the EFTP protocol is the bilateral closure of a transmission. Open Æthernet (OAE) generalises it into a link-layer admission primitive in which every frame is gated on a peer-issued token, so a sender without one cannot transmit. The consequence is structural rather than statistical: uninvited frames never enter the fabric. Congestion control then becomes an admission discipline within the network, rather than a feedback loop above it. We frame this as a Promise Theory problem and sketch the Linux kernel surface it would require. This is a moonshot proposal, presented for community critique.

### Resilient AI Supercomputer Networking using MRC and SRv6
Speakers: Christoph Paasch and and many more
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/resilient-ai-supercomputer-networking-using-mrc-and-srv6.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper45-talk-slides/2026_MRC_netdevconf.pdf | video: https://youtu.be/qlVweM7rLx4
Tail latency dominates the performance of synchronous pretraining jobs when running at very large scales. We describe a three-pronged approach: (1) a new RDMA-based transport protocol, MRC, sprays across many paths and actively load-balances between them, eliminating the issue of flow collisions (2) the use of multi-plane Clos topologies to get the benefits of high switch radix and redundancy, allowing training clusters well over 100K GPUs to be built as two-tier topologies while increasing physical redundancy, and (3) the use of static source-routing using SRv6 to allow MRC the freedom to bypass failures by itself. We describe our experiences running MRC and static SRv6 routing in production in OpenAI and Microsoft’s largest training clusters, where it has been used to train the latest frontier models. We demonstrate how MRC allows AI training jobs to ride out many network failures that previously would have interrupted training.

### Closing Remarks
Speakers: Jamal Hadi Salim and PJ Waskiewicz
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/closing-remarks.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper50-talk-slides/Closing-0x1a.pdf | video: https://youtu.be/uS_pTJwED4I
The closing session

### Chat with the Maintainers - A Netdev Panel
Speakers: Jakub Kicinski and Eric Dumazet and Paolo Abeni
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/chat-with-the-maintainers-a-netdev-panel.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper52-talk-slides/netconf update.pdf | video: https://youtu.be/lL02fwnIYvk
Chat with the Maintainers - A Netdev Panel

### Netconf Update
Speakers: Jakub Kicinski
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/talk/netconf-update.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper51-talk-slides/netconf update.pdf | video: https://youtu.be/UMSx84HAatY
Netconf Update

## Session type: tutorial

### Making Time Uncertainty a First-Class Concept in Linux Timing
Speakers: Instructor: Maciek Machnikowski
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/tutorial/making-time-uncertainty-a-first-class-concept-in-linux-timing.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper2-talk-slides/time-uncertainty-error-bar.pdf | video: https://youtu.be/FXxOGZ87KTU
This talk presents time uncertainty as a key aspect of modern timekeeping systems. Instead of viewing timestamps as precise points, it treats them as intervals with a quantified margin of error and highlights the advantages of explicitly calculating an uncertainty window. This approach enables applications to evaluate temporal correctness explicitly, without relying on implicit assumptions about accuracy.
The presentation explores how uncertainty arises in real-world scenarios - from clock synchronization offsets, network delay variations, hardware timestamping methods, to kernel-to-user-space transfer paths - and demonstrates that neglecting these factors can lead to errors in determining order, causality, and compliance.
It then describes a model implementation of a time-uncertainty daemon and reviews the capabilities of existing Linux kernel APIs. While some data needed for uncertainty estimation (e.g., frequency offset) are available, essential elements such as oscillator stability and the “staleness” of clock calibration data are not. Hence, precise uncertainty estimation today depends on manual configuration and hardware-specific knowledge.

## Session type: workshop

### XDP Workshop
Speakers: Chair: Alexander Lobakin
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/workshop/xdp-workshop.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper3-talk-slides/XDP Workshop.pdf | video: https://youtu.be/nmyuxyIxddU
Annual XDP Workshop to discuss current topics and throw new ideas.

### What's next for the PSP Security Protocol.
Speakers: Chair: Willem de Bruijn
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/workshop/whats-next-for-the-psp-security-protocol.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper19-talk-slides/Netdevconf 2026 Panel_ What's next for the PSP Security Protocol.pdf | video: https://youtu.be/7rA3roMcrDg
PSP is an inline cryptography protocol optimized for large-scale datacenter deployments. It scales to high performance and high connection count. PSP is supported by network devices from Broadcom, Intel, Nvidia and others and by the Linux kernel as of v6.18.
Current hardware implements the initial PSP Architecture Spec. This workshop will discuss candidate extensions for the next version of PSP, such as confidential compute and multi-host support, future directions for Linux kernel PSP stack, and for support infra such as packetdrill test coverage.

### SRV6 Workshop
Speakers: Chair: Stefano Salsano
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/workshop/srv6-workshop.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper48-talk-slides/netdev-0x1A-srv6-l2-services.pdf | video: https://youtu.be/VWlH9D7FSCU
Segment Routing over IPv6 (SRv6, RFC 8986) lets an application or operator encode a packet-processing program directly in the IPv6 header. SRv6 has been supported in the Linux kernel since release 4.10, and a rich open-source ecosystem (FRR, SONiC, Cilium, VPP) has grown on top of it. Following the SRv6 workshops at Netdev 0x16 (Lisbon 2022) and 0x19 (Zagreb 2025), this edition covers three directions that directly impact the kernel datapath — source-routed AI backends, L2 services beyond VXLAN, and provider-grade SRv6 deployment with service protection — plus a short ecosystem update.
Source-routed AI backend networks - AI backends are tightly controlled fabrics where ECMP-based spreading gives little direct control over how flows map onto the fabric. Source routing with SRv6 enables deterministic, congestion-aware path placement decided at the host/NIC, removing hash collisions and reacting to link/switch failures without waiting for control-plane convergence. Our group has been exploring this direction [1], which also underpins the recently announced industry MRC protocol (covered in a main-track talk). Here we focus on what this means for Linux: efficient per-packet segment-list selection in seg6/seg6local, the interplay of eBPF/XDP and NIC offload at line rate, and the supporting role of FRR, SONiC and telemetry.
SRv6 L2 services beyond VXLAN - RFC 8986 defines the L2 endpoint behaviors (End.DX2/DT2U/DT2M) and RFC 9252 the EVPN overlay over SRv6. Kernel L2 support is still limited to the End.DX2 cross-connect, with no native L2 endpoint netdevice. A recent netdev RFC series adds End.DT2U and the sr6 Ethernet pseudowire device, enabling a VXLAN-like deployment model. We discuss the path to multipoint services, EVPN-over-SRv6 in FRR, and replacing VXLAN in cloud orchestrators (Kubernetes CNIs, OVN, OpenStack Neutron).
SRv6 for network providers and service protection - Beyond the data-center and emerging use cases above, SRv6 is gaining traction in telco/provider networks. This contribution presents an end-to-end provider-style design built entirely on the GNU/Linux and FRRouting stack: addressing and per-service VRF design, SRv6 SID allocation, BGP and IS-IS configuration, and traffic engineering — with the same end-to-end services also realized in SR-MPLS on the same network to contrast the coexistence, configuration and operation of the two technologies. To troubleshoot such networks it introduces tablesnoop [2], a lookup-level observability tool for live tracing of policy-based routing, IPv4/IPv6 route lookups, SRv6 head-end and endpoint behaviors, and (SR-)MPLS label operations (swap/push/pop), filling the gap between coarse header-level capture (tcpdump) and verbose kernel function-call tracing (pwru, retis, ipftrace2). Finally, it extends Linux SRv6 programming with Redundancy Protection (including DetNet use cases): a new R-SID format (draft-ietf-spring-sr-redundancy-protection) and SR policy head-end behaviors, with the IEEE 802.1CB FRER implementation XDPFRER [3] extended for SRv6 encapsulation. The session shows how XDP and the existing SRv6 routing stack are combined, and measures the performance impact relative to unprotected SRv6 forwarding.
The agenda also includes updates on the SRv6 open-source ecosystem:
Agenda
10:00–10:05 — Workshop Introduction — Stefano Salsano (University of Rome Tor Vergata) 10:05–10:15 — SRv6 Introduction — Ahmed Abdelsalam (Cisco) 10:15–10:25 — SRv6 for the AI Backend — Stefano Salsano (University of Rome Tor Vergata) 10:25–10:40 — SRv6 in SONiC: “Enabling AI Backend use-case and many others” — Ahmed Abdelsalam (Cisco) 10:40–10:55 — SRv6 in FRR: “5 Years of mainline support” — Carmine Scarpitta (Cisco) 10:55–11:15 — SRv6 for network providers and service protection — Ferenc Fejes (Ericsson) 11:15–11:25 — SRv6 in Linux: “9 Years of mainline support” — Andrea Mayer (University of Rome Tor Vergata) 11:25–11:45 — SRv6 Layer 2 Services support — Andrea Mayer (University of Rome Tor Vergata) 11:45–12:00 — Recap and Discussion
Workshop slides Agenda, abstract and slides (interactive decks + PDF) are collected on the workshop home page: https://netgroup.github.io/netdev-0x1A-srv6-workshop/
References
[1] C. Filsfils, P. Camarillo, A. Abdelsalam, A. Quinci, A. Tulumello, A. Mayer, P. Loreti, L. Bracciale, S. Salsano, “Toward Deterministic Path Placement in AI Backends: A Practical SRv6-Based Architecture”, IEEE CNSM 2025.
[2] tablesnoop, https://github.com/EricssonResearch/tablesnoop
[3] XDPFRER, https://github.com/EricssonResearch/xdpfrer

### Device Driver Workshop
Speakers: Chair: Paolo Abeni
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/workshop/device-driver-workshop.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper49-talk-slides/ixd_idpf_netdev0x1A.pptx.pdf | video: https://youtu.be/HwIsvLv1odQ
Current Agenda
1) How to improve the process of new device driver upstreaming, setting reasonable expectation for the submitter, the reviewers and maintainers, and eventual (process) documentation gaps to try to reduce the very high number of iterations (some) newcomers are stuck with
2)ixd and idpf are 2 intel ethernet drivers that are targeted for multiple generations of intel ethernet products in various formats like discrete PCI NIC across multiple hosts, SOC NIC, SOC SWITCH and IPU, all based on a common networking IP. idpf is a open specification based unified pf/vf ethernet driver supporting IDPF pci programming interface. It has been in the upstream linux kernel for past few years, supported in linux kernel distributions across x86/ARM architectures and widely deployed in google cloud environments. ixd is a new control+data path driver that supports switchdev framework to provision, configure, control and manage devices that expose idpf data path functions. In this talk we will go over the driver architecture, design, challenges and the strategy we are following to refactor idpf to enable sharing the code between the 2 drivers. We will also go over the various PCI functions(PF/VF), Subfunctions exposed by the device and the drivers loaded to support the possible configurations and device modes.
3) The auxiliary bus gives us a clean way to split a single PCI device into multiple cooperating drivers, but its communication model is limited: the parent (aux_device creator) exposes data to the child (aux_driver), and the child consumes them. There is no first-class mechanism for either side to notify the other of events (asynchronous or synchronous) like link change, reset, FLR, capability change, config update, teardown intent, or specific kernel API calls targeted at the child but requiring parent resources to complete.

## Session type: bof

### Network Observability BoF
Speakers: Chairs: Jason Xing and Jamal Hadi Salim
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/bof/network-observability-bof.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper12-talk-slides/netdev-0x1a-paper12.pdf | video: https://youtu.be/PJuTETh0mEQ
Network observability has a long history that can be traced back to the last century — tcpdump is a classic example. Nowadays, there is a clear trend toward relying on stronger observability capabilities distributed across different layers of the stack, enabling engineers to trace down to the root cause after an issue is reported. BPF-based tools such as bcc and bpftrace provide a general-purpose and transparent framework that helps administrators analyze a wide variety of issues without modifying the kernel or applications.
The scope of network observability spans latency measurement, throughput analysis, skb drop monitoring, protocol-specific diagnostics, reference count tracking, and more. This BoF, introduced for the first time, aims to provide an overview of existing techniques and foster discussions on emerging topics.
Apart from that, known sub-topics will be discussed:
P.S. As AI is evolving drastically, the future shape of network observability would be adjusted accordingly. Any related topics that cover this scenario are greatly welcome.

### Your Fu is Better Than Mine, 3.0! BoF
Speakers: Chairs: PJ Waskiewicz and Lourival Vieira Neto and Anjali Singhai Jain
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/bof/your-fu-is-better-than-mine-30-bof.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper20-talk-slides/Your Fu is Better Than Mine!  3.0… - Netdev 0x1a.pdf | video: https://youtu.be/feDfRT_FtKg
The ever-popular, often-requested, BoF is back, again. This is a safe space, a judgement-free zone. Come with your cool hacks, workflows, test harnesses, whatever. This is a place where all of us who have worked in this space for decades or months can converge, and share knowledge of how we work in this space better.
If you’re interested, just bring a short demo. Bonus points this year if we can ride the AI train, and bring a Skill or share effective prompts. Or a simple benchmark that you can show why it’s important to you. No judgements, just pure sharing. Often people in the audience get encouraged by who is presenting, and spontaneously decide to present something of theirs. That’s the spirit of the OG BoF. Let’s do this again, again.

### New Age Tooling BoF
Speakers: Chair: Jamal Hadi Salim
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/bof/new-age-tooling-bof.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper28-talk-slides/Yuan Tan.pdf | video: https://youtu.be/w-fGQuNK3pU
The networking subsystem has been on the receiving end of a lot of bugs discovered via AI and often patches generated by AI. In this BoF we will explore experiences and tools of trade in the security aspect of generating the bugs and fixes, effect of AI generated fixes, doing code reviews, and generating kernel patches.
Tentative agenda below. If you wish to discuss your experiences or tricks of trade, ping me.
1) Shardul Bankar
In-kernel transport protocols increasingly embed cryptography in the data path: MPTCP’s MP_JOIN HMAC, QUIC’s mandatory TLS 1.3. The crypto gates that protect the protocol also reject stateless fuzzers: random bytes fail the kernel’s token-lookup-then-HMAC chain at multiple gates. Reaching the interesting code requires an executor that constructs protocol state before the fuzzer mutates it.
We extended Hung & Amiri Sani’s BRF (arXiv:2305.08782, UC Irvine; a Syzkaller fork) for kernel transport-security protocol flows, MPTCP-first. The talk presents a prescriptive five-step guide that carries a fuzzer past a transport-security protocol’s crypto gates: BRF’s state-carrier pseudo-syscall pattern, AI-drafted syzlang and executor C under a strict VM-verification step, audit-driven coverage-gap closure, kcov on the gated softirq paths, and continuous instrumentation of whichever quality metric the generator can silently degrade. For our BPF struct_ops MPTCP scheduler generator that metric is verifier-accept rate, ~60% over 32,822 loads recorded per-load, with the rejection-reason breakdown still being categorized.
The guide is validated by two upstream-mergeable bugs on two distinct surfaces of net/mptcp/: a userspace-PM alloc-during-teardown race (https://lore.kernel.org/all/20260523212930.2957096-1-shardul. b@mpiricsoftware.com/, v2 in upstream review), and a kernel-PM-reachable close-path divide-by-zero in tcp_tso_segs (https://lore.kernel.org/all/20260525194828.1137119-1-shardul.b@mpiricsoftware.com/, v3 in review with Paolo Abeni), a partial-fix re-emergence of a 2021 bug class. We close on honest limits (N=2, no controlled Syzkaller baseline yet), ongoing MPTCP harness work (kernel-PM mode, wire-level option mutation, MP_JOIN syncookie path, HMAC reset surface); substrate extensions to QUIC and tlshd are hypothesis, not yet built.
2) Rajat Gupta
AI-generated security submissions to the kernel are increasing in volume and decreasing in quality. Reviewing each one takes significant time, and most turn out to be noise. This talk proposes a 4-gate verification framework that can filter submissions before they waste human time:
Three of the four gates are fully automatable as a CI system. The framework doesn’t replace maintainer judgment on whether a fix is in the right place, but it eliminates the 80% of submissions where the bug doesn’t exist, the RCA is hallucinated, or the patch was never tested. The talk includes concrete examples of what passes and fails each gate, and proposes this as an actionable filter for maintainers regardless of whether AI was involved in the submission.
3) Andrea Mayer and Stefano Salsano
In this talk we will discuss our adventure on analysis of an AI-generated patchset submitted to the Linux kernel SRv6 subsystem: what went wrong, why, and lessons learned for using AI in kernel development.
4) Yuan Tan
VEGA is an LLM agent for finding Linux kernel bugs. This talk shares practical lessons from building a verification-driven framework for LLM-based bug finding: turning plausible AI-generated reports into real, verifiable issues, defining which bugs are worth pursuing, and reducing false positives with PoC generation and sanitizer feedback. I will also briefly discuss what we learned from early experiments with LLM-assisted bug fixing.
5) Roman Gushchin
Sashiko was introduced mid-March 2026 and by now was adopted by most major subsystems. I plan to share some stories behind the initial development approach and architecture choices, as well as speculate on what can be ahead. I want to leave a lot of time for AMA and free-form discussions on how to properly incorporate the AI code review into the linux kernel development process and what features/qualities of Sashiko are currently limiting this process.
6) Open Session

### Could an IPv6-Only Kernel Be a Reality? An Architectural and Performance Evaluation
Speakers: Chair: Fernando Fernandez Mancera
Track: Nuts and Bolts
page: https://netdevconf.info/0x1A/sessions/bof/could-an-ipv6-only-kernel-be-a-reality-an-architectural-and-performance-evaluation.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper32-talk-slides/Could an IPv6-Only Kerne Be a Reality_ An Architectural and Performance Evaluation.pdf | video: https://youtu.be/DsKtkYXwGKo
Currently, compiling the Linux kernel with IPv6 support strictly requires the IPv4 network stack. After seeing the interest on the support for an IPv6-only kernel during the IPv6 de-modularization series earlier this year, we decided to give it a try.
In this BoF, we explore the technical feasibility and performance impact of a standalone IPv6 kernel. We present an experimental implementation and analyze its impact across three vectors: architectural changes, performance and changeset scope.
The goal of this workshop is to share our initial findings and listen to questions, suggestions, possible pain points or blockers we may have overlooked.

## Session type: keynote

### LLMs and the kernel security process
Speakers: Greg Kroah-Hartman
Track: Moonshot
page: https://netdevconf.info/0x1A/sessions/keynote/llms-and-the-kernel-security-process.html | pdf: https://netdevconf.info/0x1A/docs/netdev-0x1a-paper47-talk-slides/gregkh_netdev.pdf | video: https://youtu.be/w71JusTenBw
Right now the networking subsystem is taking the brunt of the abuse of recent LLM advances with a flood of “security” bug reports. This talk will go into a bit of the history of what has been happening, how the kernel security team has tried to make it better, and perhaps a few things that we can do in the future to reduce the load you all are currently having. Also any feedback on what the kernel security team can do better to help aliviate the load is always welcome.

