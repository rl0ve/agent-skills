# The brand pack

A `brand.json` is everything this skill needs to know about one organisation's PowerPoint template.
It is the whole reason the skill is brand-agnostic: swap the pack, build a different company's decks
with the same engineering.

Generate a starter with:

```bash
python3 scripts/make_brand_pack.py corporate.pptx --list-layouts
python3 scripts/make_brand_pack.py corporate.pptx \
  --grid-from "NAME OF A PLAIN ONE-COLUMN CONTENT LAYOUT" --out brand/brand.json
```

## Schema

```jsonc
{
  // Every value below is an illustrative placeholder. Your own numbers come
  // from make_brand_pack.py reading your template.
  "template": {
    "build_base": "brand/build_base.pptx",  // the file you actually build from
    "slide_w_in": 13.333,                   // 16:9 widescreen, the usual default
    "slide_h_in": 7.5,
    "master_count": 2,
    "layout_count": 40
  },

  "typography": {
    "theme_fonts": { "major": "<theme heading font>", "minor": "<theme body font>" },
    "min_body_pt": 14
  },

  // The theme colour scheme, read straight from your template.
  // dk2 is very often the flat dark background colour.
  "palette": {
    "dk1": "#000000",  "lt1": "#FFFFFF",
    "dk2": "#1A1A1A",  "lt2": "#EEEEEE",
    "accent1": "#AA0000", "accent2": "#BB6600", "accent3": "#00AAAA",
    "accent4": "#0066BB", "accent5": "#663399", "accent6": "#448844",
    "hlink": "#0066CC", "folHlink": "#663399"
  },

  // Measured from ONE layout you nominate. Check it by eye.
  "grid": {
    "slide_w_in": 13.333,
    "slide_h_in": 7.5,
    "measured_from_layout": "<the layout you passed to --grid-from>",
    "title": { "x_in": 0.50, "y_in": 0.40, "w_in": 11.00, "h_in": 0.90 },
    "body":  { "x_in": 0.50, "y_in": 1.50, "w_in": 11.00, "h_in": 0.40 },
    "left_edge_in": 0.50
  },

  // Space content must not cover. Usually the logo.
  "reserved_zones": [
    { "name": "<shape name from the master>",
      "x_in": 11.90, "y_in": 0.45, "w_in": 0.90, "h_in": 0.30 }
  ],

  "modes": {
    "light":      { "layout_hints": [], "set_background": false },
    "dark_flat":  { "layout_hints": [], "background_hex": "#1A1A1A", "set_background": true },
    "dark_decorated": {
      "layout_hints": ["<layouts that carry their own background picture>"],
      "set_background": false
    }
  },

  // Every master and every layout, with placeholder types and whether the
  // layout carries a full-bleed background picture.
  "masters": [ { "index": 0, "name": "", "layouts": [ /* ... */ ] } ]
}
```

## What the generator gets right on its own

Layout and master enumeration, slide dimensions, the theme palette, the theme fonts, and which
layouts carry a full-bleed background picture. These are read directly out of the file, so trust
them.

The layout inventory is the most valuable part, because it is the one thing nobody maintains by
hand. On one real corporate template the generator found roughly seven times as many decorated
layouts as the hand-written list that preceded it. Hand-maintained inventories go stale silently.

## What needs a human

**The alignment grid.** It is measured from a single layout you nominate with `--grid-from`. Pick a
plain one-column content layout, not a title slide or a photo layout. Then check the numbers against
a rendered slide. Placeholder bounds are a good proxy for the grid, not a definition of it.

**Reserved zones.** The generator lists picture shapes on the first master, which is where a logo
normally lives, but it cannot tell a logo from a decorative flourish. Confirm each one, delete the
rest, and add any zone the template owns that is not a picture: page numbers, footer rules,
corner furniture.

**Mode layout hints.** `dark_decorated` is populated automatically. `light` and `dark_flat` are left
empty because layout naming is a house convention the generator cannot infer. Fill in the handful of
layout names you actually build on.

**`build_base`.** Prefer a stripped copy of the corporate template with few or no slides in it. A
full template carrying a couple of hundred slides makes package-name collisions much worse (see the
duplicate-entry section in `SKILL.md`).

**Fonts on the build machine.** `theme_fonts` records what the template asks for, not what is
installed. If the font is missing, PowerPoint and LibreOffice will substitute and your rendered
review images will not match what a colleague sees.

## Keeping it honest

Anything the generator could not determine is written as `null`, so the gaps are visible rather than
guessed. Leave a value `null` rather than inventing one: a wrong constant in a brand pack is worse
than a missing one, because every later slide inherits it silently.

Regenerate the pack when the corporate template is updated. Layout names change, and a build script
pinned to an old name fails with `Layout not found` at generation time rather than at review time.
