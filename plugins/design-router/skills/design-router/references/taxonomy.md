# Routing taxonomy

Classify the work itself first, then the people and purpose it serves.

## Surface axis

| Surface | Use when | Do not confuse with |
|---|---|---|
| `marketing-landing` | A public page must explain, persuade, establish trust, or convert | A signed-in product workflow |
| `product-app` | Users complete recurring tasks in an application, dashboard, portal, admin, or tool | A campaign or brand page |
| `creative-expressive` | Visual expression, art direction, 3D, WebGL, generative work, or cinematic interaction is itself part of the value | Decorative motion added to an ordinary app |
| `content-editorial` | The main surface is built for reading, reference, publication, documentation, or a sustained editorial narrative | Copy-only editing or a conversion-first campaign page |
| `motion-only` | The structure and visual system are accepted; only transition, animation, gesture, or feedback behavior should change | A redesign |
| `image-to-code` | A screenshot, Figma node, URL, video, or existing design is the visual specification | A loose inspiration moodboard |
| `systems-extraction` | The output is tokens, components, patterns, `DESIGN.md`, or a reusable design system | Implementing a new page |
| `review-audit` | The user wants critique, accessibility, performance, UX, or visual-quality findings | A request to fix the findings |
| `writing-anti-slop` | The main job is interface copy, voice, labels, errors, onboarding, or removal of generic language | Page art direction |
| `component-library` | The output is a reusable component, pattern, primitive, variant system, or documentation | One-off page markup |

## Audience axis

| Audience | Primary success signal |
|---|---|
| `b2b-saas` | Fast expert work, legible density, trust, semantic states |
| `b2c-ecommerce` | Product confidence, conversion, honest urgency, safe checkout |
| `b2c-consumer-app` | Habit, personality, direct manipulation, culturally current interaction |
| `b2b-marketing` | Clear category/value, proof, risk reduction, executive scanability |
| `b2c-marketing` | Emotional relevance, brand memory, image-led persuasion |
| `prosumer-tool` | Expert speed with visible craft, keyboard fluency, creator/developer taste |
| `internal-tool` | Operational throughput, low training cost, predictable behavior |
| `content-editorial` | Comprehension, reading rhythm, navigation, citation and structure |
| `portfolio-personal` | Distinctive point of view, memorable work, intentional motion |

Use `audience-agnostic` only for a non-user-facing artifact such as a raw token extraction. If the result will be seen or used by people, choose an audience.

## Consequential ambiguity tests

Ask before acting when any of these are unresolved:

- “Dashboard” could mean `b2b-saas`, `prosumer-tool`, or `internal-tool`.
- “Website” could mean `marketing-landing`, `content-editorial`, or `portfolio-personal`.
- “Make it impressive” could mean restrained craft or `creative-expressive`.
- A reference could be inspiration or a fidelity specification.

Do not ask when surrounding context makes the answer clear. State the inferred axes and proceed.
