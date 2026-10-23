# Explain an interface

Use when the reader cannot identify controls, distinguish similar badges, or connect
an on-screen state to what they can do next. Explain the current interface without
inventing a problem or turning the request into a redesign or tutorial production.
One annotated screenshot and a short explanation may be the entire deliverable.

## Verify the meaning before drawing the label

Identify the application, relevant view and state. Use the supplied screenshot as
evidence of appearance. Verify unfamiliar meanings through accessible tooltips,
labels, current documentation or implementation source; the shape or color of an
icon is not enough. Keep unresolved meanings visibly unknown. Do not repeat a guess
as a factual label, and correct any earlier explanation that verification disproves.

Distinguish status indicators from controls. For a control, explain the action and
its meaningful consequences, including whether it affects conversation history,
files, shared resources or live state when relevant. Verify those consequences
separately from the icon's name. For a status badge, describe what it reports rather
than imply it performs an action. Read-only inspection is normally sufficient; do
not exercise a destructive, publishing or permission-changing action just to discover
what it does. Follow host access restrictions rather than bypassing blocked inspection.

## Make the actual target recognizable

Keep the original screenshot and preserve its pixels. Crop or uniformly enlarge the
relevant region while retaining enough surrounding labels to orient the reader; use
an overview plus a magnified inset when the full view is needed. Do not generatively
reconstruct the interface, even when asked for an image-generation tool; explain the
pixel-preserving annotation route and use native shapes or overlays instead.

Use restrained numbered markers and short leader lines to the exact controls. Put
the matching legend close by: recognizable name, plain-language meaning, and what
happens on activation if it is a control. Group related labels only when that helps
the reader; do not force one-issue-at-a-time triage onto a request for several icons.
Use the requested style when supplied, and do not rely on color alone. Avoid covering
the target, its tooltip or the labels needed to recognize it. Disclose crops and
scaling; a proposed or schematic image must remain clearly labeled as such.

## Check the delivered guide

Inspect the annotated output at the size the reader will actually see. Confirm every
marker/legend pair reaches the intended target, neighboring icons remain distinct,
the labels match verified meanings, and the source region was not redrawn or distorted.
Keep essential consequences in adjacent text rather than hidden in a tooltip or only
in the image. Include a short text equivalent and show the image inline when supported.
Do not claim click behavior or persistence was tested when only appearance was checked.

A useful completion check is whether the reader can now locate the item, explain
what it means, and decide whether to activate it. If a short definition already does
that, skip the visual. Use a short sequence or clip only when state transitions are
necessary to explain the behavior; a still does not prove an interaction occurred.
