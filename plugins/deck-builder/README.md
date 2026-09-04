# Deck Builder

Build PowerPoint decks with `python-pptx`, then verify them by rendering slides and running
automated checks rather than by re-reading the build script.

The value here is the checking. A build script that reads correctly produces broken decks all the
time: text that overflows, a panel covering the words underneath it, a package PowerPoint refuses to
open, a condensed deck missing the one statistic that mattered. Eleven of those failures are
detected automatically, with an explanation of each in `references/failure-catalog.md`.

The brand is configuration, not code. This plugin ships no palette, no logo, and no template; a
generator reads your own corporate template and writes the pack the checks use.

## Install

```bash
# Claude Code
claude plugin marketplace add rl0ve/agent-skills
claude plugin install deck-builder@rl0ve-agent-skills

# Codex
codex plugin marketplace add rl0ve/agent-skills
codex plugin add deck-builder@rl0ve-agent-skills
```

Requires `python-pptx` and `lxml`. Optional: `pywin32` (Windows screenshots), `pypdf` (macOS
screenshots).

## Start here

```bash
python3 scripts/make_brand_pack.py corporate.pptx --list-layouts
python3 scripts/make_brand_pack.py corporate.pptx \
  --grid-from "NAME OF A PLAIN ONE-COLUMN CONTENT LAYOUT" --out brand/brand.json
```

That reports every slide master and layout, the slide size, the theme palette and fonts, which
layouts carry a decorated background, and a measured alignment grid and logo zone. Run against a
real corporate template it reproduced, to the thousandth of an inch, a set of constants that had
until then been maintained by hand, and found several times as many decorated layouts as the
hand-written list knew about.

## The problems it actually solves

**Half your template is invisible.** `prs.slide_layouts` returns only the *first* slide master.
Templates routinely put dark-mode and alternate layouts on a second one, so any code that iterates
`prs.slide_layouts` raises `Layout not found` on layouts that are plainly there. The skill carries
the multi-master lookup.

**Setting a background deletes the design.** Decorated layouts carry a full-bleed picture. Override
the slide background and the decoration silently disappears. The brand pack lists exactly which
layouts this applies to, so you never have to guess.

**The repair dialog.** `python-pptx` cannot always drop a slide part from the package zip, so a
stale `slide1.xml` and your new one can both end up in the archive, and PowerPoint reports a corrupt
file on every open. `dedupe_pptx_zip.py --check` tells you in one second whether your deck has it.
(It depends on your `python-pptx` version and how the stub slide was removed. On 1.0.2 with
`drop_rel` it does not happen, so the tool checks rather than assuming.)

**macOS screenshot export lies.** AppleScript `save as picture` reports success and writes nothing.
The skill documents the PDF-split-and-convert pipeline that works, so nobody spends an afternoon
debugging a silent no-op.

**Condensing a deck drops content.** Rebuilding for a new structure silently loses whatever was not
explicitly coded into the new script: stats, proof points, framing language. Step 11 is a
slide-by-slide content audit against the original.

**Every slide looks the same.** `references/layout-repertoire.md` has eleven patterns, a hard rule
of at least four per deck, and the graphic elements that break up text without becoming decoration.

## What is in it

| | |
|---|---|
| `check_deck.py` | **The check suite.** Eleven checks, severity-ranked, `--json`, useful exit codes |
| `diff_deck_content.py` | What a rebuild dropped: numbers, names, and whole sentences |
| `dedupe_pptx_zip.py` | Detect and fix the duplicate-entry repair dialog |
| `make_brand_pack.py` | Read any corporate template, emit `brand.json` |
| `inspect_template_layouts.py` | Exact layout names, placeholder types, and bounds |
| `start_template_deck.py` | A deterministic template-backed starting deck |
| `validate_template_deck.py` | Layout discipline against the brand template |
| `report_pptx_weight.py` | Which package parts are making the file large |
| `ooxml_effects.py` | Gradients, shadows, glows, rounded corners via `lxml` |
| `export_powerpoint_screenshots_{mac,win32}.py` | Ground-truth renders from real PowerPoint |
| `references/failure-catalog.md` | Every failure: how it looks, why, how to detect, what to do |
| `references/layout-repertoire.md` | Eleven layout patterns, and alignment discipline |
| `references/brand-pack.md` | The `brand.json` schema and its limits |
| `references/slide-spec-format.md` | Plan the deck before placing objects |
| `references/deck-archetypes.md` | Pick a repeatable deck shape |
| `references/visual-complexity-modes.md` | Pick a level of visual ambition |

## License

MIT.
