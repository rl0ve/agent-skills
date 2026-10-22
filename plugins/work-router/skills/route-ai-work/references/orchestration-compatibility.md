# Ultra and engineering workflows

Choose one owner of task decomposition, worker dispatch and acceptance. Several tools
can support that owner, but competing orchestration loops duplicate context, reviews
and writes. These are composable choices only when their responsibilities are explicit.

## Separate the controls

| Control | Responsibility |
|---|---|
| Work Router | Select execution location, model/effort and ownership within user and host constraints. |
| Model and reasoning effort | Capability and reasoning depth available for the assigned work. |
| Native orchestration | Subagent creation, steering and result collection permitted by the current host. |
| Engineering workflow | Specification, diagnosis, implementation and review method. |
| Service tier | Account-supported processing priority and billing; independent of the above. |
| Native goal or schedule | Continuation toward a bounded finish, or a separately authorized future wakeup. |

Ultra reasoning, Ultrafast service, Claude `ultracode`, a cloud executor and the
Superpowers plugin are different capabilities. None grants the others automatically.

## Ultra: check the host, then choose the owner

As checked October 22, 2026, OpenAI distinguishes ChatGPT Work's Ultra intelligence
level, which can proactively delegate suitable work, from local Codex's delegation
trigger: a direct user request or applicable project/skill instruction. The local
catalog may also expose `ultra` as an effort value. That value alone does not establish
permission to delegate, an active service tier, or the models used by children.
[Official subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents).

- **Native orchestration leads:** when the user selects that behavior and the host
  supports it, let it decompose and dispatch. Work Router supplies constraints,
  destination suitability, one-writer boundaries and acceptance criteria. Do not add
  a second fan-out or rerun completed native reviews merely to satisfy the router.
- **Work Router leads:** for an explicit location/model split or cross-thread
  coordination, the accepting parent owns the work map and uses native controls to
  execute it. Ultra can provide depth inside an assigned task; it does not require
  another coordinator or recursive worker tree.
- **Restricted delegation:** verify that the selected mode can honor a no-subagents
  or locked-model requirement. Custom profiles can select their own model. Do not
  assume an Astra parent makes every worker Astra. If the native route cannot verify
  compliance, report the incompatibility and continue feasible work in the capable
  parent without secretly changing its effort or tier.

Choose Ultra for a task-specific depth need, or preserve it when explicitly chosen.
It is unnecessary just to use threads, remote machines, cloud tasks or a development
method. High effort cannot repair unavailable files or a broken execution environment.
There is no measured claim here that Ultra plus another orchestrator is faster or
better than one capable coordinator.

## Superpowers: optional method, overlapping coordinator

Superpowers is not required for Work Router's location or model routing. Selected
debugging, specification, testing and verification skills can augment a task when
that discipline is useful. Its full development workflow also selects implementers,
reviews their work and finishes branches, so it overlaps with orchestration.
[Upstream overview](https://github.com/obra/superpowers).

Inspect the **installed version and exact skill**, not only the latest README. The
October 22 review found upstream 7.0.1 and older installed variants with different
review and session rules. Do not assume those versions have identical behavior.

| Overlap | How to compose it |
|---|---|
| Broad `using-superpowers` activation and mandatory planning | A task-specific user choice and host instructions govern. Do not let a broad trigger introduce an unnecessary planning interview for an already defined small change. A skill cannot change the system/developer instruction hierarchy. |
| `subagent-driven-development` assigns implementers and reviewers | If explicitly selected, let its controller own that phase. Work Router supplies compatible model/location constraints. Do not assign a second implementer or duplicate review loop for the same task. |
| Cheapest-capable-model guidance | Respect the user's priorities and locked model; assess total completion cost. A framework's economy default cannot override an Astra-only instruction. |
| Worktrees and branch finishing | Reuse the host's managed isolation and the established integration owner. Respect live tool authorization. A worker's finish workflow does not grant permission to merge, delete another owner's branch or retire its checkout. |
| Test-first development and repeated reviews | Use the selected method where it improves the actual change. Existing verification may satisfy a shared gate when it covers the same artifact and criteria; do not invent tests that only restate documentation. |
| Missing subagent capability | Use the framework's supported inline workflow if compatible with the request, or keep work in the parent. Do not install another runtime or switch hosts solely to imitate its agent diagram. |

If the user wants the full Superpowers workflow, honor it within higher-priority
instructions and explain any actual incompatibility. If only one method is needed,
use that named skill and keep orchestration with the existing owner. For a routine
contained change, no added framework is necessary. Installing, updating or disabling
Superpowers is separate from deciding how to compose it; an overlap finding alone
does not authorize changing the installation.

Apply the same rule to other engineering families: one owner per concern. UI Router
still owns visual/design method, Natural Writing owns final prose, and Work Router owns
execution selection. Do not stack several planning, TDD or final-edit frameworks by
default. See [known collaborators](../../discover-capabilities/references/known-collaborators.md)
when a method is missing, and [long-running work](long-running-work.md#host-native-long-task-features)
for Claude dynamic workflows; `ultracode` has its own opt-in and cost rules.

## Source scope

The compatibility judgments are routing policy, not comparative performance results.
Superpowers sources inspected October 22, 2026:
[manifest](https://github.com/obra/superpowers/blob/main/.claude-plugin/plugin.json),
[activation](https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md),
[subagent development](https://github.com/obra/superpowers/blob/main/skills/subagent-driven-development/SKILL.md),
[branch finishing](https://github.com/obra/superpowers/blob/main/skills/finishing-a-development-branch/SKILL.md).
These are moving upstream links. Reinspect the installed content when a conflict
matters; do not import upstream instructions merely by researching them.
