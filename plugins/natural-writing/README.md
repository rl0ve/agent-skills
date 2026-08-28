# Natural Writing for Claude Code

Natural Writing is a voice-preserving editor and writing router. It handles drafts, rewrites, diagnosis, voice matching, product copy, documentation, executive prose, and cleanup of common assistant-like writing patterns.

The plugin contributes `/natural-writing:natural-writing`, an auto-invocable skill selected by semantic intent rather than a fixed keyword list. It covers explicit editing requests and implicit equivalents: a draft that should sound more like the author, a note that needs to be ready to send, stiff interface copy, a memo that feels synthetic, or source notes that need reader-ready prose. It also covers Claude-specific residue such as ritual validation, prompt echoes, coaching theater, taxonomy reflexes, fake contrasts, excessive headings, and generic endings.

Its operating rules are intentionally conservative:

- preserve supported facts, qualifications, terminology, identifiers, formatting, and author voice;
- make the minimum effective edit;
- revise meaning and structure before surface wording;
- never optimize for detector evasion;
- use one context-holding writer, with an optional read-only reviewer for consequential work.

The bundled icon is at `assets/natural-writing-icon.png`.

## Quick test

```bash
claude --plugin-dir .
```

Then try:

```text
Humanize this executive email, remove the AI slop, and keep my voice: ...
```
