# Slide spec format

Provide (or infer) a slide spec like this before building PPTX:

## Deck metadata
- Audience:
- Goal:
- Tone: (external customer pitch | internal | exec brief)
- Archetype: (case-study system | executive narrative | product proof | platform architecture)
- Mode: light (default) | dark
- Visual ambition: minimal | standard | rich | showpiece
- Preferred media: mixed | diagrams | screenshots | charts | photos | icons
- Asset sourcing policy: existing local assets first | user-provided only | generation/source allowed | vector-only
- Slide-master policy: required | preferred | not required
- Build mode: template-native | template-canvas | freeform
- Deck system notes: (cover formula, recurring frame, section rhythm, repeatable slide types)
- Slide count:
- Source material: (template deck | existing deck | outline | none)
- Delivery goal: (pptx only | pptx + editable source)

## Slides
For each slide:
1. Title:
2. System role: (cover | section opener | repeatable body slide | proof slide | closer | outlier slide)
3. Slide type: (title | section | narrative diagram | comparison | timeline | metrics | screenshot)
4. Key message (one sentence):
5. Must-include elements: (bullets, diagram labels, metrics, callouts)
6. Primary medium: (native shapes | svg/vector | screenshot | chart | photo | hybrid)
7. Visual structure: (two-column, stacked layers, cards, ecosystem map, image-led, etc.)
8. Template/master match: (exact layout if known | clean template canvas | prebuilt template element | from scratch)
9. Placeholder policy: (fill native placeholders | remove unused placeholders | no large body/media placeholders allowed)
10. System notes: (what recurring frame, module, caption style, or diagram grammar must match the rest of the deck)
11. Brand notes: (light/dark, logo treatment, required emphasis color)
12. Notes (optional): speaker notes, assumptions, disclaimers

If the slide-master policy is `required`, avoid `from scratch` unless the user changes that requirement.
If the slide-master policy is `preferred`, note where the template is reused and where bespoke slides are justified.
If the build mode is `template-canvas`, choose a clean corporate layout and explicitly note that unused placeholders must not survive into the final slide.
If the archetype is `case-study system`, define the repeatable body-slide frame once and reuse it unless there is a clear reason to break pattern.
If the archetype is `executive narrative`, limit the deck to a small family of recurring slide types instead of reinventing every page.
If the archetype is `product proof`, keep screenshot and callout treatment consistent.
If the archetype is `platform architecture`, keep node styles, layer logic, and legend behavior consistent across slides.
