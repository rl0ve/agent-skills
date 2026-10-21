# Changelog

## 1.11.0 - 2026-10-20

- Add host-native long-task features to the long-running guide. Claude Code dynamic
  workflows fit fan-out audits, migrations, cross-checked research and repeated
  check-and-fix cycles. Opt in per task, run each stage that needs sign-off as its own
  workflow, and start with a scoped run because token use is higher. The `ultracode`
  keyword counts only as human input. Codex cross-window notes for Astra are
  experimental and still listed as unavailable in the configuration reference; check
  the client first, and keep the state-spec handoff for changes of model, agent or host.

## 1.10.1 - 2026-10-20

- Add a fidelity-rounds default for Dream Loop and the visual build loop in both hosts:
  start at medium, cap at 2–3 rounds with stop criteria recorded first, and raise effort
  one level only when a round stops closing a recorded gap.

## 1.10.0 - 2026-10-20

- Add Codex Ultrafast (GPT-6 Astra and GPT-6.1 Sol) as a separate service tier: 8x
  Standard usage then 6x credits on Pro $500, workspace credits on eligible Enterprise
  and Edu. Never a default; offer it only on request or for a stated deadline, after
  confirming access. Setup checks report it as unavailable unless shown.
- Add a dated Haiku 5.5 review. `haiku` resolves to Haiku 5.5 only on the Anthropic API
  with Claude Code 2.1.293+; Bedrock, Vertex and Foundry still map it to Haiku 4.5.
  `fast-scout` stays at low effort and implementation stays on Sonnet.
- Add `haiku-builder`, an opt-in, untested sole writer for mechanical edits with
  objective checks. It is not in the default route table.
- Add known engineering-discipline collaborators (mattpocock/skills,
  addyosmani/agent-skills, obra/superpowers) to capability discovery as leads to
  inspect, with one-family-per-concern and handoff-overlap rules. Nothing is installed.
- Document Codex and ChatGPT publication paths: workspace import with daily sync and
  admin-set policy, the root `plugin.json` portable manifest, and hook-based plugins'
  ineligibility for OpenAI's public directory.
- Make the README's subagent summary version-free.

## 1.9.2 - 2026-10-19

- Extend capability discovery to review the distribution and freshness of installed
  plugins. Honor plugin preferences and inspect a maintained upstream plugin before
  recommending a collection of standalone skills.
- Add a shared distribution guide covering separate publication paths, content parity,
  authenticated connectors and host runtimes, incomplete inventories, migration scope,
  exact plugin targeting and separate installed/enabled/loaded verification.
- Connect standalone-to-plugin consolidation to the existing deduplication workflow.
  An audit remains read-only; no automatic migration, cleanup or monitor is introduced.

## 1.9.1 - 2026-10-18

- Add Artificial Analysis AA-3D to the benchmark sources as a conditional input for
  model and effort choice on agent-built interactive three.js scenes. Keep its version,
  board date, printed effort label and 95% interval, treat overlapping leaders as tied,
  and read cost per task as token cost in its harness. It does not measure Claude Code
  or Codex behavior, device frame rate, Blender production or a fidelity loop.
- Record the October 18 review in `references/3d-benchmarks-review-2026-10-18.md`:
  defer 3JSBench until its grader and full results are published, keep Blender Bench v1
  as reference only (two models, effort not stated), and reject LuminaBench 3D Seaplane
  as a routing source (scoring method not published). No default route changes.
- Policy walkthrough: a fresh read-only agent used AA-3D only for a three.js scene
  brief, read the overlapping leaders as tied without an effort or cost-per-result
  claim, and left Blender scripting and a 2D dashboard on their existing sources.

## 1.9.0 - 2026-10-11

- Slim `route-ai-work/SKILL.md` from ~4,290 to ~1,550 words: overrides, timing, the
  eight routing rules, both route tables, lean-context rules, delegation, escalation
  and host notes stay; the full rationale moves verbatim to `references/model-routes.md`.
- Narrow the description so ordinary single-session architecture, debugging and review
  tasks no longer load the skill; model/effort choice, delegation, parallel and long
  autonomous work still do.
- Add the host-native harness rule: host-sensitive workflows such as Dream Loop run in
  the active host's model (Codex → GPT-6 Astra, Claude Code → Claude Opus 5.5) unless
  the user names another; no cross-host move to match an upstream harness.
- Root README keeps a short summary; the task-by-task matrix and latency/token table
  move to the Work Router README as the single human-facing copy.

## 1.8.9 - 2026-10-04

- Add reversible task, project and host-wide routing overrides with ordered priorities,
  a separate credit policy, optional model/effort constraints, and explicit on/off behavior.
- Preserve default routing and separate useful allowance use from extra spending, service
  tier changes and waste; document child-model constraints and loaded-session limits.
- Add setup diagnostics and realistic override review cases.

## 1.8.8 - 2026-10-02

- Start new substantial Claude work at Opus 5.5 medium, including long projects and
  prose; keep Fable conditional on preference, representative benefit or a capability/style limit.
- Record current Anthropic, Claude Code, Arena, Artificial Analysis and METR evidence;
  retire the old blanket Sonnet effort claim and preserve host, alias, effort and billing boundaries.
- Add conditional API migration/completion guidance and realistic routing review cases.

## 1.8.7 - 2026-10-01

- Correct Claude Max Fable allowance guidance and separate subscription authentication, shared limits and API billing without changing performance rankings.

## 1.8.6 - 2026-10-01

- Make GPT-6.1 Sol the default for substantial and complex Codex work, including
  typical new UI builds; retain upfront Astra for the hardest quality-first judgment.
- Record dated OpenAI, Arena, and Artificial Analysis evidence and limits, update
  routing cases and documentation, and retarget bundled Sol profiles to `gpt-6.1-sol`.

## 1.8.5 - 2026-09-28

- Correct the PreToolUse hook timeout from 5,000 seconds to 5 seconds. The hook
  schema uses seconds, so this keeps sudo blocking deterministic without allowing a
  stalled hook to run for more than an hour.

## 1.8.4 - 2026-09-27

- Store agent-profile backups beside the agents directory so recursive Codex discovery
  cannot load duplicate roles. On apply, preserve and relocate existing nested backups,
  even when the selected profiles are already current; dry runs report the move.

## 1.8.3 - 2026-09-27

- Make Arena and Artificial Analysis regular model-review sources, with task-specific
  original benchmarks, dated evidence, uncertainty and harness/effort boundaries.
- Add a verified Arena/Artificial Analysis assessment and prefer Astra for new
  substantial UI builds where visual quality is central; retain Sol for settled designs.
- Keep benchmark reviews conditional, preserve active contexts, and avoid automatic
  Max settings, paid trials or recurring monitors.

## 1.8.2 - 2026-09-22

- Treat an explicit same-quality savings request as a constrained usage optimization;
  remove redundant context and repeated work before reducing capability or checks.
- Add a conditional verbatim current-state reading method, review cases, and a local
  byte-volume observation that is explicitly not a token, quality or quota benchmark.
- Require measured whole-task benefit before adding decision-model integrations;
  credentials and social demos alone establish neither savings nor spending authority.

## 1.8.1 - 2026-09-22

- Align the opening routing rules with upfront Astra/xhigh selection and remove
  the unsupported claim that any retry proves a larger model is cheaper.
- Make Sol xhigh and Astra xhigh explicit skill routes, including justified upfront
  selection; add review cases for effort, urgency and whole-job token tradeoffs.
- Distinguish timing flexibility from an explicit cost-first request; no rush alone
  does not request the Luna max profile or relax judgment requirements.

- Infer urgency from context and use an occasional lightweight timing preference
  when it materially changes the route; keep Luna eligible for suitable urgent work.

- Add README task/model/effort and reasoning-level matrices, distinguishing starting
  recommendations from measured benchmark results.

- Assess all current Codex routes: Luna 6 for bounded objective work, Sol 6 for
  substantial everyday work, Astra 6 for the hardest judgment or quality-first
  direction, and Terra 5.6 as a conditional reading specialist.
- Add direct Astra selection and capability escalation without a mandatory Sol max
  attempt; preserve useful context, explicit constraints and Standard service.
- Record current benchmark settings, API-price limits, historical version boundaries,
  and the absence of a verified four-model visual-quality or elapsed-time comparison.
- Align specialist instructions and review scenarios; no new custom agent is required.

## 1.8.0 - 2026-09-22

- Make GPT-6 Sol the default for new demanding Codex work and GPT-6 Luna the
  bounded implementation and economy worker; update the stable profile names to the
  new model IDs.
- Preserve a well-progressing Astra parent, conditional Terra exploration, explicit
  model constraints, and the separation between routing speed and Codex Fast service.
- Keep GPT-5.6 measurements historical rather than presenting them as GPT-6 evidence;
  add current scenarios and an evidence-bound release review.

## 1.7.3 - 2026-09-22

- Recover interrupted processes and external jobs from current artifacts and original
  handles; distinguish polling timeouts from termination and avoid duplicate paid work.
- Preserve accepted work and user state on resume. Model, effort, delegation and
  service-tier defaults remain unchanged.

## 1.7.2 - 2026-09-20

- At long-task checkpoints, prioritize the highest-priority unmet requirement over
  easier growth in content, tests or assets. Repeated misses require cause diagnosis
  and a phase that changes the approach or resolves its prerequisite.
- Keep implementation scores and verified coverage separate from measured outcomes;
  preserve optional improvements without continually expanding completion scope.
- No model, effort, delegation or service-tier defaults change.

## 1.7.1 - 2026-09-17

- Correct the basis recorded for retiring Sonnet above medium. The direction now cites
  this repository's own harness evidence in `source-wall-clock-evidence.md` and
  `source-research-evidence.md` rather than a secondary score table.
- Record that the triggering synthesis quoted Intelligence Index scores for Sonnet 5 at
  medium and high, two settings for which this repository already verified that
  Artificial Analysis publishes no index. Those figures are unsourced.
- Note that Sonnet 5 high is the product's default effort, so narrowing Sonnet to low
  and medium is a deliberate departure from a default.

## 1.7.0 - 2026-09-17

- Retire Sonnet high, xhigh and max as routes. Sonnet medium is now the top of that
  family; the step above it is Opus low, not more Sonnet effort.
- Make Opus low the primary route for reasoning-dense implementation, in the parent,
  with Opus medium as the first escalation when it stalls or thrashes.
- Rank the Fable band explicitly and prefer Opus high/xhigh over Fable medium for long
  autonomous runs, since Fable bills separately.
- Declare `max` off the efficient frontier in every family.
- Add a retry-count rule: cost per completed task, not token price, decides the route.
- Record the caveats on Opus low: low effort does not shorten output and it delegates
  to subagents readily, so real burn can exceed a per-task estimate.
- Time a family switch to a phase or compaction boundary, because the prompt cache is
  per-model.
- Add phase-boundary handoff guidance: write a state spec rather than a conversation
  recap, keep the rejected alternatives with reasons, write to a file, and treat the
  replacement's re-reads as correct behavior.
- Document the basis for the dominance ordering and its four limits in
  `references/routing-policy.md`. It is a secondary synthesis over a composite
  benchmark, not an agentic-coding measurement.

## 1.6.0 - 2026-09-06

- Add `deduplicate-skills` as the owner for installed-skill consolidation across Codex,
  separate from capability discovery and domain-specific routing.
- Include a read-only inventory helper for explicit roots, exact listed plugin
  versions, symlink aliases, entrypoint/bundle fingerprints and disable-rule evidence.
- Distinguish copies, variants, competing owners, useful specialists and inactive
  remnants. Require scoped cleanup decisions, private backups and state verification;
  do not infer permission to remove skills from an audit request.
- Route overlap cleanup from Work Router and capability discovery without adding a
  global audit to ordinary tasks. Add regression checks for inventory safety and scope.

## 1.5.0 - 2026-09-05

- Add cross-domain capability discovery with a conditional source shortlist, installed-first checks, and explicit ownership of overlapping skills/plugins.

## 1.4.0 - 2026-09-05

- Add conditional long-task phases with explicit outcomes, ownership, acceptance
  evidence, stall diagnosis and compact handoffs. Keep routine work in the parent.
- Distinguish useful source methods from anecdotal agent counts, stale model routes,
  unexplained settings and untested context-reset suggestions.
- Preserve required scope when progress slows; phase completion is not whole-task
  completion. Extend routing review cases without claiming comparative benchmarks.

## 1.3.0 - 2026-09-05

- Make Codex routing Astra-aware: keep demanding work and loaded context in an
  active Astra parent; retain Sol, Terra, and Luna as deliberate bounded specialists.
- Separate effort escalation from model selection, and Fast routing from Codex Fast
  service. Preserve Standard service by default and explicit user model constraints.
- Verify child model/effort rather than assuming a built-in worker or a named Sol
  profile inherits Astra. No new custom profile or global settings change is required.
- Update bundled profile escalation, shared setup checks, documentation, and scenario
  guidance. Mark pre-Astra source packs as historical evidence.
- Basis: current host model catalog and routing judgment; no Astra speed/cost benchmark.

## 1.2.0

Adds `fable-wordsmith` and the rule that puts work there.

- **New agent: `work-router:fable-wordsmith`** (Fable, high, read-only). For prose whose
  quality is the deliverable: talk tracks, narration, naming, UX copy, executive writing,
  voice matching, line-level naturalness. It invokes natural-writing, runs that skill's
  linter per piece and across the set, preserves every fact, and returns keyed text for the
  parent to verify and apply. Read-only on purpose: prose edits are cheap to review and
  expensive to apply blindly.
- **Language work routes on a different axis.** The route table ranks families by reasoning
  difficulty, and that ranking does not carry to writing. Prose goes to the wordsmith rather
  than to `opus-architect` at any difficulty; Opus keeps prose only when the hard part is the
  argument or the facts rather than the words.
- **New escalation trigger.** A reader rejecting prose on feel rather than content ("this
  sounds off") is a language problem, not a reasoning one, and escalates to the wordsmith
  once the parent's own revision has failed to land.

Basis is one observed session, recorded as such in `references/routing-policy.md`, not a
benchmark.


## 1.0.0 - 2026-08-18

- Initial Claude Code-native release.
- Added task-first model and effort routing.
- Added five bounded subagents and one-writer guardrails.
- Added managed-workspace fallback behavior.
- Added deterministic `sudo` blocking hook.
