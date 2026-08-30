>>> HOW TO RUN THIS <<<
This is the digest prompt for srecon-2025-americas. If you are a Claude session with
filesystem access to the conference-digest repo, you can read this same
file directly from `prompts/srecon-2025-americas.md` instead of having it pasted.
Produce the digest below and SAVE IT as a markdown file at exactly:
    digests/srecon-2025-americas.md
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

Below is the program for SREcon25 Americas (operator). Read it and produce a digest
of the talks/papers/sessions most worth their attention.

## How to read this program

This is an operator program (network/infrastructure operators). Focus on
operational practice, failure stories, and techniques that transfer across
environments rather than org-specific anecdotes. Up-rank concrete postmortems,
tooling and automation that others can adopt, and hard-won lessons about
running networks at scale. Down-rank vendor-sponsored sessions that are pitches
in disguise. Note when a technique depends on a specific operator's scale or
topology.

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
conference: SREcon25 Americas
type: operator
source_url: https://www.usenix.org/conference/srecon25americas/program
generated: 2026-08-30
registry_key: srecon-2025-americas
-->

Then the digest as markdown (tiers as `##` sections, Themes as a final `##`
section).

============================ PROGRAM TEXT ============================


Program Co-Chairs: Dan Fainstein, The D. E. Shaw Group; Laura Maguire, Trace Cognitive Engineering

9:00 am–10:30 am
Hide details  ▾

Opening Plenary Session
Grand Ballroom ABGH
Safe Evaluation and Rollout of AI Models
Tuesday, 9:00 am–9:45 am PDT
Brendan Burns, Microsoft

Available Media
Hide details  ▾  
More and more online services and systems depend on artificial intelligence and large language models to implement core user experiences. Consequently, the safe and reliable rollout of new models and new prompts are critical parts of maintaining the reliability and performance of the overall system. However, unlike traditional systems, there is rarely a clean "working" or "broken" signal from releases. Instead the performance of new models and new prompts is based on probabilistic evaluation of the performance of the new system across many different user inputs. Any change to model or prompt may make some responses better, some responses worse, we need to be able to measure in aggregate across many experiences to determine if there is a regression that needs to be fixed or rolled back. This talk will be a hands-on introduction to approaches that we took during the development of the Azure Copilot and will both describe the problem of reliability in the world of AI models as well as real-world applications that are in use in production today.


Brendan Burns is Corporate Vice President for Azure Cloud Native Open Source and Management Platform. He is also a co-founder of the Kubernetes open source project. Before working at Microsoft Azure, he spent eight years working at Google where he worked on search infrastructure and the Google Cloud Platform. Prior to Google he was a Professor of Computer Science at Union College in Schnectady, NY. He has a PhD in Computer Science from the University of Massachusetts Amherst and a BA in Computer Science and Studio Art from Williams College, in Williamstown MA.

Improving the SRE Experience for 10 Years as a Free, Open, and Automated Certificate Authority
Tuesday, 9:45 am–10:30 am PDT
Matthew McPherrin, Internet Security Research Group

Available Media
Hide details  ▾  
Ubiquitous HTTPS is an essential part of a secure and privacy-respecting Internet. To that end, the public benefit certificate authority Let’s Encrypt has been issuing TLS certificates free of cost in a reliable, automated, and trustworthy manner for ten years. In that time, we’ve grown to servicing over 500,000,000 websites.

In this talk we’ll dive into the history of Let’s Encrypt and share helpful context for those managing TLS certificates, as well as information about upcoming changes to Let’s Encrypt and guidance for the future. We’ll also cover how we have strived to make the working lives of SREs around the world easier, and how the SRE community has helped us in return.


Matthew is the technical lead of the Let's Encrypt site reliability engineering team, which runs the Let’s Encrypt Certificate Authority and Certificate Transparency logs. Previously Matthew worked on internal PKI and security infrastructure at Stripe and Square.

Connect: 
Mastodon
Bluesky
10:30 am–11:00 am
Coffee and Tea Break
Grand Ballroom CDEF

11:00 am–12:35 pm
Track 1
Hide details  ▾

Grand Ballroom AB
An SRE Approach to Monitoring ML in Production
Tuesday, 11:00 am–11:45 am PDT
Daria Barteneva, Microsoft Azure

Available Media
Hide details  ▾  
Machine Learning (ML) is becoming a part of many aspects of SRE life. As an SRE, we are (or will be soon) dealing with the challenge of serving ML models as part of a large distributed production system. Unfortunately the domain expertise required to build ML doesn't overlap with the expertise required to run large distributed system. The SRE community lacks standard practices and experiences that would allow us to operationalize ML and help to answer critical question: how exactly do we operate ML at scale reliably?

In this talk we will explore the (lack of) overlap between ML and SRE domains and discuss how we can help practitioners to solve common challenges. Scoping this talk to ML Observability we will be decomposing a complex system into its primary components helping engineers to bridge domain expertise gap in making ML systems more observable.

But when our production system serves ML models, relying only on traditional observability practices is not enough. We will review the characteristics and requirements specific to serving ML in production and discuss mechanisms that will help us to understand the end to end system reliability and quality.


Daria is a Principal Site Reliability Engineer in Observability Engineering in Azure. With a background in Applied Mathematics, Artificial Intelligence, and Music, Daria is passionate about machine learning, diversity in tech, and opera. In her current role, Daria is focused on changing organisational culture, processes, and platforms to improve service reliability and on-call experience. She has spoken at conferences on various aspects of reliability and human factors that play a key role in engineering practices, and has written for O'Reilly. Daria is originally from Moscow, Russia, having spent 20 years in Portugal, 10 years in Ireland, and now lives in the Pacific NorthWest.

Transformers in SRE Land: Evolving to Manage AI Infrastructure
Tuesday, 11:50 am–12:35 pm PDT
Qian Ding, Ant Group

Available Media
Hide details  ▾  
The rapid advancement of AI has fundamentally transformed the technological landscape. As AI models grow in complexity and scale, the challenges of managing the underlying infrastructure have intensified commensurately. This presentation explores the unique demands of AI infrastructure and how SREs can adapt to this evolving environment.

We'll delve into the specific challenges of managing GPU-accelerated clusters, including anomaly detection, node lifecycle management, and the distinctive requirements of AI workloads. By sharing real-world experiences and lessons learned, we aim to provide valuable insights into how SREs can effectively navigate this new frontier, ensuring the reliability, scalability, and performance of AI infrastructure.


Qian is a staff engineer at Ant Group, specializing in site reliability engineering. He leads the infrastructure SRE team, applying SRE principles to manage AI infrastructure. His expertise spans heterogeneous cluster management, xPU maintenance, and leveraging observability to enhance the team's capability in diagnosing model training and inference issues. With a wealth of experience in infrastructure management, Qian is currently exploring the evolving skill set required for SRE professionals in the era of large language models. His goal is to adapt and grow in this rapidly changing technological landscape, ensuring that SRE practices remain at the forefront of AI infrastructure management.

Connect: 
LinkedIn
X
Track 2
Hide details  ▾

Grand Ballroom GH
Tackling Slow Queries: A Practical Approach to Prevention and Correction
Tuesday, 11:00 am–11:45 am PDT
Kurni Famili and Brad Feehan, Shopify

Available Media
Hide details  ▾  
Slow queries can cripple the reliability of production systems, leading to performance bottlenecks and user dissatisfaction. This session explores a dual-component framework for tackling slow queries, covering preventive measures integrated into CI pipelines and corrective actions utilizing production monitoring. Attendees will gain actionable insights to boost their systems’ reliability by identifying and resolving slow queries effectively.


Kurni Famili is a Senior Site Reliability Engineer at Shopify, originally from Indonesia and now living in Singapore. They have a broad interest in system reliability, with a particular focus on databases and observability. At Shopify, they work alongside teams to improve infrastructure performance, making sure systems are reliable and scalable.

Connect: 
LinkedIn

Brad Feehan is a Senior Site Reliability Engineer at Shopify, currently based in Melbourne, Australia. With over a decade of experience in high-traffic web applications, they have a deep understanding of every layer of the tech stack. Starting in full-stack web development, they transitioned to focus on the back-end and then developed expertise in system administration, DevOps, and SRE principles, all while maintaining a passion for exploring new technologies and how things work.

Connect: 
LinkedIn
The Search for Speed
Tuesday, 11:50 am–12:35 pm PDT
Scott Laird

Available Media
Hide details  ▾  
What do you do when you're new to a service and all you know is that you're spending huge amounts of money on it and no one is happy with the service's performance? You use science, of course!

The speaker joined a team with a severe OpenSearch performance problem and applied basic monitoring principles, built models to understand the problem space, conducted experiments to understand what was happening under the hood of a managed service, and then halved the system's latency, cut costs by more than half, and left the team with a framework for further improvement.


Scott worked as an SRE at Google for 17 years, working on many products including Chrome, Google Docs, Calendar, and storage in Google Cloud, but never search. More recently he worked as a part of Figma's Production Engineering team.

He lives in the Seattle area and holds strong opinions on monitoring, sources of truth, and Terraform.

Discussion Track
Hide details  ▾

Magnolia Room
Running ML in Production
Tuesday, 11:00 am–12:35 pm PDT
Todd Underwood, Anthropic, and Brendan Burns, Microsoft

Format: Breakout Group Discussion

Hide details  ▾  
Running ML systems is a major new area for many SRE organizations. This session will dive into the differences between running reliable software services in general and ML systems: infrastructure considerations, monitoring, rollouts, performance and cost management, and more.


Todd Underwood leads reliability at Anthropic, a company working to create AI systems that are safe, reliable, and beneficial to society.

Prior to that he led reliability for the Research Platform at Open AI. Before that he was a Senior Engineering Director at Google leading ML capacity engineering at Alphabet. Before that, he founded and led ML Site Reliability Engineering, a set of teams that build and scale internal and external AI/ML services. He was also the Site Lead for Google’s Pittsburgh office. Along with several colleagues, he published Reliable Machine Learning: Applying SRE Principles to ML in Production (O’Reilly Press, 2022).


Brendan Burns is Corporate Vice President for Azure Cloud Native Open Source and Management Platform. He is also a co-founder of the Kubernetes open source project. Before working at Microsoft Azure, he spent eight years working at Google where he worked on search infrastructure and the Google Cloud Platform. Prior to Google he was a Professor of Computer Science at Union College in Schnectady, NY. He has a PhD in Computer Science from the University of Massachusetts Amherst and a BA in Computer Science and Studio Art from Williams College, in Williamstown MA.

12:35 pm–1:50 pm
Luncheon
Santa Clara Ballroom

Sponsored by Causely

1:50 pm–3:25 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Case Study: A Thundering Herd in the Wild
Tuesday, 1:50 pm–2:35 pm PDT
Nicolas Arroyo, Bloomberg LP

Available Media
Hide details  ▾  
The 'thundering herd problem' is an issue that occurrs when multiple threads wait on the same event and are all woken up at the same time. If only one thread can handle the event, then that means that the others waste resources with noop context switches. This problem has been largely resolved in modern kernels and through the use of notification APIs (e.g., epoll, kqueue, and/or IOCP).

We will present how we investigated and identified an unexpected variant of this problem. We will review our performance troubleshooting process, starting with aggregated sampling, followed by dynamic instrumentation and detailed sampling, and finally, kernel mode sampling. With every step, we will explain what information we gained to help us discover the problem: system calls buried inside commonly used libraries that use absolute timers, which caused threads to synchronize and led to a multitude of threads waking up at the same time.


Nicolas Arroyo is a seasoned developer with 20 years of experience across diverse domains, including machine learning, data science, security, performance, systems architecture, embedded systems, distributed systems, and networking. He is passionate about performance optimization, scalability, and solving complex technical challenges. Currently he focuses on performance analysis and tooling for low-latency/high-throughput financial systems.

Connect: 
LinkedIn
Techniques Netflix Uses to Weather Significant Demand Shifts
Tuesday, 2:40 pm–3:25 pm PDT
Joseph Lynch, Netflix

Available Media
Hide details  ▾  
Netflix runs a complex architecture supporting hundreds of different types of devices connecting from all over the world at all times. For various reasons at various times, load on these systems shifts significantly in pattern and magnitude, sometimes by multiple orders of magnitude in just a few minutes. When demand shifts, dozens of edge gateways, thousands of microservices, and tens of thousands of caches and databases have to weather the load shift while maintaining a high quality of service for our users.

In this talk, we will start with understanding how the four-region full-active architecture of Netflix's streaming control plane gives us the levers to shape and prioritize traffic. Techniques like balancing load and at key times unbalancing it or using partial or complete failover and shifting help us mitigate demand shifts.

Next, once load has entered one of our regions, we will see a combination of intelligent pre-scaling with automated service buffer management paired with reactive measures such as load shedding and rapid autoscaling to best bring available capacity supply to bear. For some types of demand shifts, we have to make hard tradeoffs between system stability and our ideal user experience, and choose to smartly degrade the service while maintaining the highest quality of experience we can. We will dive deep into these techniques with examples and tradeoffs.

Finally, we will touch on how the underlying data architecture makes all of this possible, and briefly what resilience techniques we use to keep our stateful systems available during load increases. For example, we will cover the use of data gateways with built-in resilience techniques, capacity planning, sharding, and thoughtful use of caching.


Joseph Lynch is a Principal Software Engineer for Netflix who focuses on building highly-reliable and high-leverage infrastructure across our stateless and stateful services. He led the shift of the Netflix data tier to abstraction, driving resilience through a Data Gateway architecture. He loves building distributed systems and learning the fun and exciting ways that they scale, operate, and break. Having wrangled many large scale distributed systems over the years, he currently spends much of his time building resilience features and automated capacity management into the Netflix fleet.

Connect: 
Website
Track 2
Hide details  ▾

Grand Ballroom GH
Live, Laugh, Log
Tuesday, 1:50 pm–2:35 pm PDT
Paige Cruz, Chronosphere

Available Media
Hide details  ▾  
Telemetry pipelines are the unsung heroes that shepherd data from applications and infrastructure to your observability and monitoring systems. It’s often up to SRE to ensure these pipelines are in tip-top shape, allowing logs to flow freely. However, a lot can go awry on the journey a log takes—from source issues and bad data formatting to misconfigured processing steps, congestion and under-provisioning. Buckle up as we dive into operating and monitoring Fluent Bit, helping you live, laugh, and log reliably.


Paige Cruz is passionate about cultivating sustainable on-call practices and bringing folks their aha moment with observability. Currently a Principal Developer Advocate at Chronosphere, she got her start as a software engineer at New Relic before switching to SRE holding the pager for InVision, Lightstep, and Weedmaps. Off-the-clock you can find her at the spinning wheel, swooning over alpacas, or watching trash TV on Bravo.

Connect: 
Bluesky
Mastodon
LinkedIn
Distributed Tracing in Action: Our Journey with OpenTelemetry
Tuesday, 2:40 pm–3:25 pm PDT
Chris Detsicas, Cisco ThousandEyes

Available Media
Hide details  ▾  
Join us as we dive into our journey with Distributed Tracing, leveraging OpenTelemetry and Istio in a dynamic microservices landscape. An internal Observability team embarked on a mission to empower engineers with deep application insights.

This talk encapsulates our journey, challenges encountered, and critical decisions made during the adoption of OpenTelemetry tracing. We'll discuss context propagation hurdles, the significance of automatic instrumentation, and importance of testing. Furthermore, we will provide an overview of our pipeline implementation and share key examples of how enabling our tracing solution has provided critical insights, helped us troubleshoot issues more effectively, and enhanced our understanding of application performance.


Chris Detsicas is a Lead SRE within the internal Observability team at ThousandEyes (part of Cisco) where he builds and maintains logging, metrics and tracing systems to empower ThousandEyes engineers with deep insights on their infrastructure and applications. He has 10+ years of experience working on developer platforms within both public and private clouds. In the last four years he has shifted focus to Observability and has recently delved deep into tracing to bring new capabilities to client teams.

Connect: 
LinkedIn
Discussion Track
Hide details  ▾

Magnolia Room
A Guided Introduction to SRE
Tuesday, 1:50 pm–3:25 pm PDT
Niall Murphy, Stanza, and Kurt Andersen, Clari

Format: AMA Session

Hide details  ▾  
Are you confused by the alphabet soup: PRRs, ICS, MTTR, o11y, SLOs, SLIs? Is SRE the same thing as DevOps? Will doing everything the SRE books say lead to success and a good night's sleep oncall?

This discussion session is the place to bring any and every question you may have about getting started as an SRE. Expect breadth rather than depth.


Niall is the CEO of Stanza Systems, has occupied various engineering and leadership roles in Microsoft, Google, and Amazon, and is the instigator of the best-selling & prize-winning Site Reliability Engineering, which he hopes at some stage to live down. His most recent book is Reliable Machine Learning, with Todd Underwood and many others.

Connect: 
X

By day, Kurt works as an infrastructure software architect at Clari. In addition, he serves on the USENIX Board and has had the pleasure to work with amazing people around the globe in the SREcon conferences. He also helps with the annual SRE survey and report that is graciously supported by Catchpoint.

3:25 pm–3:55 pm
Coffee and Tea Break
Grand Ballroom CDEF

3:55 pm–5:30 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Using Statistical Techniques to Automatically Detect Game-Breaking Issues
Tuesday, 3:55 pm–4:15 pm PDT
Ian Neidel, Netflix

Available Media
Hide details  ▾  
Content Delivery Network SREs are accustomed to metrics such as latency, bitrate, and dropped packets that measure how well we deliver content. However, as our team at Netflix expanded into ensuring good quality of experience for cloud gaming, a new challenge emerged: we must also be sure that what we deliver is fine as well. That is, we need to be able to automatically detect broken gameplay sessions and game breaking issues in a scalable way.

With a growing number of sessions and reams of logs per day, we turn to statistics and machine learning techniques to solve these otherwise difficult tasks at scale. In this talk we will cover the variety of metrics we use to infer brokenness, explain accessible methods to vectorize and cluster exception messages, and provide some insight into the statistics we use to find broken sessions, identify game breaking issues, and infer their impact with confidence.


Ian Neidel is a SRE for Open Connect, Netflix’s in-house CDN. He works on Quality of Experience for Cloud Games, improving resiliency and realtime observability for Live Streaming, and automatic diagnosis and remediation of issues across Netflix’s distributed fleet of servers using Temporal — to choose a few. He attempts to back everything he and his software does in data where possible. Ian previously worked for two NASA centers and Amazon while an undergraduate studying Computer Science and Global Affairs at Yale.

Connect: 
LinkedIn
Mapping a Better Future with STPA
Tuesday, 4:20 pm–4:40 pm PDT
Theo Klein, Google

Available Media
Hide details  ▾  
Want to prevent outages before they happen? Traditional SRE methods focus on component failures, but a whole class of outages stem from unexpected system interactions. We found a solution.

In our team, we use Systems Theoretic Process Analysis (STPA) to identify and fix system-level vulnerabilities before they cause outages. By applying STPA during the design phase, we've prevented major incidents and saved countless engineering hours.

This talk will show you how STPA can transform your approach to reliability. We'll share a real-world example where STPA caught critical design flaws that traditional methods missed, saving us months of costly rework.

Don't wait for outages to happen. Learn how STPA can help you build more resilient systems and become a 1000x engineer.


Theo Klein is a Senior Site Reliability Engineer working on Google Maps. Over the past year, he has lead an effort to improve the safety and reliability of road disruptions data on Google Maps. Previously, he lead efforts to remove unneeded dependencies on critical systems, which de-risked Google's many serving layers from global outages.

His primary interests are in systems thinking, dependency management and horizontal analyses of large-scale systems.

Is the S in SRE for “Security”?
Tuesday, 4:45 pm–5:30 pm PDT
John Benninghoff, Security Differently

Available Media
Hide details  ▾  
There is significant overlap between Cybersecurity and SRE; understanding and leveraging that can improve the performance of both. Lessons from safety science tell us that security and SRE come through being successful more often, not failing less. Research in DevOps, Software Security, and elsewhere shows a strong link between different types of organizational performance, including development, operations, SRE, and security; in many cases, organizations most effectively reduce cybersecurity risk by improving general technology performance.

Many SRE capabilities overlap with Security, including the critical activities of patching & managing attack surface, along with observability, incident response, postmortems, testing, and platform engineering. SRE and Security teams can collaborate by supporting their mutual goals, sharing their perspectives dealing with incidents both frequent and rare, and by setting Security Level Objectives to inform decisions on when to divert resources to security as SRE teams do with Service Level Objectives.


John Benninghoff is a long-time student and practitioner of managing information risk. His 25-year career in Cybersecurity and SRE includes diverse experience in financial services, retail, government, and health care. He founded Security Differently to advise organizations on how to integrate security into how work is done, quantify risk, improve performance, and make better decisions about risk. John holds a Masters Degree in Safety Science from Trinity College Dublin.

Connect: 
LinkedIn
Bluesky
Track 2
Hide details  ▾

Grand Ballroom GH
Lies Programmers Believe about Memory
Tuesday, 3:55 pm–4:40 pm PDT
Chris Down, Meta

Available Media
Hide details  ▾  
How does kernel memory management actually work? The Linux kernel provides a number of abstractions on top of physical memory, which, like most abstractions, can either be a blessing or a curse, especially when it comes to understanding application behavior. Some of these exist in conjunction with the hardware, like translation lookaside buffers, page tables, and the like, and some of them are Linux's own internal abstractions over memory, like different classes of memory within the operating system itself (with bonus special and often misunderstood properties).

Join Chris Down, a kernel engineer who works on the Linux memory management subsystem, as we go over things like the CPU's memory management internals, pages, the inner workings of virtual memory, and the complex tradeoffs made during modern memory management. Along the way, we will demystify the kernel and CPU behaviors around memory, go over how this might actually affect you as an SRE, and hopefully enable you to introspect and build more reliable systems as a result.


Chris Down is an engineer on Meta's Kernel team, based in London. He works on memory management within the kernel, especially cgroups, and is also a maintainer of the systemd project. Inside Meta, he is responsible for debugging and resolving major production issues, helping streamline engineering workflows, and improving the reliability and efficiency of Meta's systems at scale.

Connect: 
Website
“On-Call Is Ruining My Life” and Other Tales about Holding the Pager as an SRE
Tuesday, 4:45 pm–5:30 pm PDT
Cory Watson

Available Media
Hide details  ▾  
There’s no other part of SRE life that evokes such a strong reaction as being on-call. From the fear and anticipation of your first shift to the white-knuckle drama of a total system outage and the joy and satisfaction of debugging a particularly thorny issue - holding the pager is as much a human experience as a technical one. Let's talk about it!

We've done some surveys, pored over the literature, marinated in our experiences and have some findings. What models are in use? How do we feel about this work? What impact does it have? Can we do better? Will I get a pony? Ok, maybe not the last one.

I'll present some provocative findings that question the status quo around on-call and suggest some experiments you can take back and and test out. Maybe there will be a pony?


Cory Watson is an engineer and founder. Cory transitioned to a focus on reliability and observability as an early SRE at Twitter, founded the observability team at Stripe, and spent time at vendors SignalFx and Splunk. He is a strong voice in the observability community, through OSS, popular tweets, blog posts and speaking engagements.

Cory has over 20 years of software engineering experience, is an active founder / contributor of several successful Open Source projects. Before finding his passion in reliability, he worked in several industries such as e-commerce, consulting, healthcare, and fintech.

Discussion Track
Hide details  ▾

Magnolia Room
AMA with David Woods
Tuesday, 3:55 pm–5:30 pm PDT
David Woods, The Ohio State University

Format: AMA Session

Hide details  ▾  
Dr. David D. Woods is a cognitive psychologist and systems safety expert who has spent his career studying resilience in systems and how people and machines can best work together—topics deeply relevant to SRE. Dr Woods will host a wide-ranging discussion on how systems adapt in the face of disturbances, how complex systems break down, how the human perceptual system works with user interfaces, and more.


David is a pioneer of Resilience Engineering that looks at how people adapt to cope with complexity in dynamic risky human-cyber systems including accident investigations in critical digital services, critical care medicine, aviation, energy, disaster response, military operations, & space operations (advisor to the Columbia Space Shuttle Accident Investigation Board).

He has discovered the key ingredients that allow systems to build the potential for resilient performance and flourish despite complexity penalties that accompany growth (https://resiliencefoundations.github.io/video-1-introduction-pt-1-it's-all-about-viability.html). His books include Behind Human Error, Resilience Engineering (the 1st book in the field), Resilience Engineering in Practice, and Joint Cognitive Systems. He started the SNAFU Catchers Consortium, a software industry-university partnership, in 2015 to apply the new science to build resilience in critical digital services (see stella.report).

He is Past-President of the Resilience Engineering Association and Past-President of the Human Factors and Ergonomics Society.

5:30 pm–7:00 pm
Conference Reception at the Sponsor Showcase
Grand Ballroom CDEF

Sponsored by Cisco ThousandEyes

Wednesday, March 26
8:00 am–9:00 am
Continental Breakfast
Grand Ballroom CDEF

9:00 am–10:30 am
Hide details  ▾

Wednesday Plenary Session
Grand Ballroom ABGH
SRE & Complexification: Where Verbs and Nouns Do Battle
Wednesday, 9:00 am–9:45 am PDT
David Woods, The Ohio State University

Available Media
Hide details  ▾  
SRE is one proving ground on resilient performance in action (also known as SNAFU Catching). It is a critical contributor to the scientific foundations for Resilience Engineering.

A new round of growth & change is producing new complexity penalties—complexification. How will/can SRE cope as the lines of tension change? The skills & expertise to do SRE well are verb-centric—"resilience—as adaptive capacity—is a verb in the future tense." The human push for advantage from technology change is noun-centric.

SRE is one arena where the two framings conflict given the expanding the layers and tangles of interdependencies. SRE can adapt by innovating new verb-based means to see ahead in order to anticipate, to see around in order to synchronize, and to see anew to reframe models.


David is a pioneer of Resilience Engineering that looks at how people adapt to cope with complexity in dynamic risky human-cyber systems including accident investigations in critical digital services, critical care medicine, aviation, energy, disaster response, military operations, & space operations (advisor to the Columbia Space Shuttle Accident Investigation Board).

He has discovered the key ingredients that allow systems to build the potential for resilient performance and flourish despite complexity penalties that accompany growth (https://resiliencefoundations.github.io/video-1-introduction-pt-1-it's-all-about-viability.html). His books include Behind Human Error, Resilience Engineering (the 1st book in the field), Resilience Engineering in Practice, and Joint Cognitive Systems. He started the SNAFU Catchers Consortium, a software industry-university partnership, in 2015 to apply the new science to build resilience in critical digital services (see stella.report).

He is Past-President of the Resilience Engineering Association and Past-President of the Human Factors and Ergonomics Society.

The Perverse Incentives of Reliability
Wednesday, 9:45 am–10:30 am PDT
Katie Wilde, Snyk

Available Media
Hide details  ▾  
Are you trying to improve reliability in your company, but coming up against it not being valued unless you're in an active SEV1? Struggling to build a reliability culture in a wider organization? Relying on heroics to keep the lights on?

This talk is for you. The reality is that, for most of us, reliability work is not extrinsically rewarded: customers won't write in about the outage you didn't have, and investors aren't impressed that your site is still up. In today's "do less with more" world, increased pressure to deliver value (read: features) often comes at the expense of building resilient systems as we race to hit ever tighter deadlines. In the face of these perverse incentives, it's no wonder that having a reliability focus isn't the norm for so many engineering cultures. There is a better way: harnessing intrinsic motivation. This talk will cover approaches, tactics and lessons learned to overcome the perverse incentive problem, and how tapping into the inherent pride, joy and hilarity of incidents can transform reliability practices.


Katie Wilde is an experienced engineering leader, and currently Senior Director at Snyk, and previously, VP Engineering at Ambassador Labs and Buffer. In this talk, she shares the problem of perverse incentives that make it so hard to build a culture of reliability in engineering organizations, and approaches to overcome these challenges.

10:30 am–11:00 am
Coffee and Tea Break
Grand Ballroom CDEF

11:00 am–12:35 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Maturing Your Data Architecture in a Week: How Bluesky Survived
Wednesday, 11:00 am–11:45 am PDT
Jaz Volpert, Bluesky PBC

Available Media
Hide details  ▾  
In November of 2024, Bluesky saw a sudden surge in activity adding one million new users per day several days in a row, with daily active users increasing by 1,200% in a week. Through this exponential growth, Bluesky's backend team of ~6 engineers kept the site online and continued to onboard new users despite all of our core infrastructure running on our own physical infrastructure. In this talk, I'll walk you through the 11 days of hell (16+ hours a day) in which we rapidly matured our data architecture to support over 1M hourly active users producing 1,600+ events/sec.

Jaz is the Backend Go developer at Bluesky responsible for scalable data systems and physical infrastructure. From a global index of billions of records, to graph databases, to video platforms, Jaz has built a wide variety of large-scale systems used by tens of millions of users around the world running on cutting-edge hardware that pushes the Go runtime to its limits.

Connect: 
Bluesky
Inclusive SRE: Best Practices for Working with a Visually Impaired Incident Analyst or Responder
Wednesday, 11:50 am–12:35 pm PDT
Randall (Randy) Horwitz, IBM CIO

Available Media
Hide details  ▾  
Fortunately, Society is becoming more inclusive, enabling all of us to learn to work with people with differing abilities, like those who are visually impaired. We all want to be more inclusive, but how do we best collaborate with a visually impaired incident analyst or responder? What kinds of challenges do they have? How can they collaborate if they can’t see our dashboards?

Resolving difficult incidents always requires leveraging different perspectives, and people who think/hear/see differently can provide a game changing perspective.

Please join Randy Horwitz, visually impaired Senior Technical Staff Member, IBM CIO and former incident responder for a 35-minute presentation demonstrating how to bridge these gaps. Screen reader demos will be provided.


Randall (Randy) Horwitz currently works as a Senior Technical Staff Member for the CIO Technology Platforms Transformation I&T Operations organization.

Since 2016, when he worked as the support manager for the IBM Developer Experience, Mr. Horwitz has been passionate about development teams being able to respond to and learn from their incidents. For example, in 2017 he was instrumental in the Virtual Private Cloud UI team being the first in its organization to have a documented follow the sun incident response process.

Mr. Horwitz currently leads the Learning from Incidents and Problem Management programs for his CIO organization.

He graduated with a Bachelor’s of Science in Computer Science from the Rochester Institute of Technology in 1999 and has been with IBM ever since. One of his proudest accomplishments remains being a blind UI developer on the WebSphere Admin Console team, where he drove line items to make it 100% accessible to those with disabilities.

Connect: 
LinkedIn
Track 2
Hide details  ▾

Grand Ballroom GH
Learning from Incidents at Scale; Actually Doing Cross-Incident Analysis
Wednesday, 11:00 am–11:45 am PDT
Vanessa Huerta Granda, Enova

Available Media
Hide details  ▾  
For a few years we have discussed this idea of Learning from Incidents that encourages folks to deeply understand an incident through a thorough, in-depth investigation of how it came to be. I personally have led these investigations, written about them, and coached folks on them and while I stand by this process I have also seen how difficult it is to scale this process.

In this talk I will describe how my team (resiliency engineering) has been able to leverage our incident review program to learn from incidents at scale. How we’ve been able to analyze a universe of incidents broken out into quarters, years, products, and technologies and gain insights and make recommendations to improve our sociotechnical systems.


Vanessa is a Technology Manager for Resilience Engineering at Enova. Previously she worked at Jeli.io helping companies make the most of their incidents and has spent the last decade focusing on Production Incident processes, learning from incidents, and handling Major Incidents as Incident Commander. She has spoken and written on incident metrics, sharing learnings, and in 2021 co-authored Jeli’s Howie: The Post-Incident Guide. She is passionate about continuous improvement, getting teams to talk to each other, and sharing incident findings.

Running DRP Tabletop Exercises
Wednesday, 11:50 am–12:35 pm PDT
Josh Simon, University of Michigan

Available Media
Hide details  ▾  
A disaster recovery plan (DRP) documents policies and detailed procedures for recovering your organization's critical technology infrastructure, systems, and applications after a disaster. Hopefully you have DRPs for your organization, but how complete are they really, and how and how often do you test them?

In this talk, we'll help you get a better understanding of what a DRP is and contains, as well as why it's important to write, test, and maintain service-specific DRPs and affiliated documentation. We'll talk about how we're developing and using collaborative discussion-based thought experiments to test our DRPs, including things you should and shouldn't do when you write and test your own. You may even get some insights on how to design your own services for reliability and recovery!


Josh is a senior systems administrator with over 30 years of experience across industry and higher education. His areas of expertise include systems administration, project management, technical writing, and facilitation. Among his many roles and responsibilities is coordinating his team's disaster recovery planning process. He enjoys sharing his experiences... especially if it saves other people from problems in the future.

Connect: 
Bluesky
LinkedIn
X
Discussion Track
Hide details  ▾

Magnolia Room
What Do SRE ICs Do? How to Build SRE Skillsets
Wednesday, 11:00 am–12:35 pm PDT
Beth Adele Long, Adaptive Capacity Labs, and Fred Hebert, Honeycomb.io

Format: Breakout Group Discussion

Hide details  ▾  
The focus of this session is developing individual contributor skills in SRE. SREs do a lot of different things, including but not limited to: load testing, setting up and maintaining infrastructure services, building integration test pipelines, setting SLOs, maintaining alerts, being an incident commander, writing post incident reviews, system design for scalability, building automation, contributing code changes to core products which are aimed at increasing reliability or performance, and troubleshooting. Few engineers come to SRE with all of these skills. How, as practitioners, should we think about building skills in new areas? Does it make sense to be an SRE jack-of-all-trades, or should one specialize?


Beth Adele Long is a writer and engineer with wide experience building, maintaining, and repairing web systems (mostly repairing). She’s a founding member of the Resilience in Software Foundation and a Principal at Adaptive Capacity Labs.


Fred Hebert is a staff SRE at Honeycomb.io, caring for SLOs and error budgets, on-call health, alert hygiene, incident response, and operational readiness. He’s a published technical author who loves distributed systems, systems engineering and has a strong interest in resilience engineering and human factors.
Connect: 
Bluesky
Mastodon
12:35 pm–1:50 pm
Luncheon
Santa Clara Ballroom

Sponsored by Jane Street

1:50 pm–3:25 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Optimizing Machine Learning Training Infrastructure: A Governance Approach
Wednesday, 1:50 pm–2:35 pm PDT
Anamaya Sullerey and Brian Hansen, Meta

Available Media
Hide details  ▾  
We share how we have transformed the way Monetization at Meta approaches machine learning training infrastructure management to unleash Efficiency and unlock Innovation. As AI model sizes and deployment footprints continue to explode, inefficient resource allocation and utilization are no longer just a nuisance – they're a major roadblock to innovation.

We'll dive into the cutting-edge strategies and real-world examples of how to use governance to:

Drive ROI: Accurately measure and attribute the cost of ML training to focus on high ROI investments.
Unlock hidden capacity: Maximize your existing resources and reduce waste
Accelerate time-to-market: Streamline your ML development process and get to production faster
Through a case study of a successful ML training workload governance system, we'll explore the complexities of attributing costs in ML training to projects and share hard-won lessons from bridging the gap between research and production.


Anamaya Sullerey is a technical leader in the AdsML Production Engineering team, focused on capacity, efficiency, and reliability in the ML production environment. He has over two decades of broad experience across ML, software, compute and network systems, and silicon. Anamaya holds an MS in EE from Stanford University and a BTech in EE from IIT Kanpur.


Brian leads the AdsML Production Engineering teams for Meta, focused on scaling machine learning in production environments. He has been a successful serial entrepreneur for two decades taking multiple start-ups from early to late stage growth. Throughout his career Brian has been a leader building global teams leveraging infrastructure to improve business performance.

Beyond Sequential: A Recipe for Async Pipeline Observability and Alerting
Wednesday, 2:40 pm–3:25 pm PDT
Jash Mistry and Gabriela Medvetska, eBay Inc

Available Media
Hide details  ▾  
Navigating the complexities of microservices observability requires more than just traditional monitoring — especially for asynchronous systems. This session provides a comprehensive “recipe” to cooking up Service Level Objectives (SLOs) for asynchronous pipelines. Learn how to identify critical metrics, instrument your app using Prometheus, design meaningful dashboards, and define actionable alerts. Whether you're a junior site reliability sous-chef or a seasoned ops chef, you'll leave with a practical cookbook of strategies to enhance your async system's observability and monitor customer experience.


Jash Mistry is a Senior Software Engineer at eBay. As a member of the Site Reliability Engineering team, he played a crucial role in the evolution of monitoring—expanding on absolute error counts and average latencies to develop a highly reliable SLO-driven observability platform. He has a Master's Degree in Computer Engineering from Georgia Institute of Technology. Movie theatres are his second home, but he does not mind seeing one from the couch as long as it's on Mubi or the Criterion Channel.

Connect: 
LinkedIn

Gabriela Medvetska is a Software Engineer at eBay. As a member of the Site Reliability Engineering team, she worked on a variety of projects ranging from developing UIs for internal observability tooling to implementing machine learning algorithms to improve site resiliency during external vendor outages. She is a banana slug from Ukraine and has a Bachelor's Degree in Computer Science from the University of California, Santa Cruz. Being a typical Gemini, she has 50 billion hobbies, but she is most excited about a cyberpunk festival called Neotropolis coming up in April.

Connect: 
LinkedIn
Track 2
Hide details  ▾

Grand Ballroom GH
Handling the Largest Domains Migration, Ever!
Wednesday, 1:50 pm–2:35 pm PDT
Franklin Angulo and Divya Kamat, Squarespace

Available Media
Hide details  ▾  
Domains remain a critical part of web infrastructure, and an essential piece of the online presence of people and businesses. In 2023, Squarespace acquired the assets behind the Google Domains business, including more than 10 million domains. Learn about the challenges of executing a migration at a scale not seen before in the domain industry.


Franklin Angulo currently leads the product & engineering teams within the Squarespace Domains organization. Before this role, he shaped the technical vision at Squarespace as its Chief Architect, built teams to scale the backend engine and data centers that power the millions of websites on the Squarespace platform, managed the teams that iterated on the features used daily by millions of Lyft riders and drivers, and worked at Amazon on route planning optimizations, shipping rate shopping and capacity planning algorithms for global inbound logistics and the Amazon Locker product. Franklin also co-founded a technology company in Costa Rica building ERP-style software for municipal governments.

Connect: 
X

Divya Kamat is an accomplished engineering leader and currently heads the engineering teams within the Squarespace Domains organization. Since joining Squarespace in 2018 as an engineer, Divya has played a pivotal role in the growth and evolution of the Domains team. She was a key contributor to the development and launch of Squarespace Registrar in 2020 and has successfully scaled the Domains team from 8 engineers to a thriving 40-person organization. Before her tenure at Squarespace, Divya worked at Microsoft, where she built highly scalable microservices to enhance the resiliency and efficiency of Azure Stack, the company’s private and hybrid cloud solution. With deep expertise in engineering leadership, scalability, and domains, Divya brings a wealth of experience to every project she undertakes.

Connect: 
X
Taming the Beast: Understanding and Harnessing the Power of HTTP Proxies
Wednesday, 2:40 pm–3:25 pm PDT
Guillaume Quintard, Varnish Software

Available Media
Hide details  ▾  
Explore the often-overlooked power of HTTP and reverse-proxies in modern SRE and DevOps workflows.

Starting with a fresh perspective on HTTP—its simplicity and quirks—the session delves into how reverse-proxies enhance observability, performance, and resilience. Attendees will learn how proxies can serve as invaluable tools for debugging, traffic manipulation, and active mitigation during production incidents.

With a focus on actionable insights, the talk includes code snippets, real-world examples, and guidance on leveraging tools like OpenTelemetry to equip SREs with practical strategies to manage complex systems effectively.


Guillaume Quintard is a systems programming and performance optimization expert, bringing years of experience to the tech industry. A passionate contributor to open-source projects, Guillaume excels in crafting high-performance software solutions and advancing system architecture. Guillaume is known for his innovative approach to reliability and scalability, and his commitment to offering a fresh perspective on systems resilience and efficiency.

Connect: 
LinkedIn
Discussion Track
Hide details  ▾

Magnolia Room
SRE Team Practices
Wednesday, 1:50 pm–3:25 pm PDT
Colette Alexander, HashiCorp, and Sarah Butt, Salesforce

Format: Breakout Group Discussion

Hide details  ▾  
This session sets out to explore SRE at the level of the engineering team. Most engineering teams do some form of planning and goal setting—is this process different for SRE teams compared to other engineering teams? Do OKRs even make sense for SREs? How does your SRE team onboard new members?

There are several team practices specific to SRE, including (but not limited to) Production Readiness Reviews, regular production meetings, and wheel of misfortune exercises. What works and what doesn't? Why? What team-level practices are most important?


Colette has been working as an engineering leader in the software industry for 10+ years. Her obsession with learning from incidents and Resilience Engineering began while managing teams at Spotify. It eventually led her to pursue her Masters in Science at Lund University in Human Factors and Systems Safety. As the current Director of SRE and observability at HashiCorp she leads teams involved in improving the reliability of HashiCorp’s cloud product line. She also maintains an active composition and recording career as a rock cellist, and lives with her rescue dog, two kids and husband in Rhode Island.


Sarah is a Principal Engineer within Salesforce's Customer Centric Reliability Engineering group, where she helps lead Salesforce's Centralized Incident Response organization. She is fascinated by scale, complexity, systems thinking, and non-functional requirements— particularly those around reliability. You'll likely find her talking about topics such as resilience engineering, observability, and incident management and response. Prior to working at Salesforce, Sarah worked in both Dell and SentinelOne's SRE organizations. In her free time, Sarah enjoys freelancing as an audio engineer, competing as an equestrian, and spending time with her husband and their three labradors.

3:25 pm–3:55 pm
Coffee and Tea Break
Grand Ballroom CDEF

3:55 pm–5:30 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Chaos Experiments - Datacenter Stress Testing
Wednesday, 3:55 pm–4:40 pm PDT
Clayton Krueger, USAA

Available Media
Hide details  ▾  
In this session, we’ll explore how a financial services provider has developed a comprehensive, automated chaos engineering program, supported by strong leadership. While chaos testing is commonly done with individual applications, we’ve elevated the practice by applying it to an entire data center. This journey didn’t happen overnight, and we’ll take you through the key stages of our progress. We’ll discuss the major challenges we faced specifically around fear, uncertainty, and doubt. Attendees will gain insights into the tools and strategies we used to overcome obstacles and the lessons learned along the way. Additionally, we’ll share our plans for future efforts and how we aim to further enhance the robustness of our infrastructure. This session is perfect for anyone looking to deepen their understanding of large-scale chaos engineering in a complex environment.


Clayton Krueger is a trailblazing leader and founding member of the SRE team at USAA, where he has played a pivotal role in shaping the company’s infrastructure resiliency strategy. Clayton has been instrumental in designing and implementing USAA’s core metrics collection and storage frameworks that power the company’s SRE capabilities. Beyond infrastructure, he is driving transformative change in USAA’s problem and change management practices by spearheading automation initiatives that eliminate manual toil and enhance operational efficiency. Clayton is also committed to developing the next generation of elite technical troubleshooters, ensuring that USAA’s teams remain at the forefront of innovation and excellence.

Measuring Availability the Player Focused Way: How Riot Games Changed Its Availability Culture
Wednesday, 4:45 pm–5:30 pm PDT
Maxfield Stewart, Riot Games
Available Media
Hide details  ▾  
Riot Games started its journey to building out SRE culture in 2020. The number 1 problem we had to solve first was a unified language across all teams and games about what availability was. In other words, we had to define "uptime". This talk will walk through how we developed our availability measurements by simple modifications to our incident management process and aligned leadership and engineers on being held accountable to availability using our most popular core value, Player Focus.


Maxfield Stewart has been shipping software and supporting production environments for over 25 years. Having worked in private consulting for fortune 500 companies like Goldman Sachs and Sprint, to over a decade and a half in the game industry. For the last 12 years Max has been helping Riot transition to continuous delivery, micro-services and changing culture around production availability, RCA's, post-mortems and observability.

Track 2
Hide details  ▾

Grand Ballroom GH
Please Give Me Back My Network Cables! On Networking Limits in AWS
Wednesday, 3:55 pm–4:40 pm PDT
Steffen Gebert and Miklos Tirpak, emnify

Available Media
Hide details  ▾  
How much is “up to 10 Gbps” for an EC2 instance? And what happens, if packets are smaller or fragmented? Over the years of running our mobile core’s network functions on AWS, we learned – the hard way – about numerous network limits. Many of them are (in the meantime) documented, but some are not.

In this presentation, we share our horror stories on what kept us awake at night. To make you better informed, we will explain limits such as packets per second and connection tracking and how those will affect your network traffic, once they are exceeded. We share, how you can (sometimes) monitor your remaining quotas, or at least how you can identify the reason, why your applications go haywire.

Finally, we highlight a couple of cases, where your next incident could be just a side note in the documentation.


Before switching into his new role, Steffen used to lead the infrastructure team at emnify, a mobile virtual network operator (MVNO) running custom-built mobile core networks for the Internet of Things on Amazon Web Services. His technical main interest is misusing AWS networking features to build a network-centric product on top of AWS (yes, it sometimes hurts).

Before joining emnify in 2017, he was a researcher at the University of Würzburg and received his PhD for his thesis on software-based networks.

Connect: 
Mastodon

Miklos works with the Packet Gateway team at emnify as an engineering manager on developing high-performance applications for packet processing with cutting-edge technologies. While such network applications are running on Amazon Web Services, packet per second rate and high reliability have always been in focus. Before emnify, he worked as a software engineer in the telecommunication and networking domains, designed and developed a patented policy engine for the routers of various telco protocols.

OpenTelemetry Semantic Conventions and How to Avoid Broken Observability
Wednesday, 4:45 pm–5:30 pm PDT
Dinesh Gurumurthy, Datadog Inc., and Laurent Querel, F5

Available Media
Hide details  ▾  
The OpenTelemetry community has introduced Semantic Conventions - a defined schema that brings consistent meaning to telemetry data, defining everything from span names and metric instruments to attribute types and valid values. Semantic Conventions standardize naming across your codebase, libraries, and platforms, ensuring smooth data flow and better insights. With these benefits come drawbacks - namely that Semantic Conventions can and will change. Join us to learn how Datadog was impacted when changes to HTTP and Deployment Semantic Conventions caused disruptions for our clients. To fix these problems, Datadog came together with the community to develop the Schema Processor - a solution built to handle these changes without painful outages.


Dinesh Gurumurthy is a Staff Engineer at Datadog and the founding leader of the company’s OpenTelemetry team. Last year, Dinesh led the initiative to embed the OpenTelemetry collector with the Datadog Agent. He is also highly involved in the OpenTelemetry community, contributing to multiple projects. Before joining Datadog, Dinesh worked at a few startups, notably FuboTV.

Connect: 
LinkedIn

Laurent Querel is a Senior Director and Distinguished Engineer at F5, focusing on observability and data processing. He is an enthusiastic supporter of open source and currently co-maintains two projects within the OpenTelemetry community: OTEL Weaver, a tool for managing and controlling semantic convention registries, and OTEL Arrow, an alternative protocol to OTLP that can improve compression rates by 30% to 70%.

Connect: 
LinkedIn
Discussion Track
Hide details  ▾

Magnolia Room
Service Level Objectives
Wednesday, 3:55 pm–5:30 pm PDT
Alex Hidalgo, Nobl9, and Cail Young, Octopus Deploy

Format: AMA Session

Hide details  ▾  
Service Level Objectives are a core element of many organizations' SRE strategies. SLOs seem simple, but the way in which they are constructed and used has broad consequences for organizations, and for SRE teams' success. The session hosts will lead a discussion that gets into the nitty-gritty of implementing, maintaining, and living with SLOs and error budgets.


Alex Hidalgo is the Field CTO at Nobl9 and author of Implementing Service Level Objectives. During his career he has developed a deep love for sustainable operations, proper observability, and using SLO data to drive discussions and make decisions. Alex's previous jobs have included IT support, network security, restaurant work, t-shirt design, and hosting game shows at bars. When not sharing his passion for technology with others, you can find him scuba diving or watching Premier League football. He lives in Brooklyn with his partner Jen and a rescue dog named Taco. Alex has a BA in philosophy from Virginia Commonwealth University.


Cail has spent the last couple of decades working at the intersection of people and technology: in the performing arts, in the motion picture industry, and now in the field of software operations. He is fascinated by learning from incidents - large and small - and will gladly trade stories about them.

Connect: 
Bluesky
LinkedIn
5:45 pm–7:30 pm
Hide details  ▾

Lightning Talks
Grand Ballroom AB
How Doing First Response Helped Me Combat Burnout and Made Me A Better SRE
Lauren Caliolio, Grafana Labs
What Real Housewives Taught Me about Postmortems
Paige Cruz, Chronosphere
When Uptime Met Downtime: My Journey from Engineer to Executive"
Hamed Silatani, Uptime Labs
But Does It Have Four Nines ON THE BOX?
Clint Byrum, HashiCorp
The Emotional Side of an Incident Commander: Balancing Responsibility and Humanity
Kartheek Mahamkali, PayPal.Inc
Storytelling in Incidents
Will Gallego, Grafana Labs
For the AWS Bill is Dark and Full of Terrors
Corey Quinn, The Duckbill Group
Available Media
Thursday, March 27
8:00 am–9:00 am
Continental Breakfast
Grand Ballroom CDEF

9:00 am–10:35 am
Track 1
Hide details  ▾

Grand Ballroom AB
Stopping Performance Regression via Changepoint Detection
Thursday, 9:00 am–9:20 am PDT
Joseph Cirella and Shanthini Velan, Bloomberg

Available Media
Hide details  ▾  
Bloomberg's Ticker Plant infrastructure provides real-time market data to almost all internal and external clients; any increase in latency impacts much of the company's real-time products. This talk discusses how statistical changepoint detection is used to identify when our complex system's performance characteristics have significantly changed. We will discuss the challenges of deploying this, such as dealing with "expected" changepoints like market open/close and downtime, relaying the change information to engineers in an effective manner, and establishing a feedback loop.


Joseph Cirella is a Software Engineer at Bloomberg, where he works within the Ticker Plant SRE Capacity & Performance team.


Shanthini Velan leads the Ticker Plant SRE Capacity & Performance team at Bloomberg.

Per Aspera ad Productum: Turning Processes into Products
Thursday, 9:25 am–9:45 am PDT
Yuri Bernstein, Medallia

Available Media
Hide details  ▾  
How to increase your team throughput by applying product management principles to SRE tools.


Yuri is now working as Senior Staff SRE at Medallia. He brings 16 years of industry experience, building and managing global teams. Yuri’s current focus is SRE organization workflow efficiency and scalability. Yuri is a zealot of keeping things simple, yet powerful applying multidisciplinary design principles to the tools and processes he creates.

Incident Management Metrics That Matter
Thursday, 9:50 am–10:35 am PDT
Laura de Vesine and Jamie Luck, Datadog Inc

Available Media
Hide details  ▾  
Businesses run on metrics. They use them to judge success, identify areas for investment, and reward employees. Unfortunately, naive metrics can do more harm than good, especially in the context of low-frequency events like incidents. Management teams often reach for MTTR (mean time to recovery) or raw incident counts to judge the success of reliability and resilience programs, but these metrics generate spurious insights and perverse incentives. As SREs we can't simply tell the business not to measure them -- we need to offer alternatives. This talk explores a starting list of things to measure instead (and how to build your own list), as well as a framework to educate less technical people on what the actual value proposition of incident management is.


Laura de Vesine is a 20+ year software industry veteran. She has spent the last 9 years in SRE working in incident analysis and prevention, chaos engineering, and the intersection of technology and organizational culture, with a recent expansion into security. Laura is currently a senior staff engineer at Datadog, Inc. She also has a PhD in computer science, but mostly her cats nap on her diploma.


Jamie is a Senior SRE working in Incident Management at Datadog. Ever since they broke their first laptop and learned about this free operating system called Linux, it was all over. They have been working in the resilience and reliability space for ten years, operating everything from bare metal SPARC machines to fleets of containers. Passionate about sustainable computing, they focus their free time on repairing old machines and putting them back in service. In their current role, they define incident management and oncall practices for a mature engineering organization to complete the cycle of resilience from breakage to systemic improvement.

Track 2
Hide details  ▾

Grand Ballroom GH
Fully Automated HW SKU Selection System to Optimize Apache Pinot’s Cost-to-Serve at LinkedIn
Thursday, 9:00 am–9:45 am PDT
Jia Guo, LinkedIn, Yifan (Sabrina) Zhao, Netflix, and Dino Occhialini, LinkedIn

Available Media
Hide details  ▾  
Join us for this session to learn more about how cost-to-serve was optimized by nearly 50% for Apache Pinot OLAP Database's production fleet of ~14K machines at LinkedIn.

The nature of OLAP workloads running in LinkedIn on Pinot have diverse characteristics in terms of:

Varying workload demand (SLOs as low as P99 query latency < 100ms at 100K read QPS).
Varying cost / resource usage (CPU, memory, IO) of SQL queries.
Varying dataset sizes (clusters serving data from as low as 500GB to as high as 2PB).
The talk will go into details of the core cost optimization algorithm that considers varying factors to recommend an optimal SKU.

Multiple SKU Profiles
Low-overhead mechanisms to collect high cardinality profiling data from production clusters
Resource constraints (CPU, Memory, Disk IOPS, Throughout etc)
The system has been built with the goal of supporting "Multiple SKUs" effectively -- both in terms of cost optimization and keeping operational overhead minimum (fully automated). Through our talk, we will go into the details of all the infrastructure pieces we have built to deliver the solution in a generic fashion.

We will further discuss how this has been integrated this into our day-to-day operational machinery.


Jia is a Senior Software Engineer at LinkedIn, a committer for Apache Pinot. Jia focuses on making Pinot Fault-Tolerant and cost-effective. He has contributed across different areas of Pinot ranging from OLAP engine, indexing, fault tolerant shard placement to several performance improvements.

Connect: 
LinkedIn

Sabrina is a Software Engineer at Netflix, focusing on relational datastores. Previously, she worked on OLAP system Pinot at LinkedIn and was a contributor for Apache Pinot where she had contributed features like SQL Pagination, availability improvements for massive multi-tenant clusters, OLAP SQL enhancements and fault-tolerant shard placement.

Connect: 
LinkedIn

Dino is a Staff Software Engineer at LinkedIn and a contributor to Apache Pinot. Dino has been a strong SRE Leader for the Pinot team at LinkedIn. Dino has made many noteworthy contributions towards improving Pinot's operational excellence, resiliency, Site-Up, provisioning and usability posture. Dino has also contributed heavily towards making Pinot more reliable and performant.

Connect: 
LinkedIn
Production Engineering When Trading Billions of Dollars a Day
Thursday, 9:50 am–10:35 am PDT
Pedro Flemming, Jane Street

Available Media
Hide details  ▾  
How do you build reliable, maintainable and performant systems that trade billions of dollars every day in financial markets across the globe?

When your software has near-unlimited access to your bank account, every single message counts. When nanoseconds can determine whether or not you make or lose money, the physical location of your server within the data center matters. Speedy alerting and incident response have a direct and measurable impact on the PnL.

This talk will lift the lid on the beating heart of a major trading firm, and offer insights into the day-to-day operations, with a touch of “when things go wrong”.


Pedro has been a Software Engineer at Jane Street for over 7 years. He has worked on systems that directly facilitate trading of financial instruments of various shapes over his entire time there. He has spent extensive time monitoring these systems live, reacting to incidents, and improving their reliability all the while expanding the business capabilities of the systems.

Connect: 
LinkedIn
GitHub
Discussion Track
Hide details  ▾

Magnolia Room
Tech Debt
Thursday, 9:00 am–10:35 am PDT
Yvonne Lam and Mike Rembetsy, Bloomberg

Format: Breakout Group Discussion

Hide details  ▾  
Technical debt—decisions made to deliver in the short term with costs in the longer term—has not traditionally been seen as an SRE concern, but it should be. SRE teams with responsibility for production services generally need to contend with technical debt in the software they create (monitoring, automation, and so on) as well as being on the sharp end of many of the consequences of technical debt in the services they run. What are your experiences of technical debt as an SRE? How have you managed to cope with or to reduce technical debt?


Yvonne plays with code, systems, books, cats, food, yarn, dirt, and boats—not all at the same time. She works on devtools, release engineering, quality, and reliability.

Connect: 
Bluesky
Mastodon
X

Michael Rembetsy is the Global Head of Network Engineering and Operations at Bloomberg. His teams are responsible for everything from the physical hardware to SRE’s who focus on the global connectivity for customers. Prior to Bloomberg, Michael was the VP of Infrastructure at Etsy.

10:35 am–11:05 am
Coffee and Tea Break
Grand Ballroom CDEF

11:05 am–12:40 pm
Track 1
Hide details  ▾

Grand Ballroom AB
Systems Thinking with Poisoned Systems
Thursday, 11:05 am–11:50 am PDT
Hazel Weakly, Nivenly Foundation; Sandeep Kanabar, Gen

Available Media
Hide details  ▾  
AI is often said to be a "garbage in, garbage out" solution. So what happens when you take a carefully tuned system and try to operate it with AI?

Chaos! Bedlam! Or maybe... not?

AI assistance has some studied drawbacks: data poisoning, bias, inaccessibility, de-skilling, and more. We could very well end up in a world that is run by inaccessible and inscrutable black box AI systems. But! The situation isn't hopeless!

AI seems to be here to stay, but the drawbacks don't have to be. Join Hazel and Sandeep as we take you on a journey through our personal experiences with biased and broken systems, how we've worked around them, and strategies we have for addressing these issues as well as preventing future ones. Together, we'll discover how to transform AI into a transparent and reliable tool that helps enable innovation rather than chaos.


Hazel spends her days working on building out teams of humans as well as the infrastructure, systems, automation, and tooling to make life better for others. She’s worked at a variety of companies, across a wide range of tech, and knows that the hardest problems to solve are the social ones. Hazel currently serves as a Director on the board of the Haskell Foundation, as a Fellow of the Nivenly Foundation, and is fondly known as the Infrastructure Witch of Hachyderm (a popular Mastodon instance). One of her favorite things is watching someone light up when they understand something for the first time, and a life goal of hers is to help as many people as possible experience that joy. She also loves shooting pool and going swing dancing, both as a leader and a follower.

Connect: 
Mastodon
LinkedIn
Bluesky

Hailing from India, Sandeep is a passionate software engineer working at Gen (formerly NortonLifeLock). A frequent meetup speaker, Sandeep enjoys sharing his lessons learned from 15+ years in the tech space with the community. He's a staunch advocate for diversity and inclusion and an active member of a tech-focused Deaf and Hard of Hearing Working Group. Despite facing sensorineural hearing loss since age 14, Sandeep successfully navigates the tech world, relying on lip-reading and captioning.

Connect: 
LinkedIn
X
No Time to Do It All! Approaching Overload on DevOps Teams
Thursday, 11:55 am–12:40 pm PDT
Alex Wise

Available Media
Hide details  ▾  
There's always more work to be done. Alex will take a look at signs of overload in your organization, how to identify them, and strategies for managing it. He'll cover concepts including Overload in Joint Cognitive Systems, WIP Spirals, the Utilization Trap, and how they can be applied to your organization.


Alex is a site reliability engineer who loves safety-critical systems and attacking problems that attack back. He is best known for his work with the Software Freedom School helping those new to tech understand how to use and why to choose open source software. He worked as a software engineer for Verica helping companies tackle the thorny resilience issues in their tech stack.

Connect: 
X
Bluesky
Track 2
Hide details  ▾

Grand Ballroom GH
Securing Distributed Cache: Achieving Secure-by-Default with Key Challenges & Insights
Thursday, 11:05 am–11:50 am PDT
Akashdeep Goel, Sriram Rangarajan, and Samuel Fu, Netflix Inc

Available Media
Hide details  ▾  
In this session, we'll discuss a distributed caching system used at Netflix in multiple regions on a public cloud, handling 400 million requests per second and managing 14 petabytes of data. We'll focus on the intricacies of securing this system, including certificate lifecycle management, spurious policy lookup calls, and securing proxy calls for polyglot clients. We will walk you through our debugging journey with tools like CPU profiling and memory dumps, share key takeaways, and demonstrate how these techniques can be applied in any organization. This session will provide valuable lessons on retrofitting high-leverage systems for security compliance and executing global-scale rollouts effectively.


Akashdeep Goel is a Senior Software Engineer at Netflix working on distributed systems handling large scale caching deployments for both streaming and gaming workloads across Netflix. Prior to this, Akashdeep was working on a distributed control plane at Azure CosmosDB (Microsoft) delivering standby and failover infrastructure. Outside of work, he enjoys road trips, playing snooker and exploring different cuisines.


Sriram Rangarajan is a Senior Software Engineer at Netflix, focusing on caching infrastructure. Previously, he worked on ad servers and search functionalities at Unity Technologies and Kamcord, and managed backend solutions at Yahoo and Hewlett Packard. Sriram holds a Master's degree in Computer Science from New York University.


Samuel Fu is a Software Engineer at Netflix working on distributed systems that help enable caching at scale, supporting both VOD and live streaming use cases. Prior to Netflix, Samuel worked on realtime streaming feature pipelines at Lyft, enabling features such as driver bonuses and ETA prediction. Outside of work, he likes to exercise (swimming, tennis), and practice music (cello and piano).

Cattle vs. Pets - A Cost-Effective Elasticsearch Architecture to Scale-Out Beyond Petabytes
Thursday, 11:55 am–12:40 pm PDT
Leonardo Antônio dos Santos, Workday, Inc.

Available Media
Hide details  ▾  
Managing Elasticsearch at tens of petabyte scale requires innovative approaches to overcome the limits of traditional single-cluster designs. In this talk, we introduce a scalable, cost-effective multi-cluster architecture that handles trillions of indexed logs monthly while reducing operational complexity. By shifting to a "Cluster of Clusters" design, we optimize ingestion, search, and cross-cluster search traffic using a centralized management cluster and standardized data clusters.

Key highlights include leveraging a custom cluster health service based on the USE Method for intelligent query routing, implementing real-time auditing for problematic query detection, and automating rate-limiting for high-demand users. Attendees will learn how these strategies cut compute costs by 57%, achieved significant storage savings, and enhanced scalability and migration efficiency.

This session provides practical insights, benchmarks, and real-world examples to help organizations sustainably optimize Elasticsearch while maintaining performance and reducing costs — which is ideal for those overseeing large-scale log data or anticipating Elasticsearch growth.


Leonardo Dos Santos is a Senior Distributed Systems Engineer at Workday, specialized in building, maintaining and scaling large distributed systems. With extensive experience managing systems spanning petabytes and thousands of nodes, Leonardo has led large-scale architecture transformations that have optimized performance at large scale and significantly reduced costs. His work at Workday also includes designing globally distributed CI/CD pipelines and creating customized, eventual-consistent solutions for critical infrastructure. Previously, Leonardo held engineering roles at Amazon, where he led innovative and global projects to enhance AWS Network Active Monitoring. He is an active mentor, interviewer and automation advocate.

Connect: 
LinkedIn
Discussion Track
Hide details  ▾

Magnolia Room
Observability
Thursday, 11:05 am–12:40 pm PDT
Daria Barteneva, Microsoft Azure

Format: Breakout Group Discussion

Hide details  ▾  
This discussion will cover all forms of observability (logs, metrics, distributed traces). How should we think about the goals of observability programs and how do we know if we are achieving good outcomes?


Daria is a Principal Site Reliability Engineer in Observability Engineering in Azure. With a background in Applied Mathematics, Artificial Intelligence, and Music, Daria is passionate about machine learning, diversity in tech, and opera. In her current role, Daria is focused on changing organisational culture, processes, and platforms to improve service reliability and on-call experience. She has spoken at conferences on various aspects of reliability and human factors that play a key role in engineering practices, and has written for O'Reilly. Daria is originally from Moscow, Russia, having spent 20 years in Portugal, 10 years in Ireland, and now lives in the Pacific NorthWest.

12:40 pm–1:55 pm
Luncheon
Santa Clara Ballroom

1:55 pm–3:30 pm
Track 1
Hide details  ▾

Grand Ballroom AB
One Million Builds per Year, Only One Page - Operating Internal Services Without Heroics
Thursday, 1:55 pm–2:15 pm PDT
Cail Young, Octopus Deploy

Available Media
Hide details  ▾  
A nuts-and-bolts examination of how a small team at Octopus Deploy was able to deliver a set of internal services that enabled in excess of 1 million builds in a calendar year - with only one out-of-hours page in that time! We'll cover the technical and social aspects of what was involved, and discuss some of the downsides of having what appears to be a stable system.


Cail has spent the last couple of decades working at the intersection of people and technology: in the performing arts, in the motion picture industry, and now in the field of software operations. He is fascinated by learning from incidents - large and small - and will gladly trade stories about them.

Connect: 
Bluesky
LinkedIn
Going Multi Cloud in a Hurry with Quality and Style
Thursday, 2:20 pm–2:40 pm PDT
Geoff Oakham, ecobee

Available Media
Hide details  ▾  
How would you extend a Kubernetes based platform to support a second cloud provider? What if no one on your team knew the second platform well? Join Geoff as he talks about the soft skills and techniques he tried while delivering the product on time, met compliance standards, and trained up his co-workers.


Geoff is a Staff SRE at ecobee. In his spare time he builds fun things his wife and 8yo find on social, and fixes up a century home. He was recently given a 3d printer and discovered he has enough spare time to spend fixing that too!

Connect: 
LinkedIn
Mitigating Against Large Scale Systemic Failures in E-Trading
Thursday, 2:45 pm–3:05 pm PDT
Chris Hawley, Morgan Stanley

Available Media
Hide details  ▾  
Electronic trading systems are inherently complex and operate within narrow, high-stakes time windows, making their availability critical. Despite employing various resiliency patterns, these systems remain vulnerable to tail risks that could lead to widespread failures with significant consequences.

This presentation will explore real-world examples to uncover the nature of these risks, examine the limitations of common resiliency strategies, and discuss alternative approaches to enhance system robustness and reliability.


Chris Hawley is an Executive Director at Morgan Stanley in Institutional Securities Technology. He is a technical lead in the Listed Sales & Trading department.

Chris is a product owner within Site Reliability Engineering for the firm's global order management and electronic trading technology, supporting the Institutional Equity Division and has worked at various levels building these systems. He joined the firm in 2007 after earning an MEng in Computer Systems Engineering from the University of Warwick.

Chris lives in London with his wife, and spends his spare time exploring the world through his camera and, depending on the weather, running and skiing.

Hijacking Service Discovery to Simulate Dependency Degradation
Thursday, 3:10 pm–3:30 pm PDT
Abdulrahman Alhamali, Shopify

Available Media
Hide details  ▾  
Services have dependencies, and dependencies degrade: they can slow down, limit the bandwidth, or go entirely offline. Service should have mechanisms to deal with that: circuit breaking, bulkheading, and graceful degradation are some of the mechanisms developers might want to implement. But how can they confirm that these mechanisms work without waiting for an incident to happen? Simulation!

There are a few solutions for simulating dependency degradation, but a majority of them require traffic to be forwarded through a proxy. In this talk, we present a few ways to streamline this traffic forwarding, by hijacking service discovery.


Abdulrahman (Abed) has been a staff site reliability engineer in Shopify for three years. During this time, he has worked on a variety of resiliency solutions for the core product, and created innovative resiliency testing tools. He has also championed scale testing, resiliency education, and large scale gamedays. Before SRE, Abed had worked in Observability, DevOps, and Web Development.

Connect: 
LinkedIn
Track 2
Hide details  ▾

Grand Ballroom GH
Network Flow Data in the Cloud
Thursday, 1:55 pm–2:15 pm PDT
Steve Dodd, Slack

Available Media
Hide details  ▾  
Everything old is new again. Or rather, everything you thought was old is as relevant to today’s distributed service-oriented architecture as it was in the days of manual OSPF metric tuning. Traditional network engineering techniques are based on discrete math – namely, graph theory. A network graph provides a visual and quantitative foundation for analyzing network behaviors to optimize data flow, routing, and resilience in complex topologies. Huge benefits await those able to apply these lost arts to large-scale cloud infrastructure. In this talk, we’ll review those traditional methods, then apply them. We’ll explore how to build network traffic attribution on a per-service level — all without spending piles of money on vendor logging solutions.


Steve is a Staff Software Engineer for the Demand Engineering team at Slack based in Hailey, Idaho. The Demand Engineering team enables fast and reliable delivery of Slack to our 12M+ globally distributed daily active users.

Outside of work Steve enjoys rock climbing, skiing, and tinkering with his van.

OLTP SQL Database Query Tracing and Linting
Thursday, 2:20 pm–2:40 pm PDT
Xiaotong Jiang, Databricks

Available Media
Hide details  ▾  
The proposed talk suggested a way how we can annotate the query and trace a query from client side to the database server side. In addition, we can effectively aggregate the database server usage from different client side dimensions, like RPC, tenants, etc. This has been proven to be effective in handling client initiated incidents. On top of this, the query tracing system can be used to analyze the query behavior in the system to facilitate the large scale data migration operations.


Xiaotong is a software engineer at Databricks and has been working in Databricks's OLTP systems, focused on data migration system.

“How’s the App Doing?” Bringing Mobile Into Your Reliability Picture
Thursday, 2:45 pm–3:05 pm PDT
Hanson Ho and David Rifkin, Embrace

Available Media
Hide details  ▾  
Do you include telemetry from mobile apps when assessing the health and performance of your application? If not, do you know what you might be missing?

Like when users can’t connect to your servers because their network connection is poor, or something failed on the device before a request could be sent to complete an order? And what about everything in the app before creation of a network request – context that's hard or impossible to derive from the request itself – and can explain WHY requests are so slow, but only in Japan?

How are you thinking about the telemetry that comes from your mobile app? Learning to make sense of the gaps, and work around them, is the best path to reliable mobile applications. We’ll discuss how user experience is the best anchoring mechanism for mobile observability, and how reliability ultimately is in the eyes of the app-holder.


Hanson Ho's niche is mobile observability and performance, an odd passion he developed while working at Twitter as Android Performance Tech Lead. He is now at Embrace, hoping to bring true observability 2.0 to mobile apps everywhere, one device at a time.

Connect: 
Bluesky

David Rifkin is a developer relations engineer at Embrace, a mobile developer by trade, always an educator at heart. He has built iOS applications in a variety of settings and team sizes. OpenTelemetry components have become his new Legos.

Connect: 
Bluesky
From HAR to OpenTelemetry Trace: Redefining Browser Observability
Thursday, 3:10 pm–3:30 pm PDT
Antonio Jimenez, Cisco ThousandEyes

Available Media
Hide details  ▾  
Have you heard about HTTP Archive (HAR) files and wondered how you could leverage this data for deeper insights into your web applications?

Imagine analyzing your page load request data as OpenTelemetry traces in your favorite observability backend. In this talk, we will explore the lessons learned from transforming HAR into an OpenTelemetry trace and streaming it to Jaeger.

You'll gain insights into the process of converting HAR data into spans following OpenTelemetry semantic conventions and learn about the architecture we used to send these traces to any observability backend via the OpenTelemetry collector.


Antonio is a Tech Lead Software Engineer at Cisco ThousandEyes, specializing in observability to ensure our customers can effectively monitor their products. His recent work involves using OpenTelemetry to stream telemetry data, enhancing network visibility and performance for our clients.

He actively participates in the tech community, frequently attending conferences and meet-ups to share knowledge and stay abreast of industry trends.

Connect: 
LinkedIn
Discussion Track
Hide details  ▾

Magnolia Room
Open Unconference on SRE
Thursday, 1:55 pm–3:30 pm PDT
Blake Bisset and Robert Barron, IBM

Format: Unconference Session

Hide details  ▾  
If you were disappointed to not see a particular topic on the discussion track agenda then this is the session for you.

Come to this session—which will be run using the Open Spaces Technology unconference format—and propose your topic. The four topic areas with the most interest will be selected for discussion in breakout groups.

Blake Bisset got his first legal tech job at 16, long enough ago that he’s entitled to make shakeyfists while shouting, "Get off my LAN!" He’s contributed to 4 major tech books, 4 cool tech start-ups, and 4 “big tech” companies (not at all in that order), but has been a regular member on the program committee for only 3 major tech conferences, which–now that he’s written it down–suddenly bothers him enough that he might actually be a mild arithmomaniac, or perhaps just an undiagnosed sparkling vampire.


Robert Barron is an SRE Architect in the office of the IBM CIO where he enjoys helping others solve problems even more than he enjoys solving them himself. Robert has over 20 years of experience in all kinds of things ending in *-ops and *-ility and is still happiest when learning something new. He lives in Israel with his wonderful wife and two children. His hobbies include history, astronomy and space exploration, and bird photography.

3:30 pm–4:00 pm
Coffee and Tea Break
Grand Ballroom CDEF

4:00 pm–5:30 pm
Hide details  ▾

Closing Plenary Session
Grand Ballroom ABGH
Technical Debt as Theory Building and Practice
Thursday, 4:00 pm–4:45 pm PDT
Yvonne Z. Lam

Available Media
Hide details  ▾  
I will examine the connections between technical debt, housework/carework, and infrastructure in order to talk through strategies for understanding the shape of your technical debt, picking pieces to pay down, and building narratives with conceptual integrity around technical debt.


Yvonne plays with code, systems, books, cats, food, yarn, dirt, and boats—not all at the same time. She works on devtools, release engineering, quality, and reliability.

Connect: 
Bluesky
Mastodon
X
AIOps: Prove It! An Open Letter to Vendors Selling AI for SREs
Thursday, 4:45 pm–5:30 pm PDT
Charity Majors and Fred Hebert, Honeycomb.io

Available Media
Hide details  ▾  
SREs are not known for being eager, optimistic early adopters of shiny new technologies. We are much more likely to subject you to lengthy monologuing about all of the ways said technologies are overhyped, under-delivered, and prone to spectacular, catastrophic systems failures. Which brings us to the topic of AI.

It’s easy to be cynical when there’s this much hype and easy money flying around, but generative AI is not a fad; it’s here to stay. Which means that even operators and cynics — no, especially operators and cynics — need to get off the sidelines and engage with it. How should responsible, forward-looking SREs evaluate the truth claims being made in the market without being reflexively antagonistic? How can we help our orgs steer into change, leveraging AI technologies to help our teams ship better software, faster? And for the vendors out there using AI to try and help solve traditional SRE domain problems, how should they demonstrate that they are engaging with these problems in good faith, that they are more than just hype and snake oil?


Charity Majors is the co-founder and CTO of honeycomb.io. She pioneered the concept of modern Observability, drawing on her years of experience building and managing massive distributed systems at Parse (acquired by Facebook), Facebook, and Linden Lab building Second Life. She is the co-author of Observability Engineering and Database Reliability Engineering (O'Reilly). She loves free speech, free software and single malt scotch.

Connect: 
Bluesky

Fred Hebert is a staff SRE at Honeycomb.io, caring for SLOs and error budgets, on-call health, alert hygiene, incident response, and operational readiness. He’s a published technical author who loves distributed systems, systems engineering and has a strong interest in resilience engineering and human factors.
Connect: 
Bluesky
Mastodon
5:30 pm–5:35 pm
Closing Remarks
Grand Ballroom ABGH
