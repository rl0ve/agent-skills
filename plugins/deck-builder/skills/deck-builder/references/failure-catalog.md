# What actually goes wrong in a generated deck

Every entry here is a defect you cannot see by reading the build script. Each one names how it
looks, why it happens, whether a tool can detect it, and what to do.

The detectable ones have check codes. Run them with:

```bash
python3 scripts/check_deck.py deck.pptx --brand brand/brand.json
```

Exit code 0 means clean or notes only, 1 means at least one warning, 2 means at least one failure.

---

## The package will not open

**`PKG001` — PowerPoint shows a repair dialog on every open**

*Looks like:* "PowerPoint found a problem with content in deck.pptx." The deck usually opens fine
after repair, so it reads as a corrupt file and is really a packaging artefact.

*Why:* `python-pptx` cannot always remove a slide part from the package zip. Deleting a slide may
only remove it from the slide ID list, leaving `slide1.xml` in the archive. When your build writes
its own `slide1.xml`, both entries coexist.

*Whether it bites you depends on your `python-pptx` version and how the stub slide was removed.* On
1.0.2 with `drop_rel` it does not happen. Do not assume either way, check.

*Fix:* `python3 scripts/dedupe_pptx_zip.py deck.pptx`. Prefer a build base with few or no slides;
starting from a full template with two hundred slides turns two colliding entries into dozens.

*Note:* a duplicated package often will not parse at all, so `check_deck.py` runs this check first
and on its own. If it fires, fix it and re-run before trusting any other result.

---

## Text does not fit

**`FIT001` — text overflows a fixed box**

*Looks like:* a sentence cut off mid-word, or copy running out past the bottom of a card.

*Why:* the box was sized for the text the author imagined, not the text that arrived. Almost always
in compact elements: stage titles, right-rail headings, footer chips, card titles. Body copy has
slack; a 0.4in label does not.

*Fix:* preflight rather than shrink at the end. You know the box bounds, the font, and the string
before you write a single character, so check whether it fits and size accordingly. Shrink only as
far as needed, and protect the title hierarchy.

*This check is an estimate.* It wraps text by character count against an average glyph width. It is
reliable for text that badly overruns and unreliable within about 15% of the boundary. Treat it as
"go and look at that slide", never as a verdict.

**`FIT003` — the shape grows instead**

*Looks like:* nothing, until the box silently renders taller than you drew it and either runs off
the slide or sits on top of its neighbour.

*Why:* `MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT`, which is the default for a text box created with
`add_textbox`. PowerPoint honours the text and discards your geometry.

*Fix:* decide which one is authoritative. Either set `auto_size = NONE` and size the text to the
box, or accept the growth and stop treating the box height as a layout constraint. Do not leave it
ambiguous, because the deck will look right on the machine that built it and wrong on the projector.

**`FIT002` — text below the readable floor**

*Looks like:* fine on a laptop, illegible from the fourth row.

*Why:* an emergency shrink that nobody revisited.

*Fix:* 14pt is the floor for body copy. If content will not fit at 14pt, the slide has too much
content. Split it.

---

## Things sit on top of other things

**`GEO002` — an opaque shape covers text beneath it**

*Looks like:* text that is simply not there, with no error anywhere.

*Why:* a panel, card background, or image added after the text, so it wins on z-order. Common when
a background is added late in a build to "tidy up" a slide.

*Fix:* move one of them, or add the background before the text. Treat this as a hard failure. A
covered word is indistinguishable from a missing word to a reader.

**`GEO003` — a shape intrudes on a reserved zone**

*Looks like:* a chip or label tucked into the top-right corner, under the logo.

*Why:* the top-right corner looks empty in your build script, because the logo comes from the master
and not from your slide.

*Fix:* record reserved zones in `brand.json` and keep content out of them. The check tests the
extent the text actually reaches, not the box bounds, so a wide left-aligned title whose words stop
short of the corner is correctly left alone. Template placeholders are exempt: the template is
allowed to occupy its own space.

**`GEO001` — a shape runs off the slide**

*Why:* usually arithmetic, occasionally `FIT003` growth.

*Fix:* it is a bug. Nothing off-canvas is intentional.

**`GEO004` — near-miss alignment**

*Looks like:* a slide that feels hand-made without anyone being able to say why.

*Why:* two shapes at 1.60in and 1.63in. Nobody sees the number; everybody sees the wobble.

*Fix:* align tops exactly, or offset them enough to read as deliberate. A 0.03in gap is neither.

---

## Every slide looks the same

**`VAR001`, `VAR002` — layout monotony**

*Looks like:* a competent deck that is boring to sit through, usually a card grid repeated eleven
times.

*Why:* the first layout that worked became the default, and nothing forced a second choice.

*Fix:* at least four distinct patterns across the content slides, and no single pattern more than
two or three times. Map every slide to a pattern before building and look at that map.
`references/layout-repertoire.md` has eleven patterns to choose from.

---

## The template shows through

**`PLC002` — helper text still present**

*Looks like:* "Click to edit Master title style" on a delivered slide.

*Why:* a placeholder was styled but never filled.

*Fix:* fill it or remove it. This is a hard failure; it is the single most embarrassing thing a
generated deck can do.

**`PLC001` — empty placeholders inherited from the layout**

*Looks like:* prompt text in the editing view. **It does not render in presentation or print**,
which is why this is a note and not a warning.

*Why:* `add_slide(layout)` copies every one of the layout's placeholders into the slide. A
template-canvas build that draws its own text boxes inherits all of them, empty.

*Fix:* only if the deck will be edited by someone else. Drop the element, or pick a layout with
fewer placeholders.

---

## Content disappears in a rebuild

**Not detectable from one deck. Needs the original.**

*Looks like:* a condensed deck that reads well and is missing the one statistic the person who
commissioned it cared about.

*Why:* rebuilding for a new structure means writing a new script. Anything not explicitly coded into
it is gone, and nothing errors.

*Detect:*

```bash
python3 scripts/diff_deck_content.py original.pptx rebuilt.pptx
```

It reports numbers, multi-word names, and whole sentences that were in the original and are nowhere
in the rebuild. Matching is whole-deck, so content that merely moved between slides is not reported,
and a sentence counts as surviving if most of its distinctive words do, so ordinary rewording is not
reported either.

*Fix:* confirm each dropped item was cut deliberately, and present the list to whoever supplied the
content. The temptation when condensing is to simplify hard. Resist it: they gave you that content
because it mattered. When several slides merge into one, everything from all of them has to land
somewhere unless someone said to cut it.

Things that vanish most often: stat bars when a layout changes, explanatory subtext when cards
merge, "why this matters" context when the focus shifts to features, and named framing headlines
replaced by generic titles.

---

## What no checker can tell you

Whether the deck is any good. Whether the argument lands, whether the order is right, whether a
slide earns its place. The checks above buy you the attention to spend on that, by making the
mechanical failures cheap to find. They do not replace exporting the slides and looking at them.
