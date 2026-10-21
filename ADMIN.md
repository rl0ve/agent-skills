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
    "work-router@rl0ve-agent-skills": true,
    "ui-router@rl0ve-agent-skills": true,
    "natural-writing@rl0ve-agent-skills": true,
    "ui-walkthrough-video@rl0ve-agent-skills": true,
    "capability-storyboard@rl0ve-agent-skills": true,
    "deck-builder@rl0ve-agent-skills": true,
    "clear-assessment-guides@rl0ve-agent-skills": true
  }
}
```

If `strictKnownMarketplaces` is enforced, the approved repository or internal Git host must also appear in that allowlist. A local ZIP alone cannot override the policy.

Enable only the plugins your organization wants; the list above is the full set.

## ChatGPT and Codex workspace import

Checked October 20, 2026. A ChatGPT workspace admin can import this repository directly
([OpenAI](https://help.openai.com/articles/20001504)):

1. Admin Console, select the workspace, open **Plugins**, then **Add**, **Import marketplace**.
2. **Source:** the repository URL only (no branch or folder URL). Leave **Path** empty;
   both `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` sit at
   the root.
3. **Branch, tag, or commit:** a branch receives future commits; a fixed commit stays put.
4. Authorize GitHub access with an account that can read the repository.
5. Review import results, then set each plugin's **Installation policy** (Available or
   Installed per role).

Import processes every valid plugin without a per-plugin approval step, and daily sync
can add new ones. The repository's `"installation": "AVAILABLE"` values are **not**
applied; workspace settings control installation. Plugin-bundled hooks (the routers'
`block_sudo`) stay inactive in Codex until each user reviews and trusts them.

## Model policy

The AI router requests family aliases from subagents:

- `haiku` for narrow read-only scouting, plus an opt-in, untested `haiku-builder` for
  mechanical edits that runs only when a user or routing override names it. `haiku`
  is Haiku 5.5 only on the Anthropic API with Claude Code 2.1.293+; Bedrock, Vertex and
  Foundry resolve it to Haiku 4.5;
- `sonnet` for routine implementation;
- `opus` for deep architecture and consequential review;
- `fable` only for long-horizon autonomous work.

Claude Code checks each request against the organization's `availableModels` and effort limits. When a family is blocked, Claude Code substitutes a permitted family version or the inherited session model. The plugin instructs Claude to report that substitution rather than claiming the requested route ran.

## Security behavior

Both plugins register a `PreToolUse` hook for Bash that denies commands containing a standalone `sudo` executable. The hook does not approve any other command, change the normal permission flow, or grant `bypassPermissions`.
