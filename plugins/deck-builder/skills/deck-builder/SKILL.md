---
name: deck-builder
description: Build, edit, and quality-check PowerPoint decks (.pptx) with python-pptx, and verify them by rendering slides and running automated checks rather than by re-reading the build script. Use when building a presentation from a brief or narrative, restyling or condensing an existing deck, or producing on-brand output from a corporate template. Also use to diagnose a specific deck defect: a repair dialog on open, text overflowing or cut off, a shape covering text, content sitting off the slide or under the logo, every slide using the same layout, text too small to read, or a rebuild that silently dropped statistics and proof points from the original.
---

# Deck Builder

Two things make a generated deck good, and neither is the build script.

**Build against what the template actually contains**, not what you assume it contains. Half of a
real template is invisible to the obvious API call.

**Verify by looking, and let the checks tell you where to look.** A build script that reads
correctly produces broken decks all the time. Nothing here is confirmed until slides have been
rendered and inspected.

## The check suite

Run this after every build, and again after every fix:

```bash
python3 scripts/check_deck.py deck.pptx --brand brand/brand.json
```

| Code | Catches | Severity |
|---|---|---|
| `PKG001` | Duplicate package entries, the PowerPoint repair dialog | FAIL |
| `PLC002` | Template helper text left in a delivered slide | FAIL |
| `GEO002` | An opaque shape covering text beneath it | FAIL |
| `GEO003` | A shape intruding on a reserved zone, usually the logo | FAIL |
| `FIT001` | Text that will overflow a fixed box (estimated) | WARN |
| `FIT003` | A shape set to grow, so it will not stay where you drew it | WARN |
| `FIT002` | Text below the readable point-size floor | WARN |
| `GEO001` | A shape running off the slide edge | WARN |
| `VAR001` `VAR002` | Layout monotony across content slides | WARN |
| `GEO004` | Near-miss alignment, the 0.03in wobble | NOTE |
| `PLC001` | Empty placeholders inherited from the layout | NOTE |

Exit 0 clean or notes only, 1 a warning, 2 a failure, 3 unreadable. `--json` for machine output,
`--only FIT,GEO` for one family, `--min-pt` and `--max-same-layout` to set thresholds.

Two properties worth knowing. `FIT001` is an **estimate**: it wraps text by character count against
an average glyph width, so it is reliable for text that badly overruns and unreadable within about
15% of the boundary. Confirm it against a rendered slide. And `PKG001` runs first and alone, because
a duplicated package often will not parse at all.

`references/failure-catalog.md` explains every code: how it looks, why it happens, and what to do.

For a rebuild or a condense, the checks above cannot help, because the defect is content that is no
longer there. That needs both decks:

```bash
python3 scripts/diff_deck_content.py original.pptx rebuilt.pptx
```

It reports numbers, multi-word names, and whole sentences present in the original and absent from
the rebuild. Content that merely moved between slides is not reported, and ordinary rewording is
not reported, so what remains is worth reading.

## Build rules

### Find layouts across ALL masters

`prs.slide_layouts` returns only the layouts of the **first** master. Templates routinely put dark
mode, alternate colourways, or event layouts on a second one, so code that iterates
`prs.slide_layouts` raises `ValueError: Layout not found` on layouts that are plainly in the file.

```python
def get_layout(prs, name):
    """Search every slide master for a layout by name."""
    for master in prs.slide_masters:
        for layout in master.slide_layouts:
            if layout.name == name:
                return layout
    raise ValueError(f"Layout not found: {name!r}")
```

`scripts/inspect_template_layouts.py` prints exact layout names, placeholder types, and bounds.

### Never override a layout's own background

Decorated layouts carry a full-bleed background picture. Setting an explicit slide background hides
the exact decoration you picked that layout for, and nothing warns you.
`scripts/make_brand_pack.py` lists which layouts this applies to.

### Decide who owns the geometry

A text box created with `add_textbox` defaults to `SHAPE_TO_FIT_TEXT`: PowerPoint honours the text
and discards your height. Either set `auto_size = NONE` and size the text to the box, or accept the
growth and stop treating the box height as a constraint. Leaving it ambiguous is how a deck looks
right on the machine that built it and wrong on the projector. This is `FIT003`.

### Preflight text fit, do not shrink at the end

The layout, the font, and the string are all known before you write a character. Check whether it
fits and size accordingly. Preflight short labels separately from body copy: a 0.4in stage title
overflows long before a paragraph does, and body copy has slack that labels do not.

### Keep out of reserved zones

The top-right corner looks empty in your build script because the logo comes from the master, not
your slide. Record reserved zones in `brand.json` and check against them. This is `GEO003`.

### Draw backgrounds before text, not after

Adding a panel late to tidy a slide puts it on top by z-order, and a covered word is
indistinguishable from a missing word. This is `GEO002`.

### Use at least four layout patterns

No single pattern more than two or three times across the content slides. Map every slide to a
pattern before building and look at the map: if one column of it is nearly all the same word, fix it
then. `references/layout-repertoire.md` has eleven patterns and the graphic elements that break up
text without becoming decoration.

### Escalate to lxml only when stuck

`python-pptx` is the authoring engine. Reach for `lxml` only for effects it cannot express:
gradients, shadows, glows, rounded picture corners. `scripts/ooxml_effects.py` has helpers. Keep the
XML narrow and behind named functions, not mixed into content code.

## Workflow

1. **Brand pack.** Generate or locate `brand.json` for the template you are building on. See
   `references/brand-pack.md`. It supplies the reserved zones and point-size floor the checks use.
2. **Confirm the visual mode** with the user: light, flat dark, or the template's decorated dark
   layouts. Do not infer it from content type, do not mix modes in one deck, do not re-ask mid-build.
3. **Spec the deck before placing objects**: per slide the message, the evidence type, and the
   layout it maps to. `references/slide-spec-format.md`. Pick an archetype
   (`references/deck-archetypes.md`) and a level of ambition
   (`references/visual-complexity-modes.md`).
4. **Build.** Template-native where a slide maps onto an existing layout; template-canvas for a
   custom composition that still inherits the master; from scratch only when the user accepts losing
   the corporate master.
5. **Run `check_deck.py`.** Fix every FAIL. Triage the WARNs.
6. **Export slide images and look at them.** See below.
7. **Iterate, bounded.** Three passes. If problems remain, report them rather than looping.
8. **For a rebuild, run `diff_deck_content.py`** and present the dropped items for confirmation.
9. **Deliver** the `.pptx` and, where practical, the script that built it, so the deck can be
   rebuilt rather than hand-patched. Summarise assumptions, passes, and anything unresolved.

## Exporting slide images

| Platform | Tool | Fidelity |
|---|---|---|
| Windows | `scripts/export_powerpoint_screenshots_win32.py` (`pywin32`) | Real PowerPoint, ground truth |
| macOS | `scripts/export_powerpoint_screenshots_mac.py` (AppleScript) | Real PowerPoint, ground truth |
| Linux / none | LibreOffice headless, or `pdftoppm` via PDF | Approximate |

PowerPoint automation is for screenshots only, never for generation.

**macOS: the direct PNG export fails silently.** AppleScript `save as picture` reports success and
writes nothing. Do not debug it. Export to PDF, split with `pypdf` into one single-page PDF per
slide, then `sips -s format png Slide01.pdf --out Slide01.png` on each. `sips` only converts the
first page of a multi-page PDF, so the split is not optional.

On LibreOffice, separate real layout bugs from known render gaps before iterating: fonts substitute,
shadows and glows differ, and arrow shapes may render as plain rectangles.

## What to avoid

- Text-character chevrons (`›`, `»`, `▶`) as arrows. Use a real arrow shape; characters render
  inconsistently and substitute badly when a font is missing.
- Decorative title underlines, and body copy below 14pt.
- Shapes, lines, or accents placed over live text.
- Silently swapping a requested template-driven build for a blank-deck build.
- Proprietary or paid libraries as required dependencies, or anything needing .NET for routine use.

## Dependencies

Required: `python-pptx`, `lxml`. Optional: `pywin32` on Windows, `pypdf` on macOS, both only for
screenshot export. PowerPoint itself only for ground-truth rendering.

## What the checks cannot tell you

Whether the deck is any good: whether the argument lands, whether the order is right, whether a
slide earns its place. The checks buy you the attention to spend on that by making the mechanical
failures cheap to find. They do not replace looking at the slides.
