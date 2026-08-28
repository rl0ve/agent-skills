---
name: check-routing-setup
description: Inspect Claude Code version, installed router components, and visible workspace constraints before changing routing policy. Run only when the user explicitly asks to check or troubleshoot the router setup.
disable-model-invocation: true
---

# Check Routing Setup

Perform a read-only check.

1. Run `claude --version`.
2. Run `claude plugin list --json` and confirm this plugin is enabled.
3. Run `claude agents` and confirm the router agents are listed.
4. Do not print tokens, credentials, environment secrets, or complete settings files.
5. Ask the user to open `/model` or `/effort` only when model visibility cannot be verified another way.
6. Separate facts into `verified`, `organization-controlled`, and `not yet verified`.
7. Recommend an upgrade only when the installed client lacks a feature the user actually needs.

Never modify user, project, local, or managed settings during this check.
