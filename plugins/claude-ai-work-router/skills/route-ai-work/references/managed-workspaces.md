# Managed workspace boundaries

Use this reference when a company controls Claude Code settings.

## The plugin can

- request a model family and effort level in plugin-shipped subagents;
- keep work in the current parent session;
- recommend a one-time `/model` or `/effort` change;
- preserve one-writer and bounded-context rules;
- report when Claude Code substitutes a permitted model.

## The plugin cannot

- add a model to an organization's `availableModels` allowlist;
- raise an organization effort cap;
- override a server-managed default;
- bypass `strictKnownMarketplaces` or a blocked marketplace;
- force Fable availability, usage-credit consent, or provider deployment;
- silently change the user's persistent model setting.

## Fallback order

1. Use the requested family when permitted.
2. Accept Claude Code's newest permitted version within that family.
3. For unavailable Fable, use Opus for deep judgment or Sonnet for routine implementation.
4. If the organization blocks the family, inherit the session model and keep the task boundary intact.
5. State the fallback once. Do not repeatedly ask the user to fight company policy.

For team rollout, give the administrator the marketplace repository plus the desired `enabledPlugins` entries. Keep model allowlists and effort policy in managed settings, not inside the plugin.
