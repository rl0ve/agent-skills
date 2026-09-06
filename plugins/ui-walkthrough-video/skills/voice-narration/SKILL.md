---
name: voice-narration
description: Select, audition, generate and revise spoken narration across speech providers, including audio-only delivery and revoicing existing media. Use for voiceover quality comparisons, pronunciation, consistent delivery and Mac-compatible local narration choices. Does not record screens or build conversational voice agents.
---

# Voice narration

Own the spoken-audio workflow: voice selection, comparative audition, synthesis,
pronunciation, revision and delivery. This skill ships beside `ui-walkthrough-video`
in the same plugin and shares its audio helper. It works without a browser, video
input, Playwright or a screen recorder.

## Choose the work

- For audio-only narration, finish here with playable audio and the transcript.
- For a narrated walkthrough, produce audio by beat ID, then hand the files and
  measured durations to `ui-walkthrough-video` for video assembly. Reuse existing
  footage when only the voice changes.
- For a simple request that already names OpenAI, an available OpenAI `speech`
  specialist may handle generation. Preserve its supported CLI and the chosen
  voice; do not run a second provider-selection workflow unnecessarily.
- For script rewriting, use natural-writing's spoken guidance if available. Keep
  claims, names, numbers and uncertainty intact. A request to read supplied text
  does not authorize rewriting it.

## Select and audition

Infer language, audience, pace, desired delivery and output length from the request.
Honor a known voice, budget and hosted/offline preference. Ask only for missing
choices that affect execution. Do not force a fresh audition for an already accepted
voice unless the script, language or delivery changes enough to warrant one.

Read [provider guidance](references/providers.md) for the selected provider and
[provider choices and evidence](references/choices.md) for comparisons. MiniMax
Speech is a candidate alongside Gemini, OpenAI and ElevenLabs; a social endorsement
or a provider benchmark does not establish this script's quality.

For a comparison, use the same 10–20 second passage with a name, a number and a
transition. Generate only the authorized candidates. Preserve the source audio;
compare copies at similar perceived loudness so volume does not bias the choice.
Judge naturalness, intelligibility, pronunciation, artifacts, pacing and consistency.
Separate voice preference from recording defects. Return the samples and a concise
comparison, not a winner inferred from a model name or price.

Rate only heard output. Use 1–5 for each dimension when useful: 1 unusable, 2 major
problems, 3 usable with edits, 4 strong with minor issues, 5 accepted for this brief.
Use **Unrated** when no listening review occurred. Record who listened and any
remaining acceptance decision. If audio playback/listening is unavailable, say so;
a waveform, transcription or successful decode cannot prove naturalness.

For a Mac, consider the actual chip/runtime. Chatterbox and Kokoro are local trial
candidates, not bundled generation adapters. A CUDA recipe is not a Mac default.
Hosted speech APIs do not require a local NVIDIA GPU, and a Mac desktop client does
not establish offline inference. No system-voice substitution when a preferred
provider is unavailable; return an honest blocker or a silent video proof instead.

## Generate and revise

Use a connected supported tool or the shared helper. The package implements
Gemini, OpenAI, ElevenLabs, OpenRouter and MiniMax request paths; availability and
successful live generation remain provider/account-specific. Read the implementation
status before promising that an adapter has been auditioned.

The shared helper needs Python 3.10+, FFmpeg and ffprobe. Copy the
[audio-only example](assets/audition.example.json), select the provider/model/voice,
and replace its text. The example is a recipe, not an authorization to spend.
From this skill's directory:

```sh
# Once the selected provider and generation budget are authorized:
python3 ../ui-walkthrough-video/scripts/render.py voice ./audition.json ./audio-take-01 --allow-paid
```

The manifest needs `version`, `voice` and `beats` with stable `id` and `narration`;
video fields are unnecessary. The output contains `ID.wav` at 48kHz stereo, source
audio and `voice.json`. `--allow-paid` records prior authorization, not a budget
limit enforced by the helper. Keep the original transcript/manifest with delivery.

Use an existing secret manager according to host instructions. Check which providers
it actually supports; do not assume the Mac helper has a MiniMax entry. MiniMax's
adapter expects `MINIMAX_API_KEY` supplied securely to the process. Never put keys
in a manifest or transcript. No global credential configuration is changed by this
skill. Respect prior authorization; do not ask for it again when already provided.

Split long scripts at sensible paragraph/scene boundaries before generation. Keep
settings constant across a batch. Pronunciation hints belong in synthesis text or
supported provider controls; preserve ordinary spelling in the displayed transcript.
The shared helper does not have a separate synthesis-text field: if using respelled
text, retain a separate display transcript and explicit subtitle cues.

Outputs refuse overwrite. For a correction, generate only affected IDs into a new
take; keep approved audio. After a timeout or provider error, inspect usage before
retrying because the failed response may still have been billed. Preserve successful
clips and metadata. Do not clone an identifiable voice without authorization.

## Finish

Measure duration and check decoding, clipping, unintended silence and missing/truncated
words. Listen to the audition, names, numbers, joins and ending; listen through a
short final narration when possible. Regenerate a mispronounced word or bad delivery
before adding effects. Loudness normalization does not fix robotic prosody.

Deliver playable WAV/MP3, transcript, exact provider/model/voice/settings and the
review status. For multi-clip delivery, include stable IDs and measured durations;
for video handoff, pass real cue points and label estimated captions. State that
speech is AI-generated. Keep technical verification, subjective review, user approval
and untested alternatives separate.
