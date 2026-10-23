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

1. Resolve the user's required model, family, revision and effort before selecting a
   fallback. Organization limits still apply; neither rule cancels the other.
2. Use the requested configuration when supported and permitted. A family preference
   can accept its newest permitted revision only when no exact revision is required.
3. For an unconstrained Fable preference, consider permitted Opus for deep judgment
   or Sonnet for bounded implementation. An inherited session model is another option
   only when it meets the user's requirements and the task's acceptance conditions.
4. Report a host-applied effort cap or substitution as the actual configuration.
   A lower level can be a fallback for task-appropriate effort; it does not satisfy
   an explicitly required level. Do not dispatch work whose required configuration
   is unavailable. Explain the constraint and offer a permissible task-only exception
   when useful; preserve the requirement until the user changes it.
5. State the fallback or unmet requirement once. Continue compatible authorized work
   where possible, without repeatedly asking the user to fight company policy.

Check current [model configuration and managed effort limits](https://code.claude.com/docs/en/model-config)
before treating a model alias or requested effort as effective state.

For team rollout, give the administrator the marketplace repository plus the desired `enabledPlugins` entries. Keep model allowlists and effort policy in managed settings, not inside the plugin.
