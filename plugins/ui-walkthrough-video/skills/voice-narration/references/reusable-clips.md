# Reusable narration in an application

Use for a requested library of clips reused in a product, lesson, game or kiosk.
For a single voiceover, keep the ordinary audition/generate/deliver route. This is
guidance for the destination application's pipeline: the bundled renderer does not
implement a spending ledger, content cache, transcript service or runtime player.

## Choose what should be recorded

Start with the approved voice and representative high-use passages. Keep generation
provisional when no human has accepted the audition; an authorization to generate a
bounded batch is not a voice-quality verdict. Do not infer that a large text catalog
needs a premium recording for every entry. Static authored guidance can be generated
once and reused; dynamic text may need a separately selected runtime speech route.

Make recorded, device and hosted speech choices explicit. Honor a named provider or
offline requirement; do not silently substitute system speech to satisfy it. For a
multilingual sequence, keep complete utterances tagged with their own language/variety
and route them accordingly. A matching word spelling alone does not justify serving
another language or dialect's recording. Document any network fallback and its data.

## Enforce the authorized budget before dispatch

For a metered batch under a spending ceiling, track the whole authorized operation:
auditions, generation, verification, replacements and uncertain requests. Available
account credit is separate from the user's authorization. `--allow-paid` in the
bundled helper records authorization; it does not enforce a monetary cap.

Use a persistent ledger or equivalent provider controls. Reserve a conservative cost
before sending a request, reconcile actual charges from provider metadata when
available, and retain the reservation while cost is unknown. Derive the bound from
current route-specific prices, units and enforced request/output limits, not a typical
clip's duration or a different provider's limits. Without a defensible bound or an
applicable provider spending control, do not claim a hard cap is enforced. Keep
verification inside the same budget. Serialize dispatch or make reservation updates
atomic if parallel generation is warranted.

A timeout is an uncertain outcome, not permission to send the same paid request again.
Inspect its status and charge; preserve completed clips and retry only the affected
item under the existing authorization. New takes retain distinct identities and cost
history. Use the host's secret manager without copying credentials into the project.

## Cache and publish by verified identity

Keep stable content IDs plus an identity for transcript, language/variety, provider,
model, voice, delivery settings and prompt recipe/version. Include synthesis-only text
when it differs from display spelling. A changed setting or transcript invalidates
only the affected recording. Preserve accents, negation and word order; a fuzzy text
match must not serve the wrong instruction.

Keep source takes and review metadata separate from the runtime package. Decode the
encoded file actually delivered, record its duration and hash, and tie checks to that
file. Automated transcription can flag added, missing or ambiguous words but cannot
establish pronunciation, naturalness or speaker quality. Use narrow, documented
normalization rules; do not accept a high similarity score that hides a changed word
or edit the intended script merely to match an uncertain transcription. Retake or
review a flagged passage and preserve its review status.

Publish a manifest that connects approved identities to real files. Check coverage of
the intended clip set and refuse an incomplete required pack; label a deliberately
partial pack and its fallback. Avoid replacing a working catalog before validation
finishes. Runtime playback should not trigger paid regeneration unless that behavior
is explicitly part of the authorized product. Learner notes and other personal data
do not belong in static synthesis requests by default.

Report actual spend separately from outstanding reservations, and technical checks
separately from heard quality. Do not call a build-time API recording local inference
merely because its cached file plays without a generation request.
