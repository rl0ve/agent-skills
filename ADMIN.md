# Company administrator handoff

Claude Code managed settings can restrict third-party marketplaces and model availability. This package does not attempt to bypass either control.

## Git-hosted marketplace

After your organization hosts this marketplace in an approved repository, an administrator can register and enable it with managed or project settings:

```json
{
  "extraKnownMarketplaces": {
    "rl0ve-agent-skills": {
      "source": {
        "source": "github",
        "repo": "YOUR-ORG/YOUR-REPOSITORY"
      }
    }
  },
  "enabledPlugins": {
    "claude-ai-work-router@rl0ve-agent-skills": true,
    "ui-router@rl0ve-agent-skills": true,
    "natural-writing@rl0ve-agent-skills": true
  }
}
```

If `strictKnownMarketplaces` is enforced, the approved repository or internal Git host must also appear in that allowlist. A local ZIP alone cannot override the policy.

## Model policy

The AI router requests family aliases from subagents:

- `haiku` for narrow read-only scouting;
- `sonnet` for routine implementation;
- `opus` for deep architecture and consequential review;
- `fable` only for long-horizon autonomous work.

Claude Code checks each request against the organization's `availableModels` and effort limits. When a family is blocked, Claude Code substitutes a permitted family version or the inherited session model. The plugin instructs Claude to report that substitution rather than claiming the requested route ran.

## Security behavior

Both plugins register a `PreToolUse` hook for Bash that denies commands containing a standalone `sudo` executable. The hook does not approve any other command, change the normal permission flow, or grant `bypassPermissions`.
