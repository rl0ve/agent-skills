# UI Router

Claude Code-native companion to the Codex Design Router.

It preserves the original named skill universe—including Taste, Hallmark, Interface Design, Impeccable, Emil, Jakub, Meng, Addy, ibelick, shadcn, systems extraction, image-to-code, writing, and marketing skills—while keeping two truths separate:

1. the canonical researched chain;
2. the chain actually available in the current Claude Code environment.

The plugin contributes:

- `/ui-router:route-ui-work`, an auto-invocable UI routing skill;
- `/ui-router:install-ui-stack`, a manual, plan-first optional installer;
- read-only scout and critic agents plus one Sonnet UI builder;
- the complete routing catalog and quality references;
- the two polished UI reference cards;
- a one-editor writing route that hands product or brand constraints to Natural Writing for the final prose pass;
- a `PreToolUse` hook that blocks `sudo`.

The router does not silently install third-party skills. The bundled installer refuses root and `sudo`, prints sources and commands before execution, and installs only explicit skills or curated profiles.

Claude Code's official `frontend-design` plugin is a strong installed fallback, but it does not erase the canonical named lead when Taste, Hallmark, or Interface Design is the researched fit.

For copy, the router does not stack humanizers. It selects one product/UX or marketing semantics owner only when needed, then uses the companion `natural-writing` plugin as the sole final editor. Verify that companion separately; package presence is not installation evidence. If it is unavailable, select exactly one documented fallback.


## Package parity

Version 1.2.0 mirrors Codex Design Router 1.3.1's active Natural Writing route. Install or enable the companion Natural Writing 1.0.1 plugin separately, reload Claude Code, then test both an expected writing trigger and explicit invocation.
