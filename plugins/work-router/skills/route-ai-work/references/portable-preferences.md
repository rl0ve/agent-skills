# Portable user preferences

A profile carries a user's chosen working preferences between environments. It is
inert package data until that user explicitly selects and applies it. Installing
Work Router does not opt anyone into a profile, grant goal-creation permission or
change the router's defaults. Never infer consent from a profile name, a checked-out
repository or an example command.

Use this workflow when the user asks to carry their preferences to another machine
or refresh a previously selected profile. Preserve newer explicit local choices;
if they conflict with the selected profile, resolve that conflict before applying it.
Keep credentials, machine paths, private context and account settings out of profiles.
For adoption in a work account, use [the work-account guide](work-account-setup.md).
The portable profile carries working preferences; separate private project records
and verified access carry the work's context. Installing either does not synchronize
the other or establish account isolation.

## Set up an environment

Install Work Router through the host's normal marketplace mechanism. Install UI
Router and Natural Writing separately if the chosen workflow calls for them; a
preference referencing a skill does not install it. From a trusted checkout of
`rl0ve/agent-skills`, run the following with Python 3.10 or newer. On Windows use
`py -3` if `python3` is unavailable.

```bash
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex --print
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex --apply
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex --check
```

These commands explicitly select the `rl0ve` profile. For Claude Code use
`--host claude-code`; its model policy stays host-specific. From an installed Work
Router package, the same script is at
`skills/route-ai-work/scripts/sync_user_preferences.py`, relative to the package root.
Discover the actual installed path; do not hard-code another machine's cache path or
edit the cache. Inspect `--print` before applying a newly published profile revision.

| Host | Default destination | Verification |
|---|---|---|
| Codex | Active `CODEX_HOME` (otherwise `~/.codex`), nonempty `AGENTS.override.md` if present, otherwise `AGENTS.md` | Start a fresh chat and verify the loaded instructions and actual model availability. |
| Claude Code | `CLAUDE_CONFIG_DIR` (otherwise `~/.claude`), `CLAUDE.md` | Start a fresh session and inspect `/memory` and the active routing/plugin setup. |
| Remote computer or container | The executing host's own user instruction file | Run setup there; local installation does not configure a remote executor. |
| Cloud or managed environment | An administrator-approved instruction surface | Review `--print`, then apply through that host's supported mechanism; verify scope and loading. |

`--destination /absolute/path/to/instructions.md` supports an explicit alternative.
A repository instruction file affects everyone who loads it; do not publish personal
opt-ins there without authorization for that scope. If a cloud runtime cannot run
this script, copy only the reviewed profile to its supported instruction surface.
Managed model, plugin and instruction policies still apply. No supported surface
means this profile cannot promise equivalent behavior in that environment.

The `rl0ve` profile currently selects accuracy before latency and credit conservation,
one writer per working tree, bounded delegation, conditional native goals for
already-authorized tasks, and an Astra constraint in Codex. Claude Code uses its own
host routing. Native goals remain conditional on actual host support. Neither profile
changes a running model, service tier, subscription, permissions or paid API access.

## Refresh, check or remove

After updating the plugin or trusted checkout, rerun `--print`, the dry run, `--apply`
and `--check` on each enrolled host. There is no background synchronizer or install
hook. The profile in Git is the portable source; the local instruction file is the
active copy. A local edit is not automatically uploaded or propagated elsewhere.

`--check` exits 0 when current, 1 on drift and 2 on an error. A dry run writes nothing.
Repeated application is idempotent. Only the profile's bounded `work-router` blocks
are replaced; unrelated bytes are preserved. Existing valid legacy blocks migrate
without adding duplicates. Malformed/duplicate markers, symlinks, hardlinks and
noticed concurrent edits are refused. Use a verified canonical path for a deliberately
linked home. Do not use root or sudo.

Changed existing files receive a private backup under
`~/.agent-skills/preference-backups` (or `--backup-dir`), outside agent instruction
discovery. Backups contain the entire private original: keep them out of shared
repositories. They use owner-only POSIX permissions; Windows users should verify
their user directory's ACLs. The updated file preserves its existing mode. Removing
the managed blocks keeps all other content:

```bash
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex --remove
python3 plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py --profile rl0ve --host codex --remove --apply
```

Report separately: source revision, publication, installed plugin, applied profile,
and verified session loading. Unit tests cover Windows-style line endings and host
paths; native Windows execution must be verified on Windows before claiming it works
there. A useful onboarding request is: "Set up rl0ve/agent-skills and apply my rl0ve
workflow profile for this environment; preserve existing instructions and verify
what loaded."

Official instruction-loading references, checked October 22, 2026:
[Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[Claude Code memory](https://code.claude.com/docs/en/memory), and
[Claude Code configuration](https://code.claude.com/docs/en/settings).
