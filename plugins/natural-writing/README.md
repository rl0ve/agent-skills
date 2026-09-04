# Natural Writing for Claude Code

Natural Writing is a voice-preserving editor and writing router. It handles drafts, rewrites, diagnosis, voice matching, product copy, documentation, executive prose, and cleanup of common assistant-like writing patterns.

The plugin contributes `/natural-writing:natural-writing`, an auto-invocable skill selected by semantic intent rather than a fixed keyword list. It covers explicit editing requests and implicit equivalents: a draft that should sound more like the author, a note that needs to be ready to send, stiff interface copy, a memo that feels synthetic, or source notes that need reader-ready prose. It also covers Claude-specific residue such as ritual validation, prompt echoes, coaching theater, taxonomy reflexes, fake contrasts, excessive headings, and generic endings.

Its operating rules are intentionally conservative:

- preserve supported facts, qualifications, terminology, identifiers, formatting, and author voice;
- make the minimum effective edit, and return the draft unchanged when it already passes;
- revise meaning and structure before surface wording;
- never optimize for detector evasion;
- use one context-holding writer, with an optional read-only reviewer for consequential work.

## Layout

```
skills/natural-writing/
  SKILL.md                         routing, the layered edit, output discipline
  eval.md                          27 checks to run before returning anything
  references/pattern-catalog.md    every written-prose pattern by family, a worked example per row
  references/spoken-register.md    talk tracks and narration: rules, patterns with examples, checks
  references/voice-and-register.md voice matching and the written registers
  references/model-routing.md      who writes, who reviews
  references/sources.md            provenance and maintenance rules
  scripts/lint_natural_writing.py  deterministic first pass; --spoken, --set; ROW_FOR maps checks to rows
  tests/                           linter tests, structure tests, forward-test cases, trigger cases
```

Each reference has one job; SKILL.md's reference map says which to read when.

## Running the checks

```bash
# one draft
python3 skills/natural-writing/scripts/lint_natural_writing.py DRAFT.md

# a talk track or demo script
python3 skills/natural-writing/scripts/lint_natural_writing.py --spoken SCRIPT.md

# many pieces edited to one standard, blank-line separated
python3 skills/natural-writing/scripts/lint_natural_writing.py --set PIECES.md

# unit tests
cd skills/natural-writing && python3 -m unittest discover -s tests
```

Every match is a review prompt, not a verdict.

The bundled icon is at `assets/natural-writing-icon.png`.

## Quick test

```bash
claude --plugin-dir .
```

Then try:

```text
Tighten this note for the CFO. Keep every number and qualification, and keep it sounding like me: ...
```
