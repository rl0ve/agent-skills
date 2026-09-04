# Layout repertoire

A deck where most content slides share one pattern reads as repetitive no matter how good the
content is. The usual offender is a card grid used for everything.

**Use at least four distinct patterns across the content slides, and let no single pattern appear
more than two or three times in a deck of a dozen or so.** Map every slide to a pattern before you
build, and look at the map. If one column of that map is nearly all the same word, fix it then,
not after the review.

## The patterns

| Pattern | Best for | Shape of it |
|---|---|---|
| **Two-panel comparison** | Before and after, linear versus non-linear, in-house versus platform | Side-by-side panels with distinct border or fill treatments |
| **Vertical flow diagram** | Architecture, data flow, an execution pipeline | Stacked boxes joined by thin connectors |
| **Numbered card grid** | A glossary, concept definitions, a capability overview | 2×3 cards. Use **once** per deck, and no more |
| **Two-column text comparison** | Feature-by-feature, traditional versus modern | Left column muted, right column bold, a divider between |
| **Parallel tracks** | Change control, deployment, migration paths | Two horizontal rows of step boxes with a connector |
| **Rows with accent blocks** | Governance items, guardrails, a checklist | A small coloured square, then title and description per row |
| **Stacked layers with an accent bar** | Competitive positioning, a market landscape | Full-width layers, the emphasised one as a bar at the bottom |
| **One versus many** | Build versus buy, consolidation | A single large block against a grid of small ones |
| **Flow columns with arrows** | Process stages, day-two operations | Three connected boxes with real arrow shapes between them |
| **Table rows, alternating fills** | A use-case matrix, a feature matrix | A header row plus data rows, no card borders |
| **Labelled rows** | Key takeaways, a summary, "why X" | Coloured labels left, descriptions right, dividers between |

## Graphic elements that break up text

Use these to give a text-heavy slide structure. None of them is decoration for its own sake; each
one carries a relationship the text would otherwise have to state.

- **Arrow shapes** between flow stages. Use a real arrow shape (`MSO_SHAPE.RIGHT_ARROW`, shape id
  13), never a text chevron such as `›`, `»`, or `▶`, which render inconsistently across
  environments and substitute badly when a font is missing. Around 0.22in square works for an inline
  stage connector. Fill with a neutral grey for a plain hand-off, or with the stage colour when the
  hand-off is the point. LibreOffice may render an arrow as a flat rectangle; that is a renderer
  limitation, not a bug in your deck.
- **Accent blocks.** Small squares, roughly 0.4in, as anchors at the left of list rows.
- **Top accent bars.** A thin bar, roughly 0.06in tall and the full width of a card, instead of a
  border around the card. Lighter and less boxy.
- **Connector lines.** Thin rectangles, roughly 0.02in tall, between architectural boxes.
- **Split composition.** One large block against a grid of small ones, to show consolidation.
- **Alternating row fills.** Two close shades for table-like layouts, so rows read without borders.

## Column alignment

Small misalignments are what make a hand-built slide look hand-built.

- Align every column top to the same `y`. Never let one column start lower than its neighbours.
- Align equivalent boxes across columns to identical `y` values, not merely similar ones.
- Keep the gap between columns consistent, around 0.14in to 0.20in. When arrows sit between columns,
  the arrow fills that gap and the gap sets the arrow size.

## Slide patterns worth reaching for

Repeated case-study frames. Annotated screenshots. Layered platform stories. Two-column
comparisons. Three-tier models. A data-proof slide carrying exactly one takeaway. Ecosystem maps
drawn in the house iconography.
