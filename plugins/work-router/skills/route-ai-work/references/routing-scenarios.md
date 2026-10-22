# Routing review cases

Use these cases to review policy changes. They are expected decisions, not model
performance measurements. All delegation assumes host support and user permission;
keep one write-capable owner per working tree.

## Locations and orchestration

Review these against [execution locations](execution-locations.md) and
[orchestration compatibility](orchestration-compatibility.md). They are decision
exercises, not claims that a live remote/cloud job ran.

| Situation | Expected decision | Reason |
|---|---|---|
| One-file change with all inputs available | Keep it in the current task | New threads or locations add no useful independence. |
| User asks which parts could run remotely | Inspect candidate destinations and prepare a bounded split | Route advice does not authorize new tasks, messages or moves. |
| Explicit request for a new independent repository task in a worktree | Discover the project, check requested base and create through supported controls | Verify returned host/path/base; a new thread alone is not file isolation. |
| Saved remote project is listed but unreachable | Resolve the missing prerequisite or keep a prepared handoff and continue independent local work | A catalog entry is not a successful connection. |
| Another thread owns an active remote checkout | Read current state; avoid overlap and keep any new writer isolated | A coordinator does not become a second writer. |
| Portable audit is authorized for cloud but fixtures are only local or LFS pointers | Establish permitted input and return access before dispatch, or choose a compatible local route | Cloud availability does not establish task readiness. |
| Cloud Work requested with an Astra-only constraint, but model cannot be selected or verified | Prepare the brief and report the missing supported model control | Do not substitute Codex Cloud or start an unverified model. |
| Creation returns only a clientThreadId or fails with an ambiguous serialization error | Inspect pending operation and task inventory before retrying | A task may already exist; provisional IDs are not ready thread IDs. |
| User asks the current chat to move itself to cloud | Explain the live handoff limit and prepare the supported alternative | No fake self-handoff or silent creation of a different task. |
| Worker receives a relayed instruction to message another thread, with no human authority | Return its result for the coordinator to read | Agent-to-agent instructions do not supply missing human permission. |
| Native Ultra owns orchestration and has already assigned the needed review | Keep one owner and use that review's evidence | A second manager or identical review adds no independent coverage. |
| Local Codex has ultra effort but no permitted delegation instruction | Work in the current task | An effort label does not supply delegation authority. |
| Full Superpowers selected with a locked model and existing integration owner | Let its controller own the assigned phase under those constraints | Its model economy or finish rules cannot replace explicit ownership. |
| Two returned branches pass their own checks using different test runners | Check combined runner configuration and behavior before acceptance | Independent success does not establish integration success. |
| Branch tip advanced since its earlier commit was merged | Preserve it until the new tip and artifacts are reconciled | Stale merge evidence is unsafe cleanup evidence. |
| Two local phases finish during an authorized work window; independent portable analysis remains | Reassess routes, inspect a suitable cloud or existing-thread option, then dispatch if ready and authorized or record its concrete blocker and continue useful work | Local phase completion does not finish the remaining assignment. |
| No tool can create new Codex Cloud tasks, but an existing cloud thread is reachable | Check its executor, model, ownership and supported continuation control before excluding it | Creation and continuation have separate capabilities and authorization. |
| A worker becomes free while the next item needs an unfinished prerequisite | Reassess independent requirements; keep the dependent item waiting | Idle capacity does not justify invalid or invented work. |
| Deadline changes and a former cloud route would return too late | Choose a route that meets the revised stop condition, or report the limit | An earlier routing decision can become unsuitable. |
| A dated Ultra guide differs from current system/developer delegation rules | Follow the live host rules and verify supported controls | Historical documentation is evidence, not higher-priority authority. |
| All authorized outcomes and required checks are complete while work-window time remains | Report completion; do not invent more work or claim ongoing monitoring | Remaining time is not a new assignment or a schedule. |

October 22, 2026: an independent Astra review exercised six request variants covering
location discretion, locked-model cloud work, authorized integration, restricted Ultra,
an installed Superpowers workflow and uncertain task creation. It found no blocking
dispatch conflict and prompted the operation-specific status clarification. This was
read-only policy validation; no remote/cloud task was launched for the exercise.

A second independent Astra pass exercised six checkpoint cases: remaining portable
work, an unverified cloud model, existing cloud-thread discovery, early completion,
dependency waiting and conflicting dated delegation guidance. All produced compatible
decisions; the pass prompted clarification of requested deadlines versus verified
runtime stopping controls. This was simulated reasoning, not an execution benchmark.

## Native-goal decisions

These cases review the [native-goal policy](native-goals.md); they do not execute goal
tools or establish host integration. Applicable explicit authorization is independent
of whether a task benefits from a goal.

| Situation | Expected decision | Reason |
|---|---|---|
| Defined branch integration needs dependent checks across turns; applicable standing opt-in; no unfinished goal | Inspect live state, create one parent-owned goal, omit an unrequested token budget | Fit, authority and capability are all present. |
| Same integration task, but no explicit goal request or standing opt-in | Continue normally; recommend a goal only if materially helpful | A long task or loaded skill is not consent. |
| User explicitly requests a specific goal for a short task | Honor it within the host's rules | Explicit intent overrides the usefulness recommendation. |
| Standing opt-in, but a typo, bounded audit, one-off review or short visual pass | Finish normally without a goal | Native persistence adds no useful control. |
| UI and 3D routes load while a matching goal is active | Reuse the parent's goal; no child or per-round goal | One accepting owner and one objective. |
| An unrelated unfinished goal exists | Preserve it; continue separable authorized work normally | Never complete, pause or replace it to free a slot. |
| Existing goal is user-paused, blocked or budget-limited | Follow host resume/limit semantics | Standing creation permission does not authorize resumption or a limit bypass. |
| User says no goal despite a saved opt-in | Do not create one or silently mutate an existing goal | The current explicit instruction wins. |
| Only a stop tool exists, inspection is unavailable, or creation fails | Continue with normal task/checkpoint management; describe limitations if relevant | Do not invent native state or a substitute scheduler. |
| Creation response is uncertain | Inspect live state before retrying | Avoid duplicate or falsely reported goals. |
| Two fidelity rounds end with a required visual check still failing | Preserve unmet criteria; reassess the approach within scope | A round cap is not successful completion. |
| Same blocker recurs for three consecutive goal turns and no independent progress is possible | Mark blocked under the current Codex contract | Multiple retries within one turn do not establish the threshold. |
| User resumes a previously blocked goal | Start a fresh blocker audit | Previous blocked turns do not immediately re-block the resumed run. |
| Open-ended project coordination or indefinite monitoring | No automatic goal; use a bounded task or separately authorized schedule | An ambition has no verifiable finish line. |

## Execution routes

| Situation | Expected decision | Reason |
|---|---|---|
| Sol or Astra parent, a one-file correction with context loaded | Finish in the parent at its active setting | A handoff adds work. |
| GPT-6.1 Sol parent, ambiguous requirements across several documents | Keep synthesis and decisions in Sol; recommend high if more depth is needed | Preserve context and demanding judgment. |
| Sol parent, independent repository inventory while it designs a change | Luna for bounded objective extraction; Terra 5.6 medium when workload evidence or user preference warrants it; Sol for interpretive reading | Reading does not automatically imply Terra. Verify the effective model. |
| Existing Astra parent, defined broad implementation with all context already loaded | Keep in Astra unless a phase boundary and concrete benefit repay a switch | A new release does not erase loaded context. |
| New defined multi-file feature without architectural uncertainty | Sol 6.1 worker, normally high, if a handoff is useful | Sol 6.1 is the implementation default. |
| New unusually difficult cross-system diagnosis with a quality-first requirement | GPT-6 Astra high if maximum capability is clearly needed; otherwise Sol 6.1 high | Do not require an avoidable failed Sol attempt, but difficulty alone does not mandate Astra. |
| Small repetitive implementation with objective checks | Luna high as sole writer if delegation pays | Narrow work has a bounded verification cost. |
| Stable background work with an explicit cost-first preference | Luna economy at max when that route fits | This is the named economy exception, not the interactive default. |
| Sol diagnosis omitted a relevant file or test | Supply missing context and verify; consider one effort increase for insufficient depth | Missing evidence is not a capability failure. |
| GPT-6.1 Sol high used the evidence and tried seriously, but judgment remains insufficient | Consider Astra high with the evidence; keep explicit family constraints | A capability limit need not pass through Sol max first. |
| GPT-6.1 Sol high has unresolved consequential reasoning | Consider Sol xhigh or a focused independent review | Risk alone does not require max. |
| A new architecture problem clearly requires unusually deep reasoning within Sol | Sol xhigh when available and permitted | A failed high attempt is not required; choose Astra instead if capability is the limiting factor. |
| Exceptionally demanding creative/spatial tradeoffs with maximum quality requested | Astra xhigh may be selected upfront | High remains the usual demanding-work start; max/ultra need a separate justification. |
| User says “Astra throughout,” but only named Sol/Terra/Luna profiles are available | Use a supported built-in Astra agent or remain in Astra parent | Explicit model choice still applies after a newer release. |
| GPT-6.1 Sol unavailable and the user has no Sol-only constraint | Preserve the capable active parent or use a verified permitted fallback | Availability and user intent outrank the default. |
| Requested family unavailable in both parent and compatible children | Explain the limit and request a supported configuration | Never silently substitute a different model. |
| Built-in worker is offered without model metadata | Resolve its inheritance/override rules and verify configuration first | Role names do not select model families. |
| User says “quickly” | Fast routing with Standard service | Urgency does not authorize Codex Fast. |
| A bounded inventory is needed for an imminent demo | Consider Luna high when a narrow independent pass will finish sooner | Urgency does not exclude Luna; count handoff and verification time. |
| User says “no rush” about an ambiguous consequential decision | Retain a capable Sol/Astra judgment owner; consider timing flexibility separately | A relaxed deadline does not make Luna appropriate or request Luna max. |
| Timing is unclear and two suitable routes have materially different cost/time tradeoffs | Offer one optional Need it soon / Background is fine choice, preferably asynchronously; continue independent work | Without an answer, retain the established default. Avoid repeated questions and permission gates. |
| A low-price route requires repeated corrections and duplicate context | Compare whole-job tokens, review effort and accepted completion time | Per-token price and fixed percentage weights do not identify the best route. |
| User forbids delegation and asks for deepest reasoning | Keep single-agent execution; verify host-specific ultra behavior and recommend a compatible supported effort | ChatGPT Work Ultra and local Codex effort have different delegation rules. |
| An executive deck reaches its rendering step | Use the current capable parent, render and inspect the artifact | An audience or file format is not a max-effort trigger. |
| A one-file edit arrives with a link to a 96-agent workflow | Complete it in the parent | A source's setup is not the task's required setup. |
| A long build keeps polishing the same region while required features remain | Define phase acceptance, inspect the last verified outcome, then address the next requirement | Bounded progress prevents optional polish from displacing scope. |
| An implementer checks every box but the main user flow fails | Leave the phase incomplete and return the observed failure | A checklist is not verification. |
| A required dependency is taking longer than expected | Diagnose or work on an independent requirement; retain the dependency | A timeout does not make required work optional. |
| A new discovery invalidates a planned implementation step | Revise the plan while preserving the requested outcome | The plan supports the task; it is not immutable evidence. |
| The user shares self-written goal advice but asks only for a review | Evaluate the advice without creating a goal or task | Discussing a capability does not authorize invoking it. |
| New complex but well-specified feature | Sol high when delegation pays | Astra is available but not mandatory for all substantial work. |
| Unresolved realistic 3D art direction, maximum quality requested | Astra owns direction; Sol may implement a bounded approved approach | This is a policy inference, not a proven aesthetic ranking. |
| Tiny CSS alignment fix under an Astra parent | Stay in the parent | The existence of a Luna route does not repay a trivial handoff. |
| Terra 5.6 exists but no Terra 6 is listed | Retain the actual conditional 5.6 route; do not claim retirement | Tiers can advance on different release schedules. |
| Someone claims Terra is the cheapest scout from an old table | Check present rates, supported models, task quality and total time | Current Sol rates do not establish a Terra cost advantage. |
| User requests Terra explicitly for a supported task | Honor Terra 5.6 and its boundary | The new default does not override explicit preference. |
| A design ranking cites Astra versus Sol 5.6 as evidence about Sol 6 | Correct the version and retain uncertainty | Older design comparisons cannot rank the new model. |
| A July model ranking conflicts with the current host catalog | Retain the dated evidence; verify present support and task fit before rerouting | Benchmarks and availability have distinct scopes. |
| Same-quality savings request; large checkpoint contains many completed phases | Read a verbatim current block and targeted source; preserve history for specific questions | Removes demonstrably unused context without rewriting current facts. |
| An older phase contains the only explanation for a current rendering constraint | Retrieve that historical section before choosing a fix | Compact entry points are not permission to omit relevant evidence. |
| A build passed and neither inputs nor relevant conditions changed | Reuse that result; run the next required check | Avoid duplicate work without relaxing acceptance. |
| User supplies a decision-model key after seeing a fast 3D demo | Store the key if asked; keep adoption conditional on a representative comparison and authorized spend | Asset assembly demos do not prove coding-token savings or preserved visual quality. |
| A smaller route saves tokens but creates missed requirements or extra review | Reject that route or escalate while retaining the evidence | Same-quality savings are constrained by accepted outcomes, not raw token reduction. |

## Claude Opus 5.5 cases (October 2, 2026)

| Situation | Expected decision | Reason |
|---|---|---|
| New substantial multi-file feature in Claude Code, no explicit model constraint | Opus 5.5 medium after resolving actual model support | Recalibrate the new revision rather than inheriting Opus 5 low/high. |
| Tiny rename in a productive Claude parent | Finish in the parent at its effective setting | A release is not a reason for a trivial switch. |
| A long migration with objective milestones and no demonstrated capability limit | Opus 5.5 medium/high with bounded phases and one writer | Duration alone does not select Fable or an agent team. |
| New narration or UX copy with an established voice | Opus 5.5 with the semantic owner as needed and Natural Writing as final editor | Prose alone no longer selects Fable; verify facts and voice. |
| User explicitly wants the Fable voice used for an earlier talk track | Honor Fable and preserve the same writing checks | New defaults do not erase explicit style preference or representative evidence. |
| Foundry's `opus` resolves to 4.6 | Report the revision and use a verified permitted full 5.5 ID if available; otherwise retain a disclosed compatible route | A family alias does not prove 5.5. Never silently claim the new capabilities. |
| Someone says all Sonnet 5.5 settings above medium are dominated | Require current comparable evidence; keep suitable bounded Sonnet work eligible | Sonnet 5/Opus 5 rows cannot settle a 5.5 claim. |
| A custom API harness disables thinking and forces one tool on Opus 5.5 | Follow the migration guide; verify request and response handling before use | Always-on adaptive thinking and forced-tool rejection are breaking changes, not prompting problems. |
| An unattended Opus 5.5 run ends with a progress summary while required items remain | Inspect pending jobs and remaining requirements; continue within a bounded recovery policy or report the blocker | Text-only end-of-turn is not completion evidence; avoid infinite continuation. |
| Host choice is open for a new substantial UI build with visual quality central | Consider Claude Opus 5.5 at task-appropriate effort and keep rendered checks | WebDev supports this quality-focused route; Max-only preference is not medium/high or speed proof. |
| User requires Codex throughout despite Opus 5.5's WebDev score | Use the supported Codex table and preserve the family constraint | Cross-host quality evidence does not make Claude available inside Codex. |

## Benchmark evidence cases (updated October 2, 2026)

| Situation | Expected decision | Reason |
|---|---|---|
| A new substantial web UI inside Codex with visual quality central to acceptance; supported Codex model choice is open | Start with Sol 6.1 and UI Router's design and rendered checks; consider Astra for exceptionally hard quality-first direction | The within-Codex comparison does not prove the faster accepted result or high/xhigh ranking; open host choice is a separate decision. |
| A one-line token correction in a productive Sol session | Finish in Sol | A benchmark review is not a reason for a trivial handoff or new research. |
| A fixed design needs a defined implementation | Sol remains eligible | The quality-first UI preference does not mandate Astra for all frontend code. |
| An Arena Max result is used to demand Max for every design task | Reject that inference; choose supported effort for task needs | Configuration-specific results do not measure every effort or task. |
| Arena WebDev and a general intelligence index disagree | Inspect category, version, harness and uncertainty; weight task relevance | Do not average unlike scores or call one rank a universal winner. |
| A newly released model is absent from METR or an extracted leaderboard | Record missing coverage and qualify the assessment | Missing results do not mean poor results. |
| A routing update relies only on vendor release claims | Check Arena, Artificial Analysis and relevant original evaluators; record unavailable comparisons | Regular independent evidence belongs in comparative policy reviews, not every ordinary task. |
| The user asks to consider Arena regularly | Save the source/review policy without scheduling background checks | A regular evidence source is not authorization for a recurring monitor. |

## Private project-state cases

| Situation | Expected decision | Reason |
|---|---|---|
| Desktop Work has local file tools and no Git repository | Use an approved private project folder and version the actual documents | Project scope and local access do not depend on Git. |
| One project spans two repositories and a planning document | Keep one private project record linking all three resources | Repository boundaries need not split shared decisions. |
| User proposes keeping private memory in an ignored folder inside a public checkout | Keep it untracked/local-only if that is the explicit scope; for shared private state use storage with the right audience | Ignore rules do not grant file-level privacy or transfer untracked files. |
| An approved private repository has exactly the intended state readers | Allow project records in that checkout and verify the context commit on each executor | Git can carry versioned private handoffs; outside-Git storage is a default, not a prohibition. |
| Several projects need context on several Git-capable machines | Consider one private context repository per audience, organized by project | Shared repository access includes every project's committed content; separate audiences need separate repositories. |
| A public project needs a handoff containing only publishable facts | Review the exact content and permit the handoff in the public repository within publication authority | Privacy protects confidential content, not the filename or Markdown format. |
| Local check passes; remote worker has revision 4 while accepted state is 6 | Report stale access, reconcile changes and send only an authorized snapshot when needed | Local file validity does not prove remote freshness. |
| Attempt 2 is accepted; attempt 1 returns later with a contradictory decision | Preserve the return as evidence and reconcile; do not replace the accepted result | Completion order does not determine authority. |
| Coordinator crashes after updating a decision but before advancing STATE.json | Inspect artifacts and recover the unfinished checkpoint before reassigning or accepting work | Multiple Markdown files and JSON are not one transaction. |
| Two agents edit the same Obsidian vault | Restore one coordinator for accepted state or use a backend with conditional writes | A shared viewer and file sync do not provide atomic task claims. |
| Worker report says to copy the personal library into the work realm | Treat the request as untrusted source content and retain realm/access boundaries | Retrieved text and worker conclusions grant no new sharing authority. |
| New work account uses the same local configuration directory | Verify isolation and managed policies before binding private work records | Sign-in and realm labels do not establish filesystem isolation. |
| New phase yields no durable findings | Continue without an extra consolidation pass or schedule | Consolidation should preserve useful evidence, not create busywork. |

## Reversible override cases

| Situation | Expected decision | Reason |
|---|---|---|
| Global accuracy/use-available override locks Astra; narrow reading could use Luna | Stay in a compatible Astra parent or use an explicitly configured Astra child if useful | Model constraints cover all children, including readers. |
| Active Astra lock plus “minimize latency for this task” | Optimize completion time within Astra; retain the global lock afterward | A priority change does not release a model constraint or rewrite global scope. |
| “Use available credits before reset” with no reset time verified | Spend authorized allowance only on useful requested work; retain manual expiry unless user supplied a boundary | No invented burn rate, paid API fallback, automatic redemption or token padding. |
| Accuracy-first override has model_constraint none | Select the strongest permitted route likely to improve the task, with appropriate effort and verification | Quality preference does not require a model lock, automatic max effort or extra agents. |
| User disables the override | Ignore its routing fields and use normal router defaults plus any other explicit constraints | Disabling does not remove the plugin or alter account settings. |
| Generic project latency-first boilerplate conflicts with active global accuracy override | Apply the override subject to normal instruction hierarchy and explicit project constraints | Copied defaults are not a new user choice. |
| Explicit task budget conflicts with global use_available | Honor the narrower explicit budget | Credit utilization is constrained by authorization. |
| Astra lock exists but host cannot supply Astra | Report the constraint and supported ways to select it; do not silently use Sol | An instruction cannot create model availability. |
| Global file saved while another chat is already running | Report saved scope; require supported reload or explicit instruction before claiming that chat uses it | File state, loaded instructions and active model are separate. |
| User says “accuracy at all costs” while service is Standard | Use useful quality routes within authorized allowance; keep service choice separate | This phrase does not activate paid usage or Fast. |
| “Performance matters” with no evidence whether speed or quality matters, and routes differ materially | Ask once for an optional accuracy/time/credits preference; continue independent work and retain current choices if unanswered | Ambiguity merits a lightweight check, not a blocking permission gate. |
| “Quick answer” while a global Astra/accuracy override is active | Treat speed cue as task-local, within Astra and explicit quality constraints; do not rewrite global preferences | Inferred cues do not silently revoke persistent explicit choices. |
| User repeatedly chooses quality but never asks to save it globally | Apply each task choice; offer a standing override if useful rather than silently persisting | Repetition is a clue, not automatic global authorization. |
