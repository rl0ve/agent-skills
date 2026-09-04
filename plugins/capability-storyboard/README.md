# Capability Storyboard

A storyboard format for showing what a product can do, to an audience that does not already know it.

Not a slide deck and not a step-by-step walkthrough. A small number of **Acts**, each proving one
capability, all riding on the same running example so the audience keeps one thread. Every scene is
one screen mockup, the literal words the presenter says, and terse director's notes including the
things not to do live.

The output is a single self-contained HTML file. No build step, no external JS. It opens in a
browser and embeds as an artifact.

## Install

```bash
# Claude Code
claude plugin marketplace add rl0ve/agent-skills
claude plugin install capability-storyboard@rl0ve-agent-skills

# Codex
codex plugin marketplace add rl0ve/agent-skills
codex plugin add capability-storyboard@rl0ve-agent-skills
```

## What is in it

| File | What it is |
|---|---|
| `skills/capability-storyboard/SKILL.md` | The format, and sixteen lessons that each ended a specific defect |
| `references/template.html` | A working skeleton with the mechanics wired up and placeholder content |
| `references/example-full.html` | A finished nine-scene board to lift components out of |

## The example

`example-full.html` follows an airline recovering from a weather cancellation, across three
invented products: a web ops console, a desktop crew tool, and a passenger phone app. The scenario
and the products are made up, so nothing in it needs sanitising before you borrow from it.

It exists to be raided. Components you can lift directly:

- a stats strip and a data grid with status pills
- a modal dialog over a dimmed screen
- a stage-canvas process diagram
- a closing slide with a thumbnail wall
- four chrome variants: light browser, dark developer tool, light business app, and a phone
- three reading modes over one dataset (Narrative, Strip, Flow)
- a masthead stat line computed from the scene data rather than typed
- an `@scene:viewkey` resolver, so a cross-reference in copy renders as a live scene number and
  never goes stale when scenes are renumbered

## The two rules that matter most

**Never let two different tools look like the same screen.** If the products exist and you can
reach them, read their actual computed CSS rather than inventing a palette. Interchangeable-looking
mockups are the fastest way to lose a reviewer who knows the products.

**Verify by rendering, not by reading the diff.** Serve the file and assert: zero overflow in every
mockup body, zero clipped headlines in strip view, zero unresolved `@scene:` tokens, every view mode
toggles. Building the example board in this repo turned up two real layout bugs that were invisible
in the source and obvious on screen.

## License

MIT.
