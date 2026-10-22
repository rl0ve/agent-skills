<!-- work-router override:begin -->
## My Codex routing override

This enabled override applies to Codex only and supersedes generic routing defaults.
Keep the underlying route tables unchanged.

- enabled: true
- scope: all projects and chats loading these Codex user instructions
- priorities: accuracy > latency > credit_conservation
- credit_policy: use_available
- model_constraint: gpt-6-astra
- effort: task_appropriate
- expires: manual

Apply the model constraint to parent and delegated model work. Use a compatible
parent or an explicitly configured supported child; do not silently substitute a
fixed-model profile. Report an unavailable model rather than claiming compatibility.
Select useful depth, not token burn. This is subject to host and organization rules
and does not authorize purchases, paid APIs, extra usage, reset redemption, or a
different service tier. Never claim it changed a running model or tier.

To disable it, set enabled to false or remove this bounded block on my request. A
request to change priorities alone leaves the model constraint in place. Keep the
canonical selected profile consistent when I request a portable preference change;
do not turn a task-only exception into a global change.
<!-- work-router override:end -->
