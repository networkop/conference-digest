>>> HOW TO RUN THIS <<<
This is the digest prompt for ietf-123. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/ietf-123.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/ietf-123.md
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

Below is the program for IETF 123 (Madrid) (standards). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is a standards program: working-group sessions and Internet-Drafts. Judge
what is moving toward consensus, what is newly adopted by a working group, and
what would affect implementations the PM cares about. The draft titles and
abstracts carry the substance; the sessions themselves are thin, so reason from
the drafts. Up-rank drafts that change wire formats, security properties, or
identity/authorization mechanisms; note when something is early (individual
draft) versus mature (WG last call, IETF stream).

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
conference: IETF 123 (Madrid)
type: standards
source_url: https://datatracker.ietf.org/meeting/123/agenda.json
generated: 2026-06-08
registry_key: ietf-123
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================

## Working Group: 6man
### IPv6-to-IPv6 Network Prefix Translation  (draft-bctb-6man-rfc6296-bis)
This document describes a stateless, transport-agnostic IPv6-to-IPv6
   Network Prefix Translation (NPTv6) function that provides the
   address-independence benefit associated with IPv4-to-IPv4 NAT
   (NAPT44) and provides a 1:1 relationship between addresses in the
   "inside" and "outside" prefixes, preserving end-to-end reachability
   at the network layer.

   This document obsoletes RFC 6296.

### IPv6 Hop-by-Hop Options Processing Procedures  (draft-ietf-6man-hbh-processing)
This document specifies procedures for how IPv6 Hop-by-Hop options
   are processed in IPv6 routers and hosts.  It modifies the procedures
   specified in the IPv6 Protocol Specification (RFC 8200) to make
   processing of the IPv6 Hop-by-Hop Options header practical with the
   goal of making IPv6 Hop-by-Hop options useful to deploy and use in
   the Internet.  When published, this document updates RFC 8200.

### IPv6 Node Requirements  (draft-ietf-6man-rfc8504-bis)
This document defines requirements for IPv6 nodes.  It is expected
   that IPv6 will be deployed in a wide range of devices and situations.
   Specifying the requirements for IPv6 nodes allows IPv6 to function
   well and interoperate in a large number of situations and
   deployments.

   This document obsoletes RFC 8504, and in turn RFC 6434 and its
   predecessor, RFC 4294.

### The IPv6 Compact Routing Header (CRH)  (draft-bonica-6man-comp-rtg-hdr)
This document describes an experiment in which two new IPv6 Routing
   headers are implemented and deployed.  Collectively, they are called
   the Compact Routing Headers (CRH).  Individually, they are called
   CRH-16 and CRH-32.

   One purpose of this experiment is to demonstrate that the CRH can be
   implemented and deployed in a production network.  Another purpose is
   to demonstrate that the security considerations, described in this
   document, can be addressed with access control lists.  Finally, this
   document encourages replication of the experiment.

### SRv6 Segment Identifiers in the IPv6 Addressing Architecture  (draft-ietf-6man-sids)
The data plane for Segment Routing over IPv6 (SRv6) is built using
   IPv6 as the underlying forwarding plane.  Due to this underlying use
   of IPv6, Segment Identifiers (SIDs) used by SRv6 can resemble IPv6
   addresses and behave like them while exhibiting slightly different
   behaviors in some situations.  This document explores the
   characteristics of SRv6 SIDs and focuses on the relationship of SRv6
   SIDs to the IPv6 Addressing Architecture.  This document allocates
   and makes a dedicated prefix available for SRv6 SIDs.

### IPv6 Router Advertisement Options for DNS Configuration  (draft-ietf-6man-dns-options-bis)
This document specifies IPv6 Router Advertisement options to allow IPv6 routers to advertise a list of DNS recursive server addresses and a DNS Search List to IPv6 hosts. [STANDARDS-TRACK]

### Preference for IPv6 ULAs over IPv4 addresses in RFC6724  (draft-buraglio-6man-rfc6724-update)
This document updates RFC 6724 based on operational experience gained
   since its publication over ten years ago.  In particular it updates
   the preference of Unique Local Addresses (ULAs) in the default
   address selection policy table, which as originally defined by RFC
   6724 has lower precedence than legacy IPv4 addressing.  The update
   places both IPv6 Global Unicast Addresses (GUAs) and ULAs ahead of
   all IPv4 addresses on the policy table to better suit operational
   deployment and management of ULAs in production.  In updating the RFC
   6724 default policy table, this document also demotes the preference
   for 6to4 addresses.  These changes to default behavior improve
   supportability of common use cases such as, but not limited to,
   automatic / unmanaged scenarios.  It is recognized that some less
   common deployment scenarios may require explicit configuration or
   custom changes to achieve desired operational parameters.

### Clarification of IPv6 Address Assignment Policy  (draft-carpenter-6man-addr-assign)
This document specifies the approval process for changes to the IPv6
   Address Space registry.  It also updates RFC 7249.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-carpenter-6man-addr-assign/.

   Discussion of this document takes place on the 6MAN Working Group
   mailing list (mailto:ipv6@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/ipv6/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/ipv6/.

### Signaling DHCPv6 Prefix per Client Availability to Hosts  (draft-ietf-6man-pio-pflag)
This document defines a "P" flag in the Prefix Information Option
   (PIO) of IPv6 Router Advertisements (RAs).  The flag is used to
   indicate that the network prefers that clients use the RFC9663
   deployment model instead of using individual adresses in the on-link
   prefix assigned using Stateless Address Autoconfiguration (SLAAC) or
   DHCPv6 address assignment.

   This document updates RFC4862 to indicate that the Autonomous flag in
   a PIO needs to be ignored if the PIO has the P flag set.  It also
   updates RFC4861 to specify that the P flag indicates DHCPv6 Prefix
   Delegation support for clients.

### Path MTU Discovery for IP version 6  (draft-hinden-6man-rfc1981bis)
This document describes Path MTU Discovery for IP version 6.  It is
   largely derived from RFC 1191, which describes Path MTU Discovery for
   IP version 4.  It obsoletes RFC1981.

### Analysis of the 64-bit Boundary in IPv6 Addressing  (draft-ietf-6man-why64)
The IPv6 unicast addressing format includes a separation between the prefix used to route packets to a subnet and the interface identifier used to specify a given interface connected to that subnet.  Currently, the interface identifier is defined as 64 bits long for almost every case, leaving 64 bits for the subnet prefix.  This document describes the advantages of this fixed boundary and analyzes the issues that would be involved in treating it as a variable boundary.

### Security Implications of Predictable Fragment Identification Values  (draft-ietf-6man-predictable-fragment-id)
IPv6 specifies the Fragment Header, which is employed for the fragmentation and reassembly mechanisms.  The Fragment Header contains an "Identification" field that, together with the IPv6 Source Address and the IPv6 Destination Address of a packet, identifies fragments that correspond to the same original datagram, such that they can be reassembled together by the receiving host.  The only requirement for setting the Identification field is that the corresponding value must be different than that employed for any other fragmented datagram sent recently with the same Source Address and Destination Address.  Some implementations use a simple global counter for setting the Identification field, thus leading to predictable Identification values.  This document analyzes the security implications of predictable Identification values, and provides implementation guidance for setting the Identification field of the Fragment Header, such that the aforementioned security implications are mitigated.

### Updates to the IPv6 Multicast Addressing Architecture  (draft-ietf-6man-multicast-addr-arch-update)
This document updates the IPv6 multicast addressing architecture by redefining the reserved bits as generic flag bits. The document also provides some clarifications related to the use of these flag bits.

 This document updates RFCs 3956, 3306, and 4291.

### Significance of IPv6 Interface Identifiers  (draft-ietf-6man-ug)
The IPv6 addressing architecture includes a unicast interface identifier that is used in the creation of many IPv6 addresses.  Interface identifiers are formed by a variety of methods.  This document clarifies that the bits in an interface identifier have no meaning and that the entire identifier should be treated as an opaque value.  In particular, RFC 4291 defines a method by which the Universal and Group bits of an IEEE link-layer address are mapped into an IPv6 unicast interface identifier.  This document clarifies that those two bits are significant only in the process of deriving interface identifiers from an IEEE link-layer address, and it updates RFC 4291 accordingly.

### Transmission and Processing of IPv6 Extension Headers  (draft-ietf-6man-ext-transmit)
Various IPv6 extension headers have been standardised since the IPv6 standard was first published.  This document updates RFC 2460 to clarify how intermediate nodes should deal with such extension headers and with any that are defined in the future.  It also specifies how extension headers should be registered by IANA, with a corresponding minor update to RFC 2780.

### Negotiation for IPv6 Datagram Compression Using IPv6 Control Protocol  (draft-ietf-ipv6-compression-nego-v2)
The Point-to-Point Protocol (PPP) provides a standard method of encapsulating network-layer protocol information over point-to-point links. PPP also defines an extensible Link Control Protocol, and proposes a family of Network Control Protocols (NCPs) for establishing and configuring different network-layer protocols.

 The IPv6 Control Protocol (IPV6CP), which is an NCP for a PPP link, allows for the negotiation of desirable parameters for an IPv6 interface over PPP.

 This document defines the IPv6 datagram compression option that can be negotiated by a node on the link through the IPV6CP. [STANDARDS-TRACK]

### IPv6 Node Requirements  (draft-ietf-6man-node-req-bis)
This document defines requirements for IPv6 nodes.  It is expected that IPv6 will be deployed in a wide range of devices and situations.  Specifying the requirements for IPv6 nodes allows IPv6 to function well and interoperate in a large number of situations and deployments.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Reserved IPv6 Interface Identifiers  (draft-ietf-6man-reserved-iids)
Interface identifiers in IPv6 unicast addresses are used to identify interfaces on a link.  They are required to be unique within a subnet.  Several RFCs have specified interface identifiers or identifier ranges that have a special meaning attached to them.  An IPv6 node autoconfiguring an interface identifier in these ranges will encounter unexpected consequences.  Since there is no centralized repository for such reserved identifiers, this document aims to create one. [STANDARDS-TRACK]

### IPv6 Subnet Model: The Relationship between Links and Subnet Prefixes  (draft-ietf-6man-ipv6-subnet-model)
IPv6 specifies a model of a subnet that is different than the IPv4 subnet model.  The subtlety of the differences has resulted in incorrect implementations that do not interoperate.  This document spells out the most important difference: that an IPv6 address isn't automatically associated with an IPv6 on-link prefix.  This document also updates (partially due to security concerns caused by incorrect implementations) a part of the definition of "on-link" from RFC 4861. [STANDARDS-TRACK]

### Update to RFC 3484 Default Address Selection for IPv6  (draft-ietf-6man-rfc3484-revise)
RFC 3484 describes algorithms for source address selection and for
   destination address selection.  The algorithms specify default
   behavior for all Internet Protocol version 6 (IPv6) implementations.
   This document specifies a set of updates that modify the algorithms
   and fix the known defects.

### Handling of Overlapping IPv6 Fragments  (draft-ietf-6man-overlap-fragment)
The fragmentation and reassembly algorithm specified in the base IPv6 specification allows fragments to overlap.  This document demonstrates the security issues associated with allowing overlapping fragments and updates the IPv6 specification to explicitly forbid overlapping fragments. [STANDARDS-TRACK]

### A Recommendation for IPv6 Address Text Representation  (draft-ietf-6man-text-addr-representation)
As IPv6 deployment increases, there will be a dramatic increase in the need to use IPv6 addresses in text.  While the IPv6 address architecture in Section 2.2 of RFC 4291 describes a flexible model for text representation of an IPv6 address, this flexibility has been causing problems for operators, system engineers, and users.  This document defines a canonical textual representation format.  It does not define a format for internal storage, such as within an application or database.  It is expected that the canonical format will be followed by humans and systems when representing IPv6 addresses as text, but all implementations must accept and be able to handle any legitimate RFC 4291 format. [STANDARDS-TRACK]

### Applicability Statement for the Use of IPv6 UDP Datagrams with Zero Checksums  (draft-ietf-6man-udpzero)
This document provides an applicability statement for the use of UDP transport checksums with IPv6.  It defines recommendations and requirements for the use of IPv6 UDP datagrams with a zero UDP checksum.  It describes the issues and design principles that need to be considered when UDP is used with IPv6 to support tunnel encapsulations, and it examines the role of the IPv6 UDP transport checksum.  The document also identifies issues and constraints for deployment on network paths that include middleboxes.  An appendix presents a summary of the trade-offs that were considered in evaluating the safety of the update to RFC 2460 that changes the use of the UDP checksum with IPv6.

### IANA Allocation Guidelines for the IPv6 Routing Header  (draft-ietf-6man-iana-routing-header)
This document specifies the IANA guidelines for allocating new values for the Routing Type field in the IPv6 Routing Header. [STANDARDS TRACK]

### Using 127-Bit IPv6 Prefixes on Inter-Router Links  (draft-ietf-6man-prefixlen-p2p)
On inter-router point-to-point links, it is useful, for security and other reasons, to use 127-bit IPv6 prefixes.  Such a practice parallels the use of 31-bit prefixes in IPv4.  This document specifies the motivation for, and usages of, 127-bit IPv6 prefix lengths on inter-router point-to-point links. [STANDARDS-TRACK]

### Using the IPv6 Flow Label for Equal Cost Multipath Routing and Link Aggregation in Tunnels  (draft-ietf-6man-flow-ecmp)
The IPv6 flow label has certain restrictions on its use.  This document describes how those restrictions apply when using the flow label for load balancing by equal cost multipath routing and for link aggregation, particularly for IP-in-IPv6 tunneled traffic. [STANDARDS-TRACK]

### Rationale for Update to the IPv6 Flow Label Specification  (draft-ietf-6man-flow-update)
Various published proposals for use of the IPv6 flow label are incompatible with its original specification in RFC 3697.  Furthermore, very little practical use is made of the flow label, partly due to some uncertainties about the correct interpretation of the specification.  This document discusses and motivates changes to the specification in order to clarify it and to introduce some additional flexibility.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### The Routing Protocol for Low-Power and Lossy Networks (RPL) Option for Carrying RPL Information in Data-Plane Datagrams  (draft-ietf-6man-rpl-option)
The Routing Protocol for Low-Power and Lossy Networks (RPL) includes routing information in data-plane datagrams to quickly identify inconsistencies in the routing topology.  This document describes the RPL Option for use among RPL routers to include such routing information. [STANDARDS-TRACK]

### Interface Identifier Assignment in IPv6 SLAAC  (draft-ietf-6man-neighbor-inform)
This document proposes an optional mechanism as part of IPv6
Stateless Address Autoconfiguration for distribution of unique
interface identifiers to IPv6 hosts on a link.  Hosts can then use
these unique interface identifiers to generate unique autoconfigured
link local and global unicast addresses.

This mechanism is intended for use in networks where link layer
identifiers are used for generating interface identifiers and where
non unique link layer identifiers will result in duplicate link local
addresses.  An example of such network is Ethernet Broadband access
networks.

### An IPv6 Routing Header for Source Routes with the Routing Protocol for Low-Power and Lossy Networks (RPL)  (draft-ietf-6man-rpl-routing-header)
In Low-Power and Lossy Networks (LLNs), memory constraints on routers may limit them to maintaining, at most, a few routes.  In some configurations, it is necessary to use these memory-constrained routers to deliver datagrams to nodes within the LLN.  The Routing Protocol for Low-Power and Lossy Networks (RPL) can be used in some deployments to store most, if not all, routes on one (e.g., the Directed Acyclic Graph (DAG) root) or a few routers and forward the IPv6 datagram using a source routing technique to avoid large routing tables on memory-constrained routers.  This document specifies a new IPv6 Routing header type for delivering datagrams within a RPL routing domain. [STANDARDS-TRACK]

### A Uniform Format for IPv6 Extension Headers  (draft-ietf-6man-exthdr)
In IPv6, optional internet-layer information is encoded in separate headers that may be placed between the IPv6 header and the transport-layer header.  There are a small number of such extension headers currently defined.  This document describes the issues that can arise when defining new extension headers and discusses the alternate extension mechanisms in IPv6.  It also provides a common format for defining any new IPv6 extension headers, if they are needed. [STANDARDS-TRACK]

### IPv6 Router Advertisement Options for DNS Configuration  (draft-ietf-6man-rdnss-rfc6106bis)
This document specifies IPv6 Router Advertisement (RA) options (called "DNS RA options") to allow IPv6 routers to advertise a list of DNS Recursive Server Addresses and a DNS Search List to IPv6 hosts.

 This document, which obsoletes RFC 6106, defines a higher default value of the lifetime of the DNS RA options to reduce the likelihood of expiry of the options on links with a relatively high rate of packet loss.

### Distributing Address Selection Policy Using DHCPv6  (draft-ietf-6man-addr-select-opt)
RFC 6724 defines default address selection mechanisms for IPv6 that allow nodes to select an appropriate address when faced with multiple source and/or destination addresses to choose between.  RFC 6724 allows for the future definition of methods to administratively configure the address selection policy information.  This document defines a new DHCPv6 option for such configuration, allowing a site administrator to distribute address selection policy overriding the default address selection parameters and policy table, and thus allowing the administrator to control the address selection behavior of nodes in their site.

### The Line-Identification Option  (draft-ietf-6man-lineid)
In Ethernet-based aggregation networks, several subscriber premises may be logically connected to the same interface of an Edge Router.  This document proposes a method for the Edge Router to identify the subscriber premises using the contents of the received Router Solicitation messages.  The applicability is limited to broadband network deployment scenarios in which multiple user ports are mapped to the same virtual interface on the Edge Router. [STANDARDS-TRACK]

### Duplicate Address Detection Proxy  (draft-ietf-6man-dad-proxy)
The document describes a proxy-based mechanism allowing the use of Duplicate Address Detection (DAD) by IPv6 nodes in a point-to-multipoint architecture with a "split-horizon" forwarding scheme, primarily deployed for Digital Subscriber Line (DSL) and Fiber access architectures.  Based on the DAD signaling, the first-hop router stores in a Binding Table all known IPv6 addresses used on a point-to-multipoint domain (e.g., VLAN).  When a node performs DAD for an address already used by another node, the first-hop router defends the address rather than the device using the address.

### IPv6 Flow Label Specification  (draft-ietf-6man-flow-3697bis)
This document specifies the IPv6 Flow Label field and the minimum requirements for IPv6 nodes labeling flows, IPv6 nodes forwarding labeled packets, and flow state establishment methods. Even when mentioned as examples of possible uses of the flow labeling, more detailed requirements for specific use cases are out of the scope for this document.

 The usage of the Flow Label field enables efficient IPv6 flow classification based only on IPv6 main header fields in fixed positions. [STANDARDS-TRACK]

### IPv6 and UDP Checksums for Tunneled Packets  (draft-ietf-6man-udpchecksums)
This document updates the IPv6 specification (RFC 2460) to improve performance when a tunnel protocol uses UDP with IPv6 to tunnel packets.  The performance improvement is obtained by relaxing the IPv6 UDP checksum requirement for tunnel protocols whose header information is protected on the "inner" packet being carried.  Relaxing this requirement removes the overhead associated with the computation of UDP checksums on IPv6 packets that carry the tunnel protocol packets.  This specification describes how the IPv6 UDP checksum requirement can be relaxed when the encapsulated packet itself contains a checksum.  It also describes the limitations and risks of this approach and discusses the restrictions on the use of this method.

### Neighbor Unreachability Detection Is Too Impatient  (draft-ietf-6man-impatient-nud)
IPv6 Neighbor Discovery includes Neighbor Unreachability Detection.  That function is very useful when a host has an alternative neighbor -- for instance, when there are multiple default routers -- since it allows the host to switch to the alternative neighbor in a short time.  By default, this time is 3 seconds after the node starts probing.  However, if there are no alternative neighbors, this timeout behavior is far too impatient.  This document specifies relaxed rules for Neighbor Discovery retransmissions that allow an implementation to choose different timeout behavior based on whether or not there are alternative neighbors.  This document updates RFC 4861.

### RFC 3627 to Historic Status  (draft-ietf-6man-3627-historic)
This document moves "Use of /127 Prefix Length Between Routers Considered Harmful" (RFC 3627) to Historic status to reflect the updated guidance contained in "Using 127-Bit IPv6 Prefixes on Inter- Router Links" (RFC 6164).  A Standards Track document supersedes an informational document; therefore, guidance provided in RFC 6164 is to be followed when the two documents are in conflict.  This document links the two RFCs so that the IETF's updated guidance on this topic is clearer.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Processing of IPv6 "Atomic" Fragments  (draft-ietf-6man-ipv6-atomic-fragments)
The IPv6 specification allows packets to contain a Fragment Header without the packet being actually fragmented into multiple pieces (we refer to these packets as "atomic fragments").  Such packets are typically sent by hosts that have received an ICMPv6 "Packet Too Big" error message that advertises a Next-Hop MTU smaller than 1280 bytes, and are currently processed by some implementations as normal "fragmented traffic" (i.e., they are "reassembled" with any other queued fragments that supposedly correspond to the same original packet).  Thus, an attacker can cause hosts to employ atomic fragments by forging ICMPv6 "Packet Too Big" error messages, and then launch any fragmentation-based attacks against such traffic.  This document discusses the generation of the aforementioned atomic fragments and the corresponding security implications.  Additionally, this document formally updates RFC 2460 and RFC 5722, such that IPv6 atomic fragments are processed independently of any other fragments, thus completely eliminating the aforementioned attack vector.

### Representing IPv6 Zone Identifiers in Address Literals and Uniform Resource Identifiers  (draft-ietf-6man-uri-zoneid)
This document describes how the zone identifier of an IPv6 scoped address, defined as <zone_id> in the IPv6 Scoped Address Architecture (RFC 4007), can be represented in a literal IPv6 address and in a Uniform Resource Identifier that includes such a literal address.  It updates the URI Generic Syntax specification (RFC 3986) accordingly.

### Default Address Selection for Internet Protocol Version 6 (IPv6)  (draft-ietf-6man-rfc3484bis)
This document describes two algorithms, one for source address selection and one for destination address selection. The algorithms specify default behavior for all Internet Protocol version 6 (IPv6) implementations. They do not override choices made by applications or upper-layer protocols, nor do they preclude the development of more advanced mechanisms for address selection. The two algorithms share a common context, including an optional mechanism for allowing administrators to provide policy that can override the default behavior. In dual-stack implementations, the destination address selection algorithm can consider both IPv4 and IPv6 addresses -- depending on the available source addresses, the algorithm might prefer IPv6 addresses over IPv4 addresses, or vice versa.

 Default address selection as defined in this specification applies to all IPv6 nodes, including both hosts and routers. This document obsoletes RFC 3484. [STANDARDS-TRACK]

### Transmission of IPv6 over MS/TP Networks  (draft-ietf-6man-6lobac)
MS/TP (Master-Slave/Token-Passing) is a contention-free access method
   for the RS-485 physical layer that is used extensively in building
   automation networks.  This document describes the frame format for
   transmission of IPv6 packets and the method of forming link-local and
   statelessly autoconfigured IPv6 addresses on MS/TP networks.

### Enhanced Duplicate Address Detection  (draft-ietf-6man-enhanced-dad)
IPv6 Loopback Suppression and Duplicate Address Detection (DAD) are discussed in Appendix A of RFC 4862.  That specification mentions a hardware-assisted mechanism to detect looped back DAD messages.  If hardware cannot suppress looped back DAD messages, a software solution is required.  Several service provider communities have expressed a need for automated detection of looped back Neighbor Discovery (ND) messages used by DAD.  This document includes mitigation techniques and outlines the Enhanced DAD algorithm to automate the detection of looped back IPv6 ND messages used by DAD.  For network loopback tests, the Enhanced DAD algorithm allows IPv6 to self-heal after a loopback is placed and removed.  Further, for certain access networks, this document automates resolving a specific duplicate address conflict.  This document updates RFCs 4429, 4861, and 4862.

### A Method for Generating Semantically Opaque Interface Identifiers with IPv6 Stateless Address Autoconfiguration (SLAAC)  (draft-ietf-6man-stable-privacy-addresses)
This document specifies a method for generating IPv6 Interface Identifiers to be used with IPv6 Stateless Address Autoconfiguration (SLAAC), such that an IPv6 address configured using this method is stable within each subnet, but the corresponding Interface Identifier changes when the host moves from one network to another.  This method is meant to be an alternative to generating Interface Identifiers based on hardware addresses (e.g., IEEE LAN Media Access Control (MAC) addresses), such that the benefits of stable addresses can be achieved without sacrificing the security and privacy of users.  The method specified in this document applies to all prefixes a host may be employing, including link-local, global, and unique-local prefixes (and their corresponding addresses).

### Security Implications of IPv6 Fragmentation with IPv6 Neighbor Discovery  (draft-ietf-6man-nd-extension-headers)
This document analyzes the security implications of employing IPv6 fragmentation with Neighbor Discovery (ND) messages.  It updates RFC 4861 such that use of the IPv6 Fragmentation Header is forbidden in all Neighbor Discovery messages, thus allowing for simple and effective countermeasures for Neighbor Discovery attacks.  Finally, it discusses the security implications of using IPv6 fragmentation with SEcure Neighbor Discovery (SEND) and formally updates RFC 3971 to provide advice regarding how the aforementioned security implications can be mitigated.

### Implications of Oversized IPv6 Header Chains  (draft-ietf-6man-oversized-header-chain)
The IPv6 specification allows IPv6 Header Chains of an arbitrary size.  The specification also allows options that can, in turn, extend each of the headers.  In those scenarios in which the IPv6 Header Chain or options are unusually long and packets are fragmented, or scenarios in which the fragment size is very small, the First Fragment of a packet may fail to include the entire IPv6 Header Chain.  This document discusses the interoperability and security problems of such traffic, and updates RFC 2460 such that the First Fragment of a packet is required to contain the entire IPv6 Header Chain.

### Packet loss resiliency for Router Solicitations  (draft-krishnan-6man-resilient-rs)
When an interface on a host is initialized, the host transmits Router
   Solicitations in order to minimize the amount of time it needs to
   wait until the next unsolicited multicast Router Advertisement is
   received.  In certain scenarios, these router solicitations
   transmitted by the host might be lost.  This document specifies a
   mechanism for hosts to cope with the loss of the initial Router
   Solicitations.  Furthermore, on some links, unsolicited multicast
   Router Advertisements are never sent and the mechanism in this
   document is intended to work even in such scenarios.

### Packet-Loss Resiliency for Router Solicitations  (draft-ietf-6man-resilient-rs)
When an interface on a host is initialized, the host transmits Router Solicitations in order to minimize the amount of time it needs to wait until the next unsolicited multicast Router Advertisement is received.  In certain scenarios, these Router Solicitations transmitted by the host might be lost.  This document specifies a mechanism for hosts to cope with the loss of the initial Router Solicitations.

### Internet Protocol, Version 6 (IPv6) Specification  (draft-ietf-6man-rfc2460bis)
This document specifies version 6 of the Internet Protocol (IPv6).  It obsoletes RFC 2460.

### IPv6 Multicast Address Scopes  (draft-ietf-6man-multicast-scopes)
This document updates the definitions of IPv6 multicast scopes and therefore updates RFCs 4007 and 4291.

### Security and Privacy Considerations for IPv6 Address Generation Mechanisms  (draft-ietf-6man-ipv6-address-generation-privacy)
This document discusses privacy and security considerations for several IPv6 address generation mechanisms, both standardized and non-standardized.  It evaluates how different mechanisms mitigate different threats and the trade-offs that implementors, developers, and users face in choosing different addresses or address generation mechanisms.

### Analysis of the 64-bit Boundary in IPv6 Addressing  (draft-carpenter-6man-why64)
The IPv6 unicast addressing format includes a separation between the
   prefix used to route packets to a subnet and the interface identifier
   used to specify a given interface connected to that subnet.
   Historically the interface identifier has been defined as 64 bits
   long, leaving 64 bits for the prefix.  This document discusses the
   reasons for this fixed boundary and the issues involved in treating
   it as a variable boundary.

### Recommendation on Stable IPv6 Interface Identifiers  (draft-ietf-6man-default-iids)
This document changes the recommended default Interface Identifier (IID) generation scheme for cases where Stateless Address Autoconfiguration (SLAAC) is used to generate a stable IPv6 address.  It recommends using the mechanism specified in RFC 7217 in such cases, and recommends against embedding stable link-layer addresses in IPv6 IIDs.  It formally updates RFC 2464, RFC 2467, RFC 2470, RFC 2491, RFC 2492, RFC 2497, RFC 2590, RFC 3146, RFC 3572, RFC 4291, RFC 4338, RFC 4391, RFC 5072, and RFC 5121.  This document does not change any existing recommendations concerning the use of temporary addresses as specified in RFC 4941.

### IPv6 Segment Routing Header (SRH)  (draft-previdi-6man-segment-routing-header)
Segment Routing (SR) allows a node to steer a packet through a
   controlled set of instructions, called segments, by prepending a SR
   header to the packet.  A segment can represent any instruction,
   topological or service-based.  SR allows to enforce a flow through
   any path (topological, or application/service based) while
   maintaining per-flow state only at the ingress node to the SR domain.

   Segment Routing can be applied to the IPv6 data plane with the
   addition of a new type of Routing Extension Header.  This draft
   describes the Segment Routing Extension Header Type and how it is
   used by SR capable nodes.

### Support for adjustable maximum router lifetimes per-link  (draft-krishnan-6man-maxra)
The neighbor discovery protocol specifies the maximum time allowed
   between sending unsolicited multicast Router Advertisements from a
   router interface as well as the maximum router lifetime.  It also
   allows the limits to be overridden by link-layer specific documents.
   This document allows for overriding these values on a per-link basis.

### Generation of IPv6 Atomic Fragments Considered Harmful  (draft-ietf-6man-deprecate-atomfrag-generation)
This document discusses the security implications of the generation of IPv6 atomic fragments and a number of interoperability issues associated with IPv6 atomic fragments.  It concludes that the aforementioned functionality is undesirable and thus documents the motivation for removing this functionality from an upcoming revision of the core IPv6 protocol specification (RFC 2460).

### IPv6 Router Advertisement Options for DNS Configuration  (draft-jeong-6man-rdnss-rfc6106-bis)
This document specifies IPv6 Router Advertisement options to allow
   IPv6 routers to advertise a list of DNS recursive server addresses
   and a DNS Search List to IPv6 hosts.

   This document obsoletes RFC 6106 and allows a higher default value of
   the lifetime of the RA DNS options to avoid the frequent expiry of
   the options on links with a relatively high rate of packet loss.

### IP Version 6 Addressing Architecture  (draft-hinden-6man-rfc4291bis)
This specification defines the addressing architecture of the IP
   Version 6 (IPv6) protocol.  The document includes the IPv6 addressing
   model, text representations of IPv6 addresses, definition of IPv6
   unicast addresses, anycast addresses, and multicast addresses, and an
   IPv6 node's required addresses.

   This document obsoletes RFC 4291, "IP Version 6 Addressing
   Architecture".

### Republishing the IPV6-MIB modules as obsolete  (draft-fenner-ipv6-mibs-obsolete)
In 2005, the IPv6 MIB update group published updated versions of the
   IP-MIB, UDP-MIB, TCP-MIB and IP-FORWARD-MIB modules, which use the
   InetAddressType/InetAddress construct to handle IPv4 and IPv6 in the
   same table.  This document contains versions of the obsoleted
   IPV6-MIB, IPV6-TC, IPV6-ICMP-MIB, IPV6-TCP-MIB and IPV6-UDP-MIB
   modules, for the purpose of updating MIB module repositories.

## Working Group: acme
### Automated Certificate Management Environment (ACME) Scoped DNS Challenges  (draft-ietf-acme-scoped-dns-challenges)
This document outlines a new challenge for the ACME protocol,
   enabling an ACME client to answer a domain control validation
   challenge from an ACME server using a DNS resource linked to the ACME
   Account ID.  This allows multiple systems or environments to handle
   challenge-solving for a single domain.

### Automated Certificate Management Environment (ACME) Challenges Using an Authority Token  (draft-ietf-acme-authority-token)
Some proposed extensions to the Automated Certificate Management Environment (ACME) rely on proving eligibility for certificates through consulting an external authority that issues a token according to a particular policy.  This document specifies a generic Authority Token Challenge for ACME that supports subtype claims for different identifiers or namespaces that can be defined separately for specific applications.

### TNAuthList Profile of Automated Certificate Management Environment (ACME) Authority Token  (draft-ietf-acme-authority-token-tnauthlist)
This document defines a profile of the Automated Certificate Management Environment (ACME) Authority Token for the automated and authorized creation of certificates for Voice over IP (VoIP) telephone providers to support Secure Telephone Identity (STI) using the TNAuthList defined by STI certificates.

### Extensions to Automatic Certificate Management Environment for End-User S/MIME Certificates  (draft-ietf-acme-email-smime)
This document specifies identifiers and challenges required to enable the Automated Certificate Management Environment (ACME) to issue certificates for use by email users that want to use S/MIME.

### Automated Certificate Management Environment (ACME) for Subdomains  (draft-ietf-acme-subdomains)
This document specifies how Automated Certificate Management Environment (ACME) can be used by a client to obtain a certificate for a subdomain identifier from a certification authority.  Additionally, this document specifies how a client can fulfill a challenge against an ancestor domain but may not need to fulfill a challenge against the explicit subdomain if certification authority policy allows issuance of the subdomain certificate without explicit subdomain ownership proof.

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge  (draft-ietf-acme-dns-account-challenge)
This document outlines a new challenge for the ACME protocol,
   enabling an ACME client to answer a domain control validation
   challenge from an ACME server using a DNS resource linked to the ACME
   Account ID.  This allows multiple systems or environments to handle
   challenge-solving for a single domain.

### ACME Identifiers and Challenges for VoIP Service Providers  (draft-ietf-acme-service-provider)
This document specifies identifiers and challenges required to enable
   the Automated Certificate Management Environment (ACME) to issue
   certificates for VoIP service providers to support Secure Telephony
   Identity (STI).

### Automatic Certificate Management Environment (ACME)  (draft-ietf-acme-acme)
Public Key Infrastructure using X.509 (PKIX) certificates are used for a number of purposes, the most significant of which is the authentication of domain names.  Thus, certification authorities (CAs) in the Web PKI are trusted to verify that an applicant for a certificate legitimately represents the domain name(s) in the certificate.  As of this writing, this verification is done through a collection of ad hoc mechanisms.  This document describes a protocol that a CA and an applicant can use to automate the process of verification and certificate issuance.  The protocol also provides facilities for other certificate management functions, such as certificate revocation.

### CA Account URI Binding for CAA Records  (draft-landau-acme-caa)
The CAA DNS record allows a domain to communicate issuance policy to
   CAs, but only allows a domain to define policy with CA-level
   granularity.  However, the CAA specification also provides facilities
   for extension to admit more granular, CA-specific policy.  This
   specification defines two such parameters, one allowing specific
   accounts of a CA to be identified by URI and one allowing specific
   methods of domain control validation as defined by the ACME protocol
   to be required.

### Certification Authority Authorization (CAA) Record Extensions for Account URI and Automatic Certificate Management Environment (ACME) Method Binding  (draft-ietf-acme-caa)
The Certification Authority Authorization (CAA) DNS record allows a domain to communicate an issuance policy to Certification Authorities (CAs) but only allows a domain to define a policy with CA-level granularity.  However, the CAA specification (RFC 8659) also provides facilities for an extension to admit a more granular, CA-specific policy.  This specification defines two such parameters: one allowing specific accounts of a CA to be identified by URIs and one allowing specific methods of domain control validation as defined by the Automatic Certificate Management Environment (ACME) protocol to be required.

### Support for Short-Term, Automatically Renewed (STAR) Certificates in the Automated Certificate Management Environment (ACME)  (draft-ietf-acme-star)
Public key certificates need to be revoked when they are compromised, that is, when the associated private key is exposed to an unauthorized entity.  However, the revocation process is often unreliable.  An alternative to revocation is issuing a sequence of certificates, each with a short validity period, and terminating the sequence upon compromise.  This memo proposes an Automated Certificate Management Environment (ACME) extension to enable the issuance of Short-Term, Automatically Renewed (STAR) X.509 certificates.

### Extensions to Automatic Certificate Management Environment for email TLS  (draft-ietf-acme-email-tls)
This document specifies identifiers and challenges required to enable
   the Automated Certificate Management Environment (ACME) to issue
   certificates for use by TLS email services.

### ACME Identifiers and Challenges for Telephone Numbers  (draft-ietf-acme-telephone)
This document specifies identifiers and challenges required to enable
   the Automated Certificate Management Environment (ACME) to issue
   certificate for telephonoe numbers.

### Automated Certificate Management Environment (ACME) IP Identifier Validation Extension  (draft-ietf-acme-ip)
This document specifies identifiers and challenges required to enable the Automated Certificate Management Environment (ACME) to issue certificates for IP addresses.

### Automated Certificate Management Environment (ACME) TLS Application-Layer Protocol Negotiation (ALPN) Challenge Extension  (draft-ietf-acme-tls-alpn)
This document specifies a new challenge for the Automated Certificate Management Environment (ACME) protocol that allows for domain control validation using TLS.

### An Automatic Certificate Management Environment (ACME) Profile for Generating Delegated Certificates  (draft-ietf-acme-star-delegation)
This document defines a profile of the Automatic Certificate Management Environment (ACME) protocol by which the holder of an identifier (e.g., a domain name) can allow a third party to obtain an X.509 certificate such that the certificate subject is the delegated identifier while the certified public key corresponds to a private key controlled by the third party.  A primary use case is that of a Content Delivery Network (CDN), the third party, terminating TLS sessions on behalf of a content provider (the holder of a domain name).  The presented mechanism allows the holder of the identifier to retain control over the delegation and revoke it at any time.  Importantly, this mechanism does not require any modification to the deployed TLS clients and servers.

### ACME End User Client and Code Signing Certificates  (draft-moriarty-acme-client)
Automated Certificate Management Environment (ACME) core protocol
   addresses the use case of web server certificates for TLS.  This
   document extends the ACME protocol to support end user client, device
   client, and code signing certificates.

### Automated Certificate Management Environment (ACME) Delay-Tolerant Networking (DTN) Node ID Validation Extension  (draft-sipos-acme-dtnnodeid)
This document specifies an extension to the Automated Certificate
   Management Environment (ACME) protocol which allows validating the
   Delay-Tolerant Networking (DTN) Node ID for an ACME client.  The use
   of a Uniform Resource Identifier (URI) as ACME identifier is also
   specified.

### Automated Certificate Management Environment (ACME) Renewal Information (ARI) Extension  (draft-ietf-acme-ari)
This document specifies how an ACME server may provide suggestions to
   ACME clients as to when they should attempt to renew their
   certificates.  This allows servers to mitigate load spikes, and
   ensures clients do not make false assumptions about appropriate
   certificate renewal periods.

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge  (draft-ietf-acme-dns-account-01)
This document outlines a new challenge for the ACME protocol,
   enabling an ACME client to answer a domain control validation
   challenge from an ACME server using a DNS resource linked to the ACME
   Account ID.  This allows multiple systems or environments to handle
   challenge-solving for a single domain.

### Automated Certificate Management Environment (ACME) Extension for Public Key Challenges  (draft-geng-acme-public-key)
The current ACME protocol [RFC8555] requires applicants to submit a
   PKCS#10 Certificate Signing Request (CSR) during the finalization
   phase.  The construction, ASN.1 encoding, and transmission of the CSR
   impose additional implementation burdens on both the client
   (especially resource-constrained devices) and the server.  Moreover,
   the CSR cannot prevent a public key from being replaced by an
   intermediary at the protocol level.

   This document introduces the "pk-01" challenge extension based on the
   ACME protocol.  Its core mechanism is as follows: the applicant
   declares the public key to be authenticated during the "newOrder"
   phase and completes the Proof of Possession (PoP) by signing with the
   private key during the challenge phase.  Since the public key is
   declared when the order is created and verified during the challenge
   phase, there is no need to submit a CSR during the finalization
   phase; the ACME server can issue the certificate directly based on
   the verified public key, thereby eliminating the CSR at the protocol
   level.

   The "pk-01" challenge supports two verification modes via the
   pop_mode field:

### Automated Certificate Management Environment (ACME) Profiles Extension  (draft-aaron-acme-profiles)
This document defines how an ACME Server may offer a selection of
   different certificate profiles to ACME Clients, and how those clients
   may indicate which profile they want.

### Automated Certificate Management Environment (ACME) Remote Attestation Identifier and Challenge Type  (draft-ietf-acme-rats)
This document describes an approach where an ACME Server can
   challenge an ACME Client to provide Evidence, Endorsements, or
   Attestation Result according to the Remote ATtestation procedureS
   (RATS) framework in any format supported by the Conceptual Message
   Wrapper (CMW).

   The ACME Server can optionally challenge the Client for specific
   claims that it wishes attestation for.

### ACME End User Client and Code Signing Certificates  (draft-ietf-acme-client)
Automated Certificate Management Environment (ACME) core protocol
   addresses the use case of web server certificates for TLS.  This
   document extends the ACME protocol to add 3 challenge types that may
   support service account authentication credentials, micro-service
   accounts credentials, device client, code signing, document signing
   certificates and keys.

### Automated Certificate Management Environment (ACME) Device Attestation Extension  (draft-acme-device-attest)
This document specifies new identifiers and a challenge for the
   Automated Certificate Management Environment (ACME) protocol which
   allows validating the identity of a device using attestation.

### JWTClaimConstraints profile of ACME Authority Token  (draft-wendt-acme-authority-token-jwtclaimcon)
This document defines an authority token profile for handling the
   validation of JWTClaimConstraints and EnhancedJWTClaimConstraints.
   This profile follows the model established in Authority Token for the
   validation of TNAuthList but is specifically tailored for the
   JWTClaimConstraints certificate extensions.  The profile enables
   validation and challenge processes necessary to support certificates
   containing both TNAuthList and JWTClaimConstraints, particularly in
   the context of Secure Telephone Identity (STI).

### Automated Certificate Management Environment (ACME) Extensions for ".onion" Special-Use Domain Names  (draft-ietf-acme-onion)
The document defines extensions to the Automated Certificate
   Management Environment (ACME) to allow for the automatic issuance of
   certificates to Tor hidden services (".onion" Special-Use Domain
   Names).

Discussion

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/AS207960/acme-onion.

   The project website and a reference implementation can be found at
   https://acmeforonions.org.

### Automated Certificate Management Environment (ACME) Profile Sets  (draft-davidben-acme-profile-sets)
This document defines how an ACME Server may indicate collections of
   related certificate profiles to ACME Clients.

### Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation  (draft-sheurich-acme-dns-persist)
This document specifies "dns-persist-01", a new validation method for
   the Automated Certificate Management Environment (ACME) protocol.
   This method allows a Certification Authority (CA) to verify control
   over a domain by confirming the presence of a persistent DNS TXT
   record containing CA and account identification information.  This
   method is particularly suited for environments where traditional
   challenge methods are impractical, such as IoT deployments, multi-
   tenant platforms, and scenarios requiring batch certificate
   operations.  The validation method is designed with a strong focus on
   security and robustness, incorporating widely adopted industry best
   practices for persistent domain control validation.  This design aims
   to make it suitable for Certification Authorities operating under
   various policy environments, including those that align with the CA/
   Browser Forum Baseline Requirements.

### Automated Certificate Management Environment (ACME) Profiles Extension  (draft-ietf-acme-profiles)
This document defines how an ACME Server may offer a selection of
   different certificate profiles to ACME Clients, and how those clients
   may indicate which profile they want.

### Automated Certificate Management Environment (ACME) SRV Identifier Validation Extension  (draft-lebihan-srv-identifier-validation-extension)
This document specifies an extension to the Automated Certificate
   Management Environment (ACME) protocol to enable validation and
   issuance of certificates containing SRV-ID identifiers as defined in
   RFC 4985.  This allows secure delegation of services where the
   service domain and hosting infrastructure are controlled by different
   entities, addressing the multi-tenancy challenges in protocols that
   use SRV records for service discovery.

### Automated Certificate Management Environment (ACME) rats Identifier and Challenge Type  (draft-liu-acme-rats)
This document describes an approach where an ACME Server can
   challenge an ACME Client to provide a Remote Attestation Evidence or
   Remote Attestation Result in any format supported by the Conceptual
   Message Wrapper.

   The ACME Server can optionally challenge the Client for specific
   claims that it wishes attestation for.

### ACME Integrations for Device Certificate Enrollment  (draft-ietf-acme-integrations)
This document outlines multiple advanced use cases and integrations
   that ACME facilitates without any modifications or enhancements
   required to the base ACME specification.  The use cases include ACME
   integration with EST, BRSKI and TEAP.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0  (draft-demarco-acme-openid-federation)
The Automatic Certificate Management Environment (ACME) protocol
   allows server operators to obtain TLS certificates for their
   websites, based on a demonstration of control over the website's
   domain via a fully-automated challenge/response protocol.

   OpenID Federation 1.0 defines how to build a trust infrastructure
   using a trusted third-party model.  It uses a trust evaluation
   mechanism to attest to the possession of private keys, protocol
   specific metadata and miscellaneous administrative and technical
   information related to a specific entity.

   This document defines how X.509 certificates associated with a given
   OpenID Federation Entity can be issued by an X.509 Certification
   Authority through the ACME protocol to the organizations which are
   part of a federation built on top of OpenID Federation 1.0.

### Automated Certificate Management Environment (ACME) Challenge for Persistent DNS TXT Record Validation  (draft-ietf-acme-dns-persist)
This document specifies "dns-persist-01", a new validation method for
   the Automated Certificate Management Environment (ACME) protocol.
   This method allows a Certification Authority (CA) to verify control
   over a domain by confirming the presence of a persistent DNS TXT
   record containing CA and account identification information.  This
   method is particularly suited for environments where traditional
   challenge methods are impractical, such as multi-tenant hosting
   platforms, enterprise DNS environments, and IoT deployments.  The
   validation method is designed with a strong focus on security and
   robustness, incorporating widely adopted industry best practices for
   persistent domain control validation.  This design aims to make it
   suitable for Certification Authorities operating under various policy
   environments, including those that align with the CA/Browser Forum
   Baseline Requirements.

### Automated Certificate Management Environment (ACME) Delay-Tolerant Networking (DTN) Node ID Validation Extension  (draft-ietf-acme-dtnnodeid)
This document specifies an extension to the Automated Certificate
   Management Environment (ACME) protocol which allows an ACME server to
   validate the Delay-Tolerant Networking (DTN) Node ID for an ACME
   client.  A DTN Node ID is an identifier used in the Bundle Protocol
   (BP) to name a "singleton endpoint", one which is registered on a
   single BP node.  The DTN Node ID is encoded as a certificate Subject
   Alternative Name (SAN) of type otherName with a name form of
   BundleEID and as an ACME Identifier type "bundleEID".

### Automated Certificate Management Environment (ACME) DNS Labeled With ACME Account ID Challenge  (draft-ietf-acme-dns-account-label)
This document outlines a new DNS-based challenge type for the ACME
   protocol that enables multiple independent systems to authorize a
   single domain name concurrently.  By adding a unique label to the DNS
   validation record name, the dns-account-01 challenge avoids CNAME
   delegation conflicts inherent to the dns-01 challenge type.  This is
   particularly valuable for multi-region or multi-cloud deployments
   that wish to rely upon DNS-based domain control validation and need
   to independently obtain certificates for the same domain.

### JWTClaimConstraints profile of ACME Authority Token  (draft-ietf-acme-authority-token-jwtclaimcon)
This document defines an authority token profile for the validation
   of JWTClaimConstraints and EnhancedJWTClaimConstraints certificate
   extensions within the Automated Certificate Management Environment
   (ACME) protocol.  This profile is based on the Authority Token
   framework and establishes the specific ACME identifier type,
   challenge mechanism, and token format necessary to authorize a client
   to request a certificate containing these constraints.

### Automatic Certificate Management Environment (ACME) with OpenID Federation 1.0  (draft-ietf-acme-openid-federation)
The Automatic Certificate Management Environment (ACME) protocol
   allows server operators to obtain TLS certificates for their
   websites, based on a demonstration of control over the website's
   domain via a fully-automated challenge/response protocol.

   OpenID Federation 1.0 defines how to build a trust infrastructure
   using a trusted third-party model.  It uses a trust evaluation
   mechanism to attest to the possession of private keys, protocol
   specific metadata and miscellaneous administrative and technical
   information related to a specific entity.

   This document defines how X.509 certificates associated with a given
   OpenID Federation Entity can be issued by an X.509 Certification
   Authority through the ACME protocol to the organizations which are
   part of a federation built on top of OpenID Federation 1.0.

### Automated Certificate Management Environment (ACME) Device Attestation Extension  (draft-ietf-acme-device-attest)
This document specifies new identifiers and a challenge for the
   Automated Certificate Management Environment (ACME) protocol which
   allows validating the identity of a device using attestation.

## Working Group: add
### DHCP and Router Advertisement Options for the Discovery of Network-designated Resolvers (DNR)  (draft-ietf-add-dnr)
This document specifies new DHCP and IPv6 Router Advertisement options to discover encrypted DNS resolvers (e.g., DNS over HTTPS, DNS over TLS, and DNS over QUIC).  Particularly, it allows a host to learn an Authentication Domain Name together with a list of IP addresses and a set of service parameters to reach such encrypted DNS resolvers.

### Service Binding Mapping for DNS Servers  (draft-ietf-add-svcb-dns)
The SVCB DNS resource record type expresses a bound collection of endpoint metadata, for use when establishing a connection to a named service.  DNS itself can be such a service, when the server is identified by a domain name.  This document provides the SVCB mapping for named DNS servers, allowing them to indicate support for encrypted transport protocols.

### Discovery of Designated Resolvers  (draft-ietf-add-ddr)
This document defines Discovery of Designated Resolvers (DDR), a set of mechanisms for DNS clients to use DNS records to discover a resolver's encrypted DNS configuration.  An Encrypted DNS Resolver discovered in this manner is referred to as a "Designated Resolver".  These mechanisms can be used to move from unencrypted DNS to encrypted DNS when only the IP address of a resolver is known.  These mechanisms are designed to be limited to cases where Unencrypted DNS Resolvers and their Designated Resolvers are operated by the same entity or cooperating entities.  It can also be used to discover support for encrypted DNS protocols when the name of an Encrypted DNS Resolver is known.

### Delegated Credentials to Host Encrypted DNS Forwarders on CPEs  (draft-reddy-add-delegated-credentials)
An encrypted DNS server is authenticated by a certificate signed by a
   Certificate Authority (CA).  However, for typical encrypted DNS
   server deployments on Customer Premise Equipment (CPEs), the
   signature cannot be obtained or requires excessive interactions with
   a Certificate Authority.

   This document explores the use of TLS delegated credentials for a DNS
   server deployed on a CPE.  This approach is meant to ease operating
   DNS forwarders in CPEs while allowing to make use of encrypted DNS
   capabilities.

### DHCP and Router Advertisement Options for Encrypted DNS Discovery  (draft-btw-add-home)
The document specifies new DHCP and IPv6 Router Advertisement options
   to discover encrypted DNS servers (e.g., DNS-over-HTTPS, DNS-over-
   TLS, DNS-over-QUIC).  Particularly, it allows to learn an
   authentication domain name together with a list of IP addresses and a
   port number to reach such encrypted DNS servers.  The discovery of
   DNS-over-HTTPS URI Templates is also discussed.

### Service Binding Mapping for DNS Servers  (draft-schwartz-svcb-dns)
The SVCB DNS record type expresses a bound collection of endpoint
   metadata, for use when establishing a connection to a named service.
   DNS itself can be such a service, when the server is identified by a
   domain name.  This document provides the SVCB mapping for named DNS
   servers, allowing them to indicate support for new transport
   protocols.

### Requirements for Discovering Designated Resolvers  (draft-box-add-requirements)
Adaptive DNS Discovery is chartered to define mechanisms that allow
   clients to discover and select encrypted DNS resolvers.  This
   document describes one common use case, namely that of clients that
   connect to a network but where they cannot securely authenticate the
   identity of that network.  In such cases the client would like to
   learn which encrypted DNS resolvers are designated by that network or
   by the Do53 resolver offered by that network.  It lists requirements
   that any proposed discovery mechanisms should seek to address.

### Discovery of Equivalent Encrypted Resolvers  (draft-pauly-add-deer)
This document defines Discovery of Equivalent Encrypted Resolvers
   (DEER), a mechanism for DNS clients to use DNS records to discover a
   resolver's encrypted DNS configuration.  This mechanism can be used
   to move from unencrypted DNS to encrypted DNS when only the IP
   address of an encrypted resolver is known.  It can also be used to
   discover support for encrypted DNS protocols when the name of an
   encrypted resolver is known.  This mechanism is designed to be
   limited to cases where equivalent encrypted and unencrypted resolvers
   are operated by the same entity.

### Establishing Local DNS Authority in Split-Horizon Environments  (draft-reddy-add-enterprise-split-dns)
When split-horizon DNS is deployed by a network, certain domains can
   be resolved authoritatively by the network-provided DNS resolver.
   DNS clients that don't always use this resolver might wish to do so
   for these domains.  This specification describes how clients can
   confirm the local resolver's authority over these domains.

### Requirements for Discovering Designated Resolvers  (draft-ietf-add-requirements)
Adaptive DNS Discovery is chartered to define mechanisms that allow
   clients to discover and select encrypted DNS resolvers.  This
   document describes one common use case, namely that of clients that
   connect to a network but where they cannot securely authenticate the
   identity of that network.  In such cases the client would like to
   learn which encrypted DNS resolvers are designated by that network or
   by the Do53 resolver offered by that network.  It lists requirements
   that any proposed discovery mechanisms should seek to address.

### DNS Resolver Information  (draft-reddy-add-resolver-info)
This document specifies a method for DNS resolvers to publish
   information about themselves.  DNS clients can use the resolver
   information to identify the capabilities of DNS resolvers.

### Reputation Verified Selection of Upstream Encrypted Resolvers  (draft-schwartz-add-ddr-forwarders)
This draft describes an extension to the Discovery of Designated
   Resolvers (DDR) standard, enabling use of encrypted DNS in the
   presence of legacy DNS forwarders.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the mailing list
   (add@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/add/.

   Source for this draft and an issue tracker can be found at
   https://github.com/bemasc/ddr-forwarders.

### DNS Resolver Information  (draft-ietf-add-resolver-info)
This document specifies a method for DNS resolvers to publish
   information about themselves.  DNS clients can use the resolver
   information to identify the capabilities of DNS resolvers.  How DNS
   clients use such an information is beyond the scope of this document.

### Establishing Local DNS Authority in Validated Split-Horizon Environments  (draft-ietf-add-split-horizon-authority)
When split-horizon DNS is deployed by a network, certain domain names
   can be resolved authoritatively by a network-provided DNS resolver.
   DNS clients that are not configured to use this resolver by default
   can use it for these specific domains only.  This specification
   defines a mechanism for domain owners to inform DNS clients about
   local resolvers that are authorized to answer authoritatively for
   certain subdomains.

### Handling Encrypted DNS Server Redirection  (draft-jt-add-dns-server-redirection)
This document defines Encrypted DNS Server Redirection (EDSR), a
   mechanism for encrypted DNS servers to redirect clients to other
   encrypted DNS servers.  This enables dynamic routing to geo-located
   or otherwise more desirable encrypted DNS servers without modifying
   DNS client endpoint configurations or the use of anycast by the DNS
   server.

### Encrypted DNS Server Redirection  (draft-ietf-add-encrypted-dns-server-redirection)
This document defines Encrypted DNS Server Redirection (EDSR), a
   mechanism for encrypted DNS servers to redirect clients to other
   encrypted DNS servers.  This enables dynamic routing to geo-located
   or otherwise more desirable encrypted DNS servers without modifying
   DNS client endpoint configurations or the use of anycast by the DNS
   server.

## Working Group: anima
### An Autonomic Control Plane (ACP)  (draft-ietf-anima-autonomic-control-plane)
Autonomic functions need a control plane to communicate, which depends on some addressing and routing.  This Autonomic Control Plane should ideally be self-managing and be as independent as possible of configuration.  This document defines such a plane and calls it the "Autonomic Control Plane", with the primary use as a control plane for autonomic functions.  It also serves as a "virtual out-of-band channel" for Operations, Administration, and Management (OAM) communications over a network that provides automatically configured, hop-by-hop authenticated and encrypted communications via automatically configured IPv6 even when the network is not configured or is misconfigured.

### GeneRic Autonomic Signaling Protocol (GRASP)  (draft-ietf-anima-grasp)
This document specifies the GeneRic Autonomic Signaling Protocol (GRASP), which enables autonomic nodes and Autonomic Service Agents to dynamically discover peers, to synchronize state with each other, and to negotiate parameter settings with each other.  GRASP depends on an external security environment that is described elsewhere.  The technical objectives and parameters for specific application scenarios are to be described in separate documents.  Appendices briefly discuss requirements for the protocol and existing protocols with comparable features.

### Bootstrapping Remote Secure Key Infrastructure (BRSKI)  (draft-ietf-anima-bootstrapping-keyinfra)
This document specifies automated bootstrapping of an Autonomic Control Plane.  To do this, a Secure Key Infrastructure is bootstrapped.  This is done using manufacturer-installed X.509 certificates, in combination with a manufacturer's authorizing service, both online and offline.  We call this process the Bootstrapping Remote Secure Key Infrastructure (BRSKI) protocol.  Bootstrapping a new device can occur when using a routable address and a cloud service, only link-local connectivity, or limited/disconnected networks.  Support for deployment models with less stringent security requirements is included.  Bootstrapping is complete when the cryptographic identity of the new key infrastructure is successfully deployed to the device.  The established secure connection can be used to deploy a locally issued certificate to the device as well.

### Autonomic IPv6 Edge Prefix Management in Large-Scale Networks  (draft-ietf-anima-prefix-management)
This document defines two autonomic technical objectives for IPv6 prefix management at the edge of large-scale ISP networks, with an extension to support IPv4 prefixes.  An important purpose of this document is to use it for validation of the design of various components of the Autonomic Networking Infrastructure.

### A Reference Model for Autonomic Networking  (draft-ietf-anima-reference-model)
This document describes a reference model for Autonomic Networking for managed networks.  It defines the behavior of an autonomic node, how the various elements in an autonomic context work together, and how autonomic services can use the infrastructure.

### Using an Autonomic Control Plane for Stable Connectivity of Network Operations, Administration, and Maintenance (OAM)  (draft-ietf-anima-stable-connectivity)
Operations, Administration, and Maintenance (OAM), as per BCP 161, for data networks is often subject to the problem of circular dependencies when relying on connectivity provided by the network to be managed for the OAM purposes.

 Provisioning while bringing up devices and networks tends to be more difficult to automate than service provisioning later on. Changes in core network functions impacting reachability cannot be automated because of ongoing connectivity requirements for the OAM equipment itself, and widely used OAM protocols are not secure enough to be carried across the network without security concerns.

 This document describes how to integrate OAM processes with an autonomic control plane in order to provide stable and secure connectivity for those OAM processes. This connectivity is not subject to the aforementioned circular dependencies.

### Generic Autonomic Signaling Protocol Application Program Interface (GRASP API)  (draft-liu-anima-grasp-api)
This document is a conceptual outline of the application programming
   interface (API) of the Generic Autonomic Signaling Protocol (GRASP).
   Such an API is needed for Autonomic Service Agents (ASA) calling the
   GRASP protocol module to exchange autonomic network messages with
   other ASAs.

### A Voucher Artifact for Bootstrapping Protocols  (draft-ietf-anima-voucher)
This document defines a strategy to securely assign a pledge to an owner using an artifact signed, directly or indirectly, by the pledge's manufacturer. This artifact is known as a "voucher".

 This document defines an artifact format as a YANG-defined JSON document that has been signed using a Cryptographic Message Syntax (CMS) structure. Other YANG-derived formats are possible. The voucher artifact is normally generated by the pledge's manufacturer (i.e., the Manufacturer Authorized Signing Authority (MASA)).

 This document only defines the voucher artifact, leaving it to other documents to describe specialized protocols for accessing it.

### Constrained Voucher Profile for Bootstrapping Protocols  (draft-richardson-anima-ace-constrained-voucher)
This document defines a strategy to securely assign a pledge to an
   owner, using an artifact signed, directly or indirectly, by the
   pledge's manufacturer.  This artifact is known as a "voucher".

   This document builds upon the work in [I-D.ietf-anima-voucher],
   encoding the resulting artifact in CBOR.  Use with two signature
   technologies are described.

   Additionally, this document explains how constrained vouchers may be
   transported in the [I-D.vanderstok-ace-coap-est] protocol.

### GeneRic Autonomic Signaling Protocol Application Program Interface (GRASP API)  (draft-ietf-anima-grasp-api)
This document is a conceptual outline of an Application Programming Interface (API) for the GeneRic Autonomic Signaling Protocol (GRASP).  Such an API is needed for Autonomic Service Agents (ASAs) calling the GRASP protocol module to exchange Autonomic Network messages with other ASAs.  Since GRASP is designed to support asynchronous operations, the API will need to be adapted according to the support for asynchronicity in various programming languages and operating systems.

### BRSKI-AE: Alternative Enrollment Protocols in BRSKI  (draft-ietf-anima-brski-async-enroll)
This document enhances Bootstrapping Remote Secure Key Infrastructure
   (BRSKI, [RFC8995]) to allow employing alternative enrollment
   protocols, such as CMP.

   Using self-contained signed objects, the origin of enrollment
   requests and responses can be authenticated independently of message
   transfer.  This supports end-to-end security and asynchronous
   operation of certificate enrollment and provides flexibility where to
   authenticate and authorize certification requests.

### Guidelines for Autonomic Service Agents  (draft-ietf-anima-asa-guidelines)
This document proposes guidelines for the design of Autonomic Service Agents for autonomic networks.  Autonomic Service Agents, together with the Autonomic Network Infrastructure, the Autonomic Control Plane, and the GeneRic Autonomic Signaling Protocol, constitute base elements of an autonomic networking ecosystem.

### Delegated Authority for Bootstrap Voucher Artifacts  (draft-ietf-anima-voucher-delegation)
This document describes an extension of the RFC8366 Voucher Artifact
   in order to support delegation of signing authority.  The initial
   voucher pins a public identity, and that public indentity can then
   issue additional vouchers.  This chain of authorization can support
   permission-less resale of devices, as well as guarding against
   business failure of the BRSKI Manufacturer Authorized Signing
   Authority (MASA).

### JWS signed Voucher Artifacts for Bootstrapping Protocols  (draft-ietf-anima-jws-voucher)
This document introduces a variant of the RFC8366 voucher artifact in
   which CMS is replaced by the JSON Object Signing and Encryption
   (JOSE) mechanism described in RFC7515.  This supports deployments in
   which JOSE is preferred over CMS.  In addition to specifying the
   format, the "application/voucher-jws+json" media type is registered
   and examples are provided.

### An Intent-based Framework of Network Services Autonomic Deployment and Management  (draft-ietf-anima-network-service-auto-deployment)
This document introduces an intent-based framework for network
   services autonomic deployment and management.  It autonomically
   deploys network services that require customized combinations of
   network resources and dynamically manage these resources throughout
   their lifecycle.  The framework leverages the GeneRic Autonomic
   Signaling Protocol (GRASP) to facilitate the dynamic exchange of
   resource management signals among autonomic nodes, thereby enabling
   coordinated and consistent operations within an autonomic network
   domain.  This framework is generic and applicable to most types of
   network resources.

### BRSKI-AE: Alternative Enrollment Protocols in BRSKI  (draft-ietf-anima-brski-ae)
This document defines enhancements to the Bootstrapping Remote Secure
   Key Infrastructure (BRSKI) protocol, known as BRSKI-AE (Alternative
   Enrollment).
   BRSKI-AE extends BRSKI to support certificate enrollment mechanisms
   instead of the originally specified use of EST.  It supports
   certificate enrollment protocols, such as CMP, that use authenticated
   self-contained signed objects for certification messages, allowing
   for flexibility in network device onboarding scenarios.
   The enhancements address use cases where the existing enrollment
   mechanism may not be feasible or optimal, providing a framework for
   integrating suitable alternative enrollment protocols.
   This document also updates the BRSKI reference architecture to
   accommodate these alternative methods, ensuring secure and scalable
   deployment across a range of network environments.

### Operational Considerations for BRSKI Registrar  (draft-ietf-anima-registrar-considerations)
This document describes a number of operational modes that a BRSKI
   Registration Authority (Registrar) may take on.

   Each mode is defined, and then each mode is given a relevance within
   an over applicability of what kind of organization the Registrar is
   deployed into.  This document does not change any protocol
   mechanisms.

   This document includes operational advice about avoiding unwanted
   consequences.

### Constrained GeneRic Autonomic Signaling Protocol  (draft-ietf-anima-constrained-grasp)
This document proposes the Constrained GeneRic Autonomic Signaling
   Protocol (cGRASP), a constrained and lightweight variant of the
   GeneRic Autonomic Signaling Protocol (GRASP, or the standard GRASP).
   cGRASP reduces message overhead and replaces TCP with CoAP as the
   transport protocol.  By leveraging CoAP's reliability features and
   deployment maturity, cGRASP can provide reliable signaling services
   without relying on TCP, making it suitable for IoT, where lightweight
   and resource-constrained devices dominate.  Furthermore, this
   document also discusses the potential approaches to adapting the
   cGRASP to work on the network without IP connectivity.

### Bootstrapping Remote Secure Key Infrastructure (BRSKI) Cloud Registrar  (draft-ietf-anima-brski-cloud)
Bootstrapping Remote Secure Key Infrastructures (BRSKI) defines how
   to onboard a device securely into an operator-maintained
   infrastructure.  It assumes that there is local network
   infrastructure for the device to discover.  On networks without that,
   there is nothing present to help onboard the device.

   This document extends BRSKI and defines behavior for bootstrapping
   devices for deployments where no local infrastructure is available,
   such as in a home or remote office.  This document defines how the
   device can use a well-defined "call-home" mechanism to find the
   operator-maintained infrastructure.

   This document defines how to contact a well-known Cloud Registrar,
   and two ways in which the device may be redirected towards the
   operator-maintained infrastructure.  The Cloud Registrar enables
   discovery of the operator-maintained infrastructure, and may enable
   establishment of trust with operator-maintained infrastructure that
   does not support BRSKI mechanisms.

   This document updates RFC 8995 (BRSKI).

### A Voucher Artifact for Bootstrapping Protocols  (draft-ietf-anima-rfc8366bis)
This document defines a strategy to securely assign a candidate
   device (Pledge) to an Owner using an artifact signed, directly or
   indirectly, by the Pledge's manufacturer.  This artifact is known as
   a "Voucher".

   This document defines an artifact format as a YANG-defined JSON or
   CBOR document that has been signed using a variety of cryptographic
   systems.

   The Voucher Artifact is normally generated by the Pledge's
   manufacturer (i.e., the Manufacturer Authorized Signing Authority
   (MASA)).

   This document obsoletes RFC8366: it includes a number of desired
   extensions into the YANG module.  The Voucher Request YANG module
   defined in RFC8995 is also updated and now included in this document,
   as well as other YANG extensions needed for variants of RFC8995.

### Information Distribution over GRASP  (draft-ietf-anima-grasp-distribution)
This document specifies experimental extensions to the GRASP protocol
   to enable information distribution capabilities.  The extension has
   two aspects: 1) new GRASP messages and options; 2) processing
   behaviors on the nodes.  With these extensions, the GRASP would have
   following new capabilities which make it a sufficient tool for
   general information distribution: 1) Pub-Sub model of information
   processing; 2) one node can actively sending data to another, without
   GRASP negotiation procedures; 3) selective flooding mechanism to
   allow the ASAs control the flooding scope.

   This document updates RFC8990, the GeneRic Autonomic Signaling
   Protocol (GRASP)[RFC8990].

### Operational Considerations for Voucher infrastructure for BRSKI MASA  (draft-ietf-anima-masa-considerations)
This document describes a number of operational modes that a BRSKI
   Manufacturer Authorized Signing Authority (MASA) may take on.

   Each mode is defined, and then each mode is given a relevance within
   an over applicability of what kind of organization the MASA is
   deployed into.  This document does not change any protocol
   mechanisms.

### Constrained Bootstrapping Remote Secure Key Infrastructure (cBRSKI)  (draft-ietf-anima-constrained-voucher)
This document defines the Constrained Bootstrapping Remote Secure Key
   Infrastructure (cBRSKI) protocol, which provides a solution for
   secure zero-touch onboarding of resource-constrained (IoT) devices
   into the network of a domain owner.  This protocol is designed for
   constrained networks, which may have limited data throughput or may
   experience frequent packet loss. cBRSKI is a variant of the BRSKI
   protocol, which uses an artifact signed by the device manufacturer
   called the "voucher" which enables a new device and the owner's
   network to mutually authenticate.  While the BRSKI voucher data is
   encoded in JSON, cBRSKI uses a compact CBOR-encoded voucher.  The
   BRSKI voucher data definition is extended with new data types that
   allow for smaller voucher sizes.  The Enrollment over Secure
   Transport (EST) protocol, used in BRSKI, is replaced with EST-over-
   CoAPS; and HTTPS used in BRSKI is replaced with DTLS-secured CoAP
   (CoAPS).  This document Updates RFC 8995 and RFC 9148.

### BRSKI discovery and variations  (draft-ietf-anima-brski-discovery)
Bootstrapping Remote Secure Key Infrastructure (BRSKI) is a protocol
   to enroll pledge devices automatically and secure with a registrar of
   an owner, relying also on proxies to facilitate the communication and
   Manufacturer Authorized Signing Authorities (MASA) and Certificate
   Authorities (CA) to enable the enrollment.

   This document specifies how to make BRSKI communications
   autoconfiguring, extensible and resilient in the face of simultaneous
   use of different variations of the BRSKI protocol (BRSKI, BRSKI-AE,
   BRSKI-PRM, constrained BRSKI, stateless constrained BRSKI proxies).
   This document specifies a data model, IANA registry and BRSKI
   component procedures to achieve this.

   This document does not define any new discovery methods.  Instead,
   its data model allows signaling of all current (and future)
   variations of the BRSKI family of protocols consistently via
   different existing network discovery mechanisms: DNS-SD, CoAP
   discovery (CORE-LF) and GRASP.  Additional/future discovery
   mechanisms can also be supported through the IANA registry.

   Automatic resiliency and load-sharing are enabled through the use of
   discovery mechanisms and the provisioning of multiple instances of
   BRSKI components such as registrars and Join Proxies.  This document
   specifies the procedures to support load-sharing and (fast) failover
   under failure and recovery of redundant components.

   Future-proof deployments of BRSKI require Join Proxies that
   automatically support any current and future BRSKI variation.  This
   document specifies the procedures by which Join Proxies can support
   this through specific Join Proxy protocol behavior and the use of
   discovery mechanisms.

   The specification of discovery of pledges by their IDevID as
   introduced by BRSKI-PRM is refined in this document.

### Join Proxy for Onboarding of Constrained Network Elements  (draft-ietf-anima-constrained-join-proxy)
This document supports the constrained Bootstrapping Remote Secure
   Key Infrastructures (cBRSKI) onboarding protocol by adding a required
   network function, the Join Proxy.  This function can be implemented
   on a constrained node.  The goal of the Join Proxy is to help new
   constrained nodes ("Pledges") securely onboard into a new IP network
   using the cBRSKI protocol.  It acts as a circuit proxy for User
   Datagram Protocol (UDP) packets that carry the onboarding messages.
   The solution is extensible to support other UDP-based onboarding
   protocols as well.  The Join Proxy functionality is designed for use
   in constrained networks, including IPv6 over Low-Power Wireless
   Personal Area Networks (6LoWPAN) based networks in which the
   onboarding authority server ("Registrar") may be multiple IP hops
   away from a Pledge.  Despite this distance, the Pledge only needs to
   use link-local communication to complete cBRSKI onboarding.  Two
   modes of Join Proxy operation are defined, stateless and stateful, to
   allow different trade-offs regarding resource usage, implementation
   complexity and security.

### BRSKI with Pledge in Responder Mode (BRSKI-PRM)  (draft-ietf-anima-brski-prm)
This document defines enhancements to Bootstrapping Remote Secure Key
   Infrastructure (BRSKI, RFC8995) as BRSKI with Pledge in Responder
   Mode (BRSKI-PRM).  BRSKI-PRM supports the secure bootstrapping of
   devices, referred to as pledges, into a domain where direct
   communication with the registrar is either limited or not possible at
   all.  To facilitate interaction between a pledge and a domain
   registrar the registrar-agent is introduced as new component.  The
   registrar-agent supports the reversal of the interaction model from a
   pledge-initiated mode, to a pledge-responding mode, where the pledge
   is in a server role.  To establish the trust relation between pledge
   and registrar, BRSKI-PRM relies on object security rather than
   transport security.  This approach is agnostic to enrollment
   protocols that connect a domain registrar to a key infrastructure
   (e.g., domain Certification Authority).

## Working Group: bess
### Label Switched Path (LSP) Ping Mechanisms for EVPN and Provider Backbone Bridging EVPN (PBB-EVPN)  (draft-ietf-bess-evpn-lsp-ping)
Label Switched Path (LSP) Ping is a widely deployed Operations, Administration, and Maintenance (OAM) mechanism in MPLS networks.  This document describes mechanisms for detecting data plane failures using LSP Ping in MPLS-based Ethernet VPN (EVPN) and Provider Backbone Bridging EVPN (PBB-EVPN) networks.

### PIM Proxy in EVPN Networks  (draft-skr-bess-evpn-pim-proxy)
Ethernet Virtual Private Networks are becoming prevalent in Data
   Centers, Data Center Interconnect (DCI) and Service Provider VPN
   applications.  One of the goals that EVPN pursues is the reduction of
   flooding and the efficiency of CE-based control plane procedures in
   Broadcast Domains.  Examples of this are Proxy ARP/ND and IGMP/MLD
   Proxy.  This document complements the latter, describing the
   procedures required to minimize the flooding of PIM messages in EVPN
   Broadcast Domains, and optimize the IP Multicast delivery between PIM
   routers.

### Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Proxies for Ethernet VPN (EVPN)  (draft-ietf-bess-evpn-igmp-mld-proxy)
This document describes how to support endpoints running the Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) efficiently for the multicast services over an Ethernet VPN (EVPN) network by incorporating IGMP/MLD Proxy procedures on EVPN Provider Edges (PEs).

### Integrated Routing and Bridging in Ethernet VPN (EVPN)  (draft-ietf-bess-evpn-inter-subnet-forwarding)
Ethernet VPN (EVPN) provides an extensible and flexible multihoming VPN solution over an MPLS/IP network for intra-subnet connectivity among Tenant Systems and end devices that can be physical or virtual.  However, there are scenarios for which there is a need for a dynamic and efficient inter-subnet connectivity among these Tenant Systems and end devices while maintaining the multihoming capabilities of EVPN.  This document describes an Integrated Routing and Bridging (IRB) solution based on EVPN to address such requirements.

### Segment Routing over IPv6 Argument Signaling for BGP Services  (draft-ietf-bess-bgp-srv6-args)
RFC9252 defines procedures and messages for BGP Overlay Services for
   Segment Routing over IPv6 (SRv6) including Layer 3 Virtual Private
   Network, Ethernet Virtual Private Network, and Global Internet
   Routing.  This document updates RFC9252 and provides more detailed
   specifications for the signaling and processing of SRv6 Segment
   Identifiers advertisements for BGP Overlay Service routes associated
   with SRv6 Endpoint Behaviors that support arguments.

### IPv6-Only PE Design for IPv4-NLRI with IPv6-NH  (draft-ietf-bess-ipv6-only-pe-design)
As Enterprises and Service Providers upgrade their brown field or
   green field MPLS/SR core to an IPv6 transport, Multiprotocol BGP (MP-
   BGP)now plays an important role in the transition of their Provider
   (P) core network as well as Provider Edge (PE) Edge network from IPv4
   to IPv6.  Operators must be able to continue to support IPv4
   customers when both the Core and Edge networks are IPv6-Only.

   This document details an important External BGP (eBGP) PE-CE Edge and
   Inter-AS IPv6-Only peering design that leverages the MP-BGP
   capability exchange by using IPv6 peering as pure transport, allowing
   both IPv4 Network Layer Reachability Information (NLRI) and IPv6
   Network Layer Reachability Information (NLRI)to be carried over the
   same (Border Gateway Protocol) BGP TCP session.  The design change
   provides the same Dual Stacking functionality that exists today with
   separate IPv4 and IPv6 BGP sessions as we have today.  With this
   design change from a control plane perspective a single IPv6 is
   required for both IPv4 and IPv6 routing updates and from a data plane
   forwarindg perspective an IPv6 address need only be configured on the
   PE and CE interface for both IPv4 and IPv6 packet forwarding.

   This document provides a much needed solution for Internet Exchange
   Point (IXP) that are facing IPv4 address depletion at large peering
   points.  With this design, IXP can now deploy PE-CE IPv6-Only eBGP
   Edge or Inter-AS peering design to eliminate IPv4 provisioning at the
   Edge.  This core and edge IPv6-Only peering design paradigm change
   can apply to any eBGP peering, public internet or private, which can
   be either Core networks, Data Center networks, Access networks or can
   be any eBGP peering scenario.  This document provides vendor specific
   test cases for the IPv6-Only peering design as well as test results
   for the five major vendors stakeholders in the routing and switching
   indusrty, Cisco, Juniper, Arista, Nokia and Huawei.  With the test
   results provided for the IPv6-Only Edge peering design, the goal is
   that all other vendors around the world that have not been tested
   will begin to adopt and implement this new Best Current Practice for
   eBGP IPv6-Only Edge peering.

   As this issue with IXP IPv4 address depletion is a critical issue
   around the world, it is imperative for an immediate solution that can
   be implemented quickly.  This Best Current Practice IPv6-only eBGP
   peering design specification will help proliferate IPv6-Only
   deployments at the eBGP Edge network peering points to starting
   immediately at a minimum with operators around the world using Cisco,
   Juniper, Arista, Nokia and Huawei.  As other vendors start to
   implement this Best Current Practice, the IXP IPv4 address depletion
   gap will eventually be eliminated.

### Optimized Ingress Replication Solution for Ethernet VPN (EVPN)  (draft-ietf-bess-evpn-optimized-ir)
Network Virtualization Overlay networks using Ethernet VPN (EVPN) as
   their control plane may use Ingress Replication or PIM (Protocol
   Independent Multicast)-based trees to convey the overlay Broadcast,
   Unknown unicast and Multicast (BUM) traffic.  PIM provides an
   efficient solution to avoid sending multiple copies of the same
   packet over the same physical link, however it may not always be
   deployed in the Network Virtualization Overlay core network.  Ingress
   Replication avoids the dependency on PIM in the Network
   Virtualization Overlay network core.  While Ingress Replication
   provides a simple multicast transport, some Network Virtualization
   Overlay networks with demanding multicast applications require a more
   efficient solution without PIM in the core.  This document describes
   a solution to optimize the efficiency of Ingress Replication trees.

### Secure EVPN  (draft-ietf-bess-secure-evpn)
The applications of EVPN-based solutions (BGP MPLS-based Ethernet VPN
   and Network Virtualization Overlay Solution using EVPN) have become
   pervasive in Data Center, Service Provider, and Enterprise segments.
   It is being used for fabric overlays and inter-site connectivity in
   the Data Center market segment, for Layer-2, Layer-3, and IRB VPN
   services in the Service Provider market segment, and for fabric
   overlay and WAN connectivity in Enterprise networks.  For Data Center
   and Enterprise applications, there is a need to provide inter-site
   and WAN connectivity over public Internet in a secured manner with
   same level of privacy, integrity, and authentication for tenant's
   traffic as IPsec tunneling using IKEv2.  This document presents a
   solution where BGP point-to-multipoint signaling is leveraged for key
   and policy exchange among PE devices to create private pair-wise
   IPsec Security Associations without IKEv2 point-to-point signaling or
   any other direct peer-to-peer session establishment messages.

### EVPN Fast Reroute  (draft-ietf-bess-evpn-fast-reroute)
This document summarises EVPN convergence mechanisms and specifies
   procedures for EVPN networks to achieve fast and scale-independent
   convergence.

### EVPN Support for L3 Fast Convergence and Aliasing/Backup Path  (draft-sajassi-bess-evpn-ip-aliasing)
This document proposes an EVPN extension to allow several of its
   multihoming functions, fast convergence and aliasing/backup path, to
   be used in conjunction with inter-subnet forwarding.  The extension
   is limited to All-Active and Single-Active redundancy modes.

### BGP Encodings and Procedures for Multicast in MPLS/BGP IP VPNs  (draft-zzhang-bess-rfc6514bis)
RFC 6514 describes the BGP encodings and procedures for exchanging
   the information elements required by Multicast in MPLS/BGP IP VPNs,
   as specified in RFC 6513.

   This document updates and obsoletes RFC 6514.  The original authors
   of RFC 6514 are listed at the end of this document.

### EVPN Interoperability Modes  (draft-ietf-bess-evpn-modes-interop)
Ethernet VPN (EVPN) provides different functional modes in the area
   of Service Interface, Integrated Route and Bridge (IRB) and IRB Core
   connectivity.  This document specifies how the different EVPN
   functional modes and types can interoperate with each other.  This
   document does not redefine the existing functional modes but
   describes how these modes interoperate.

### BGP Overlay Services Based on Segment Routing over IPv6 (SRv6)  (draft-ietf-bess-srv6-services)
This document defines procedures and messages for SRv6-based BGP services, including Layer 3 Virtual Private Network (L3VPN), Ethernet VPN (EVPN), and Internet services.  It builds on "BGP/MPLS IP Virtual Private Networks (VPNs)" (RFC 4364) and "BGP MPLS-Based Ethernet VPN" (RFC 7432).

### Inter-AS Option D for BGP/MPLS IP VPN  (draft-mapathak-interas-ab)
This document describes a new option known as an Inter-AS option D to
   the 'Multi-AS Backbones' section of [RFC4364].  This option combines
   VPN VRFs at the Autonomous System Border Router (ASBR) as described
   in 'Option A' with the distribution of labeled VPN-IP routes as
   described in 'Option B'.  In addition, this option allows for a data
   plane consisting of two methods of traffic forwarding between
   attached ASBR pairs.

### Simulating Partial Mesh of Multipoint-to-Multipoint (MP2MP) Provider Tunnels with Ingress Replication  (draft-ietf-bess-mvpn-bidir-ingress-replication)
RFC 6513 ("Multicast in MPLS/BGP IP VPNs") describes a method to support bidirectional customer multicast flows using a partial mesh of Multipoint-to-Multipoint (MP2MP) tunnels.  This document specifies how a partial mesh of MP2MP tunnels can be simulated using Ingress Replication.  This solution enables a service provider to use Ingress Replication to offer transparent bidirectional multicast service to its VPN customers.

### BGP ACCEPT_OWN Community Attribute  (draft-ietf-l3vpn-acceptown-community)
Under certain conditions, it is desirable for a Border Gateway Protocol (BGP) route reflector to be able to modify the Route Target (RT) list of a Virtual Private Network (VPN) route that the route reflector distributes, enabling the route reflector to control how a route originated within one VPN Routing and Forwarding table (VRF) is imported into other VRFs.  This technique works effectively as long as the VRF that exports the route is not on the same Provider Edge (PE) router as the VRF(s) that imports the route.  However, due to the constraints of BGP, it does not work if the two are on the same PE.  This document describes a modification to BGP allowing this technique to work when the VRFs are on the same PE and to be used in a standard manner throughout an autonomous system.

### IGMP and MLD Proxy for EVPN  (draft-sajassi-bess-evpn-igmp-mld-proxy)
Ethernet Virtual Private Network (EVPN) solution [RFC 7432] is
   becoming pervasive in data center (DC) applications for Network
   Virtualization Overlay (NVO) and DC interconnect (DCI) services, and
   in service provider (SP) applications for next generation virtual
   private LAN services.

   This draft describes how to support efficiently endpoints running
   IGMP for the above services over an EVPN network by incorporating
   IGMP proxy procedures on EVPN PEs.

### MVPN: Using Bidirectional P-Tunnels  (draft-ietf-l3vpn-mvpn-bidir)
A set of prior RFCs specify procedures for supporting multicast in
   BGP/MPLS IP VPNs.  These procedures allow customer multicast data to
   travel across a service provider's backbone network through a set of
   multicast tunnels.  The tunnels are advertised in certain BGP
   multicast "auto-discovery" routes, by means of a BGP attribute known
   as the "Provider Multicast Service Interface (PMSI) Tunnel
   attribute".  Encodings have been defined that allow the PMSI Tunnel
   attribute to identify bidirectional (multipoint-to-multipoint)
   multicast distribution trees.  However, the prior RFCs do not provide
   all the necessary procedures for using bidirectional tunnels to
   support multicast VPNs.  This document updates RFCs 6513 and 6625 by
   specifying those procedures.  In particular, it specifies the
   procedures for assigning customer multicast flows (unidirectional or
   bidirectional) to specific bidirectional tunnels in the provider
   backbone, for advertising such assignments, and for determining which
   flows have been assigned to which tunnels.

### Registry and Extensions for P-Multicast Service Interface Tunnel Attribute Flags  (draft-ietf-bess-pta-flags)
The BGP-based control procedures for Multicast Virtual Private Networks (MVPNs) make use of a BGP attribute known as the "P-Multicast Service Interface (PMSI) Tunnel" attribute.  The attribute contains a one-octet "Flags" field.  The purpose of this document is to establish an IANA registry for the assignment of the bits in this field.  Since the "Flags" field contains only eight bits, this document also defines a new BGP Extended Community, "Additional PMSI Tunnel Attribute Flags", that can be used to carry additional flags for the "P-Multicast Service Interface (PMSI) Tunnel" attribute.  This document updates RFC 6514.

### TRILL-EVPN  (draft-ietf-l2vpn-trill-evpn)
This document discusses how Ethernet VPN (E-VPN) technology is used
   to interconnect TRILL [TRILL] networks over an MPLS/IP network, with
   two key characteristics: C-MAC address transparency on the hand-off
   point and control-plane isolation among the interconnected TRILL
   networks.

Conventions

### VPWS support in EVPN  (draft-boutros-l2vpn-evpn-vpws)
This document describes how EVPN can be used to support virtual
   private wire service (VPWS) in MPLS/IP networks. EVPN enables the
   following characteristics for VPWS: single-active as well as all-
   active multi-homing with flow-based load-balancing, eliminates the
   need for single-segment and multi-segment PW signaling, and provides
   fast protection using data-plane prefix independent convergence upon
   node or link failure.

### Extranet Multicast in BGP/IP MPLS VPNs  (draft-ietf-l3vpn-mvpn-extranet)
Previous RFCs specify the procedures necessary to allow IP multicast
   traffic to travel from one site to another within a BGP/MPLS IP VPN
   (Virtual Private Network).  However, it is sometimes desirable to
   allow multicast traffic whose source is in one VPN to be received by
   systems that are in another VPN.  This is known as a "Multicast VPN
   (MVPN) extranet".  This document updates RFCs 6513, 6514, and 6625 by
   specifying the procedures that are necessary in order to provide MVPN
   extranet service.

### Encoding Multipoint LDP (mLDP) Forwarding Equivalence Classes (FECs) in the NLRI of BGP MCAST-VPN Routes  (draft-ietf-l3vpn-mvpn-mldp-nlri)
Many service providers offer "BGP/MPLS IP VPN" service to their customers.  Existing IETF standards specify the procedures and protocols that a service provider uses in order to offer this service to customers who have IP unicast and IP multicast traffic in their VPNs.  It is also desirable to be able to support customers who have MPLS multicast traffic in their VPNs.  This document specifies the procedures and protocol extensions that are needed to support customers who use the Multipoint LDP (mLDP) as the control protocol for their MPLS multicast traffic.  Existing standards do provide some support for customers who use mLDP, but only under a restrictive set of circumstances.  This document generalizes the existing support to include all cases where the customer uses mLDP, without any restrictions.  This document updates RFC 6514.

### IP Prefix Advertisement in EVPN  (draft-rabadan-l2vpn-evpn-prefix-advertisement)
EVPN provides a flexible control plane that allows intra-subnet
   connectivity in an IP/MPLS and/or an NVO-based network. In NVO
   networks, there is also a need for a dynamic and efficient inter-
   subnet connectivity across Tenant Systems and End Devices that can be
   physical or virtual and may not support their own routing protocols.
   This document defines a new EVPN route type for the advertisement of
   IP Prefixes and explains some use-case examples where this new route-
   type is used.

### BGP as an MVPN PE-CE Protocol  (draft-ietf-l3vpn-mvpn-pe-ce)
When a Service Provider offers BGP/MPLS IP VPN service to its
   customers, RFCs 6513 and 6514 describe protocols and procedures that
   the Service Provider can use in order to carry the customer's IP
   multicast traffic from one customer site to others.  BGP can be used
   to carry customer multicast routing information from one Provider
   Edge (PE) router to another, but it is assumed that PIM is running on
   the interface between a Customer Edge (CE) router and a PE router.
   This document specifies protocols and procedures that, under certain
   conditions, allow customer multicast routing information to carried
   between PE and CE via BGP.  This can eliminate the need to run PIM on
   the PE-CE interfaces, potentially eliminating the need to run PIM on
   the PE routers at all.

### Ingress Replication Tunnels in Multicast VPN  (draft-rosen-l3vpn-ir)
RFCs 6513, 6514, and other RFCs describe procedures by which a
   Service Provider may offer Multicast VPN service to its customers.
   These procedures create point-to-multipoint (P2MP) or multipoint-to-
   multipoint trees across the Service Provider's backbone.  One type of
   P2MP tree that may be used is known as an "Ingress Replication (IR)
   tunnel".  In an IR tunnel, a parent node need not be "directly
   connected" to its child nodes.  When a parent node has to send a
   multicast data packet to its child nodes, it does not use layer 2
   multicast, IP multicast, or MPLS multicast to do so.  Rather, it
   makes n individual copies, and then unicasts each copy, through an IP
   or MPLS unicast tunnel, to exactly one child node.  While the prior
   MVPN specifications allow the use of IR tunnels, those specifications
   are not always very clear or explicit about how the MVPN protocol
   elements and procedures are applied to IR tunnels.  This document
   updates RFCs 6513 and 6514 by adding additional details that are
   specific to the use of IR tunnels.

### Extensions to BGP Signaled Pseudowires to support Flow-Aware Transport Labels  (draft-keyupate-l2vpn-fat-pw-bgp)
[RFC6391] describes a mechanism that uses an additional label (Flow
   Label) in the MPLS label stack that allows Label Switch Routers to
   balance flows within Pseudowires at a finer granularity than the
   individual Pseudowires across the Equal Cost Multiple Paths (ECMPs)
   that exists within the Packet Switched Network (PSN).

   Furthermore,[RFC6391] defines the LDP protocol extensions required to
   synchronize the flow label states between the ingress and egress PEs
   when using the signaling procedures defined in the [RFC4447].

   This draft defines protocol extensions required to synchronize flow
   label states among PEs when using the BGP-based signaling procedures
   defined in [RFC4761].  These protocol extensions are equally
   applicable to point-to-point L2VPNs defined in [RFC6624].

### Shortest Path Bridging, MAC mode Support over EVPN  (draft-ietf-l2vpn-spbm-evpn)
This document describes how Ethernet Shortest Path Bridging MAC mode
   (802.1aq) can be combined with EVPN in a way that interworks with
   PBB-PEs as described in the PBB-EVPN solution. This is achieved via
   operational isolation of each Ethernet network subtending an EVPN
   core while supporting full interworking between the different
   variations of Ethernet networks.

### Simulating "Partial Mesh of MP2MP P-Tunnels" with Ingress Replication  (draft-ietf-l3vpn-mvpn-bidir-ingress-replication)
RFC 6513 described a method to support bidirectional C-flow using
   "Partial Mesh of MP2MP P-Tunnels".  This document describes how
   partial mesh of MP2MP P-Tunnels can be simulated with Ingress
   Replication, instead of a real MP2MP tunnel.  This enables a Service
   Provider to use Ingress Replication to offer transparent BIDIR-PIM
   service to its VPN customers.

### FIB Reduction in Virtual Subnet  (draft-xu-l3vpn-virtual-subnet-fib-reduction)
Virtual Subnet is a BGP/MPLS IP VPN-based subnet extension solution
   which is intended for building Layer3 network virtualization overlays
   within and/or across data centers.  This document describes a
   mechanism for reducing the FIB size of PE routers in the Virtual
   Subnet context.

### Virtual Subnet: A L3VPN-based Subnet Extension Solution  (draft-ietf-l3vpn-virtual-subnet)
This document describes a Layer3 Virtual Private Network (L3VPN)-
   based subnet extension solution referred to as Virtual Subnet, which
   can be used for building Layer3 network virtualization overlays
   within and/or across data centers.

### Global Table Multicast with BGP-MVPN Procedures  (draft-ietf-l3vpn-mvpn-global-table-mcast)
RFC6513, RFC6514, and other RFCs describe protocols and procedures
   which a Service Provider (SP) may deploy in order offer Multicast
   Virtual Private Network (Multicast VPN or MVPN) service to its
   customers.  Some of these procedures use BGP to distribute VPN-
   specific multicast routing information across a backbone network.
   With a small number of relatively minor modifications, the very same
   BGP procedures can also be used to distribute multicast routing
   information that is not specific to any VPN.  Multicast that is
   outside the context of a VPN is known as "Global Table Multicast", or
   sometimes simply as "Internet multicast".  In this document, we
   describe the modifications that are needed to use the MVPN BGP
   procedures for Global Table Multicast.

### Multicast VPN fast upstream failover  (draft-morin-bess-mvpn-fast-failover)
This document defines multicast VPN extensions and procedures that
   allow fast failover for upstream failures, by allowing downstream PEs
   to take into account the status of Provider-Tunnels (P-tunnels) when
   selecting the upstream PE for a VPN multicast flow, and extending BGP
   MVPN routing so that a C-multicast route can be advertized toward a
   standby upstream PE.

### Covering Prefixes Outbound Route Filter for BGP-4  (draft-ietf-l3vpn-orf-covering-prefixes)
This document defines a new ORF-type, called the "Covering Prefixes
   ORF (CP-ORF)".  CP-ORF is applicable in Virtual Hub-and-Spoke VPNs.
   It also is applicable in BGP/MPLS Ethernet VPN (EVPN) Networks.

### Requirements for Extending BGP/MPLS VPNs to End-Systems  (draft-ietf-l3vpn-end-system-requirements)
The proven scalability and extensibility of the BGP/MPLS IP VPNs (IP
   VPN) technology has made it an attractive candidate for data
   center/cloud virtualization. Virtualized end-system environment
   imposes additional requirements to MPLS/BGP VPN technology. This
   document provides the requirements for extending IP VPN technology
   (in original or modified versions) into the end-systems/hosts, such
   as a server in a data center.

### Multicast VPN state damping  (draft-morin-bess-multicast-damping)
This document describes procedures to damp multicast VPN routing
   state changes and control the effect of the churn due to the
   multicast dynamicity in customer site.  The procedures described in
   this document are applicable to BGP-based multicast VPN and help
   avoid uncontrolled control plane load increase in the core routing
   infrastructure.  New procedures are proposed inspired from BGP
   unicast route damping principles, but adapted to multicast.

### (PBB-)EVPN Seamless Integration with (PBB-)VPLS  (draft-sajassi-bess-evpn-vpls-seamless-integ)
This draft discusses the backward compatibility of the (PBB-)EVPN
   solution with (PBB-)VPLS and provides mechanisms for seamless
   integration of the two technologies in the same MPLS/IP network on a
   per-VPN-instance basis.

### Interconnect Solution for EVPN Overlay networks  (draft-rabadan-bess-dci-evpn-overlay)
This document describes how Network Virtualization Overlay networks
   (NVO) can be connected to a Wide Area Network (WAN) in order to
   extend the layer-2 connectivity required for some tenants. The
   solution analyzes the interaction between NVO networks running EVPN
   and other L2VPN technologies used in the WAN, such as VPLS/PBB-VPLS
   or EVPN/PBB-EVPN, and proposes a solution for the interworking
   between both.

### Optimized Ingress Replication solution for EVPN  (draft-rabadan-bess-evpn-optimized-ir)
Network Virtualization Overlay (NVO) networks using EVPN as control
   plane may use ingress replication (IR) or PIM-based trees to convey
   the overlay multicast traffic. PIM provides an efficient solution to
   avoid sending multiple copies of the same packet over the same
   physical link, however it may not always be deployed in the NVO core
   network. IR avoids the dependency on PIM in the NVO network core.
   While IR provides a simple multicast transport, some NVO networks
   with demanding multicast applications require a more efficient
   solution without PIM in the core. This document describes a solution
   to optimize the efficiency of IR in NVO networks.

### AC-Influenced Designated Forwarder Election for EVPN  (draft-rabadan-bess-evpn-ac-df)
The Designated Forwarder (DF) in EVPN networks is the PE responsible
   for sending multicast, broadcast and unknown unicast traffic to a
   multi-homed CE, on a given Ethernet Tag on a particular Ethernet
   Segment (ES). The DF is selected based on the list of PEs that
   advertise the Ethernet Segment Identifier (ESI) to the EVPN network.
   While PE node or link failures trigger the DF re-election for a given
   <ESI, EVI>, individual Attachment Circuit (AC) or MAC-VRF failures do
   not trigger such DF re-election and the traffic may therefore be
   permanently impacted, even though there is an alternative path. This
   document improves the DF election algorithm so that the AC status can
   influence the result of the election and this type of "logical"
   failures can be protected too.

### Inter-AS Option C between NVO3 and BGP/MPLS IP VPN network  (draft-hao-bess-inter-nvo3-vpn-optionc)
This draft describes inter-as option-C solution between NVO3 network
   and MPLS/IP VPN network. Transport layer stitching solution should
   be provided. Also to ensure VPNv4 route exchange correctly between
   local NVE and remote PE, VNID space should be partitioned, only the
   VNIDs of lower 1 Million can be used for interconnection with outer
   MPLS VPN network using option-C solution, the rest 15 Million VNIDs
   can only be used for intra DC.

### L2L3 VPN Multicast MIB  (draft-ietf-bess-l2l3-vpn-mcast-mib)
This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in the Internet community.  In particular, it describes two MIB modules that will be used by other MIB modules for monitoring and/or configuring Layer 2 and Layer 3 Virtual Private Networks that support multicast.

### BGP/MPLS Layer 3 VPN Multicast Management Information Base  (draft-ietf-bess-mvpn-mib)
This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in the Internet community.  In particular, it describes managed objects to configure and/or monitor Multicast communication over IP Virtual Private Networks (VPNs) supported by the Multiprotocol Label Switching/Border Gateway Protocol (MPLS/BGP) on a Provider Edge (PE) router.

### A new Designated Forwarder Election for the EVPN  (draft-mohanty-bess-evpn-df-election)
This document describes an improved EVPN Designated Forwarder
   Election (DF) algorithm which can be used to enhance operational
   experience in terms of convergence speed and robustness over a WAN
   deploying EVPN

### EVPN Virtual Ethernet Segment  (draft-sajassi-bess-evpn-virtual-eth-segment)
EVPN and PBB-EVPN introduce a family of solutions for multipoint
   Ethernet services over MPLS/IP network with many advanced
   capabilities among which their multi-homing capabilities. These
   solutions define two types of multi-homing for an Ethernet Segment
   (ES): 1) Single-Active and 2) All-Active, where an Ethernet Segment
   is defined as a set of links between the multi-homed device/network
   and the set of PE devices that they are connected to.

   Some Service Providers want to extend the concept of the physical
   links in an ES to Ethernet Virtual Circuits (EVCs) where many of such
   EVCs can be aggregated on a single physical External Network-to-
   Network Interface (ENNI). An ES that consists of a set of EVCs
   instead of physical links is referred to as a virtual ES (vES). This
   draft describes the requirements and the extensions needed to support
   vES in EVPN and PBB-EVPN.

### E-TREE Support in EVPN & PBB-EVPN  (draft-sajassi-bess-evpn-etree)
The Metro Ethernet Forum (MEF) has defined a rooted-multipoint
   Ethernet service known as Ethernet Tree (E-Tree).  [ETREE-FMWK]
   proposes a solution framework for supporting this service in MPLS
   networks. This document discusses how those functional requirements
   can be easily met with EVPN.

### Covering Prefixes Outbound Route Filter for BGP-4  (draft-ietf-bess-orf-covering-prefixes)
This document defines a new Outbound Route Filter (ORF) type, called the Covering Prefixes ORF (CP-ORF).  CP-ORF is applicable in Virtual Hub-and-Spoke VPNs.  It also is applicable in BGP/MPLS Ethernet VPN (EVPN) networks.

### Usage and Applicability of BGP MPLS-Based Ethernet VPN  (draft-ietf-bess-evpn-usage)
This document discusses the usage and applicability of BGP MPLS-based Ethernet VPN (EVPN) in a simple and fairly common deployment scenario.  The different EVPN procedures are explained in the example scenario along with the benefits and trade-offs of each option.  This document is intended to provide a simplified guide for the deployment of EVPN networks.

### Requirements for Extending BGP/MPLS VPNs to End-Systems  (draft-ietf-bess-end-system-requirements)
The proven scalability and extensibility of the BGP/MPLS IP VPNs (IP
   VPN) technology has made it an attractive candidate for data
   center/cloud virtualization. Virtualized end-system environment
   imposes additional requirements to MPLS/BGP VPN technology. This
   document provides the requirements for extending IP VPN technology
   (in original or modified versions) into the end-systems/hosts, such
   as a server in a data center.

### BGP/MPLS VPN Virtual PE  (draft-ietf-bess-virtual-pe)
This document describes the architecture solutions for BGP/MPLS L3
   and L2 Virtual Private Networks (VPNs) with virtual Provider Edge
   (vPE) routers. It provides a functional description of the vPE
   control, forwarding, and management. The proposed vPE solutions
   support both the Software Defined Networks (SDN) approach which
   allows physical decoupling of the control and the forwarding, and the
   traditional distributed routing approach. A vPE can reside in any
   network or compute devices, such as a server as co-resident with the
   application virtual machines (VMs), or a Top-of-Rack (ToR) switch in
   a Data Center (DC) network.

### A Network Virtualization Overlay Solution Using Ethernet VPN (EVPN)  (draft-ietf-bess-evpn-overlay)
This document specifies how Ethernet VPN (EVPN) can be used as a Network Virtualization Overlay (NVO) solution and explores the various tunnel encapsulation options over IP and their impact on the EVPN control plane and procedures.  In particular, the following encapsulation options are analyzed: Virtual Extensible LAN (VXLAN), Network Virtualization using Generic Routing Encapsulation (NVGRE), and MPLS over GRE.  This specification is also applicable to Generic Network Virtualization Encapsulation (GENEVE); however, some incremental work is required, which will be covered in a separate document.  This document also specifies new multihoming procedures for split-horizon filtering and mass withdrawal.  It also specifies EVPN route constructions for VXLAN/NVGRE encapsulations and Autonomous System Border Router (ASBR) procedures for multihoming of Network Virtualization Edge (NVE) devices.

### Multicast Virtual Private Network (MVPN): Using Bidirectional P-Tunnels  (draft-ietf-bess-mvpn-bidir)
A set of prior RFCs specify procedures for supporting multicast in BGP/MPLS IP VPNs.  These procedures allow customer multicast data to travel across a service provider's backbone network through a set of multicast tunnels.  The tunnels are advertised in certain BGP multicast auto-discovery routes, by means of a BGP attribute known as the "Provider Multicast Service Interface (PMSI) Tunnel" attribute.  Encodings have been defined that allow the PMSI Tunnel attribute to identify bidirectional (multipoint-to-multipoint) multicast distribution trees.  However, the prior RFCs do not provide all the necessary procedures for using bidirectional tunnels to support multicast VPNs.  This document updates RFCs 6513, 6514, and 6625 by specifying those procedures.  In particular, it specifies the procedures for assigning customer multicast flows (unidirectional or bidirectional) to specific bidirectional tunnels in the provider backbone, for advertising such assignments, and for determining which flows have been assigned to which tunnels.

### Extranet Multicast in BGP/IP MPLS VPNs  (draft-ietf-bess-mvpn-extranet)
Previous RFCs specify the procedures necessary to allow IP multicast traffic to travel from one site to another within a BGP/MPLS IP VPN (Virtual Private Network).  However, it is sometimes desirable to allow multicast traffic whose source is in one VPN to be received by systems that are in another VPN.  This is known as a "Multicast VPN (MVPN) extranet".  This document updates RFCs 6513, 6514, and 6625 by specifying the procedures that are necessary in order to provide extranet MVPN service.

### Global Table Multicast with BGP Multicast VPN (BGP-MVPN) Procedures  (draft-ietf-bess-mvpn-global-table-mcast)
RFCs 6513, 6514, and others describe protocols and procedures that a Service Provider (SP) may deploy in order to offer Multicast Virtual Private Network (Multicast VPN or MVPN) service to its customers.  Some of these procedures use BGP to distribute VPN-specific multicast routing information across a backbone network.  With a small number of relatively minor modifications, the same BGP procedures can also be used to distribute multicast routing information that is not specific to any VPN.  Multicast that is outside the context of a VPN is known as "Global Table Multicast", or sometimes simply as "Internet multicast".  In this document, we describe the modifications that are needed to use the BGP-MVPN procedures for Global Table Multicast.

### Virtual Private Wire Service Support in Ethernet VPN  (draft-ietf-bess-evpn-vpws)
This document describes how Ethernet VPN (EVPN) can be used to support the Virtual Private Wire Service (VPWS) in MPLS/IP networks.  EVPN accomplishes the following for VPWS: provides Single-Active as well as All-Active multihoming with flow-based load-balancing, eliminates the need for Pseudowire (PW) signaling, and provides fast protection convergence upon node or link failure.

### Ingress Replication Tunnels in Multicast VPN  (draft-ietf-bess-ir)
RFCs 6513, 6514, and other RFCs describe procedures by which a Service Provider may offer Multicast VPN (MVPN) service to its customers.  These procedures create point-to-multipoint (P2MP) or multipoint-to-multipoint (MP2MP) trees across the Service Provider's backbone.  One type of P2MP tree that may be used is known as an "Ingress Replication (IR) tunnel".  In an IR tunnel, a parent node need not be directly connected to its child nodes.  When a parent node has to send a multicast data packet to its n child nodes, it does not use Layer 2 multicast, IP multicast, or MPLS multicast to do so.  Rather, it makes n individual copies, and then unicasts each copy, through an IP or MPLS unicast tunnel, to exactly one child node.  While the prior MVPN specifications allow the use of IR tunnels, those specifications are not always very clear or explicit about how the MVPN protocol elements and procedures are applied to IR tunnels.  This document updates RFCs 6513 and 6514 by adding additional details that are specific to the use of IR tunnels.

### Interconnect Solution for Ethernet VPN (EVPN) Overlay Networks  (draft-ietf-bess-dci-evpn-overlay)
This document describes how Network Virtualization Overlays (NVOs) can be connected to a Wide Area Network (WAN) in order to extend the Layer 2 connectivity required for some tenants.  The solution analyzes the interaction between NVO networks running Ethernet Virtual Private Networks (EVPNs) and other Layer 2 VPN (L2VPN) technologies used in the WAN, such as Virtual Private LAN Services (VPLSs), VPLS extensions for Provider Backbone Bridging (PBB-VPLS), EVPN, or PBB-EVPN.  It also describes how the existing technical specifications apply to the interconnection and extends the EVPN procedures needed in some cases.  In particular, this document describes how EVPN routes are processed on Gateways (GWs) that interconnect EVPN-Overlay and EVPN-MPLS networks, as well as the Interconnect Ethernet Segment (I-ES), to provide multihoming.  This document also describes the use of the Unknown MAC Route (UMR) to avoid issues of a Media Access Control (MAC) scale on Data Center Network Virtualization Edge (NVE) devices.

### FIB Reduction in Virtual Subnet  (draft-ietf-bess-virtual-subnet-fib-reduction)
Virtual Subnet is a BGP/MPLS IP VPN-based subnet extension solution
   which is intended for building Layer3 network virtualization overlays
   within and/or between data centers.  This document describes a
   mechanism for reducing the FIB size of PE routers in the Virtual
   Subnet context.

### IP Prefix Advertisement in Ethernet VPN (EVPN)  (draft-ietf-bess-evpn-prefix-advertisement)
The BGP MPLS-based Ethernet VPN (EVPN) (RFC 7432) mechanism provides a flexible control plane that allows intra-subnet connectivity in an MPLS and/or Network Virtualization Overlay (NVO) (RFC 7365) network.  In some networks, there is also a need for dynamic and efficient inter-subnet connectivity across Tenant Systems and end devices that can be physical or virtual and do not necessarily participate in dynamic routing protocols.  This document defines a new EVPN route type for the advertisement of IP prefixes and explains some use-case examples where this new route type is used.

### Multicast VPN State Damping  (draft-ietf-bess-multicast-damping)
This document describes procedures to damp Multicast VPN (MVPN) routing state changes and control the effect of the churn due to the multicast dynamicity in customer sites.  The procedures described in this document are applicable to BGP-based multicast VPN and help avoid uncontrolled control-plane load increase in the core routing infrastructure.  The new procedures proposed were inspired by BGP unicast route damping principles that have been adapted to multicast.

## Working Group: cose
### CBOR Object Signing and Encryption (COSE): AES-CTR and AES-CBC  (draft-ietf-cose-aes-ctr-and-cbc)
The Concise Binary Object Representation (CBOR) data format is designed for small code size and small message size.  CBOR Object Signing and Encryption (COSE) is specified in RFC 9052 to provide basic security services using the CBOR data format.  This document specifies the conventions for using AES-CTR and AES-CBC as content encryption algorithms with COSE.

### COSE "typ" (type) Header Parameter  (draft-ietf-cose-typ-header-parameter)
This specification adds the equivalent of the JSON Object Signing and
   Encryption (JOSE) typ (type) header parameter to CBOR Object Signing
   and Encryption (COSE).  This enables the benefits of explicit typing,
   as defined in the JSON Web Token Best Current Practices BCP, to be
   brought to COSE objects.  The syntax of the COSE type header
   parameter value is the same as the existing COSE content type header
   parameter.

### CBOR Encoded Message Syntax  (draft-schaad-cose-msg)
Concise Binary Object Representation (CBOR) is data format designed
   for small code size and small message size.  There is a need for the
   ability to have the basic security services defined for this data
   format.  This document specifies how to do signatures, message
   authentication codes and encryption using this data format.

### CBOR Object Signing and Encryption (COSE)  (draft-ietf-cose-msg)
Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size.  There is a need for the ability to have basic security services defined for this data format.  This document defines the CBOR Object Signing and Encryption (COSE) protocol.  This specification describes how to create and process signatures, message authentication codes, and encryption using CBOR for serialization.  This specification additionally describes how to represent cryptographic keys using CBOR.

### Use of the HSS/LMS Hash-Based Signature Algorithm with CBOR Object Signing and Encryption (COSE)  (draft-ietf-cose-hash-sig)
This document specifies the conventions for using the Hierarchical Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based signature algorithm with the CBOR Object Signing and Encryption (COSE) syntax.  The HSS/LMS algorithm is one form of hash-based digital signature; it is described in RFC 8554.

### CBOR Object Signing and Encryption (COSE): Header Parameters for Carrying and Referencing X.509 Certificates  (draft-ietf-cose-x509)
The CBOR Object Signing and Encryption (COSE) message structure uses references to keys in general.  For some algorithms, additional properties are defined that carry parameters relating to keys as needed.  The COSE Key structure is used for transporting keys outside of COSE messages.  This document extends the way that keys can be identified and transported by providing attributes that refer to or contain X.509 certificates.

### CBOR Object Signing and Encryption (COSE): Initial Algorithms  (draft-ietf-cose-rfc8152bis-algs)
Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size. There is a need to be able to define basic security services for this data format. This document defines a set of algorithms that can be used with the CBOR Object Signing and Encryption (COSE) protocol (RFC 9052).

 This document, along with RFC 9052, obsoletes RFC 8152.

### CBOR Object Signing and Encryption (COSE): Structures and Process  (draft-ietf-cose-rfc8152bis-struct)
Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size. There is a need to be able to define basic security services for this data format. This document defines the CBOR Object Signing and Encryption (COSE) protocol. This specification describes how to create and process signatures, message authentication codes, and encryption using CBOR for serialization. This specification additionally describes how to represent cryptographic keys using CBOR.

 This document, along with RFC 9053, obsoletes RFC 8152.

### CBOR Object Signing and Encryption (COSE): Hash Algorithms  (draft-ietf-cose-hash-algs)
The CBOR Object Signing and Encryption (COSE) syntax (see RFC 9052) does not define any direct methods for using hash algorithms.  There are, however, circumstances where hash algorithms are used, such as indirect signatures, where the hash of one or more contents are signed, and identification of an X.509 certificate or other object by the use of a fingerprint.  This document defines hash algorithms that are identified by COSE algorithm identifiers.

### CBOR Object Signing and Encryption (COSE) and JSON Object Signing and Encryption (JOSE) Registrations for Web Authentication (WebAuthn) Algorithms  (draft-ietf-cose-webauthn-algorithms)
The W3C Web Authentication (WebAuthn) specification and the FIDO Alliance FIDO2 Client to Authenticator Protocol (CTAP) specification use CBOR Object Signing and Encryption (COSE) algorithm identifiers.  This specification registers the following algorithms (which are used by WebAuthn and CTAP implementations) in the IANA "COSE Algorithms" registry: RSASSA-PKCS1-v1_5 using SHA-256, SHA-384, SHA-512, and SHA-1; and Elliptic Curve Digital Signature Algorithm (ECDSA) using the secp256k1 curve and SHA-256.  It registers the secp256k1 elliptic curve in the IANA "COSE Elliptic Curves" registry.  Also, for use with JSON Object Signing and Encryption (JOSE), it registers the algorithm ECDSA using the secp256k1 curve and SHA-256 in the IANA "JSON Web Signature and Encryption Algorithms" registry and the secp256k1 elliptic curve in the IANA "JSON Web Key Elliptic Curve" registry.

### CBOR Object Signing and Encryption (COSE): Countersignatures  (draft-ietf-cose-countersign)
Concise Binary Object Representation (CBOR) is a data format designed for small code size and small message size.  CBOR Object Signing and Encryption (COSE) defines a set of security services for CBOR.  This document defines a countersignature algorithm along with the needed header parameters and CBOR tags for COSE.  This document updates RFC 9052.

### JOSE and COSE Encoding for Post-Quantum Signatures  (draft-ietf-cose-post-quantum-signatures)
This document describes JSON and CBOR serializations for several
   Post-Quantum Cryptography (PQC) based suites including CRYSTALS
   Dilithium, Falcon, and SPHINCS+.

   This document does not define any new cryptography, only
   seralizations of existing cryptographic systems.

   This document registers key types for JOSE and COSE, specifically
   LWE, NTRU, and HASH.

   Key types in this document are specified by the cryptographic
   algorithm family in use by a particular algorithm as discussed in
   RFC7517.

   This document registers signature algorithms types for JOSE and COSE,
   specifically CRYDI3 and others as required for use of various post-
   quantum signature schemes.

### FN-DSA for JOSE and COSE  (draft-ietf-cose-falcon)
This document specifies JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for FFT
   (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature
   Algorithm (FN-DSA), a Post-Quantum Cryptography (PQC) digital
   signature scheme defined in US NIST FIPS 206 (expected to be
   published in late 2026 early 2027).

   It does not define new cryptographic primitives; rather, it specifies
   how existing FN-DSA mechanisms are serialized for use in JOSE and
   COSE.  This document registers signature algorithms for JOSE and
   COSE, specifically FN-DSA-512 and FN-DSA-1024.

### SLH-DSA for JOSE and COSE  (draft-ietf-cose-sphincs-plus)
This document specifies JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for
   Stateless Hash-Based Digital Signature Standard (SLH-DSA), a Post-
   Quantum Cryptography (PQC) digital signature scheme defined in US
   NIST FIPS 205.

### CBOR Web Token (CWT) Claims in COSE Headers  (draft-ietf-cose-cwt-claims-in-headers)
This document describes how to include CBOR Web Token (CWT) claims in
   the header parameters of any COSE structure.  This functionality
   helps to facilitate applications that wish to make use of CBOR Web
   Token (CWT) claims in encrypted COSE structures and/or COSE
   structures featuring detached signatures, while having some of those
   claims be available before decryption and/or without inspecting the
   detached payload.  Another use case is using CWT claims with payloads
   that are not CWT Claims Sets, including payloads that are not CBOR at
   all.

### CBOR Object Signing and Encryption (COSE) Key Thumbprint  (draft-ietf-cose-key-thumbprint)
This specification defines a method for computing a hash value over a
   CBOR Object Signing and Encryption (COSE) Key. It specifies which
   fields within the COSE Key structure are included in the
   cryptographic hash computation, the process for creating a canonical
   representation of these fields, and how to hash the resulting byte
   sequence.  The resulting hash value, referred to as a "thumbprint,"
   can be used to identify or select the corresponding key.

### ML-DSA for JOSE and COSE  (draft-ietf-cose-dilithium)
This document specifies JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for Module-
   Lattice-Based Digital Signature Standard (ML-DSA), a Post-Quantum
   Cryptography (PQC) digital signature scheme defined in US NIST FIPS
   204.

### COSE Header parameter for RFC 3161 Time-Stamp Tokens  (draft-ietf-cose-tsa-tst-header-parameter)
This document defines two CBOR Signing And Encrypted (COSE) header
   parameters for incorporating RFC 3161-based timestamping into COSE
   message structures (COSE_Sign and COSE_Sign1).  This enables the use
   of established RFC 3161 timestamping infrastructure in COSE-based
   protocols.

### Use of Hybrid Public-Key Encryption (HPKE) with CBOR Object Signing and Encryption (COSE)  (draft-ietf-cose-hpke)
This specification defines hybrid public-key encryption (HPKE) for
   use with CBOR Object Signing and Encryption (COSE).  HPKE offers a
   variant of public-key encryption of arbitrary-sized plaintexts for a
   recipient public key.

   HPKE is a general encryption framework utilizing an asymmetric key
   encapsulation mechanism (KEM), a key derivation function (KDF), and
   an Authenticated Encryption with Associated Data (AEAD) algorithm.

   This document defines the use of HPKE with COSE.  Authentication for
   HPKE in COSE is provided by COSE-native security mechanisms or by the
   pre-shared key authenticated variant of HPKE.

### COSE Hash Envelope  (draft-ietf-cose-hash-envelope)
This document defines new COSE header parameters for signaling a
   payload as an output of a hash function.  This mechanism enables
   faster validation, as access to the original payload is not required
   for signature validation.  Additionally, hints of the hashed
   payload's content format and availability are defined, providing
   references to optional discovery mechanisms that can help to find
   original payload content.

### Barreto-Lynn-Scott Elliptic Curve Key Representations for JOSE and COSE  (draft-ietf-cose-bls-key-representations)
This specification defines how to represent cryptographic keys for
   the pairing-friendly elliptic curves known as Barreto-Lynn-Scott
   (BLS), for use with the key representation formats of JSON Web Key
   (JWK) and COSE (COSE_Key).

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/tplooker/draft-ietf-cose-bls-key-representations.

### COSE (CBOR Object Signing and Encryption) Receipts  (draft-ietf-cose-merkle-tree-proofs)
COSE (CBOR Object Signing and Encryption) Receipts prove properties
   of a verifiable data structure to a verifier.  Verifiable data
   structures and associated proof types enable security properties,
   such as minimal disclosure, transparency and non-equivocation.
   Transparency helps maintain trust over time, and has been applied to
   certificates, end to end encrypted messaging systems, and supply
   chain security.  This specification enables concise transparency
   oriented systems, by building on CBOR (Concise Binary Object
   Representation) and COSE.  The extensibility of the approach is
   demonstrated by providing CBOR encodings for Merkle inclusion and
   consistency proofs.

### Test Vectors for CBOR Encoded X.509 (C509) Certificates  (draft-ietf-cose-c509-test-vectors)
This document contains examples of CBOR-encoded X.509 (C509)
   certificates, certification requests, and certification request
   templates.

### Split Signing Algorithms for COSE  (draft-ietf-cose-split-signing-algs)
This specification defines COSE algorithm identifiers for negotiating
   how to split a signature algorithm between two cooperating parties.
   Typically the first party hashes the data to be signed and the second
   party finishes the signature over the hashed data.  This is a common
   technique, useful for example when the signing private key is held in
   a smart card or similar hardware component with limited processing
   power and communication bandwidth.  The resulting signatures are
   identical in structure to those computed by a single party, and can
   be verified using the same verification algorithm without additional
   steps to preprocess the signed data.

### CBOR Encoded X.509 Certificates (C509 Certificates)  (draft-ietf-cose-cbor-encoded-cert)
This document specifies a CBOR encoding of X.509 certificates.  The
   resulting certificates are called C509 certificates.  The CBOR
   encoding supports a large subset of RFC 5280 and common certificate
   profiles, and it is extensible.

   Two types of C509 certificates are defined.  One type is an
   invertible CBOR re-encoding of DER-encoded X.509 certificates with
   the signature field copied from the DER encoding.  The other type is
   identical except that the signature is computed over the CBOR
   encoding instead of the DER encoding, thereby avoiding the use of
   ASN.1.  Both types of certificates have the same semantics as X.509
   while providing comparable size reduction.

   This document also specifies CBOR-encoded data structures for
   certification requests and certification request templates, new COSE
   headers, as well as a TLS certificate type and a file format for
   C509.  This document updates RFC 6698 by extending the TLSA selectors
   registry to include C509 certificates.

## Working Group: dnsop
### DNS Terminology  (draft-ietf-dnsop-rfc8499bis)
The Domain Name System (DNS) is defined in literally dozens of
   different RFCs.  The terminology used by implementers and developers
   of DNS protocols, and by operators of DNS systems, has changed in the
   decades since the DNS was first defined.  This document gives current
   definitions for many of the terms used in the DNS in a single
   document.

   This document updates RFC 2308 by clarifying the definitions of
   "forwarder" and "QNAME".  It obsoletes RFC 8499 by adding multiple
   terms and clarifications.  Comprehensive lists of changed and new
   definitions can be found in Appendices A and B.

### Compact Denial of Existence in DNSSEC  (draft-huque-dnsop-compact-lies)
This document describes a technique to generate a signed DNS response
   on demand for a non-existent name by claiming that the name exists
   but doesn't have any data for the queried record type.  Such answers
   require only one minimal NSEC record, allow online signing servers to
   minimize signing operations and response sizes, and prevent zone
   content disclosure.

### The .alt Special-Use Top-Level Domain  (draft-ietf-dnsop-alt-tld)
This document reserves a Top-Level Domain (TLD) label "alt" to be used in non-DNS contexts.  It also provides advice and guidance to developers creating alternative namespaces.

### In the DNS, QDCOUNT is (usually) One  (draft-ietf-dnsop-qdcount-is-one)
This document updates RFC 1035 by constraining the allowed value of
   the QDCOUNT parameter in DNS messages with OPCODE = 0 (QUERY) to a
   maximum of one, and specifies the required behaviour when values that
   are not allowed are encountered.

### DNS Glue Requirements in Referral Responses  (draft-ietf-dnsop-glue-is-not-optional)
The DNS uses glue records to allow iterative clients to find the addresses of name servers that are contained within a delegated zone.  Authoritative servers are expected to return all available glue records for in-domain name servers in a referral response.  If message size constraints prevent the inclusion of all glue records for in-domain name servers, the server must set the TC (Truncated) flag to inform the client that the response is incomplete and that the client should use another transport to retrieve the full response.  This document updates RFC 1034 to clarify correct server behavior.

### Greasing Protocol Extension Points in the DNS  (draft-huque-dnsop-grease)
Long term evolvability of the Domain Name System (DNS) protocol
   requires the ability to support change.  Greasing is one technique
   that exercises the regular use of unallocated protocol extension
   points to prevent ossification of their current usage patterns by
   middleboxes or DNS implementations.  This document describes
   considerations and proposals for applying grease to the DNS protocol.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/shuque/ietf-dns-grease.

### Use of GOST 2012 Signature Algorithms in DNSKEY and RRSIG Resource Records for DNSSEC  (draft-ietf-dnsop-rfc5933-bis)
This document describes how to produce digital signatures and hash
   functions using the GOST R 34.10-2012 and GOST R 34.11-2012
   algorithms for DNSKEY, RRSIG, and DS resource records, for use in the
   Domain Name System Security Extensions (DNSSEC).

   This document obsoletes RFC 5933 and updates RFC 8624.

### Service Binding and Parameter Specification via the DNS (SVCB and HTTPS Resource Records)  (draft-ietf-dnsop-svcb-https)
This document specifies the "SVCB" ("Service Binding") and "HTTPS" DNS resource record (RR) types to facilitate the lookup of information needed to make connections to network services, such as for HTTP origins.  SVCB records allow a service to be provided from multiple alternative endpoints, each with associated parameters (such as transport protocol configuration), and are extensible to support future uses (such as keys for encrypting the TLS ClientHello).  They also enable aliasing of apex domains, which is not possible with CNAME.  The HTTPS RR is a variation of SVCB for use with HTTP (see RFC 9110, "HTTP Semantics").  By providing more information to the client before it attempts to establish a connection, these records offer potential benefits to both performance and privacy.

### Remove deprecated GOST algorithms from active use within DNSSEC  (draft-hardaker-dnsop-must-not-ecc-gost)
This document retires the use of ECC-GOST within DNSSEC.

### Initializing a DNS Resolver with Priming Queries  (draft-klh-dnsop-rfc8109bis)
This document describes the queries that a DNS resolver should emit
   to initialize its cache.  The result is that the resolver gets both a
   current NS Resource Record Set (RRset) for the root zone and the
   necessary address information for reaching the root servers.

   This document, when published, obsoletes RFC 8109.

### Running a Root Server Local to a Resolver  (draft-ietf-dnsop-7706bis)
Some DNS recursive resolvers have longer-than-desired round-trip times to the closest DNS root server; those resolvers may have difficulty getting responses from the root servers, such as during a network attack. Some DNS recursive resolver operators want to prevent snooping by third parties of requests sent to DNS root servers. In both cases, resolvers can greatly decrease the round-trip time and prevent observation of requests by serving a copy of the full root zone on the same server, such as on a loopback address or in the resolver software. This document shows how to start and maintain such a copy of the root zone that does not cause problems for other users of the DNS, at the cost of adding some operational fragility for the operator.

 This document obsoletes RFC 7706.

### Consistency for CDS/CDNSKEY and CSYNC is Mandatory  (draft-thomassen-dnsop-cds-consistency)
Maintenance of DNS delegations requires occasional changes of the DS
   and NS record sets on the parent side of the delegation.  [RFC7344]
   automates this for DS records by having the child publish CDS and/or
   CDNSKEY records which hold the prospective DS parameters.  Similarly,
   CSYNC records indicate a desired update of the delegation's NS
   records [RFC7477].  Parent-side entities (e.g.  Registries,
   Registrars) typically discover these records by periodically querying
   them from the child ("polling"), before using them to update the
   delegation's parameters.

   This document specifies that if polling is used, parent-side entities
   MUST ensure that updates triggered via CDS/CDNSKEY and CSYNC records
   are consistent across the child's authoritative nameservers, before
   taking any action based on these records.

### DNS Error Reporting  (draft-ietf-dnsop-dns-error-reporting)
DNS error reporting is a lightweight reporting mechanism that
   provides the operator of an authoritative server with reports on DNS
   resource records that fail to resolve or validate.  A domain owner or
   DNS hosting organization can use these reports to improve domain
   hosting.  The reports are based on extended DNS errors as described
   in [RFC8914].

   When a domain name fails to resolve or validate due to a
   misconfiguration or an attack, the operator of the authoritative
   server may be unaware of this.  To mitigate this lack of feedback,
   this document describes a method for a validating resolver to
   automatically signal an error to a monitoring agent specified by the
   authoritative server.  The error is encoded in the QNAME, thus the
   very act of sending the query is to report the error.

### Negative Caching of DNS Resolution Failures  (draft-ietf-dnsop-caching-resolution-failures)
In the DNS, resolvers employ caching to reduce both latency for end
   users and load on authoritative name servers.  The process of
   resolution may result in one of three types of responses: (1) a
   response containing the requested data; (2) a response indicating the
   requested data does not exist; or (3) a non-response due to a
   resolution failure in which the resolver does not receive any useful
   information regarding the data's existence.  This document concerns
   itself only with the third type.

   RFC 2308 specifies requirements for DNS negative caching.  There,
   caching of type (2) responses is mandatory and caching of type (3)
   responses is optional.  This document updates RFC 2308 to require
   negative caching for DNS resolution failures.

   RFC 4035 allows DNSSEC validation failure caching.  This document
   updates RFC 4035 to require caching for DNSSEC validation failures.

   RFC 4697 prohibits aggressive requerying for NS records at a failed
   zone's parent zone.  This document updates RFC 4697 to expand this
   requirement to all query types and to all ancestor zones.

### CHAIN Query Requests in DNS  (draft-ietf-dnsop-edns-chain-query)
This document defines an EDNS0 extension that can be used by a security-aware validating resolver configured to use a forwarding resolver to send a single query, requesting a complete validation path along with the regular query answer.  The reduction in queries potentially lowers the latency and reduces the need to send multiple queries at once.  This extension mandates the use of source-IP- verified transport such as TCP or UDP with EDNS-COOKIE, so it cannot be abused in amplification attacks.

### The edns-tcp-keepalive EDNS0 Option  (draft-ietf-dnsop-edns-tcp-keepalive)
DNS messages between clients and servers may be received over either UDP or TCP. UDP transport involves keeping less state on a busy server, but can cause truncation and retries over TCP. Additionally, UDP can be exploited for reflection attacks. Using TCP would reduce retransmits and amplification. However, clients commonly use TCP only for retries and servers typically use idle timeouts on the order of seconds.

 This document defines an EDNS0 option ("edns-tcp-keepalive") that allows DNS servers to signal a variable idle timeout. This signalling encourages the use of long-lived TCP connections by allowing the state associated with TCP transport to be managed effectively with minimal impact on the DNS transaction time.

### A Common Operational Problem in DNS Servers - Failure To Respond.  (draft-andrews-dns-no-response-issue)
The DNS is a query / response protocol.  Failure to respond or to
   respond correctly to queries causes both immediate operational
   problems and long term problems with protocol development.

   This document identifies a number of common classes of queries to
   which some servers either fail to respond or else respond
   incorrectly.  This document also suggests procedures for TLD and
   other similar zone operators to apply to help reduce / eliminate the
   problem.

   The document does not look at the DNS data itself, just the structure
   of the responses.

### Root Name Server Operational Requirements  (draft-ietf-dnsop-root-opreq)
The primary focus of this document is to provide guidelines for operation of the root name servers.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Distributing Authoritative Name Servers via Shared Unicast Addresses  (draft-ietf-dnsop-hardie-shared-root-server)
This memo describes a set of practices intended to enable an authoritative name server operator to provide access to a single named server in multiple locations.  The primary motivation for the development and deployment of these practices is to increase the distribution of Domain Name System (DNS) servers to previously under- served areas of the network topology and to reduce the latency for DNS query responses in those areas.  This memo provides information for the Internet community.

### Observed DNS Resolution Misbehavior  (draft-ietf-dnsop-bad-dns-res)
This memo describes DNS iterative resolver behavior that results in a significant query volume sent to the root and top-level domain (TLD) name servers.  We offer implementation advice to iterative resolver developers to alleviate these unnecessary queries.  The recommendations made in this document are a direct byproduct of observation and analysis of abnormal query traffic patterns seen at two of the thirteen root name servers and all thirteen com/net TLD name servers.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Requirements for a Mechanism Identifying a Name Server Instance  (draft-ietf-dnsop-serverid)
With the increased use of DNS anycast, load balancing, and other mechanisms allowing more than one DNS name server to share a single IP address, it is sometimes difficult to tell which of a pool of name servers has answered a particular query.  A standardized mechanism to determine the identity of a name server responding to a particular query would be useful, particularly as a diagnostic aid for administrators.  Existing ad hoc mechanisms for addressing this need have some shortcomings, not the least of which is the lack of prior analysis of exactly how such a mechanism should be designed and deployed.  This document describes the existing convention used in some widely deployed implementations of the DNS protocol, including advantages and disadvantages, and discusses some attributes of an improved mechanism.  This memo provides information for the Internet community.

### Operational Considerations and Issues with IPv6 DNS  (draft-ietf-dnsop-ipv6-dns-issues)
This memo presents operational considerations and issues with IPv6 Domain Name System (DNS), including a summary of special IPv6 addresses, documentation of known DNS implementation misbehavior, recommendations and considerations on how to perform DNS naming for service provisioning and for DNS resolver IPv6 support, considerations for DNS updates for both the forward and reverse trees, and miscellaneous issues.  This memo is aimed to include a summary of information about IPv6 DNS considerations for those who have experience with IPv4 DNS.  This memo provides information for the Internet community.

### DNS IPv6 Transport Operational Guidelines  (draft-ietf-dnsop-ipv6-transport-guidelines)
This memo provides guidelines and Best Current Practice for operating DNS in a world where queries and responses are carried in a mixed environment of IPv4 and IPv6 networks.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### DNSSEC Operational Practices  (draft-ietf-dnsop-dnssec-operational-practices)
This document describes a set of practices for operating the DNS with security extensions (DNSSEC). The target audience is zone administrators deploying DNSSEC.

 The document discusses operational aspects of using keys and signatures in the DNS. It discusses issues of key generation, key storage, signature generation, key rollover, and related policies.

 This document obsoletes RFC 2541, as it covers more operational ground and gives more up-to-date requirements with respect to key sizes and the new DNSSEC specification. This memo provides information for the Internet community.

### Common Misbehavior Against DNS Queries for IPv6 Addresses  (draft-ietf-dnsop-misbehavior-against-aaaa)
There is some known misbehavior of DNS authoritative servers when they are queried for AAAA resource records.  Such behavior can block IPv4 communication that should actually be available, cause a significant delay in name resolution, or even make a denial of service attack.  This memo describes details of known cases and discusses their effects.  This memo provides information for the Internet community.

### IPv6 Host Configuration of DNS Server Information Approaches  (draft-ietf-dnsop-ipv6-dns-configuration)
This document describes three approaches for IPv6 recursive DNS server address configuration.  It details the operational attributes of three solutions: RA option, DHCPv6 option, and well-known anycast addresses for recursive DNS servers.  Additionally, it suggests the deployment scenarios in four kinds of networks (ISP, enterprise, 3GPP, and unmanaged networks) considering multi-solution resolution.  This memo provides information for the Internet community.

### DNS Terminology  (draft-ietf-dnsop-dns-terminology)
The DNS is defined in literally dozens of different RFCs.  The terminology used by implementers and developers of DNS protocols, and by operators of DNS systems, has sometimes changed in the decades since the DNS was first defined.  This document gives current definitions for many of the terms used in the DNS in a single document.

### Preventing Use of Recursive Nameservers in Reflector Attacks  (draft-ietf-dnsop-reflectors-are-evil)
This document describes ways to prevent the use of default configured recursive nameservers as reflectors in Denial of Service (DoS) attacks.  It provides recommended configuration as measures to mitigate the attack.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Domain Name System (DNS) Cookies  (draft-eastlake-dnsext-cookies)
DNS cookies are a lightweight DNS transaction security mechanism that
   provides limited protection to DNS servers and clients against a
   variety of increasingly common denial-of-service and amplification /
   forgery or cache poisoning attacks by off-path attackers. DNS Cookies
   are tolerant of NAT, NAT-PT, and anycast and can be incrementally
   deployed.

### Locally Served DNS Zones  (draft-ietf-dnsop-default-local-zones)
Experience with the Domain Name System (DNS) has shown that there are a number of DNS zones that all iterative resolvers and recursive nameservers should automatically serve, unless configured otherwise.  RFC 4193 specifies that this should occur for D.F.IP6.ARPA.  This document extends the practice to cover the IN-ADDR.ARPA zones for RFC 1918 address space and other well-known zones with similar characteristics.  This memo documents an Internet Best Current Practice.

### DNS Scoped Data Through '_Underscore' Attribute Leaves  (draft-crocker-dns-attrleaf)
Historically, any DNS RR may occur for any domain name.  Recent
   additions have defined DNS leaf nodes that contain a reserved node
   name, beginning with an underscore.  The underscore construct is used
   to define a semantic scope for DNS records that are associated with
   the parent domain.  This specification explores the nature of this
   DNS usage and defines the "underscore names" registry with IANA.

### Initializing a DNS Resolver with Priming Queries  (draft-ietf-dnsop-resolver-priming)
This document describes the queries that a DNS resolver should emit to initialize its cache.  The result is that the resolver gets both a current NS Resource Record Set (RRset) for the root zone and the necessary address information for reaching the root servers.

### I'm Being Attacked by PRISONER.IANA.ORG!  (draft-ietf-dnsop-as112-under-attack-help-help)
Many sites connected to the Internet make use of IPv4 addresses that are not globally unique. Examples are the addresses designated in RFC 1918 for private use within individual sites.

 Hosts should never normally send DNS reverse-mapping queries for those addresses on the public Internet. However, such queries are frequently observed. Authoritative servers are deployed to provide authoritative answers to such queries as part of a loosely coordinated effort known as the AS112 project.

 Since queries sent to AS112 servers are usually not intentional, the replies received back from those servers are typically unexpected. Unexpected inbound traffic can trigger alarms on intrusion detection systems and firewalls, and operators of such systems often mistakenly believe that they are being attacked.

 This document provides background information and technical advice to those firewall operators. This document is not an Internet Standards Track specification; it is published for informational purposes.

### AS112 Nameserver Operations  (draft-ietf-dnsop-as112-ops)
Many sites connected to the Internet make use of IPv4 addresses that are not globally unique. Examples are the addresses designated in RFC 1918 for private use within individual sites.

 Devices in such environments may occasionally originate Domain Name System (DNS) queries (so-called "reverse lookups") corresponding to those private-use addresses. Since the addresses concerned have only local significance, it is good practice for site administrators to ensure that such queries are answered locally. However, it is not uncommon for such queries to follow the normal delegation path in the public DNS instead of being answered within the site.

 It is not possible for public DNS servers to give useful answers to such queries. In addition, due to the wide deployment of private-use addresses and the continuing growth of the Internet, the volume of such queries is large and growing. The AS112 project aims to provide a distributed sink for such queries in order to reduce the load on the IN-ADDR.ARPA authoritative servers. The AS112 project is named after the Autonomous System Number (ASN) that was assigned to it.

 This document describes the steps required to install a new AS112 node and offers advice relating to such a node's operation. This document is not an Internet Standards Track specification; it is published for informational purposes.

### Requirements for Management of Name Servers for the DNS  (draft-ietf-dnsop-name-server-management-reqs)
Management of name servers for the Domain Name System (DNS) has traditionally been done using vendor-specific monitoring, configuration, and control methods. Although some service monitoring platforms can test the functionality of the DNS itself, there is not an interoperable way to manage (monitor, control, and configure) the internal aspects of a name server itself.

 This document discusses the requirements of a management system for name servers and can be used as a shopping list of needed features for such a system. This document is not an Internet Standards Track specification; it is published for informational purposes.

### Reverse DNS in IPv6 for Internet Service Providers  (draft-howard-isp-ip6rdns)
In IPv4, Internet Service Providers (ISPs) commonly provide IN-
   ADDR.ARPA information for their customers by prepopulating the zone
   with one PTR record for every available address.  This practice does
   not scale in IPv6.  This document analyzes different approaches and
   considerations for ISPs in managing the ip6.arpa zone for IPv6
   address space assigned to many customers.

### DNSSEC Key Rollover Timing Considerations  (draft-ietf-dnsop-dnssec-key-timing)
This document describes the issues surrounding the timing of events in the rolling of a key in a DNSSEC-secured zone.  It presents timelines for the key rollover and explicitly identifies the relationships between the various parameters affecting the process.

### DNSSEC Operational Practices, Version 2  (draft-ietf-dnsop-rfc4641bis)
This document describes a set of practices for operating the DNS with security extensions (DNSSEC). The target audience is zone administrators deploying DNSSEC.

 The document discusses operational aspects of using keys and signatures in the DNS. It discusses issues of key generation, key storage, signature generation, key rollover, and related policies.

 This document obsoletes RFC 4641, as it covers more operational ground and gives more up-to-date requirements with respect to key sizes and the DNSSEC operations.

### Algorithm Implementation Requirements and Usage Guidance for DNSSEC  (draft-wouters-sury-dnsop-algorithm-update)
The DNSSEC protocol makes use of various cryptographic algorithms in
   order to provide authentication of DNS data and proof of non-
   existence.  To ensure interoperability between DNS resolvers and DNS
   authoritative servers, it is necessary to specify a set of algorithm
   implementation requirements and usage guidance to ensure that there
   is at least one algorithm that all implementations support.  This
   document defines the current algorithm implementation requirements
   and usage guidance for DNSSEC.  This document obsoletes RFC-6944.

### Decreasing Access Time to Root Servers by Running One on Loopback  (draft-ietf-dnsop-root-loopback)
Some DNS recursive resolvers have longer-than-desired round-trip times to the closest DNS root server.  Some DNS recursive resolver operators want to prevent snooping of requests sent to DNS root servers by third parties.  Such resolvers can greatly decrease the round-trip time and prevent observation of requests by running a copy of the full root zone on a loopback address (such as 127.0.0.1).  This document shows how to start and maintain such a copy of the root zone that does not pose a threat to other users of the DNS, at the cost of adding some operational fragility for the operator.

### A Framework for DNSSEC Policies and DNSSEC Practice Statements  (draft-ietf-dnsop-dnssec-dps-framework)
This document presents a framework to assist writers of DNS Security Extensions (DNSSEC) Policies and DNSSEC Practice Statements, such as domain managers and zone operators on both the top level and secondary level, who are managing and operating a DNS zone with Security Extensions implemented.

 In particular, the framework provides a comprehensive list of topics that should be considered for inclusion into a DNSSEC Policy definition and Practice Statement. This document is not an Internet Standards Track specification; it is published for informational purposes.

### Domain Name System (DNS) Cookies  (draft-ietf-dnsop-cookies)
DNS Cookies are a lightweight DNS transaction security mechanism that provides limited protection to DNS servers and clients against a variety of increasingly common denial-of-service and amplification/ forgery or cache poisoning attacks by off-path attackers.  DNS Cookies are tolerant of NAT, NAT-PT (Network Address Translation - Protocol Translation), and anycast and can be incrementally deployed. (Since DNS Cookies are only returned to the IP address from which they were originally received, they cannot be used to generally track Internet users.)

### AS112 Redirection Using DNAME  (draft-ietf-dnsop-as112-dname)
AS112 provides a mechanism for handling reverse lookups on IP addresses that are not unique (e.g., RFC 1918 addresses). This document describes modifications to the deployment and use of AS112 infrastructure that will allow zones to be added and dropped much more easily, using DNAME resource records.

 This approach makes it possible for any DNS zone administrator to sink traffic relating to parts of the global DNS namespace under their control to the AS112 infrastructure without coordination with the operators of AS112 infrastructure.

### Adding 100.64.0.0/10 Prefixes to the IPv4 Locally-Served DNS Zones Registry  (draft-ietf-dnsop-rfc6598-rfc6303)
RFC 6598 specifies that "Reverse DNS queries for Shared Address Space addresses [100.64.0.0/10] MUST NOT be forwarded to the global DNS infrastructure."

 This document formally directs IANA to add the associated zones to the "IPv4 Locally-Served DNS Zones Registry" to prevent such queries from accidentally leaking to the global DNS infrastructure.

### Automating DNSSEC Delegation Trust Maintenance  (draft-ietf-dnsop-delegation-trust-maintainance)
This document describes a method to allow DNS Operators to more easily update DNSSEC Key Signing Keys using the DNS as a communication channel.  The technique described is aimed at delegations in which it is currently hard to move information from the Child to Parent.

### The ALT Special Use Top Level Domain  (draft-wkumari-dnsop-alt-tld)
This document reserves a string (ALT) to be used as a TLD label in
   non-DNS contexts or for names that have no meaning in a global
   context.  It also provides advice and guidance to developers
   developing alternate namespaces.

   [ Ed note: This document lives in GitHub at:
   https://github.com/wkumari/draft-wkumari-dnsop-alt-tld . Issues and
   pull requests happily accpeted. ]

### Recommendations for DNSSEC Resolvers Operators  (draft-mglt-dnsop-dnssec-validator-requirements)
The DNS Security Extensions define a process for validating received
   data and assert them authentic and complete as opposed to forged.

   This document is focused clarifying the scope and responsibilities of
   DNSSEC Resolver Operators (DRO) as well as operational
   recommendations that DNSSEC validators operators SHOULD put in place
   in order to implement sufficient Trust that makes DNSSEC validation
   output accurate.  The recommendations described in this document
   include, provisioning mechanisms as well as monitoring and management
   mechanisms.

### Child-to-Parent Synchronization in DNS  (draft-ietf-dnsop-child-syncronization)
This document specifies how a child zone in the DNS can publish a record to indicate to a parental agent that the parental agent may copy and process certain records from the child zone.  The existence of the record and any change in its value can be monitored by a parental agent and acted on depending on local policy.

### DNSSEC Roadblock Avoidance  (draft-ietf-dnsop-dnssec-roadblock-avoidance)
This document describes problems that a Validating DNS resolver, stub-resolver, or application might run into within a non-compliant infrastructure.  It outlines potential detection and mitigation techniques.  The scope of the document is to create a shared approach to detect and overcome network issues that a DNSSEC software/system may face.

### AS112 Nameserver Operations  (draft-ietf-dnsop-rfc6304bis)
Many sites connected to the Internet make use of IPv4 addresses that are not globally unique. Examples are the addresses designated in RFC 1918 for private use within individual sites.

 Devices in such environments may occasionally originate Domain Name System (DNS) queries (so-called "reverse lookups") corresponding to those private-use addresses. Since the addresses concerned have only local significance, it is good practice for site administrators to ensure that such queries are answered locally. However, it is not uncommon for such queries to follow the normal delegation path in the public DNS instead of being answered within the site.

 It is not possible for public DNS servers to give useful answers to such queries. In addition, due to the wide deployment of private-use addresses and the continuing growth of the Internet, the volume of such queries is large and growing. The AS112 project aims to provide a distributed sink for such queries in order to reduce the load on the corresponding authoritative servers. The AS112 project is named after the Autonomous System Number (ASN) that was assigned to it.

 This document describes the steps required to install a new AS112 node and offers advice relating to such a node's operation.

 This document obsoletes RFC 6304.

### DNS query name minimisation to improve privacy  (draft-bortzmeyer-dns-qname-minimisation)
This document describes one of the techniques that could be used to
   improve DNS privacy (see [I-D.bortzmeyer-dnsop-dns-privacy]), a
   technique called "qname minimisation".

   Discussions of the document should currently take place on the dns-
   privacy mailing list [dns-privacy].

### DNS Query Name Minimisation to Improve Privacy  (draft-ietf-dnsop-qname-minimisation)
This document describes a technique to improve DNS privacy, a technique called "QNAME minimisation", where the DNS resolver no longer sends the full original QNAME to the upstream name server.

### Decreasing Access Time to Root Servers by Running One on Loopback  (draft-wkumari-dnsop-root-loopback)
Some DNS recursive resolvers have longer-than-desired round trip
   times to the closest DNS root server.  Such resolvers can greatly
   decrease the round trip time by running a copy of the full root zone
   on a loopback address (such as 127.0.0.1).  Typically, the vast
   majority of queries going to the root are for names that do not exist
   in the root zone, and the negative answers are cached for a much
   shorter period of time.  This document shows how to start and
   maintain such a copy of the root zone in a manner that is secure for
   the operator of the recursive resolver and does not pose a threat to
   other users of the DNS.

### DNS Transport over TCP - Implementation Requirements  (draft-dickinson-dnsop-5966-bis)
This document updates the requirements for the support of TCP as a
   transport protocol for DNS implementations.

### Client Subnet in DNS Queries  (draft-ietf-dnsop-edns-client-subnet)
This document describes an Extension Mechanisms for DNS (EDNS0) option that is in active use to carry information about the network that originated a DNS query and the network for which the subsequent response can be cached.  Since it has some known operational and privacy shortcomings, a revision will be worked through the IETF for improvement.

### DNS Transport over TCP - Implementation Requirements  (draft-ietf-dnsop-5966bis)
This document specifies the requirement for support of TCP as a transport protocol for DNS implementations and provides guidelines towards DNS-over-TCP performance on par with that of DNS-over-UDP.  This document obsoletes RFC 5966 and therefore updates RFC 1035 and RFC 1123.

### Definition and Use of DNSSEC Negative Trust Anchors  (draft-ietf-dnsop-negative-trust-anchors)
DNS Security Extensions (DNSSEC) is now entering widespread deployment.  However, domain signing tools and processes are not yet as mature and reliable as those for non-DNSSEC-related domain administration tools and processes.  This document defines Negative Trust Anchors (NTAs), which can be used to mitigate DNSSEC validation failures by disabling DNSSEC validation at specified domains.

### Reverse DNS in IPv6 for Internet Service Providers  (draft-ietf-dnsop-isp-ip6rdns)
In IPv4, Internet Service Providers (ISPs) commonly provide IN-ADDR.ARPA information for their customers by prepopulating the zone with one PTR record for every available address.  This practice does not scale in IPv6.  This document analyzes different approaches and considerations for ISPs in managing the IP6.ARPA zone.

### The .onion Special-Use Domain Name  (draft-appelbaum-dnsop-onion-tld)
This document registers the ".onion" Special-Use Domain Name.

### Aggressive use of NSEC/NSEC3  (draft-fujiwara-dnsop-nsec-aggressiveuse)
While DNS highly depends on cache, its cache usage of non-existence
   information has been limited to exact matching.  This draft proposes
   the aggressive use of a NSEC/NSEC3 resource record, which is able to
   express non-existence of a range of names authoritatively.  With this
   proposal, it is expected that shorter latency to many of negative
   responses as well as some level of mitigation of random sub-domain
   attacks (referred to as "Water Torture" attacks).  It is also
   expected that non-existent TLD queries to Root DNS servers will
   decrease.

## Working Group: grow
### Updated BGP Operations and Security  (draft-fiebig-grow-bgpopsecupd)
The Border Gateway Protocol (BGP) is the protocol almost exclusively
   used in the Internet to exchange routing information between network
   domains.  Due to this central nature, it is important to understand
   the security and reliability measures that can and should be deployed
   to prevent accidental or intentional routing disturbances.

   Previously, security considerations for BGP have been described in
   [RFC7454].  Since the publications of [RFC7454], several developments
   and changes in operational practice took place that warrant an update
   of these best current practices.

   This document updates [RFC7454], reiterating the best practices for
   BGP security from that document and adding new practices and
   recommendations that emerged since the publication of [RFC7454].  In
   the current version, this document covers practices to protect the
   BGP sessions itself such as Time to Live (TTL), the TCP
   Authentication Option (TCP-AO), and control-plane filtering.  It also
   describes measures to better control the flow of routing information,
   using prefix filtering and automation of prefix filters, max-prefix
   filtering, Autonomous System(AS) path filtering, route flap
   dampening, and BGP community scrubbing.

   Newly added information and improvements include a unification of
   terminology, orienting it in [RFC9234], changing recommendations
   regarding IXP LAN prefixes to align with operational practice,
   discussing ASPA and BGP roles, expanding on community scrubbing,
   filter generation and evaluation practices to limit performance
   overhead, expanding on outbound and internal filtering for defense in
   depth, global prefix limits, and community based filtering for
   downstream prefixes.

### Logging of routing events in BGP Monitoring Protocol (BMP)  (draft-lucente-grow-bmp-rel)
The BGP Monitoring Protocol (BMP) does provision for BGP session
   event logging (Peer Up, Peer Down), state synchronization (Route
   Monitoring), debugging (Route Mirroring) and Statistics messages,
   among the others.  This document defines a new Route Event Logging
   (REL) message type for BMP with the aim of covering use-cases with
   affinity to alerting, reporting and on-change analysis.

### Distribution of Diverse BGP Paths  (draft-ietf-grow-diverse-bgp-path-dist)
The BGP4 protocol specifies the selection and propagation of a single best path for each prefix. As defined and widely deployed today, BGP has no mechanisms to distribute alternate paths that are not considered best path between its speakers. This behavior results in a number of disadvantages for new applications and services.

 The main objective of this document is to observe that by simply adding a new session between a route reflector and its client, the Nth best path can be distributed. This document also compares existing solutions and proposed ideas that enable distribution of more paths than just the best path.

 This proposal does not specify any changes to the BGP protocol definition. It does not require a software upgrade of provider edge (PE) routers acting as route reflector clients. This document is not an Internet Standards Track specification; it is published for informational purposes.

### YANG Module for BGP Communities  (draft-pels-grow-yang-bgp-communities)
This document provides a YANG module for describing BGP communities.

### BMP Peer Up Message Namespace  (draft-ietf-grow-bmp-peer-up)
RFC 7854, BGP Monitoring Protocol, uses different message types for
   different purposes.  Most of these are Type, Length, Value (TLV)
   structured.  One message type, the Peer Up message, lacks a set of
   TLVs defined for its use, instead sharing a namespace with the
   Initiation message.  Subsequent experience has shown that this
   namespace sharing was a mistake, as it hampers the extension of the
   protocol.

   This document updates RFC 7854 by creating an independent namespace
   for the Peer Up message.  It also updates RFC 8671 and RFC 9069 by
   moving the defined codepoints in the newly introduced registry.
   Compliant implementations of RFC 7854, RFC 8671 and RFC 9069 also
   comply with this specification.

### Currently Used Terminology in Global Routing Operations  (draft-ietf-grow-routing-ops-terms)
Operating the global routing ecosystem entails a divers set of
   interacting components, while operational practice evolved over time.
   In that time, terms emerged, disappeared, and sometimes changed their
   meaning.

   To aid operators and implementers in reading contemporary drafts,
   this document provides an overview of terms and abbreviations used in
   the global routing operations community.  The document explicitly
   does not serve as an authoritative source of correct terminology, but
   instead strives to provide an overview of practice.

### Revision to Registration Procedures for Multiple BMP Registries  (draft-ietf-grow-bmp-registries-change)
This document updates RFC 7854, "BGP Monitoring Protocol (BMP)", by changing the registration procedures for several registries.  Specifically, any BMP registry with a range of 32768-65530 designated "Specification Required" has that range redesignated as "First Come First Served".

### Peering API  (draft-ramseyer-grow-peering-api)
We propose an API standard for BGP Peering, also known as interdomain
   interconnection through global Internet Routing.  This API offers a
   standard way to request public (settlement-free) peering, verify the
   status of a request or BGP session, and list potential connection
   locations.  The API is backed by PeeringDB OIDC, the industry
   standard for peering authentication.  We also propose future work to
   cover private peering, and alternative authentication methods.

### BMP Extension for Path Status TLV  (draft-ietf-grow-bmp-path-marking-tlv)
The BGP Monitoring Protocol (BMP) provides an interface for obtaining
   BGP path information, which is conveyed through BMP Route Monitoring
   (RM) messages.  This document specifies a BMP extension to convey the
   status of a path after being processed by the BGP process.

### Definition For New BMP Statistics Type  (draft-msri-grow-bmp-bgp-rib-stats)
RFC 7854 defined different BMP statistics messages types to observe
   interesting events that occur on the router.  This document updates
   RFC 7854 by adding new statistics type.

### Impact of BGP Filtering on Inter-Domain Routing Policies  (draft-ietf-grow-filtering-threats)
This document describes how unexpected traffic flows can emerge across an autonomous system as the result of other autonomous systems filtering or restricting the propagation of more-specific prefixes.  We provide a review of the techniques to detect the occurrence of this issue and defend against it.

### The "import-via" and "export-via" attributes in RPSL Policy Specifications  (draft-snijders-rpsl-via)
This document defines two attributes in the aut-num Class which can
   be used in RPSL policy specifications to publish desired routing
   policy regarding non-adjacent networks.

### Considerations for Internet Routing Registries (IRRs) and Routing Policy Configuration  (draft-ietf-grow-irr-routing-policy-considerations)
The purpose of this document is to catalog issues that influenced the efficacy of Internet Routing Registries (IRRs) for inter-domain routing policy specification and application in the global routing system over the past two decades.  Additionally, it provides a discussion regarding which of these issues are still problematic in practice, and which are simply artifacts that are no longer applicable but continue to stifle inter-provider policy-based filtering adoption and IRR utility to this day.

### Route-Leaks & MITM Attacks Against BGPSEC  (draft-ietf-grow-simple-leak-attack-bgpsec-no-help)
This document describes a very simple attack vector that illustrates
   how RPKI-enabled BGPSEC machinery as currently defined can be easily
   circumvented in order to launch a Man In The Middle (MITM) attack via
   BGP.  It is meant to serve as input to the IETF's Global Routing
   Operations Working group (GROW) during routing security requirements
   discussions and subsequent specification.

### Controlling the redistribution of BGP routes  (draft-ietf-grow-bgp-redistribution)
This document proposes the redistribution extended community.  This
new extended community allows a router to influence how a specific
route should be redistributed towards a specified set of eBGP
speakers. Several types of redistribution communities are proposed.
The first type may be used to indicate that a specific route should
not be announced over a specified set of eBGP sessions. The second
type may be used to indicate that the attached route should only be
announced with the NO_EXPORT community over the specified set of eBGP
sessions and the third type may be used to indicate that the attached
route should be prepended n times when announced over a specified set
of eBGP sessions.

### Bounding Longest Match Considered  (draft-grow-bounded-longest-match)
Some ASes currently use length-based filters to manage the size of
the routing table they use and propagate.  This draft explores an
alternative to length-based filters which allows for more automatic
configuration and which provides for better redundancy.
Rather than use a filter, this draft proposes a method of modifying
the BGP longest match algorithm by setting a bound on the prefix
lengths eligible for preference.  A bound would operate on long
prefixes when covering route announcements are available; in certain
circumstances it would cause a router to prefer an aggregate over a
more specific route announcement.

### BGP Communities for Data Collection  (draft-ietf-grow-collection-communities)
BGP communities (RFC 1997) are used by service providers for many purposes, including tagging of customer, peer, and geographically originated routes.  Such tagging is typically used to control the scope of redistribution of routes within a provider's network and to its peers and customers.  With the advent of large-scale BGP data collection (and associated research), it has become clear that the information carried in such communities is essential for a deeper understanding of the global routing system.  This memo defines standard (outbound) communities and their encodings for export to BGP route collectors.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### BGP MULTI_EXIT_DISC (MED) Considerations  (draft-ietf-grow-bgp-med-considerations)
The BGP MULTI_EXIT_DISC (MED) attribute provides a mechanism for BGP speakers to convey to an adjacent AS the optimal entry point into the local AS. While BGP MEDs function correctly in many scenarios, a number of issues may arise when utilizing MEDs in dynamic or complex topologies.

 This document discusses implementation and deployment considerations regarding BGP MEDs and provides information with which implementers and network operators should be familiar. This memo provides information for the Internet community.

### Embedding Globally-Routable Internet Addresses Considered Harmful  (draft-ietf-grow-embed-addr)
This document discourages the practice of embedding references to unique, globally-routable IP addresses in Internet hosts, describes some of the resulting problems, and considers selected alternatives.  This document is intended to clarify best current practices in this regard.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Operational Concerns and Considerations for Routing Protocol Design -- Risk, Interference, and Fit (RIFT)  (draft-ietf-grow-rift)
The Risk, Interference, and Fit (RIFT) design team was formed to
   document the concerns and considerations surrounding the use of
   Internet routing protocols for functions not directly related to
   routing of IP packets within the Internet and IP networks. This
   document is the output of that activity.

### BGP Wedgies  (draft-ietf-grow-bgp-wedgies)
It has commonly been assumed that the Border Gateway Protocol (BGP) is a tool for distributing reachability information in a manner that creates forwarding paths in a deterministic manner.  In this memo we will describe a class of BGP configurations for which there is more than one potential outcome, and where forwarding states other than the intended state are equally stable.  Also, the stable state where BGP converges may be selected by BGP in a non-deterministic manner.  These stable, but unintended, BGP states are termed here "BGP Wedgies".  This memo provides information for the Internet community.

### Operation of Anycast Services  (draft-ietf-grow-anycast)
As the Internet has grown, and as systems and networked services within enterprises have become more pervasive, many services with high availability requirements have emerged. These requirements have increased the demands on the reliability of the infrastructure on which those services rely.

 Various techniques have been employed to increase the availability of services deployed on the Internet. This document presents commentary and recommendations for distribution of services using anycast. This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan  (draft-ietf-grow-rfc1519bis)
This memo discusses the strategy for address assignment of the existing 32-bit IPv4 address space with a view toward conserving the address space and limiting the growth rate of global routing state.  This document obsoletes the original Classless Inter-domain Routing (CIDR) spec in RFC 1519, with changes made both to clarify the concepts it introduced and, after more than twelve years, to update the Internet community on the results of deploying the technology described.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Multi-Threaded Routing Toolkit (MRT) Routing Information Export Format  (draft-ietf-grow-mrt)
This document describes the MRT format for routing information export.  This format was developed in concert with the Multi-threaded Routing Toolkit (MRT) from whence the format takes it name.  The format can be used to export routing protocol messages, state changes, and routing information base contents. [STANDARDS-TRACK]

### BGP Monitoring Protocol (BMP)  (draft-ietf-grow-bmp)
This document defines the BGP Monitoring Protocol (BMP), which can be used to monitor BGP sessions.  BMP is intended to provide a convenient interface for obtaining route views.  Prior to the introduction of BMP, screen scraping was the most commonly used approach to obtaining such views.  The design goals are to keep BMP simple, useful, easily implemented, and minimally service affecting.  BMP is not suitable for use as a routing protocol.

### Routing System Stability  (draft-ietf-grow-rss)
Understanding the dynamics of the Internet routing system is 
   fundamental to ensure its robustness/stability and to improve the 
   mechanisms of the BGP routing protocol. This documents outlines a 
   program of activity for identifying, documenting and analyzing the 
   dynamic properties of the Internet and its routing system.

### MPLS Tunnels for Virtual Aggregation  (draft-ietf-grow-va-mpls)
The document "FIB Suppression with Virtual Aggregation"
[I-D.francis-intra-va] describes how FIB size may be reduced.  The
latest revision of that draft refers generically to tunnels, and
leaves it to other documents to define the usage and signaling
methods for specific tunnel types.  This document provides those
definitions for MPLS Label Switched Paths (LSP), without tag
stacking.

### Requirements for the Graceful Shutdown of BGP Sessions  (draft-ietf-grow-bgp-graceful-shutdown-requirements)
The Border Gateway Protocol (BGP) is heavily used in Service Provider networks for both Internet and BGP/MPLS VPN services.  For resiliency purposes, redundant routers and BGP sessions can be deployed to reduce the consequences of an Autonomous System Border Router (ASBR) or BGP session breakdown on customers' or peers' traffic.  However, simply taking down or even bringing up a BGP session for maintenance purposes may still induce connectivity losses during the BGP convergence.  This is no longer satisfactory for new applications (e.g., voice over IP, online gaming, VPN).  Therefore, a solution is required for the graceful shutdown of a (set of) BGP session(s) in order to limit the amount of traffic loss during a planned shutdown.  This document expresses requirements for such a solution.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Graceful BGP Session Shutdown  (draft-ietf-grow-bgp-gshut)
This document standardizes a new well-known BGP community, GRACEFUL_SHUTDOWN, to signal the graceful shutdown of paths.  This document also describes operational procedures that use this well-known community to reduce the amount of traffic lost when BGP peering sessions are about to be shut down deliberately, e.g., for planned maintenance.

### Performance of Virtual Aggregation  (draft-ietf-grow-va-perf)
The document "FIB Suppression with Virtual Aggregation"
[I-D.francis-intra-va] describes how router FIB size may be reduced.
This approach entails a trade-off between path-length and load versus
FIB size.  It also has the potential to reduce convergence time.
This document describes the results of several studies that examine
these characteristics.  The results of a study for a Tier-1 ISP with
a relatively sophisticated deployment of VA, shows that FIB size
could be reduced ten times or more with a worst-case latency penalty
of 4ms and a worst-case load increase of <1.5%.  Another study,
examining a much simpler style of VA deployment, also for a Tier-1
ISP, shows that FIB size can be reduced by four times (in routers
serving as APRs), and more than 10 times in other routers.  Here,
worst-case latency increase was 16 ms, though this is almost
certainly an over-estimate, both because traceroute was used to make
the measurement, and because popular prefixes were not considered.

### GRE and IP-in-IP Tunnels for Virtual Aggregation  (draft-ietf-grow-va-gre)
The document "FIB Suppression with Virtual Aggregation" [I-D.grow-va]
   describes how FIB size may be reduced.  That draft refers generically
   to tunnels, and leaves it to other documents to define the tunnel
   establishment methods for specific tunnel types.  This document
   provides those definitions for GRE and IP-in-IP tunnels.

### Proposal to use an inner MPLS label to identify the remote ASBR VA  (draft-ietf-grow-va-mpls-innerlabel)
The draft "MPLS Tunnels for Virtual Aggregation"
[I-D.ietf-grow-va-mpls] specifies how MPLS is used as the tunneling
protocol for Virtual Aggregation (VA).  The -00 version of that draft
specifies only one level of labels, with the result that one Label
Switched Path (LSP) for every remote ASBR must be established.  For
large ISPs, this can amount to a large number of LSPs.  This draft
proposes adding the option of using an inner label to identify the
remote ASBR.  Either an outer label or an IP tunnel is used to reach
the local ASBR.  When MPLS is used as the tunneling protocol, this
reduces the number of LSPs to the number of local border routers
(ASBR).

### Simple Virtual Aggregation (S-VA)  (draft-ietf-grow-simple-va)
All BGP routers in the Default-Free Zone (DFZ) are required to carry all routes in the Default-Free Routing Table (DFRT). This document describes a technique, Simple Virtual Aggregation (S-VA), that allows some BGP routers not to install all of those routes into the Forwarding Information Base (FIB).

 Some routers in an Autonomous System (AS) announce an aggregate (the VA prefix) in addition to the routes they already announce. This enables other routers not to install the routes covered by the VA prefix into the FIB as long as those routes have the same next-hop as the VA prefix.

 The VA prefixes that are announced within an AS are not announced to any other AS. The described functionality is of very low operational complexity, as it proposes a confined BGP speaker solution without any dependency on network-wide configuration or requirement for any form of intra-domain tunneling. This document is not an Internet Standards Track specification; it is published for informational purposes.

### Multi-Threaded Routing Toolkit (MRT) Border Gateway Protocol (BGP) Routing Information Export Format with Geo-Location Extensions  (draft-ietf-grow-geomrt)
This document updates the Multi-threaded Routing Toolkit (MRT) export format for Border Gateway Protocol (BGP) routing information by extending it to include optional terrestrial coordinates of a BGP collector and its BGP peers. [STANDARDS-TRACK]

### Unique Origin Autonomous System Numbers (ASNs) per Node for Globally Anycasted Services  (draft-ietf-grow-unique-origin-as)
This document makes recommendations regarding the use of unique origin autonomous system numbers (ASNs) per node for globally anycasted critical infrastructure services in order to provide routing system discriminators for a given anycasted prefix.  Network management and monitoring techniques, or other operational mechanisms, may employ this new discriminator in whatever manner best accommodates their operating environment.  This memo documents an Internet Best Current Practice.

### Time to Remove Filters for Previously Unallocated IPv4 /8s  (draft-ietf-grow-no-more-unallocated-slash8s)
It has been common for network administrators to filter IP traffic from and BGP prefixes of unallocated IPv4 address space. Now that there are no longer any unallocated IPv4 /8s, this practise is more complicated, fragile, and expensive. Network administrators are advised to remove filters based on the registration status of the address space.

 This document explains why any remaining packet and BGP prefix filters for unallocated IPv4 /8s should now be removed on border routers and documents those IPv4 unicast prefixes that should not be routed across the public Internet. This memo documents an Internet Best Current Practice.

### Issues with Private IP Addressing in the Internet  (draft-ietf-grow-private-ip-sp-cores)
The purpose of this document is to provide a discussion of the potential problems of using private, RFC 1918, or non-globally routable addressing within the core of a Service Provider (SP) network.  The discussion focuses on link addresses and, to a small extent, loopback addresses.  While many of the issues are well recognised within the ISP community, there appears to be no document that collectively describes the issues.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Internet Exchange BGP Route Server Operations  (draft-ietf-grow-ix-bgp-route-server-operations)
The popularity of Internet Exchange Points (IXPs) brings new challenges to interconnecting networks. While bilateral External BGP (EBGP) sessions between exchange participants were historically the most common means of exchanging reachability information over an IXP, the overhead associated with this interconnection method causes serious operational and administrative scaling problems for IXP participants.

 Multilateral interconnection using Internet route servers can dramatically reduce the administrative and operational overhead associated with connecting to IXPs; in some cases, route servers are used by IXP participants as their preferred means of exchanging routing information.

 This document describes operational considerations for multilateral interconnections at IXPs.

### The "import-via" and "export-via" attributes in RPSL Policy Specifications  (draft-ietf-grow-rpsl-via)
This document defines two attributes in the aut-num Class which can
   be used in RPSL policy specifications to publish desired routing
   policy regarding non-adjacent networks.

### Problem Definition and Classification of BGP Route Leaks  (draft-ietf-grow-route-leak-problem-definition)
A systemic vulnerability of the Border Gateway Protocol routing system, known as "route leaks", has received significant attention in recent years.  Frequent incidents that result in significant disruptions to Internet routing are labeled route leaks, but to date a common definition of the term has been lacking.  This document provides a working definition of route leaks while keeping in mind the real occurrences that have received significant attention.  Further, this document attempts to enumerate (though not exhaustively) different types of route leaks based on observed events on the Internet.  The aim is to provide a taxonomy that covers several forms of route leaks that have been observed and are of concern to the Internet user community as well as the network operator community.

### Default External BGP (EBGP) Route Propagation Behavior without Policies  (draft-ietf-grow-bgp-reject)
This document updates RFC 4271 by defining the default behavior of a BGP speaker when there is no Import or Export Policy associated with an External BGP session.

### BLACKHOLE Community  (draft-ietf-grow-blackholing)
This document describes the use of a well-known Border Gateway Protocol (BGP) community for destination-based blackholing in IP networks.  This well-known advisory transitive BGP community named "BLACKHOLE" allows an origin Autonomous System (AS) to specify that a neighboring network should discard any traffic destined towards the tagged IP prefix.

### Multi-Threaded Routing Toolkit (MRT) Routing Information Export Format with BGP Additional Path Extensions  (draft-ietf-grow-mrt-add-paths)
This document extends the Multi-threaded Routing Toolkit (MRT) export format for Border Gateway Protocol (BGP) routing information by supporting the advertisement of multiple paths in BGP extensions.

### Usage of Large BGP Communities  (draft-snijders-grow-large-communities-usage)
Examples and inspiration for operators on how to use Large BGP
   Communities.

### Use of BGP Large Communities  (draft-ietf-grow-large-communities-usage)
This document presents examples and inspiration for operator application of BGP Large Communities.  Based on operational experience with BGP Communities, this document suggests logical categories of BGP Large Communities and demonstrates an orderly manner of organizing community values within them to achieve typical goals in routing policy.  Any operator can consider using the concepts presented as the basis for their own BGP Large Communities repertoire.

### Support for Adj-RIB-Out in BGP Monitoring Protocol (BMP)  (draft-evens-grow-bmp-adj-rib-out)
The BGP Monitoring Protocol (BMP) defines access to only the Adj-RIB-
   In Routing Information Bases (RIBs).  This document updates the BGP
   Monitoring Protocol (BMP) RFC 7854 by adding access to the Adj-RIB-
   Out RIBs. It adds a new flag to the peer header to distinguish Adj-
   RIB-In and Adj-RIB-Out.

### Support for Local RIB in BGP Monitoring Protocol (BMP)  (draft-evens-grow-bmp-local-rib)
The BGP Monitoring Protocol (BMP) defines access to the Adj-RIB-In
   and locally originated routes (e.g. routes distributed into BGP from
   protocols such as static) but not access to the BGP instance Loc-RIB.
   This document updates the BGP Monitoring Protocol (BMP) RFC 7854 by
   adding access to the BGP instance Local-RIB, as defined in RFC 4271
   the routes that have been selected by the local BGP speaker's
   Decision Process. These are the routes over all peers, locally
   originated, and after best-path selection.

### Mitigating the Negative Impact of Maintenance through BGP Session Culling  (draft-ietf-grow-bgp-session-culling)
This document outlines an approach to mitigate the negative impact on networks resulting from maintenance activities.  It includes guidance for both IP networks and Internet Exchange Points (IXPs).  The approach is to ensure BGP-4 sessions that will be affected by maintenance are forcefully torn down before the actual maintenance activities commence.

### Support for Local RIB in the BGP Monitoring Protocol (BMP)  (draft-ietf-grow-bmp-local-rib)
The BGP Monitoring Protocol (BMP) defines access to local Routing
Information Bases (RIBs).  This document updates BMP (RFC 7854) by
adding access to the Local Routing Information Base (Loc-RIB), as
defined in RFC 4271.  The Loc-RIB contains the routes that have been
selected by the local BGP speaker's Decision Process.

### Support for Adj-RIB-Out in the BGP Monitoring Protocol (BMP)  (draft-ietf-grow-bmp-adj-rib-out)
The BGP Monitoring Protocol (BMP) only defines access to the Adj-RIB-In Routing Information Bases (RIBs).  This document updates BMP (RFC 7854) by adding access to the Adj-RIB-Out RIBs.  It also adds a new flag to the peer header to distinguish between Adj-RIB-In and Adj-RIB-Out.

### Policy Behavior for Well-Known BGP Communities  (draft-ietf-grow-wkc-behavior)
Well-known BGP communities are manipulated differently across various current implementations, resulting in difficulties for operators.  Network operators should deploy consistent community handling across their networks while taking the inconsistent behaviors from the various BGP implementations into consideration.  This document recommends specific actions to limit future inconsistency: namely, BGP implementors must not create further inconsistencies from this point forward.  These behavioral changes, though subtle, actually update RFC 1997.

### RPKI Autonomous Systems Cones: A Profile To Define Sets of Autonomous Systems Numbers To Facilitate BGP Filtering  (draft-ietf-grow-rpki-as-cones)
This document describes a way to define groups of Autonomous System
   numbers in RPKI [RFC6480].  We call them AS-Cones.  AS-Cones provide
   a mechanism to be used by operators for filtering BGP-4 [RFC4271]
   announcements.

### Revision to Registration Procedures for Multiple BMP Registries  (draft-scudder-grow-bmp-registries-change)
This document updates RFC 7854, BGP Monitoring Protocol (BMP) by
   making a change to the registration procedures for several
   registries.  Specifically, any BMP registry with a range of
   32768-65530 designated "Specification Required" has that range re-
   designated as "First Come First Served".

### A well-known BGP community to denote prefixes used for Anycast  (draft-ietf-grow-anycast-community)
In theory routing decisions on the Internet and by extension within
   ISP networks should always use hot-potato routing to reach any given
   destination.  In reality operators sometimes choose to not use the
   hot-potato paths to forward traffic due to a variety of reasons,
   mostly motivated by traffic engineering considerations.  For prefixes
   carrying anycast traffic in virtually all situations it is advisable
   to stick to the hot-potato principle.  As operators mostly don't know
   which prefixes are carrying unicast or anycast traffic, they can't
   differentiate between them in their routing policies.

   To allow operators to take well informed decisions on which prefixes
   are carrying anycast traffic this document proposes a well-known BGP
   community to denote this property.

### AS Path Prepending  (draft-ietf-grow-as-path-prepending)
Autonomous System (AS) path prepending is a tool to manipulate the
   BGP AS_PATH attribute through prepending one or more Autonomous
   System Numbers (ASNs).  AS path prepending is used to deprioritize a
   route in the presence of a route with a shorter AS_PATH.  By
   prepending a local ASN multiple times, ASes can make advertised AS
   paths appear artificially longer.  However, excessive AS path
   prepending has caused routing issues in the Internet.  This document
   provides guidance for the use of AS path prepending, including
   alternative solutions, in order to avoid negatively affecting the
   Internet.

### A YANG Data Model for BMP  (draft-ietf-grow-bmp-yang)
This document defines a YANG data model for the configuration and
   monitoring of the BGP Monitoring Protocol (BMP).  The data model
   covers the base BMP protocol defined in [RFC7854] and includes
   support for the Loc-RIB extension defined in [RFC9069].

### Currently Used Terminology in Global Routing Operations  (draft-fiebig-grow-routing-ops-terms)
Operating the global routing ecosystem entails a divers set of
   interacting components, while operational practice evolved over time.
   In that time, terms emerged, disappeared, and sometimes changed their
   meaning.

   To aid operators and implementers in reading contemporary drafts,
   this document provides an overview of terms and abbreviations used in
   the global routing operations community.  The document explicitly
   does not serve as an authoritative source of correct terminology, but
   instead strives to provide an overview of practice.

### BMP Loc-RIB: Peer address  (draft-francois-grow-bmp-loc-peer)
BMP Loc-RIB lets a BMP publisher set the Peer Address value of a path
   information to zero.  This document introduces the option to
   communicate the actual peer from which a path was received when
   advertising that path with BMP Loc-RIB.

### Logging of routing events in BGP Monitoring Protocol (BMP)  (draft-ietf-grow-bmp-rel)
The BGP Monitoring Protocol (BMP) does provide for BGP session event
   logging (Peer Up, Peer Down), state synchronization (Route
   Monitoring), debugging (Route Mirroring) and Statistics messages,
   among others.  This document defines a new Route Event Logging (REL)
   message type for BMP with the aim of covering use cases with affinity
   to alerting, reporting and on-change analysis.

### TCP-AO Protection for BGP Monitoring Protocol (BMP)  (draft-ietf-grow-bmp-tcp-ao)
This document outlines the utilization of the TCP Authentication
   Option (TCP-AO), as specified in [RFC5925], for the authentication of
   BGP Monitoring Protocol (BMP) sessions, as specified in [RFC7854].
   TCP-AO provides for the authentication of BMP sessions established
   between routers and BMP stations at the TCP layer.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/hmntsharma/draft-hmntsharma-bmp-tcp-ao.

## Working Group: httpbis
### Structured Field Values for HTTP  (draft-ietf-httpbis-sfbis)
This document describes a set of data types and associated algorithms
   that are intended to make it easier and safer to define and handle
   HTTP header and trailer fields, known as "Structured Fields",
   "Structured Headers", or "Structured Trailers".  It is intended for
   use by specifications of new HTTP fields that wish to use a common
   syntax that is more restrictive than traditional HTTP field values.

   This document obsoletes RFC 8941.

### Template-Driven HTTP CONNECT Proxying for TCP  (draft-schwartz-httpbis-connect-tcp)
TCP proxying using HTTP CONNECT has long been part of the core HTTP
   specification.  However, this proxying functionality has several
   important deficiencies in modern HTTP environments.  This
   specification defines an alternative HTTP proxy service configuration
   for TCP connections.  This configuration is described by a URI
   Template, similar to the CONNECT-UDP and CONNECT-IP protocols.

### The ORIGIN Extension in HTTP/3  (draft-ietf-httpbis-origin-h3)
The ORIGIN frame for HTTP/2 is equally applicable to HTTP/3, but it needs to be separately registered.  This document describes the ORIGIN frame for HTTP/3.

### HTTP Proxy-Status Parameter for Next-Hop Aliases  (draft-ietf-httpbis-alias-proxy-status)
This document defines the next-hop-aliases HTTP Proxy-Status
   Parameter.  This parameter carries the list of aliases and canonical
   names an intermediary received during DNS resolution as part of
   establishing a connection to the next hop.

### HTTP Message Signatures  (draft-ietf-httpbis-message-signatures)
This document describes a mechanism for creating, encoding, and
   verifying digital signatures or message authentication codes over
   components of an HTTP message.  This mechanism supports use cases
   where the full HTTP message may not be known to the signer, and where
   the message may be transformed (e.g., by intermediaries) before
   reaching the verifier.  This document also describes a means for
   requesting that a signature be applied to a subsequent HTTP message
   in an ongoing HTTP exchange.

### Client-Cert HTTP Header Field  (draft-ietf-httpbis-client-cert-field)
This document describes HTTP extension header fields that allow a TLS terminating reverse proxy (TTRP) to convey the client certificate information of a mutually authenticated TLS connection to the origin server in a common and predictable manner.

### Window Sizing for Zstandard Content Encoding  (draft-jaju-httpbis-zstd-window-size)
Deployments of Zstandard, or "zstd", can use different window sizes
   to limit memory usage during compression and decompression.  Some
   browsers and user agents limit window sizes to mitigate memory usage
   concerns, causing interoperability issues.  This document updates the
   window size limit in RFC8878 from a recommendation to a requirement
   in HTTP contexts.

### HTTP Cache Groups  (draft-nottingham-http-cache-groups)
This specification introduces a means of describing the relationships
   between stored responses in HTTP caches, "grouping" them by
   associating a stored response with one or more opaque strings.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-nottingham-http-cache-groups/.

   information can be found at https://mnot.github.io/I-D/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mnot/I-D/labels/http-cache-groups.

### Compression Dictionary Transport  (draft-meenan-httpbis-compression-dictionary)
This specification defines a mechanism for using designated [HTTP]
   responses as an external dictionary for future HTTP responses for
   compression schemes that support using external dictionaries (e.g.
   Brotli [RFC7932] and Zstandard [RFC8878]).

### Secondary Certificate Authentication of HTTP Servers  (draft-egorbaty-httpbis-secondary-server-certs)
This document defines a way for HTTP/2 and HTTP/3 servers to send
   additional certificate-based credentials after a TLS connection is
   established, based on TLS Exported Authenticators.

### Extensible Prioritization Scheme for HTTP  (draft-ietf-httpbis-priority)
This document describes a scheme that allows an HTTP client to communicate its preferences for how the upstream server prioritizes responses to its requests, and also allows a server to hint to a downstream intermediary how its responses should be prioritized when they are forwarded.  This document defines the Priority header field for communicating the initial priority in an HTTP version-independent manner, as well as HTTP/2 and HTTP/3 frames for reprioritizing responses.  These share a common format structure that is designed to provide future extensibility.

### Secondary Certificate Authentication of HTTP Servers  (draft-ietf-httpbis-secondary-server-certs)
This document defines a way for HTTP/2 and HTTP/3 servers to send
   additional certificate-based credentials after a TLS connection is
   established, based on TLS Exported Authenticators.

### Window Sizing for Zstandard Content Encoding  (draft-ietf-httpbis-zstd-window-size)
Deployments of Zstandard, or "zstd", can use different window sizes
   to limit memory usage during compression and decompression.  Some
   browsers and user agents limit window sizes to mitigate memory usage
   concerns, causing interoperability issues.  This document updates the
   window size limit in RFC8878 from a recommendation to a requirement
   in HTTP contexts.

### No-Vary-Search  (draft-wicg-http-no-vary-search)
A proposed HTTP header field for changing how URL search parameters
   impact caching.

About This Document

   This note is to be removed before publishing as an RFC.

   The latest revision of this draft can be found at
   https://jeremyroman.github.io/http-no-vary-search/draft-wicg-http-no-
   vary-search.html.  Status information for this document may be found
   at https://datatracker.ietf.org/doc/draft-wicg-http-no-vary-search/.

   Source for this draft and an issue tracker can be found at
   https://github.com/jeremyroman/http-no-vary-search.

### HTTP Caching  (draft-ietf-httpbis-cache)
The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems. This document defines HTTP caches and the associated header fields that control cache behavior or indicate cacheable response messages.

 This document obsoletes RFC 7234.

### The Preliminary Request Denied HTTP Status Code  (draft-ietf-httpbis-pre-denied)
This specification defines a HTTP status code to indicate that the
   server is denying a prefetch or preload request.

### Security Considerations for Optimistic Use of HTTP Upgrade  (draft-schwartz-httpbis-optimistic-upgrade)
The HTTP/1.1 Upgrade mechanism allows the client to request a change
   to a new protocol.  This document discusses the security
   considerations that apply to data sent by the client before this
   request is confirmed, and updates RFC 9298 to avoid related security
   issues.

### HTTP/1.1  (draft-ietf-httpbis-messaging)
The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems. This document specifies the HTTP/1.1 message syntax, message parsing, connection management, and related security concerns.

 This document obsoletes portions of RFC 7230.

### HPACK: Header Compression for HTTP/2  (draft-ietf-httpbis-header-compression)
This specification defines HPACK, a compression format for efficiently representing HTTP header fields, to be used in HTTP/2.

### Hypertext Transfer Protocol (HTTP/1.1): Authentication  (draft-ietf-httpbis-p7-auth)
The Hypertext Transfer Protocol (HTTP) is a stateless application- level protocol for distributed, collaborative, hypermedia information systems.  This document defines the HTTP Authentication framework.

### Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing  (draft-ietf-httpbis-p1-messaging)
The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems.  This document provides an overview of HTTP architecture and its associated terminology, defines the "http" and "https" Uniform Resource Identifier (URI) schemes, defines the HTTP/1.1 message syntax and parsing requirements, and describes related security concerns for implementations.

### Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content  (draft-ietf-httpbis-p2-semantics)
The Hypertext Transfer Protocol (HTTP) is a stateless \%application- level protocol for distributed, collaborative, hypertext information systems.  This document defines the semantics of HTTP/1.1 messages, as expressed by request methods, request header fields, response status codes, and response header fields, along with the payload of messages (metadata and body content) and mechanisms for content negotiation.

### HTTP/1.1, part 3: Message Payload and Content Negotiation  (draft-ietf-httpbis-p3-payload)
This part is now obsolete.  Please see HTTPbis, Part 2.

### Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests  (draft-ietf-httpbis-p4-conditional)
The Hypertext Transfer Protocol (HTTP) is a stateless application- level protocol for distributed, collaborative, hypertext information systems.  This document defines HTTP/1.1 conditional requests, including metadata header fields for indicating state changes, request header fields for making preconditions on such state, and rules for constructing the responses to a conditional request when one or more preconditions evaluate to false.

### Hypertext Transfer Protocol (HTTP/1.1): Range Requests  (draft-ietf-httpbis-p5-range)
The Hypertext Transfer Protocol (HTTP) is a stateless application- level protocol for distributed, collaborative, hypertext information systems.  This document defines range requests and the rules for constructing and combining responses to those requests.

### Hypertext Transfer Protocol (HTTP/1.1): Caching  (draft-ietf-httpbis-p6-cache)
The Hypertext Transfer Protocol (HTTP) is a stateless \%application- level protocol for distributed, collaborative, hypertext information systems.  This document defines HTTP caches and the associated header fields that control cache behavior or indicate cacheable response messages.

### Security Requirements for HTTP  (draft-ietf-httpbis-security-properties)
Recent IESG practice dictates that IETF protocols must specify
   mandatory-to-implement (MTI) security mechanisms, so that all
   conformant implementations share a common baseline.  This document
   examines all widely deployed HTTP security technologies, and analyzes
   the trade-offs of each.

### Initial Hypertext Transfer Protocol (HTTP) Method Registrations  (draft-ietf-httpbis-method-registrations)
This document registers those Hypertext Transfer Protocol (HTTP) methods that have been defined in RFCs before the IANA HTTP Method Registry was established.

### Use of the Content-Disposition Header Field in the Hypertext Transfer Protocol (HTTP)  (draft-ietf-httpbis-content-disp)
RFC 2616 defines the Content-Disposition response header field, but points out that it is not part of the HTTP/1.1 Standard.  This specification takes over the definition and registration of Content-Disposition, as used in HTTP, and clarifies internationalization aspects. [STANDARDS-TRACK]

### Reactive Certificate-Based Client Authentication in HTTP/2  (draft-thomson-http2-client-certs)
Some HTTP servers provide a subset of resources that require
   additional authentication to interact with.  HTTP/1.1 servers rely on
   TLS renegotiation that is triggered by a request to a protected
   resource.  HTTP/2 made this pattern impossible by forbidding the use
   of TLS renegotiation.  While TLS 1.3 provides an alternate mechanism
   to obtain client certificates, this mechanism does not map well to
   usage in TLS 1.2.

   This document describes a how client authentication might be
   requested by a server as a result of receiving a request to a
   protected resource.

### Initial Hypertext Transfer Protocol (HTTP) Authentication Scheme Registrations  (draft-ietf-httpbis-authscheme-registrations)
This document registers Hypertext Transfer Protocol (HTTP) authentication schemes that have been defined in RFCs before the IANA HTTP Authentication Scheme Registry was established.

### The ORIGIN HTTP/2 Frame  (draft-ietf-httpbis-origin-frame)
This document specifies the ORIGIN frame for HTTP/2, to indicate what origins are available on a given connection.

### HTTP Client Hints  (draft-grigorik-http-client-hints)
An increasing diversity of Web-connected devices and software
   capabilities has created a need to deliver optimized content for each
   device.

   This specification defines a set of HTTP request header fields,
   colloquially known as Client Hints, to address this.  They are
   intended to be used as input to proactive content negotiation; just
   as the Accept header allows clients to indicate what formats they
   prefer, Client Hints allow clients to indicate a list of device and
   agent specific preferences.

### Hypertext Transfer Protocol Version 2 (HTTP/2)  (draft-ietf-httpbis-http2)
This specification describes an optimized expression of the semantics of the Hypertext Transfer Protocol (HTTP), referred to as HTTP version 2 (HTTP/2). HTTP/2 enables a more efficient use of network resources and a reduced perception of latency by introducing header field compression and allowing multiple concurrent exchanges on the same connection. It also introduces unsolicited push of representations from servers to clients.

 This specification is an alternative to, but does not obsolete, the HTTP/1.1 message syntax. HTTP's existing semantics remain unchanged.

### The Key HTTP Response Header Field  (draft-fielding-http-key)
The 'Key' header field for HTTP responses allows an origin server to
   describe the secondary cache key ([RFC7234], section 4.1) for a
   resource, by conveying what is effectively a short algorithm that can
   be used upon later requests to determine if a stored response is
   reusable for a given request.

   Key has the advantage of avoiding an additional round trip for
   validation whenever a new request differs slightly, but not
   significantly, from prior requests.

   Key also informs user agents of the request characteristics that
   might result in different content, which can be useful if the user
   agent is not sending request header fields in order to reduce the
   risk of fingerprinting.

### HTTP Alternative Services  (draft-ietf-httpbis-alt-svc)
This document specifies "Alternative Services" for HTTP, which allow an origin's resources to be authoritatively available at a separate network location, possibly accessed with a different protocol configuration.

### Opportunistic Security for HTTP/2  (draft-ietf-httpbis-http2-encryption)
This document describes how "http" URIs can be accessed using Transport Layer Security (TLS) and HTTP/2 to mitigate pervasive monitoring attacks.  This mechanism not a replacement for "https" URIs; it is vulnerable to active attacks.

### The ALPN HTTP Header Field  (draft-ietf-httpbis-tunnel-protocol)
This specification allows HTTP CONNECT requests to indicate what protocol is intended to be used within the tunnel once established, using the ALPN header field.

### The Hypertext Transfer Protocol Status Code 308 (Permanent Redirect)  (draft-ietf-httpbis-rfc7238bis)
This document specifies the additional Hypertext Transfer Protocol (HTTP) status code 308 (Permanent Redirect).

### Same-site Cookies  (draft-west-first-party-cookies)
This document updates RFC6265 by defining a "SameSite" attribute
   which allows servers to assert that a cookie ought not to be sent
   along with cross-site requests.  This assertion allows user agents to
   mitigate the risk of cross-origin information leakage, and provides
   some protection against cross-site request forgery attacks.

### HTTP SEARCH Method  (draft-snell-search-method)
This specification updates the definition and semantics of the HTTP
   SEARCH request method originally defined by RFC 5323.

### HTTP Authentication-Info and Proxy-Authentication-Info Response Header Fields  (draft-ietf-httpbis-auth-info)
This specification defines the "Authentication-Info" and "Proxy- Authentication-Info" response header fields for use in Hypertext Transfer Protocol (HTTP) authentication schemes that need to return information once the client's authentication credentials have been accepted.

### Hypertext Transfer Protocol (HTTP) Client-Initiated Content-Encoding  (draft-ietf-httpbis-cice)
In HTTP, content codings allow for payload encodings such as for compression or integrity checks. In particular, the "gzip" content coding is widely used for payload data sent in response messages.

 Content codings can be used in request messages as well; however, discoverability is not on par with response messages. This document extends the HTTP "Accept-Encoding" header field for use in responses, to indicate the content codings that are supported in requests.

### An HTTP Status Code to Report Legal Obstacles  (draft-ietf-httpbis-legally-restricted-status)
This document specifies a Hypertext Transfer Protocol (HTTP) status code for use when resource access is denied as a consequence of legal demands.

### The Key HTTP Response Header Field  (draft-ietf-httpbis-key)
The 'Key' header field for HTTP responses allows an origin server to
   describe the secondary cache key (RFC 7234, Section 4.1) for a
   resource, by conveying what is effectively a short algorithm that can
   be used upon later requests to determine if a stored response is
   reusable for a given request.

   Key has the advantage of avoiding an additional round trip for
   validation whenever a new request differs slightly, but not
   significantly, from prior requests.

   Key also informs user agents of the request characteristics that
   might result in different content, which can be useful if the user
   agent is not sending request header fields in order to reduce the
   risk of fingerprinting.

### The ORIGIN HTTP/2 Frame  (draft-nottingham-httpbis-origin-frame)
This document specifies the ORIGIN frame for HTTP/2, to indicate what
   origins are available on a given connection.

### Indicating Character Encoding and Language for HTTP Header Field Parameters  (draft-ietf-httpbis-rfc5987bis)
By default, header field values in Hypertext Transfer Protocol (HTTP) messages cannot easily carry characters outside the US-ASCII coded character set. RFC 2231 defines an encoding mechanism for use in parameters inside Multipurpose Internet Mail Extensions (MIME) header field values. This document specifies an encoding suitable for use in HTTP header fields that is compatible with a simplified profile of the encoding defined in RFC 2231.

 This document obsoletes RFC 5987.

### HTTP Client Hints  (draft-ietf-httpbis-client-hints)
HTTP defines proactive content negotiation to allow servers to select the appropriate response for a given request, based upon the user agent's characteristics, as expressed in request headers. In practice, user agents are often unwilling to send those request headers, because it is not clear whether they will be used, and sending them impacts both performance and privacy.

 This document defines an Accept-CH response header that servers can use to advertise their use of request headers for proactive content negotiation, along with a set of guidelines for the creation of such headers, colloquially known as "Client Hints."

### Encrypted Content-Encoding for HTTP  (draft-ietf-httpbis-encryption-encoding)
This memo introduces a content coding for HTTP that allows message payloads to be encrypted.

### Cookie Prefixes  (draft-ietf-httpbis-cookie-prefixes)
This document updates RFC6265 by adding a set of restrictions upon
   the names which may be used for cookies with specific properties.
   These restrictions enable user agents to smuggle cookie state to the
   server within the confines of the existing "Cookie" request header
   syntax, and limits the ways in which cookies may be abused in a
   conforming user agent.

### Deprecate modification of 'secure' cookies from non-secure origins  (draft-ietf-httpbis-cookie-alone)
This document updates RFC6265 by removing the ability for a non-
   secure origin to set cookies with a 'secure' flag, and to overwrite
   cookies whose 'secure' flag is set.  This deprecation improves the
   isolation between HTTP and HTTPS origins, and reduces the risk of
   malicious interference.

### Secondary Certificate Authentication in HTTP/2  (draft-bishop-httpbis-http2-additional-certs)
TLS provides fundamental mutual authentication services for HTTP,
   supporting up to one server certificate and up to one client
   certificate associated to the session to prove client and server
   identities as necessary.  This draft provides mechanisms for
   providing additional such certificates at the HTTP layer when these
   constraints are not sufficient.

   Many HTTP servers host content from several origins.  HTTP/2
   [RFC7540] permits clients to reuse an existing HTTP connection to a
   server provided that the secondary origin is also in the certificate
   provided during the TLS [I-D.ietf-tls-tls13] handshake.

   In many cases, servers will wish to maintain separate certificates
   for different origins but still desire the benefits of a shared HTTP
   connection.  Similarly, servers may require clients to present
   authentication, but have different requirements based on the content
   the client is attempting to access.

   This document describes how TLS exported authenticators
   [I-D.ietf-tls-exported-authenticator] can be used to provide proof of
   ownership of additional certificates to the HTTP layer to support
   both scenarios.

### Same-Site Cookies  (draft-ietf-httpbis-cookie-same-site)
This document updates RFC6265 by defining a "SameSite" attribute
   which allows servers to assert that a cookie ought not to be sent
   along with cross-site requests.  This assertion allows user agents to
   mitigate the risk of cross-origin information leakage, and provides
   some protection against cross-site request forgery attacks.

### A JSON Encoding for HTTP Header Field Values  (draft-ietf-httpbis-jfv)
This document establishes a convention for use of JSON-encoded field
   values in HTTP header fields.

Editorial Note (To be removed by RFC Editor before publication)

   Discussion of this draft takes place on the HTTPBIS working group
   mailing list (ietf-http-wg@w3.org), which is archived at
   <https://lists.w3.org/Archives/Public/ietf-http-wg/>.

   Working Group information can be found at <http://httpwg.github.io/>;
   source code and issues list for this draft can be found at
   <https://github.com/httpwg/http-extensions>.

   The changes in this draft are summarized in Appendix A.

### Cache Digests for HTTP/2  (draft-ietf-httpbis-cache-digest)
This specification defines a HTTP/2 frame type to allow clients to
   inform the server of their cache's contents.  Servers can then use
   this to inform their choices of what to push to clients.

Note to Readers

   Discussion of this draft takes place on the HTTP working group
   mailing list (ietf-http-wg@w3.org), which is archived at
   https://lists.w3.org/Archives/Public/ietf-http-wg/ .

   Working Group information can be found at http://httpwg.github.io/ ;
   source code and issues list for this draft can be found at
   https://github.com/httpwg/http-extensions/labels/cache-digest .

### Structured Field Values for HTTP  (draft-ietf-httpbis-header-structure)
This document describes a set of data types and associated algorithms that are intended to make it easier and safer to define and handle HTTP header and trailer fields, known as "Structured Fields", "Structured Headers", or "Structured Trailers".  It is intended for use by specifications of new HTTP fields that wish to use a common syntax that is more restrictive than traditional HTTP field values.

### HTTP Immutable Responses  (draft-ietf-httpbis-immutable)
The immutable HTTP response Cache-Control extension allows servers to identify resources that will not be updated during their freshness lifetime.  This ensures that a client never needs to revalidate a cached fresh resource to be certain it has not been modified.

### An HTTP Status Code for Indicating Hints  (draft-ietf-httpbis-early-hints)
This memo introduces an informational HTTP status code that can be used to convey hints that help a client make preparations for processing the final response.

### Expect-CT Extension for HTTP  (draft-ietf-httpbis-expect-ct)
This document defines a new HTTP header field named "Expect-CT", which allows web host operators to instruct user agents (UAs) to expect valid Signed Certificate Timestamps (SCTs) to be served on connections to these hosts.  Expect-CT allows web host operators to discover misconfigurations in their Certificate Transparency (CT) deployments.  Further, web host operators can use Expect-CT to ensure that if a UA that supports Expect-CT accepts a misissued certificate, that certificate will be discoverable in Certificate Transparency logs.

### HTTP Random Access and Live Content  (draft-ietf-httpbis-rand-access-live)
To accommodate byte-range requests for content that has data appended over time, this document defines semantics that allow an HTTP client and a server to perform byte-range GET and HEAD requests that start at an arbitrary byte offset within the representation and end at an indeterminate offset.

## Working Group: idr
### Deprecation of BGP OPEN Message Error subcodes 8, 9, and 10.  (draft-ietf-idr-deprecate-8-9-10)
This document requests IANA to mark BGP OPEN Message Error subcodes
   8, 9, and 10 as "deprecated".

### BGP for Mirror Binding  (draft-chen-idr-mbinding)
BGP is used to distribute a binding to a node.  The binding includes
   a binding SID and a path represented by a list of SIDs.  This
   document describes extensions to BGP for distributing the information
   about the binding to a protecting node.  For an SR path via the node
   with the binding SID, when the node fails, the protecting node such
   as the upstream neighbor on the path uses the information to protect
   the binding SID of the failed node.

### BGP Extensions for IDs Allocation  (draft-wu-idr-bgp-segment-allocation-ext)
This document describes extensions to the BGP for IDs allocation.
   The IDs are SIDs for segment routing (SR), including SR for IPv6
   (SRv6).  They are distributed to their domains if needed.

### BGP UPDATE for SD-WAN Edge Discovery  (draft-ietf-idr-sdwan-edge-discovery)
The document describes the BGP mechanisms for SD-WAN (Software
   Defined Wide Area Network) edge node attribute discovery.  These
   mechanisms include a new tunnel type and sub-TLVs for the BGP Tunnel-
   Encapsulation Attribute (RFC9012) and set of NLRI (network layer
   reachability information) for SD-WAN underlay information.

### BGP Flowspec for IETF Network Slice Traffic Steering  (draft-dong-idr-flowspec-network-slice-ts)
BGP Flow Specification (Flowspec) provides a mechanism to distribute
   traffic flow specifications and the forwarding actions to be
   performed to the specific traffic flows.  A set of Flowspec
   components are defined to specify the matching criteria that can be
   applied to the packet, and a set of BGP extended communities are
   defined to encode the actions a routing system can take on a packet
   which matches the flow specification.

   An IETF Network Slice enables connectivity between a set of Service
   Demarcation Points (SDPs) with specific Service Level Objectives
   (SLOs) and Service Level Expectations (SLEs) over a common underlay
   network.  To meet the connectivity and performance requirements of
   network slice services, network slice service traffic needs to be
   mapped to a corresponding Network Resource Partition (NRP).  The edge
   nodes of the NRP needs to identify the traffic flows which belong to
   a network slice and steer the matched traffic into the corresponding
   NRP, or a specific path within the corresponding NRP.

   BGP Flowspec can be used to distribute the matching criteria and the
   forwarding actions to be preformed on network slice service traffic.
   The existing Flowspec components can be reused for the matching of
   network slice services flows at the edge of an NRP.  New components
   and traffic action may need to be defined for steering network slice
   service flows into the corresponding NRP.  This document defines the
   extensions to BGP Flowspec for IETF network slice traffic steering
   (NS-TS).

### BGP Flow Specification Filter for MPLS Label  (draft-ietf-idr-flowspec-mpls-match)
This draft proposes BGP flow specification rules that are used to
   filter MPLS labeled packets.

### Carrying Label Information for BGP FlowSpec  (draft-ietf-idr-bgp-flowspec-label)
This document specifies a method in which the label mapping
   information for a particular FlowSpec rule is piggybacked in the same
   Border Gateway Protocol (BGP) Update message that is used to
   distribute the FlowSpec rule.  Based on the proposed method, the
   Label Switching Routers (LSRs) (except the ingress LSR) on the Label
   Switched Path (LSP) can use label to indentify the traffic matching a
   particular FlowSpec rule; this facilitates monitoring and traffic
   statistics for FlowSpec rules.

### Distribution of Link-State and Traffic Engineering Information Using BGP  (draft-ietf-idr-rfc7752bis)
In many environments, a component external to a network is called
   upon to perform computations based on the network topology and the
   current state of the connections within the network, including
   Traffic Engineering (TE) information.  This is information typically
   distributed by IGP routing protocols within the network.

   This document describes a mechanism by which link-state and TE
   information can be collected from networks and shared with external
   components using the BGP routing protocol.  This is achieved using a
   BGP Network Layer Reachability Information (NLRI) encoding format.
   The mechanism applies to physical and virtual (e.g., tunnel) IGP
   links.  The mechanism described is subject to policy control.

   Applications of this technique include Application-Layer Traffic
   Optimization (ALTO) servers and Path Computation Elements (PCEs).

   This document obsoletes RFC7752 by completely replacing that
   document.  It makes some small changes and clarifications to the
   previous specification.  This document also obsoletes RFC9029 by
   incorporating the updates that it made to RFC7752.

### Applying TCP User Timeout Parameter to BGP Sessions  (draft-chen-idr-tcp-user-timeout)
In this document we discuss the TCP "User Timeout" parameter and
   recommend using it to handle stuck BGP sessions.

### BGP-LS Advertisement of Segment Routing Service Segments  (draft-ietf-idr-bgp-ls-sr-service-segments)
Service functions are deployed as, physical or virtualized elements
   along with network nodes or on servers in data centers.  Segment
   Routing (SR) brings in the concept of segments which can be
   topological or service instructions.  Service segments are SR
   segments that are associated with service functions.  SR Policies are
   used for the setup of paths for steering of traffic through service
   functions using their service segments.

   BGP Link-State (BGP-LS) enables distribution of topology information
   from the network to a controller or an application in general so it
   can learn the network topology.  This document specifies the
   extensions to BGP-LS for the advertisement of service functions along
   their associated service segments.  The BGP-LS advertisement of
   service function information along with the network nodes that they
   are attached to, or associated with, enables controllers compute and
   setup service paths in the network.

### BGP MultiNexthop Attribute  (draft-kaliraj-idr-multinexthop-attribute)
Today, a BGP speaker can advertise one nexthop for a set of NLRIs in
   an Update.  This nexthop can be encoded in either the top-level BGP-
   Nexthop attribute (code 3), or inside the MP_REACH_NLRI attribute
   (code 14).

   This document defines a new optional non-transitive BGP attribute
   called "MultiNexthop (MNH)" with IANA BGP attribute type code TBD,
   that can be used to carry an ordered set of one or more Nexthops in
   the same route, with forwaring information scoped on a per nexthop
   basis.

### Segment Routing BGP Egress Peer Engineering over Layer 2 Bundle Members  (draft-lin-idr-sr-epe-over-l2bundle)
There are deployments where the Layer 3 interface on which a BGP
   peer session is established is a Layer 2 interface bundle. In order
   to allow BGP-EPE to control traffic flows on individual member links
   of the underlying Layer 2 bundle, BGP Peering SIDs need to be
   allocated to individual bundle member links, and advertisement of
   such BGP Peering SIDs in BGP-LS is required. This document describes
   how to support Segment Routing BGP Egress Peer Engineering over
   Layer 2 bundle members. This document updates [RFC9085] to allow the
   L2 Bundle Member Attributes TLV to be added to the BGP-LS Attribute
   associated with the Link NLRI of BGP peering link. This document
   updates [RFC9085] and [RFC9086] to allow the PeerAdj SID TLV to be
   included as a sub-TLV of the L2 Bundle Member Attributes TLV.

### BGP Extension for SR-MPLS Entropy Label Position  (draft-zhou-idr-bgp-srmpls-elp)
This document proposes extensions for BGP to indicate the entropy
   label position in the SR-MPLS label stack when delivering SR Policy
   via BGP.

### YANG Model for Border Gateway Protocol (BGP-4)  (draft-ietf-idr-bgp-model)
This document defines a YANG data model for configuring and managing
   BGP, including protocol, policy, and operational aspects, such as
   RIB, based on data center, carrier, and content provider operational
   requirements.

### Constrain Attribute announcement within BGP  (draft-ietf-idr-bgp-attribute-announcement)
[RFC4271] defines four different categories of BGP Path attributes.
   The different Path attribute categories can be identified by the
   attribute flag values.  These flags help identify if an attribute is
   optional or well-known, Transitive or non-Transitive, Partial, or of
   an Extended length type.  BGP attribute announcement depends on
   whether an attribute is a well-known or optional, and whether an
   attribute is a transitive or non-transitive.  BGP implementations
   MUST recognize all well-known attributes.  The well-known attributes
   are always Transitive.  It is not required for BGP implementations to
   recognise all the Optional attributes.  The Optional attributes could
   be Transitive or Non-Transitive.  BGP implementations MUST store and
   forward any Unknown Optional Transitive attributes and ignore and
   drop any Unknown Optional Non-Transitive attributes.

   Currently, there is no way to confine the scope of Path attributes
   within a given Autonomous System (AS) or a given BGP member-AS in
   Confederation.  This draft defines attribute extensions that help
   confine the scope of Optional attributes within a given AS or a given
   BGP member-AS in Confederation

### Link-Local Next Hop Capability for BGP  (draft-white-linklocal-capability)
BGP [RFC4271], was originally designed to provide reachability
   between domains and between the edges of a domain.  As such, BGP
   assumes the next hop towards any reachable destination may not reside
   on the advertising speaker, but rather may either be through a router
   connected to the same subnet as the speaker, or through a router only
   reachable by traversing multiple hops through the network.  Because
   of this, as per [RFC4291] - BGP does not recognize IPv6 link-local
   addresses, as a valid next hop for the forwarding purposes.

   This draft standardizes the operation of BGP over a point-to-point
   link using link-local IPv6 addressing only.

### YANG Data Model for BGP about RPKI  (draft-ietf-idr-bgp-rpki-yang)
This document defines YANG data models for configuring and managing
   BGP information about Resource Public Key Infrastructure (RPKI).

### Border Gateway Protocol - Link State (BGP-LS) Extensions for Segment Routing over IPv6 (SRv6)  (draft-ietf-idr-bgpls-srv6-ext)
Segment Routing over IPv6 (SRv6) allows for a flexible definition of end-to-end paths within various topologies by encoding paths as sequences of topological or functional sub-paths called "segments". These segments are advertised by various protocols such as BGP, IS-IS, and OSPFv3.

 This document defines extensions to BGP - Link State (BGP-LS) to advertise SRv6 segments along with their behaviors and other attributes via BGP. The BGP-LS address-family solution for SRv6 described in this document is similar to BGP-LS for SR for the MPLS data plane, which is defined in RFC 9085.

### BGP Dissemination of Flow Specification Rules for Tunneled Traffic  (draft-ietf-idr-flowspec-nvo3)
This draft specifies a Border Gateway Protocol (BGP) Network Layer
   Reachability Information (NLRI) encoding format for flow
   specifications (RFC 8955) that can match on a variety of tunneled
   traffic.  In addition, flow specification components are specified
   for certain tunneling header fields.

### Enhanced Route Refresh Implementation Report  (draft-ietf-idr-enhanced-refresh-impl)
This document provides an implementation report for Enhanced Route
   refresh as defined in draft-ietf-idr-bgp-enhanced-route-refresh.  The
   editor did not verify the accuracy of the information provided by
   respondents or by any alternative means.  The respondents are experts
   with the implementations they reported on, and their responses are
   considered authoritative for the implementations for which their
   responses represent.

### Deterministic Route Redistribution into BGP  (draft-chen-bgp-redist)
In this document we present several examples of non-deterministic
   routing behavior involving route redistribution into BGP.  To
   eliminate such non-deterministic behavior, we propose an enhancement
   to BGP route selection that would take into account the
   administrative distance under certain conditions.  Additionally, We
   recommend lowering the LOCAL_PREF value in implementation for the
   redistributed backup route when appropriate.

### BGP Flow Specification Version 2  (draft-ietf-idr-flowspec-v2)
BGP flow specification version 1 (FSv1), defined in RFC 8955, RFC
   8956, and RFC 9117 describes the distribution of traffic filter
   policy (traffic filters and actions) distributed via BGP.  Multiple
   applications have used BGP FSv1 to distribute traffic filter policy.
   These applications include the following: mitigation of denial of
   service (DoS), enabling traffic filtering in BGP/MPLS VPNs,
   centralized traffic control of router firewall functions, and SFC
   traffic insertion.

   During the deployment of BGP FSv1 a number of issues were detected
   due to lack of consistent TLV encoding for rules for flow
   specifications, lack of user ordering of filter rules and/or actions,
   and lack of clear definition of interaction with BGP peers not
   supporting FSv1.  Version 2 of the BGP flow specification (FSv2)
   protocol addresses these features.  In order to provide a clear
   demarcation between FSv1 and FSv2, a different NLRI encapsulates
   FSv2.

### IANA Registrations for the BGP Finite State Machine (FSM)  (draft-hhp-idr-bgp-fsm-iana)
The Border Gateway Protocol, version 4 (BGP-4) finite state machine
   (FSM) is defined in RFC 4271.  Over the years, various extensions to
   BGP have been authored that update the protocol's FSM.  Some elements
   of the FSM are enumerated.  Those elements are referred to across BGP
   extensions in their respective state machine changes, and may also be
   used for management purposes in things such as YANG [RFC7950].

   To provide consistent naming and enumeration of these FSM elements,
   this draft requests IANA to create and maintain registries for
   elements in the BGP FSM.

### IANA Registrations for the BGP Finite State Machine (FSM)  (draft-ietf-idr-bgp-fsm-iana)
The Border Gateway Protocol, version 4 (BGP-4) finite state machine
   (FSM) is defined in RFC 4271.  Over the years, various extensions to
   BGP have been authored that update the protocol's FSM.  Some elements
   of the FSM are enumerated.  Those elements are referred to across BGP
   extensions in their respective state machine changes, and may also be
   used for management purposes in things such as YANG (RFC 7950).

   To provide consistent naming and enumeration of these FSM elements,
   this document requests IANA to create and maintain registries for
   elements in the BGP FSM.

### Advertising Segment Routing Policies in BGP  (draft-ietf-idr-segment-routing-te-policy)
This document introduces a BGP SAFI with two NLRIs to advertise a
   candidate path of a Segment Routing (SR) Policy.  An SR Policy is an
   ordered list of segments (i.e., instructions) that represent a
   source-routed policy.  An SR Policy consists of one or more candidate
   paths, each consisting of one or more segment lists.  A headend may
   be provisioned with candidate paths for an SR Policy via several
   different mechanisms, e.g., CLI, NETCONF, PCEP, or BGP.  This
   document specifies how BGP may be used to distribute SR Policy
   candidate paths.  It defines sub-TLVs for the Tunnel Encapsulation
   Attribute for signaling information about these candidate paths.

   This documents updates RFC9012 with extensions to the Color Extended
   Community to support additional steering modes over SR Policy.

### Autonomous System (AS) Reservation for Private Use  (draft-ietf-idr-as-private-reservation)
This document describes the reservation of Autonomous System Numbers (ASNs) that are for Private Use only, known as Private Use ASNs, and provides operational guidance on their use.  This document enlarges the total space available for Private Use ASNs by documenting the reservation of a second, larger range and updates RFC 1930 by replacing Section 10 of that document.

### Dissemination of Flow Specification Rules for IPv6  (draft-ietf-idr-flow-spec-v6)
"Dissemination of Flow Specification Rules" (RFC 8955) provides a Border Gateway Protocol (BGP) extension for the propagation of traffic flow information for the purpose of rate limiting or filtering IPv4 protocol data packets.

 This document extends RFC 8955 with IPv6 functionality. It also updates RFC 8955 by changing the IANA Flow Spec Component Types registry.

### BGP SR Policy Extensions for Network Resource Partition  (draft-dong-idr-sr-policy-nrp)
Segment Routing (SR) Policy is a set of candidate paths, each
   consisting of one or more segment lists and the associated
   information.  The header of a packet steered in an SR Policy is
   augmented with an ordered list of segments associated with that SR
   Policy.  A Network Resource Partition (NRP) is a subset of network
   resources allocated in the underlay network which can be used to
   support one or a group of RFC XXXX network slice services.

   In networks where there are multiple NRPs, an SR Policy may be
   associated with a particular NRP.  The association between SR Policy
   and NRP needs to be specified, so that for service traffic which is
   steered into the SR Policy, the header of the packets can be
   augmented with the information associated with the NRP.  An SR Policy
   candidate path can be distributed using BGP SR Policy.  This document
   defines the extensions to BGP SR policy to specify the NRP which the
   SR Policy candidate path is associated with.

### Inbound BGP Maximum Prefix Limits  (draft-sas-idr-maxprefix-inbound)
This document describes two threshold types to consider when
   receiving BGP address prefixes from adjacent systems in order to
   limit the negative impact of route leaks or resource exhaustion in
   BGP implementations.

### BGP Colored Prefix Routing (CPR) for SRv6 based Services  (draft-wang-idr-cpr)
This document describes a mechanism to advertise IPv6 prefixes in BGP
   which are associated with Color Extended Communities to establish
   end-to-end intent-aware paths for SRv6 services.  Such IPv6 prefixes
   are called "Colored Prefixes", and this mechanism is called Colored
   Prefix Routing (CPR).  In SRv6 networks, the Colored prefixes are the
   SRv6 locators associated with different intent.  SRv6 services (e.g.
   SRv6 VPN services) with specific intent could be assigned with SRv6
   SIDs under the corresponding SRv6 locators, which are advertised as
   Colored prefixes.  This allows the SRv6 service traffic to be steered
   into end-to-end intent-aware paths simply based on the longest prefix
   matching of SRv6 Service SIDs to the Colored prefixes.  In data
   plane, dedicated transport label or SID for the inter-domain path is
   not needed, thus the encapsulation efficiency could be optimized.
   The existing IPv6 Address Family could be used for the advertisement
   of IPv6 Colored prefixes, thus this mechanism is easy to interoperate
   and can be deployed incrementally in multi-domain networks.

### Dissemination of Flow Specification Rules  (draft-ietf-idr-rfc5575bis)
This document defines a Border Gateway Protocol Network Layer Reachability Information (BGP NLRI) encoding format that can be used to distribute (intra-domain and inter-domain) traffic Flow Specifications for IPv4 unicast and IPv4 BGP/MPLS VPN services. This allows the routing system to propagate information regarding more specific components of the traffic aggregate defined by an IP destination prefix.

 It also specifies BGP Extended Community encoding formats, which can be used to propagate Traffic Filtering Actions along with the Flow Specification NLRI. Those Traffic Filtering Actions encode actions a routing system can take if the packet matches the Flow Specification.

 This document obsoletes both RFC 5575 and RFC 7674.

### Application of the Border Gateway Protocol in the Internet  (draft-ietf-iwg-bgpapplication)
This RFC, together with its companion RFC-1163, "A Border Gateway Protocol (BGP)", specify an inter-autonomous system routing protocol for the Internet. [STANDARDS-TRACK]

### Border Gateway Protocol (BGP)  (draft-ietf-iwg-bgp)
This RFC, together with its companion RFC-1164, "Application of the Border Gateway Protocol in the Internet", specify an inter-autonomous system routing protocol for the Internet. [STANDARDS-TRACK]

### Definitions of Managed Objects for the Border Gateway Protocol: Version 3  (draft-ietf-iwg-bgp-mib)
This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in TCP/IP-based internets.  In particular, it defines objects for managing the Border Gateway Protocol. [STANDARDS-TRACK]

### Border Gateway Protocol 3 (BGP-3)  (draft-ietf-bgp-bgp3)
This memo, together with its companion document, "Application of the Border Gateway Protocol in the Internet", define an inter-autonomous system routing protocol for the Internet. [STANDARDS-TRACK]

### Experience with the BGP Protocol  (draft-ietf-bgp-experience)
The purpose of this memo is to document how the requirements for advancing a routing protocol to Draft Standard have been satisfied by Border Gateway Protocol (BGP).  This memo provides information for the Internet community.  It does not specify an Internet standard.

### BGP Protocol Analysis  (draft-ietf-bgp-analysis)
This report summarizes the key feature of BGP, and analyzes the protocol with respect to scaling and performance.  This memo provides information for the Internet community.  It does not specify an Internet standard.

### Default Route Advertisement In BGP2 and BGP3 Version of The Border Gateway Protocol  (draft-ietf-bgp-defaultroute)
This document speficies the recommendation of the BGP Working Group on default route advertisement support in BGP2 [1] and BGP3 [2] versions of the Border Gateway Protocol. [STANDARDS-TRACK]

### Application of the Border Gateway Protocol in the Internet  (draft-ietf-bgp-usage)
This document describes the usage of the BGP in the Internet. [STANDARDS-TRACK]

### BGP OSPF Interaction  (draft-ietf-bgp-ospfinteract)
This memo defines the various criteria to be used when designing Autonomous System Border Routers (ASBR) that will be run BGP with other ASBRs external to the AS, and OSPF as its IGP.

### A Border Gateway Protocol 4 (BGP-4)  (draft-ietf-bgp-bgp4)
This document defines an inter-autonomous system routing protocol for the Internet. [STANDARDS-TRACK]

### Definitions of Managed Objects for the Fourth Version of the Border Gateway Protocol (BGP-4) using SMIv2  (draft-ietf-bgp-mibv4)
This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in the Internet community.  In particular, it describes managed objects used for managing the Border Gateway Protocol Version 4 or lower [1, 2]. [STANDARDS-TRACK]

### BGP4/IDRP for IP---OSPF Interaction  (draft-ietf-idr-bgp4ospf-interact)
This memo defines the various criteria to be used when designing an Autonomous System Border Router (ASBR) that will run either BGP4 or IDRP for IP with other ASBRs external to the AS and OSPF as its IGP. [STANDARDS-TRACK]

### Application of the Border Gateway Protocol in the Internet  (draft-ietf-bgp-application)
This document, together with its companion document, "A Border Gateway Protocol 4 (BGP-4)", define an inter-autonomous system routing protocol for the Internet. [STANDARDS-TRACK]

### BGP-4 Protocol Document Roadmap and Implementation Experience  (draft-ietf-bgp-bgp4-implement)
Border Gateway Protocol v4 (BGP-4) [1] is an inter-Autonomous System routing protocol.  It is built on experience gained with BGP as defined in RFC-1267 [2] and BGP usage in the connected Internet as described in RFC-1268 [3].  This memo provides information for the Internet community.  This memo does not specify an Internet standard of any kind.

### Guidelines for creation, selection, and registration of an Autonomous System (AS)  (draft-ietf-idr-autosys-guide)
This memo discusses when it is appropriate to register and utilize an Autonomous System (AS), and lists criteria for such.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Experience with the BGP-4 protocol  (draft-ietf-idr-bgp4-experience)
The purpose of this memo is to document how the requirements for advancing a routing protocol to Draft Standard have been satisfied by Border Gateway Protocol version 4 (BGP-4).  This report documents experience with BGP.  This memo provides information for the Internet community.  This memo does not specify an Internet standard of any kind.

### BGP-4 Protocol Analysis  (draft-ietf-idr-bgp4-analysis)
The purpose of this report is to document how the requirements for advancing a routing protocol to Draft Standard have been satisfied by the Border Gateway Protocol version 4 (BGP-4).  This report summarizes the key features of BGP, and analyzes the protocol with respect to scaling and performance.  This memo provides information for the Internet community.  This memo does not specify an Internet standard of any kind.

### A Border Gateway Protocol 4 (BGP-4)  (draft-ietf-idr-bgp4)
This document discusses the Border Gateway Protocol (BGP), which is an inter-Autonomous System routing protocol.

 The primary function of a BGP speaking system is to exchange network reachability information with other BGP systems. This network reachability information includes information on the list of Autonomous Systems (ASes) that reachability information traverses. This information is sufficient for constructing a graph of AS connectivity for this reachability from which routing loops may be pruned, and, at the AS level, some policy decisions may be enforced.

 BGP-4 provides a set of mechanisms for supporting Classless Inter-Domain Routing (CIDR). These mechanisms include support for advertising a set of destinations as an IP prefix, and eliminating the concept of network "class" within BGP. BGP-4 also introduces mechanisms that allow aggregation of routes, including aggregation of AS paths.

 This document obsoletes RFC 1771. [STANDARDS-TRACK]

### A BGP/IDRP Route Server alternative to a full mesh routing  (draft-haskin-bgp-idrp-mesh-routing)
This document describes the use and detailed design of Route Servers for dissemination of routing information among BGP/IDRP speaking routers.  This memo defines an Experimental Protocol for the Internet community.

### BGP Communities Attribute  (draft-ietf-idr-communities)
This document describes an extension to BGP which may be used to pass additional information to both neighboring and remote BGP peers. [STANDARDS-TRACK]

### Application of the BGP Destination Preference Attribute in Implementing Symmetric Routing  (draft-ietf-idr-dpa-application)
This paper presents applications of the proposed Destination Preference Attribute (DPA) for BGP.  It shows how the DPA attribute can aid in the implementation of symmetric inter-domain routing in the multi-provider Internet.

### Current Practice of Implementing Symmetric Routing and Load Sharing in the Multi-Provider Internet  (draft-ietf-idr-symm-multi-prov)
In the current multi-provider Internet, it is common for an entity to have multiple service providers. Symmetric routing becomes increasingly important for various reasons.  This memo documents and analyzes the current practice in implementing symmetric inter-domain routing using BGP for several representative topologies of Internet connections.

### Operational Experience with the BGP-4 protocol  (draft-ietf-idr-bgp4-op-experience)
The purpose of this memo is to document how the requirements for advancing a routing protocol to Full Standard have been satisfied by Border Gateway Protocol version 4 (BGP-4).  This report documents experience with BGP.  It is the second of two reports on the BGP protocol.                       The remaining sections of this memo document how BGP satisfies General Requirements specified in Section 3.0, as well as the Requirements for Full Standard as specified in Section 6.0 of the 'Internet Routing Protocol Standardization Criteria' document [1].                           Please send comments to bgp@ans.net.

### Definitions of Managed Objects for BGP-4  (draft-ietf-idr-bgp4-mib)
This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in the Internet community In particular, it describes managed objects used for managing the Border Gateway Protocol Version 4 or lower.

 The origin of this memo is from RFC 1269 "Definitions of Managed Objects for the Border Gateway Protocol (Version 3)", which was updated to support BGP-4 in RFC 1657. This memo fixes errors introduced when the MIB module was converted to use the SMIv2 language. This memo also updates references to the current SNMP framework documents.

 This memo is intended to document deployed implementations of this MIB module in a historical context, to provide clarifications of some items, and to note errors where the MIB module fails to fully represent the BGP protocol. Work is currently in progress to replace this MIB module with a new one representing the current state of the BGP protocol and its extensions.

 This document obsoletes RFC 1269 and RFC 1657. [STANDARDS-TRACK]

### An Application of the BGP Community Attribute in Multi-home Routing  (draft-ietf-idr-community-usage)
This document presents an application of the BGP community attribute [2] in simplifying the implementation and configuration of routing policies in the multi-provider Internet.  This memo provides information for the Internet community.  This memo does not specify an Internet standard of any kind.

### BGP Route Reflection An alternative to full mesh IBGP  (draft-ietf-idr-route-reflect)
This document describes the use and design of a method known as "Route Reflection" to alleviate the the need for "full mesh" IBGP.  This memo defines an Experimental Protocol for the Internet community.

### Autonomous System Confederations for BGP  (draft-ietf-idr-bgp-confed)
This document describes an extension to BGP which may be used to create a confederation of autonomous systems which is represented as one single autonomous system to BGP peers external to the confederation.  This memo defines an Experimental Protocol for the Internet community.

### A Framework for Inter-Domain Route Aggregation  (draft-ietf-idr-aggregation-framework)
This document presents a framework for inter-domain route aggregation and shows an example router configuration which 'implements' this framework.  This memo provides information for the Internet community

### Using a Dedicated AS for Sites  Homed to a Single Provider  (draft-ietf-idr-as-dedicated)
With the increased growth of the Internet, the number of customers using BGP4 has grown significantly.  RFC1930 outlines a set of guidelines for when one needs and should use an AS.  However, the customer and service provider (ISP) are left with a problem as a result of this in that while there is no need for an allocated AS under the guidelines, certain conditions make the use of BGP4 a very pragmatic and perhaps only way to connect a customer homed to a single ISP.  This paper proposes a solution to this problem in line with recommendations set forth in RFC1930.  This memo provides information for the Internet community.  It does not specify an Internet standard of any kind.

## Working Group: ipsecme
### Internet Key Exchange Protocol Version 2 (IKEv2) Configuration for Encrypted DNS  (draft-ietf-ipsecme-add-ike)
This document specifies new Internet Key Exchange Protocol Version 2 (IKEv2) Configuration Payload Attribute Types to assign DNS resolvers that support encrypted DNS protocols, such as DNS over HTTPS (DoH), DNS over TLS (DoT), and DNS over QUIC (DoQ).

### Deprecation of the Internet Key Exchange Version 1 (IKEv1) Protocol and Obsoleted Algorithms  (draft-ietf-ipsecme-ikev1-algo-to-historic)
Internet Key Exchange Version 1 (IKEv1) has been deprecated, and RFCs 2407, 2408, and 2409 have been moved to Historic status.  This document updates RFCs 8221 and 8247 to reflect the usage guidelines of old algorithms that are associated with IKEv1 and are not specified or commonly implemented for IKEv2.  This document further updates the IANA registries for IKEv2 "Transform Type Values" by adding a "Status" column where the deprecation status can be listed.

### Multiple Key Exchanges in the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2-multiple-ke)
This document describes how to extend the Internet Key Exchange Protocol Version 2 (IKEv2) to allow multiple key exchanges to take place while computing a shared secret during a Security Association (SA) setup.

 This document utilizes the IKE_INTERMEDIATE exchange, where multiple key exchanges are performed when an IKE SA is being established. It also introduces a new IKEv2 exchange, IKE_FOLLOWUP_KE, which is used for the same purpose when the IKE SA is being rekeyed or is creating additional Child SAs.

 This document updates RFC 7296 by renaming a Transform Type 4 from "Diffie-Hellman Group (D-H)" to "Key Exchange Method (KE)" and renaming a field in the Key Exchange Payload from "Diffie-Hellman Group Num" to "Key Exchange Method". It also renames an IANA registry for this Transform Type from "Transform Type 4 - Diffie- Hellman Group Transform IDs" to "Transform Type 4 - Key Exchange Method Transform IDs". These changes generalize key exchange algorithms that can be used in IKEv2.

### ESP Header Compression Profile  (draft-mglt-ipsecme-diet-esp)
ESP Header Compression Profile (EHCP) defines a profile to compress
   communications protected with IPsec/ESP.

### Internet Key Exchange version 2 (IKEv2) extension for the ESP Header Compression (EHC)  (draft-mglt-ipsecme-ikev2-diet-esp-extension)
This document describes an IKEv2 extension of for the ESP Header
   Compression (EHC) to agree on a specific ESP Header Compression (EHC)
   Context.

### Separate Transports for IKE and ESP  (draft-smyslov-ipsecme-ikev2-reliable-transport)
The Internet Key Exchange protocol version 2 (IKEv2) can operate
   either over unreliable (UDP) transport or over reliable (TCP)
   transport.  If TCP is used, then IPsec tunnels created by IKEv2 also
   use TCP.  This document specifies how to decouple IKEv2 and IPsec
   transports so that IKEv2 can operate over TCP, while IPsec tunnels
   use unreliable transport.  This feature allows IKEv2 to effectively
   exchange large blobs of data (e.g., when post-quantum algorithms are
   employed) while avoiding performance problems that arise when IPsec
   uses TCP.

### IKEv2 negotiation for Bound End-to-End Tunnel (BEET) mode ESP  (draft-antony-ipsecme-iekv2-beet-mode)
This document specifies a new Notify Message Type Payload for the
   Internet Key Exchange Protocol Version 2 (IKEv2), to negotiate IPsec
   ESP Bound End-to-End Tunnel (BEET) mode.  BEET mode combines the
   benefits of tunnel mode with reduced overhead, making it suitable for
   applications requiring minimalistic end-to-end tunnels, mobility
   support, and multi-address multi-homing capabilities.  The
   introduction of the USE_BEET_MODE Notify Message enables the
   negotiation and establishment of BEET mode security associations.

### More Raw Public Keys for IKEv2  (draft-ietf-ipsecme-oob-pubkey)
The Internet Key Exchange Version 2 (IKEv2) protocol currently only
   supports raw RSA keys.  In some environments it is useful to make use
   of other types of public keys, such as those based on Elliptic Curve
   Cryptography.  This documents adds support for other types of raw
   public keys to IKEv2 and obsoletes the old raw RSA key format.

### An Extension for EAP-Only Authentication in IKEv2  (draft-ietf-ipsecme-eap-mutual)
IKEv2 specifies that Extensible Authentication Protocol (EAP) authentication must be used together with responder authentication based on public key signatures. This is necessary with old EAP methods that provide only unilateral authentication using, e.g., one- time passwords or token cards.

 This document specifies how EAP methods that provide mutual authentication and key agreement can be used to provide extensible responder authentication for IKEv2 based on methods other than public key signatures. [STANDARDS-TRACK]

### Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2bis)
This document describes version 2 of the Internet Key Exchange (IKE) protocol.  IKE is a component of IPsec used for performing mutual authentication and establishing and maintaining Security Associations (SAs).  This document replaces and updates RFC 4306, and includes all of the clarifications from RFC 4718. [STANDARDS-TRACK]

### IPv6 Configuration in Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2-ipv6-config)
When Internet Key Exchange Protocol version 2 (IKEv2) is used for remote VPN access (client to VPN gateway), the gateway assigns the client an IP address from the internal network using IKEv2 configuration payloads.  The configuration payloads specified in RFC 4306 work well for IPv4 but make it difficult to use certain features of IPv6.  This document specifies new configuration attributes for IKEv2 that allows the VPN gateway to assign IPv6 prefixes to clients, enabling all features of IPv6 to be used with the client-gateway "virtual link".  This document defines an Experimental Protocol for the Internet community.

### Wrapped Encapsulating Security Payload (ESP) for Traffic Visibility  (draft-ietf-ipsecme-traffic-visibility)
This document describes the Wrapped Encapsulating Security Payload (WESP) protocol, which builds on the Encapsulating Security Payload (ESP) RFC 4303 and is designed to allow intermediate devices to (1) ascertain if data confidentiality is being employed within ESP, and if not, (2) inspect the IPsec packets for network monitoring and access control functions.  Currently, in the IPsec ESP standard, there is no deterministic way to differentiate between encrypted and unencrypted payloads by simply examining a packet.  This poses certain challenges to the intermediate devices that need to deep inspect the packet before making a decision on what should be done with that packet (Inspect and/or Allow/Drop).  The mechanism described in this document can be used to easily disambiguate integrity-only ESP from ESP-encrypted packets, without compromising on the security provided by ESP. [STANDARDS-TRACK]

### Redirect Mechanism for the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2-redirect)
The Internet Key Exchange Protocol version 2 (IKEv2) is a protocol for setting up Virtual Private Network (VPN) tunnels from a remote location to a gateway so that the VPN client can access services in the network behind the gateway.  This document defines an IKEv2 extension that allows an overloaded VPN gateway or a VPN gateway that is being shut down for maintenance to redirect the VPN client to attach to another gateway.  The proposed mechanism can also be used in Mobile IPv6 to enable the home agent to redirect the mobile node to another home agent. [STANDARDS-TRACK]

### Internet Key Exchange Protocol Version 2 (IKEv2) Session Resumption  (draft-ietf-ipsecme-ikev2-resumption)
The Internet Key Exchange version 2 (IKEv2) protocol has a certain computational and communication overhead with respect to the number of round trips required and the cryptographic operations involved. In remote access situations, the Extensible Authentication Protocol (EAP) is used for authentication, which adds several more round trips and consequently latency.

 To re-establish security associations (SAs) upon a failure recovery condition is time consuming especially when an IPsec peer (such as a VPN gateway) needs to re-establish a large number of SAs with various endpoints. A high number of concurrent sessions might cause additional problems for an IPsec peer during SA re-establishment.

 In order to avoid the need to re-run the key exchange protocol from scratch, it would be useful to provide an efficient way to resume an IKE/IPsec session. This document proposes an extension to IKEv2 that allows a client to re-establish an IKE SA with a gateway in a highly efficient manner, utilizing a previously established IKE SA.

 A client can reconnect to a gateway from which it was disconnected. The proposed approach encodes partial IKE state into an opaque ticket, which can be stored on the client or in a centralized store, and is later made available to the IKEv2 responder for re-authentication. We use the term ticket to refer to the opaque data that is created by the IKEv2 responder. This document does not specify the format of the ticket but examples are provided. [STANDARDS-TRACK]

### Cryptographic Algorithm Implementation Requirements and Usage Guidance for Encapsulating Security Payload (ESP) and Authentication Header (AH)  (draft-ietf-ipsecme-esp-ah-reqts)
This document updates the Cryptographic Algorithm Implementation Requirements for the Encapsulating Security Payload (ESP) and Authentication Header (AH). It also adds usage guidance to help in the selection of these algorithms.

 ESP and AH protocols make use of various cryptographic algorithms to provide confidentiality and/or data origin authentication to protected data communications in the IP Security (IPsec) architecture. To ensure interoperability between disparate implementations, the IPsec standard specifies a set of mandatory-to- implement algorithms. This document specifies the current set of mandatory-to-implement algorithms for ESP and AH, specifies algorithms that should be implemented because they may be promoted to mandatory at some future time, and also recommends against the implementation of some obsolete algorithms. Usage guidance is also provided to help the user of ESP and AH best achieve their security goals through appropriate choices of cryptographic algorithms.

### IP Security (IPsec) and Internet Key Exchange (IKE) Document Roadmap  (draft-ietf-ipsecme-roadmap)
Over the past few years, the number of RFCs that define and use IPsec and Internet Key Exchange (IKE) has greatly proliferated. This is complicated by the fact that these RFCs originate from numerous IETF working groups: the original IPsec WG, its various spin-offs, and other WGs that use IPsec and/or IKE to protect their protocols' traffic.

 This document is a snapshot of IPsec- and IKE-related RFCs. It includes a brief description of each RFC, along with background information explaining the motivation and context of IPsec's outgrowths and extensions. It obsoletes RFC 2411, the previous "IP Security Document Roadmap."

 The obsoleted IPsec roadmap (RFC 2411) briefly described the interrelationship of the various classes of base IPsec documents. The major focus of RFC 2411 was to specify the recommended contents of documents specifying additional encryption and authentication algorithms. This document is not an Internet Standards Track specification; it is published for informational purposes.

### Heuristics for Detecting ESP-NULL Packets  (draft-ietf-ipsecme-esp-null-heuristics)
This document describes a set of heuristics for distinguishing IPsec ESP-NULL (Encapsulating Security Payload without encryption) packets from encrypted ESP packets.  These heuristics can be used on intermediate devices, like traffic analyzers, and deep-inspection engines, to quickly decide whether or not a given packet flow is encrypted, i.e., whether or not it can be inspected.  Use of these heuristics does not require any changes made on existing IPsec hosts that are compliant with RFC 4303.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Using Advanced Encryption Standard Counter Mode (AES-CTR) with the Internet Key Exchange version 02 (IKEv2) Protocol  (draft-ietf-ipsecme-aes-ctr-ikev2)
This document describes the usage of Advanced Encryption Standard Counter Mode (AES-CTR), with an explicit Initialization Vector, by the Internet Key Exchange version 2 (IKEv2) protocol, for encrypting the IKEv2 exchanges that follow the IKE_SA_INIT exchange.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### IPsec Cluster Problem Statement  (draft-ietf-ipsecme-ipsec-ha)
This document defines the terminology, problem statement, and requirements for implementing Internet Key Exchange (IKE) and IPsec on clusters.  It also describes gaps in existing standards and their implementation that need to be filled in order to allow peers to interoperate with clusters from different vendors.  Agreed upon terminology, problem statement, and requirements will allow IETF working groups to consider development of IPsec/IKEv2 mechanisms to simplify cluster implementations.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Group Key Management using IKEv2  (draft-yeung-g-ikev2)
This document presents a set of IKEv2 exchanges that comprise a group
   key management protocol.  The protocol is in conformance with the
   Multicast Security (MSEC) key management architecture, which contains
   two components: member registration and group rekeying.  Both
   components require a Group Controller/Key Server to download IPsec
   group security associations to authorized members of a group.  The
   group members then exchange IP multicast or other group traffic as
   IPsec packets.  This document obsoletes RFC 6407.

### A Quick Crash Detection Method for the Internet Key Exchange Protocol (IKE)  (draft-ietf-ipsecme-failure-detection)
This document describes an extension to the Internet Key Exchange Protocol version 2 (IKEv2) that allows for faster detection of Security Association (SA) desynchronization using a saved token.

 When an IPsec tunnel between two IKEv2 peers is disconnected due to a restart of one peer, it can take as much as several minutes for the other peer to discover that the reboot has occurred, thus delaying recovery. In this text, we propose an extension to the protocol that allows for recovery immediately following the restart. [STANDARDS-TRACK]

### Protocol Support for High Availability of IKEv2/IPsec  (draft-ietf-ipsecme-ipsecha-protocol)
The IPsec protocol suite is widely used for business-critical network traffic. In order to make IPsec deployments highly available, more scalable, and failure-resistant, they are often implemented as IPsec High Availability (HA) clusters. However, there are many issues in IPsec HA clustering, and in particular in Internet Key Exchange Protocol version 2 (IKEv2) clustering. An earlier document, "IPsec Cluster Problem Statement", enumerates the issues encountered in the IKEv2/IPsec HA cluster environment. This document resolves these issues with the least possible change to the protocol.

 This document defines an extension to the IKEv2 protocol to solve the main issues of "IPsec Cluster Problem Statement" in the commonly deployed hot standby cluster, and provides implementation advice for other issues. The main issues solved are the synchronization of IKEv2 Message ID counters, and of IPsec replay counters. [STANDARDS-TRACK]

### Auto Discovery VPN Problem Statement and Requirements  (draft-ietf-ipsecme-p2p-vpn-problem)
This document describes the problem of enabling a large number of
   systems to communicate directly using IPsec to protect the traffic
   between them.  It them expands on the requirements, for such a
   solution.

   Manual configuration of all possible tunnels is too cumbersome in
   many such cases.  In other cases the IP address of end points change
   or the end points may be behind NAT gateways, making static
   configuration impossible.  The Auto Discovery VPN solution is
   chartered to address these requirements.

### Signature Authentication in the Internet Key Exchange Version 2 (IKEv2)  (draft-kivinen-ipsecme-signature-auth)
The Internet Key Exchange Version 2 (IKEv2) protocol has limited support for the Elliptic Curve Digital Signature Algorithm (ECDSA).  The current version only includes support for three Elliptic Curve groups, and there is a fixed hash algorithm tied to each group.  This document generalizes IKEv2 signature support to allow any signature method supported by PKIX and also adds signature hash algorithm negotiation.  This is a generic mechanism and is not limited to ECDSA; it can also be used with other signature algorithms.

### Internet Key Exchange Protocol Version 2 (IKEv2) Message Fragmentation  (draft-ietf-ipsecme-ikev2-fragmentation)
This document describes a way to avoid IP fragmentation of large Internet Key Exchange Protocol version 2 (IKEv2) messages.  This allows IKEv2 messages to traverse network devices that do not allow IP fragments to pass through.

### Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-kivinen-ipsecme-ikev2-rfc5996bis)
This document describes version 2 of the Internet Key Exchange (IKE) protocol.  IKE is a component of IPsec used for performing mutual authentication and establishing and maintaining Security Associations (SAs).  This document obsoletes RFC 5996, and includes all of the errata for it.  It advances IKEv2 to be an Internet Standard.

### Auto-Discovery VPN Problem Statement and Requirements  (draft-ietf-ipsecme-ad-vpn-problem)
This document describes the problem of enabling a large number of systems to communicate directly using IPsec to protect the traffic between them. It then expands on the requirements for such a solution.

 Manual configuration of all possible tunnels is too cumbersome in many such cases. In other cases, the IP addresses of endpoints change, or the endpoints may be behind NAT gateways, making static configuration impossible. The Auto-Discovery VPN solution will address these requirements.

### Additional Diffie-Hellman Tests for the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-dh-checks)
This document adds a small number of mandatory tests required for the secure operation of the Internet Key Exchange Protocol version 2 (IKEv2) with elliptic curve groups.  No change is required to IKE implementations that use modular exponential groups, other than a few rarely used so-called Digital Signature Algorithm (DSA) groups.  This document updates the IKEv2 protocol, RFC 5996.

### The NULL Authentication Method in the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2-null-auth)
This document specifies the NULL Authentication method and the ID_NULL Identification Payload ID Type for Internet Key Exchange Protocol version 2 (IKEv2).  This allows two IKE peers to establish single-side authenticated or mutual unauthenticated IKE sessions for those use cases where a peer is unwilling or unable to authenticate or identify itself.  This ensures IKEv2 can be used for Opportunistic Security (also known as Opportunistic Encryption) to defend against Pervasive Monitoring attacks without the need to sacrifice anonymity.

### Protecting Internet Key Exchange Protocol Version 2 (IKEv2) Implementations from Distributed Denial-of-Service Attacks  (draft-ietf-ipsecme-ddos-protection)
This document recommends implementation and configuration best practices for Internet Key Exchange Protocol version 2 (IKEv2) Responders, to allow them to resist Denial-of-Service and Distributed Denial-of-Service attacks.  Additionally, the document introduces a new mechanism called "Client Puzzles" that helps accomplish this task.

### ChaCha20, Poly1305, and Their Use in the Internet Key Exchange Protocol (IKE) and IPsec  (draft-ietf-ipsecme-chacha20-poly1305)
This document describes the use of the ChaCha20 stream cipher along with the Poly1305 authenticator, combined into an AEAD algorithm for the Internet Key Exchange Protocol version 2 (IKEv2) and for IPsec.

### Algorithm Implementation Requirements and Usage Guidance for the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-rfc4307bis)
The IPsec series of protocols makes use of various cryptographic algorithms in order to provide security services.  The Internet Key Exchange (IKE) protocol is used to negotiate the IPsec Security Association (IPsec SA) parameters, such as which algorithms should be used.  To ensure interoperability between different implementations, it is necessary to specify a set of algorithm implementation requirements and usage guidance to ensure that there is at least one algorithm that all implementations support.  This document updates RFC 7296 and obsoletes RFC 4307 in defining the current algorithm implementation requirements and usage guidance for IKEv2, and does minor cleaning up of the IKEv2 IANA registry.  This document does not update the algorithms used for packet encryption using IPsec Encapsulating Security Payload (ESP).

### Curve25519 and Curve448 for the Internet Key Exchange Protocol Version 2 (IKEv2) Key Agreement  (draft-ietf-ipsecme-safecurves)
This document describes the use of Curve25519 and Curve448 for ephemeral key exchange in the Internet Key Exchange Protocol Version 2 (IKEv2).

### TCP Encapsulation of IKEv2 and IPSec Packets  (draft-pauly-ipsecme-tcp-encaps)
This document describes a method to transport IKEv2 and IPSec packets
   over a TCP connection for traversing network middleboxes that may
   block IKEv2 negotiation over UDP.  This method, referred to as TCP
   encapsulation, involves sending all packets for tunnel establishment
   as well as tunneled packets over a TCP connection.  This method is
   intended to be used as a fallback option when IKE cannot be
   negotiated over UDP.

### Postquantum Preshared Keys for IKEv2  (draft-fluhrer-qr-ikev2)
The possibility of quantum computers pose a serious challenge to
   cryptography algorithms widely today.  IKEv2 is one example of a
   cryptosystem that could be broken; someone storing VPN communications
   today could decrypt them at a later time when a quantum computer is
   available.  It is anticipated that IKEv2 will be extended to support
   quantum secure key exchange algorithms; however that is not likely to
   happen in the near term.  To address this problem before then, this
   document describes an extension of IKEv2 to allow it to be resistant
   to a Quantum Computer, by using preshared keys.

### Split DNS Configuration for IKEv2  (draft-pauly-ipsecme-split-dns)
This document defines two Configuration Payload Attribute Types for
   the IKEv2 protocol that add support for private DNS domains.  These
   domains should be resolved using DNS servers reachable through an
   IPsec connection, while leaving all other DNS resolution unchanged.
   This approach of resolving a subset of domains using non-public DNS
   servers is referred to as "Split DNS".

### Cryptographic Algorithm Implementation Requirements and Usage Guidance for Encapsulating Security Payload (ESP) and Authentication Header (AH)  (draft-mglt-ipsecme-rfc7321bis)
This document updates the Cryptographic Algorithm Implementation
   Requirements for ESP and AH.  The goal of these document is to enable
   ESP and AH to benefit from cryptography that is up to date while
   making IPsec interoperable.

   This document obsoletes RFC 7321 on the cryptographic recommendations
   only.

### Using Edwards-curve Digital Signature Algorithm (EdDSA) in the Internet Key Exchange (IKEv2)  (draft-nir-ipsecme-eddsa)
This document describes the use of the Edwards-curve digital
   signature algorithm in the IKEv2 protocol.

### Implicit IV for Counter-based Ciphers in IPsec  (draft-mglt-ipsecme-implicit-iv)
IPsec ESP sends an initialization vector (IV) or nonce in each
   packet, adding 8 or 16 octets.  Some algorithms such as AES-GCM, AES-
   CCM, AES-CTR and ChaCha20-Poly1305 require a unique nonce but do not
   require an unpredictable nonce.  When using such algorithms the
   packet counter value can be used to generate a nonce, saving 8 octets
   per packet.  This document describes how to do this.

### TCP Encapsulation of IKE and IPsec Packets  (draft-ietf-ipsecme-tcp-encaps)
This document describes a method to transport Internet Key Exchange Protocol (IKE) and IPsec packets over a TCP connection for traversing network middleboxes that may block IKE negotiation over UDP.  This method, referred to as "TCP encapsulation", involves sending both IKE packets for Security Association establishment and Encapsulating Security Payload (ESP) packets over a TCP connection.  This method is intended to be used as a fallback option when IKE cannot be negotiated over UDP.

### Cryptographic Algorithm Implementation Requirements and Usage Guidance for Encapsulating Security Payload (ESP) and Authentication Header (AH)  (draft-ietf-ipsecme-rfc7321bis)
This document replaces RFC 7321, "Cryptographic Algorithm Implementation Requirements and Usage Guidance for Encapsulating Security Payload (ESP) and Authentication Header (AH)".  The goal of this document is to enable ESP and AH to benefit from cryptography that is up to date while making IPsec interoperable.

### Using the Edwards-Curve Digital Signature Algorithm (EdDSA) in the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-eddsa)
This document describes the use of the Edwards-curve Digital Signature Algorithm (EdDSA) in the Internet Key Exchange Protocol Version 2 (IKEv2).

### Split DNS Configuration for the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-split-dns)
This document defines two Configuration Payload Attribute Types (INTERNAL_DNS_DOMAIN and INTERNAL_DNSSEC_TA) for the Internet Key Exchange Protocol version 2 (IKEv2).  These payloads add support for private (internal-only) DNS domains.  These domains are intended to be resolved using non-public DNS servers that are only reachable through the IPsec connection.  DNS resolution for other domains remains unchanged.  These Configuration Payloads only apply to split- tunnel configurations.

### Framework to Integrate Post-quantum Key Exchanges into Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-tjhai-ipsecme-hybrid-qske-ikev2)
This document describes how to extend Internet Key Exchange Protocol
   Version 2 (IKEv2) so that the shared secret exchanged between peers
   has resistance against quantum computer attacks.  The basic idea is
   to exchange one or more post-quantum key exchange payloads in
   conjunction with the existing (Elliptic Curve) Diffie-Hellman
   payload.

### IKEv2 Notification Codes for IPv4/IPv6 Coexistence  (draft-boucadair-ipsecme-ipv6-ipv4-codes)
This document specifies new IKEv2 notification codes to better manage
   IPv4 and IPv6 co-existence.

### Intermediate Exchange in the Internet Key Exchange Protocol Version 2 (IKEv2)  (draft-ietf-ipsecme-ikev2-intermediate)
This document defines a new exchange, called "Intermediate Exchange", for the Internet Key Exchange Protocol Version 2 (IKEv2).  This exchange can be used for transferring large amounts of data in the process of IKEv2 Security Association (SA) establishment.  An example of the need to do this is using key exchange methods resistant to Quantum Computers (QCs) for IKE SA establishment.  The Intermediate Exchange makes it possible to use the existing IKE fragmentation mechanism (which cannot be used in the initial IKEv2 exchange), helping to avoid IP fragmentation of large IKE messages if they need to be sent before IKEv2 SA is established.

### Mixing Preshared Keys in the Internet Key Exchange Protocol Version 2 (IKEv2) for Post-quantum Security  (draft-ietf-ipsecme-qr-ikev2)
The possibility of quantum computers poses a serious challenge to cryptographic algorithms deployed widely today.  The Internet Key Exchange Protocol Version 2 (IKEv2) is one example of a cryptosystem that could be broken; someone storing VPN communications today could decrypt them at a later time when a quantum computer is available.  It is anticipated that IKEv2 will be extended to support quantum-secure key exchange algorithms; however, that is not likely to happen in the near term.  To address this problem before then, this document describes an extension of IKEv2 to allow it to be resistant to a quantum computer by using preshared keys.

### Implicit Initialization Vector (IV) for Counter-Based Ciphers in Encapsulating Security Payload (ESP)  (draft-ietf-ipsecme-implicit-iv)
Encapsulating Security Payload (ESP) sends an initialization vector (IV) in each packet.  The size of the IV depends on the applied transform and is usually 8 or 16 octets for the transforms defined at the time this document was written.  When used with IPsec, some algorithms, such as AES-GCM, AES-CCM, and ChaCha20-Poly1305, take the IV to generate a nonce that is used as an input parameter for encrypting and decrypting.  This IV must be unique but can be predictable.  As a result, the value provided in the ESP Sequence Number (SN) can be used instead to generate the nonce.  This avoids sending the IV itself and saves 8 octets per packet in the case of AES-GCM, AES-CCM, and ChaCha20-Poly1305.  This document describes how to do this.

### Intermediate Exchange in the IKEv2 Protocol  (draft-smyslov-ipsecme-ikev2-aux)
This documents defines a new exchange, called Intermediate Exchange,
   for the Internet Key Exchange protocol Version 2 (IKEv2).  This
   exchange can be used for transferring large amount of data in the
   process of IKEv2 Security Association (SA) establishment.
   Introducing Intermediate Exchange allows re-using existing IKE
   Fragmentation mechanism, that helps to avoid IP fragmentation of
   large IKE messages, but cannot be used in the initial IKEv2 exchange.

### IP Traffic Flow Security  (draft-hopps-ipsecme-iptfs)
This document describes a mechanism to enhance IPsec traffic flow
   security by adding traffic flow confidentiality to encrypted IP
   encapsulated traffic.  Traffic flow confidentiality is provided by
   obscuring the size and frequency of IP traffic using a fixed-sized,
   constant-send-rate IPsec tunnel.  The solution allows for congestion
   control as well.

### Internet Key Exchange Protocol Version 2 (IKEv2) Notification Status Types for IPv4/IPv6 Coexistence  (draft-ietf-ipsecme-ipv6-ipv4-codes)
This document specifies new Internet Key Exchange Protocol Version 2 (IKEv2) notification status types to better manage IPv4 and IPv6 coexistence by allowing the responder to signal to the initiator which address families are allowed.

 This document updates RFC 7296.

### IKEv2 Optional SA&TS Payloads in Child Exchange  (draft-kampati-ipsecme-ikev2-sa-ts-payloads-opt)
This document describes a method for reducing the size of the
   Internet Key Exchange version 2 (IKEv2) CREATE_CHILD_SA exchanges
   used for rekeying of the IKE or Child SA by replacing the SA and TS
   payloads with a Notify Message payload.  Reducing size and complexity
   of IKEv2 exchanges is especially useful for low power consumption
   battery powered devices.

### Deprecation of IKEv1 and obsoleted algorithms  (draft-pwouters-ikev1-ipsec-graveyard)
Internet Key Exchange version 1 (IKEv1) is deprecated.  Accordingly,
   IKEv1 has been moved to Historic status.  A number of old algorithms
   that are associated with IKEv1, and not widely implemented for IKEv2
   are deprecated as well.  IANA is instructed to close all IKEv1
   registries.

### Aggregation and Fragmentation Mode for Encapsulating Security Payload (ESP) and Its Use for IP Traffic Flow Security (IP-TFS)  (draft-ietf-ipsecme-iptfs)
This document describes a mechanism for aggregation and fragmentation of IP packets when they are being encapsulated in Encapsulating Security Payload (ESP).  This new payload type can be used for various purposes, such as decreasing encapsulation overhead for small IP packets; however, the focus in this document is to enhance IP Traffic Flow Security (IP-TFS) by adding Traffic Flow Confidentiality (TFC) to encrypted IP-encapsulated traffic.  TFC is provided by obscuring the size and frequency of IP traffic using a fixed-size, constant-send-rate IPsec tunnel.  The solution allows for congestion control, as well as nonconstant send-rate usage.

### Announcing Supported Authentication Methods in IKEv2  (draft-smyslov-ipsecme-ikev2-auth-announce)
This specification defines a mechanism that allows the Internet Key
   Exchange version 2 (IKEv2) implementations to indicate the list of
   supported authentication methods to their peers while establishing
   IKEv2 Security Association (SA).  This mechanism improves
   interoperability when IKEv2 partners are configured with multiple
   different credentials to authenticate each other.

### Internet Key Exchange Protocol Version 2 (IKEv2) Configuration for Encrypted DNS  (draft-btw-add-ipsecme-ike)
This document specifies a new Internet Key Exchange Protocol Version
   2 (IKEv2) Configuration Payload Attribute Types for encrypted DNS
   protocols such as DNS-over-HTTPS (DoH), DNS-over-TLS (DoT), and DNS-
   over-QUIC (DoQ).

### TCP Encapsulation of IKE and IPsec Packets  (draft-smyslov-ipsecme-rfc8229bis)
This document describes a method to transport Internet Key Exchange
   Protocol (IKE) and IPsec packets over a TCP connection for traversing
   network middleboxes that may block IKE negotiation over UDP.  This
   method, referred to as "TCP encapsulation", involves sending both IKE
   packets for Security Association establishment and Encapsulating
   Security Payload (ESP) packets over a TCP connection.  This method is
   intended to be used as a fallback option when IKE cannot be
   negotiated over UDP.

   TCP encapsulation for IKE and IPsec was defined in [RFC8229].  This
   document updates specification for TCP encapsulation by including
   additional calarifications obtained during implementation and
   deployment of this method.  This documents makes RFC8229 obsolete.

### IP Traffic Flow Security YANG Module  (draft-fedyk-ipsecme-yang-iptfs)
This document describes a yang module for the management of IP
   Traffic Flow Security additions to IKEv2 and IPsec.

### Definitions of Managed Objects for IP Traffic Flow Security  (draft-fedyk-ipsecme-mib-iptfs)
This document describes managed objects for the the management of IP
   Traffic Flow Security additions to IKEv2 and IPsec.  This document
   provides a read only version of the objects defined in the YANG
   module for the same purpose.

   This is an unpublished work in progress.

### A YANG Data Model for IP Traffic Flow Security  (draft-ietf-ipsecme-yang-iptfs)
This document describes a YANG module for the management of IP Traffic Flow Security (IP-TFS) additions to Internet Key Exchange Protocol version 2 (IKEv2) and IPsec.

## Working Group: jose
### JSON Proof Algorithms  (draft-jmiller-jose-json-proof-algorithms)
The JSON Proof Algorithms (JPA) specification registers cryptographic
   algorithms and identifiers to be used with the JSON Web Proof (JWP)
   (https://www.ietf.org/archive/id/draft-jmiller-jose-json-web-proof-
   01.html) and JSON Web Key (JWK) specifications.  It defines several
   IANA registries for these identifiers.

### JSON Proof Token  (draft-jmiller-jose-json-proof-token)
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving
   representation of claims to be transferred between three parties.
   The claims in a JPT are encoded as base64url-encoded JSON objects
   that are used as the payloads of a JSON Web Proof (JWP)
   (https://www.ietf.org/archive/id/draft-jmiller-jose-json-web-proof-
   01.html) structure, enabling them to be digitally signed and
   selectively disclosed.  JPTs also support reusability and
   unlinkability when using Zero-Knowledge Proofs (ZKPs).

### JSON Web Proof  (draft-jmiller-jose-json-web-proof)
The JOSE set of standards established JSON-based container formats
   for Keys (https://datatracker.ietf.org/doc/rfc7517/), Signatures
   (https://datatracker.ietf.org/doc/rfc7515/), and Encryption
   (https://datatracker.ietf.org/doc/rfc7516/).  They also established
   IANA registries (https://www.iana.org/assignments/jose/jose.xhtml) to
   enable the algorithms and representations used for them to be
   extended.  Since those were created, newer cryptographic algorithms
   that support selective disclosure and unlinkability have matured and
   started seeing early market adoption.

   This document defines a new container format similar in purpose and
   design to JSON Web Signature (JWS) called a _JSON Web Proof (JWP)_.
   Unlike JWS, which integrity-protects only a single payload, JWP can
   integrity-protect multiple payloads in one message.  It also
   specifies a new presentation form that supports selective disclosure
   of individual payloads, enables additional proof computation, and
   adds a protected header to prevent replay and support binding
   mechanisms.

### Use of Hybrid Public Key Encryption (HPKE) with JSON Object Signing and Encryption (JOSE)  (draft-rha-jose-hpke-encrypt)
This specification defines Hybrid Public Key Encryption (HPKE) for
   use with JSON Object Signing and Encryption (JOSE).  HPKE offers a
   variant of public key encryption of arbitrary-sized plaintexts for a
   recipient public key.

   HPKE works for any combination of an asymmetric key encapsulation
   mechanism (KEM), key derivation function (KDF), and authenticated
   encryption with additional data (AEAD) function.  Authentication for
   HPKE in JOSE is provided by JOSE-native security mechanisms or by one
   of the authenticated variants of HPKE.

   This document defines the use of the HPKE with JOSE.

### JSON Proof Algorithms  (draft-ietf-jose-json-proof-algorithms)
The JSON Proof Algorithms (JPA) specification registers cryptographic
   algorithms and identifiers to be used with the JSON Web Proof, JSON
   Web Key (JWK), and COSE specifications.  It defines IANA registries
   for these identifiers.

### Guidance for COSE and JOSE Protocol Designers and Implementers  (draft-tschofenig-jose-cose-guidance)
JSON Object Signing and Encryption (JOSE) and CBOR Object Signing and
   Encryption (COSE) are two widely used security wrappers, which have
   been developed in the IETF and have intentionally been kept in sync.

   This document provides guidance for protocol designers developing
   extensions for JOSE/COSE and for implementers of JOSE/COSE libraries.
   Developers of application using JSON and/or JOSE should also read
   this document but are realistically more focused on the documentation
   offered by the library they are using.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for JOSE and COSE  (draft-reddy-cose-jose-pqc-kem)
This document describes the conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) within JOSE and COSE.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-reddy-cose-jose-pqc/.

   Discussion of this document takes place on the cose Working Group
   mailing list (mailto:cose@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/cose/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/cose/.

### Fully-Specified Algorithms for JOSE and COSE  (draft-jones-jose-fully-specified-algorithms)
This specification refers to cryptographic algorithm identifiers that
   fully specify the cryptographic operations to be performed, including
   any curve, key derivation function (KDF), hash functions, etc., as
   being "fully specified".  Whereas, it refers to cryptographic
   algorithm identifiers that require additional information beyond the
   algorithm identifier to determine the cryptographic operations to be
   performed as being "polymorphic".  This specification creates fully-
   specified algorithm identifiers for all registered JOSE and COSE
   polymorphic algorithm identifiers, enabling applications to use only
   fully-specified algorithm identifiers.

### Use Cases and Requirements for JSON Object Signing and Encryption (JOSE)  (draft-ietf-jose-use-cases)
Many Internet applications have a need for object-based security mechanisms in addition to security mechanisms at the network layer or transport layer.  For many years, the Cryptographic Message Syntax (CMS) has provided a binary secure object format based on ASN.1.  Over time, binary object encodings such as ASN.1 have become less common than text-based encodings, such as the JavaScript Object Notation (JSON).  This document defines a set of use cases and requirements for a secure object format encoded using JSON, drawn from a variety of application security mechanisms currently in development.

### JSON Web Signature (JWS)  (draft-ietf-jose-json-web-signature)
JSON Web Signature (JWS) represents content secured with digital signatures or Message Authentication Codes (MACs) using JSON-based data structures.  Cryptographic algorithms and identifiers for use with this specification are described in the separate JSON Web Algorithms (JWA) specification and an IANA registry defined by that specification.  Related encryption capabilities are described in the separate JSON Web Encryption (JWE) specification.

### JSON Web Key (JWK)  (draft-ietf-jose-json-web-key)
A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a cryptographic key.  This specification also defines a JWK Set JSON data structure that represents a set of JWKs.  Cryptographic algorithms and identifiers for use with this specification are described in the separate JSON Web Algorithms (JWA) specification and IANA registries established by that specification.

### JSON Web Encryption (JWE)  (draft-ietf-jose-json-web-encryption)
JSON Web Encryption (JWE) represents encrypted content using JSON-based data structures.  Cryptographic algorithms and identifiers for use with this specification are described in the separate JSON Web Algorithms (JWA) specification and IANA registries defined by that specification.  Related digital signature and Message Authentication Code (MAC) capabilities are described in the separate JSON Web Signature (JWS) specification.

### JSON Web Algorithms (JWA)  (draft-ietf-jose-json-web-algorithms)
This specification registers cryptographic algorithms and identifiers to be used with the JSON Web Signature (JWS), JSON Web Encryption (JWE), and JSON Web Key (JWK) specifications.  It defines several IANA registries for these identifiers.

### Examples of Protecting Content Using JSON Object Signing and Encryption (JOSE)  (draft-ietf-jose-cookbook)
This document contains a set of examples using JSON Object Signing and Encryption (JOSE) technology to protect data.  These examples present a representative sampling of JSON Web Key (JWK) objects as well as various JSON Web Signature (JWS) and JSON Web Encryption (JWE) results given similar inputs.

### JSON Web Key (JWK) Thumbprint  (draft-ietf-jose-jwk-thumbprint)
This specification defines a method for computing a hash value over a JSON Web Key (JWK).  It defines which fields in a JWK are used in the hash computation, the method of creating a canonical form for those fields, and how to convert the resulting Unicode string into a byte sequence to be hashed.  The resulting hash value can be used for identifying or selecting the key represented by the JWK that is the subject of the thumbprint.

### JWS Signing Input Options  (draft-jones-jose-jws-signing-input-options)
JSON Web Signature (JWS) represents the payload of a JWS as a
   base64url encoded value and uses this value in the JWS Signature
   computation.  While this enables arbitrary payloads to be integrity
   protected, some have described use cases in which the base64url
   encoding is unnecessary and/or an impediment to adoption, especially
   when the payload is large and/or detached.  This specification
   defines a means of accommodating these use cases by defining an
   option to change the JWS Signing Input computation to not base64url-
   encode the payload.

   Also, JWS includes a representation of the JWS Protected Header and a
   period ('.') character in the JWS Signature computation.  While this
   cryptographically binds the protected Header Parameters to the
   integrity protected payload, some of have described use cases in
   which this binding is unnecessary and/or an impediment to adoption,
   especially when the payload is large and/or detached.  This
   specification defines a means of accommodating these use cases by
   defining an option to change the JWS Signing Input computation to not
   include a representation of the JWS Protected Header and a period
   ('.') character in the JWS Signing Input.

   These options are intended to broaden the set of use cases for which
   the use of JWS is a good fit.

### JSON Web Signature (JWS) Unencoded Payload Option  (draft-ietf-jose-jws-signing-input-options)
JSON Web Signature (JWS) represents the payload of a JWS as a base64url-encoded value and uses this value in the JWS Signature computation. While this enables arbitrary payloads to be integrity protected, some have described use cases in which the base64url encoding is unnecessary and/or an impediment to adoption, especially when the payload is large and/or detached. This specification defines a means of accommodating these use cases by defining an option to change the JWS Signing Input computation to not base64url- encode the payload. This option is intended to broaden the set of use cases for which the use of JWS is a good fit.

 This specification updates RFC 7519 by stating that JSON Web Tokens (JWTs) MUST NOT use the unencoded payload option defined by this specification.

### CFRG Elliptic Curve Diffie-Hellman (ECDH) and Signatures in JSON Object Signing and Encryption (JOSE)  (draft-ietf-jose-cfrg-curves)
This document defines how to use the Diffie-Hellman algorithms "X25519" and "X448" as well as the signature algorithms "Ed25519" and "Ed448" from the IRTF CFRG elliptic curves work in JSON Object Signing and Encryption (JOSE).

### JOSE: Deprecate 'none' and 'RSA1_5'  (draft-madden-jose-deprecate-none-rsa15)
This draft updates [RFC7518] to deprecate the JWS algorithm "none"
   and the JWE algorithm "RSA1_5".  These algorithms have known security
   weaknesses.

### PQ/T Hybrid Composite Signatures for JOSE and COSE  (draft-prabel-jose-pq-composite-sigs)
This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.

### Use of Hybrid Public Key Encryption (HPKE) with JSON Web Encryption (JWE)  (draft-ietf-jose-hpke-encrypt)
This specification defines how to use Hybrid Public Key Encryption
   (HPKE) with JSON Web Encryption (JWE).  HPKE enables public key
   encryption of arbitrary-sized plaintexts to a recipient's public key,
   and provides security against adaptive chosen ciphertext attacks.
   This specification chooses a specific subset of the HPKE features to
   use with JWE.

   This specification updates RFC 7516 (JWE) to enable use of Integrated
   Encryption as a Key Management Mode.

### Fully-Specified Algorithms for JOSE and COSE  (draft-ietf-jose-fully-specified-algorithms)
This specification refers to cryptographic algorithm identifiers that
   fully specify the cryptographic operations to be performed, including
   any curve, key derivation function (KDF), and hash functions, as
   being "fully specified".  It refers to cryptographic algorithm
   identifiers that require additional information beyond the algorithm
   identifier to determine the cryptographic operations to be performed
   as being "polymorphic".  This specification creates fully-specified
   algorithm identifiers for registered JSON Object Signing and
   Encryption (JOSE) and CBOR Object Signing and Encryption (COSE)
   polymorphic algorithm identifiers, enabling applications to use only
   fully-specified algorithm identifiers.  It deprecates those
   polymorphic algorithm identifiers.

   This specification updates RFC 7518, RFC 8037, and RFC 9053.  It
   deprecates polymorphic algorithms defined by RFC 8037 and RFC 9053
   and provides fully-specified replacements for them.  It adds to the
   instructions to designated experts in RFC 7518 and RFC 9053.

### JOSE: Deprecate 'none' and 'RSA1_5'  (draft-ietf-jose-deprecate-none-rsa15)
This document updates [RFC7518] to deprecate the JWS algorithm "none"
   and the JWE algorithm "RSA1_5".  These algorithms have known security
   weaknesses.  It also updates the Review Instructions for Designated
   Experts to establish baseline security requirements that future
   algorithm registrations should meet.

### JSON Proof Token and CBOR Proof Token  (draft-ietf-jose-json-proof-token)
JSON Proof Token (JPT) is a compact, URL-safe, privacy-preserving
   representation of claims to be transferred between three parties.
   The claims in a JPT are encoded as base64url-encoded JSON objects
   that are used as the payloads of a JSON Web Proof (JWP) structure,
   enabling them to be digitally signed and selectively disclosed.  JPTs
   also support reusability and unlinkability when using Zero-Knowledge
   Proofs (ZKPs).

   A CBOR-based representation of JPTs is also defined, called a CBOR
   Proof Token (CPT).  It has the same properties as JPTs, but uses the
   JSON Web Proof (JWP) CBOR Serialization, rather than the JSON-based
   JWP Compact Serialization.

### Post-Quantum Key Encapsulation Mechanisms (PQ KEMs) for JOSE and COSE  (draft-ietf-jose-pqc-kem)
This document describes the conventions for using Post-Quantum Key
   Encapsulation Mechanisms (PQ-KEMs) within JOSE and COSE.

About This Document

   This note is to be removed before publishing as an RFC.

   Status information for this document may be found at
   https://datatracker.ietf.org/doc/draft-ietf-jose-pqc/.

   Discussion of this document takes place on the jose Working Group
   mailing list (mailto:jose@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/cose/.  Subscribe at
   https://www.ietf.org/mailman/listinfo/jose/.

### PQ/T Hybrid Composite Signatures for JOSE and COSE  (draft-ietf-jose-pq-composite-sigs)
This document describes JSON Object Signing and Encryption (JOSE) and
   CBOR Object Signing and Encryption (COSE) serializations for PQ/T
   hybrid composite signatures.  The composite algorithms described
   combine ML-DSA as the post-quantum component and either ECDSA or
   EdDSA as the traditional component.

### JSON Web Proof  (draft-ietf-jose-json-web-proof)
The JOSE set of standards established JSON-based container formats
   for Keys, Signatures, and Encryption.  They also established IANA
   registries to enable the algorithms and representations used for them
   to be extended.  Since those were created, newer cryptographic
   algorithms that support selective disclosure and unlinkability have
   matured and started seeing early market adoption.  The COSE set of
   standards likewise does this for CBOR-based containers, focusing on
   the needs of environments which are better served using CBOR, such as
   constrained devices and networks.

   This document defines a new container format similar in purpose and
   design to JSON Web Signature (JWS) and COSE Signed Messages called a
   _JSON Web Proof (JWP)_.  Unlike JWS, which integrity-protects only a
   single payload, JWP can integrity-protect multiple payloads in one
   message.  It also specifies a new presentation form that supports
   selective disclosure of individual payloads, enables additional proof
   computation, and adds a Presentation Header to prevent replay.

### JOSE HPKE PQ & PQ/T Algorithm Registrations  (draft-skokan-jose-hpke-pq-pqt)
This document registers Post-Quantum (PQ) and Post-Quantum/
   Traditional (PQ/T) hybrid algorithm identifiers for use with JSON
   Object Signing and Encryption (JOSE), building on the Hybrid Public
   Key Encryption (HPKE) framework.

## Working Group: lamps
### DNS Certification Authority Authorization (CAA) Resource Record  (draft-hoffman-andrews-caa-simplification)
The Certification Authority Authorization (CAA) DNS Resource Record
   allows a DNS domain name holder to specify one or more Certification
   Authorities (CAs) authorized to issue certificates for that domain.
   CAA Resource Records allow a public Certification Authority to
   implement additional controls to reduce the risk of unintended
   certificate mis-issue.  This document defines the syntax of the CAA
   record and rules for processing CAA records by certificate issuers.

### X.509 Certificate Extended Key Usage (EKU) for (JOSE) and CBOR Object Signing and Encryption (COSE)  (draft-reddy-lamps-jose-eku)
RFC 5280 specifies several extended key purpose identifiers
   (KeyPurposeIds) for X.509 certificates.  This document defines JSON
   Web Signature (JWS), JSON Web Encryption (JWE), CBOR Object Web
   Signature (CWS) and CBOR Object Web Encryption (CWE) KeyPurposeIds
   inclusion in the Extended Key Usage (EKU) extension of X.509 public
   key certificates.  An application processing JWS, JWE, CWS or CWE may
   require that the EKU extension be present and that a JWS, JWE, CWS or
   CWE KeyPurposeId be indicated in order for the certificate to be
   acceptable to validate the JWS or CWS signature or to encrypt a key
   in JWE or CWE.

### Online Certificate Status Protocol (OCSP) Nonce Extension  (draft-ietf-lamps-ocsp-nonce-update)
RFC 8954 imposed the size constraints on the optional Nonce extension
   for the Online Certificate Status Protocol (OCSP).  OCSP is used for
   checking the status of a certificate, and the Nonce extension is used
   to cryptographically bind an OCSP response message to a particular
   OCSP request message.

   Some environments use cryptographic algorithms that generate a Nonce
   value that is longer than 32 octets.  This document updates the
   maximum allowed length of Nonce to 128 octets.  This document also
   modifies Nonce section to clearly define the encoding format and
   values distinctively for an easier implementation and understanding.
   This document obsoletes RFC 8954 and provides updated ASN.1 modules
   for OCSP, updates RFC 6960.

### Certificate Management over CMS (CMC): Transport Protocols  (draft-mandel-lamps-rfc5273bis)
This document defines a number of transport mechanisms that are used
   to move CMC (Certificate Management over CMS (Cryptographic Message
   Syntax)) messages.  The transport mechanisms described in this
   document are HTTP, file, mail, and TCP.

   This document obsoletes RFCs 5273 and 6402.

### Certificate Management Messages over CMS (CMC): Compliance Requirements  (draft-mandel-lamps-rfc5274bis)
This document provides a set of compliance statements about the CMC
   (Certificate Management over CMS) enrollment protocol.  The ASN.1
   structures and the transport mechanisms for the CMC enrollment
   protocol are covered in other documents.  This document provides the
   information needed to make a compliant version of CMC.

   This document obsoletes RFCs 5274 and 6402.

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA  (draft-gazdag-x509-slhdsa)
Digital signatures are used within X.509 certificates, Certificate
   Revocation Lists (CRLs), and to sign messages.  This document
   describes the conventions for using the Stateless Hash-Based Digital
   Signature Standard (SLH-DSA) in Internet X.509 certificates and
   certificate revocation lists.  The conventions for the associated
   signatures, subject public keys, and private key are also described.

   [EDNOTE: This draft is not expected to be finalized before the NIST
   PQC Project has standardized FIPS 205 Stateless Hash-Based Digital
   Signature Standard.  The current FIPS draft was published August 24,
   2023 for public review.  Final versions are expected by April 2024.
   This specification will use object identifiers for the new algorithms
   that are assigned by NIST, and will use placeholders until these are
   released.]

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for HSS and XMSS  (draft-gazdag-x509-shbs)
This document specifies algorithm identifiers and ASN.1 encoding
   formats for the Stateful Hash-Based Signature Schemes (S-HBS)
   Hierarchical Signature System (HSS), eXtended Merkle Signature Scheme
   (XMSS), and XMSS^MT, a multi-tree variant of XMSS.  This
   specification applies to the Internet X.509 Public Key infrastructure
   (PKI) when those digital signatures are used in Internet X.509
   certificates and certificate revocation lists.

### Hash Of Root Key Certificate Extension  (draft-ietf-lamps-hash-of-root-key-cert-extn)
This document specifies the Hash Of Root Key certificate extension.  This certificate extension is carried in the self-signed certificate for a trust anchor, which is often called a Root Certification Authority (CA) certificate.  This certificate extension unambiguously identifies the next public key that will be used at some point in the future as the next Root CA certificate, eventually replacing the current one.

### X.509 Certificate Extended Key Usage (EKU) for 5G Network Functions  (draft-ietf-lamps-nf-eku)
RFC 5280 specifies several extended key purpose identifiers
   (KeyPurposeIds) for X.509 certificates.  This document defines
   encrypting JSON objects in HTTP messages, JSON Web Token (JWT) and
   signing the OAuth 2.0 access tokens KeyPurposeIds for inclusion in
   the Extended Key Usage (EKU) extension of X.509 v3 public key
   certificates used by Network Functions (NFs) for the 5G System.

### Nonce-based Freshness for Remote Attestation in Certificate Signing Requests (CSRs) for the Certification Management Protocol (CMP) and for Enrollment over Secure Transport (EST)  (draft-tschofenig-lamps-nonce-cmp-est)
Certificate Management Protocol (CMP) and Enrollment over Secure
   Transport (EST) define protocol messages for X.509v3 certificate
   creation and management.  Both protocol provide interactions between
   client systems and PKI management entities, such as a Registration
   Authority (RA) and a Certification Authority (CA).

   CMP and EST allow an RA/CA to request additional information it has
   to provide in a certification request.  When an end entity places
   attestation Evidence in a Certificate Signing Request (CSR) it may
   need to demonstrate freshness of the provided Evidence.  Attestation
   technology today often accomplishes this task via the help of nonces.

   This document specifies how nonces are provided by an RA/CA to the
   end entity for inclusion in Evidence.

### X.509 Certificate Extended Key Usage (EKU) for Instant Messaging URIs  (draft-mahy-lamps-im-keyusage)
RFC 5280 specifies several extended key purpose identifiers
   (KeyPurposeIds) for X.509 certificates.  This document defines
   Instant Messaging (IM) identity KeyPurposeId for inclusion in the
   Extended Key Usage (EKU) extension of X.509 v3 public key
   certificates

### Internet X.509 Public Key Infrastructure - Algorithm Identifiers for the Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM)  (draft-ietf-lamps-kyber-certificates)
The Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) is a
   quantum-resistant key-encapsulation mechanism (KEM).  This document
   specifies the conventions for using the ML-KEM in X.509 Public Key
   Infrastructure.  The conventions for the subject public keys and
   private keys are also specified.

### Use of KYBER in the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-kyber)
This document describes the conventions for using a Key Encapsulation
   Mechanism algorithm (KEM) within the Cryptographic Message Syntax
   (CMS). The CMS specifies the envelopped-data content type, which
   consists of an encrypted content and encrypted content-encryption
   keys for one or more recipients. The mechanism proposed here can
   rely on either post-quantum KEMs, hybrid KEMs or classical KEMs but 
   this document specifies the use of Kyber.

### Composite KEM For Use In Internet PKI  (draft-ounsworth-pq-composite-kem)
The migration to post-quantum cryptography is unique in the history
   of modern digital cryptography in that neither the old outgoing nor
   the new incoming algorithms are fully trusted to protect data for the
   required data lifetimes.  The outgoing algorithms, such as RSA and
   elliptic curve, may fall to quantum cryptalanysis, while the incoming
   post-quantum algorithms face uncertainty about both the underlying
   mathematics as well as hardware and software implementations that
   have not had sufficient maturing time to rule out classical
   cryptanalytic attacks and implementation bugs.

   Cautious implementers may wish to layer cryptographic algorithms such
   that an attacker would need to break all of them in order to
   compromise the data being protected using either a Post-Quantum /
   Traditional Hybrid, Post-Quantum / Post-Quantum Hybrid, or
   combinations thereof.  This document, and its companions, defines a
   specific instantiation of hybrid paradigm called "composite" where
   multiple cryptographic algorithms are combined to form a single key,
   signature, or key encapsulation mechanism (KEM) such that they can be
   treated as a single atomic object at the protocol level.

   This document defines the structure CompositeCiphertextValue which is
   a sequence of the respective ciphertexts for each component
   algorithm.  Explicit pairings of algorithms are defined which should
   meet most Internet needs.  For the purpose of combining KEMs, the
   combiner function from [I-D.ounsworth-cfrg-kem-combiners] is used.

   This document is intended to be coupled with the composite keys
   structure define in [I-D.ounsworth-pq-composite-keys] and the CMS
   KEMRecipientInfo mechanism in [I-D.housley-lamps-cms-kemri].

### Certificate Management Protocol (CMP) Algorithms  (draft-ietf-lamps-cmp-algorithms)
This document describes the conventions for using several cryptographic algorithms with the Certificate Management Protocol (CMP).  CMP is used to enroll and further manage the lifecycle of X.509 certificates.  This document also updates the algorithm use profile from Appendix D.2 of RFC 4210.

### Lightweight Certificate Management Protocol (CMP) Profile  (draft-ietf-lamps-lightweight-cmp-profile)
This document aims at simple, interoperable, and automated PKI management operations covering typical use cases of industrial and Internet of Things (IoT) scenarios.  This is achieved by profiling the Certificate Management Protocol (CMP), the related Certificate Request Message Format (CRMF), and transfer based on HTTP or Constrained Application Protocol (CoAP) in a succinct but sufficiently detailed and self-contained way.  To make secure certificate management for simple scenarios and constrained devices as lightweight as possible, only the most crucial types of operations and options are specified as mandatory.  More specialized or complex use cases are supported with optional features.

### Certification Authority Authorization (CAA) Processing for Email Addresses  (draft-ietf-lamps-caa-issuemail)
The Certification Authority Authorization (CAA) DNS resource record (RR) provides a mechanism for domains to express the allowed set of Certification Authorities that are authorized to issue certificates for the domain.  RFC 8659 contains the core CAA specification, where Property Tags that restrict the issuance of certificates that certify domain names are defined.  This specification defines a Property Tag that grants authorization to Certification Authorities to issue certificates that contain the key purpose in the extension and at least one value or value of type that includes the domain name in the extension.

### Updates to X.509 Policy Validation  (draft-ietf-lamps-x509-policy-graph)
This document updates RFC 5280 to replace the algorithm for X.509
   policy validation with an equivalent, more efficient algorithm.  The
   original algorithm built a structure which scaled exponentially in
   the worst case, leaving implementations vulnerable to denial-of-
   service attacks.

### X.509 Certificate Extended Key Usage (EKU) for Instant Messaging URIs  (draft-ietf-lamps-im-keyusage)
RFC 5280 specifies several extended key purpose identifiers
   (KeyPurposeIds) for X.509 certificates.  This document defines
   Instant Messaging (IM) identity KeyPurposeId for inclusion in the
   Extended Key Usage (EKU) extension of X.509 v3 public key
   certificates

### Internet X.509 Public Key Infrastructure: Algorithm Identifiers for SLH-DSA  (draft-ietf-lamps-x509-slhdsa)
Digital signatures are used within X.509 Public Key Infrastructure
   such as X.509 certificates, Certificate Revocation Lists (CRLs), and
   to sign messages.  This document specifies the conventions for using
   the Stateless Hash-Based Digital Signature Algorithm (SLH-DSA) in
   X.509 Public Key Infrastructure.  The conventions for the associated
   signatures, subject public keys, and private keys are also specified.

### Use of Attestation with Certification Signing Requests  (draft-ounsworth-csr-attestation)
Utilizing information from a device or hardware security module about
   its posture can help to improve security of the overall system.
   Information about the manufacturer of the hardware, the version of
   the firmware running on this hardware and potentially about the
   layers of software above the firmware, the presence of hardware
   security functionality to protect keys and many more properties can
   be made available to remote parties in a cryptographically secured
   way.  This functionality is accomplished with attestation technology.

   This document describes extensions to encode evidence produced by an
   attester for inclusion in PKCS10 certificate signing requests.  More
   specifically, two new ASN.1 Attribute definitions, and an ASN.1 CLASS
   definition to convey attestation information to a Registration
   Authority or to a Certification Authority are described.

### Use of the HSS/LMS Hash-Based Signature Algorithm in the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-rfc8708bis)
This document specifies the conventions for using the Hierarchical
   Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based
   signature algorithm with the Cryptographic Message Syntax (CMS).  In
   addition, the algorithm identifier and public key syntax are
   provided.  The HSS/LMS algorithm is one form of hash-based digital
   signature; it is described in RFC 8554.  This document obsoletes RFC
   8708.

### Online Certificate Status Protocol (OCSP) Nonce Extension  (draft-hsharma-lamps-ocsp-nonce-update)
This document updates the Nonce extension section of RFC-8954.  Nonce
   extension is an optional extension for Online Certificate Status
   Protocol (OCSP) request and response messages.  OCSP is used for
   checking the status of a certificate, and the Nonce extension is used
   to cryptographically bind an OCSP response message to a particular
   OCSP request message.  Some environments use cryptographic algorithms
   that generate a Nonce that is longer than 32 octets.  This document
   updates the maximum allowed length of Nonce to 128 octets.

### Encryption Key Derivation in the Cryptographic Message Syntax (CMS) using HKDF with SHA-256  (draft-housley-lamps-cms-cek-hkdf-sha256)
This document specifies the derivation of the content-encryption key
   or the content-authenticated-encryption key in the Cryptographic
   Message Syntax (CMS).  The use of this mechanism provides protection
   against where the attacker manipulates the content-encryption
   algorithm identifier or the content-authenticated-encryption
   algorithm identifier.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Certificate Handling  (draft-turner-lamps-rfc8550bis)
This document specifies conventions for X.509 certificate usage by
   Secure/Multipurpose Internet Mail Extensions (S/MIME) v4.0 agents.
   S/MIME provides a method to send and receive secure MIME messages,
   and certificates are an integral part of S/MIME agent processing.  S/
   MIME agents validate certificates as described in RFC 5280 ("Internet
   X.509 Public Key Infrastructure Certificate and Certificate
   Revocation List (CRL) Profile").  S/MIME agents must meet the
   certificate-processing requirements in this document as well as those
   in RFC 5280.  This document obsoletes RFC 5750.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Message Specification  (draft-turner-lamps-rfc8551bis)
This document defines Secure/Multipurpose Internet Mail Extensions
   (S/MIME) version 4.0.  S/MIME provides a consistent way to send and
   receive secure MIME data.  Digital signatures provide authentication,
   message integrity, and non-repudiation with proof of origin.
   Encryption provides data confidentiality.  Compression can be used to
   reduce data size.  This document obsoletes RFC 5751.

### Composite ML-KEM for use in X.509 Public Key Infrastructure  (draft-ietf-lamps-pq-composite-kem)
This document defines combinations of US NIST ML-KEM in hybrid with
   traditional algorithms RSA-OAEP, ECDH, X25519, and X448.  These
   combinations are tailored to meet security best practices and
   regulatory guidelines.  Composite ML-KEM is applicable in any
   application that uses X.509 or PKIX data structures that accept ML-
   KEM, but where the operator wants extra protection against breaks or
   catastrophic bugs in ML-KEM.

### Internationalized Email Addresses in X.509 Certificates  (draft-ietf-lamps-rfc8398bis)
This document defines a new name form for inclusion in the otherName
   field of an X.509 Subject Alternative Name and Issuer Alternative
   Name extension that allows a certificate subject to be associated
   with an internationalized email address.

   This document updates RFC 5280 and obsoletes RFC 8398.

### Internationalization Updates to RFC 5280  (draft-ietf-lamps-rfc8399bis)
The updates to RFC 5280 described in this document provide alignment
   with the 2008 specification for Internationalized Domain Names (IDNs)
   and includes support for internationalized email addresses in X.509
   certificates.  The update ensures that name constraints for
   traditional email addresses and internationalized email addresses are
   handled in the same manner.  This document (once approved) obsoletes
   RFC 8399.

### Clarification of Enrollment over Secure Transport (EST): Transfer Encodings and ASN.1  (draft-ietf-lamps-rfc7030est-clarify)
This document updates RFC 7030: Enrollment over Secure Transport to resolve some errata that were reported and that have proven to cause interoperability issues when RFC 7030 was extended.

 This document deprecates the specification of "Content-Transfer-Encoding" headers for Enrollment over Secure Transport (EST) endpoints. This document fixes some syntactical errors in ASN.1 that were present.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Certificate Handling  (draft-ietf-lamps-rfc5750-bis)
This document specifies conventions for X.509 certificate usage by Secure/Multipurpose Internet Mail Extensions (S/MIME) v4.0 agents.  S/MIME provides a method to send and receive secure MIME messages, and certificates are an integral part of S/MIME agent processing.  S/MIME agents validate certificates as described in RFC 5280 ("Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile").  S/MIME agents must meet the certificate-processing requirements in this document as well as those in RFC 5280.  This document obsoletes RFC 5750.

### Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 Message Specification  (draft-ietf-lamps-rfc5751-bis)
This document defines Secure/Multipurpose Internet Mail Extensions (S/MIME) version 4.0.  S/MIME provides a consistent way to send and receive secure MIME data.  Digital signatures provide authentication, message integrity, and non-repudiation with proof of origin.  Encryption provides data confidentiality.  Compression can be used to reduce data size.  This document obsoletes RFC 5751.

### Internationalized Email Addresses in X.509 Certificates  (draft-ietf-lamps-eai-addresses)
This document defines a new name form for inclusion in the otherName field of an X.509 Subject Alternative Name and Issuer Alternative Name extension that allows a certificate subject to be associated with an internationalized email address.

 This document updates RFC 5280.

### Internationalization Updates to RFC 5280  (draft-ietf-lamps-rfc5280-i18n-update)
The updates to RFC 5280 described in this document provide alignment with the 2008 specification for Internationalized Domain Names (IDNs) and add support for internationalized email addresses in X.509 certificates.

### Internet X.509 Public Key Infrastructure: Additional Algorithm Identifiers for RSASSA-PSS and ECDSA Using SHAKEs  (draft-ietf-lamps-pkix-shake)
Digital signatures are used to sign messages, X.509 certificates, and Certificate Revocation Lists (CRLs).  This document updates the "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile" (RFC 3279) and describes the conventions for using the SHAKE function family in Internet X.509 certificates and revocation lists as one-way hash functions with the RSA Probabilistic signature and Elliptic Curve Digital Signature Algorithm (ECDSA) signature algorithms.  The conventions for the associated subject public keys are also described.

### Use of the SHAKE One-Way Hash Functions in the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-cms-shakes)
This document updates the "Cryptographic Message Syntax (CMS) Algorithms" (RFC 3370) and describes the conventions for using the SHAKE family of hash functions in the Cryptographic Message Syntax as one-way hash functions with the RSA Probabilistic Signature Scheme (RSASSA-PSS) and Elliptic Curve Digital Signature Algorithm (ECDSA).  The conventions for the associated signer public keys in CMS are also described.

### Certification Authority Authorization (CAA) Processing for Email Addresses  (draft-bonnell-caa-issuemail)
The Certification Authority Authorization (CAA) DNS resource record
   type provides a mechanism for domains to express the allowed set of
   Certification Authorities that may issue certificates for the domain.
   The core CAA specification ([RFC8659]) solely defines Property Tags
   that restrict the issuance of certificates that certify domain names;
   it does not define a mechanism for domains to restrict the issuance
   of certificates that include email addresses.  This specification
   defines a Property Tag that grants authorization to Certification
   Authorities to issue certificates which certify email addresses.

### DNS Certification Authority Authorization (CAA) Resource Record  (draft-ietf-lamps-rfc6844bis)
The Certification Authority Authorization (CAA) DNS Resource Record allows a DNS domain name holder to specify one or more Certification Authorities (CAs) authorized to issue certificates for that domain name. CAA Resource Records allow a public CA to implement additional controls to reduce the risk of unintended certificate mis-issue. This document defines the syntax of the CAA record and rules for processing CAA records by CAs.

 This document obsoletes RFC 6844.

### Use of the HSS/LMS Hash-Based Signature Algorithm in the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-cms-hash-sig)
This document specifies the conventions for using the Hierarchical Signature System (HSS) / Leighton-Micali Signature (LMS) hash-based signature algorithm with the Cryptographic Message Syntax (CMS).  In addition, the algorithm identifier and public key syntax are provided.  The HSS/LMS algorithm is one form of hash-based digital signature; it is described in RFC 8554.

### Using Pre-Shared Key (PSK) in the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-cms-mix-with-psk)
The invention of a large-scale quantum computer would pose a serious challenge for the cryptographic algorithms that are widely deployed today.  The Cryptographic Message Syntax (CMS) supports key transport and key agreement algorithms that could be broken by the invention of such a quantum computer.  By storing communications that are protected with the CMS today, someone could decrypt them in the future when a large-scale quantum computer becomes available.  Once quantum-secure key management algorithms are available, the CMS will be extended to support the new algorithms if the existing syntax does not accommodate them.  This document describes a mechanism to protect today's communication from the future invention of a large-scale quantum computer by mixing the output of key transport and key agreement algorithms with a pre-shared key.

### Certificate Management Protocol (CMP) Updates  (draft-ietf-lamps-cmp-updates)
This document contains a set of updates to the syntax of Certificate Management Protocol (CMP) version 2 and its HTTP transfer mechanism. This document updates RFCs 4210, 5912, and 6712.

 The aspects of CMP updated in this document are using EnvelopedData instead of EncryptedValue, clarifying the handling of p10cr messages, improving the crypto agility, as well as adding new general message types, extended key usages to identify certificates for use with CMP, and well-known URI path segments.

 CMP version 3 is introduced to enable signaling support of EnvelopedData instead of EncryptedValue and signal the use of an explicit hash AlgorithmIdentifier in certConf messages, as far as needed.

### Clarification of Enrollment over Secure Transport (EST): transfer encodings and ASN.1  (draft-richardson-lamps-rfc7030est-clarify)
This document updates RFC7030: Enrollment over Secure Transport (EST)
   to resolve some errata that was reported, and which has proven to
   have interoperability when RFC7030 has been extended.

   This document deprecates the specification of "Content-Transfer-
   Encoding" headers for EST endpoints, providing a way to do this in an
   upward compatible way.  This document additional defines a GRASP
   discovery mechanism for EST endpoints, and specifies requirements for
   them.

   Finally, this document fixes some syntactical errors in ASN.1 that
   was presented.

### Clarifications for Elliptic Curve Cryptogtaphy Subject Public Key Information  (draft-turner-5480-ku-clarifications)
This document updates RFC 5480 to specify semantics for the
   keyEncipherment and dataEncipherment key usage bits when used in
   certificates that support Elliptic Curve Cryptography.

### Problem Statement and Requirements for Header Protection  (draft-ietf-lamps-header-protection-requirements)
Privacy and security issues with email header protection in S/MIME
   have been identified for some time.  However, the desire to fix these
   issues has only recently been expressed in the IETF LAMPS Working
   Group.  The existing S/MIME specification is likely to be updated
   regarding header protection.

   This document describes the problem statement, generic use cases, and
   requirements of header protection.

### Update to the Cryptographic Message Syntax (CMS) for Algorithm Identifier Protection  (draft-housley-lamps-cms-update-alg-id-protect)
This document updates the Cryptographic Message Syntax (CMS)
   specified in RFC 5652 to ensure that algorithm identifiers are
   adequately protected.

### Clarifications for Elliptic Curve Cryptography Subject Public Key Information  (draft-ietf-lamps-5480-ku-clarifications)
This document updates RFC 5480 to specify semantics for the keyEncipherment and dataEncipherment key usage bits when used in certificates that support Elliptic Curve Cryptography.

### Update to the Cryptographic Message Syntax (CMS) for Algorithm Identifier Protection  (draft-ietf-lamps-cms-update-alg-id-protect)
This document updates the Cryptographic Message Syntax (CMS) specified in RFC 5652 to ensure that algorithm identifiers in signed-data and authenticated-data content types are adequately protected.

### Online Certificate Status Protocol (OCSP) Nonce Extension  (draft-ietf-lamps-ocsp-nonce)
This document specifies the updated format of the Nonce extension in the Online Certificate Status Protocol (OCSP) request and response messages.  OCSP is used to check the status of a certificate, and the Nonce extension is used to cryptographically bind an OCSP response message to a particular OCSP request message.  This document updates RFC 6960.

### Algorithm Requirements Update to the Internet X.509 Public Key Infrastructure Certificate Request Message Format (CRMF)  (draft-housley-lamps-crmf-update-algs)
This document updates the cryptographic algorithm requirements for
   the Password-Based Message Authentication Code in the Internet X.509
   Public Key Infrastructure Certificate Request Message Format (CRMF)
   specified in RFC 4211.

### Guidance on End-to-End E-mail Security  (draft-dkg-lamps-e2e-mail-guidance)
End-to-end cryptographic protections for e-mail messages can provide
   useful security.  However, the standards for providing cryptographic
   protection are extremely flexible.  That flexibility can trap users
   and cause surprising failures.  This document offers guidance for
   mail user agent implementers that need to compose or interpret e-mail
   messages with end-to-end cryptographic protection.  It provides a
   useful set of vocabulary as well as suggestions to avoid common
   failures.

### Using the AES-GMAC Algorithm with the Cryptographic Message Syntax (CMS)  (draft-housley-lamps-cms-aes-mac-alg)
This document specifies the conventions for using the AES-GMAC
   Message Authentication Code algorithms with the Cryptographic Message
   Syntax (CMS) as specified in RFC 5652.

### Using the AES-GMAC Algorithm with the Cryptographic Message Syntax (CMS)  (draft-ietf-lamps-cms-aes-gmac-alg)
This document specifies the conventions for using the AES-GMAC Message Authentication Code algorithm with the Cryptographic Message Syntax (CMS) as specified in RFC 5652.

### Algorithm Requirements Update to the Internet X.509 Public Key Infrastructure Certificate Request Message Format (CRMF)  (draft-ietf-lamps-crmf-update-algs)
This document updates the cryptographic algorithm requirements for the Password-Based Message Authentication Code in the Internet X.509 Public Key Infrastructure Certificate Request Message Format (CRMF) specified in RFC 4211.

### General Purpose Extended Key Usage (EKU) for Document Signing X.509 Certificates  (draft-ito-documentsigning-eku)
[RFC5280] specifies several extended key usages for X.509
   certificates.  This document defines a general purpose document
   signing extended key usage for X.509 public key certificates which
   restricts the usage of the certificates for document signing.

### S/MIME Example Keys and Certificates  (draft-ietf-lamps-samples)
The S/MIME development community benefits from sharing samples of signed or encrypted data.  This document facilitates such collaboration by defining a small set of X.509v3 certificates and keys for use when generating such samples.

### Update to the Object Identifier Registry for the PKIX Working Group  (draft-ietf-lamps-rfc7299-update)
RFC 7299 describes the object identifiers that were assigned by the Public Key Infrastructure using X.509 (PKIX) Working Group in an arc that was allocated by IANA (1.3.6.1.5.5.7).  A small number of object identifiers that were assigned in RFC 4212 are omitted from RFC 7299, and this document updates RFC 7299 to correct that oversight.

### Clarification of RFC7030 CSR Attributes definition  (draft-richardson-lamps-rfc7030-csrattrs)
The Enrollment over Secure Transport (EST, RFC7030) is ambiguous in
   its specification of the CSR Attributes Response.  This has resulted
   in implementation challenges and implementor confusion.

   This document updates RFC7030 (EST) and clarifies how the CSR
   Attributes Response can be used by an EST server to specify both CSR
   attribute OIDs and also CSR attribute values that the server expects
   the client to include in subsequent CSR request.

### Use of Post-Quantum KEM in the Cryptographic Message Syntax (CMS)  (draft-perret-prat-lamps-cms-pq-kem)
This document describes the conventions for using a Key Encapsulation
   Mechanism algorithm (KEM) within the Cryptographic Message Syntax
   (CMS).  The CMS specifies the enveloped-data content type, which
   consists of an encrypted content and encrypted content-encryption
   keys for one or more recipients.  The mechanism proposed here can
   rely on either post-quantum KEMs, hybrid KEMs or classical KEMs.

### Clarifications for Ed25519, Ed448, X25519, and X448 Algorithm Identifiers  (draft-ietf-lamps-8410-ku-clarifications)
This document updates RFC 8410 to clarify existing semantics, and specify missing semantics, for key usage bits when used in certificates that support the Ed25519, Ed448, X25519, and X448 Elliptic Curve Cryptography algorithms.

### Clarifications for Ed25519, Ed448, X25519, and X448 Algorithm Identifiers  (draft-mtis-lamps-8410-ku-clarifications)
This document updates RFC 8410 to clarify existing and specify
   missing semantics for key usage bits when used in certificates that
   support the Ed25519, Ed448, X25519, and X448 Elliptic Curve
   Cryptography algorithms.

## Working Group: masque
### The CONNECT-UDP HTTP Method  (draft-schinazi-masque-connect-udp)
This document describes the CONNECT-UDP HTTP method.  CONNECT-UDP is
   similar to the HTTP CONNECT method, but it uses UDP instead of TCP.

   Discussion of this work is encouraged to happen on the MASQUE IETF
   mailing list masque@ietf.org or on the GitHub repository which
   contains the draft: https://github.com/DavidSchinazi/masque-drafts.

### Requirements for a MASQUE Protocol to Proxy IP Traffic  (draft-cms-masque-ip-proxy-reqs)
There is interest among MASQUE working group participants in
   designing a protocol that can proxy IP traffic over HTTP.  This
   document describes the set of requirements for such a protocol.

   Discussion of this work is encouraged to happen on the MASQUE IETF
   mailing list masque@ietf.org or on the GitHub repository which
   contains the draft: https://github.com/DavidSchinazi/masque-drafts.

### Proxying UDP in HTTP  (draft-ietf-masque-connect-udp)
This document describes how to proxy UDP in HTTP, similar to how the HTTP CONNECT method allows proxying TCP in HTTP.  More specifically, this document defines a protocol that allows an HTTP client to create a tunnel for UDP communications through an HTTP server that acts as a proxy.

### Requirements for a MASQUE Protocol to Proxy IP Traffic  (draft-ietf-masque-ip-proxy-reqs)
There is interest among MASQUE working group participants in
   designing a protocol that can proxy IP traffic over HTTP.  This
   document describes the set of requirements for such a protocol.

   Discussion of this work is encouraged to happen on the MASQUE IETF
   mailing list masque@ietf.org or on the GitHub repository which
   contains the draft: https://github.com/ietf-wg-masque/draft-ietf-
   masque-ip-proxy-reqs.

### QUIC-Aware Proxying Using HTTP  (draft-pauly-masque-quic-proxy)
This document defines an extension to UDP Proxying over HTTP that
   adds specific optimizations for proxied QUIC connections.  This
   extension allows a proxy to reuse UDP 4-tuples for multiple
   connections.  It also defines a mode of proxying in which QUIC short
   header packets can be forwarded using an HTTP/3 proxy rather than
   being re-encapsulated and re-encrypted.

### Using QUIC Datagrams with HTTP/3  (draft-schinazi-masque-h3-datagram)
The QUIC DATAGRAM extension provides application protocols running
   over QUIC with a mechanism to send unreliable data while leveraging
   the security and congestion-control properties of QUIC.  However,
   QUIC DATAGRAM frames do not provide a means to demultiplex
   application contexts.  This document defines how to use QUIC DATAGRAM
   frames when the application protocol running over QUIC is HTTP/3 by
   adding an identifier at the start of the frame payload.  This allows
   HTTP messages to convey related information using unreliable DATAGRAM
   frames, ensuring those frames are properly associated with an HTTP
   message.

   Discussion of this work is encouraged to happen on the MASQUE IETF
   mailing list (masque@ietf.org (mailto:masque@ietf.org)) or on the
   GitHub repository which contains the draft:
   https://github.com/DavidSchinazi/draft-h3-datagram.

### HTTP Datagrams and the Capsule Protocol  (draft-ietf-masque-h3-datagram)
This document describes HTTP Datagrams, a convention for conveying multiplexed, potentially unreliable datagrams inside an HTTP connection.

 In HTTP/3, HTTP Datagrams can be sent unreliably using the QUIC DATAGRAM extension. When the QUIC DATAGRAM frame is unavailable or undesirable, HTTP Datagrams can be sent using the Capsule Protocol, which is a more general convention for conveying data in HTTP connections.

 HTTP Datagrams and the Capsule Protocol are intended for use by HTTP extensions, not applications.

### IP Proxying Support for HTTP  (draft-age-masque-connect-ip)
This document describes a method of proxying IP packets over HTTP.
   This protocol is similar to CONNECT-UDP, but allows transmitting
   arbitrary IP packets, without being limited to just TCP like CONNECT
   or UDP like CONNECT-UDP.

### Proxying IP in HTTP  (draft-ietf-masque-connect-ip)
This document describes how to proxy IP packets in HTTP.  This protocol is similar to UDP proxying in HTTP but allows transmitting arbitrary IP packets.  More specifically, this document defines a protocol that allows an HTTP client to create an IP tunnel through an HTTP server that acts as an IP proxy.  This document updates RFC 9298.

### QUIC-Aware Proxying Using HTTP  (draft-ietf-masque-quic-proxy)
This document extends UDP Proxying over HTTP to add optimizations for
   proxied QUIC connections.  Specifically, it allows a proxy to reuse
   UDP 4-tuples for multiple proxied connections, and adds a mode of
   proxying in which QUIC short header packets can be forwarded and
   transformed through a HTTP/3 proxy rather than being fully re-
   encapsulated and re-encrypted.

### Proxying Ethernet in HTTP  (draft-ietf-masque-connect-ethernet)
This document describes how to proxy Ethernet frames in HTTP.  This
   protocol is similar to IP proxying in HTTP, but for Layer 2 instead
   of Layer 3.  More specifically, this document defines a protocol that
   allows an HTTP client to create a tunnel to exchange Layer 2 Ethernet
   frames through an HTTP server with an attached physical or virtual
   Ethernet segment.

### DNS and PREF64 Configuration for Proxying IP in HTTP  (draft-ietf-masque-connect-ip-dns)
Proxying IP in HTTP allows building a VPN through HTTP load
   balancers.  However, at the time of writing, that mechanism lacks a
   way to communicate network configuration details such as DNS
   information or IPv6 NAT64 prefixes (PREF64).  In contrast, most
   existing VPN protocols provide mechanisms to exchange such
   configuration information.

   This document defines extensions that convey DNS and PREF64
   configuration using HTTP capsules.  This mechanism supports encrypted
   DNS transports and can be used to inform peers about network
   translation prefixes for IPv6/IPv4 synthesis.

### ECN and DSCP support for HTTPS's Connect-UDP  (draft-westerlund-masque-connect-udp-ecn-dscp)
HTTP's Extended Connect's Connect-UDP protocol enables a client to
   proxy a UDP flow from the HTTP server towards a specified target IP
   address and UDP port.  QUIC and Real-time transport protocol (RTP)
   are examples of transport protocols that use UDP and support Explicit
   Congestion Notification (ECN) and provide the necessary feedback.
   This document specifies how ECN and DSCP can be supported through an
   extension to the Connect-UDP protocol for HTTP without per-packet
   byte overhead, soley using Context IDs.

### Extensions to Compress and Derive Fields in HTTP Datagrams  (draft-rosomakho-masque-connect-ip-optimizations)
This document defines extensions for HTTP Datagram-based protocols
   that improve transmission efficiency by introducing templates for
   compressing or deriving datagram fields.

   These templates allow endpoints to define parts of datagrams that are
   static and can be removed, and other parts that can be derived (such
   as packet lengths and checksum values).

   Additionally, this document defines a checksum offload procedure
   enabling receivers to complete Internet checksums using sender-
   provided partial values.

   These optimisations reduce per-packet overhead, processing cost, and
   increase the effective maximum transmission unit (MTU) when datagrams
   are encapsulated in QUIC DATAGRAM frames.

### Proxying Bound UDP in HTTP  (draft-ietf-masque-connect-udp-listen)
The mechanism to proxy UDP in HTTP only allows each UDP proxying
   request to transmit to a specific host and port.  This is well suited
   for UDP client-server protocols such as HTTP/3, but is not sufficient
   for some UDP peer-to-peer protocols like WebRTC.  This document
   proposes an extension to UDP proxying in HTTP that enables such use-
   cases.

## Working Group: nvo3
### NVO3 Data Plane Requirements  (draft-ietf-nvo3-dataplane-requirements)
Several IETF drafts relate to the use of overlay networks to support
       large scale virtual data centers. This draft provides a list of data
       plane requirements for Network Virtualization over L3 (NVO3) that
       have to be addressed in solutions documents.

### Network Virtualization NVE to NVA Control Protocol Requirements  (draft-ietf-nvo3-nve-nva-cp-req)
[RFC7364] "Problem Statement: Overlays for Network Virtualization"
   discusses the needs for network virtualization using overlay networks
   in highly virtualized data centers.  The problem statement outlines a
   need for control protocols to facilitate running these overlay
   networks.  This document outlines the high level requirements to be
   fulfilled by the control protocols related to building and managing
   the mapping tables and other state information used by the Network
   Virtualization Edge to transmit encapsulated packets across the
   underlying network.

### BFD for Geneve  (draft-ietf-nvo3-bfd-geneve)
This document describes the use of the Bidirectional Forwarding
   Detection (BFD) protocol in point-to-point Generic Network
   Virtualization Encapsulation (Geneve) unicast tunnels used to make up
   an overlay network.

### Generic Protocol Extension for VXLAN (VXLAN-GPE)  (draft-ietf-nvo3-vxlan-gpe)
This document describes extending Virtual eXtensible Local Area
   Network (VXLAN), via changes to the VXLAN header, with four new
   capabilities: support for multi-protocol encapsulation, support for
   operations, administration and maintenance (OAM) signaling, support
   for ingress-replicated BUM Traffic (i.e.  Broadcast, Unknown unicast,
   or Multicast), and explicit versioning.  New protocol capabilities
   can be introduced via shim headers.

### Network-related VM Mobility Issues  (draft-ietf-nvo3-vm-mobility-issues)
This document describes a set of network-related issues presented by
   the desire to support seamless Virtual Machine mobility in the data
   center and between data centers. In particular, it looks at the
   implications of meeting the requirements for "seamless mobility".

### NVO3 Gap Analysis - Requirements Versus Available Technology Choices  (draft-ietf-nvo3-gap-analysis)
This document evaluates candidate protocols against the NVO3
   requirements.  Gaps are identified and further work recommended.

### Security Requirements of NVO3  (draft-ietf-nvo3-security-requirements)
The draft describes a list of essential requirements in order to
   benefit the design of NVO3 security solutions. In addition, this
   draft introduces the candidate techniques which could be used to
   construct a security solution fulfilling these security requirements.

### Framework for DC Network Virtualization  (draft-lasserre-nvo3-framework)
Several IETF drafts relate to the use of overlay networks to support
        large scale virtual data centers. This draft provides a framework
        for Network Virtualization over L3 (NVO3) and is intended to help
        plan a set of work items in order to provide a complete solution
        set. It defines a logical view of the main components with the
        intention of streamlining the terminology and focusing the solution
        set.

### Use Cases for DC Network Virtualization Overlays  (draft-mity-nvo3-use-case)
This draft describes the general NVO3 use cases. The work intention
   is to help validate the NVO3 framework and requirements as along
   with the development of the solutions.

### Problem Statement: Overlays for Network Virtualization  (draft-ietf-nvo3-overlay-problem-statement)
This document describes issues associated with providing multi-tenancy in large data center networks and how these issues may be addressed using an overlay-based network virtualization approach.  A key multi-tenancy requirement is traffic isolation so that one tenant's traffic is not visible to any other tenant.  Another requirement is address space isolation so that different tenants can use the same address space within different virtual networks.  Traffic and address space isolation is achieved by assigning one or more virtual networks to each tenant, where traffic within a virtual network can only cross into another virtual network in a controlled fashion (e.g., via a configured router and/or a security gateway).  Additional functionality is required to provision virtual networks, associating a virtual machine's network interface(s) with the appropriate virtual network and maintaining that association as the virtual machine is activated, migrated, and/or deactivated.  Use of an overlay-based approach enables scalable deployment on large network infrastructures.

### Framework for Data Center (DC) Network Virtualization  (draft-ietf-nvo3-framework)
This document provides a framework for Data Center (DC) Network Virtualization over Layer 3 (NVO3) and defines a reference model along with logical components required to design a solution.

### Use Cases for Data Center Network Virtualization Overlay Networks  (draft-ietf-nvo3-use-case)
This document describes Network Virtualization over Layer 3 (NVO3) use cases that can be deployed in various data centers and serve different data-center applications.

### Generic Protocol Extension for VXLAN  (draft-quinn-vxlan-gpe)
This draft describes extending Virtual eXtensible Local Area Network
   (VXLAN), via changes to the VXLAN header, with three new
   capabilities: support for multi-protocol encapsulation, operations,
   administration and management (OAM) signaling and explicit
   versioning.

### An Architecture for Data-Center Network Virtualization over Layer 3 (NVO3)  (draft-ietf-nvo3-arch)
This document presents a high-level overview architecture for building data-center Network Virtualization over Layer 3 (NVO3) networks.  The architecture is given at a high level, showing the major components of an overall system.  An important goal is to divide the space into individual smaller components that can be implemented independently with clear inter-component interfaces and interactions.  It should be possible to build and implement individual components in isolation and have them interoperate with other independently implemented components.  That way, implementers have flexibility in implementing individual components and can optimize and innovate within their respective components without requiring changes to other components.

### Generic UDP Encapsulation  (draft-herbert-gue)
This specification describes Generic UDP Encapsulation (GUE), which
   is a scheme for using UDP to encapsulate packets of arbitrary IP
   protocols for transport across layer 3 networks. By encapsulating
   packets in UDP, specialized capabilities in networking hardware for
   efficient handling of UDP packets can be leveraged. GUE specifies
   basic encapsulation methods upon which higher level constructs, such
   tunnels and overlay networks for network virtualization, can be
   constructed. GUE is extensible by allowing optional data fields as
   part of the encapsulation, and is generic in that it can encapsulate
   packets of various IP protocols.

### Geneve: Generic Network Virtualization Encapsulation  (draft-gross-geneve)
Network virtualization involves the cooperation of devices with a
   wide variety of capabilities such as software and hardware tunnel
   endpoints, transit fabrics, and centralized control clusters.  As a
   result of their role in tying together different elements in the
   system, the requirements on tunnels are influenced by all of these
   components.  Flexibility is therefore the most important aspect of a
   tunnel protocol if it is to keep pace with the evolution of the
   system.  This draft describes Geneve, a protocol designed to
   recognize and accommodate these changing capabilities and needs.

### Split Network Virtualization Edge (Split-NVE) Control-Plane Requirements  (draft-ietf-nvo3-hpvr2nve-cp-req)
In the Split Network Virtualization Edge (Split-NVE) architecture, the functions of the NVE are split across a server and a piece of external network equipment that is called an "External NVE". The server-resident control-plane functionality resides in control software, which may be part of hypervisor or container-management software; for simplicity, this document refers to the hypervisor as the "location" of this software.

 One or more control-plane protocols between a hypervisor and its associated External NVE(s) are used by the hypervisor to distribute its virtual-machine networking state to the External NVE(s) for further handling. This document illustrates the functionality required by this type of control-plane signaling protocol and outlines the high-level requirements. Virtual-machine states as well as state transitioning are summarized to help clarify the protocol requirements.

### A Framework for Multicast in NVO3  (draft-ghanwani-nvo3-mcast-framework)
This document discusses a framework of supporting multicast traffic,
   , in a network that uses Network Virtualization using Overlays over
   Layer 3 (NVO3). Both infrastructure multicast and application-
   specific multicast are discussed. It describes the various
   mechanisms and considerations that can be used for delivering such
   traffic as well as the data plane and control plane considerations
   for each of the mechanisms.

### Generic UDP Encapsulation  (draft-ietf-nvo3-gue)
This specification describes Generic UDP Encapsulation (GUE), which
   is a scheme for using UDP to encapsulate packets of different IP
   protocols for transport across layer 3 networks. By encapsulating
   packets in UDP, specialized capabilities in networking hardware for
   efficient handling of UDP packets can be leveraged. GUE specifies
   basic encapsulation methods upon which higher level constructs, such
   tunnels and overlay networks for network virtualization, can be
   constructed. GUE is extensible by allowing optional data fields as
   part of the encapsulation, and is generic in that it can encapsulate
   packets of various IP protocols.

### Geneve: Generic Network Virtualization Encapsulation  (draft-ietf-nvo3-geneve)
Network virtualization involves the cooperation of devices with a wide variety of capabilities such as software and hardware tunnel endpoints, transit fabrics, and centralized control clusters.  As a result of their role in tying together different elements of the system, the requirements on tunnels are influenced by all of these components.  Therefore, flexibility is the most important aspect of a tunneling protocol if it is to keep pace with the evolution of technology.  This document describes Geneve, an encapsulation protocol designed to recognize and accommodate these changing capabilities and needs.

### A Framework for Multicast in Network Virtualization over Layer 3  (draft-ietf-nvo3-mcast-framework)
This document provides a framework for supporting multicast traffic in a network that uses Network Virtualization over Layer 3 (NVO3).  Both infrastructure multicast and application-specific multicast are discussed.  It describes the various mechanisms that can be used for delivering such traffic as well as the data plane and control plane considerations for each of the mechanisms.

### Applicability of Ethernet Virtual Private Network (EVPN) to Network Virtualization over Layer 3 (NVO3) Networks  (draft-ietf-nvo3-evpn-applicability)
An Ethernet Virtual Private Network (EVPN) provides a unified control plane that solves the issues of Network Virtualization Edge (NVE) auto-discovery, tenant Media Access Control (MAC) / IP dissemination, and advanced features in a scablable way as required by Network Virtualization over Layer 3 (NVO3) networks.  EVPN is a scalable solution for NVO3 networks and keeps the independence of the underlay IP Fabric, i.e., there is no need to enable Protocol Independent Multicast (PIM) in the underlay network and maintain multicast states for tenant Broadcast Domains.  This document describes the use of EVPN for NVO3 networks and discusses its applicability to basic Layer 2 and Layer 3 connectivity requirements and to advanced features such as MAC Mobility, MAC Protection and Loop Protection, multihoming, Data Center Interconnect (DCI), and much more.  No new EVPN procedures are introduced.

### Network Virtualization Overlays (NVO3) Encapsulation Considerations  (draft-ietf-nvo3-encap)
The IETF Network Virtualization Overlays (NVO3) Working Group
   developed considerations for a common encapsulation that addresses
   various network virtualization overlay technical concerns.  This
   document provides a record, for the benefit of the IETF community, of
   the considerations arrived at starting from the output of an NVO3
   encapsulation design team.  These considerations may be helpful with
   future deliberations by working groups over the choice of
   encapsulation formats.

   There are implications of having different encapsulations in real
   environments consisting of both software and hardware implementations
   and within and spanning multiple data centers.  For example, OAM
   functions such as path MTU discovery become challenging with multiple
   encapsulations along the data path.

   Based on these considerations, the Working Group determined that
   Geneve with a few modifications as the common encapsulation.  This
   document provides more details, particularly in Section 7.

### Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks  (draft-md-nvo3-rfc7348bis)
This document is a resubmission of RFC7348 as an IETF document stream
   so that proper IETF code points can be assigned in the IANA section
   for future work based on this RFC.  This document obsoletes RFC7348
   (Virtual eXtensible Local Area Network - VXLAN), which is used to
   address the need for overlay networks within virtualized data centers
   accommodating multiple tenants.  The scheme and the related protocols
   can be used in networks for cloud service providers and enterprise
   data centers.  This memo documents the deployed VXLAN protocol for
   the benefit of the Internet community.

### Active OAM for use in Geneve  (draft-ietf-nvo3-geneve-oam)
Geneve (Generic Network Virtualization Encapsulation) is a flexible
   and extensible network virtualization overlay protocol designed to
   encapsulate network packets for transport across underlying physical
   networks.  This document specifies the requirements and provides a
   framework for Operations, Administration, and Maintenance (OAM) in
   Geneve networks.  It outlines the OAM functions necessary to monitor,
   diagnose, and troubleshoot Geneve overlay networks to ensure proper
   operation and performance.  The document aims to guide the
   implementation of OAM mechanisms within the Geneve protocol to
   support network operators in maintaining reliable and efficient
   virtualized network environments.

### Base YANG Data Model for NVO3 Protocols  (draft-ietf-nvo3-yang-cfg)
This document describes the base YANG data model that can be used by
   operators to configure and manage Network Virtualization Overlay
   protocols.  The model is focused on the common configuration
   requirement of various encapsulation options, such as VXLAN, NVGRE,
   GENEVE and VXLAN-GPE.  Using this model as a starting point,
   incremental work can be done to satisfy the requirement of a specific
   encapsulation.  The model is based on YANG 1.1, which is defined in
   RFC 7950 and conforms to the Network Management Datastore
   Architecture (NMDA).

### Virtual Machine Mobility Solutions for L2 and L3 Overlay Networks  (draft-ietf-nvo3-vmm)
This document describes virtual machine (VM) mobility
   solutions commonly used in data centers built with an overlay
   network. This document is intended for describing the
   solutions and the impact of moving VMs, or applications, from
   one rack to another connected by the overlay network.

   For layer 2, it is based on using an NVA (Network
   Virtualization Authority) to NVE (Network Virtualization
   Edge) protocol to update ARP (Address Resolution Protocol)
   tables or neighbor cache entries after a VM moves from an old
   NVE to a new NVE.  For Layer 3, it is based on address and
   connection migration after the move.

### Virtual eXtensible Local Area Network (VXLAN): A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks  (draft-ietf-nvo3-rfc7348bis)
This document specifies Virtual eXtensible Local Area Network
   (VXLAN), which is used to address the need for overlay networks
   within virtualized data centers accommodating multiple tenants.  The
   scheme and the related protocols can be used in networks for cloud
   service providers and enterprise data centers.  This document
   obsoletes RFC 7348, which documented the deployed VXLAN protocol for
   the benefit of the Internet community, and moves the VXLAN
   specification to the IETF document stream, allowing for the creation
   of extensions to VXLAN that require additions to the VXLAN header and
   their registration with IANA.  The format and processing described
   here are fully compatible with those in RFC7348.

## Working Group: oauth
### OAuth 2.0 Dynamic Client Registration Protocol  (draft-ietf-oauth-dyn-reg)
This specification defines mechanisms for dynamically registering OAuth 2.0 clients with authorization servers.  Registration requests send a set of desired client metadata values to the authorization server.  The resulting registration responses return a client identifier to use at the authorization server and the client metadata values registered for the client.  The client can then use this registration information to communicate with the authorization server using the OAuth 2.0 protocol.  This specification also defines a set of common client metadata fields and values for clients to use during registration.

### OAuth 2.0 Token Exchange  (draft-ietf-oauth-token-exchange)
This specification defines a protocol for an HTTP- and JSON-based Security Token Service (STS) by defining how to request and obtain security tokens from OAuth 2.0 authorization servers, including security tokens employing impersonation and delegation.

### JWT Response for OAuth Token Introspection  (draft-ietf-oauth-jwt-introspection-response)
This specification proposes an additional JSON Web Token (JWT)
   secured response for OAuth 2.0 Token Introspection.

### The OAuth 2.1 Authorization Framework  (draft-ietf-oauth-v2-1)
The OAuth 2.1 authorization framework enables an application to
   obtain limited access to a protected resource, either on behalf of a
   resource owner by orchestrating an approval interaction between the
   resource owner and an authorization service, or by allowing the
   application to obtain access on its own behalf.  This specification
   replaces and obsoletes the OAuth 2.0 Authorization Framework
   described in RFC 6749 and the Bearer Token Usage in RFC 6750.

### OAuth 2.0 Protected Resource Metadata  (draft-ietf-oauth-resource-metadata)
This specification defines a metadata format that an OAuth 2.0 client
   or authorization server can use to obtain the information needed to
   interact with an OAuth 2.0 protected resource.

### OAuth 2.0 Demonstrating Proof of Possession (DPoP)  (draft-ietf-oauth-dpop)
This document describes a mechanism for sender-constraining OAuth 2.0 tokens via a proof-of-possession mechanism on the application level.  This mechanism allows for the detection of replay attacks with access and refresh tokens.

### The OAuth Protocol: Authentication  (draft-ietf-oauth-authentication)
This document specifies the OAuth protocol authentication method.
OAuth allows clients to access server resources on behalf of another
party (such a different client or an end user).  This document
defines an HTTP authentication method which supports the ability to
include two sets of credential with each request, one identifying the
client and another identifying the resource owner on whose behalf the
request is made.

### The OAuth Protocol: Web Delegation  (draft-ietf-oauth-web-delegation)
This document specifies the OAuth protocol web delegation method.
OAuth allows clients to access server resources on behalf of another
party (such a different client or an end user).  This document
defines a redirection-based user-agent process for end users to
authorize access to clients by substituting their credentials
(typically, a username and password pair) with a different set of
delegation-specific credentials.

### Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants  (draft-ietf-oauth-saml2-bearer)
This specification defines the use of a Security Assertion Markup Language (SAML) 2.0 Bearer Assertion as a means for requesting an OAuth 2.0 access token as well as for client authentication.

### The OAuth 2.0 Authorization Framework: Bearer Token Usage  (draft-ietf-oauth-v2-bearer)
This specification describes how to use bearer tokens in HTTP requests to access OAuth 2.0 protected resources.  Any party in possession of a bearer token (a "bearer") can use it to get access to the associated resources (without demonstrating possession of a cryptographic key).  To prevent misuse, bearer tokens need to be protected from disclosure in storage and in transport. [STANDARDS-TRACK]

### OAuth 2.0 Message Authentication Code (MAC) Tokens  (draft-ietf-oauth-v2-http-mac)
This specification describes how to use MAC Tokens in HTTP requests
   to access OAuth 2.0 protected resources.  An OAuth client willing to
   access a protected resource needs to demonstrate possession of a
   cryptographic key by using it with a keyed message digest function to
   the request.

   The document also defines a key distribution protocol for obtaining a
   fresh session key.

### OAuth 2.0 Threat Model and Security Considerations  (draft-ietf-oauth-v2-threatmodel)
This document gives additional security considerations for OAuth, beyond those in the OAuth 2.0 specification, based on a comprehensive threat model for the OAuth 2.0 protocol.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants  (draft-ietf-oauth-assertions)
This specification provides a framework for the use of assertions with OAuth 2.0 in the form of a new client authentication mechanism and a new authorization grant type. Mechanisms are specified for transporting assertions during interactions with a token endpoint; general processing rules are also specified.

 The intent of this specification is to provide a common framework for OAuth 2.0 to interwork with other identity systems using assertions and to provide alternative client authentication mechanisms.

 Note that this specification only defines abstract message flows and processing rules. In order to be implementable, companion specifications are necessary to provide the corresponding concrete instantiations.

### An IETF URN Sub-Namespace for OAuth  (draft-ietf-oauth-urn-sub-ns)
This document establishes an IETF URN Sub-namespace for use with OAuth-related specifications.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### JSON Web Token (JWT)  (draft-ietf-oauth-json-web-token)
JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.  The claims in a JWT are encoded as a JSON object that is used as the payload of a JSON Web Signature (JWS) structure or as the plaintext of a JSON Web Encryption (JWE) structure, enabling the claims to be digitally signed or integrity protected with a Message Authentication Code (MAC) and/or encrypted.

### JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants  (draft-ietf-oauth-jwt-bearer)
This specification defines the use of a JSON Web Token (JWT) Bearer Token as a means for requesting an OAuth 2.0 access token as well as for client authentication.

### OAuth Use Cases  (draft-ietf-oauth-use-cases)
This document lists the OAuth use cases.  The provided list is based
   on the Internet Drafts of the OAUTH working group and discussions on
   the group's mailing list.

### OAuth 2.0 Token Revocation  (draft-ietf-oauth-revocation)
This document proposes an additional endpoint for OAuth authorization servers, which allows clients to notify the authorization server that a previously obtained refresh or access token is no longer needed.  This allows the authorization server to clean up security credentials.  A revocation request will invalidate the actual token and, if applicable, other tokens based on the same authorization grant.

### OAuth 2.0 Dynamic Client Registration Metadata  (draft-ietf-oauth-dyn-reg-metadata)
This specification is obsolete.  Its previous contents have been
   merged into draft-ietf-oauth-dyn-reg.

### OAuth 2.0 Dynamic Client Registration Management Protocol  (draft-ietf-oauth-dyn-reg-management)
This specification defines methods for management of OAuth 2.0 dynamic client registrations for use cases in which the properties of a registered client may need to be changed during the lifetime of the client.  Not all authorization servers supporting dynamic client registration will support these management methods.

### OAuth 2.0 Proof-of-Possession: Authorization Server to Client Key Distribution  (draft-ietf-oauth-pop-key-distribution)
RFC 6750 specified the bearer token concept for securing access to
   protected resources.  Bearer tokens need to be protected in transit
   as well as at rest.  When a client requests access to a protected
   resource it hands-over the bearer token to the resource server.

   The OAuth 2.0 Proof-of-Possession security concept extends bearer
   token security and requires the client to demonstrate possession of a
   key when accessing a protected resource.

### Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)  (draft-ietf-oauth-proof-of-possession)
This specification describes how to declare in a JSON Web Token (JWT) that the presenter of the JWT possesses a particular proof-of- possession key and how the recipient can cryptographically confirm proof of possession of the key by the presenter.  Being able to prove possession of a key is also sometimes described as the presenter being a holder-of-key.

### A Method for Signing HTTP Requests for OAuth  (draft-ietf-oauth-signed-http-request)
This document a method for offering data origin authentication and
   integrity protection of HTTP requests.  To convey the relevant data
   items in the request a JSON-based encapsulation is used and the JSON
   Web Signature (JWS) technique is re-used.  JWS offers integrity
   protection using symmetric as well as asymmetric cryptography.

### The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)  (draft-ietf-oauth-jwsreq)
The authorization request in OAuth 2.0 described in RFC 6749 utilizes query parameter serialization, which means that authorization request parameters are encoded in the URI of the request and sent through user agents such as web browsers. While it is easy to implement, it means that a) the communication through the user agents is not integrity protected and thus, the parameters can be tainted, b) the source of the communication is not authenticated, and c) the communication through the user agents can be monitored. Because of these weaknesses, several attacks to the protocol have now been put forward.

 This document introduces the ability to send request parameters in a JSON Web Token (JWT) instead, which allows the request to be signed with JSON Web Signature (JWS) and encrypted with JSON Web Encryption (JWE) so that the integrity, source authentication, and confidentiality properties of the authorization request are attained. The request can be sent by value or by reference.

### Proof Key for Code Exchange by OAuth Public Clients  (draft-ietf-oauth-spop)
OAuth 2.0 public clients utilizing the Authorization Code Grant are susceptible to the authorization code interception attack.  This specification describes the attack as well as a technique to mitigate against the threat through the use of Proof Key for Code Exchange (PKCE, pronounced "pixy").

### OAuth 2.0 Token Introspection  (draft-ietf-oauth-introspection)
This specification defines a method for a protected resource to query an OAuth 2.0 authorization server to determine the active state of an OAuth 2.0 token and to determine meta-information about this token.  OAuth 2.0 deployments can use this method to convey information about the authorization context of the token from the authorization server to the protected resource.

### OAuth 2.0 Device Authorization Grant  (draft-ietf-oauth-device-flow)
The OAuth 2.0 device authorization grant is designed for Internet- connected devices that either lack a browser to perform a user-agent- based authorization or are input constrained to the extent that requiring the user to input text in order to authenticate during the authorization flow is impractical.  It enables OAuth clients on such devices (like smart TVs, media consoles, digital picture frames, and printers) to obtain user authorization to access protected resources by using a user agent on a separate device.

### OAuth 2.0 Security: Closing Open Redirectors in OAuth  (draft-ietf-oauth-closing-redirectors)
This document gives additional security considerations for OAuth,
   beyond those in the OAuth 2.0 specification and in the OAuth 2.0
   Threat Model and Security Considerations.

### OAuth 2.0 for Native Apps  (draft-ietf-oauth-native-apps)
OAuth 2.0 authorization requests from native apps should only be made through external user-agents, primarily the user's browser.  This specification details the security and usability reasons why this is the case and how native apps and authorization servers can implement this best practice.

### OAuth 2.0 Authorization Server Metadata  (draft-ietf-oauth-discovery)
This specification defines a metadata format that an OAuth 2.0 client can use to obtain the information needed to interact with an OAuth 2.0 authorization server, including its endpoint locations and authorization server capabilities.

### Authentication Method Reference Values  (draft-ietf-oauth-amr-values)
The "amr" (Authentication Methods References) claim is defined and registered in the IANA "JSON Web Token Claims" registry, but no standard Authentication Method Reference values are currently defined.  This specification establishes a registry for Authentication Method Reference values and defines an initial set of Authentication Method Reference values.

### OAuth 2.0 Mix-Up Mitigation  (draft-ietf-oauth-mix-up-mitigation)
This specification defines an extension to The OAuth 2.0
   Authorization Framework that enables the authorization server to
   dynamically provide the client using it with additional information
   about the current protocol interaction that can be validated by the
   client and that enables the client to dynamically provide the
   authorization server with additional information about the current
   protocol interaction that can be validated by the authorization
   server.  This additional information can be used by the client and
   the authorization server to prevent classes of attacks in which the
   client might otherwise be tricked into using inconsistent sets of
   metadata from multiple authorization servers, including potentially
   using a token endpoint that does not belong to the same authorization
   server as the authorization endpoint used.  Recent research
   publications refer to these as "IdP Mix-Up" and "Malicious Endpoint"
   attacks.

### OAuth 2.0 Token Binding  (draft-ietf-oauth-token-binding)
This specification enables OAuth 2.0 implementations to apply Token
   Binding to Access Tokens, Authorization Codes, Refresh Tokens, JWT
   Authorization Grants, and JWT Client Authentication.  This
   cryptographically binds these tokens to a client's Token Binding key
   pair, possession of which is proven on the TLS connections over which
   the tokens are intended to be used.  This use of Token Binding
   protects these tokens from man-in-the-middle and token export and
   replay attacks.

### Distributed OAuth  (draft-ietf-oauth-distributed)
The Distributed OAuth profile enables an OAuth client to discover
   what authorization server or servers may be used to obtain access
   tokens for a given resource, and what parameter values to provide in
   the access token request.

### OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens  (draft-ietf-oauth-mtls)
This document describes OAuth client authentication and certificate-bound access and refresh tokens using mutual Transport Layer Security (TLS) authentication with X.509 certificates.  OAuth clients are provided a mechanism for authentication to the authorization server using mutual TLS, based on either self-signed certificates or public key infrastructure (PKI).  OAuth authorization servers are provided a mechanism for binding access tokens to a client's mutual-TLS certificate, and OAuth protected resources are provided a method for ensuring that such an access token presented to it was issued to the client presenting the token.

### JSON Web Token Best Current Practices  (draft-ietf-oauth-jwt-bcp)
JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security tokens that contain a set of claims that can be signed and/or encrypted.  JWTs are being widely used and deployed as a simple security token format in numerous protocols and applications, both in the area of digital identity and in other application areas.  This Best Current Practices document updates RFC 7519 to provide actionable guidance leading to secure implementation and deployment of JWTs.

### Reciprocal OAuth  (draft-ietf-oauth-reciprocal)
There are times when a user has a pair of protected resources that
   would like to request access to each other.  While OAuth flows
   typically enable the user to grant a client access to a protected
   resource, granting the inverse access requires an additional flow.
   Reciprocal OAuth enables a more seamless experience for the user to
   grant access to a pair of protected resources.

### OAuth 2.0 Incremental Authorization  (draft-ietf-oauth-incremental-authz)
OAuth 2.0 authorization requests that include every scope the client
   might ever need can result in over-scoped authorization and a sub-
   optimal end-user consent experience.  This specification enhances the
   OAuth 2.0 authorization protocol by adding incremental authorization,
   the ability to request specific authorization scopes as needed, when
   they're needed, removing the requirement to request every possible
   scope that might be needed upfront.

### Resource Indicators for OAuth 2.0  (draft-ietf-oauth-resource-indicators)
This document specifies an extension to the OAuth 2.0 Authorization Framework defining request parameters that enable a client to explicitly signal to an authorization server about the identity of the protected resource(s) to which it is requesting access.

### JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens  (draft-ietf-oauth-access-token-jwt)
This specification defines a profile for issuing OAuth 2.0 access tokens in JSON Web Token (JWT) format.  Authorization servers and resource servers from different vendors can leverage this profile to issue and consume access tokens in an interoperable manner.

### OAuth 2.0 Pushed Authorization Requests  (draft-ietf-oauth-par)
This document defines the pushed authorization request (PAR) endpoint, which allows clients to push the payload of an OAuth 2.0 authorization request to the authorization server via a direct request and provides them with a request URI that is used as reference to the data in a subsequent call to the authorization endpoint.

### OAuth 2.0 Rich Authorization Requests  (draft-ietf-oauth-rar)
This document specifies a new parameter that is used to carry fine-grained authorization data in OAuth messages.

### OAuth 2.0 Authorization Server Issuer Identification  (draft-ietf-oauth-iss-auth-resp)
This document specifies a new parameter called iss.  This parameter is used to explicitly include the issuer identifier of the authorization server in the authorization response of an OAuth authorization flow.  The iss parameter serves as an effective countermeasure to "mix-up attacks".

### JWK Thumbprint URI  (draft-ietf-oauth-jwk-thumbprint-uri)
This specification registers a kind of URI that represents a JSON Web Key (JWK) Thumbprint value.  JWK Thumbprints are defined in RFC 7638.  This enables JWK Thumbprints to be used, for instance, as key identifiers in contexts requiring URIs.

### OAuth 2.0 Step Up Authentication Challenge Protocol  (draft-ietf-oauth-step-up-authn-challenge)
It is not uncommon for resource servers to require different authentication strengths or recentness according to the characteristics of a request.  This document introduces a mechanism that resource servers can use to signal to a client that the authentication event associated with the access token of the current request does not meet its authentication requirements and, further, how to meet them.  This document also codifies a mechanism for a client to request that an authorization server achieve a specific authentication strength or recentness when processing an authorization request.

### OAuth 2.0 Security Best Current Practice  (draft-ietf-oauth-security-topics)
This document describes best current security practice for OAuth 2.0.
   It updates and extends the threat model and security advice given in
   RFC 6749, RFC 6750, and RFC 6819 to incorporate practical experiences
   gathered since OAuth 2.0 was published and covers new threats
   relevant due to the broader application of OAuth 2.0.  Further, it
   deprecates some modes of operation that are deemed less secure or
   even insecure.

### Transaction Tokens  (draft-ietf-oauth-transaction-tokens)
Transaction Tokens (Txn-Tokens) are designed to maintain and
   propagate user identity, workload identity and authorization context
   throughout the Call Chain within a trusted domain during the
   processing of external requests (e.g. such as API calls) or requests
   initiated internally within the trust domain.  Txn-Tokens ensure that
   this context is preserved throughout the Call Chain thereby enhancing
   security and consistency in complex, multi-service architectures.

### Selective Disclosure for JWTs (SD-JWT)  (draft-ietf-oauth-selective-disclosure-jwt)
This specification defines a mechanism for the selective disclosure
   of individual elements of a JSON data structure used as the payload
   of a JSON Web Signature (JWS).  The primary use case is the selective
   disclosure of JSON Web Token (JWT) claims.

### OAuth 2.0 Proof-of-Possession (PoP) Security Architecture  (draft-ietf-oauth-pop-architecture)
The OAuth 2.0 bearer token specification, as defined in RFC 6750,
   allows any party in possession of a bearer token (a "bearer") to get
   access to the associated resources (without demonstrating possession
   of a cryptographic key).  To prevent misuse, bearer tokens must be
   protected from disclosure in transit and at rest.

   Some scenarios demand additional security protection whereby a client
   needs to demonstrate possession of cryptographic keying material when
   accessing a protected resource.  This document motivates the
   development of the OAuth 2.0 proof-of-possession security mechanism.

### The OAuth 2.0 Authorization Framework  (draft-ietf-oauth-v2)
The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.  This specification replaces and obsoletes the OAuth 1.0 protocol described in RFC 5849. [STANDARDS-TRACK]

### OAuth 2.0 Refresh Token and Authorization Expiration  (draft-watson-oauth-refresh-token-expiration)
This specification extends OAuth 2.0 [RFC6749] by adding new token
   endpoint response parameters to specify refresh token expiration and
   user authorization expiration.

### Token Status List (TSL)  (draft-ietf-oauth-status-list)
This specification defines a status mechanism called Token Status
   List (TSL), data structures and processing rules for representing the
   status of tokens secured by JSON Object Signing and Encryption (JOSE)
   or CBOR Object Signing and Encryption (COSE), such as JWT, SD-JWT,
   CBOR Web Token, and ISO mdoc.  It also defines an extension point and
   a registry for future status mechanisms.

### Identity Assertion Authorization Grant  (draft-parecki-oauth-identity-assertion-authz-grant)
This specification provides a mechanism for an application to use an
   identity assertion to obtain an access token for a third-party API by
   coordinating through a common enterprise identity provider using
   Token Exchange [RFC8693] and JWT Profile for OAuth 2.0 Authorization
   Grants [RFC7523].

### OAuth Identity and Authorization Chaining Across Domains  (draft-ietf-oauth-identity-chaining)
This specification describes a mechanism for preserving identity and
   authorization information across trust domains that use the OAuth 2.0
   Framework.  A JSON Web Token (JWT) authorization grant, obtained
   through an intra-domain OAuth 2.0 Token Exchange, facilitates the
   cross-domain acquisition of an access token.  The relevant identity
   and authorization information is chained throughout the flow by being
   conveyed in the respective artifacts exchanged at each step of the
   process.  Chaining across multiple domains is achieved by using the
   same protocol every time a trust domain boundary is crossed.

### JSON Web Token Best Current Practices  (draft-ietf-oauth-rfc8725bis)
JSON Web Tokens, also known as JWTs, are URL-safe JSON-based security
   tokens that contain a set of claims that can be signed and/or
   encrypted.  JWTs are being widely used and deployed as a simple
   security token format in numerous protocols and applications, both in
   the area of digital identity and in other application areas.  This
   Best Current Practices (BCP) specification updates RFC 7519 to
   provide actionable guidance leading to secure implementation and
   deployment of JWTs.

   This BCP specification furthermore replaces the existing JWT BCP
   specification RFC 8725 to provide additional actionable guidance
   covering threats and attacks that have been discovered since RFC 8725
   was published.

### Cross-Device Flows: Security Best Current Practice  (draft-ietf-oauth-cross-device-security)
This document describes threats against cross-device flows along with
   practical mitigations, protocol selection guidance, and a summary of
   formal analysis results identified as relevant to the security of
   cross-device flows.  It serves as a security guide to system
   designers, architects, product managers, security specialists, fraud
   analysts and engineers implementing cross-device flows.

### Identity Assertion JWT Authorization Grant  (draft-ietf-oauth-identity-assertion-authz-grant)
This specification provides a mechanism for an application to use an
   identity assertion to obtain an access token for a third-party API by
   coordinating through an identity provider that the downstream
   Resource Authorization Server already trusts for single sign-on
   (SSO), using Token Exchange [RFC8693] and JWT Profile for OAuth 2.0
   Authorization Grants [RFC7523].  This pattern is informally referred
   to as Cross-App Access (XAA).

### OAuth 2.0 Attestation-Based Client Authentication  (draft-ietf-oauth-attestation-based-client-auth)
This specification defines an extension to the OAuth 2.0 protocol
   [RFC6749] that enables a client instance to include a key-bound
   attestation when interacting with an Authorization Server or Resource
   Server.  This mechanism allows a client instance to prove its
   authenticity verified by a client attester without revealing its
   target audience to that attester.  It may also serve as a mechanism
   for client authentication as per OAuth 2.0.

### SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)  (draft-ietf-oauth-sd-jwt-vc)
This specification describes data formats as well as validation and
   processing rules to express Verifiable Digital Credentials with JSON
   payloads with and without selective disclosure based on the SD-JWT
   format.

### OAuth Client ID Metadata Document  (draft-parecki-oauth-client-id-metadata-document)
This specification defines a mechanism through which an OAuth client
   can identify itself to authorization servers, without prior dynamic
   client registration or other existing registration.  This is through
   the usage of a URL as a client_id in an OAuth flow, where the URL
   refers to a document containing the necessary client metadata,
   enabling the authorization server to fetch the metadata about the
   client as needed.

## Working Group: pquip
### Hash-based Signatures: State and Backup Management  (draft-wiggers-hbs-state)
Stateful Hash-Based Signature Schemes (S-HBS) such as LMS, HSS, XMSS
   and XMSS^MT combine Merkle trees with One-Time Signatures (OTS) to
   provide signatures that are resistant against attacks using large-
   scale quantum computers.  Unlike conventional stateless digital
   signature schemes, S-HBS have a state to keep track of which OTS keys
   have been used, as double-signing with the same OTS key allows
   forgeries.

   This document provides guidance and documents security considerations
   for the operational and technical aspects of deploying systems that
   rely on S-HBS.  Management of the state of the S-HBS, including any
   handling of redundant key material, is a sensitive topic, and we
   discuss some approaches to handle the associated challenges.  We also
   describe the challenges that need to be resolved before certain
   approaches should be considered.

### Terminology for Post-Quantum Traditional Hybrid Schemes  (draft-ietf-pquip-pqt-hybrid-terminology)
One aspect of the transition to post-quantum algorithms in
   cryptographic protocols is the development of hybrid schemes that
   incorporate both post-quantum and traditional asymmetric algorithms.
   This document defines terminology for such schemes.  It is intended
   to be used as a reference and, hopefully, to ensure consistency and
   clarity across different protocols, standards, and organisations.

### Hybrid signature spectrums  (draft-ietf-pquip-hybrid-signature-spectrums)
This document describes classification of design goals and security
   considerations for hybrid digital signature schemes, including proof
   composability, non-separability of the component signatures given a
   hybrid signature, backwards/forwards compatibility, hybrid
   generality, and simultaneous verification.

### Post-Quantum Cryptography for Engineers  (draft-ietf-pquip-pqc-engineers)
The advent of a cryptographically relevant quantum computer (CRQC)
   would render state-of-the-art, traditional public key algorithms
   deployed today obsolete, as the mathematical assumptions underpinning
   their security would no longer hold.  To address this, protocols and
   infrastructure must transition to post-quantum algorithms, which are
   designed to resist both traditional and quantum attacks.  This
   document explains why engineers need to be aware of and understand
   post-quantum cryptography (PQC), detailing the impact of CRQCs on
   existing systems and the challenges involved in transitioning to
   post-quantum algorithms.  Unlike previous cryptographic updates, this
   shift may require significant protocol redesign due to the unique
   properties of post-quantum algorithms.

### Hash-based Signatures: State and Backup Management  (draft-ietf-pquip-hbs-state)
Stateful Hash-Based Signature Schemes (Stateful HBS) such as
   Leighton-Micali Signature (LMS), Hierarchical Signature System (HSS),
   eXtended Merkle Signature Scheme (XMSS), and XMSS^MT combine Merkle
   trees with One-Time Signatures (OTS) to provide signatures that are
   resistant against attacks using large-scale quantum computers.
   Unlike conventional stateless digital signature schemes, Stateful HBS
   have a state to keep track of which OTS keys have been used, as
   double-signing with the same OTS key allows forgeries.

   This document provides guidance and catalogs security considerations
   for the operational and technical aspects of deploying systems that
   rely on Stateful HBS.  Management of the state of the Stateful HBS,
   including any handling of redundant key material, is a sensitive
   topic.  This document describes some approaches to handle the
   associated challenges.  It also describes the challenges that need to
   be resolved before certain approaches should be considered.

### Adapting Constrained Devices for Post-Quantum Cryptography  (draft-ietf-pquip-pqc-hsm-constrained)
This document provides guidance on integrating Post-Quantum
   Cryptography (PQC) into resource-constrained devices, such as IoT
   nodes and lightweight Hardware Security Modules (HSMs).  These
   systems often operate with strict limitations on processing power,
   RAM, and flash memory, and may even be battery-powered.  The document
   emphasizes the role of hardware security as the basis for secure
   operations, supporting features such as seed-based key generation to
   minimize persistent storage, efficient handling of ephemeral keys,
   and the offloading of cryptographic tasks in low-resource
   environments.  It also explores the implications of PQC on firmware
   update mechanisms in such constrained systems.

## Working Group: quic
### QMux  (draft-opik-quic-qmux)
This document specifies QMux version 1.  QMux version 1 provides,
   over bi-directional streams such as TLS, the same set of stream and
   datagram operations that applications rely upon in QUIC version 1.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the QUIC Working Group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/quic/.

   Source for this draft and an issue tracker can be found at
   https://github.com/kazuho/draft-opik-quic-qmux.

### QUIC Address Discovery  (draft-seemann-quic-address-discovery)
Unless they have out-of-band knowledge, QUIC endpoints have no
   information about their network situation.  They neither know their
   external IP address and port, nor do they know if they are directly
   connected to the internet or if they are behind a NAT.  This QUIC
   extension allows nodes to determine their public IP address and port
   for any QUIC path.

### QUIC Address Discovery  (draft-ietf-quic-address-discovery)
Unless they have out-of-band knowledge, QUIC endpoints have no
   information about their network situation.  They neither know their
   external IP address and port, nor do they know if they are directly
   connected to the internet or if they are behind a NAT.  This QUIC
   extension allows nodes to determine their public IP address and port
   for any QUIC path.

### Compatible Version Negotiation for QUIC  (draft-ietf-quic-version-negotiation)
QUIC does not provide a complete version negotiation mechanism but instead only provides a way for the server to indicate that the version the client chose is unacceptable.  This document describes a version negotiation mechanism that allows a client and server to select a mutually supported version.  Optionally, if the client's chosen version and the negotiated version share a compatible first flight format, the negotiation can take place without incurring an extra round trip.  This document updates RFC 8999.

### QUIC Version 2  (draft-ietf-quic-v2)
This document specifies QUIC version 2, which is identical to QUIC version 1 except for some trivial details. Its purpose is to combat various ossification vectors and exercise the version negotiation framework. It also serves as a template for the minimum changes in any future version of QUIC.

 Note that "version 2" is an informal name for this proposal that indicates it is the second version of QUIC to be published as a Standards Track document. The protocol specified here uses a version number other than 2 in the wire image, in order to minimize ossification risks.

### QUIC Loss Detection and Congestion Control  (draft-ietf-quic-recovery)
This document describes loss detection and congestion control mechanisms for QUIC.

### Using Transport Layer Security (TLS) to Secure QUIC  (draft-thomson-quic-tls)
This document describes how Transport Layer Security (TLS) can be
   used to secure QUIC.

### QUIC: A UDP-Based Multiplexed and Secure Transport  (draft-hamilton-quic-transport-protocol)
QUIC is a multiplexed and secure transport protocol that runs on top
   of UDP.  QUIC builds on past transport experience, and implements
   mechanisms that make it useful as a modern general-purpose transport
   protocol.  Using UDP as the basis of QUIC is intended to address
   compatibility issues with legacy clients and middleboxes.  QUIC
   authenticates all of its headers, preventing third parties from from
   changing them.  QUIC encrypts most of its headers, thereby limiting
   protocol evolution to QUIC endpoints only.  Therefore, middleboxes,
   in large part, are not required to be updated as new protocol
   versions are deployed.  This document describes the core QUIC
   protocol, including the conceptual design, wire format, and
   mechanisms of the QUIC protocol for connection establishment, stream
   multiplexing, stream and connection-level flow control, and data
   reliability.  Accompanying documents describe QUIC's loss recovery
   and congestion control, and the use of TLS 1.3 for key negotiation.

### QUIC Congestion Control And Loss Recovery  (draft-iyengar-quic-loss-recovery)
QUIC is a new multiplexed and secure transport atop UDP.  QUIC builds
   on decades of transport and security experience, and implements
   mechanisms that make it attractive as a modern general-purpose
   transport.  QUIC implements the spirit of known TCP loss detection
   mechanisms, described in RFCs, various Internet-drafts, and also
   those prevalent in the Linux TCP implementation.  This document
   describes QUIC loss detection and congestion control, and attributes
   the TCP equivalent in RFCs, Internet-drafts, academic papers, and TCP
   implementations.

### HTTP/2 Semantics Using The QUIC Transport Protocol  (draft-shade-quic-http2-mapping)
The QUIC transport protocol has several features that are desirable
   in a transport for HTTP/2, such as stream multiplexing, per-stream
   flow control, and low-latency connection establishment.  This
   document describes a mapping of HTTP/2 semantics over QUIC.
   Specifically, this document identifies HTTP/2 features that are
   subsumed by QUIC, and describes how the other features can be
   implemented atop QUIC.

### HTTP/3  (draft-ietf-quic-http)
The QUIC transport protocol has several features that are desirable in a transport for HTTP, such as stream multiplexing, per-stream flow control, and low-latency connection establishment.  This document describes a mapping of HTTP semantics over QUIC.  This document also identifies HTTP/2 features that are subsumed by QUIC and describes how HTTP/2 extensions can be ported to HTTP/3.

### QUIC: A UDP-Based Multiplexed and Secure Transport  (draft-ietf-quic-transport)
This document defines the core of the QUIC transport protocol.  QUIC provides applications with flow-controlled streams for structured communication, low-latency connection establishment, and network path migration.  QUIC includes security measures that ensure confidentiality, integrity, and availability in a range of deployment circumstances.  Accompanying documents describe the integration of TLS for key negotiation, loss detection, and an exemplary congestion control algorithm.

### Using TLS to Secure QUIC  (draft-ietf-quic-tls)
This document describes how Transport Layer Security (TLS) is used to secure QUIC.

### Applicability of the QUIC Transport Protocol  (draft-kuehlewind-quic-applicability)
This document discusses the applicability of the QUIC transport
   protocol, focusing on caveats impacting application protocol
   development and deployment over QUIC.  Its intended audience is
   designers of application protocol mappings to QUIC, and implementors
   of these application protocols.

### Manageability of the QUIC Transport Protocol  (draft-kuehlewind-quic-manageability)
This document discusses manageability of the QUIC transport protocol,
   focusing on caveats impacting network operations involving QUIC
   traffic.  Its intended audience is network operators, as well as
   content providers that rely on the use of QUIC-aware middleboxes,
   e.g. for load balancing.

### Header Compression for HTTP over QUIC  (draft-krasic-quic-qcram)
The design of the core QUIC transport subsumes many HTTP/2 features,
   prominent among them stream multiplexing.  A key advantage of the
   QUIC transport is stream multiplexing free of head-of-line (HoL)
   blocking between streams.  In HTTP/2, multiplexed streams can suffer
   HoL blocking due to TCP.

   If HTTP/2's HPACK is used for header compression, HTTP/QUIC is still
   vulnerable to HoL blocking, because of HPACK's assumption of in-order
   delivery.  This draft defines QCRAM, a variation of HPACK and
   mechanisms in the HTTP/QUIC mapping that allow the flexibility to
   avoid header-compression-induced HoL blocking.

### QPACK: Field Compression for HTTP/3  (draft-ietf-quic-qpack)
This specification defines QPACK: a compression format for efficiently representing HTTP fields that is to be used in HTTP/3.  This is a variation of HPACK compression that seeks to reduce head-of-line blocking.

### Version-Independent Properties of QUIC  (draft-ietf-quic-invariants)
This document defines the properties of the QUIC transport protocol that are common to all versions of the protocol.

### Applicability of the QUIC Transport Protocol  (draft-ietf-quic-applicability)
This document discusses the applicability of the QUIC transport protocol, focusing on caveats impacting application protocol development and deployment over QUIC.  Its intended audience is designers of application protocol mappings to QUIC and implementors of these application protocols.

### Manageability of the QUIC Transport Protocol  (draft-ietf-quic-manageability)
This document discusses manageability of the QUIC transport protocol and focuses on the implications of QUIC's design and wire image on network operations involving QUIC traffic.  It is intended as a "user's manual" for the wire image to provide guidance for network operators and equipment vendors who rely on the use of transport-aware network functions.

### Version-Independent Properties of QUIC  (draft-thomson-quic-invariants)
This document defines the properties of the QUIC transport protocol
   that are expected to remain unchanged over time as new versions of
   the protocol are developed.

Note to Readers

   Discussion of this draft takes place on the QUIC working group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/search/?email_list=quic [1].

   Working Group information can be found at https://github.com/quicwg
   [2]; source code and issues list for this draft can be found at
   https://github.com/quicwg/base-drafts/labels/-invariants [3].

### QUIC-LB: Generating Routable QUIC Connection IDs  (draft-duke-quic-load-balancers)
QUIC connection IDs allow continuation of connections across address/
   port 4-tuple changes, and can store routing information for stateless
   or low-state load balancers.  They also can prevent linkability of
   connections across deliberate address migration through the use of
   protected communications between client and server.  This creates
   issues for load-balancing intermediaries.  This specification
   standardizes methods for encoding routing information and proposes an
   optional protocol called QUIC-LB to exchange the parameters of that
   encoding.  This framework also enables offload of other QUIC
   functions to trusted intermediaries, given the explicit cooperation
   of the QUIC server.

### Header Compression for HTTP over QUIC  (draft-ietf-quic-qcram)
The design of the core QUIC transport subsumes many HTTP/2 features,
   prominent among them stream multiplexing.  A key advantage of the
   QUIC transport is stream multiplexing free of head-of-line (HoL)
   blocking between streams.  In HTTP/2, multiplexed streams can suffer
   HoL blocking due to TCP.

   If HTTP/2's HPACK is used for header compression, HTTP/QUIC is still
   vulnerable to HoL blocking, because of HPACK's assumption of in-order
   delivery.  This draft defines QCRAM, a variation of HPACK and
   mechanisms in the HTTP/QUIC mapping that allow the flexibility to
   avoid header-compression-induced HoL blocking.

### The QUIC Latency Spin Bit  (draft-ietf-quic-spin-exp)
This document specifies the addition of a latency spin bit to the
   QUIC transport protocol and describes how to use it to measure end-
   to-end latency.

Note to Readers

   This document specifies an experimental delta to the QUIC transport
   protocol.  Specifically, this experimentation is intended to
   determine:

   o  the impact of the addition of the latency spin bit on
      implementation and specification complexity; and

   o  the accuracy and value of the information derived from spin bit
      measurement on live network traffic.

   The information generated by this experiment will be used by the QUIC
   working group as input to a decision about the standardization of the
   latency spin bit.  Although this is a Working Group document, it is
   currently NOT a Working Group deliverable.

   Discussion of this draft takes place on the QUIC working group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/search/?email_list=quic [1].

   Working Group information can be found at https://github.com/quicwg
   [2]; source code and issues list for this draft can be found at
   https://github.com/quicwg/base-drafts/labels/-spin [3].

### An Unreliable Datagram Extension to QUIC  (draft-pauly-quic-datagram)
This document defines an extension to the QUIC transport protocol to
   add support for sending and receiving unreliable datagrams over a
   QUIC connection.

   Discussion of this work is encouraged to happen on the QUIC IETF
   mailing list quic@ietf.org [1] or on the GitHub repository which
   contains the draft: https://github.com/tfpauly/draft-pauly-quic-
   datagram [2].

### Compatible Version Negotiation for QUIC  (draft-schinazi-quic-version-negotiation)
QUIC does not provide a complete version negotiation mechanism but
   instead only provides a way for the server to indicate that the
   version the client offered is unacceptable.  This document describes
   a version negotiation mechanism that allows a client and server to
   select a mutually supported version.  Optionally, if the original and
   negotiated version share a compatible Initial format, the negotiation
   can take place without incurring an extra round trip.

   Discussion of this work is encouraged to happen on the QUIC IETF
   mailing list quic@ietf.org [1] or on the GitHub repository which
   contains the draft: http://github.com/ekr/draft-schinazi-quic-
   version-negotiation [2].

### Main logging schema for qlog  (draft-marx-qlog-main-schema)
This document describes a high-level schema for a standardized
   logging format called qlog.  This format allows easy sharing of data
   and the creation of reusable visualization and debugging tools.  The
   high-level schema in this document is intended to be protocol-
   agnostic.  Separate documents specify how the format should be used
   for specific protocol data.  The schema is also format-agnostic, and
   can be represented in for example JSON, csv or protobuf.

### QUIC and HTTP/3 event definitions for qlog  (draft-marx-qlog-event-definitions-quic-h3)
This document describes concrete qlog event definitions and their
   metadata for QUIC and HTTP/3-related events.  These events can then
   be embedded in the higher level schema defined in [QLOG-MAIN].

### Sender Control of Acknowledgement Delays in QUIC  (draft-iyengar-quic-delayed-ack)
This document describes a QUIC extension for an endpoint to control
   its peer's delaying of acknowledgements.

Note to Readers

   Discussion of this draft takes place on the QUIC working group
   mailing list (quic@ietf.org), which is archived at
   <https://mailarchive.ietf.org/arch/search/?email_list=quic>.

   Working Group information can be found at <https://github.com/
   quicwg>; source code and issues list for this draft can be found at
   <https://github.com/quicwg/base-drafts/labels/-transport>.

### An Unreliable Datagram Extension to QUIC  (draft-ietf-quic-datagram)
This document defines an extension to the QUIC transport protocol to add support for sending and receiving unreliable datagrams over a QUIC connection.

### QUIC Version Aliasing  (draft-ietf-quic-version-aliasing)
The QUIC transport protocol [QUIC-TRANSPORT] preserves its future
   extensibility partly by specifying its version number.  There will be
   a relatively small number of published version numbers for the
   foreseeable future.  This document provides a method for clients and
   servers to negotiate the use of other version numbers in subsequent
   connections.  If a sizeable subset of QUIC connections use this
   mechanism, this should prevent middlebox ossification around the
   current set of published version numbers and the contents of QUIC
   Initial packets.

### Greasing the QUIC Bit  (draft-thomson-quic-bit-grease)
This document describes a method for negotiating the ability to send
   an arbitrary value for the second-to-most significant bit in QUIC
   packets.

### QUIC Version 2  (draft-duke-quic-v2)
This document specifies QUIC version 2, which is identical to QUIC
   version 1 except for some trivial details.  Its purpose is to combat
   various ossification vectors and exercise the version negotiation
   framework.  Over time, it may also serve as a vehicle for needed
   protocol design changes.

   Discussion of this work is encouraged to happen on the QUIC IETF
   mailing list quic@ietf.org or on the GitHub repository which contains
   the draft: https://github.com/martinduke/draft-duke-quic-v2.

### Greasing the QUIC Bit  (draft-ietf-quic-bit-grease)
This document describes a method for negotiating the ability to send an arbitrary value for the second-most significant bit in QUIC packets.

### QUIC event definitions for qlog  (draft-marx-quic-qlog-quic-events)
This document describes concrete qlog event definitions and their
   metadata for QUIC events.  These events can then be embedded in the
   higher level schema defined in [QLOG-MAIN].

### HTTP/3 and QPACK event definitions for qlog  (draft-marx-quic-qlog-h3-events)
This document describes concrete qlog event definitions and their
   metadata for HTTP/3 and QPACK-related events.  These events can then
   be embedded in the higher level schema defined in [QLOG-MAIN].

### Multipath Extension for QUIC  (draft-lmbdhk-quic-multipath)
This document specifies a multipath extension for the QUIC protocol
   to enable the simultaneous usage of multiple paths for a single
   connection.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the QUIC Working Group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/quic/.

   Source for this draft and an issue tracker can be found at
   https://github.com/mirjak/draft-lmbdhk-quic-multipath.

### QUIC Retry Offload  (draft-duke-quic-retry-offload)
QUIC uses Retry packets to reduce load on stressed servers, by
   forcing the client to prove ownership of its address before the
   server commits state.  QUIC also has an anti-tampering mechanism to
   prevent the unauthorized injection of Retry packets into a
   connection.  However, a server operator may want to offload
   production of Retry packets to an anti-Denial-of-Service agent or
   hardware accelerator.  "Retry Offload" is a mechanism for
   coordination between a server and an external generator of Retry
   packets that can succeed despite the anti-tampering mechanism.

### QUIC Retry Offload  (draft-ietf-quic-retry-offload)
QUIC uses Retry packets to reduce load on stressed servers, by
   forcing the client to prove ownership of its address before the
   server commits state.  QUIC also has an anti-tampering mechanism to
   prevent the unauthorized injection of Retry packets into a
   connection.  However, a server operator may want to offload
   production of Retry packets to an anti-Denial-of-Service agent or
   hardware accelerator.  "Retry Offload" is a mechanism for
   coordination between a server and an external generator of Retry
   packets that can succeed despite the anti-tampering mechanism.

### QUIC event definitions for qlog  (draft-ietf-quic-qlog-quic-events)
This document describes a qlog event schema containing concrete qlog
   event definitions and their metadata for the core QUIC protocol and
   selected extensions.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.

### Extended Key Update for QUIC  (draft-ietf-quic-extended-key-update)
This document specifies an Extended Key Update mechanism for the QUIC
   protocol, building on the foundation of the TLS Extended Key Update.
   The TLS Extended Key Update specification enhances the TLS protocol
   by introducing key updates with forward secrecy, eliminating the need
   to perform a full handshake.  This feature is particularly beneficial
   for maintaining security in scenarios involving long-lived
   connections.

   This specification replaces the QUIC Key Update mechanism described
   in the "Using TLS to Secure QUIC" specification.

### QUIC-LB: Generating Routable QUIC Connection IDs  (draft-ietf-quic-load-balancers)
QUIC address migration allows clients to change their IP address
   while maintaining connection state.  To reduce the ability of an
   observer to link two IP addresses, clients and servers use new
   connection IDs when they communicate via different client addresses.
   This poses a problem for traditional "layer-4" load balancers that
   route packets via the IP address and port 4-tuple.  This
   specification provides a standardized means of securely encoding
   routing information in the server's connection IDs so that a properly
   configured load balancer can route packets with migrated addresses
   correctly.  As it proposes a structured connection ID format, it also
   provides a means of connection IDs self-encoding their length to aid
   some hardware offloads.

### QMux  (draft-ietf-quic-qmux)
This document specifies QMux version 1.  QMux version 1 provides,
   over bi-directional streams such as TLS, the same set of stream and
   datagram operations that applications rely upon in QUIC version 1.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Discussion of this document takes place on the QUIC Working Group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/browse/quic/.

   Source for this draft and an issue tracker can be found at
   https://github.com/quicwg/qmux.

### qlog: Structured Logging for Network Protocols  (draft-ietf-quic-qlog-main-schema)
qlog provides extensible structured logging for network protocols,
   allowing for easy sharing of data that benefits common debug and
   analysis methods and tooling.  This document describes key concepts
   of qlog: formats, files, traces, events, and extension points.  This
   definition includes the high-level log file schemas, and generic
   event schemas.  Requirements and guidelines for creating protocol-
   specific event schemas are also presented.  All schemas are defined
   independent of serialization format, allowing logs to be represented
   in various ways such as JSON, CSV, or protobuf.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.

### HTTP/3 qlog event definitions  (draft-ietf-quic-qlog-h3-events)
This document defines a qlog event schema containing concrete events
   for the core HTTP/3 protocol and selected extensions.

Note to Readers

      Note to RFC editor: Please remove this section before publication.

   Feedback and discussion are welcome at https://github.com/quicwg/qlog
   (https://github.com/quicwg/qlog).  Readers are advised to refer to
   the "editor's draft" at that URL for an up-to-date version of this
   document.

### QUIC Acknowledgment Frequency  (draft-ietf-quic-ack-frequency)
This document specifies an extension to QUIC that enables an endpoint
   to request its peer change its behavior when sending or delaying
   acknowledgments.

Note to Readers

   Discussion of this draft takes place on the QUIC working group
   mailing list (quic@ietf.org), which is archived at
   https://mailarchive.ietf.org/arch/search/?email_list=quic.  Source
   code and issues list for this draft can be found at
   https://github.com/quicwg/ack-frequency.

   Working Group information can be found at https://github.com/quicwg.

### Managing multiple paths for a QUIC connection  (draft-ietf-quic-multipath)
This document specifies a multipath extension for the QUIC protocol
   to enable the simultaneous usage of multiple paths for a single
   connection.  It introduces explicit path identifiers to create,
   delete, and manage multiple paths.  This document does not specify
   address discovery or management, nor how applications using QUIC
   schedule traffic over multiple paths.

### QUIC Extended Acknowledgement for Reporting Packet Receive Timestamps  (draft-ietf-quic-receive-ts)
This document defines an extension to the QUIC transport protocol
   which supports reporting multiple packet receive timestamps for post-
   handshake packets.

### QUIC Stream Resets with Partial Delivery  (draft-ietf-quic-reliable-stream-reset)
QUIC defines a RESET_STREAM frame to abort sending on a stream.  When
   a sender resets a stream, it also stops retransmitting STREAM frames
   for this stream in the event of packet loss.  On the receiving side,
   there is no guarantee that any data sent on that stream is delivered.

   This document defines a new QUIC frame, the RESET_STREAM_AT frame,
   that allows resetting a stream, while guaranteeing delivery of stream
   data up to a certain byte offset.

## Working Group: rats
### EAT Measured Component  (draft-fft-rats-eat-measured-component)
A measured component is a measurable object of an attester's target
   environment, that is, an object whose state can be sampled and
   digested.  Examples of measured components include the invariant part
   of firmware that is loaded in memory at startup time, a run-time
   integrity check, a file system object, or a CPU register.

   This document defines a "measured component" format that can be used
   with the EAT Measurements claim.

### Concise TA Stores (CoTS)  (draft-ietf-rats-concise-ta-stores)
Trust anchor (TA) stores may be used for several purposes in the
   Remote Attestation Procedures (RATS) architecture including verifying
   endorsements, reference values, digital letters of approval,
   attestations, or public key certificates.  This document describes a
   Concise Reference Integrity Manifest (CoRIM) extension that may be
   used to convey optionally constrained trust anchor stores containing
   optionally constrained trust anchors in support of these purposes.

### Remote ATtestation procedureS (RATS) Architecture  (draft-ietf-rats-architecture)
In network protocol exchanges, it is often useful for one end of a communication to know whether the other end is in an intended operating state.  This document provides an architectural overview of the entities involved that make such tests possible through the process of generating, conveying, and evaluating evidentiary Claims.  It provides a model that is neutral toward processor architectures, the content of Claims, and protocols.

### TPM-based Network Device Remote Integrity Verification  (draft-ietf-rats-tpm-based-network-device-attest)
This document describes a workflow for remote attestation of the
   integrity of firmware and software installed on network devices that
   contain Trusted Platform Modules [TPM1.2], [TPM2.0], as defined by
   the Trusted Computing Group (TCG)), or equivalent hardware
   implementations that include the protected capabilities, as provided
   by TPMs.

### Concise Reference Integrity Manifest  (draft-birkholz-rats-corim)
Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester and therefore to decide
   whether to engage in secure interactions with it.  Evidence about
   trustworthiness can be rather complex and it is deemed unrealistic
   that every Relying Party is capable of the appraisal of Evidence.
   Therefore that burden is typically offloaded to a Verifier.  In order
   to conduct Evidence appraisal, a Verifier requires not only fresh
   Evidence from an Attester, but also trusted Endorsements and
   Reference Values from Endorsers and Reference Value Providers, such
   as manufacturers, distributors, or device owners.  This document
   specifies Concise Reference Integrity Manifests (CoRIM) that
   represent Endorsements and Reference Values in CBOR format.
   Composite devices or systems are represented by a collection of
   Concise Module Identifiers (CoMID) and Concise Software Identifiers
   (CoSWID) bundled in a CoRIM document.

### EAT Media Types  (draft-lundblade-rats-eat-media-type)
Payloads used in Remote Attestation Procedures may require an
   associated media type for their conveyance, for example when used in
   RESTful APIs.

   This memo defines media types to be used for Entity Attestation
   Tokens (EAT).

### EAT Media Types  (draft-ietf-rats-eat-media-type)
Payloads used in Remote Attestation Procedures may require an
   associated media type for their conveyance, for example when used in
   RESTful APIs.

   This memo defines media types to be used for Entity Attestation
   Tokens (EAT).

### Remote Posture Assessment for Systems, Containers, and Applications  (draft-moriarty-rats-posture-assessment)
This document establishes an architectural pattern whereby a remote
   attestation could be issued for a complete set of benchmarks or
   controls that are defined and grouped by an external entity,
   preventing the need to send over individual attestations for each
   item within a benchmark or control framework.  This document
   establishes a pattern to list sets of benchmarks and controls within
   CWT and JWT formats for use as an Entity Attestation Token (EAT).

### PKI-based Attestation Evidence  (draft-ounsworth-rats-pkix-evidence)
This document specifies ASN.1 structures produced by an Attester as
   part of the remote attestation procedures and constitute Evidence.

   This document follows the Remote ATtestation procedureS (RATS)
   architecture where Evidence is sent by an Attester and processed by a
   Verifier.

### Reference Interaction Models for Remote Attestation Procedures  (draft-ietf-rats-reference-interaction-models)
This document describes interaction models for remote attestation
   procedures (RATS) [RFC9334].  Three conveying mechanisms --
   Challenge/Response, Uni-Directional, and Streaming Remote Attestation
   -- are illustrated and defined.  Analogously, a general overview
   about the information elements typically used by corresponding
   conveyance protocols are highlighted.

### Concise Reference Integrity Manifest  (draft-ietf-rats-corim)
Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester and therefore to decide
   whether or not to engage in secure interactions with it.  Evidence
   about trustworthiness can be rather complex and it is deemed
   unrealistic that every Relying Party is capable of the appraisal of
   Evidence.  Therefore that burden is typically offloaded to a
   Verifier.  In order to conduct Evidence appraisal, a Verifier
   requires not only fresh Evidence from an Attester, but also trusted
   Endorsements and Reference Values from Endorsers and Reference Value
   Providers, such as manufacturers, distributors, or device owners.
   This document specifies the information elements for representing
   Endorsements and Reference Values in CBOR format.

### The Entity Attestation Token (EAT)  (draft-ietf-rats-eat)
An Entity Attestation Token (EAT) provides an attested claims set
   that describes state and characteristics of an entity, a device like
   a smartphone, IoT device, network equipment or such.  This claims set
   is used by a relying party, server or service to determine the type
   and degree of trust placed in the entity.

   An EAT is either a CBOR Web Token (CWT) or JSON Web Token (JWT) with
   attestation-oriented claims.

### Epoch Markers  (draft-birkholz-rats-epoch-markers)
This document defines Epoch Markers as a way to establish a notion of
   freshness among actors in a distributed system.  Epoch Markers are
   similar to "time ticks" and are produced and distributed by a
   dedicated system, the Epoch Bell.  Systems that receive Epoch Markers
   do not have to track freshness using their own understanding of time
   (e.g., via a local real-time clock).  Instead, the reception of a
   certain Epoch Marker establishes a new epoch that is shared between
   all recipients.

### PKI-based Attestation Evidence  (draft-ietf-rats-pkix-evidence)
This document specifies ASN.1 structures produced by an Attester as
   part of the remote attestation procedures and constitute Evidence.

   This document follows the Remote ATtestation procedureS (RATS)
   architecture where Evidence is sent by an Attester and processed by a
   Verifier.

### Remote Posture Assessment for Systems, Containers, and Applications at Scale  (draft-ietf-rats-posture-assessment)
This document establishes an architectural pattern whereby
   Attestation Results could be produced for a complete set of
   benchmarks or controls that are defined and grouped by an external
   entity, eliminating the need to convey individual Evidence items for
   each item within a benchmark or control framework.  This document
   establishes a pattern to list sets of benchmarks and controls within
   CWT and JWT formats for use as an Entity Attestation Token (EAT).
   While the discussion below pertains mostly to TPM, other Roots of
   Trust such as TCG DICE and non-TCG defined components will also be
   included.

### A YANG Data Model for Challenge-Response-based Remote Attestation Procedures using TPMs  (draft-ietf-rats-yang-tpm-charra)
This document defines YANG Remote Procedure Calls (RPCs) and a few
   configuration nodes required to retrieve attestation evidence about
   integrity measurements from a device, following the operational
   context defined in TPM-based Network Device Remote Integrity
   Verification.  Complementary measurement logs are also provided by
   the YANG RPCs, originating from one or more roots of trust for
   measurement (RTMs).  The module defined requires at least one TPM 1.2
   or TPM 2.0 as well as a corresponding TPM Software Stack (TSS), or
   equivalent hardware implementations that include the protected
   capabilities as provided by TPMs as well as a corresponding software
   stack, included in the device components of the composite device the
   YANG server is running on.

### Evidence Transformations  (draft-smith-rats-evidence-trans)
Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester to decide if continued
   interaction is warrented.  Evidence structures can vary making
   appraisals challenging for Verifiers.  Verifiers need to understand
   Evidence encoding formats and some of the Evidence semantics to
   appraise it.  Consequently, Evidence may require format
   transformation to an internal representation that preserves original
   semantics.  This document specifies Evidence transformation methods
   for DiceTcbInfo, concise evidence, and SPDM measurements block
   structures.  These Evidence structures are converted to the CoRIM
   internal representation and follow CoRIM defined appraisal
   procedures.

### Remote Attestation with Multiple Verifiers  (draft-deshpande-rats-multi-verifier)
IETF RATS Architecture, defines the key role of a Verifier.  In a
   complex system, this role needs to be performed by multiple Verfiers
   coordinating together to assess the full trustworthiness of an
   Attester.  This document focuses on various topological patterns for
   a multiple Verifier system.  It only covers the architectural aspects
   introduced by the Multi Verifier concept, which is neutral with
   regard to specific wire formats, encoding, transport mechanisms, or
   processing details.

### EAT Attestation Results  (draft-fv-rats-ear)
This document defines the EAT Attestation Result (EAR) message
   format.

   EAR is used by a verifier to encode the result of the appraisal over
   an attester's evidence.  It embeds an AR4SI's "trustworthiness
   vector" to present a normalized view of the evaluation results, thus
   easing the task of defining and computing authorization policies by
   relying parties.  Alongside the trustworthiness vector, EAR provides
   contextual information bound to the appraisal process.  This allows a
   relying party (or an auditor) to reconstruct the frame of reference
   in which the trustworthiness vector was originally computed.  EAR
   supports simple devices with one attester as well as composite
   devices that are made of multiple attesters, allowing the state of
   each attester to be separately examined.  EAR can also accommodate
   registered and unregistered extensions.  It can be serialized and
   protected using either CWT or JWT.

### A CBOR Tag for Unprotected CWT Claims Sets  (draft-ietf-rats-uccs)
This document defines the Unprotected CWT Claims Set (UCCS), a data
   format for representing a CBOR Web Token (CWT) Claims Set without
   protecting it by a signature, message authentication code (MAC), or
   encryption.  UCCS enables the use of CWT claims in environments where
   protection is provided by other means, such as secure communication
   channels or trusted execution environments.  This specification
   defines a CBOR tag for UCCS and describes the UCCS format, its
   encoding, and processing considerations, and discusses security
   implications of using unprotected claims sets.


   // (This editors' note will be removed by the RFC editor:) The
   // present revision (–12) contains remaining document changes based
   // on feedback from the IESG evaluation and has been submitted as
   // input to IETF 121.

### Attestation Results for Secure Interactions  (draft-ietf-rats-ar4si)
This document defines reusable Attestation Result information
   elements.  When these elements are offered to Relying Parties as
   Evidence, different aspects of Attester trustworthiness can be
   evaluated.  Additionally, where the Relying Party is interfacing with
   a heterogeneous mix of Attesting Environment and Verifier types,
   consistent policies can be applied to subsequent information exchange
   between each Attester and the Relying Party.

   This document also defines two serialisations of the proposed
   information model, utilising CBOR and JSON.

### Direct Anonymous Attestation for the Remote Attestation Procedures Architecture  (draft-ietf-rats-daa)
This document maps the concept of Direct Anonymous Attestation (DAA)
   to the Remote Attestation Procedures (RATS) Architecture.  The
   protocol entity DAA Issuer is introduced and its mapping with
   existing RATS roles in DAA protocol steps is specified.

### Concise Selector for Endorsements and Reference Values  (draft-ietf-rats-coserv)
In the Remote Attestation Procedures (RATS) architecture, Verifiers
   require Endorsements and Reference Values to assess the
   trustworthiness of Attesters.  This document specifies the Concise
   Selector for Endorsements and Reference Values (CoSERV), a structured
   query/result format designed to facilitate the discovery and
   retrieval of these artifacts from various providers.  CoSERV defines
   a query language and corresponding result structure using CDDL, which
   can be serialized in CBOR format, enabling efficient interoperability
   across diverse systems.

### Epoch Markers  (draft-ietf-rats-epoch-markers)
This document defines Epoch Markers as a means to establish a notion
   of freshness among actors in a distributed system.  Epoch Markers are
   similar to "time ticks" and are produced and distributed by a
   dedicated system known as the Epoch Bell.  Systems receiving Epoch
   Markers do not need to track freshness using their own understanding
   of time (e.g., via a local real-time clock).  Instead, the reception
   of a specific Epoch Marker establishes a new epoch that is shared
   among all recipients.  This document defines Epoch Marker types,
   including CBOR time tags, RFC 3161 TimeStampToken, and nonce-like
   structures.  It also defines a CWT Claim to embed Epoch Markers in
   RFC 8392 CBOR Web Tokens, which serve as vehicles for signed protocol
   messages.

### Evidence Transformations  (draft-ietf-rats-evidence-trans)
Remote Attestation Procedures (RATS) enable Relying Parties to assess
   the trustworthiness of a remote Attester to decide if continued
   interaction is warrented.  Evidence structures can vary making
   appraisals challenging for Verifiers.  Verifiers need to understand
   Evidence encoding formats and some of the Evidence semantics to
   appraise it.  Consequently, Evidence may require format
   transformation to an internal representation that preserves original
   semantics.  This document specifies Evidence transformation methods
   for DiceTcbInfo, concise evidence, and SPDM measurements block
   structures.  These Evidence structures are converted to the CoRIM
   internal representation and follow CoRIM defined appraisal
   procedures.

### EAT Attestation Results  (draft-ietf-rats-ear)
This document defines the EAT Attestation Result (EAR) message
   format.

   EAR is used by a verifier to encode the result of the appraisal over
   an attester's evidence.  It embeds an AR4SI's "trustworthiness
   vector" to present a normalized view of the evaluation results, thus
   easing the task of defining and computing authorization policies by
   relying parties.  Alongside the trustworthiness vector, EAR provides
   contextual information bound to the appraisal process.  This allows a
   relying party (or an auditor) to reconstruct the frame of reference
   in which the trustworthiness vector was originally computed.  EAR
   supports simple devices with one attester as well as composite
   devices that are made of multiple attesters, allowing the state of
   each attester to be separately examined.  EAR can also accommodate
   registered and unregistered extensions.  It can be serialized and
   protected using either CWT or JWT.

### Attestation Event Stream Subscription  (draft-ietf-rats-network-device-subscription)
This document defines how to subscribe to YANG Event Streams for
   Remote Attestation Procedures (RATS).  Specifically, this document
   defines a YANG module that augments the YANG module for Trusted
   Platform Module (TPM)-based Challenge-Response Remote Attestation
   (CHARRA), enabling subscription to RATS Conceptual Messages of the
   Evidence type and auxiliary Event Logs as part of that Evidence.  The
   module defined requires at least one Trusted Platform Module (TPM)
   1.2 or TPM 2.0 (or equivalent hardware implementation providing the
   same protected capabilities as a TPM) must be available on the
   Attester on which the YANG server is running.

### Entity Attestation Token (EAT) Measured Component  (draft-ietf-rats-eat-measured-component)
The term "measured component" refers to an object within the
   attester's target environment whose state can be sampled and
   typically digested using a cryptographic hash function.  Examples of
   measured components include firmware stored in flash memory, software
   loaded into memory at start time, data stored in a file system, or
   values in a CPU register.  This document provides the information
   model for the "measured component" and two associated data models.
   This separation is intentional: the JSON and CBOR serializations,
   coupled with the media types and associated Constrained Application
   Protocol (CoAP) Content-Formats, enable the immediate use of the
   semantics within the Entity Attestation Token (EAT) framework.
   Meanwhile, the information model can be reused in future
   specifications to provide additional serializations, for example,
   using ASN.1.

### RATS Endorsements  (draft-ietf-rats-endorsements)
In the IETF Remote Attestation Procedures (RATS) architecture, a
   Verifier accepts Evidence and uses Appraisal Policy for Evidence,
   typically with additional input from Endorsements and Reference
   Values, to generate Attestation Results in formats that are useful
   for Relying Parties.  This document illustrates the purpose and role
   of Endorsements and discusses some considerations in the choice of
   message format for Endorsements in the scope of the RATS
   architecture.

   This document does not aim to define a conceptual message format for
   Endorsements and Reference Values.  Instead, it extends RFC9334 to
   provide further details on Reference Values and Endorsements, as
   these topics were outside the scope of the RATS charter when RFC9334
   was developed.

### Evidence Encoding for Hardware Security Modules  (draft-ietf-rats-pkix-key-attestation)
This document specifies a vendor-agnostic format for Evidence
   produced and verified within a PKIX context.  The Evidence produced
   this way includes claims collected about a cryptographic module, such
   as a Hardware Security Module (HSM), and elements found within it
   such as cryptographic keys.

   One scenario envisaged is that the state information about the
   cryptographic module can be securely presented to a remote operator
   or auditor in a vendor-agnostic verifiable format.  A more complex
   scenario would be to submit this Evidence to a Certification
   Authority to aid in determining whether the storage properties of
   this key meet the requirements of a given certificate profile.

   This specification also offers a format for requesting a
   cryptographic module to produce Evidence tailored for expected use.

### Remote Attestation with Multiple Verifiers  (draft-ietf-rats-multi-verifier)
IETF RATS Architecture, defines the key role of a Verifier.  In a
   complex system, this role needs to be performed by multiple Verfiers
   coordinating together to assess the full trustworthiness of an
   Attester.  This document focuses on various topological patterns for
   a multiple Verifier system.  It only covers the architectural aspects
   introduced by the Multi Verifier concept, which is neutral with
   regard to specific wire formats, encoding, transport mechanisms, or
   processing details.

### RATS Conceptual Messages Wrapper (CMW)  (draft-ietf-rats-msg-wrap)
The Conceptual Messages introduced by the RATS architecture (RFC
   9334) are protocol-agnostic data units that are conveyed between RATS
   roles during remote attestation procedures.  Conceptual Messages
   describe the meaning and function of such data units within RATS data
   flows without specifying a wire format, encoding, transport
   mechanism, or processing details.  The initial set of Conceptual
   Messages is defined in Section 8 of RFC 9334 and includes Evidence,
   Attestation Results, Endorsements, Reference Values, and Appraisal
   Policies.

   This document introduces the Conceptual Message Wrapper (CMW) that
   provides a common structure to encapsulate these messages.  It
   defines a dedicated CBOR tag, corresponding JSON Web Token (JWT) and
   CBOR Web Token (CWT) claims, and an X.509 extension.

   This allows CMWs to be used in CBOR-based protocols, web APIs using
   JWTs and CWTs, and PKIX artifacts like X.509 certificates.
   Additionally, the draft defines a media type and a CoAP content
   format to transport CMWs over protocols like HTTP, MIME, and CoAP.

   The goal is to improve the interoperability and flexibility of remote
   attestation protocols.  Introducing a shared message format such as
   CMW enables consistent support for different attestation message
   types, evolving message serialization formats without breaking
   compatibility, and avoiding the need to redefine how messages are
   handled within each protocol.

## Working Group: rift
### RIFT: Routing in Fat Trees  (draft-ietf-rift-rift)
This document defines a specialized, dynamic routing protocol for
   Clos, fat tree, and variants thereof.  These topologies were
   initially used within crossbar interconnects, and consequently router
   and switch backplanes, but their characteristics make them ideal for
   constructing IP fabrics as well.  The protocol specified by this
   document is optimized toward the minimization of control plane state
   to support very large substrates as well as the minimization of
   configuration and operational complexity to allow for simplified
   deployment of said topologies.

### RIFT: Routing in Fat Trees  (draft-przygienda-rift)
This document outlines a specialized, dynamic routing protocol for
   Clos and fat-tree network topologies.  The protocol (1) deals with
   automatic construction of fat-tree topologies based on detection of
   links, (2) minimizes the amount of routing state held at each level,
   (3) automatically prunes the topology distribution exchanges to a
   sufficient subset of links, (4) supports automatic disaggregation of
   prefixes on link and node failures to prevent black-holing and
   suboptimal routing, (5) allows traffic steering and re-routing
   policies, (6) allows non-ECMP forwarding, (7) automatically re-
   balances traffic towards the spines based on bandwidth available and
   ultimately (8) provides mechanisms to synchronize a limited key-value
   data-store that can be used after protocol convergence to e.g.
   bootstrap higher levels of functionality on nodes.

### RIFT Applicability  (draft-wei-rift-applicability)
This document discusses the properties, applicability and operational
   considerations of RIFT in different network scenarios.  It intends to
   provide a rough guide how RIFT can be deployed to simplify routing
   operations in Clos topologies and their variations.

### RIFT YANG Model  (draft-zhang-rift-yang)
This document defines a YANG data model for the configuration and
   management of RIFT Protocol.

### RIFT Key/Value Structure and Registry  (draft-ietf-rift-kv-registry)
The RIFT (Routing in Fat-Trees) protocol allows for key/value pairs
   to be advertised within Key-Value Topology Information Elements (KV-
   TIEs).  The data contained within these KV-TIEs can be used for any
   imaginable purpose.  This document defines the various Key-Types
   (i.e.  Well-Known, OUI, and Experimental) and a method to structure
   corresponding values.

### SRIFT: Segment Routing in Fat Trees  (draft-ietf-rift-sr)
This document specifies signaling procedures for Segment Routing in
   RIFT.  Each node's loopback address, Segment Routing Global Block
   (SRGB) and Node Segment Identifier (Node-SID), which are typically
   assigned by a configuration management system and distibuted by
   routing protocols, are distributed southbound from the Top Of Fabric
   (TOF) nodes via RIFT's Key-Value distribution mechanism, so that each
   node can compute how to reach a segment represented by the active SID
   in a packet.  An SR controller signals SR policies to ingress nodes
   so that they can send packets with a desired segment list to steer
   traffic.

### RIFT Applicability and Operational Considerations  (draft-ietf-rift-applicability)
This document discusses the properties, applicability and operational
   considerations of RIFT in different network scenarios.  It intends to
   provide a rough guide how RIFT can be deployed to simplify routing
   operations in Clos topologies and their variations.

### YANG Data Model for Routing in Fat Trees (RIFT)  (draft-ietf-rift-yang)
This document defines a YANG data model for the configuration and
   management of Routing in Fat Trees (RIFT) Protocol.  The model is
   based on YANG 1.1 as defined in RFC7950 and conforms to the Network
   Management Datastore Architecture (NMDA) as described in RFC8342.

### RIFT Auto-EVPN  (draft-ietf-rift-auto-evpn)
This document specifies procedures that allow an EVPN overlay to be
   fully and automatically provisioned when using RIFT as underlay by
   leveraging RIFT's no-touch ZTP architecture.

### Routing in Fat Trees (RIFT) Key/Value Topology Information Elements Structure and Processing  (draft-ietf-rift-kv-tie-structure-and-processing)
The RIFT (Routing in Fat Trees) protocol allows for key/value pairs
   to be advertised within Key-Value Topology Information Elements (KV
   TIEs).  The data contained within these KV TIEs can be used for any
   imaginable purpose.

   This document specifies behavior for the various Key-Types (i.e.,
   Well-Known, OUI, and Experimental) and a method to structure
   corresponding values.  It also defines a Well-Known Key Sub-Type used
   for testing tie-breaking behavior.

## Working Group: rtgwg
### A YANG Data Model for RIB Extensions  (draft-ietf-rtgwg-yang-rib-extend)
A Routing Information Base (RIB) is a list of routes and their corresponding administrative data and operational state.

 RFC 8349 defines the basic building blocks for the RIB data model, and this model augments it to support multiple next hops (aka paths) for each route as well as additional attributes.

### Multi-segment SD-WAN via Cloud DCs  (draft-dmk-rtgwg-multisegment-sdwan)
This document describes a method for SD-WAN CPEs using GENEVE
   Encapsulation (RFC8926) to encapsulate the IPsec encrypted
   packets and send them to their closest Cloud GWs, who can
   steer the IPsec encrypted payload through the Cloud Backbone
   without decryption to the egress Cloud GWs which then forward
   the original IPsec encrypted payload to the destination CPEs.
   This method is for Cloud Backbone to connect multiple
   segments of SD-WAN without the Cloud GWs decrypting and re-
   encrypting the payloads.

### Applicability of Bidirectional Forwarding Detection (BFD) for Multi-point Networks in Virtual Router Redundancy Protocol (VRRP)  (draft-ietf-rtgwg-vrrp-p2mp-bfd)
This document specifies the applicability of Bidirectional Forwarding
   Detection in multipoint networks to support sub-second failure
   detection for Virtual Router Redundancy Protocol Router Role
   election.  The mechanism enables faster determination of the Active
   Router without requiring any modification to the protocol behavior or
   message formats defined in RFC 9568.

### Virtual Router Redundancy Protocol (VRRP) Version 3 for IPv4 and IPv6  (draft-ietf-rtgwg-vrrp-rfc5798bis)
This document defines version 3 of the Virtual Router Redundancy
   Protocol (VRRP) for IPv4 and IPv6.  It obsoletes RFC 5798 which
   previously specified VRRP (version 3).  RFC 5798 obsoleted RFC 3768
   which specified VRRP (version 2) for IPv4.  VRRP specifies an
   election protocol that dynamically assigns responsibility for a
   Virtual Router to one of the VRRP Routers on a LAN.  The VRRP Router
   controlling the IPv4 or IPv6 address(es) associated with a Virtual
   Router is called the Active Router, and it forwards packets routed to
   these IPv4 or IPv6 addresses.  Active Routers are configured with
   virtual IPv4 or IPv6 addresses, and Backup Routers infer the address
   family of the virtual addresses being advertised based on the IP
   protocol version.  Within a VRRP Router, the Virtual Routers in each
   of the IPv4 and IPv6 address families are independent of one another
   and always treated as separate Virtual Router instances.  The
   election process provides dynamic failover in the forwarding
   responsibility should the Active Router become unavailable.  For
   IPv4, the advantage gained from using VRRP is a higher-availability
   default path without requiring configuration of dynamic routing or
   router discovery protocols on every end-host.  For IPv6, the
   advantage gained from using VRRP for IPv6 is a quicker switchover to
   Backup Routers than can be obtained with standard IPv6 Neighbor
   Discovery mechanisms.

### Calculating IGP routes over Traffic Engineering tunnels  (draft-hsmit-mpls-igp-spf)
This document describes how conventional hop-by-hop link-state
routing protocols interact with new Traffic Engineering capabilities
to create IGP shortcuts.  In particular this document describes how
Dijkstra's SPF algorithm should be adapted so that link-state IGPs
will calculate IP routes to forward traffic over tunnels that are
set up by Traffic Engineering.

### The Generalized TTL Security Mechanism (GTSM)  (draft-ietf-rtgwg-rfc3682bis)
The use of a packet's Time to Live (TTL) (IPv4) or Hop Limit (IPv6) to verify whether the packet was originated by an adjacent node on a connected link has been used in many recent protocols.  This document generalizes this technique.  This document obsoletes Experimental RFC 3682. [STANDARDS-TRACK]

### Calculating Interior Gateway Protocol (IGP) Routes Over Traffic Engineering Tunnels  (draft-ietf-rtgwg-igp-shortcut)
This document describes how conventional hop-by-hop link-state routing protocols interact with new Traffic Engineering capabilities to create Interior Gateway Protocol (IGP) shortcuts.  In particular, this document describes how Dijkstra's Shortest Path First (SPF) algorithm can be adapted so that link-state IGPs will calculate IP routes to forward traffic over tunnels that are set up by Traffic Engineering.  This memo provides information for the Internet community.

### IP Fast Reroute Framework  (draft-ietf-rtgwg-ipfrr-framework)
This document provides a framework for the development of IP fast- reroute mechanisms that provide protection against link or router failure by invoking locally determined repair paths.  Unlike MPLS fast-reroute, the mechanisms are applicable to a network employing conventional IP routing and forwarding.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Basic Specification for IP Fast Reroute: Loop-Free Alternates  (draft-ietf-rtgwg-ipfrr-spec-base)
This document describes the use of loop-free alternates to provide local protection for unicast traffic in pure IP and MPLS/LDP networks in the event of a single failure, whether link, node, or shared risk link group (SRLG).  The goal of this technology is to reduce the packet loss that happens while routers converge after a topology change due to a failure.  Rapid failure repair is achieved through use of precalculated backup next-hops that are loop-free and safe to use until the distributed network convergence process completes.  This simple approach does not require any support from other routers.  The extent to which this goal can be met by this specification is dependent on the topology of the network. [STANDARDS-TRACK]

### IP MIB for IP Fast-Reroute  (draft-ietf-rtgwg-ipfrr-ip-mib)
This draft defines a portion of the Management Information Base (MIB)
   for use with network management protocols in the Internet community.
   In particular, it describes managed objects relevant for IP routes
   using IP Fast-Reroute [RFC5714]

### A Framework for Loop-Free Convergence  (draft-ietf-rtgwg-lf-conv-frmwk)
A micro-loop is a packet forwarding loop that may occur transiently among two or more routers in a hop-by-hop packet forwarding paradigm.

 This framework provides a summary of the causes and consequences of micro-loops and enables the reader to form a judgement on whether micro-looping is an issue that needs to be addressed in specific networks. It also provides a survey of the currently proposed mechanisms that may be used to prevent or to suppress the formation of micro-loops when an IP or MPLS network undergoes topology change due to failure, repair, or management action. When sufficiently fast convergence is not available and the topology is susceptible to micro-loops, use of one or more of these mechanisms may be desirable. This document is not an Internet Standards Track specification; it is published for informational purposes.

### A Framework for IP and MPLS Fast Reroute Using Not-Via Addresses  (draft-ietf-rtgwg-ipfrr-notvia-addresses)
This document presents an illustrative framework for providing fast reroute in an IP or MPLS network through encapsulation and forwarding to "not-via" addresses. The general approach described here uses a single level of encapsulation and could be used to protect unicast, multicast, and LDP traffic against link, router, and shared risk group failure, regardless of network topology and metrics.

 The mechanisms presented in this document are purely illustrative of the general approach and do not constitute a protocol specification. The document represents a snapshot of the work of the Routing Area Working Group at the time of publication and is published as a document of record. Further work is needed before implementation or deployment.

### Analysis and Minimization of Microloops in Link-state Routing Protocols  (draft-ietf-rtgwg-microloop-analysis)
Link-state routing protocols (e.g. OSPF or IS-IS) are known to
   converge to a loop-free state within a finite period of time after a
   change in the topology. It is normal, however, to observe short-term
   loops during the period of topology update propagation, route
   recalculation, and forwarding table update, due to the asynchronous
   nature of link-state protocol operation. This document provides an
   analysis of formation of such microloops and suggests simple
   mechanisms to minimize them.

### Framework for Loop-Free Convergence Using the Ordered Forwarding Information Base (oFIB) Approach  (draft-ietf-rtgwg-ordered-fib)
This document describes an illustrative framework of a mechanism for use in conjunction with link-state routing protocols that prevents the transient loops that would otherwise occur during topology changes. It does this by correctly sequencing the forwarding information base (FIB) updates on the routers.

 This mechanism can be used in the case of non-urgent (management action) link or node shutdowns and restarts or link metric changes. It can also be used in conjunction with a fast reroute mechanism that converts a sudden link or node failure into a non-urgent topology change. This is possible where a complete repair path is provided for all affected destinations.

 After a non-urgent topology change, each router computes a rank that defines the time at which it can safely update its FIB. A method for accelerating this loop-free convergence process by the use of completion messages is also described.

 The technology described in this document has been subject to extensive simulation using pathological convergence behavior and real network topologies and costs. However, the mechanisms described in this document are purely illustrative of the general approach and do not constitute a protocol specification. This document represents a snapshot of the work of the Routing Area Working Group at the time of publication and is published as a document of record. Further work is needed before implementation or deployment.

### Loop-Free Alternate (LFA) Applicability in Service Provider (SP) Networks  (draft-ietf-rtgwg-lfa-applicability)
In this document, we analyze the applicability of the Loop-Free Alternate (LFA) method of providing IP fast reroute in both the core and access parts of Service Provider networks.  We consider both the link and node failure cases, and provide guidance on the applicability of LFAs to different network topologies, with special emphasis on the access parts of the network.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Requirements for Advanced Multipath in MPLS Networks  (draft-ietf-rtgwg-cl-requirement)
This document provides a set of requirements for Advanced Multipath in MPLS networks.

 Advanced Multipath is a formalization of multipath techniques currently in use in IP and MPLS networks and a set of extensions to existing multipath techniques.

### Selection of Loop-Free Alternates for Multi-Homed Prefixes  (draft-ietf-rtgwg-multihomed-prefix-lfa)
Deployment experience gained from implementing algorithms to determine Loop-Free Alternates (LFAs) for multi-homed prefixes (MHPs) has revealed some avenues for potential improvement.  This document provides explicit inequalities that can be used to evaluate neighbors as potential alternates for MHPs.  It also provides detailed criteria for evaluating potential alternates for external prefixes advertised by OSPF ASBRs.  This document updates Section 6 of RFC 5286 by expanding some of the routing aspects.

### An Architecture for IP/LDP Fast Reroute Using Maximally Redundant Trees (MRT-FRR)  (draft-ietf-rtgwg-mrt-frr-architecture)
This document defines the architecture for IP and LDP Fast Reroute using Maximally Redundant Trees (MRT-FRR).  MRT-FRR is a technology that gives link-protection and node-protection with 100% coverage in any network topology that is still connected after the failure.

### Remote Loop-Free Alternate (LFA) Fast Reroute (FRR)  (draft-ietf-rtgwg-remote-lfa)
This document describes an extension to the basic IP fast reroute mechanism, described in RFC 5286, that provides additional backup connectivity for point-to-point link failures when none can be provided by the basic mechanisms.

### Advanced Multipath Use Cases and Design Considerations  (draft-ietf-rtgwg-cl-use-cases)
Advanced Multipath is a formalization of multipath techniques
   currently in use in IP and MPLS networks and a set of extensions to
   existing multipath techniques.

   This document provides a set of use cases and design considerations
   for Advanced Multipath.  Existing practices are described.  Use cases
   made possible through Advanced Multipath extensions are described.

### Advanced Multipath Framework in MPLS  (draft-ietf-rtgwg-cl-framework)
This document specifies a framework for support of Advanced Multipath
   in MPLS networks.  As defined in this framework, an Advanced
   Multipath consists of a group of homogenous or non-homogenous links
   that have the same forward adjacency (FA) and can be considered as a
   single TE link or an IP link when advertised into IGP routing.

### Multicast-Only Fast Reroute  (draft-ietf-rtgwg-mofrr)
As IPTV deployments grow in number and size, service providers are looking for solutions that minimize the service disruption due to faults in the IP network carrying the packets for these services.  This document describes a mechanism for minimizing packet loss in a network when node or link failures occur.  Multicast-only Fast Reroute (MoFRR) works by making simple enhancements to multicast routing protocols such as Protocol Independent Multicast (PIM) and Multipoint LDP (mLDP).

### Microloop prevention by introducing a local convergence delay  (draft-litkowski-rtgwg-uloop-delay)
This document describes a mechanism for link-state routing protocols
   to prevent local transient forwarding loops in case of link failure.
   This mechanism Proposes a two-steps convergence by introducing a
   delay between the convergence of the node adjacent to the topology
   change and the network wide convergence.

   As this mechanism delays the IGP convergence it may only be used for
   planned maintenance or when fast reroute protects the traffic between
   the link failure and the IGP convergence.

   Simulations using real network topologies have been performed and
   show that local loops are a significant portion (>50%) of the total
   forwarding loops.

### Operational Management of Loop-Free Alternates  (draft-ietf-rtgwg-lfa-manageability)
Loop-Free Alternates (LFAs), as defined in RFC 5286, constitute an IP Fast Reroute (IP FRR) mechanism enabling traffic protection for IP traffic (and, by extension, MPLS LDP traffic). Following early deployment experiences, this document provides operational feedback on LFAs, highlights some limitations, and proposes a set of refinements to address those limitations. It also proposes required management specifications.

 This proposal is also applicable to remote-LFA solutions.

### Remote-LFA Node Protection and Manageability  (draft-psarkar-rtgwg-rlfa-node-protection)
The loop-free alternates computed following the current Remote-LFA
   [I-D.ietf-rtgwg-remote-lfa] specification gaurantees only link-
   protection.  The resulting Remote-LFA nexthops (also called PQ-
   nodes), may not gaurantee node-protection for all destinations being
   protected by it.

   This document describes procedures for determining if a given PQ-node
   provides node-protection for a specific destination or not.  The
   document also shows how the same procedure can be utilised for
   collection of complete characteristics for alternate paths.
   Knowledge about the characteristics of all alternate path is
   precursory to apply operator defined policy for eliminating paths not
   fitting constraints.

### An Algorithm for Computing IP/LDP Fast Reroute Using Maximally Redundant Trees (MRT-FRR)  (draft-ietf-rtgwg-mrt-frr-algorithm)
This document supports the solution put forth in "An Architecture for IP/LDP Fast Reroute Using Maximally Redundant Trees (MRT-FRR)" (RFC 7812) by defining the associated MRT Lowpoint algorithm that is used in the Default MRT Profile to compute both the necessary Maximally Redundant Trees with their associated next hops and the alternates to select for MRT-FRR.

### Routing Timer Parameter Synchronization  (draft-bryant-rtgwg-param-sync)
This document describes a mechanism for a link state routing protocol
   to coordinate the value of a routing timer parameter amongst routers
   in the flooding domain.  The document also defines the solution to
   one specific case: the agreement of a common convergence timer value
   for use by routers in network convergence.

### Node Potential Oriented Multi-NextHop Routing Protocol  (draft-ietf-rtgwg-npmnrp)
The Node Potential Oriented Multi-Nexthop Routing Protocol (NP-MNRP)
   bases on the idea of "hop-by-hop routing forwarding, multi-backup
   next hop" and combines with the phenomena that water flows from
   higher place to lower.  NP-MNRP defines a metric named as node
   potential, which is based on hop count and the actual link bandwidth,
   and calculates multiple next-hops through the potential difference
   between the nodes.

### Remote-LFA Node Protection and Manageability  (draft-ietf-rtgwg-rlfa-node-protection)
The loop-free alternates (LFAs) computed following the current remote-LFA specification guarantees only link protection. The resulting remote-LFA next hops (also called "PQ-nodes") may not guarantee node protection for all destinations being protected by it.

 This document describes an extension to the remote-loop-free-based IP fast reroute mechanisms that specifies procedures for determining whether or not a given PQ-node provides node protection for a specific destination. The document also shows how the same procedure can be utilized for the collection of complete characteristics for alternate paths. Knowledge about the characteristics of all alternate paths is a precursor to applying the operator-defined policy for eliminating paths not fitting the constraints.

### Use of BGP for Routing in Large-Scale Data Centers  (draft-ietf-rtgwg-bgp-routing-large-dc)
Some network operators build and operate data centers that support over one hundred thousand servers.  In this document, such data centers are referred to as "large-scale" to differentiate them from smaller infrastructures.  Environments of this scale have a unique set of network requirements with an emphasis on operational simplicity and network stability.  This document summarizes operational experience in designing and operating large-scale data centers using BGP as the only routing protocol.  The intent is to report on a proven and stable routing design that could be leveraged by others in the industry.

### Destination/Source Routing  (draft-lamparter-rtgwg-dst-src-routing)
This note specifies using packets' source addresses in route lookups
   as additional qualifier to be used in route lookup.  This applies to
   IPv6 [RFC2460] in general with specific considerations for routing
   protocol left for separate documents.

### LFA selection for Multi-Homed Prefixes  (draft-psarkar-rtgwg-multihomed-prefix-lfa)
This document shares experience gained from implementing algorithms
   to determine Loop-Free Alternates for multi-homed prefixes.  In
   particular, this document provides explicit inequalities that can be
   used to evaluate neighbors as a potential alternates for multi-homed
   prefixes.  It also provides detailed criteria for evaluating
   potential alternates for external prefixes advertised by OSPF ASBRs.

### A YANG Data Model for Virtual Router Redundancy Protocol (VRRP)  (draft-liu-rtgwg-yang-vrrp)
This document describes a data model for Virtual Router Redundancy
   Protocol (VRRP). Both version 2 and version 3 of VRRP are covered.

### RIB YANG Data Model  (draft-acee-rtgwg-yang-rib-extend)
The Routing Information Base (RIB) is a list of routes and their
   corresponding administrative data and operational state.

   RFC 8349 defines the basic building blocks for RIB, and this model
   augments it to support multiple next-hops (aka, paths) for each route
   as well as additional attributes.

### Routing Policy Configuration Model for Service Provider Networks  (draft-shaikh-rtgwg-policy-model)
This document defines a YANG data model for configuring and managing
   routing policies in a vendor-neutral way and based on actual
   operational practice.  The model provides a generic policy framework
   which can be augmented with protocol-specific policy configuration.

### Shortest Path First (SPF) Back-Off Delay Algorithm for Link-State IGPs  (draft-ietf-rtgwg-backoff-algo)
This document defines a standard algorithm to temporarily postpone or "back off" link-state IGP Shortest Path First (SPF) computations. This reduces the computational load and churn on IGP nodes when multiple temporally close network events trigger multiple SPF computations.

 Having one standard algorithm improves interoperability by reducing the probability and/or duration of transient forwarding loops during the IGP convergence when the IGP reacts to multiple temporally close IGP events.

### Impact of Shortest Path First (SPF) Trigger and Delay Strategies on IGP Micro-loops  (draft-ietf-rtgwg-spf-uloop-pb-statement)
A micro-loop is a packet-forwarding loop that may occur transiently among two or more routers in a hop-by-hop packet-forwarding paradigm.

 This document analyzes the impact of using different link state IGP implementations in a single network with respect to micro-loops. The analysis is focused on the Shortest Path First (SPF) delay algorithm but also mentions the impact of SPF trigger strategies.

### Encapsulation Considerations  (draft-rtg-dt-encap)
The IETF Routing Area director has chartered a design team to look at
   common issues for the different data plane encapsulations being
   discussed in the NVO3 and SFC working groups and also in the BIER
   BoF, and also to look at the relationship between such encapsulations
   in the case that they might be used at the same time.  The purpose of
   this design team is to discover, discuss and document considerations
   across the different encapsulations in the different WGs/BoFs so that
   we can reduce the number of wheels that need to be reinvented in the
   future.

### A YANG Data Model for Routing Information Protocol (RIP)  (draft-liu-rtgwg-yang-rip)
This document describes a data model for Routing Information Protocol
   (RIP). Both RIP version 2 and RIPng are covered.

### Network Device YANG Organizational Models  (draft-rtgyangdt-rtgwg-device-model)
This document presents an approach for organizing YANG models in a
   comprehensive structure that may be used to configure and operate
   network devices.  The structure is itself represented as a YANG
   model, with all of the related component models logically organized
   in a way that is operationally intuitive, but this model is not
   expected to be implemented.  The identified component modules are
   expected to be defined and implemented on common network devices.

   This document is derived from work submitted to the IETF by members
   of the informal OpenConfig working group of network operators and is
   a product of the Routing Area YANG Architecture design team.

### Encapsulation Considerations  (draft-ietf-rtgwg-dt-encap)
The IETF Routing Area director has chartered a design team to look at
   common issues for the different data plane encapsulations being
   discussed in the NVO3 and SFC working groups and also in the BIER
   BoF, and also to look at the relationship between such encapsulations
   in the case that they might be used at the same time.  The purpose of
   this design team is to discover, discuss and document considerations
   across the different encapsulations in the different WGs/BoFs so that
   we can reduce the number of wheels that need to be reinvented in the
   future.

### A YANG Data Model for the Routing Information Protocol (RIP)  (draft-ietf-rtgwg-yang-rip)
This document describes a data model for the management of the Routing Information Protocol (RIP). Both RIP version 2 and RIPng are covered. The data model includes definitions for configuration, operational state, and Remote Procedure Calls (RPCs).

 The YANG data model in this document conforms to the Network Management Datastore Architecture (NMDA).

### A YANG Data Model for Routing Policy  (draft-ietf-rtgwg-policy-model)
This document defines a YANG data model for configuring and managing routing policies in a vendor-neutral way.  The model provides a generic routing policy framework that can be extended for specific routing protocols using the YANG 'augment' mechanism.

### Destination/Source Routing  (draft-ietf-rtgwg-dst-src-routing)
This note specifies using packets' source addresses in route lookups
   as additional qualifier to be used in hop-by-hop routing decisions.
   This applies to IPv6 [RFC2460] in general with specific
   considerations for routing protocol left for separate documents.
   There is nothing precluding similar operation in IPv4, but this is
   not in scope of this document.

   Note that destination/source routing, source/destination routing,
   SADR, source-specific routing, source-sensitive routing, S/D routing
   and D/S routing are all used synonymously.

### Micro-loop Prevention by Introducing a Local Convergence Delay  (draft-ietf-rtgwg-uloop-delay)
This document describes a mechanism for link-state routing protocols that prevents local transient forwarding loops in case of link failure. This mechanism proposes a two-step convergence by introducing a delay between the convergence of the node adjacent to the topology change and the network-wide convergence.

 Because this mechanism delays the IGP convergence, it may only be used for planned maintenance or when Fast Reroute (FRR) protects the traffic during the time between the link failure and the IGP convergence.

 The mechanism is limited to the link-down event in order to keep the mechanism simple.

 Simulations using real network topologies have been performed and show that local loops are a significant portion (>50%) of the total forwarding loops.

### YANG Data Model for Key Chains  (draft-ietf-rtgwg-yang-key-chain)
This document describes the key chain YANG data model.  Key chains are commonly used for routing protocol authentication and other applications requiring symmetric keys.  A key chain is a list containing one or more elements containing a Key ID, key string, send/accept lifetimes, and the associated authentication or encryption algorithm.  By properly overlapping the send and accept lifetimes of multiple key chain elements, key strings and algorithms may be gracefully updated.  By representing them in a YANG data model, key distribution can be automated.

### Logical Network Element Model  (draft-rtgyangdt-rtgwg-lne-model)
This document defines a logical network element module.  This module
   along with the network instance module can be used to manage the
   logical and virtual resource representations that may be present on a
   network device.  Examples of common industry terms for logical
   resource representations are Logical Systems or Logical Routers.
   Examples of of common industry terms for virtual resource
   representations are Virtual Routing and Forwarding (VRF) instances
   and Virtual Switch Instances (VSIs).

### Network Instance Model  (draft-rtgyangdt-rtgwg-ni-model)
This document defines a network instance module.  This module along
   with the logical network element module can be used to manage the
   logical and virtual resource representations that may be present on a
   network device.  Examples of common industry terms for logical
   resource representations are Logical Systems or Logical Routers.
   Examples of common industry terms for virtual resource
   representations are Virtual Routing and Forwarding (VRF) instances
   and Virtual Switch Instances (VSIs).

### Network Device YANG Logical Organization  (draft-ietf-rtgwg-device-model)
This document presents an approach for organizing YANG models in a
   comprehensive logical structure that may be used to configure and
   operate network devices.  The structure is itself represented as an
   example YANG model, with all of the related component models
   logically organized in a way that is operationally intuitive, but
   this model is not expected to be implemented.  The identified
   component modules are expected to be defined and implemented on
   common network devices.

   This document is derived from work submitted to the IETF by members
   of the informal OpenConfig working group of network operators and is
   a product of the Routing Area YANG Architecture design team.

### A YANG Data Model for the Virtual Router Redundancy Protocol (VRRP)  (draft-ietf-rtgwg-yang-vrrp)
This document describes a data model for the Virtual Router Redundancy Protocol (VRRP).  Both versions 2 and 3 of VRRP are covered.

### YANG Model for Logical Network Elements  (draft-ietf-rtgwg-lne-model)
This document defines a logical network element (LNE) YANG module that is compliant with the Network Management Datastore Architecture (NMDA).  This module can be used to manage the logical resource partitioning that may be present on a network device.  Examples of common industry terms for logical resource partitioning are logical systems or logical routers.  The YANG model in this document conforms with NMDA as defined in RFC 8342.

### YANG Data Model for Network Instances  (draft-ietf-rtgwg-ni-model)
This document defines a network instance module. This module can be used to manage the virtual resource partitioning that may be present on a network device. Examples of common industry terms for virtual resource partitioning are VPN Routing and Forwarding (VRF) instances and Virtual Switch Instances (VSIs).

 The YANG data model in this document conforms to the Network Management Datastore Architecture (NMDA) defined in RFC 8342.

### Enterprise Multihoming using Provider-Assigned Addresses without Network Prefix Translation: Requirements and Solution  (draft-bowbakova-rtgwg-enterprise-pa-multihoming)
Connecting an enterprise site to multiple ISPs using provider-
   assigned addresses is difficult without the use of some form of
   Network Address Translation (NAT).  Much has been written on this
   topic over the last 10 to 15 years, but it still remains a problem
   without a clearly defined or widely implemented solution.  Any
   multihoming solution without NAT requires hosts at the site to have
   addresses from each ISP and to select the egress ISP by selecting a
   source address for outgoing packets.  It also requires routers at the
   site to take into account those source addresses when forwarding
   packets out towards the ISPs.

   This document attempts to define a complete solution to this problem.
   It covers the behavior of routers to forward traffic taking into
   account source address, and it covers the behavior of host to select
   appropriate source addresses.  It also covers any possible role that
   routers might play in providing information to hosts to help them
   select appropriate source addresses.  In the process of exploring
   potential solutions, this documents also makes explicit requirements
   for how the solution would be expected to behave from the perspective
   of an enterprise site network administrator .

### YANG Model for QoS  (draft-asechoud-rtgwg-qos-model)
This document describes a YANG model for Quality of Service (QoS)
   configuration and operational parameters.

### Routing Area Common YANG Data Types  (draft-rtgyangdt-rtgwg-routing-types)
This document defines a collection of common data types using YANG
   data modeling language.  These derived common types are designed to
   be imported by other modules defined in the routing area.

### Common YANG Data Types for the Routing Area  (draft-ietf-rtgwg-routing-types)
This document defines a collection of common data types using the YANG data modeling language.  These derived common types are designed to be imported by other modules defined in the routing area.

### Topology Independent Fast Reroute using Segment Routing  (draft-bashandy-rtgwg-segment-routing-ti-lfa)
This document presents Topology Independent Loop-free Alternate Fast
   Re-route (TI-LFA), aimed at providing protection of node and
   adjacency segments within the Segment Routing (SR) framework.  This
   Fast Re-route (FRR) behavior builds on proven IP-FRR concepts being
   LFAs, remote LFAs (RLFA), and remote LFAs with directed forwarding
   (DLFA).  It extends these concepts to provide guaranteed coverage in
   any IGP network.  A key aspect of TI-LFA is the FRR path selection
   approach establishing protection over post-convergence paths from
   the point of local repair, dramatically reducing the operational
   need to control the tie-breaks among various FRR options.

### A Simple BGP-based Mobile Routing System for the Aeronautical Telecommunications Network  (draft-templin-atn-bgp)
The International Civil Aviation Organization (ICAO) is investigating
   mobile routing solutions for a worldwide Aeronautical
   Telecommunications Network with Internet Protocol Services (ATN/IPS).
   The ATN/IPS will eventually replace existing communication services
   with an IPv6-based service supporting pervasive Air Traffic
   Management (ATM) for Air Traffic Controllers (ATC), Airline
   Operations Controllers (AOC), and all commercial aircraft worldwide.
   This informational document describes a simple and extensible mobile
   routing service based on industry-standard BGP to address the ATN/IPS
   requirements.

### Enterprise Multihoming using Provider-Assigned IPv6 Addresses without Network Prefix Translation: Requirements and Solutions  (draft-ietf-rtgwg-enterprise-pa-multihoming)
Connecting an enterprise site to multiple ISPs over IPv6 using provider-assigned addresses is difficult without the use of some form of Network Address Translation (NAT). Much has been written on this topic over the last 10 to 15 years, but it still remains a problem without a clearly defined or widely implemented solution. Any multihoming solution without NAT requires hosts at the site to have addresses from each ISP and to select the egress ISP by selecting a source address for outgoing packets. It also requires routers at the site to take into account those source addresses when forwarding packets out towards the ISPs.

 This document examines currently available mechanisms for providing a solution to this problem for a broad range of enterprise topologies. It covers the behavior of routers to forward traffic by taking into account source address, and it covers the behavior of hosts to select appropriate default source addresses. It also covers any possible role that routers might play in providing information to hosts to help them select appropriate source addresses. In the process of exploring potential solutions, this document also makes explicit requirements for how the solution would be expected to behave from the perspective of an enterprise site network administrator.

### Routing Timer Parameter Synchronization  (draft-ietf-rtgwg-routing-timer-param-sync)
This document describes a mechanism for a link state routing protocol
   to coordinate the value of a routing timer parameter amongst routers
   in the flooding domain.  The document also defines the solution to
   one specific case: the agreement of a common convergence timer value
   for use by routers in network convergence.

## Working Group: savnet
### Source Address Validation in Inter-domain Networks Gap Analysis, Problem Statement, and Requirements  (draft-wu-savnet-inter-domain-problem-statement)
This document provides the gap analysis of existing inter-domain
   source address validation mechanisms, describes the fundamental
   problems, and defines the requirements for technical improvements.

### Intra-domain Source Address Validation (SAVNET) Architecture  (draft-li-savnet-intra-domain-architecture)
This document proposes the intra-domain SAVNET architecture, which
   achieves accurate source address validation (SAV) in an intra-domain
   network by an automatic way.  Compared with uRPF-like SAV mechanisms
   that only depend on routers' local routing information, SAVNET
   routers generate SAV rules by using both local routing information
   and SAV-specific information exchanged among routers, resulting in
   more accurate SAV validation in asymmetric routing scenarios.
   Compared with ACL rules that require manual efforts to accommodate to
   network dynamics, SAVNET routers learn the SAV rules automatically in
   a distributed way.

### Source Address Validation in Intra-domain Networks Gap Analysis, Problem Statement, and Requirements  (draft-li-savnet-intra-domain-problem-statement)
This document provides the gap analysis of existing intra-domain
   source address validation mechanisms, describes the fundamental
   problems, and defines the requirements for technical improvements.

### Inter-domain Source Address Validation (SAVNET) Architecture  (draft-wu-savnet-inter-domain-architecture)
This document introduces an inter-domain SAVNET architecture for
   performing AS-level SAV and provides a comprehensive framework for
   guiding the design of inter-domain SAV mechanisms.  The proposed
   architecture empowers ASes to generate SAV rules by sharing SAV-
   specific information between themselves, which can be used to
   generate more accurate and trustworthy SAV rules in a timely manner
   compared to the general information.  During the incremental or
   partial deployment of SAV-specific information, it can utilize
   general information to generate SAV rules, if an AS's SAV-specific
   information is unavailable.  Rather than delving into protocol
   extensions or implementations, this document primarily concentrates
   on proposing SAV-specific and general information and guiding how to
   utilize them to generate SAV rules.  To this end, it also defines
   some architectural components and their relations.

### Problem Statement, Gap Analysis, and Requirements for Intra-domain Source Address Validation  (draft-ietf-savnet-intra-domain-problem-statement)
Source address validation (SAV) is an important means to mitigate IP
   source address spoofing [RFC2827].  This document analyzes the gaps
   in current operational mechanisms for intra-domain SAV.  It also
   identifies the properties that new intra-domain SAV mechanisms are
   expected to provide.

### Problem Statement, Gap Analysis, and Requirements for Inter-Domain Source Address Validation  (draft-ietf-savnet-inter-domain-problem-statement)
This document analyzes the problem space and provides a gap analysis
   of existing inter-domain source address validation (SAV) mechanisms.
   Based on these findings, it outlines the technical requirements for
   future improvements.

### General Source Address Validation Capabilities  (draft-ietf-savnet-general-sav-capabilities)
The SAV rules of existing source address validation (SAV) mechanisms,
   are derived from other core data structures, e.g., FIB-based uRPF,
   which are not dedicatedly designed for source filtering.  Therefore
   there are some limitations related to deployable scenarios and
   traffic handling policies.

   To overcome these limitations, this document introduces the general
   SAV capabilities from data plane perspective.  How to implement the
   capabilities and how to generate SAV rules are not in the scope of
   this document.

### Intra-domain Source Address Validation (SAVNET) Architecture  (draft-ietf-savnet-intra-domain-architecture)
This document specifies the architecture of intra-domain SAVNET,
   which aims to achieve accurate source address validation (SAV) at
   external interfaces of an intra-domain network in an automated
   manner.  It describes the conceptual design of intra-domain SAVNET,
   along with its use cases and design requirements, to help ensure that
   the intended objectives are met.

### Source Address Validation Using BGP UPDATEs, ASPA, and ROA (BAR-SAV)  (draft-ietf-sidrops-bar-sav)
Designing an efficient source address validation (SAV) filter
   requires minimizing false positives (i.e., avoiding blocking
   legitimate traffic) while maintaining directionality (see RFC8704).
   This document advances the technology for SAV filter design through a
   method that makes use of BGP UPDATE messages, Autonomous System
   Provider Authorization (ASPA), and Route Origin Authorization (ROA).
   The proposed method's name is abbreviated as BAR-SAV.  BAR-SAV can be
   used by network operators to derive more robust SAV filters and thus
   improve network resilience.  This document updates RFC8704.

### Inter-domain Source Address Validation (SAVNET) Architecture  (draft-ietf-savnet-inter-domain-architecture)
This document introduces an inter-domain SAVNET architecture for
   performing AS-level SAV and provides a comprehensive framework for
   guiding the design of inter-domain SAV mechanisms.  The proposed
   architecture empowers ASes to generate SAV rules by sharing SAV-
   specific information between themselves, which can be used to
   generate more accurate and trustworthy SAV rules in a timely manner
   compared to the general information.  During the incremental or
   partial deployment of SAV-specific information, it can utilize
   general information to generate SAV rules, if an AS's SAV-specific
   information is unavailable.  Rather than delving into protocol
   extensions or implementations, this document primarily concentrates
   on proposing SAV-specific and general information and guiding how to
   utilize them to generate SAV rules.  To this end, it also defines
   some architectural components and their relations.

## Working Group: scitt
### Detailed Software Supply Chain Uses Cases for SCITT  (draft-ietf-scitt-software-use-cases)
This document includes a collection of representative Software Supply
   Chain Use Cases.  These use cases aim to identify software supply
   chain problems that the industry faces today and act as a guideline
   for developing a comprehensive security architecture and solutions
   for these scenarios.

### COSE Receipts with CCF  (draft-birkholz-cose-receipts-ccf-profile)
This document defines a new verifiable data structure type for COSE
   Signed Merkle Tree Proofs specifically designed for transaction
   ledgers produced via Trusted Execution Environments (TEEs), such as
   the Confidential Consortium Framework ([CCF]) to provide stronger
   tamper-evidence guarantees.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/ietf-scitt/draft-birkholz-cose-cometre-ccf-
   profile.

### Supply Chain Integrity, Transparency, and Trust (SCITT) Reference APIs  (draft-ietf-scitt-scrapi)
This document describes a REST API with the HTTP resources, request
   and response messages, and error handling needed for an interoperable
   implementation of a SCITT Transparency Service, as defined by the
   Supply Chain Integrity, Transparency, and Trust (SCITT) Architecture.

### An Architecture for Trustworthy and Transparent Digital Supply Chains  (draft-ietf-scitt-architecture)
Traceability in supply chains is a growing security concern.  While
   verifiable data structures have addressed specific issues, such as
   equivocation over digital certificates, they lack a universal
   architecture for all supply chains.  This document defines such an
   architecture for single-issuer signed statement transparency.  It
   ensures extensibility, interoperability between different
   transparency services, and compliance with various auditing
   procedures and regulatory requirements.

### CCF Profile for COSE Receipts  (draft-ietf-scitt-receipts-ccf-profile)
This document defines a new verifiable data structure (VDS) type for
   COSE Receipts and inclusion proofs specifically designed for append-
   only logs produced by the Confidential Consortium Framework (CCF) to
   provide stronger tamper-evidence guarantees.

## Working Group: spice
### OpenID Connect standard claims registration for CBOR Web Tokens  (draft-maldant-spice-oidc-cwt)
This document registers OpenId Connect standards claims already used
   in JSON Web Tokens for CBOR Web Tokens.

### Use Cases for SPICE  (draft-ietf-spice-use-cases)
This document describes various use cases related to credential
   exchange in a three party model (issuer, holder, verifier).  These
   use cases aid in the identification of which Secure Patterns for
   Internet CrEdentials (SPICE) are most in need of specification or
   detailed documentation.

### SPICE GLUE: GLobal Unique Enterprise (GLUE) Identifiers  (draft-zundel-spice-glue-id)
This specification establishes an IETF URN namespace for GLobal
   Unique Enterprise (GLUE) Identifiers.  It also establishes an IETF
   URN namespace for identifiers defined by the IETF Secure Patterns for
   Internet CrEdentials (SPICE) working group.  The GLUE URN namespace
   is within the SPICE URN namespace.

### Traceability Claims  (draft-prorock-spice-cwt-traceability-claims)
This document defines claims to support traceability of physical
   goods across supply chains, focusing on items such as bills of
   lading, transport modes, and container manifests.  These claims
   standardize the encoding of essential logistics and transport
   metadata, facilitating enhanced transparency and accountability in
   global supply chains.  These claims are registered for use in both
   CBOR Web Tokens (CWTs) and JSON Web Tokens (JWTs).

### A reference architecture for direct presentation credential flows  (draft-johansson-direct-presentation-arch)
This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.

### GLobal Unique Enterprise (GLUE) Identifiers  (draft-ietf-spice-glue-id)
This specification establishes a URI scheme for GLobal Unique
   Enterprise (GLUE) Identifiers.  This enables URI identifiers to be
   used for businesses and organizations.  It enables organizational
   identities from existing authorities to be represented within this
   URI scheme.

### OpenID Connect Standard Claims Registration for CBOR Web Tokens  (draft-ietf-spice-oidc-cwt)
This document registers OpenID Connect standard claims already used
   in JSON Web Tokens for use in CBOR Web Tokens.

### Selective Disclosure CBOR Web Tokens (SD-CWT)  (draft-ietf-spice-sd-cwt)
This specification describes a data minimization technique for use
   with CBOR Web Tokens (CWTs).  The approach is inspired by the
   Selective Disclosure JSON Web Token (SD-JWT), with changes to align
   with CBOR Object Signing and Encryption (COSE) and CWTs.

### A reference architecture for direct presentation credential flows  (draft-ietf-spice-vdcarch)
This document defines a reference architecture for direct
   presentation flows of digital credentials.  The architecture
   introduces the concept of a presentation mediator as the active
   component responsible for managing, presenting, and selectively
   disclosing credentials while preserving a set of security and privacy
   promises that will also be defined.

Discussion Venues

   This note is to be removed before publishing as an RFC.

   Source for this draft and an issue tracker can be found at
   https://github.com/leifj/wallet-refarch.

## Working Group: tcpm
### TCP Extended Data Offset Option  (draft-ietf-tcpm-tcp-edo)
TCP segments include a Data Offset field to indicate space for TCP
   options but the size of the field can limit the space available for
   complex options such as SACK and Multipath TCP and can limit the
   combination of such options supported in a single connection. This
   document updates RFC 9293 with an optional TCP extension to that
   space to support the use of multiple large options. It also explains
   why the initial SYN of a connection cannot be extending a single
   segment.

### CUBIC for Fast and Long-Distance Networks  (draft-ietf-tcpm-rfc8312bis)
CUBIC is a standard TCP congestion control algorithm that uses a cubic function instead of a linear congestion window increase function to improve scalability and stability over fast and long-distance networks. CUBIC has been adopted as the default TCP congestion control algorithm by the Linux, Windows, and Apple stacks.

 This document updates the specification of CUBIC to include algorithmic improvements based on these implementations and recent academic work. Based on the extensive deployment experience with CUBIC, this document also moves the specification to the Standards Track and obsoletes RFC 8312. This document also updates RFC 5681, to allow for CUBIC's occasionally more aggressive sending behavior.

### Survey of Security Hardening Methods for Transmission Control Protocol (TCP) Implementations  (draft-ietf-tcpm-tcp-security)
This document surveys methods to harden Transmission Control Protocol
   (TCP) implementations.  It provides an overview of known attacks and
   refers to the corresponding solutions in the TCP standards.

### Using TCP Selective Acknowledgement (SACK) Information to Determine Duplicate Acknowledgements for Loss Recovery Initiation  (draft-ietf-tcpm-sack-recovery-entry)
This document describes a TCP sender algorithm to trigger loss
 recovery based on the TCP Selective Acknowledgement (SACK)
 information gathered on a SACK scoreboard instead of simply counting
 the number of arriving duplicate acknowledgements (ACKs) in the
 traditional way.  The given algorithm is more robust to ACK losses,
 ACK reordering, missed duplicate acknowledgements due to delayed
 acknowledgements, and extra duplicate acknowledgements due to
 duplicated segments and out-of-window segments. The algorithm allows
 not only a timely initiation of TCP loss recovery but also reduces
 false fast retransmits.  It has a low implementation cost on top of
 the SACK scoreboard defined in RFC 3517.

### Forward RTO-Recovery (F-RTO): An Algorithm for Detecting Spurious Retransmission Timeouts with TCP and the Stream Control Transmission Protocol (SCTP)  (draft-ietf-tcpm-frto)
Spurious retransmission timeouts cause suboptimal TCP performance because they often result in unnecessary retransmission of the last window of data.  This document describes the F-RTO detection algorithm for detecting spurious TCP retransmission timeouts.  F-RTO is a TCP sender-only algorithm that does not require any TCP options to operate.  After retransmitting the first unacknowledged segment triggered by a timeout, the F-RTO algorithm of the TCP sender monitors the incoming acknowledgments to determine whether the timeout was spurious.  It then decides whether to send new segments or retransmit unacknowledged segments.  The algorithm effectively helps to avoid additional unnecessary retransmissions and thereby improves TCP performance in the case of a spurious timeout.  The F-RTO algorithm can also be applied to the Stream Control Transmission Protocol (SCTP).  This memo defines an Experimental Protocol for the Internet community.

### Improving the Robustness of TCP to Non-Congestion Events  (draft-ietf-tcpm-tcp-dcr)
This document specifies Non-Congestion Robustness (NCR) for TCP.  In the absence of explicit congestion notification from the network, TCP uses loss as an indication of congestion.  One of the ways TCP detects loss is using the arrival of three duplicate acknowledgments.  However, this heuristic is not always correct, notably in the case when network paths reorder segments (for whatever reason), resulting in degraded performance.  TCP-NCR is designed to mitigate this degraded performance by increasing the number of duplicate acknowledgments required to trigger loss recovery, based on the current state of the connection, in an effort to better disambiguate true segment loss from segment reordering.  This document specifies the changes to TCP, as well as the costs and benefits of these modifications.  This memo defines an Experimental Protocol for the Internet community.

### Improving TCP's Robustness to Blind In-Window Attacks  (draft-ietf-tcpm-tcpsecure)
TCP has historically been considered to be protected against spoofed off-path packet injection attacks by relying on the fact that it is difficult to guess the 4-tuple (the source and destination IP addresses and the source and destination ports) in combination with the 32-bit sequence number(s).  A combination of increasing window sizes and applications using longer-term connections (e.g., H-323 or Border Gateway Protocol (BGP) [STANDARDS-TRACK]

### A Roadmap for Transmission Control Protocol (TCP) Specification Documents  (draft-ietf-tcpm-tcp-roadmap)
This document contains a "roadmap" to the Requests for Comments (RFC) documents relating to the Internet's Transmission Control Protocol (TCP).  This roadmap provides a brief summary of the documents defining TCP and various TCP extensions that have accumulated in the RFC series.  This serves as a guide and quick reference for both TCP implementers and other parties who desire information contained in the TCP-related RFCs.  This memo provides information for the Internet community.

### Defending TCP Against Spoofing Attacks  (draft-ietf-tcpm-tcp-antispoof)
Recent analysis of potential attacks on core Internet infrastructure indicates an increased vulnerability of TCP connections to spurious resets (RSTs), sent with forged IP source addresses (spoofing).  TCP has always been susceptible to such RST spoofing attacks, which were indirectly protected by checking that the RST sequence number was inside the current receive window, as well as via the obfuscation of TCP endpoint and port numbers.  For pairs of well-known endpoints often over predictable port pairs, such as BGP or between web servers and well-known large-scale caches, increases in the path bandwidth-delay product of a connection have sufficiently increased the receive window space that off-path third parties can brute-force generate a viable RST sequence number.  The susceptibility to attack increases with the square of the bandwidth, and thus presents a significant vulnerability for recent high-speed networks.  This document addresses this vulnerability, discussing proposed solutions at the transport level and their inherent challenges, as well as existing network level solutions and the feasibility of their deployment.  This document focuses on vulnerabilities due to spoofed TCP segments, and includes a discussion of related ICMP spoofing attacks on TCP connections.  This memo provides information for the Internet community.

### TCP User Timeout Option  (draft-ietf-tcpm-tcp-uto)
The TCP user timeout controls how long transmitted data may remain unacknowledged before a connection is forcefully closed.  It is a local, per-connection parameter.  This document specifies a new TCP option -- the TCP User Timeout Option -- that allows one end of a TCP connection to advertise its current user timeout value.  This information provides advice to the other end of the TCP connection to adapt its user timeout accordingly.  Increasing the user timeouts on both ends of a TCP connection allows it to survive extended periods without end-to-end connectivity.  Decreasing the user timeouts allows busy servers to explicitly notify their clients that they will maintain the connection state only for a short time without connectivity. [STANDARDS-TRACK]

### Adding Explicit Congestion Notification (ECN) Capability to TCP's SYN/ACK Packets  (draft-ietf-tcpm-ecnsyn)
The proposal in this document is Experimental. While it may be deployed in the current Internet, it does not represent a consensus that this is the best possible mechanism for the use of Explicit Congestion Notification (ECN) in TCP SYN/ACK packets.

 This document describes an optional, experimental modification to RFC 3168 to allow TCP SYN/ACK packets to be ECN-Capable. For TCP, RFC 3168 specifies setting an ECN-Capable codepoint on data packets, but not on SYN and SYN/ACK packets. However, because of the high cost to the TCP transfer of having a SYN/ACK packet dropped, with the resulting retransmission timeout, this document describes the use of ECN for the SYN/ACK packet itself, when sent in response to a SYN packet with the two ECN flags set in the TCP header, indicating a willingness to use ECN. Setting the initial TCP SYN/ACK packet as ECN-Capable can be of great benefit to the TCP connection, avoiding the severe penalty of a retransmission timeout for a connection that has not yet started placing a load on the network. The TCP responder (the sender of the SYN/ACK packet) must reply to a report of an ECN-marked SYN/ACK packet by resending a SYN/ACK packet that is not ECN-Capable. If the resent SYN/ACK packet is acknowledged, then the TCP responder reduces its initial congestion window from two, three, or four segments to one segment, thereby reducing the subsequent load from that connection on the network. If instead the SYN/ACK packet is dropped, or for some other reason the TCP responder does not receive an acknowledgement in the specified time, the TCP responder follows TCP standards for a dropped SYN/ACK packet (setting the retransmission timer). This memo defines an Experimental Protocol for the Internet community.

### TCP Congestion Control  (draft-ietf-tcpm-rfc2581bis)
This document defines TCP's four intertwined congestion control algorithms: slow start, congestion avoidance, fast retransmit, and fast recovery.  In addition, the document specifies how TCP should begin transmission after a relatively long idle period, as well as discussing various acknowledgment generation methods.  This document obsoletes RFC 2581. [STANDARDS-TRACK]

### TCP's Reaction to Soft Errors  (draft-ietf-tcpm-tcp-soft-errors)
This document describes a non-standard, but widely implemented, modification to TCP's handling of ICMP soft error messages that rejects pending connection-requests when those error messages are received.  This behavior reduces the likelihood of long delays between connection-establishment attempts that may arise in a number of scenarios, including one in which dual-stack nodes that have IPv6 enabled by default are deployed in IPv4 or mixed IPv4 and IPv6 environments.  This memo provides information for the Internet community.

### ICMP Attacks against TCP  (draft-ietf-tcpm-icmp-attacks)
This document discusses the use of the Internet Control Message Protocol (ICMP) to perform a variety of attacks against the Transmission Control Protocol (TCP).  Additionally, this document describes a number of widely implemented modifications to TCP's handling of ICMP error messages that help to mitigate these issues.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### TCP SYN Flooding Attacks and Common Mitigations  (draft-ietf-tcpm-syn-flood)
This document describes TCP SYN flooding attacks, which have been well-known to the community for several years.  Various countermeasures against these attacks, and the trade-offs of each, are described.  This document archives explanations of the attack and common defense techniques for the benefit of TCP implementers and administrators of TCP servers or networks, but does not make any standards-level recommendations.  This memo provides information for the Internet community.

### Forward RTO-Recovery (F-RTO): An Algorithm for Detecting Spurious Retransmission Timeouts with TCP  (draft-ietf-tcpm-rfc4138bis)
The purpose of this document is to move the F-RTO (Forward RTO-Recovery) functionality for TCP in RFC 4138 from Experimental to Standards Track status. The F-RTO support for Stream Control Transmission Protocol (SCTP) in RFC 4138 remains with Experimental status. See Appendix B for the differences between this document and RFC 4138.

 Spurious retransmission timeouts cause suboptimal TCP performance because they often result in unnecessary retransmission of the last window of data. This document describes the F-RTO detection algorithm for detecting spurious TCP retransmission timeouts. F-RTO is a TCP sender-only algorithm that does not require any TCP options to operate. After retransmitting the first unacknowledged segment triggered by a timeout, the F-RTO algorithm of the TCP sender monitors the incoming acknowledgments to determine whether the timeout was spurious. It then decides whether to send new segments or retransmit unacknowledged segments. The algorithm effectively helps to avoid additional unnecessary retransmissions and thereby improves TCP performance in the case of a spurious timeout. [STANDARDS-TRACK]

### TCP Extensions for High Performance  (draft-ietf-tcpm-1323bis)
This document specifies a set of TCP extensions to improve performance over paths with a large bandwidth * delay product and to provide reliable operation over very high-speed paths. It defines the TCP Window Scale (WS) option and the TCP Timestamps (TS) option and their semantics. The Window Scale option is used to support larger receive windows, while the Timestamps option can be used for at least two distinct mechanisms, Protection Against Wrapped Sequences (PAWS) and Round-Trip Time Measurement (RTTM), that are also described herein.

 This document obsoletes RFC 1323 and describes changes from it.

### The TCP Authentication Option  (draft-ietf-tcpm-tcp-auth-opt)
This document specifies the TCP Authentication Option (TCP-AO), which obsoletes the TCP MD5 Signature option of RFC 2385 (TCP MD5).  TCP-AO specifies the use of stronger Message Authentication Codes (MACs), protects against replays even for long-lived TCP connections, and provides more details on the association of security with TCP connections than TCP MD5.  TCP-AO is compatible with either a static Master Key Tuple (MKT) configuration or an external, out-of-band MKT management mechanism; in either case, TCP-AO also protects connections when using the same MKT across repeated instances of a connection, using traffic keys derived from the MKT, and coordinates MKT changes between endpoints.  The result is intended to support current infrastructure uses of TCP MD5, such as to protect long-lived connections (as used, e.g., in BGP and LDP), and to support a larger set of MACs with minimal other system and operational changes.  TCP-AO uses a different option identifier than TCP MD5, even though TCP-AO and TCP MD5 are never permitted to be used simultaneously.  TCP-AO supports IPv6, and is fully compatible with the proposed requirements for the replacement of TCP MD5. [STANDARDS-TRACK]

### TCP Sender Clarification for Persist Condition  (draft-ietf-tcpm-persist)
This document clarifies the Zero Window Probes (ZWPs) described in RFC 1122 ("Requirements for Internet Hosts -- Communication Layers").  In particular, it clarifies the actions that can be taken on connections that are experiencing the ZWP condition.  Rather than making a change to the standard, this document clarifies what has been until now a misinterpretation of the standard as specified in RFC 1122.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Early Retransmit for TCP and Stream Control Transmission Protocol (SCTP)  (draft-ietf-tcpm-early-rexmt)
This document proposes a new mechanism for TCP and Stream Control Transmission Protocol (SCTP) that can be used to recover lost segments when a connection's congestion window is small.  The "Early Retransmit" mechanism allows the transport to reduce, in certain special circumstances, the number of duplicate acknowledgments required to trigger a fast retransmission.  This allows the transport to use fast retransmit to recover segment losses that would otherwise require a lengthy retransmission timeout. [STANDARDS-TRACK]

### On the Implementation of the TCP Urgent Mechanism  (draft-ietf-tcpm-urgent-data)
This document analyzes how current TCP implementations process TCP urgent indications and how the behavior of some widely deployed middleboxes affects how end systems process urgent indications.  This document updates the relevant specifications such that they accommodate current practice in processing TCP urgent indications, raises awareness about the reliability of TCP urgent indications in the Internet, and recommends against the use of urgent indications (but provides advice to applications that do). [STANDARDS-TRACK]

### Reducing the TIME-WAIT State Using TCP Timestamps  (draft-ietf-tcpm-tcp-timestamps)
This document describes an algorithm for processing incoming SYN segments that allows higher connection-establishment rates between any two TCP endpoints when a TCP Timestamps option is present in the incoming SYN segment.  This document only modifies processing of SYN segments received for connections in the TIME-WAIT state; processing in all other states is unchanged.  This memo documents an Internet Best Current Practice.

### Cryptographic Algorithms, Use, & Implementation Requirments for TCP Authentication Option  (draft-lebovitz-ietf-tcpm-tcp-ao-crypto)
The TCP Authentication Option, TCP-AO, relies on security algorithms
to provide authentication between two end-points.  There are many
such algorithms available, and two TCP-AO systems cannot interoperate
unless they are using the same algorithm(s).  This document specifies
the algorithms and attributes that can be used in TCP-AO's current
manual keying mechanism.

### Cryptographic Algorithms for the TCP Authentication Option (TCP-AO)  (draft-ietf-tcpm-tcp-ao-crypto)
The TCP Authentication Option (TCP-AO) relies on security algorithms to provide authentication between two end-points.  There are many such algorithms available, and two TCP-AO systems cannot interoperate unless they are using the same algorithms.  This document specifies the algorithms and attributes that can be used in TCP-AO's current manual keying mechanism and provides the interface for future message authentication codes (MACs). [STANDARDS-TRACK]

### TCP Options and Maximum Segment Size (MSS)  (draft-ietf-tcpm-tcpmss)
This memo discusses what value to use with the TCP Maximum Segment Size (MSS) option, and updates RFC 879 and RFC 2385.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Making TCP More Robust to Long Connectivity Disruptions (TCP-LCD)  (draft-ietf-tcpm-tcp-lcd)
Disruptions in end-to-end path connectivity, which last longer than one retransmission timeout, cause suboptimal TCP performance. The reason for this performance degradation is that TCP interprets segment loss induced by long connectivity disruptions as a sign of congestion, resulting in repeated retransmission timer backoffs. This, in turn, leads to a delayed detection of the re-establishment of the connection since TCP waits for the next retransmission timeout before it attempts a retransmission.

 This document proposes an algorithm to make TCP more robust to long connectivity disruptions (TCP-LCD). It describes how standard ICMP messages can be exploited during timeout-based loss recovery to disambiguate true congestion loss from non-congestion loss caused by connectivity disruptions. Moreover, a reversion strategy of the retransmission timer is specified that enables a more prompt detection of whether or not the connectivity to a previously disconnected peer node has been restored. TCP-LCD is a TCP sender- only modification that effectively improves TCP performance in the case of connectivity disruptions. This document defines an Experimental Protocol for the Internet community.

### Computing TCP's Retransmission Timer  (draft-paxson-tcpm-rfc2988bis)
This document defines the standard algorithm that Transmission Control Protocol (TCP) senders are required to use to compute and manage their retransmission timer.  It expands on the discussion in Section 4.2.3.1 of RFC 1122 and upgrades the requirement of supporting the algorithm from a SHOULD to a MUST.  This document obsoletes RFC 2988. [STANDARDS-TRACK]

### Support for Stronger Error Detection Codes in TCP for Jumbo Frames  (draft-ietf-tcpm-anumita-tcp-stronger-checksum)
There is a class of data serving protocols and applications that
cannot tolerate undetected data corruption on the wire.  Data
corruption could occur at the source in software, in the network
interface card, out on the link, on intermediate routers or at the
destination network interface card or node.  The Ethernet CRC and the
16-bit checksum in the TCP/UDP headers are used to detect data
errors.  Most applications rely on these checksums to detect data
corruptions and do not use any checksums or CRC checks at their
level.  Research has shown that the TCP/UDP checksums are catching a
significant number of errors, however, the research suggests that one
packet in 10 billion will have an error that goes undetected for
Ethernet MTU frames (MTU of 1500).  Under certain situations, "bad"
hosts can introduce undetected errors at a much higher frequency and
order.  With the use of Jumbo frames on the rise, and therefore more
data bits on the wire that could be corrupted, the current 16-bit
TCP/UDP checksum, or the Ethernet 32-bit CRC are simply not
sufficient for detecting errors.  This document specifies a proposal
to use stronger checksum algorithms for TCP Jumbo Frames for IPv4 and
IPv6 networks.  The Castagnoli CRC 32C algorithm used in iSCSI and
SCTP is proposed as the error detection code of choice.

### Moving the Undeployed TCP Extensions RFC 1072, RFC 1106, RFC 1110, RFC 1145, RFC 1146, RFC 1379, RFC 1644, and RFC 1693 to Historic Status  (draft-eggert-tcpm-historicize)
This document reclassifies several TCP extensions that have never seen widespread use to Historic status.  The affected RFCs are RFC 1072, RFC 1106, RFC 1110, RFC 1145, RFC 1146, RFC 1379, RFC 1644, and RFC 1693.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Increasing TCP's Initial Window  (draft-ietf-tcpm-initcwnd)
This document proposes an experiment to increase the permitted TCP initial window (IW) from between 2 and 4 segments, as specified in RFC 3390, to 10 segments with a fallback to the existing recommendation when performance issues are detected.  It discusses the motivation behind the increase, the advantages and disadvantages of the higher initial window, and presents results from several large-scale experiments showing that the higher initial window improves the overall performance of many web services without resulting in a congestion collapse.  The document closes with a discussion of usage and deployment for further experimental purposes recommended by the IETF TCP Maintenance and Minor Extensions (TCPM) working group.

### The NewReno Modification to TCP's Fast Recovery Algorithm  (draft-ietf-tcpm-rfc3782-bis)
RFC 5681 documents the following four intertwined TCP congestion control algorithms: slow start, congestion avoidance, fast retransmit, and fast recovery.  RFC 5681 explicitly allows certain modifications of these algorithms, including modifications that use the TCP Selective Acknowledgment (SACK) option (RFC 2883), and modifications that respond to "partial acknowledgments" (ACKs that cover new data, but not all the data outstanding when loss was detected) in the absence of SACK.  This document describes a specific algorithm for responding to partial acknowledgments, referred to as "NewReno".  This response to partial acknowledgments was first proposed by Janey Hoe.  This document obsoletes RFC 3782. [STANDARDS-TRACK]

### Defending against Sequence Number Attacks  (draft-ietf-tcpm-rfc1948bis)
This document specifies an algorithm for the generation of TCP Initial Sequence Numbers (ISNs), such that the chances of an off-path attacker guessing the sequence numbers in use by a target connection are reduced.  This document revises (and formally obsoletes) RFC 1948, and takes the ISN generation algorithm originally proposed in that document to Standards Track, formally updating RFC 793. [STANDARDS-TRACK]

### Proportional Rate Reduction for TCP  (draft-ietf-tcpm-proportional-rate-reduction)
This document describes an experimental Proportional Rate Reduction (PRR) algorithm as an alternative to the widely deployed Fast Recovery and Rate-Halving algorithms.  These algorithms determine the amount of data sent by TCP during loss recovery.  PRR minimizes excess window adjustments, and the actual window size at the end of recovery will be as close as possible to the ssthresh, as determined by the congestion control algorithm.

### A Conservative Loss Recovery Algorithm Based on Selective Acknowledgment (SACK) for TCP  (draft-ietf-tcpm-3517bis)
This document presents a conservative loss recovery algorithm for TCP that is based on the use of the selective acknowledgment (SACK) TCP option.  The algorithm presented in this document conforms to the spirit of the current congestion control specification (RFC 5681), but allows TCP senders to recover more effectively when multiple segments are lost from a single flight of data.  This document obsoletes RFC 3517 and describes changes from it. [STANDARDS-TRACK]

### Shared Use of Experimental TCP Options  (draft-ietf-tcpm-experimental-options)
This document describes how the experimental TCP option codepoints can concurrently support multiple TCP extensions, even within the same connection, using a new IANA TCP experiment identifier.  This approach is robust to experiments that are not registered and to those that do not use this sharing mechanism.  It is recommended for all new TCP options that use these codepoints.

### TCP Fast Open  (draft-ietf-tcpm-fastopen)
This document describes an experimental TCP mechanism called TCP Fast Open (TFO).  TFO allows data to be carried in the SYN and SYN-ACK packets and consumed by the receiving end during the initial connection handshake, and saves up to one full round-trip time (RTT) compared to the standard TCP, which requires a three-way handshake (3WHS) to complete before data can be exchanged.  However, TFO deviates from the standard TCP semantics, since the data in the SYN could be replayed to an application in some rare circumstances.  Applications should not use TFO unless they can tolerate this issue, as detailed in the Applicability section.

### Problem Statement and Requirements for Increased Accuracy in Explicit Congestion Notification (ECN) Feedback  (draft-ietf-tcpm-accecn-reqs)
Explicit Congestion Notification (ECN) is a mechanism where network nodes can mark IP packets, instead of dropping them, to indicate congestion to the endpoints.  An ECN-capable receiver will feed this information back to the sender.  ECN is specified for TCP in such a way that it can only feed back one congestion signal per Round-Trip Time (RTT).  In contrast, ECN for other transport protocols, such as RTP/UDP and SCTP, is specified with more accurate ECN feedback.  Recent new TCP mechanisms (like Congestion Exposure (ConEx) or Data Center TCP (DCTCP)) need more accurate ECN feedback in the case where more than one marking is received in one RTT.  This document specifies requirements for an update to the TCP protocol to provide more accurate ECN feedback.

### Updating TCP to Support Rate-Limited Traffic  (draft-ietf-tcpm-newcwv)
This document provides a mechanism to address issues that arise when TCP is used for traffic that exhibits periods where the sending rate is limited by the application rather than the congestion window. It provides an experimental update to TCP that allows a TCP sender to restart quickly following a rate-limited interval. This method is expected to benefit applications that send rate-limited traffic using TCP while also providing an appropriate response if congestion is experienced.

 This document also evaluates the Experimental specification of TCP Congestion Window Validation (CWV) defined in RFC 2861 and concludes that RFC 2861 sought to address important issues but failed to deliver a widely used solution. This document therefore reclassifies the status of RFC 2861 from Experimental to Historic. This document obsoletes RFC 2861.

### TCP and Stream Control Transmission Protocol (SCTP) RTO Restart  (draft-ietf-tcpm-rtorestart)
This document describes a modified sender-side algorithm for managing the TCP and Stream Control Transmission Protocol (SCTP) retransmission timers that provides faster loss recovery when there is a small amount of outstanding data for a connection.  The modification, RTO Restart (RTOR), allows the transport to restart its retransmission timer using a smaller timeout duration, so that the effective retransmission timeout (RTO) becomes more aggressive in situations where fast retransmit cannot be used.  This enables faster loss detection and recovery for connections that are short lived or application limited.

### A Roadmap for Transmission Control Protocol (TCP) Specification Documents  (draft-ietf-tcpm-tcp-rfc4614bis)
This document contains a roadmap to the Request for Comments (RFC) documents relating to the Internet's Transmission Control Protocol (TCP). This roadmap provides a brief summary of the documents defining TCP and various TCP extensions that have accumulated in the RFC series. This serves as a guide and quick reference for both TCP implementers and other parties who desire information contained in the TCP-related RFCs.

 This document obsoletes RFC 4614.

### Moving Outdated TCP Extensions and TCP-Related Documents to Historic or Informational Status  (draft-ietf-tcpm-undeployed)
This document reclassifies several TCP extensions and TCP-related documents that either have been superseded, have never seen widespread use, or are no longer recommended for use to "Historic" status.  The affected documents are RFCs 675, 721, 761, 813, 816, 879, 896, 1078, and 6013.  Additionally, this document reclassifies RFCs 700, 794, 814, 817, 872, 889, 964, and 1071 to "Informational" status.

### CUBIC for Fast Long-Distance Networks  (draft-ietf-tcpm-cubic)
CUBIC is an extension to the current TCP standards.  It differs from the current TCP standards only in the congestion control algorithm on the sender side.  In particular, it uses a cubic function instead of a linear window increase function of the current TCP standards to improve scalability and stability under fast and long-distance networks.  CUBIC and its predecessor algorithm have been adopted as defaults by Linux and have been used for many years.  This document provides a specification of CUBIC to enable third-party implementations and to solicit community feedback through experimentation on the performance of CUBIC.

### Transmission Control Protocol (TCP)  (draft-ietf-tcpm-rfc793bis)
This document specifies the Transmission Control Protocol (TCP).  TCP is an important transport-layer protocol in the Internet protocol stack, and it has continuously evolved over decades of use and growth of the Internet.  Over this time, a number of changes have been made to TCP as it was specified in RFC 793, though these have only been documented in a piecemeal fashion.  This document collects and brings those changes together with the protocol specification from RFC 793.  This document obsoletes RFC 793, as well as RFCs 879, 2873, 6093, 6429, 6528, and 6691 that updated parts of RFC 793.  It updates RFCs 1011 and 1122, and it should be considered as a replacement for the portions of those documents dealing with TCP requirements.  It also updates RFC 5961 by adding a small clarification in reset handling while in the SYN-RECEIVED state.  The TCP header control bits from RFC 793 have also been updated based on RFC 3168.

### Data Center TCP (DCTCP): TCP Congestion Control for Data Centers  (draft-ietf-tcpm-dctcp)
This Informational RFC describes Data Center TCP (DCTCP): a TCP congestion control scheme for data-center traffic.  DCTCP extends the Explicit Congestion Notification (ECN) processing to estimate the fraction of bytes that encounter congestion rather than simply detecting that some congestion has occurred.  DCTCP then scales the TCP congestion window based on this estimate.  This method achieves high-burst tolerance, low latency, and high throughput with shallow- buffered switches.  This memo also discusses deployment issues related to the coexistence of DCTCP and conventional TCP, discusses the lack of a negotiating mechanism between sender and receiver, and presents some possible mitigations.  This memo documents DCTCP as currently implemented by several major operating systems.  DCTCP, as described in this specification, is applicable to deployments in controlled environments like data centers, but it must not be deployed over the public Internet without additional measures.

### Requirements for Time-Based Loss Detection  (draft-ietf-tcpm-rto-consider)
Many protocols must detect packet loss for various reasons (e.g., to ensure reliability using retransmissions or to understand the level of congestion along a network path).  While many mechanisms have been designed to detect loss, ultimately, protocols can only count on the passage of time without delivery confirmation to declare a packet "lost".  Each implementation of a time-based loss detection mechanism represents a balance between correctness and timeliness; therefore, no implementation suits all situations.  This document provides high-level requirements for time-based loss detectors appropriate for general use in unicast communication across the Internet.  Within the requirements, implementations have latitude to define particulars that best address each situation.

### The RACK-TLP Loss Detection Algorithm for TCP  (draft-ietf-tcpm-rack)
This document presents the RACK-TLP loss detection algorithm for TCP.  RACK-TLP uses per-segment transmit timestamps and selective acknowledgments (SACKs) and has two parts.  Recent Acknowledgment (RACK) starts fast recovery quickly using time-based inferences derived from acknowledgment (ACK) feedback, and Tail Loss Probe (TLP) leverages RACK and sends a probe packet to trigger ACK feedback to avoid retransmission timeout (RTO) events.  Compared to the widely used duplicate acknowledgment (DupAck) threshold approach, RACK-TLP detects losses more efficiently when there are application-limited flights of data, lost retransmissions, or data packet reordering events.  It is intended to be an alternative to the DupAck threshold approach.

### TCP Alternative Backoff with ECN (ABE)  (draft-ietf-tcpm-alternativebackoff-ecn)
Active Queue Management (AQM) mechanisms allow for burst tolerance while enforcing short queues to minimise the time that packets spend enqueued at a bottleneck.  This can cause noticeable performance degradation for TCP connections traversing such a bottleneck, especially if there are only a few flows or their bandwidth-delay product (BDP) is large.  The reception of a Congestion Experienced (CE) Explicit Congestion Notification (ECN) mark indicates that an AQM mechanism is used at the bottleneck, and the bottleneck network queue is therefore likely to be short.  Feedback of this signal allows the TCP sender-side ECN reaction in congestion avoidance to reduce the Congestion Window (cwnd) by a smaller amount than the congestion control algorithm's reaction to inferred packet loss.  Therefore, this specification defines an experimental change to the TCP reaction specified in RFC 3168, as permitted by RFC 8311.

### 0-RTT TCP Convert Protocol  (draft-ietf-tcpm-converters)
This document specifies an application proxy, called Transport Converter, to assist the deployment of TCP extensions such as Multipath TCP. A Transport Converter may provide conversion service for one or more TCP extensions. The conversion service is provided by means of the 0-RTT TCP Convert Protocol (Convert).

 This protocol provides 0-RTT (Zero Round-Trip Time) conversion service since no extra delay is induced by the protocol compared to connections that are not proxied. Also, the Convert Protocol does not require any encapsulation (no tunnels whatsoever).

 This specification assumes an explicit model, where the Transport Converter is explicitly configured on hosts. As a sample applicability use case, this document specifies how the Convert Protocol applies for Multipath TCP.

### TCP Control Block Interdependence  (draft-ietf-tcpm-2140bis)
This memo provides guidance to TCP implementers that is intended to help improve connection convergence to steady-state operation without affecting interoperability.  It updates and replaces RFC 2140's description of sharing TCP state, as typically represented in TCP Control Blocks, among similar concurrent or consecutive connections.

### HyStart++: Modified Slow Start for TCP  (draft-ietf-tcpm-hystartplusplus)
This document describes HyStart++, a simple modification to the slow start phase of congestion control algorithms.  Slow start can overshoot the ideal send rate in many cases, causing high packet loss and poor performance.  HyStart++ uses increase in round-trip delay as a heuristic to find an exit point before possible overshoot.  It also adds a mitigation to prevent jitter from causing premature slow start exit.

### TCP Authentication Option (TCP-AO) Test Vectors  (draft-ietf-tcpm-ao-test-vectors)
This document provides test vectors to validate implementations of the two mandatory authentication algorithms specified for the TCP Authentication Option over both IPv4 and IPv6.  This includes validation of the key derivation function (KDF) based on a set of test connection parameters as well as validation of the message authentication code (MAC).  Vectors are provided for both currently required pairs of KDF and MAC algorithms: KDF_HMAC_SHA1 and HMAC- SHA-1-96, and KDF_AES_128_CMAC and AES-128-CMAC-96.  The vectors also validate both whole TCP segments as well as segments whose options are excluded for middlebox traversal.

### A YANG Model for Transmission Control Protocol (TCP) Configuration and State  (draft-ietf-tcpm-yang-tcp)
This document specifies a minimal YANG model for TCP on devices that
   are configured and managed by network management protocols.  The YANG
   model defines a container for all TCP connections, and groupings of
   authentication parameters that can be imported and used in TCP
   implementations or by other models that need to configure TCP
   parameters.  The model also includes basic TCP statistics.  The model
   is compliant with Network Management Datastore Architecture (NMDA)
   (RFC 8342).

### ECN++: Adding Explicit Congestion Notification (ECN) to TCP Control Packets  (draft-ietf-tcpm-generalized-ecn)
This document specifies an experimental modification to ECN when used
   with TCP.  It allows the use of ECN in the IP header of the following
   TCP packets: SYNs, SYN/ACKs, pure ACKs, Window probes, FINs, RSTs and
   retransmissions.  This specification obsoletes RFC5562, which
   described a different way to use ECN on SYN/ACKs alone.

### Improve TCP Handling of Out-of-Window Packets to Mitigate Ghost ACKs  (draft-ietf-tcpm-tcp-ghost-acks)
Historically, TCP as specified in RFC 793 was threatened by the blind
   data injection attack because of the loose SEG.ACK value validation,
   where the SEG.ACK value of a TCP segment is considered valid as long
   as it does not acknowledge data ahead of what has been sent.  RFC
   5961 improved the input validation by shrinking the range of
   acceptable SEG.ACK values in a TCP segment.  Later, RFC 9293
   incorporated the updates proposed by RFC 5961 as a TCP stack
   implementation option.
   However, an endpoint that follows the RFC 9293 specifications can
   still accept a TCP segment containing an SEG.ACK value acknowledging
   data that the endpoint has never sent.  This document specifies small
   modifications to the way TCP verifies incoming TCP segments' SEG.ACK
   value to prevent TCP from accepting such invalid SEG.ACK values.

### Proportional Rate Reduction  (draft-ietf-tcpm-prr-rfc6937bis)
This document specifies a standards-track version of the Proportional
   Rate Reduction (PRR) algorithm that obsoletes the experimental
   version described in RFC6937.  PRR regulates the amount of data sent
   by TCP or other transport protocols during fast recovery.  PRR
   accurately regulates the actual flight size through recovery such
   that at the end of recovery it will be as close as possible to the
   slow start threshold (ssthresh), as determined by the congestion
   control algorithm.

### TCP ACK Rate Request Option  (draft-ietf-tcpm-ack-rate-request)
TCP Delayed Acknowledgments (ACKs) is a widely deployed mechanism
   that allows reducing protocol overhead in many scenarios.  However,
   Delayed ACKs may also contribute to suboptimal performance.  When a
   relatively large congestion window (cwnd) can be used, less frequent
   ACKs may be desirable.  On the other hand, in relatively small cwnd
   scenarios, eliciting an immediate ACK may avoid unnecessary delays
   that may be incurred by the Delayed ACKs mechanism.  This document
   specifies the TCP ACK Rate Request (TARR) option.  This option allows
   a sender to request the ACK rate to be used by a receiver, and it
   also allows to request immediate ACKs from a receiver.

### More Accurate Explicit Congestion Notification (AccECN) Feedback in TCP  (draft-ietf-tcpm-accurate-ecn)
Explicit Congestion Notification (ECN) is a mechanism where network
   nodes can mark IP packets instead of dropping them to indicate
   incipient congestion to the endpoints.  Receivers with an ECN-capable
   transport protocol feed back this information to the sender.  ECN was
   originally specified for TCP in such a way that only one feedback
   signal can be transmitted per Round-Trip Time (RTT).  Recent new TCP
   mechanisms like Congestion Exposure (ConEx), Data Center TCP (DCTCP)
   or Low Latency, Low Loss, and Scalable Throughput (L4S) need more
   Accurate ECN (AccECN) feedback information whenever more than one
   marking is received in one RTT.  This document updates the original
   ECN specification in RFC 3168 to specify a scheme that provides more
   than one feedback signal per RTT in the TCP header.  Given TCP header
   space is scarce, it allocates a reserved header bit previously
   assigned to the ECN-Nonce.  It also overloads the two existing ECN
   flags in the TCP header.  The resulting extra space is additionally
   exploited to feed back the IP-ECN field received during the TCP
   connection establishment.  Supplementary feedback information can
   optionally be provided in two new TCP option alternatives, which are
   never used on the TCP SYN.  The document also specifies the treatment
   of this updated TCP wire protocol by middleboxes.

### Additional Cryptographic Algorithms For Use With TCP-AO  (draft-ietf-tcpm-tcp-ao-algs)
RFC5926 creates a list of cryptographic algorithms that can be used
   with TCP-AO.  This document expands that list, adding two Message
   Authentication Code (MAC) algorithms, HMAC-SHA256-128 and
   KMAC256-128.  For each MAC algorithm, a corresponding Key Derivation
   Function (KDF) is also added.

   The MAC algorithms described by this document produce 128-bit (i.e.,
   16-byte) MACs.  When 16-byte MACs are encoded in TCP-AO, the TCP-AO
   consumes 20 bytes.  This does not challenge TCP's 40-byte option size
   limitation.

### TCP RST Diagnostic Payload  (draft-ietf-tcpm-rst-diagnostic-payload)
This document specifies an experimental diagnostic payload format
   returned in TCP RST segments.  Such payloads are used to share with
   an endpoint the reasons for which a TCP connection has been reset.
   Sharing this information is meant to ease diagnostic and
   troubleshooting.

   This specification builds on provisions that are already present in
   RFC 9293 "Transmission Control Protocol (TCP)".  As such, this
   document does not require any change to RFC 9293.

## Working Group: tls
### Using the Secure Remote Password (SRP) Protocol for TLS Authentication  (draft-ietf-tls-srp)
This memo presents a technique for using the Secure Remote Password protocol as an authentication method for the Transport Layer Security protocol.  This memo provides information for the Internet community.

### TLS Flag - Request mTLS  (draft-jhoyla-req-mtls-flag)
Normally in TLS there is no way for the client to signal to the
   server that it has been configured with a certificate suitable for
   mTLS.  This document defines a TLS Flag [I-D.ietf-tls-tlsflags] that
   enables clients to provide this hint.

### ML-KEM Post-Quantum Key Agreement for TLS 1.3  (draft-connolly-tls-mlkem-key-agreement)
This memo defines ML-KEM-512, ML-KEM-768, and ML-KEM-1024 as a
   standalone NamedGroups for use in TLS 1.3 to achieve post-quantum key
   agreement.

### Delegated Credentials for TLS and DTLS  (draft-ietf-tls-subcerts)
The organizational separation between operators of TLS and DTLS endpoints and the certification authority can create limitations.  For example, the lifetime of certificates, how they may be used, and the algorithms they support are ultimately determined by the Certification Authority (CA).  This document describes a mechanism to overcome some of these limitations by enabling operators to delegate their own credentials for use in TLS and DTLS without breaking compatibility with peers that do not support this specification.

### Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3  (draft-ietf-tls-ecdhe-mlkem)
This draft defines three hybrid key agreement mechanisms for TLS 1.3
   - X25519MLKEM768, SecP256r1MLKEM768, and SecP384r1MLKEM1024 - that
   combine the post-quantum ML-KEM (Module-Lattice-Based Key
   Encapsulation Mechanism) with an ECDHE (Elliptic Curve Diffie-
   Hellman) exchange.

### Abridged Compression for WebPKI Certificates  (draft-jackson-tls-cert-abridge)
This draft defines a new TLS Certificate Compression scheme which
   uses a shared dictionary of root and intermediate WebPKI
   certificates.  The scheme smooths the transition to post-quantum
   certificates by eliminating the root and intermediate certificates
   from the TLS certificate chain without impacting trust negotiation.
   It also delivers better compression than alternative proposals whilst
   ensuring fair treatment for both CAs and website operators.  It may
   also be useful in other applications which store certificate chains,
   e.g.  Certificate Transparency logs.

### TLS Trust Anchor Identifiers  (draft-ietf-tls-trust-anchor-ids)
This document defines the TLS Trust Anchors extension, a mechanism
   for relying parties to convey trusted certification authorities.  It
   describes individual certification authorities more succinctly than
   the TLS Certificate Authorities extension.

   Additionally, to support TLS clients with many trusted certification
   authorities, it supports a mode where servers describe their
   available certification paths and the client selects from them.
   Servers may describe this during connection setup, or in DNS for
   lower latency.

### TLS Key Share Prediction  (draft-ietf-tls-key-share-prediction)
This document defines a mechanism for servers to communicate
   supported key share algorithms in DNS.  Clients may use this
   information to reduce TLS handshake round-trips.

### Use of ML-DSA in TLS 1.3  (draft-ietf-tls-mldsa)
This memo specifies how the post-quantum signature scheme ML-DSA
   (FIPS 204) is used for authentication in TLS 1.3.

### Extended Key Update for Transport Layer Security (TLS) 1.3  (draft-tschofenig-tls-extended-key-update)
The Transport Layer Security (TLS) 1.3 specification offers a
   dedicated message to update cryptographic keys during the lifetime of
   an ongoing session.  The traffic secret and the initialization vector
   are updated directionally but the sender may trigger the recipient,
   via the request_update field, to transmit a key update message in the
   reverse direction.

   In environments where sessions are long-lived, such as industrial IoT
   or telecommunication networks, this key update alone is insufficient
   since forward secrecy is not offered via this mechanism.  Earlier
   versions of TLS allowed the two peers to perform renegotiation, which
   is a handshake that establishes new cryptographic parameters for an
   existing session.  When a security vulnerability with the
   renegotiation mechanism was discovered, RFC 5746 was developed as a
   fix.  Renegotiation has, however, been removed from version 1.3
   leaving a gap in the feature set of TLS.

   This specification defines an extended key update that supports
   forward secrecy.

### Abridged Compression for WebPKI Certificates  (draft-ietf-tls-cert-abridge)
This draft defines a new TLS Certificate Compression scheme which
   uses a shared dictionary of root and intermediate WebPKI
   certificates.  The scheme smooths the transition to post-quantum
   certificates by eliminating the root and intermediate certificates
   from the TLS certificate chain without impacting trust negotiation.
   It also delivers better compression than alternative proposals whilst
   ensuring fair treatment for both CAs and website operators.  It may
   also be useful in other applications which store certificate chains,
   e.g.  Certificate Transparency logs.

### The SSLKEYLOGFILE Format for TLS  (draft-ietf-tls-keylogfile)
A format that supports logging information about the secrets used in
   a TLS connection is described.  Recording secrets to a file in
   SSLKEYLOGFILE format allows diagnostic and logging tools that use
   this file to decrypt messages exchanged by TLS endpoints.  This
   format is intended for use in systems where TLS only protects test
   data.

### Compact TLS 1.3  (draft-ietf-tls-ctls)
This document specifies a "compact" version of TLS 1.3 and DTLS 1.3.
   It saves bandwidth by trimming obsolete material, tighter encoding, a
   template-based specialization technique, and alternative
   cryptographic techniques. cTLS is not directly interoperable with TLS
   1.3 or DTLS 1.3 since the over-the-wire framing is different.  A
   single server can, however, offer cTLS alongside TLS or DTLS.

### Guidance for External Pre-Shared Key (PSK) Usage in TLS  (draft-ietf-tls-external-psk-guidance)
This document provides usage guidance for external Pre-Shared Keys (PSKs) in Transport Layer Security (TLS) 1.3 as defined in RFC 8446.  It lists TLS security properties provided by PSKs under certain assumptions, then it demonstrates how violations of these assumptions lead to attacks.  Advice for applications to help meet these assumptions is provided.  This document also discusses PSK use cases and provisioning processes.  Finally, it lists the privacy and security properties that are not provided by TLS 1.3 when external PSKs are used.

### TLS Key Share Prediction  (draft-davidben-tls-key-share-prediction)
This document defines a mechanism for servers to communicate key
   share preferences in DNS.  Clients may use this information to reduce
   TLS handshake round-trips.

### Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS) Versions 1.2 and Earlier  (draft-nir-tls-rfc4492bis)
This document describes key exchange algorithms based on Elliptic
   Curve Cryptography (ECC) for the Transport Layer Security (TLS)
   protocol.  In particular, it specifies the use of Elliptic Curve
   Diffie-Hellman (ECDH) key agreement in a TLS handshake and the use of
   Elliptic Curve Digital Signature Algorithm (ECDSA) as a new
   authentication mechanism.

### Addition of Shared Key Authentication to Transport Layer Security (TLS)  (draft-ietf-tls-passauth)
This document presents a shared-key authentication mechanism for the TLS protocol.  It is intended to allow TLS clients to authenticate using a secret key (such as a password) shared with either the server or a third-party authentication service.  The security of the secret authentication key is augmented by its integration into the normal SSL/TLS server authentication/key exchange mechanism.

### The SSL Protocol Version 3.0  (draft-ietf-tls-ssl-version3)
This document specifies Version 3.0 of the Secure Sockets Layer (SSL V3.0) protocol, a security protocol that provides communications privacy over the Internet.  The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery.

### SSH Transport Layer Protocol  (draft-ietf-tls-ssh)
This document describes the SSH transport layer protocol.  The protocol can be used as a basis for a number of secure network services.  It provides strong encryption, mutual authentication, and integrity protection.

### Addition of Kerberos Cipher Suites to Transport Layer Security (TLS)  (draft-ietf-tls-kerb-cipher-suites)
This document proposes the addition of new cipher suites to the TLS protocol to support Kerberos-based authentication. [STANDARDS-TRACK]

### Modifications to the SSL protocol for TLS  (draft-ietf-tls-ssl-mods)
This document recommends for several modifications be made to the SSL 3.0 protocol as it is standardized by the IETF under the name of TLS.  These changes primarily standardize various technical details of the protocol and make some other minor modifications.

### The TLS Protocol Version 1.0  (draft-ietf-tls-protocol)
This document specifies Version 1.0 of the Transport Layer Security (TLS) protocol.  The TLS protocol provides communications privacy over the Internet.  The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery.

### HTTP Over TLS  (draft-ietf-tls-https)
This memo describes how to use Transport Layer Security (TLS) to secure Hypertext Transfer Protocol (HTTP) connections over the Internet.  This memo provides information for the Internet community.

### TLS extensions for AttributeCertificate based authorization  (draft-ietf-tls-attr-cert)
This document describes extensions to [TLS] providing
   authorization support based on the use of X.509
   AttributeCertificates.

### Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS)  (draft-ietf-tls-ecc)
This document describes new key exchange algorithms based on Elliptic Curve Cryptography (ECC) for the Transport Layer Security (TLS) protocol.  In particular, it specifies the use of Elliptic Curve Diffie-Hellman (ECDH) key agreement in a TLS handshake and the use of Elliptic Curve Digital Signature Algorithm (ECDSA) as a new authentication mechanism.  This memo provides information for the Internet community.

### Transport Layer Security (TLS) Application-Layer Protocol Negotiation Extension  (draft-ietf-tls-applayerprotoneg)
This document describes a Transport Layer Security (TLS) extension for application-layer protocol negotiation within the TLS handshake.  For instances in which multiple application protocols are supported on the same TCP or UDP port, this extension allows the application layer to negotiate which protocol will be used within the TLS connection.

### An Internet AttributeCertificate Profile for Authorization  (draft-ietf-tls-ac509prof)
Authorization support is required for various Internet
   protocols, for example, TLS, CMS and their consumers,
   and others. The X.509 AttributeCertificate provides a
   structure which can form the basis for such services
   [X.509]. This specification defines two profiles (a
   simple one and a 'full' one)  for the use of X.509
   AttributeCertificates to provide such authorization
   services.

### NTRU Cipher Suites for TLS  (draft-ietf-tls-ntru)
This document defines a group of new TLS cipher suites that utilize 
the NTRU encryption algorithm and the NSS signature algorithm.  
These cipher suites are designed to maximize computational 
efficiency on both the client and server sides and ease deployment 
of the TLS protocol on constrained and embedded devices.  The 
document assumes the reader is familiar with the TLS protocol.

### Upgrading to TLS Within HTTP/1.1  (draft-ietf-tls-http-upgrade)
This memo explains how to use the Upgrade mechanism in HTTP/1.1 to initiate Transport Layer Security (TLS) over an existing TCP connection. [STANDARDS-TRACK]

### 56-bit Export Cipher Suites For TLS  (draft-ietf-tls-56-bit-ciphersuites)
This document describes several cipher suites to be used with the 
Transport Layer Security (TLS) protocol.  Changes in US export
regulations in 1999 permitted the export of software programs 
using 56-bit data encryption and 1024-bit key exchange.  
The cipher suites described in this document were designed to take
advantage of this change in the regulations.

### Extensions to TLS for OpenPGP keys  (draft-ietf-tls-openpgp)
This document builds upon the TLS Protocol Specification [TLS].  The
extensions described herein are intended to apply to Version 1.0 of
the TLS specification.
The purpose of this document is to update the TLS protocol with
extensions to support the certificates, public key algorithms,
symmetric ciphers, hash algorithms, and trust model used by OpenPGP
[OpenPGP].

   This document uses the same notation used in the TLS Protocol draft.

### TLS Extension for SEED and HAS-160  (draft-ietf-tls-seedhas)
This document proposes the addition of new cipher suites to the TLS
protocol 1.0 [TLS] to support SEED and HAS-160.
The SEED algorithm is 128-bit symmetric block cipher algorithm.
[SEED] The HAS-160 is 160-bit secure hash function, whose block size
is 512 bit. [HAS] Both algorithms are developed in Korea since 1997
for stronger communication security.  Currently, SEED is widely used
and is the mandatory cipher in banking and stock applications in
Korea.

### Addition of MISTY1 to TLS  (draft-ietf-tls-misty1)
This document proposes the addition of new cipher suites to the TLS
protocol version 1.0 to support the MISTY1 encryption algorithm as a
bulk cipher algorithm.  Major change from the previous version is the
addition of intellectual property section.

### Advanced Encryption Standard (AES) Ciphersuites for Transport Layer Security (TLS)  (draft-ietf-tls-ciphersuite)
This document proposes several new ciphersuites.  At present, the symmetric ciphers supported by Transport Layer Security (TLS) are RC2, RC4, International Data Encryption Algorithm (IDEA), Data Encryption Standard (DES), and triple DES.  The protocol would be enhanced by the addition of Advanced Encryption Standard (AES) ciphersuites. [STANDARDS-TRACK]

### Addition of Camellia Cipher Suites to Transport Layer Security (TLS)  (draft-ietf-tls-camellia)
This document proposes the addition of new cipher suites to the Transport Layer Security (TLS) protocol to support the Camellia encryption algorithm as a bulk cipher algorithm. [STANDARDS-TRACK]

### Kerberos Cipher Suites in Transport Layer Security (TLS)  (draft-ietf-tls-kerb)
RFC 2712 [KERBTLS] introduced mechanisms for supporting Kerberos 
[KERB] authentication within the TLS protocol [TLS].  This document 
extends RFC 2712 to support delegation of Kerberos credentials.  In 
this way, a TLS server may obtain a Kerberos service ticket on behalf 
of the TLS client.  Thus, a single client identity may be used for 
authentication within a multi-tier architecture.  This draft also 
proposes a mechanism for a TLS server to indicate Kerberos-specific 
information to the client within the certificate request message in 
the initial exchange.

### Wireless Extensions to TLS  (draft-ietf-tls-wireless)
This document suggests extensions to TLS designed to make TLS more 
amenable to use within wireless environments. The extensions may be
used by TLS clients and servers. The extensions are backwards
compatible - communication is possible between TLS 1.0 clients
that support the extensions and TLS 1.0 servers that do not
support the extensions, and vice versa.

### TLS Delegation Protocol  (draft-ietf-tls-delegation)
This document specifies a delegation protocol for use with the 
Transport Layer Security (TLS) protocol.  When the TLS session is 
using X.509 certificates for authentication, then the delegation is 
of an X.509 Proxy Certificate, as defined in draft-ggf-x509-proxy.  
When the TSL session is using Kerberos 5 for authentication, then 
the delegation is of a Kerberos 5 forwardable ticket, as defined in 
RFC 1510.

### Transport Layer Security (TLS) Extensions  (draft-ietf-tls-extensions)
This document describes extensions that may be used to add functionality to Transport Layer Security (TLS).  It provides both generic extension mechanisms for the TLS handshake client and server hellos, and specific extensions using these generic mechanisms.  The extensions may be used by TLS clients and servers.  The extensions are backwards compatible - communication is possible between TLS 1.0 clients that support the extensions and TLS 1.0 servers that do not support the extensions, and vice versa. [STANDARDS-TRACK]

### TLS Pathsec Protocol  (draft-ietf-tls-pathsec)
The TLS Pathsec Protocol (or Pathsec Protocol in short) extends the
TLS protocol into securing data in transit not only between two end
points, but also between the intermediaries en route, based on TLS
1.0 with appropriate extensions that include injecting source routing
policies above the Transport layer.

### Using OpenPGP Keys for Transport Layer Security (TLS) Authentication  (draft-ietf-tls-openpgp-keys)
This memo proposes extensions to the Transport Layer Security (TLS) protocol to support the OpenPGP key format.  The extensions discussed here include a certificate type negotiation mechanism, and the required modifications to the TLS Handshake Protocol.  This memo defines an Experimental Protocol for the Internet community.

### The Transport Layer Security (TLS) Protocol Version 1.1  (draft-ietf-tls-rfc2246-bis)
This document specifies Version 1.1 of the Transport Layer Security (TLS) protocol.  The TLS protocol provides communications security over the Internet.  The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery.

### Transport Layer Security Protocol Compression Methods  (draft-ietf-tls-compression)
The Transport Layer Security (TLS) protocol (RFC 2246) includes features to negotiate selection of a lossless data compression method as part of the TLS Handshake Protocol and to then apply the algorithm associated with the selected method as part of the TLS Record Protocol.  TLS defines one standard compression method which specifies that data exchanged via the record protocol will not be compressed.  This document describes an additional compression method associated with a lossless data compression algorithm for use with TLS, and it describes a method for the specification of additional TLS compression methods. [STANDARDS-TRACK]

### Use of Shared Keys in the TLS Protocol  (draft-ietf-tls-sharedkeys)
The TLS handshake requires the use of CPU-intensive public-key algorithms with a considerable overhead in resource-constrained environments or ones such as mainframes where users are charged for CPU time.  This document describes a means of employing TLS using symmetric keys or passwords shared in advance among communicating parties.  No modifications or alterations to the TLS protocol are required for this process.

### Update to Transport Layer Security (TLS) Extensions  (draft-ietf-tls-emailaddr)
This document is an update to the Transport Layer Security (TLS) 
Extensions.  This update provides an additional choice in the 
ServerName type of the Server_Name extension.  The Server Name 
extension allows the client to specify the name of the server to 
which it is attempting to connect.  The new choice specified in this 
document allows the client to specify an email name as the server name.

### Pre-Shared Key Ciphersuites for Transport Layer Security (TLS)  (draft-ietf-tls-psk)
This document specifies three sets of new ciphersuites for the Transport Layer Security (TLS) protocol to support authentication based on pre-shared keys (PSKs).  These pre-shared keys are symmetric keys, shared in advance among the communicating parties.  The first set of ciphersuites uses only symmetric key operations for authentication.  The second set uses a Diffie-Hellman exchange authenticated with a pre-shared key, and the third set combines public key authentication of the server with pre-shared key authentication of the client. [STANDARDS-TRACK]

### Transport Layer Security (TLS) Extensions  (draft-ietf-tls-rfc3546bis)
This document describes extensions that may be used to add functionality to Transport Layer Security (TLS). It provides both generic extension mechanisms for the TLS handshake client and server hellos, and specific extensions using these generic mechanisms.

 The extensions may be used by TLS clients and servers. The extensions are backwards compatible: communication is possible between TLS clients that support the extensions and TLS servers that do not support the extensions, and vice versa. [STANDARDS-TRACK]

### AES Counter Mode Cipher Suites for TLS and DTLS  (draft-ietf-tls-ctr)
This document describes the use of the Advanced Encryption Standard
   (AES) Counter Mode for use as a Transport Layer Security (TLS) and
   Datagram Transport Layer Security (DTLS) confidentiality mechanism.

### The Transport Layer Security (TLS) Protocol Version 1.2  (draft-ietf-tls-rfc4346-bis)
This document specifies Version 1.2 of the Transport Layer Security (TLS) protocol.  The TLS protocol provides communications security over the Internet.  The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery. [STANDARDS-TRACK]

### Pre-Shared Key (PSK) Ciphersuites with NULL Encryption for Transport Layer Security (TLS)  (draft-ietf-tls-psk-null)
This document specifies authentication-only ciphersuites (with no encryption) for the Pre-Shared Key (PSK) based Transport Layer Security (TLS) protocol.  These ciphersuites are useful when authentication and integrity protection is desired, but confidentiality is not needed or not permitted. [STANDARDS-TRACK]

### Clientside interoperability experiences for the SSL and TLS protocols  (draft-ietf-tls-interoperability)
This document presents a number of problems encountered when
   implementing TLS 1.0, TLS 1.1 and TLS Extensions for clients, and
   their consequences.  The problems include servers that refuse to
   connect with clients supporting newer versions of the protocol, or
   that do not handle such negotiation properly.  Another problem
   encountered is the incorrect use of values in the protocol messages.

### Keying Material Exporters for Transport Layer Security (TLS)  (draft-ietf-tls-extractor)
A number of protocols wish to leverage Transport Layer Security (TLS) to perform key establishment but then use some of the keying material for their own purposes.  This document describes a general mechanism for allowing that. [STANDARDS-TRACK]

### AES Galois Counter Mode (GCM) Cipher Suites for TLS  (draft-ietf-tls-rsa-aes-gcm)
This memo describes the use of the Advanced Encryption Standard (AES) in Galois/Counter Mode (GCM) as a Transport Layer Security (TLS) authenticated encryption operation.  GCM provides both confidentiality and data origin authentication, can be efficiently implemented in hardware for speeds of 10 gigabits per second and above, and is also well-suited to software implementations.  This memo defines TLS cipher suites that use AES-GCM with RSA, DSA, and Diffie-Hellman-based key exchange mechanisms. [STANDARDS-TRACK]

### Suite B Cipher Suites for TLS  (draft-ietf-tls-suiteb)
The United States Government has published guidelines for "NSA Suite
   B Cryptography" dated July, 2005, which defines cryptographic
   algorithm polcy for national security applications.  This document
   defines a profile of TLS which is conformant with Suite B.

### TLS Elliptic Curve Cipher Suites with SHA-256/384 and AES Galois Counter Mode (GCM)  (draft-ietf-tls-ecc-new-mac)
RFC 4492 describes elliptic curve cipher suites for Transport Layer Security (TLS).  However, all those cipher suites use HMAC-SHA-1 as their Message Authentication Code (MAC) algorithm.  This document describes sixteen new cipher suites for TLS that specify stronger MAC algorithms.  Eight use Hashed Message Authentication Code (HMAC) with SHA-256 or SHA-384, and eight use AES in Galois Counter Mode (GCM).  This memo provides information for the Internet community.

### ECDHE_PSK Cipher Suites for Transport Layer Security (TLS)  (draft-ietf-tls-ecdhe-psk)
This document extends RFC 4279, RFC 4492, and RFC 4785 and specifies a set of cipher suites that use a pre-shared key (PSK) to authenticate an Elliptic Curve Diffie-Hellman exchange with Ephemeral keys (ECDHE).  These cipher suites provide Perfect Forward Secrecy (PFS).  This memo provides information for the Internet community.

### Transport Layer Security (TLS) Extensions: Extension Definitions  (draft-ietf-tls-rfc4366-bis)
This document provides specifications for existing TLS extensions.  It is a companion document for RFC 5246, "The Transport Layer Security (TLS) Protocol Version 1.2".  The extensions specified are server_name, max_fragment_length, client_certificate_url, trusted_ca_keys, truncated_hmac, and status_request. [STANDARDS-TRACK]

### DES and IDEA Cipher Suites for Transport Layer Security (TLS)  (draft-ietf-tls-des-idea)
Transport Layer Security (TLS) versions 1.0 (RFC 2246) and 1.1 (RFC 4346) include cipher suites based on DES (Data Encryption Standard) and IDEA (International Data Encryption Algorithm) algorithms.  DES (when used in single-DES mode) and IDEA are no longer recommended for general use in TLS, and have been removed from TLS version 1.2 (RFC 5246).  This document specifies these cipher suites for completeness and discusses reasons why their use is no longer recommended.  This memo provides information for the Internet community.

### Pre-Shared Key Cipher Suites for TLS with SHA-256/384 and AES Galois Counter Mode  (draft-ietf-tls-psk-new-mac-aes-gcm)
RFC 4279 and RFC 4785 describe pre-shared key cipher suites for Transport Layer Security (TLS).  However, all those cipher suites use SHA-1 in their Message Authentication Code (MAC) algorithm.  This document describes a set of pre-shared key cipher suites for TLS that uses stronger digest algorithms (i.e., SHA-256 or SHA-384) and another set that uses the Advanced Encryption Standard (AES) in Galois Counter Mode (GCM). [STANDARDS-TRACK]

### Datagram Transport Layer Security Version 1.2  (draft-ietf-tls-rfc4347-bis)
This document specifies version 1.2 of the Datagram Transport Layer Security (DTLS) protocol.  The DTLS protocol provides communications privacy for datagram protocols.  The protocol allows client/server applications to communicate in a way that is designed to prevent eavesdropping, tampering, or message forgery.  The DTLS protocol is based on the Transport Layer Security (TLS) protocol and provides equivalent security guarantees.  Datagram semantics of the underlying transport are preserved by the DTLS protocol.  This document updates DTLS 1.0 to work with TLS version 1.2. [STANDARDS-TRACK]

## Working Group: tsvwg
### Considerations for Assigning a New Recommended Differentiated Services Code Point (DSCP)  (draft-ietf-tsvwg-dscp-considerations)
This document discusses considerations for assigning a new recommended Differentiated Services Code Point (DSCP) for a standard Per-Hop Behavior (PHB).  It considers the common observed re-marking behaviors that the Diffserv field might be subjected to along an Internet path.  It also notes some implications of using a specific DSCP.

### Careful convergence of congestion control from retained state  (draft-kuhn-tsvwg-careful-resume)
This document specifies careful convergence of Congestion Control
   (CC), providing a cautious method that enables fast startup for a
   wide range of connections or reconnections.

   The method reuses a set of computed CC parameters that are based on
   the previously observed path characteristics between the same pair of
   transport endpoints, such as the bottleneck bandwidth, available
   capacity, or the RTT.  These parameters are stored, allowing them to
   be later used to modify the CC behavior of a subsequent connection.
   The document also discusses assumptions and defines requirements
   around how a sender utilizes these parameters to provide
   opportunities for a connection to more quickly get up to speed (i.e.
   utilize the available capacity).  It discusses how these changes
   impact the capacity at a shared network bottleneck and the safe
   response that is needed after any indication that the new rate is
   inappropriate.  The method is expected to be appropriate to IETF
   transports.

### Mapping Diffserv to IEEE 802.11  (draft-ietf-tsvwg-ieee-802-11)
As Internet traffic is increasingly sourced from and destined to wireless endpoints, it is crucial that Quality of Service (QoS) be aligned between wired and wireless networks; however, this is not always the case by default.  This document specifies a set of mappings from Differentiated Services Code Point (DSCP) to IEEE 802.11 User Priority (UP) to reconcile the marking recommendations offered by the IETF and the IEEE so as to maintain consistent QoS treatment between wired and IEEE 802.11 wireless networks.

### An Extension to the Selective Acknowledgement (SACK) Option for TCP  (draft-floyd-sack)
This note defines an extension of the Selective Acknowledgement (SACK) Option for TCP. [STANDARDS-TRACK]

### TCP Processing of the IPv4 Precedence Field  (draft-xiao-tcp-prec)
This memo describes a conflict between TCP and DiffServ on the use of the three leftmost bits in the TOS octet of an IPv4 header. [STANDARDS-TRACK]

### Computing TCP's Retransmission Timer  (draft-paxson-tcp-rto)
This document defines the standard algorithm that Transmission Control Protocol (TCP) senders are required to use to compute and manage their retransmission timer. [STANDARDS-TRACK]

### TCP Congestion Window Validation  (draft-handley-tcp-cwv)
This document describes a simple modification to TCP's congestion control algorithms to decay the congestion window cwnd after the transition from a sufficiently-long application-limited period, while using the slow-start threshold ssthresh to save information about the previous value of the congestion window.  This memo defines an Experimental Protocol for the Internet community.

### Enhancing TCP's Loss Recovery Using Limited Transmit  (draft-ietf-tsvwg-limited-xmit)
This document proposes a new Transmission Control Protocol (TCP) mechanism that can be used to more effectively recover lost segments when a connection's congestion window is small, or when a large number of segments are lost in a single transmission window. [STANDARDS-TRACK]

### A Conservative Selective Acknowledgment (SACK)-based Loss Recovery Algorithm for TCP  (draft-allman-tcp-sack)
This document presents a conservative loss recovery algorithm for TCP that is based on the use of the selective acknowledgment (SACK) TCP option.  The algorithm presented in this document conforms to the spirit of the current congestion control specification (RFC 2581), but allows TCP senders to recover more effectively when multiple segments are lost from a single flight of data. [STANDARDS-TRACK]

### TCP with ECN: The Treatment of Retransmitted Data Packets  (draft-ietf-tsvwg-tcp-ecn)
This document makes recommendations for the use of ECN with
retransmitted data packets, for an ECN-capable TCP connection.  This
document supplements RFC 2481 [RFC2481], which did not address the
issue of retransmitted data packets.  This document recommends that
for ECN-capable TCP implementations, the ECT bit (ECN-Capable
Transport) in the IP header SHOULD NOT be set on retransmitted data
packets, and that the TCP data receiver SHOULD ignore the ECN field
on arriving data packets that are outside of the receiver's current
window.  This is for greater security against denial-of-service
attacks.

### ECN Interactions with IP Tunnels  (draft-ietf-tsvwg-ecn-tunnels)
The encapsulation of IP packet headers in tunnels is used in many
places, including IPsec and IP in IP [RFC2003].  Explicit Congestion
Notification (ECN) is an experimental addition to the IP architecture
that uses the ECN field in the IP header to provide an indication of
the onset of congestion to applications.  ECN provides this
congestion indication to enable end-node adaptation to network
conditions without the use of dropped packets [RFC 2481].  Currently,
the ECN specification does not accommodate the constraints imposed by
some of these pre-existing specifications for tunnels.  This document
considers issues related to interactions between ECN and IP tunnels,
and proposes two alternative solutions

### The Addition of Explicit Congestion Notification (ECN) to IP  (draft-ietf-tsvwg-ecn)
This memo specifies the incorporation of ECN (Explicit Congestion Notification) to TCP and IP, including ECN's use of two bits in the IP header. [STANDARDS-TRACK]

### The Eifel Detection Algorithm for TCP  (draft-ietf-tsvwg-tcp-eifel-alg)
The Eifel detection algorithm allows a TCP sender to detect a posteriori whether it has entered loss recovery unnecessarily.  It requires that the TCP Timestamps option defined in RFC 1323 be enabled for a connection.  The Eifel detection algorithm makes use of the fact that the TCP Timestamps option eliminates the retransmission ambiguity in TCP.  Based on the timestamp of the first acceptable ACK that arrives during loss recovery, it decides whether loss recovery was entered unnecessarily.  The Eifel detection algorithm provides a basis for future TCP enhancements.  This includes response algorithms to back out of loss recovery by restoring a TCP sender's congestion control state.  This memo defines an Experimental Protocol for the Internet community.

### TCP Friendly Rate Control (TFRC): Protocol Specification  (draft-ietf-tsvwg-tfrc)
This document specifies TCP-Friendly Rate Control (TFRC).  TFRC is a congestion control mechanism for unicast flows operating in a best- effort Internet environment.  It is reasonably fair when competing for bandwidth with TCP flows, but has a much lower variation of throughput over time compared with TCP, making it more suitable for applications such as telephony or streaming media where a relatively smooth sending rate is of importance. [STANDARDS-TRACK]

### Robust Explicit Congestion Notification (ECN) Signaling with Nonces  (draft-ietf-tsvwg-tcp-nonce)
This note describes the Explicit Congestion Notification (ECN)-nonce, an optional addition to ECN that protects against accidental or malicious concealment of marked packets from the TCP sender.  It improves the robustness of congestion control by preventing receivers from exploiting ECN to gain an unfair share of network bandwidth.  The ECN-nonce uses the two ECN-Capable Transport (ECT)codepoints in the ECN field of the IP header, and requires a flag in the TCP header.  It is computationally efficient for both routers and hosts.  This memo defines an Experimental Protocol for the Internet community.

### An Open ECN Service in the IP layer  (draft-ietf-tsvwg-ecn-ip)
This document contributes to the effort to add explicit congestion
notification (ECN) to IP. In the current effort to standardise ECN for TCP it is unavoidably necessary to standardise certain new aspects of IP.However, the IP aspects will not and cannot only be specific to TCP. We specify interaction with features of IP such as fragmentation,
differentiated services, multicast forwarding, and a definition of the
service offered to higher layer congestion control protocols. This document
only concerns aspects related to the IP layer, but includes any aspects
likely to be common to all higher layer protocols. Any specification of ECN
support in higher layer protocols is expected to appear in a separate
specification for each such protocol.

### Stream Control Transmission Protocol (SCTP) Dynamic Address Reconfiguration  (draft-ietf-tsvwg-addip-sctp)
A local host may have multiple points of attachment to the Internet, giving it a degree of fault tolerance from hardware failures.  Stream Control Transmission Protocol (SCTP) (RFC 4960) was developed to take full advantage of such a multi-homed host to provide a fast failover and association survivability in the face of such hardware failures.  This document describes an extension to SCTP that will allow an SCTP stack to dynamically add an IP address to an SCTP association, dynamically delete an IP address from an SCTP association, and to request to set the primary address the peer will use when sending to an endpoint. [STANDARDS-TRACK]

### Stream Control Transmission Protocol  (draft-ietf-tsvwg-rfc2960-bis)
This document describes the Stream Control Transmission Protocol
(SCTP).  SCTP is designed to transport PSTN signaling messages over
IP networks, but is capable of broader applications.

### Stream Control Transmission Protocol  (draft-ietf-tsvwg-2960bis)
This document obsoletes RFC 2960 and RFC 3309. It describes the Stream Control Transmission Protocol (SCTP). SCTP is designed to transport Public Switched Telephone Network (PSTN) signaling messages over IP networks, but is capable of broader applications.

 SCTP is a reliable transport protocol operating on top of a connectionless packet network such as IP. It offers the following services to its users:

 -- acknowledged error-free non-duplicated transfer of user data,

 -- data fragmentation to conform to discovered path MTU size,

 -- sequenced delivery of user messages within multiple streams, with an option for order-of-arrival delivery of individual user messages,

 -- optional bundling of multiple user messages into a single SCTP packet, and

 -- network-level fault tolerance through supporting of multi-homing at either or both ends of an association.

 The design of SCTP includes appropriate congestion avoidance behavior and resistance to flooding and masquerade attacks. [STANDARDS-TRACK]

### Increasing TCP's Initial Window  (draft-ietf-tsvwg-initwin)
This document specifies an optional standard for TCP to increase the
permitted initial window from one segment to roughly 4K bytes,
replacing RFC 2414.  This document discusses the advantages and
disadvantages of the higher initial window.  The document includes
discussion of experiments and simulations showing that the higher
initial window does not lead to congestion collapse. Finally, the
document provides guidance on implementation issues.

### Sockets API Extensions for the Stream Control Transmission Protocol (SCTP)  (draft-ietf-tsvwg-sctpsocket)
This document describes a mapping of the Stream Control Transmission Protocol (SCTP) into a sockets API.  The benefits of this mapping include compatibility for TCP applications, access to new SCTP features, and a consolidated error and event notification scheme.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Stream Control Transmission Protocol (SCTP) Specification Errata and Issues  (draft-ietf-tsvwg-sctpimpguide)
This document is a compilation of issues found during six interoperability events and 5 years of experience with implementing, testing, and using SCTP along with the suggested fixes.  This document provides deltas to RFC 2960 and is organized in a time-based way.  The issues are listed in the order they were brought up.  Because some text is changed several times, the last delta in the text is the one that should be applied.  In addition to the delta, a description of the problem and the details of the solution are also provided.  This memo provides information for the Internet community.

### Stream Control Transmission Protocol (SCTP) Checksum Change  (draft-ietf-tsvwg-sctpcsum)
Stream Control Transmission Protocol [RFC2960] (SCTP) currently uses an 
Adler-32 checksum.  For small packets Adler-32 provides weak detection 
of errors.  This document changes that checksum and updates SCTP to 
use a 32 bit CRC checksum.

### ULP Framing for TCP  (draft-ietf-tsvwg-tcp-ulp-frame)
The TCP ULP Framing (TUF) protocol defines a shim layer protocol
between an Upper Layer Protocol (ULP) and TCP.  TUF also depends on
a specified TCP segmentation convention between TUF endpoints.
Together, the shim and segmentation conventions enable a TUF/TCP
receiver to recognize ULP data units within a TCP segment
independently of other TCP segments.

### Transport Layer Security over Stream Control Transmission Protocol  (draft-ietf-tsvwg-tls-over-sctp)
This document describes the usage of the Transport Layer Security (TLS) protocol, as defined in RFC 2246, over the Stream Control Transmission Protocol (SCTP), as defined in RFC 2960 and RFC 3309.  The user of TLS can take advantage of the features provided by SCTP, namely the support of multiple streams to avoid head of line blocking and the support of multi-homing to provide network level fault tolerance.  Additionally, discussions of extensions of SCTP are also supported, meaning especially the support of dynamic reconfiguration of IP- addresses. [STANDARDS-TRACK]

### The Lightweight User Datagram Protocol (UDP-Lite)  (draft-ietf-tsvwg-udp-lite)
This document describes the Lightweight User Datagram Protocol (UDP-Lite), which is similar to the User Datagram Protocol (UDP) (RFC 768), but can also serve applications in error-prone network environments that prefer to have partially damaged payloads delivered rather than discarded.  If this feature is not used, UDP-Lite is semantically identical to UDP. [STANDARDS-TRACK]

### TCP Extended Statistics MIB  (draft-ietf-tsvwg-tcp-mib-extension)
This document describes extended performance statistics for TCP.  They are designed to use TCP's ideal vantage point to diagnose performance problems in both the network and the application.  If a network-based application is performing poorly, TCP can determine if the bottleneck is in the sender, the receiver, or the network itself.  If the bottleneck is in the network, TCP can provide specific information about its nature. [STANDARDS-TRACK]

### Stream Control Transmission Protocol (SCTP) Partial Reliability Extension  (draft-ietf-tsvwg-prsctp)
This memo describes an extension to the Stream Control Transmission Protocol (SCTP) that allows an SCTP endpoint to signal to its peer that it should move the cumulative ack point forward.  When both sides of an SCTP association support this extension, it can be used by an SCTP implementation to provide partially reliable data transmission service to an upper layer protocol.  This memo describes the protocol extensions, which consist of a new parameter for INIT and INIT ACK, and a new FORWARD TSN chunk type, and provides one example of a partially reliable service that can be provided to the upper layer via this mechanism. [STANDARDS-TRACK]

### The Eifel Response Algorithm for TCP  (draft-ietf-tsvwg-tcp-eifel-response)
Based on an appropriate detection algorithm, the Eifel response algorithm provides a way for a TCP sender to respond to a detected spurious timeout.  It adapts the retransmission timer to avoid further spurious timeouts and (depending on the detection algorithm) can avoid the often unnecessary go-back-N retransmits that would otherwise be sent.  In addition, the Eifel response algorithm restores the congestion control state in such a way that packet bursts are avoided. [STANDARDS-TRACK]

### The NewReno Modification to TCP's Fast Recovery Algorithm  (draft-ietf-tsvwg-newreno)
The purpose of this document is to advance NewReno TCP's Fast Retransmit and Fast Recovery algorithms in RFC 2582 from Experimental to Standards Track status.  The main change in this document relative to RFC 2582 is to specify the Careful variant of NewReno's Fast Retransmit and Fast Recovery algorithms.  The base algorithm described in RFC 2582 did not attempt to avoid unnecessary multiple Fast Retransmits that can occur after a timeout.  However, RFC 2582 also defined "Careful" and "Less Careful" variants that avoid these unnecessary Fast Retransmits, and recommended the Careful variant.  This document specifies the previously-named "Careful" variant as the basic version of NewReno TCP. [STANDARDS-TRACK]

### Using TCP Duplicate Selective Acknowledgement (DSACKs) and Stream Control Transmission Protocol (SCTP) Duplicate Transmission Sequence Numbers (TSNs) to Detect Spurious Retransmissions  (draft-ietf-tsvwg-dsack-use)
TCP and Stream Control Transmission Protocol (SCTP) provide notification of duplicate segment receipt through Duplicate Selective Acknowledgement (DSACKs) and Duplicate Transmission Sequence Number (TSN) notification, respectively.  This document presents conservative methods of using this information to identify unnecessary retransmissions for various applications.  This memo defines an Experimental Protocol for the Internet community.

### HighSpeed TCP for Large Congestion Windows  (draft-ietf-tsvwg-highspeed)
The proposals in this document are experimental.  While they may be deployed in the current Internet, they do not represent a consensus that this is the best method for high-speed congestion control.  In particular, we note that alternative experimental proposals are likely to be forthcoming, and it is not well understood how the proposals in this document will interact with such alternative proposals.  This document proposes HighSpeed TCP, a modification to TCP's congestion control mechanism for use with TCP connections with large congestion windows.  The congestion control mechanisms of the current Standard TCP constrains the congestion windows that can be achieved by TCP in realistic environments.  For example, for a Standard TCP connection with 1500-byte packets and a 100 ms round-trip time, achieving a steady-state throughput of 10 Gbps would require an average congestion window of 83,333 segments, and a packet drop rate of at most one congestion event every 5,000,000,000 packets (or equivalently, at most one congestion event every 1 2/3 hours).  This is widely acknowledged as an unrealistic constraint.  To address his limitation of TCP, this document proposes HighSpeed TCP, and solicits experimentation and feedback from the wider community.

### Limited Slow-Start for TCP with Large Congestion Windows  (draft-ietf-tsvwg-slowstart)
This document describes an optional modification for TCP's slow-start for use with TCP connections with large congestion windows.  For TCP connections that are able to use congestion windows of thousands (or tens of thousands) of MSS-sized segments (for MSS the sender's MAXIMUM SEGMENT SIZE), the current slow-start procedure can result in increasing the congestion window by thousands of segments in a single round-trip time.  Such an increase can easily result in thousands of packets being dropped in one round-trip time.  This is often counter-productive for the TCP flow itself, and is also hard on the rest of the traffic sharing the congested link.  This note describes Limited Slow-Start as an optional mechanism for limiting the number of segments by which the congestion window is increased for one window of data during slow-start, in order to improve performance for TCP connections with large congestion windows.  This memo defines an Experimental Protocol for the Internet community.

### F-RTO: An Algorithm for Detecting Spurious Retransmission Timeouts with TCP and SCTP  (draft-ietf-tsvwg-tcp-frto)
Spurious retransmission timeouts (RTOs) cause suboptimal TCP
   performance, because they often result in unnecessary retransmission
   of the last window of data. This document describes the 'Forward RTO
   Recovery' (F-RTO) algorithm for detecting spurious TCP RTOs. F-RTO is
   a TCP sender only algorithm that does not require any TCP options to
   operate. After retransmitting the first unacknowledged segment
   triggered by an RTO, the F-RTO algorithm at a TCP sender monitors the
   incoming acknowledgements to determine whether the timeout was
   spurious and to decide whether to send new segments or retransmit
   unacknowledged segments. The algorithm effectively helps to avoid
   additional unnecessary retransmissions and thereby improves TCP
   performance in case of a spurious timeout. The F-RTO algorithm can
also be applied with the SCTP protocol.

### Implementing an Emergency Telecommunications Service (ETS) for Real-Time Services in the Internet Protocol Suite  (draft-ietf-tsvwg-mlpp-that-works)
RFCs 3689 and 3690 detail requirements for an Emergency Telecommunications Service (ETS), of which an Internet Emergency Preparedness Service (IEPS) would be a part. Some of these types of services require call preemption; others require call queuing or other mechanisms. IEPS requires a Call Admission Control (CAC) procedure and a Per Hop Behavior (PHB) for the data that meet the needs of this architecture. Such a CAC procedure and PHB is appropriate to any service that might use H.323 or SIP to set up real-time sessions. The key requirement is to guarantee an elevated probability of call completion to an authorized user in time of crisis.

 This document primarily discusses supporting ETS in the context of the US Government and NATO, because it focuses on the Multi-Level Precedence and Preemption (MLPP) and Government Emergency Telecommunication Service (GETS) standards. The architectures described here are applicable beyond these organizations. This memo provides information for the Internet community.

### Security Attacks Found Against the Stream Control Transmission Protocol (SCTP) and Current Countermeasures  (draft-ietf-tsvwg-sctpthreat)
This document describes certain security threats to SCTP.  It also describes ways to mitigate these threats, in particular by using techniques from the SCTP Specification Errata and Issues memo (RFC 4460).  These techniques are included in RFC 4960, which obsoletes RFC 2960.  It is hoped that this information will provide some useful background information for many of the newest requirements spelled out in the SCTP Specification Errata and Issues and included in RFC 4960.  This memo provides information for the Internet community.

### Quality of Service (QoS) Signaling in a Nested Virtual Private Network  (draft-ietf-tsvwg-vpn-signaled-preemption)
Some networks require communication between an interior and exterior portion of a Virtual Private Network (VPN) or through a concatenation of such networks resulting in a nested VPN, but have sensitivities about what information is communicated across the boundary, especially while providing quality of service to communications with different precedence.  This note seeks to outline the issues and the nature of the proposed solutions based on the framework for Integrated Services operation over Diffserv networks as described in RFC 2998.  This memo provides information for the Internet community.

### Aggregation of Diffserv Service Classes  (draft-ietf-tsvwg-diffserv-class-aggr)
In the core of a high-capacity network, service differentiation may still be needed to support applications' utilization of the network.  Applications with similar traffic characteristics and performance requirements are mapped into Diffserv service classes based on end- to-end behavior requirements of the applications.  However, some network segments may be configured in such a way that a single forwarding treatment may satisfy the traffic characteristics and performance requirements of two or more service classes.  In these cases, it may be desirable to aggregate two or more Diffserv service classes into a single forwarding treatment.  This document provides guidelines for the aggregation of Diffserv service classes into forwarding treatments.  This memo provides information for the Internet community.

### MLEF Without Capacity Admission Does Not Satisfy MLPP Requirements  (draft-ietf-tsvwg-mlef-concerns)
The Defense Information Systems Agency of the United States
   Department of Defense, with its contractors, has proposed a service
   architecture for military (NATO and related agencies) telephone
   systems.  This is called the Assured Service, and is defined in two
   documents: "Architecture for Assured Service Capabilities in Voice
   over IP" and "Requirements for Assured Service Capabilities in Voice
   over IP".  Responding to these are three documents: "Extending the
   Session Initiation Protocol Reason Header to account for Preemption
   Events", "Communications Resource Priority for the Session Initiation
   Protocol", and the "Multi-Level Expedited Forwarding Per Hop
   Behavior" (MLEF PHB).  MLEF, as currently defined, has serious
   problems, which this draft seeks to discuss.

### A Resource Reservation Protocol (RSVP) Extension for the Reduction of Bandwidth of a Reservation Flow  (draft-ietf-tsvwg-rsvp-bw-reduction)
This document proposes an extension to the Resource Reservation Protocol (RSVPv1) to reduce the guaranteed bandwidth allocated to an existing reservation.  This mechanism can be used to affect individual reservations, aggregate reservations, or other forms of RSVP tunnels.  This specification is an extension of RFC 2205. [STANDARDS-TRACK]

### Configuration Guidelines for DiffServ Service Classes  (draft-ietf-tsvwg-diffserv-service-classes)
This document describes service classes configured with Diffserv and recommends how they can be used and how to construct them using Differentiated Services Code Points (DSCPs), traffic conditioners, Per-Hop Behaviors (PHBs), and Active Queue Management (AQM) mechanisms.  There is no intrinsic requirement that particular DSCPs, traffic conditioners, PHBs, and AQM be used for a certain service class, but as a policy and for interoperability it is useful to apply them consistently.  This memo provides information for the Internet community.

### Quick-Start for TCP and IP  (draft-ietf-tsvwg-quickstart)
This document specifies an optional Quick-Start mechanism for transport protocols, in cooperation with routers, to determine an allowed sending rate at the start and, at times, in the middle of a data transfer (e.g., after an idle period). While Quick-Start is designed to be used by a range of transport protocols, in this document we only specify its use with TCP. Quick-Start is designed to allow connections to use higher sending rates when there is significant unused bandwidth along the path, and the sender and all of the routers along the path approve the Quick-Start Request.

 This document describes many paths where Quick-Start Requests would not be approved. These paths include all paths containing routers, IP tunnels, MPLS paths, and the like that do not support Quick- Start. These paths also include paths with routers or middleboxes that drop packets containing IP options. Quick-Start Requests could be difficult to approve over paths that include multi-access layer- two networks. This document also describes environments where the Quick-Start process could fail with false positives, with the sender incorrectly assuming that the Quick-Start Request had been approved by all of the routers along the path. As a result of these concerns, and as a result of the difficulties and seeming absence of motivation for routers, such as core routers to deploy Quick-Start, Quick-Start is being proposed as a mechanism that could be of use in controlled environments, and not as a mechanism that would be intended or appropriate for ubiquitous deployment in the global Internet. This memo defines an Experimental Protocol for the Internet community.

### Authenticated Chunks for the Stream Control Transmission Protocol (SCTP)  (draft-ietf-tsvwg-sctp-auth)
This document describes a new chunk type, several parameters, and procedures for the Stream Control Transmission Protocol (SCTP).  This new chunk type can be used to authenticate SCTP chunks by using shared keys between the sender and receiver.  The new parameters are used to establish the shared keys. [STANDARDS-TRACK]

### Aggregation of Resource ReSerVation Protocol (RSVP) Reservations over MPLS TE/DS-TE Tunnels  (draft-ietf-tsvwg-rsvp-dste)
RFC 3175 specifies aggregation of Resource ReSerVation Protocol (RSVP) end-to-end reservations over aggregate RSVP reservations.  This document specifies aggregation of RSVP end-to-end reservations over MPLS Traffic Engineering (TE) tunnels or MPLS Diffserv-aware MPLS Traffic Engineering (DS-TE) tunnels.  This approach is based on RFC 3175 and simply modifies the corresponding procedures for operations over MPLS TE tunnels instead of aggregate RSVP reservations.  This approach can be used to achieve admission control of a very large number of flows in a scalable manner since the devices in the core of the network are unaware of the end-to-end RSVP reservations and are only aware of the MPLS TE tunnels. [STANDARDS-TRACK]

### Adding Explicit Congestion Notification (ECN) Capability to TCP's SYN/ACK Packets  (draft-ietf-tsvwg-ecnsyn)
This draft specifies a modification to RFC 3168 to allow TCP SYN/ACK
   packets to be ECN-Capable.  For TCP, RFC 3168 only specified setting
   an ECN-Capable codepoint on data packets, and not on SYN and SYN/ACK
   packets.  However, because of the high cost to the TCP transfer of
   having a SYN/ACK packet dropped, with the resulting retransmit
   timeout, this document is specifying the use of ECN for the SYN/ACK
   packet itself, when sent in response to a SYN packet with the two ECN
   flags set in the TCP header, indicating a willingness to use ECN.
   Setting TCP SYN/ACK packets as ECN-Capable can be of great benefit to
   the TCP connection, avoiding the severe penalty of a retransmit
   timeout for a connection that has not yet started placing a load on
   the network.  The sender of the SYN/ACK packet must respond to an ECN
   mark by reducing its initial congestion window from two, three, or
   four segments to one segment, reducing the subsequent load from that
   connection on the network.

### Specifying Alternate Semantics for the Explicit Congestion Notification (ECN) Field  (draft-ietf-tsvwg-ecn-alternates)
There have been a number of proposals for alternate semantics for the Explicit Congestion Notification (ECN) field in the IP header RFC 3168.  This document discusses some of the issues in defining alternate semantics for the ECN field, and specifies requirements for a safe coexistence in an Internet that could include routers that do not understand the defined alternate semantics.  This document evolved as a result of discussions with the authors of one recent proposal for such alternate semantics.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Padding Chunk and Parameter for the Stream Control Transmission Protocol (SCTP)  (draft-ietf-tsvwg-sctp-padding)
This document defines a padding chunk and a padding parameter and describes the required receiver side procedures.  The padding chunk is used to pad a Stream Control Transmission Protocol (SCTP) packet to an arbitrary size.  The padding parameter is used to pad an SCTP INIT chunk to an arbitrary size. [STANDARDS-TRACK]

### Generic Aggregate Resource ReSerVation Protocol (RSVP) Reservations  (draft-ietf-tsvwg-rsvp-ipsec)
RFC 3175 defines aggregate Resource ReSerVation Protocol (RSVP) reservations allowing resources to be reserved in a Diffserv network for a given Per Hop Behavior (PHB), or given set of PHBs, from a given source to a given destination.  RFC 3175 also defines how end-to-end RSVP reservations can be aggregated onto such aggregate reservations when transiting through a Diffserv cloud.  There are situations where multiple such aggregate reservations are needed for the same source IP address, destination IP address, and PHB (or set of PHBs).  However, this is not supported by the aggregate reservations defined in RFC 3175.  In order to support this, the present document defines a more flexible type of aggregate RSVP reservations, referred to as generic aggregate reservation.  Multiple such generic aggregate reservations can be established for a given PHB (or set of PHBs) from a given source IP address to a given destination IP address.  The generic aggregate reservations may be used to aggregate end-to-end RSVP reservations.  This document also defines the procedures for such aggregation.  The generic aggregate reservations may also be used end-to-end directly by end-systems attached to a Diffserv network. [STANDARDS-TRACK]

### MIB for the UDP-Lite protocol  (draft-ietf-tsvwg-udplite-mib)
This document specifies a Management Information Base (MIB) module for the Lightweight User Datagram Protocol (UDP-Lite).  It defines a set of new MIB objects to characterise the behaviour and performance of transport layer endpoints deploying UDP-Lite.  UDP-Lite resembles UDP, but differs from the semantics of UDP by the addition of a single option.  This adds the capability for variable-length data checksum coverage, which can benefit a class of applications that prefer delivery of (partially) corrupted datagram payload data in preference to discarding the datagram. [STANDARDS-TRACK]

### A Differentiated Services Code Point (DSCP) for Capacity-Admitted Traffic  (draft-ietf-tsvwg-admitted-realtime-dscp)
This document requests one Differentiated Services Code Point (DSCP) from the Internet Assigned Numbers Authority (IANA) for a class of real-time traffic.  This traffic class conforms to the Expedited Forwarding Per-Hop Behavior.  This traffic is also admitted by the network using a Call Admission Control (CAC) procedure involving authentication, authorization, and capacity admission.  This differs from a real-time traffic class that conforms to the Expedited Forwarding Per-Hop Behavior but is not subject to capacity admission or subject to very coarse capacity admission. [STANDARDS-TRACK]

### User-Defined Errors for RSVP  (draft-ietf-tsvwg-rsvp-user-error-spec)
The Resource ReserVation Protocol (RSVP) defines an ERROR_SPEC object for communicating errors. That object has a defined format that permits the definition of 256 error codes. As RSVP has been developed and extended, the convention has been to be conservative in defining new error codes. Further, no provision for user-defined errors exists in RSVP.

 This document defines a USER_ERROR_SPEC to be used in addition to the ERROR_SPEC to carry additional user information related to errors. [STANDARDS-TRACK]

### Resource Reservation Protocol (RSVP) Extensions for Path-Triggered RSVP Receiver Proxy  (draft-ietf-tsvwg-rsvp-proxy-proto)
Resource Reservation Protocol (RSVP) signaling can be used to make end-to-end resource reservations in an IP network in order to guarantee the Quality of Service (QoS) required by certain flows.  With conventional RSVP, both the data sender and receiver of a given flow take part in RSVP signaling.  Yet, there are many use cases where resource reservation is required, but the receiver, the sender, or both, is not RSVP-capable.  Where the receiver is not RSVP- capable, an RSVP router may behave as an RSVP Receiver Proxy, thereby performing RSVP signaling on behalf of the receiver.  This allows resource reservations to be established on the segment of the end-to- end path from the sender to the RSVP Receiver Proxy.  However, as discussed in the companion document "RSVP Proxy Approaches", RSVP extensions are needed to facilitate operations with an RSVP Receiver Proxy whose signaling is triggered by receipt of RSVP Path messages from the sender.  This document specifies these extensions. [STANDARDS-TRACK]

### RSVP Extensions for Admission Priority  (draft-ietf-tsvwg-emergency-rsvp)
Some applications require the ability to provide an elevated probability of session establishment to specific sessions in times of network congestion. When supported over the Internet Protocol suite, this may be facilitated through a network-layer admission control solution that supports prioritized access to resources (e.g., bandwidth). These resources may be explicitly set aside for prioritized sessions, or may be shared with other sessions. This document specifies extensions to the Resource reSerVation Protocol (RSVP) that can be used to support such an admission priority capability at the network layer.

 Based on current security concerns, these extensions are intended for use in a single administrative domain. [STANDARDS-TRACK]

### Recommendations for Transport-Protocol Port Randomization  (draft-ietf-tsvwg-port-randomization)
During the last few years, awareness has been raised about a number of "blind" attacks that can be performed against the Transmission Control Protocol (TCP) and similar protocols.  The consequences of these attacks range from throughput reduction to broken connections or data corruption.  These attacks rely on the attacker's ability to guess or know the five-tuple (Protocol, Source Address, Destination Address, Source Port, Destination Port) that identifies the transport protocol instance to be attacked.  This document describes a number of simple and efficient methods for the selection of the client port number, such that the possibility of an attacker guessing the exact value is reduced.  While this is not a replacement for cryptographic methods for protecting the transport-protocol instance, the aforementioned port selection algorithms provide improved security with very little effort and without any key management overhead.  The algorithms described in this document are local policies that may be incrementally deployed and that do not violate the specifications of any of the transport protocols that may benefit from them, such as TCP, UDP, UDP-lite, Stream Control Transmission Protocol (SCTP), Datagram Congestion Control Protocol (DCCP), and RTP (provided that the RTP application explicitly signals the RTP and RTCP port numbers).  This memo documents an Internet Best Current Practice.

### Specifying New Congestion Control Algorithms  (draft-ietf-tsvwg-cc-alt)
The IETF's standard congestion control schemes have been widely shown to be inadequate for various environments (e.g., high-speed networks).  Recent research has yielded many alternate congestion control schemes that significantly differ from the IETF's congestion control principles.  Using these new congestion control schemes in the global Internet has possible ramifications to both the traffic using the new congestion control and to traffic using the currently standardized congestion control.  Therefore, the IETF must proceed with caution when dealing with alternate congestion control proposals.  The goal of this document is to provide guidance for considering alternate congestion control algorithms within the IETF.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Unicast UDP Usage Guidelines for Application Designers  (draft-ietf-tsvwg-udp-guidelines)
The User Datagram Protocol (UDP) provides a minimal message-passing transport that has no inherent congestion control mechanisms.  Because congestion control is critical to the stable operation of the Internet, applications and upper-layer protocols that choose to use UDP as an Internet transport must employ mechanisms to prevent congestion collapse and to establish some degree of fairness with concurrent traffic.  This document provides guidelines on the use of UDP for the designers of unicast applications and upper-layer protocols.  Congestion control guidelines are a primary focus, but the document also provides guidance on other topics, including message sizes, reliability, checksums, and middlebox traversal.  This document specifies an Internet Best Current Practices for the Internet Community, and requests discussion and suggestions for improvements.

### Resource Reservation Protocol (RSVP) Proxy Approaches  (draft-ietf-tsvwg-rsvp-proxy-approaches)
The Resource Reservation Protocol (RSVP) can be used to make end-to- end resource reservations in an IP network in order to guarantee the quality of service required by certain flows.  RSVP assumes that both the data sender and receiver of a given flow take part in RSVP signaling.  Yet, there are use cases where resource reservation is required, but the receiver, the sender, or both, is not RSVP-capable.  This document presents RSVP proxy behaviors allowing RSVP routers to initiate or terminate RSVP signaling on behalf of a receiver or a sender that is not RSVP-capable.  This allows resource reservations to be established on a critical subset of the end-to-end path.  This document reviews conceptual approaches for deploying RSVP proxies and discusses how RSVP reservations can be synchronized with application requirements, despite the sender, receiver, or both not participating in RSVP.  This document also points out where extensions to RSVP (or to other protocols) may be needed for deployment of a given RSVP proxy approach.  However, such extensions are outside the scope of this document.  Finally, practical use cases for RSVP proxy are described.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Explicit Congestion Marking in MPLS  (draft-ietf-tsvwg-ecn-mpls)
RFC 3270 defines how to support the Diffserv architecture in MPLS networks, including how to encode Diffserv Code Points (DSCPs) in an MPLS header.  DSCPs may be encoded in the EXP field, while other uses of that field are not precluded.  RFC 3270 makes no statement about how Explicit Congestion Notification (ECN) marking might be encoded in the MPLS header.  This document defines how an operator might define some of the EXP codepoints for explicit congestion notification, without precluding other uses. [STANDARDS-TRACK]

### Byte and Packet Congestion Notification  (draft-ietf-tsvwg-byte-pkt-congest)
This document provides recommendations of best current practice for dropping or marking packets using any active queue management (AQM) algorithm, including Random Early Detection (RED), BLUE, Pre- Congestion Notification (PCN), and newer schemes such as CoDel (Controlled Delay) and PIE (Proportional Integral controller Enhanced).  We give three strong recommendations: (1) packet size should be taken into account when transports detect and respond to congestion indications, (2) packet size should not be taken into account when network equipment creates congestion signals (marking, dropping), and therefore (3) in the specific case of RED, the byte- mode packet drop variant that drops fewer small packets should not be used.  This memo updates RFC 2309 to deprecate deliberate preferential treatment of small packets in AQM algorithms.

### Support for the Resource Reservation Protocol (RSVP) in Layer 3 VPNs  (draft-ietf-tsvwg-rsvp-l3vpn)
RFC 4364 and RFC 4659 define an approach to building provider-provisioned Layer 3 VPNs (L3VPNs) for IPv4 and IPv6.  It may be desirable to use Resource Reservation Protocol (RSVP) to perform admission control on the links between Customer Edge (CE) routers and Provider Edge (PE) routers.  This document specifies procedures by which RSVP messages traveling from CE to CE across an L3VPN may be appropriately handled by PE routers so that admission control can be performed on PE-CE links.  Optionally, admission control across the provider's backbone may also be supported. [STANDARDS-TRACK]

## Working Group: v6ops
### Unintended Operational Issues With ULA  (draft-ietf-v6ops-ula)
The behavior of ULA addressing as defined by [RFC6724] is preferred
   below legacy IPv4 addressing, thus rendering ULA IPv6 deployment
   functionally unusable in IPv4 / IPv6 dual-stacked environments.  The
   lack of a consistent and supportable way to manipulate this behavior,
   across all platforms and at scale is counter to the operational
   behavior of GUA IPv6 addressing on nearly all modern operating
   systems that leverage a preference model based on [RFC6724] .

### IPv6 Deployment Status  (draft-ietf-v6ops-ipv6-deployment)
This document provides an overview of the status of IPv6 deployment in 2022.  Specifically, it looks at the degree of adoption of IPv6 in the industry, analyzes the remaining challenges, and proposes further investigations in areas where the industry has not yet taken a clear and unified approach in the transition to IPv6.  It obsoletes RFC 6036.

### IPv6-only Capable Resolvers Utilising NAT64  (draft-ietf-v6ops-ipv6-only-resolver)
This document outlines how IPv6-only iterative resolvers can use
   stateful NAT64 to establish communications with IPv4-only
   authoritative servers.  It outlines a mechanism for translating the
   IPv4 addresses of authoritative servers to IPv6 addresses to initiate
   communications.  Through the mechanism of IPv4-to-IPv6 address
   translation, these resolvers can operate in an IPv6-only network
   environment.

### IPv6-Mostly Networks: Deployment and Operations Considerations  (draft-link-v6ops-6mops)
This document discusses a deployment scenario called "an IPv6-Mostly
   network", when IPv6-only and IPv4-enabled endpoints coexist on the
   same network (network segment, VLAN, SSID etc).

### Basic Requirements for IPv6 Customer Edge Routers  (draft-ietf-v6ops-6204bis)
This document specifies requirements for an IPv6 Customer Edge (CE) router.  Specifically, the current version of this document focuses on the basic provisioning of an IPv6 CE router and the provisioning of IPv6 hosts attached to it.  The document also covers IP transition technologies.  Two transition technologies in RFC 5969's IPv6 Rapid Deployment on IPv4 Infrastructures (6rd) and RFC 6333's Dual-Stack Lite (DS-Lite) are covered in the document.  The document obsoletes RFC 6204.

### Considerations For Using Unique Local Addresses  (draft-ietf-v6ops-ula-usage-recommendations)
This document provides considerations for using IPv6 Unique Local
   Addresses (ULAs).  It identifies cases where ULA addresses are
   helpful as well as potential problems that their use could introduce,
   based on an analysis of different ULA usage scenarios.

### Transition Scenarios for 3GPP Networks  (draft-ietf-v6ops-3gpp-cases)
This document describes different scenarios in Third Generation Partnership Project (3GPP) defined packet network, i.e., General Packet Radio Service (GPRS) that would need IP version 6 and IP version 4 transition.  The focus of this document is on the scenarios where the User Equipment (UE) connects to nodes in other networks, e.g., in the Internet.  GPRS network internal transition scenarios, i.e., between different GPRS elements in the network, are out of scope.  The purpose of the document is to list the scenarios for further discussion and study.  This memo provides information for the Internet community.

### Analysis on IPv6 Transition in Third Generation Partnership Project (3GPP) Networks  (draft-ietf-v6ops-3gpp-analysis)
This document analyzes the transition to IPv6 in Third Generation Partnership Project (3GPP) packet networks. These networks are based on General Packet Radio Service (GPRS) technology, and the radio network architecture is based on Global System for Mobile Communications (GSM) or Universal Mobile Telecommunications System (UMTS)/Wideband Code Division Multiple Access (WCDMA) technology.

 The focus is on analyzing different transition scenarios and applicable transition mechanisms and finding solutions for those transition scenarios. In these scenarios, the User Equipment (UE) connects to other nodes, e.g., in the Internet, and IPv6/IPv4 transition mechanisms are needed. This memo provides information for the Internet community.

### Unmanaged Networks IPv6 Transition Scenarios  (draft-ietf-v6ops-unman-scenarios)
This document defines the scenarios in which IPv6 transition mechanisms are to be used in unmanaged networks.  In order to evaluate the suitability of these mechanisms, we need to define the scenarios in which these mechanisms have to be used.  One specific scope is the "unmanaged network", which typically corresponds to a home or small office network.  The scenarios are specific to a single subnet, and are defined in terms of IP connectivity supported by the gateway and the Internet Service Provider (ISP).  We first examine the generic requirements of four classes of applications: local, client, peer to peer and server.  Then, for each scenario, we infer transition requirements by analyzing the needs for smooth migration of applications from IPv4 to IPv6.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Application Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-apps)
This document describes IPv4 addressing dependencies in an attempt to clarify the necessary steps in re-designing and re-implementing specifications to become network address independent, or at least, to dually support IPv4 and IPv6.  This transition requires several interim steps, one of them being the evolution of current IPv4 dependent specifications to a format independent of the type of IP addressing schema used.  Hence, it is hoped that specifications will be re-designed and re-implemented to become network address independent, or at least to dually support IPv4 and IPv6.  To achieve that step, it is necessary to survey and document all IPv4 dependencies experienced by current standards (Full, Draft, and Proposed) as well as Experimental RFCs.  Hence, this document describes IPv4 addressing dependencies that deployed IETF Application Area documented Standards may experience.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF General Area Standards  (draft-ietf-v6ops-ipv4survey-gen)
This document seeks to document all usage of IPv4 addresses in currently
deployed IETF General Area documented standards.  In order to 
successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken. One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.

### Survey of IPv4 Addresses in Currently Deployed IETF Operations & Management Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-ops)
This document seeks to record all usage of IPv4 addresses in currently deployed IETF Operations & Management Area accepted standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed), as well as Experimental RFCs, will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Internet Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-int)
This document seeks to document all usage of IPv4 addresses in currently deployed IETF Internet Area documented standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### Introduction to the Survey of IPv4 Addresses in Currently Deployed IETF Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-intro)
This document is a general overview and introduction to the v6ops IETF workgroup project of documenting all usage of IPv4 addresses in IETF standards track and experimental RFCs.  It is broken into seven documents conforming to the current IETF areas.  It also describes the methodology used during documentation, which types of RFCs have been documented, and provides a concatenated summary of results.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Routing Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-routing)
This investigation work seeks to document all usage of IPv4 addresses in currently deployed IETF Routing Area documented standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Security Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-sec)
This document seeks to document all usage of IPv4 addresses in currently deployed IETF Security Area documented standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Sub-IP Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-subip)
This document seeks to document all usage of IPv4 addresses in currently deployed IETF Sub-IP Area documented standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### Survey of IPv4 Addresses in Currently Deployed IETF Transport Area Standards Track and Experimental Documents  (draft-ietf-v6ops-ipv4survey-trans)
This document seeks to document all usage of IPv4 addresses in currently deployed IETF Transport Area documented standards.  In order to successfully transition from an all IPv4 Internet to an all IPv6 Internet, many interim steps will be taken.  One of these steps is the evolution of current protocols that have IPv4 dependencies.  It is hoped that these protocols (and their implementations) will be redesigned to be network address independent, but failing that will at least dually support IPv4 and IPv6.  To this end, all Standards (Full, Draft, and Proposed) as well as Experimental RFCs will be surveyed and any dependencies will be documented.  This memo provides information for the Internet community.

### IPv6 Enterprise Networks Scenarios  (draft-ietf-v6ops-entnet-scenarios)
IPv6 will be deployed in Enterprise networks. This scenario has
requirements for the adoption of IPv6.  This document will focus upon
and define: a set of technology scenarios that shall exist for the
enterprise network, the set of transition variables, transition
methods, and tools required by different scenarios. The document
using these definitions will define the points of transition for an
Enterprise network.

### Basic Transition Mechanisms for IPv6 Hosts and Routers  (draft-ietf-v6ops-mech-v2)
This document specifies IPv4 compatibility mechanisms that can be implemented by IPv6 hosts and routers. Two mechanisms are specified, dual stack and configured tunneling. Dual stack implies providing complete implementations of both versions of the Internet Protocol (IPv4 and IPv6), and configured tunneling provides a means to carry IPv6 packets over unmodified IPv4 routing infrastructures.

 This document obsoletes RFC 2893. [STANDARDS-TRACK]

### IPv6 Transition/Co-existence Security Considerations  (draft-ietf-v6ops-security-overview)
The transition from a pure IPv4 network to a network where IPv4 and IPv6 coexist brings a number of extra security considerations that need to be taken into account when deploying IPv6 and operating the dual-protocol network and the associated transition mechanisms. This document attempts to give an overview of the various issues grouped into three categories:

 o issues due to the IPv6 protocol itself, o issues due to transition mechanisms, and o issues due to IPv6 deployment.

 This memo provides information for the Internet community.

### Evaluation of IPv6 Transition Mechanisms for Unmanaged Networks  (draft-ietf-v6ops-unmaneval)
This document analyzes issues involved in the transition of "unmanaged networks" from IPv4 to IPv6.  Unmanaged networks typically correspond to home networks or small office networks.  A companion paper analyzes out the requirements for mechanisms needed in various transition scenarios of these networks to IPv6.  Starting from this analysis, we evaluate the suitability of mechanisms that have already been specified, proposed, or deployed.  This memo provides information for the Internet community.

### Security Considerations for 6to4  (draft-ietf-v6ops-6to4-security)
The IPv6 interim mechanism 6to4 (RFC3056) uses automatic IPv6-over-IPv4 tunneling to interconnect IPv6 networks.  The architecture includes 6to4 routers and 6to4 relay routers, which accept and decapsulate IPv4 protocol-41 ("IPv6-in-IPv4") traffic from any node in the IPv4 internet.  This characteristic enables a number of security threats, mainly Denial of Service.  It also makes it easier for nodes to spoof IPv6 addresses.  This document discusses these issues in more detail and suggests enhancements to alleviate the problems.  This memo provides information for the Internet community.

### IPv6 Enterprise Network Scenarios  (draft-ietf-v6ops-ent-scenarios)
This document describes the scenarios for IPv6 deployment within enterprise networks.  It defines a small set of basic enterprise scenarios and includes pertinent questions to allow enterprise administrators to further refine their deployment scenarios.  Enterprise deployment requirements are discussed in terms of coexistence with IPv4 nodes, networks and applications, and in terms of basic network infrastructure requirements for IPv6 deployment.  The scenarios and requirements described in this document will be the basis for further analysis to determine what coexistence techniques and mechanisms are needed for enterprise IPv6 deployment.  The results of that analysis will be published in a separate document.  This memo provides information for the Internet community.

### Issues with Dual Stack IPv6 on by Default  (draft-ietf-v6ops-v6onbydefault)
This document discusses problems that can occur when dual stack nodes
   that have IPv6 enabled by default are deployed in IPv4 or mixed IPv4
   and IPv6 environments.  The problems include application connection
   delays, poor connectivity, and network insecurity.  The purpose of
   this memo is to raise awareness of these problems so that they can be
   fixed or worked around, not to try to specify whether IPv6 should be
   enabled by default or not.

### IPv6 Neighbor Discovery On-Link Assumption Considered Harmful  (draft-ietf-v6ops-onlinkassumption)
This document describes the historical and background information behind the removal of the "on-link assumption" from the conceptual host sending algorithm defined in Neighbor Discovery for IP Version 6 (IPv6).  According to the algorithm as originally described, when a host's default router list is empty, the host assumes that all destinations are on-link.  This is particularly problematic with IPv6-capable nodes that do not have off-link IPv6 connectivity (e.g., no default router).  This document describes how making this assumption causes problems and how these problems outweigh the benefits of this part of the conceptual sending algorithm.  This memo provides information for the Internet community.

### Scenarios and Analysis for Introducing IPv6 into ISP Networks  (draft-ietf-v6ops-isp-scenarios-analysis)
This document describes different scenarios for the introduction of IPv6 into an ISP's existing IPv4 network without disrupting the IPv4 service.  The scenarios for introducing IPv6 are analyzed, and the relevance of already defined transition mechanisms are evaluated.  Known challenges are also identified.  This memo provides information for the Internet community.

### Application Aspects of IPv6 Transition  (draft-ietf-v6ops-application-transition)
As IPv6 networks are deployed and the network transition is discussed, one should also consider how to enable IPv6 support in applications running on IPv6 hosts, and the best strategy to develop IP protocol support in applications.  This document specifies scenarios and aspects of application transition.  It also proposes guidelines on how to develop IP version-independent applications during the transition period.  This memo provides information for the Internet community.

### Procedures for Renumbering an IPv6 Network without a Flag Day  (draft-ietf-v6ops-renumbering-procedure)
This document describes a procedure that can be used to renumber a network from one prefix to another.  It uses IPv6's intrinsic ability to assign multiple addresses to a network interface to provide continuity of network service through a "make-before-break" transition, as well as addresses naming and configuration management issues.  It also uses other IPv6 features to minimize the effort and time required to complete the transition from the old prefix to the new prefix.  This memo provides information for the Internet community.

### Using IPsec to Secure IPv6-in-IPv4 Tunnels  (draft-ietf-v6ops-ipsec-tunnels)
This document gives guidance on securing manually configured IPv6-in- IPv4 tunnels using IPsec in transport mode.  No additional protocol extensions are described beyond those available with the IPsec framework.  This memo provides information for the Internet community.

### Goals for Registered Assisted Tunneling  (draft-ietf-v6ops-assisted-tunneling-requirements)
This document defines requirements for a tunnel set-up protocol that
   could be used by an ISP to jumpstart its IPv6 offering to its
   customers by providing them IPv6 connectivity through tunneling.

### ISP IPv6 Deployment Scenarios in Broadband Access Networks  (draft-ietf-v6ops-bb-deployment-scenarios)
This document provides a detailed description of IPv6 deployment and integration methods and scenarios in today\'s Service Provider (SP) Broadband (BB) networks in coexistence with deployed IPv4 services.  Cable/HFC, BB Ethernet, xDSL, and WLAN are the main BB technologies that are currently deployed, and discussed in this document.  The emerging Broadband Power Line Communications (PLC/BPL) access technology is also discussed for completeness.  In this document we will discuss main components of IPv6 BB networks, their differences from IPv4 BB networks, and how IPv6 is deployed and integrated in each of these networks using tunneling mechanisms and native IPv6.  This memo provides information for the Internet community.

### IPv6 Enterprise Network Analysis - IP Layer 3 Focus  (draft-ietf-v6ops-ent-analysis)
This document analyzes the transition to IPv6 in enterprise networks focusing on IP Layer 3.  These networks are characterized as having multiple internal links and one or more router connections to one or more Providers, and as being managed by a network operations entity.  The analysis focuses on a base set of transition notational networks and requirements expanded from a previous document on enterprise scenarios.  Discussion is provided on a focused set of transition analysis required for the enterprise to transition to IPv6, assuming a Dual-IP layer (IPv4 and IPv6) network and node environment within the enterprise.  Then, a set of transition mechanisms are recommended for each notational network.  This memo provides information for the Internet community.

### Reasons to Move NAT-PT to Experimental  (draft-ietf-v6ops-natpt-to-exprmntl)
This document discusses issues with the specific form of IPv6-IPv4
   protocol translation mechanism implemented by the Network Address
   Translator - Protocol Translator (NAT-PT) defined in RFC 2766.  These
   issues are sufficiently serious that recommending RFC 2766 as a
   general purpose transition mechanism is no longer desirable, and this
   document recommends that the IETF should reclassify RFC 2766 from
   Standards Track to Experimental status.

### Reasons to Move the Network Address Translator - Protocol Translator (NAT-PT) to Historic Status  (draft-ietf-v6ops-natpt-to-historic)
This document discusses issues with the specific form of IPv6-IPv4 protocol translation mechanism implemented by the Network Address Translator - Protocol Translator (NAT-PT) defined in RFC 2766.  These issues are sufficiently serious that recommending RFC 2766 as a general purpose transition mechanism is no longer desirable, and this document recommends that the IETF should reclassify RFC 2766 from Proposed Standard to Historic status.  This memo provides information for the Internet community.

### Local Network Protection for IPv6  (draft-ietf-v6ops-nap)
Although there are many perceived benefits to Network Address Translation (NAT), its primary benefit of "amplifying" available address space is not needed in IPv6.  In addition to NAT's many serious disadvantages, there is a perception that other benefits exist, such as a variety of management and security attributes that could be useful for an Internet Protocol site.  IPv6 was designed with the intention of making NAT unnecessary, and this document shows how Local Network Protection (LNP) using IPv6 can provide the same or more benefits without the need for address translation.  This memo provides information for the Internet community.

### IPv6 Address Assignment to End Sites  (draft-ietf-v6ops-3177bis-end-sites)
RFC 3177 argued that in IPv6, end sites should be assigned /48 blocks in most cases. The Regional Internet Registries (RIRs) adopted that recommendation in 2002, but began reconsidering the policy in 2005. This document obsoletes the RFC 3177 recommendations on the assignment of IPv6 address space to end sites. The exact choice of how much address space to assign end sites is an issue for the operational community. The IETF's role in this case is limited to providing guidance on IPv6 architectural and operational considerations. This document reviews the architectural and operational considerations of end site assignments as well as the motivations behind the original recommendations in RFC 3177. Moreover, this document clarifies that a one-size-fits-all recommendation of /48 is not nuanced enough for the broad range of end sites and is no longer recommended as a single default.

 This document obsoletes RFC 3177. [STANDARDS-TRACK]

### Use of VLANs for IPv4-IPv6 Coexistence in Enterprise Networks  (draft-ietf-v6ops-vlan-usage)
Ethernet VLANs are quite commonly used in enterprise networks for the purposes of traffic segregation.  This document describes how such VLANs can be readily used to deploy IPv6 networking in an enterprise, which focuses on the scenario of early deployment prior to availability of IPv6-capable switch-router equipment.  In this method, IPv6 may be routed in parallel with the existing IPv4 in the enterprise and delivered at Layer 2 via VLAN technology.  The IPv6 connectivity to the enterprise may or may not enter the site via the same physical link.  This memo provides information for the Internet community.

### Unique IPv6 Prefix per Host  (draft-ietf-v6ops-unique-ipv6-prefix-per-host)
This document outlines an approach utilizing existing IPv6 protocols to allow hosts to be assigned a unique IPv6 prefix (instead of a unique IPv6 address from a shared IPv6 prefix).  Benefits of using a unique IPv6 prefix over a unique service-provider IPv6 address include improved host isolation and enhanced subscriber management on shared network segments.

### Best Current Practice for Filtering ICMPv6 Messages in Firewalls  (draft-ietf-v6ops-icmpv6-filtering-bcp)
In networks supporting IPv6 the Internet Control Message Protocol
version 6 (ICMPv6) plays a fundamental role with a large number of
functions, and a correspondingly large number of message types and
options.  A number of security risks are associated with uncontrolled
forwarding of ICMPv6 messages.  On the other hand, compared with IPv4
and the corresponding protocol ICMP, ICMPv6 is essential to the
functioning of IPv6 rather than a useful auxiliary.

This document provides some recommendations for ICMPv6 firewall
filter configuration that will allow propagation of ICMPv6 messages
that are needed to maintain the functioning of the network but drop
messages which are potential security risks.

### Recommendations for Filtering ICMPv6 Messages in Firewalls  (draft-ietf-v6ops-icmpv6-filtering-recs)
In networks supporting IPv6, the Internet Control Message Protocol version 6 (ICMPv6) plays a fundamental role with a large number of functions, and a correspondingly large number of message types and options. ICMPv6 is essential to the functioning of IPv6, but there are a number of security risks associated with uncontrolled forwarding of ICMPv6 messages. Filtering strategies designed for the corresponding protocol, ICMP, in IPv4 networks are not directly applicable, because these strategies are intended to accommodate a useful auxiliary protocol that may not be required for correct functioning.

 This document provides some recommendations for ICMPv6 firewall filter configuration that will allow propagation of ICMPv6 messages that are needed to maintain the functioning of the network but drop messages that are potential security risks. This memo provides information for the Internet community.

### IPv6 Unicast Address Assignment Considerations  (draft-ietf-v6ops-addcon)
One fundamental aspect of any IP communications infrastructure is its addressing plan.  With its new address architecture and allocation policies, the introduction of IPv6 into a network means that network designers and operators need to reconsider their existing approaches to network addressing.  Lack of guidelines on handling this aspect of network design could slow down the deployment and integration of IPv6.  This document aims to provide the information and recommendations relevant to planning the addressing aspects of IPv6 deployments.  The document also provides IPv6 addressing case studies for both an enterprise and an ISP network.  This memo provides information for the Internet community.

### IPv6 Deployment Scenarios in 802.16 Networks  (draft-ietf-v6ops-802-16-deployment-scenarios)
This document provides a detailed description of IPv6 deployment and integration methods and scenarios in wireless broadband access networks in coexistence with deployed IPv4 services.  In this document, we will discuss the main components of IPv6 IEEE 802.16 access networks and their differences from IPv4 IEEE 802.16 networks and how IPv6 is deployed and integrated in each of the IEEE 802.16 technologies.  This memo provides information for the Internet community.

### Problem Statement for Default Address Selection in Multi-Prefix Environments: Operational Issues of RFC 3484 Default Rules  (draft-ietf-v6ops-addr-select-ps)
A single physical link can have multiple prefixes assigned to it.  In that environment, end hosts might have multiple IP addresses and be required to use them selectively.  RFC 3484 defines default source and destination address selection rules and is implemented in a variety of OSs.  But, it has been too difficult to use operationally for several reasons.  In some environments where multiple prefixes are assigned on a single physical link, the host using the default address selection rules will experience some trouble in communication.  This document describes the possible problems that end hosts could encounter in an environment with multiple prefixes.  This memo provides information for the Internet community.

### IPv6 Implications for Network Scanning  (draft-ietf-v6ops-scanning-implications)
The much larger default 64-bit subnet address space of IPv6 should in principle make traditional network (port) scanning techniques used by certain network worms or scanning tools less effective.  While traditional network scanning probes (whether by individuals or automated via network worms) may become less common, administrators should be aware that attackers may use other techniques to discover IPv6 addresses on a target network, and thus they should also be aware of measures that are available to mitigate them.  This informational document discusses approaches that administrators could take when planning their site address allocation and management strategies as part of a defence-in-depth approach to network security.  This memo provides information for the Internet community.

### Requirements for Address Selection Mechanisms  (draft-ietf-v6ops-addr-select-req)
There are some problematic cases when using the default address selection mechanism that RFC 3484 defines.  This document describes additional requirements that operate with RFC 3484 to solve the problems.  This memo provides information for the Internet community.

### Special-Use IPv6 Addresses  (draft-ietf-v6ops-rfc3330-for-ipv6)
This document is a compilation of special IPv6 addresses defined in other RFCs.  It can be used as a checklist of invalid routing prefixes for developing filtering policies for routes and IP packets.  It does not discuss addresses that are assigned to operators and users through the Regional Internet Registries.  This memo provides information for the Internet community.

### Recommended Simple Security Capabilities in Customer Premises Equipment (CPE) for Providing Residential IPv6 Internet Service  (draft-ietf-v6ops-cpe-simple-security)
This document identifies a set of recommendations for the makers of devices and describes how to provide for "simple security" capabilities at the perimeter of local-area IPv6 networks in Internet-enabled homes and small offices.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Teredo Security Concerns  (draft-ietf-v6ops-teredo-security-concerns)
Additional security concerns with Teredo are documented, beyond what
is in RFC 4380.  This is based on an independent analysis of Teredo's
security implications.  The primary intent of this document is to
raise the awareness regarding the security issues in Teredo as
deployed today.

### Security Concerns with IP Tunneling  (draft-ietf-v6ops-tunnel-security-concerns)
A number of security concerns with IP tunnels are documented in this memo.  The intended audience of this document includes network administrators and future protocol developers.  The primary intent of this document is to raise the awareness level regarding the security issues with IP tunnels as deployed and propose strategies for the mitigation of those issues. [STANDARDS-TRACK]

### Rogue IPv6 Router Advertisement Problem Statement  (draft-ietf-v6ops-rogue-ra)
When deploying IPv6, whether IPv6-only or dual-stack, routers are configured to send IPv6 Router Advertisements (RAs) to convey information to nodes that enable them to autoconfigure on the network.  This information includes the implied default router address taken from the observed source address of the RA message, as well as on-link prefix information.  However, unintended misconfigurations by users or administrators, or possibly malicious attacks on the network, may lead to bogus RAs being present, which in turn can cause operational problems for hosts on the network.  In this document, we summarise the scenarios in which rogue RAs may be observed and present a list of possible solutions to the problem.  We focus on the unintended causes of rogue RAs in the text.  The goal of this text is to be Informational, and as such to present a framework around which solutions can be proposed and discussed.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Basic Requirements for IPv6 Customer Edge Routers  (draft-ietf-v6ops-ipv6-cpe-router)
This document specifies requirements for an IPv6 Customer Edge (CE) router.  Specifically, the current version of this document focuses on the basic provisioning of an IPv6 CE router and the provisioning of IPv6 hosts attached to it.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### IPv6 Router Advertisement Guard  (draft-ietf-v6ops-ra-guard)
Routed protocols are often susceptible to spoof attacks.  The canonical solution for IPv6 is Secure Neighbor Discovery (SEND), a solution that is non-trivial to deploy.  This document proposes a light-weight alternative and complement to SEND based on filtering in the layer-2 network fabric, using a variety of filtering criteria, including, for example, SEND status.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### An Incremental Carrier-Grade NAT (CGN) for IPv6 Transition  (draft-ietf-v6ops-incremental-cgn)
Global IPv6 deployment was slower than originally expected. As IPv4 address exhaustion approaches, IPv4 to IPv6 transition issues become more critical and less tractable. Host-based transition mechanisms used in dual-stack environments cannot meet all transition requirements. Most end users are not sufficiently expert to configure or maintain host-based transition mechanisms. Carrier-Grade NAT (CGN) devices with integrated transition mechanisms can reduce the operational changes required during the IPv4 to IPv6 migration or coexistence period.

 This document proposes an incremental CGN approach for IPv6 transition. It can provide IPv6 access services for IPv6 hosts and IPv4 access services for IPv4 hosts while leaving much of a legacy ISP network unchanged during the initial stage of IPv4 to IPv6 migration. Unlike CGN alone, incremental CGN also supports and encourages smooth transition towards dual-stack or IPv6-only ISP networks. An integrated configurable CGN device and an adaptive home gateway (HG) device are described. Both are reusable during different transition phases, avoiding multiple upgrades. This enables IPv6 migration to be incrementally achieved according to real user requirements. This document is not an Internet Standards Track specification; it is published for informational purposes.

### IPv6 Deployment in Internet Exchange Points (IXPs)  (draft-ietf-v6ops-v6inixp)
This document provides guidance on IPv6 deployment in Internet Exchange Points (IXPs).  It includes information regarding the switch fabric configuration, the addressing plan and general organizational tasks that need to be performed.  IXPs are mainly a Layer 2 infrastructure, and, in many cases, the best recommendations suggest that the IPv6 data, control, and management plane should not be handled differently than in IPv4.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Emerging Service Provider Scenarios for IPv6 Deployment  (draft-ietf-v6ops-isp-scenarios)
This document describes practices and plans that are emerging among Internet Service Providers for the deployment of IPv6 services.  They are based on practical experience so far, as well as current plans and requirements, reported in a survey of a number of ISPs carried out in early 2010.  This document identifies a number of technology gaps, but it does not make recommendations.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Routing Loop Attack Using IPv6 Automatic Tunnels: Problem Statement and Proposed Mitigations  (draft-ietf-v6ops-tunnel-loops)
This document is concerned with security vulnerabilities in IPv6-in- IPv4 automatic tunnels.  These vulnerabilities allow an attacker to take advantage of inconsistencies between the IPv4 routing state and the IPv6 routing state.  The attack forms a routing loop that can be abused as a vehicle for traffic amplification to facilitate denial- of-service (DoS) attacks.  The first aim of this document is to inform on this attack and its root causes.  The second aim is to present some possible mitigation measures.  It should be noted that at the time of this writing there are no known reports of malicious attacks exploiting these vulnerabilities.  Nonetheless, these vulnerabilities can be activated by accidental misconfiguration.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### IPv6 in 3rd Generation Partnership Project (3GPP) Evolved Packet System (EPS)  (draft-ietf-v6ops-3gpp-eps)
The use of cellular broadband for accessing the Internet and other data services via smartphones, tablets, and notebook/netbook computers has increased rapidly as a result of high-speed packet data networks such as HSPA, HSPA+, and now Long-Term Evolution (LTE) being deployed.  Operators that have deployed networks based on 3rd Generation Partnership Project (3GPP) network architectures are facing IPv4 address shortages at the Internet registries and are feeling pressure to migrate to IPv6.  This document describes the support for IPv6 in 3GPP network architectures.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### Mobile Networks Considerations for IPv6 Deployment  (draft-ietf-v6ops-v6-in-mobile-networks)
Mobile Internet access from smartphones and other mobile devices is accelerating the exhaustion of IPv4 addresses.  IPv6 is widely seen as crucial for the continued operation and growth of the Internet, and in particular, it is critical in mobile networks.  This document discusses the issues that arise when deploying IPv6 in mobile networks.  Hence, this document can be a useful reference for service providers and network designers.  This document is not an Internet Standards Track specification; it is published for informational purposes.

### IPv6 Multihoming without Network Address Translation  (draft-ietf-v6ops-multihoming-without-nat66)
Network Address and Port Translation (NAPT) works well for conserving
global addresses and addressing multihoming requirements, because an
IPv4 NAPT router implements three functions: source address
selection, next-hop resolution and optionally DNS resolution.  For
IPv6 hosts one approach could be the use of IPv6 NAT.  However, NAT
should be avoided, if at all possible, to permit transparent host-to-
host connectivity.  In this document, we analyze the use cases of
multihoming.  We also describe functional requirements for
multihoming without the use of NAT in IPv6 for hosts and small IPv6
networks that would otherwise be unable to meet minimum IPv6
allocation criteria .

## Working Group: wimse
### Workload Identity in a Multi System Environment (WIMSE) Architecture  (draft-salowey-wimse-arch)
The increasing prevalence of cloud computing and micro service
   architectures has led to the rise of complex software functions being
   built and deployed as workloads, where a workload is defined as a
   running instance of software executing for a specific purpose.  This
   document discusses an architecture for designing and standardizing
   protocols and payloads for conveying workload identity and security
   context information.

### OAuth 2.0 Client Assertion in Workload Environments  (draft-ietf-wimse-workload-identity-bcp)
The use of the OAuth 2.0 framework for container orchestration
   systems poses a challenge as managing secrets, such as client_id and
   client_secret, can be complex and error-prone.  Instead of manual
   provisioning these credentials the industry has moved to a
   federation-based approach where credentials of the underlying
   workload platform are used as assertions towards an OAuth
   authorization server leveraging the Client Assertion Flow [RFC7521],
   in particular [RFC7523].

   This specification describes a meta flow in Section 3.1, gives
   security recommendations in Section 4 and outlines concrete patterns
   in Appendix A.

### Workload Identity Practices  (draft-ietf-wimse-workload-identity-practices)
This document describes industry practices for providing secure
   identities to workloads in container orchestration, cloud platforms,
   and other workload platforms.  It explains how workloads obtain
   credentials for external authentication purposes, without managing
   long-lived secrets directly.  It does not take into account the
   standards work in progress for the WIMSE architecture [WIMSE-ARCH]
   and other protocols, such as [WIMSE-HTTPSIG].

### WIMSE Workload-to-Workload Authentication  (draft-ietf-wimse-s2s-protocol)
The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones up to complex multi-service, multi-cloud, multi-
   tenant deployments.  This document defines the simplest, atomic unit
   of this architecture: the protocol between two workloads that need to
   verify each other's identity in order to communicate securely.  The
   scope of this protocol is a single HTTP request-and-response pair.
   To address the needs of different setups, we propose two protocols,
   one at the application level and one that makes use of trusted TLS
   transport.  These two protocols are compatible, in the sense that a
   single call chain can have some calls use one protocol and some use
   the other.  Workload A can call Workload B with mutual TLS
   authentication, while the next call from Workload B to Workload C
   would be authenticated at the application level.

### Workload Identifier  (draft-ietf-wimse-identifier)
This document defines a canonical identifier for workloads, referred
   to as the Workload Identifier.  A Workload Identifier is a URI that
   uniquely identifies a workload within the context of a specific trust
   domain.  This identifier can be embedded in digital credentials,
   including X.509 certificates and security tokens, to support
   authentication, authorization, and policy enforcement across diverse
   systems.  The Workload Identifier format ensures interoperability,
   facilitates secure identity federation, and enables consistent
   identity semantics.

### Workload Authentication Using Mutual TLS  (draft-ietf-wimse-mutual-tls)
The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document profiles a workload authentication based
   on X.509 workload identity certificates using mutual TLS (mTLS).

### WIMSE Workload Credentials  (draft-ietf-wimse-workload-creds)
The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones up to complex multi-service, multi-cloud, multi-
   tenant deployments.

   This document defines the credentials that workloads use to represent
   their identity.  They can be used in various protocols to
   authenticate workloads to each other.  To use these credentials,
   workloads must provide proof of possession of the associated private
   key material, which is covered in other documents.  This document
   focuses on the credentials alone, independent of the proof-of-
   possession mechanism.

### WIMSE Workload Proof Token  (draft-ietf-wimse-wpt)
The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from basic
   deployments to complex multi-service, multi-cloud, multi-tenant
   systems.  This document specifies the Workload Proof Token (WPT), a
   mechanism for workloads to prove possession of the private key
   associated with a Workload Identity Token (WIT).  The WPT is a signed
   JWT that binds the workload's authentication to a specific HTTP
   request, providing application-level proof of possession for
   workload-to-workload communication.  This specification is designed
   to work alongside the WIT credential format defined in draft-ietf-
   wimse-workload-creds and can be combined with other WIMSE protocols
   in multi-hop call chains.

### WIMSE Workload-to-Workload Authentication with HTTP Signatures  (draft-ietf-wimse-http-signature)
The WIMSE architecture defines authentication and authorization for
   software workloads in a variety of runtime environments, from the
   most basic ones to complex multi-service, multi-cloud, multi-tenant
   deployments.  This document defines one of the mechanisms to provide
   workload authentication, using HTTP Signatures.  While only
   applicable to HTTP traffic, the protocol provides end-to-end
   protection of requests (and optionally, responses), even when service
   traffic is not end-to-end encrypted, that is, when TLS proxies and
   load balancers are used.  Authentication is based on the Workload
   Identity Token (WIT).

### Workload Identity in a Multi System Environment (WIMSE) Architecture  (draft-ietf-wimse-arch)
The increasing prevalence of cloud computing and micro service
   architectures has led to the rise of complex software functions being
   built and deployed as workloads, where a workload is defined as
   software executing for a specific purpose, potentially comprising one
   or more running instances.  This document discusses an architecture
   for designing and standardizing protocols and payloads for conveying
   workload identity and security context information.

