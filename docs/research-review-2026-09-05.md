# AI workflow and design source review

Reviewed September 5, 2026. These selected public sources informed Work Router 1.4.0
and UI Router 1.5.0. This is a targeted review, not a comprehensive survey or a model
benchmark. Source dates matter; adoption is a routing judgment unless explicitly
described as an observed test.

## Changes and deliberate non-changes

| Source | Assessment | Result |
|---|---|---|
| [Matt Shumer: Manager Loop, September 3, 2026](https://x.com/mattshumer_/status/2095723177389232540) and [follow-up, September 4](https://x.com/mattshumer_/status/2095724719408386326) | **Conditional.** Phase boundaries and acceptance checks address a plausible long-task failure. The agent count and wording preference are anecdotal; the follow-up explicitly labels its suggestions untested. | Work Router adds bounded phases and stall diagnosis. No mandatory manager, 96-agent configuration, automatic goals, checkbox velocity target or routine context reset. |
| [Pablo Stanley: scoped delegation, July 7, 2026](https://x.com/pablostanley/status/2074704410211467294) | **Already covered, with a refinement.** Clear assignments and parent review are useful; the particular family mapping is not a benchmark. | Preserve the current host-aware routes; explicitly reuse a progressing implementer for related fixes. |
| [Pietro Schirano: agent-written goals, June 14, 2026](https://x.com/skirano/status/2066225908202053818) | **Conditional.** Drafting acceptance criteria can reduce user effort. A self-authored goal can also expand scope. The post text was reviewed; its embedded demonstration was not fully evaluated. | Keep the user's outcome and host authorization requirements. Reading this advice does not create a goal or new task. |
| [CJ Zafir: context-saving recipe, May 8, 2026](https://x.com/cjzafir/status/2052801300627435996) | **Mostly already covered; reject the universal recipe.** Bounded context and orderly files are useful. The claimed savings, unexplained setting, universal task lists and fixed model/service recipe are not established by the post. | Keep short relevant handoffs, existing file structure and proportionate planning. No configuration change or promise of percentage savings. |
| [Dan McAteer: Luna Max orchestration, August 1, 2026](https://x.com/daniel_mac8/status/2083607027813662810) | **Historical routing lead.** A cost-oriented example with different models and roles does not establish the fastest route for this host. | Retain Luna's bounded economy role and current Astra-aware policy. Do not assign complex implementation to Terra or choose max globally from this example. |
| [Arena frontend ranking, July 16, 2026](https://x.com/arena/status/2077824029126504525), [Perplexity WANDR announcement, September 3](https://x.com/perplexity_ai/status/2095620419906830788), and [Meng's Fable impressions, September 2](https://x.com/MengTo/status/2095104073590808644) | **Reference only.** These are different tasks and kinds of evidence. A ranking or a creator's demonstration does not settle implementation correctness, accessibility or full-task latency. | No global model switch. Recheck current availability and comparable evidence if a model-selection task calls for it. |
| [George's design-skill list, May 23, 2026](https://x.com/nurijanian/status/2058231994329497922) → [Jamie Mill's Layers](https://layers.jamiemill.com/) | **Adopt a scoped diagnostic.** The upstream intro and orientation skills distinguish product decisions from surface treatment and discourage unnecessary artifacts. Remaining pack instructions were not fully reviewed. | UI Router adds product-decision diagnosis for broad or unexplained problems. Existing design leads remain; no nine-skill bulk installation or mandatory workshop. |
| [Meng: animation and typography vocabulary, May 6, 2025](https://x.com/MengTo/status/1919769539409224122) | **Durable method, already covered.** Naming visual traits is useful despite the older tool links. | Retain reference extraction, explicit motion states and viewport comparison. The old tutorial links do not establish current pricing or require a subscription. |
| [Meng's resource list, August 12, 2026](https://x.com/MengTo/status/2087494338909741113), [ThreeUI Community](https://github.com/MengTo/threeui), and [Abraham John's list, August 30](https://x.com/Abmankendrick/status/2093990028011556918) | **Adopt as resources.** Sources serve different jobs; public viewing, free code and paid MCP access must remain distinct. | UI Router's resource map selects references, fonts, components and creative-editor tools by need, with attribution and license boundaries. |
| [HeyGen: HyperFrames, April 27, 2026](https://x.com/HeyGen/status/2048882211022311614) → [current upstream](https://github.com/heygen-com/hyperframes) | **Conditional resource.** The official repository and Apache 2.0 license support a free local HTML-to-video route. The entire skill pack and a local render were not evaluated. | Add a video option to UI Router. Review selected skills at installation; separate preview from export checks and local rendering from paid services. |
| [Awesome Design MD promotion, April 4, 2026](https://x.com/heynavtoor/status/2040339518822432893) | **Defer code reuse.** A third-party reconstruction is not an official brand system. Upstream fidelity and asset rights were not established in this review. | Retain as a lead; prefer direct references and extraction. No automatic brand pack installation. |
| [Perplexity skills-manual announcement, May 8, 2026](https://x.com/perplexity_ai/status/2052786858774630665) | **Defer.** The announcement was readable, but browser policy blocked the linked article. | No claims about the full manual or changes attributed to it. |
| [YC's QM announcement, July 31, 2026](https://x.com/ycombinator/status/2083243960684908768), [anticipated Claude workflows, May 24](https://x.com/DanielMiessler/status/2058699741140222055), and [the 2025 coding-tool survey](https://x.com/johnrush/status/1928096496987066604) | **Discovery only.** Product announcements and old tool surveys are insufficient evidence for a new harness or integration. | No harness replacement, background service or broader permissions. Revisit only for a concrete missing capability and verify its current upstream. |

## Supporting evidence

[Anthropic's November 2025 long-task harness report](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
supports incremental work, durable state and end-to-end checks in its tested setting.
It explicitly leaves the best multi-agent arrangement unresolved. The
[December 2024 agent-pattern guide](https://www.anthropic.com/engineering/building-effective-agents)
supports starting simply and adding orchestration for a concrete benefit; its model
examples are historical. Neither is a benchmark of these router changes.

See [skill maintenance](skill-maintenance.md) for the adoption and release process,
[long-task guidance](../plugins/work-router/skills/route-ai-work/references/long-running-work.md),
[product-decision guidance](../plugins/ui-router/skills/route-ui-work/references/product-decisions.md),
and the [resource map](../plugins/ui-router/skills/route-ui-work/references/visual-resources.md).

## Validation scope

The 12 repository tests passed, including shared-manifest and marketplace version
parity. Changed Markdown links resolve locally, both entrypoint frontmatters parse,
and the field guide's embedded JSON matches its canonical data. Routing cases were
reviewed for ordinary edits, stalled phases, failed user flows and stale model advice;
this was a policy review, not an independent execution benchmark.

The bundled generic skill validator rejects the existing `compatibility` frontmatter
key on both the unchanged baseline and these revisions. That pre-existing validator
schema limitation was kept separate from the package checks; the cross-host metadata
was preserved rather than deleted to obtain a passing result.
