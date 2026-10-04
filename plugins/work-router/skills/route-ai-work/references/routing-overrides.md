# Reversible routing overrides

An override changes the user's routing preferences without editing the default route
tables, replacing the skill, or changing a running model. Resolve it before applying
any default. It remains subject to higher-priority instructions, host availability,
permissions and the user's explicit constraints.

## Controls

Use a clearly marked instruction block. These are agent-readable preferences, not
Codex configuration keys or an automatically executed settings file.

| Field | Meaning |
|---|---|
| `enabled` | `true` applies the block; `false` ignores all its routing fields and restores normal routing for its scope. Removing the block has the same effect. |
| `scope` | Current task, current project, or all projects/chats on the configured host. Persist only the scope the user requested. |
| `priorities` | Order `accuracy`, `latency`, and `credit_conservation`; earlier goals win tradeoffs. Preserve required acceptance criteria in every order. No invented percentage weights. |
| `credit_policy` | `normal`, `conserve`, or `use_available`. This is separate from the priority order and any model constraint. |
| `model_constraint` | `none`, an explicit family, or an exact supported model ID. Applies to parent and children; never silently substitute. |
| `effort` | `task_appropriate` or an explicit supported level. Preserve an effective active setting unless the user requests a change. |
| `expires` | `manual` or a user-specified time/boundary. Do not invent a reset time or create a monitor to manage it. |

`accuracy` first means choose the strongest permitted route and verification likely
to improve the outcome, without a mandatory attempt on a cheaper model. It does not
promise perfect accuracy, force an automatic maximum effort level, or require extra
agents. `latency` first means shortest accepted completion time, including handoffs,
retries and review. `credit_conservation` first minimizes total usage while preserving
acceptance criteria; token price alone does not establish subscription consumption.

`use_available` means the user prefers spending already available allowance on useful
quality, depth or independent verification over downgrading merely to save credits.
It never means maximize token count, pad an answer, rerun passed checks without reason,
create unrequested work, or consume a reset. `conserve` favors avoiding redundant work
and permitted economical routes. Neither credit policy authorizes new purchases,
extra usage, paid APIs, external generation, or a different service tier. Verify live
usage/reset facts only when needed; never guarantee a specific burn rate or exhaustion.

## Scope and precedence

A new explicit user choice wins over an older override in its stated scope. A task-only
choice does not rewrite the global preference. A global override supersedes generic
router defaults and copied latency-first personalization, while explicit task/project
constraints and the normal instruction hierarchy remain binding. Do not treat a generic
project default as a new user choice cancelling an active global override.

When a user asks to change priorities, update those fields and retain any model lock
unless they also release it. For example, “minimize latency” under an Astra constraint
means optimize within Astra; “let the router choose the model” removes that constraint.
If mutually exclusive instructions would materially change the route, resolve the
conflict rather than silently dropping one. An unavailable locked model is a reported
constraint, not permission to use another family. Verify actual child configurations;
fixed-model named profiles do not become compliant through the parent's model alone.

For persistence, use the host's user instructions (Codex: the active Codex home's
`AGENTS.md`; Claude Code: its user `CLAUDE.md`) with a small bounded block. Preserve
unrelated instructions and keep a backup. Do not edit installed plugin caches, copied
agent profiles or account settings to implement an instruction override. Do not publish
personal active preferences in a shared plugin repository.

User instruction files are local to their host. They do not synchronize remote/cloud
hosts or other applications. A saved block is not proof that existing chats reloaded
it; new chats must load the updated instructions, and existing chats need a supported
reload or an explicit instruction. A routing rule cannot switch a running parent's
model, effort or service tier; report requested and confirmed settings separately.
If the host loads a higher-precedence instruction file instead, update that effective
location only within the user's authorized scope and preserve its other content.

## Example block

```markdown
<!-- work-router override:begin -->
## Active routing override

This enabled override supersedes Work Router's default optimization and model choices,
including generic latency-first personalization. Keep underlying defaults unchanged.

- enabled: true
- scope: all projects and chats on this Codex host
- priorities: accuracy > latency > credit_conservation
- credit_policy: use_available
- model_constraint: gpt-6-astra
- effort: task_appropriate
- expires: manual

Apply the model constraint to all model work, including delegated reading and review.
Use a compatible parent or explicitly configured supported child; do not silently
substitute a fixed-model profile. Select depth for useful quality, not token burn.
Use already available credits for useful work; this does not authorize purchases,
paid APIs, extra usage, reset redemption or Codex Fast. Service tier is a separate
choice; default new choices to Standard unless explicitly authorized otherwise.
Never claim that this block changed a running model or service tier.

To turn off the override, set enabled to false or remove this bounded block. To change
priorities or the model constraint, update only those fields on the user's request.
<!-- work-router override:end -->
```

## Plain-language changes

| User request | Override change |
|---|---|
| “Highest accuracy at all costs” | Put accuracy first; spend only within already authorized allowance, retain model constraints, choose useful depth and checks. |
| “Use my available credits for quality” | Set `credit_policy: use_available`; do not equate consumption with quality. |
| “Minimize latency” | Put latency first; preserve an existing explicit model constraint unless released. |
| “Conserve credits” | Put credit conservation first and set `credit_policy: conserve`; preserve required quality and explicit model choice. |
| “Use Astra for everything” | Set the verified Astra ID as `model_constraint`; include children. |
| “Let the router choose the model” | Set `model_constraint: none`; keep other override preferences. |
| “Turn off the override” | Set `enabled: false` in the requested scope; do not reset account settings or remove the router. |

These changes need no new installation or plugin release. When persisting a request,
report the effective scope, priorities, model constraint and loading limits briefly.

## Listen for cues; ask only when useful

Treat clear cues as task-local preferences: “quick answer” or an imminent deadline
favors latency; “save credits” favors conservation; “use my credits before reset”
favors `use_available`; “highest accuracy” favors quality. These cues do not implicitly
create or rewrite a persistent override, release a model lock, grant delegation, or
approve paid services. Strong explicit choices win over inferred cues. “Performance”
alone can mean accuracy or speed; infer only when context makes the meaning clear.

When ambiguity or conflicting cues would materially change the route, ask once with
an optional concise choice: “For this task: best accuracy, shortest time, or conserve
credits?” Use an available asynchronous preference control when possible. Continue
independent authorized work while waiting; without an answer, retain the current
explicit override/default and state the assumption only when material. Do not ask on
every task, treat silence as authorization, block useful work on an optional answer,
or repeatedly offer a choice already settled by the user. If permission is actually
required, this optional preference check cannot supply it.

Offer persistence only when the user signals a recurring preference or asks for a
standing change; ordinary task cues stay local. “From now on,” “all projects/chats,”
and “make that my default override” explicitly request persistence at the stated scope.
An explicitly supplied “until reset” boundary requires a verified reset time or a
clarification before saving a timestamp; it does not create a wakeup or automation.
