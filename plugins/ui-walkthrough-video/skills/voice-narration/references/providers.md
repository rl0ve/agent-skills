# Provider guidance

Ask for a quality target or range, budget, language/style and any named provider,
model or voice. Translate a target into a short audition, not a fixed model ranking.
“Premium” means more selection and listening, not simply higher price.

| Target | Route | Needed |
|---|---|---|
| Natural narration | Audition preferred Google Gemini voice plus a current challenger | Key and budget; listen before full generation |
| Exact voice/model | Preserve user's selection and audition style | Verify current model/account access |
| Another provider / human narration | Supply one WAV per beat | Accurate manifest describing actual origin |
| Technical capture test | Silent render | No speech or key |

No automatic system-speech fallback. The local adapter is retained only for explicitly
requested engineering tests via `--allow-local-test`; it is not a quality tier to
recommend. A high-ranked model can still produce a voice the user dislikes.

Google Gemini adapter: `provider: "gemini"`, explicit `model` and `voice`, optional
`instructions`, and `GEMINI_API_KEY`.

**Current models (GA 2026-09-22, checked 2026-10-11):** `gemini-3.8-flash-tts`
(flagship, expressive, long-form) and `gemini-3.8-flash-lite-tts` (cheaper; Google's
stated replacement for `gemini-3.1-flash-tts-preview`). See the
[speech guide](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation)
and [release notes](https://ai.google.dev/gemini-api/docs/changelog). For 3.8+ the
adapter sends the verbatim transcript as `text`, puts `instructions` in
`speech_metadata.style`, passes `voice` as `speechConfig.voiceConfig.voice` (a prebuilt
name, an Extended Voice Library ID or a `voice_...` design/replication ID), and saves
the returned RIFF WAV after checking it is 24 kHz mono PCM16. Inline tags such as
`<short pause>` belong in the transcript only when you want them spoken as events.
Keep `instructions` short on 3.8 (one clause such as "calm, conversational, medium
pace"): Google's guide says long style or "director's notes" blocks are the main cause
of voice drift, and most takes need no style at all.
The 3.8 path is covered by offline request/response tests; **no live 3.8 call has
been made by this package yet**, so run a short audition before a full take.

`gemini-3.1-flash-tts-preview` still uses the legacy schema (instructions prefixed to
the text, `prebuiltVoiceConfig`, headerless PCM wrapped in WAV). Keep it only to
continue an accepted take; it is slated for replacement.

The 30 prebuilt names (Kore, Algenib, Algieba, Sulafat and others) carry over to 3.8,
but **the same name on a new model is a new voice for acceptance purposes**:
re-audition before mixing 3.1 and 3.8 clips in one production. Voice design and
replication need their own authorization; never replicate an identifiable voice
without consent. The adapter is separate from Google Cloud Chirp/Studio/WaveNet and
from Gemini Live. Do not infer a model from the voice name alone.

`gemini-3.5-transcribe` is a distinct, opposite-direction model: audio-to-text
(speech recognition with diarization/timestamps), not text-to-speech. Its similar
name and release timing next to `gemini-3.1-flash-tts-preview` invites confusion;
it cannot generate narration and is irrelevant to this skill. Confirmed 2026-09-13.

Gemini prebuilt voice names belong to the model rather than the access route. When
OpenRouter exposes the same Gemini TTS model, names such as Algieba, Sulafat and Kore
can be available through either route. Verify the live catalog and make a short
request before promising parity. Direct Gemini exposes native prompt steering and
up-to-two-speaker configuration. This package's `gemini` and `openrouter` adapters
currently synthesize one configured voice per beat; use a supported direct Gemini
tool for native two-speaker generation rather than implying the helper implements it.

API examples, not permanent defaults or quality guarantees. OpenAI (checked
2026-09-05): `gpt-4o-mini-tts` supports delivery instructions; legacy `tts-1` /
`tts-1-hd` do not. ElevenLabs (checked 2026-10-11): `eleven_v4` is the current
flagship ([models](https://elevenlabs.io/docs/overview/models)) and accepts only
`stability` and `similarity_boost` in `voice_settings`, which the adapter enforces;
`eleven_v4_turbo` targets ~100 ms real-time streaming and is not needed for
narration. v3, Multilingual v2 and Flash v2.5 remain available. Whether the
`/with-timestamps` endpoint returns alignment for `eleven_v4` has not been verified
here; check the first response before relying on word sidecars. ElevenLabs also
publishes [official agent skills](https://github.com/elevenlabs/skills) that can
handle a request already committed to ElevenLabs. Check current model/voice
availability and prices before paid generation.

**Blind-preference snapshot** ([Artificial Analysis Speech Arena](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice),
2026-10-10): Eleven v4 Turbo and Eleven v4 lead, followed by Qwen-Audio-3.1-TTS-Plus,
Cartesia Sonic 3.6 and Gemini 3.8 Flash TTS. Use it to pick audition candidates,
not to choose a winner: the arena measures short generic clips, not this script,
voice or delivery.

Suggested delivery instruction: “Speak clearly and conversationally for a product
walkthrough. Calm, confident, medium pace. Brief pause after each UI result. Avoid
sales-announcer emphasis. Pronounce the supplied product terms as written.”
Change this for the user's desired style. Do not pretend arbitrary instruction text
works on every model: the ElevenLabs adapter takes provider-specific voice_settings;
use supported audio tags only for models that document them.

The included tool uses environment variables, never a key embedded in the manifest:
`GEMINI_API_KEY`, `OPENAI_API_KEY` or `ELEVENLABS_API_KEY`. If missing, ask the user to set the named
variable in the execution environment (or use their secret manager) and tell you
when ready. Never ask them to paste a key into chat or put one into a command that
will be retained in shell history. Do not open unrelated .env files to find keys.

Paid generation requires `--allow-paid` to confirm the selected provider/budget is
already authorized. The tool preflights keys before creating output. It does not
retry HTTP failures automatically because generation may have incurred a charge.
Keep successful scene files after partial failure; finish missing scenes using a
new manifest/output and combine by beat ID. Record provider/model/voice/settings
with audio. Never include credentials in exports or package artifacts.

For a 10–15 second audition, use a temporary manifest containing one representative
beat, synthesize it, listen, then continue with the agreed selection. New providers
can use their own supported tools and deliver WAV files to the assembler. Changing
providers must not change narration facts or silently switch languages.

Pronunciation workflow: keep display/caption spelling separate from synthesis-only
respellings. Audition difficult names in short samples, preserve accepted pronunciations
and the full delivery style, then regenerate only affected audio. Do not exaggerate
accent tags to manufacture warmth. Prefer natural cadence and restrained direction.

OpenAI distinction: `tts-1`/`tts-1-hd` are older dedicated TTS models;
`gpt-4o-mini-tts` is a newer steerable TTS route. ChatGPT Voice and the Realtime API
are conversational voice experiences, not interchangeable evidence of TTS quality.
Audition the current TTS model before dismissing OpenAI based on the older models.

For an OpenAI comparison, audition `gpt-4o-mini-tts` with `marin` or `cedar`,
the voices recommended for quality in the current [Speech guide](https://developers.openai.com/api/docs/guides/text-to-speech).
Compare identical copy against the preferred Gemini voice. The current
[ChatGPT Voice documentation](https://help.openai.com/en/articles/20001274) describes
Live as GPT-Live-1/mini; this is not the Speech endpoint. The
[Realtime API](https://developers.openai.com/api/docs/models/gpt-realtime-2.1)
is a separate conversational route and is not implemented by this helper.
Do not infer mini-TTS quality from rankings for tts-1 or tts-1-hd.

## Shared credentials and OpenRouter

First consult global instructions for an existing Keychain/secret-manager helper.
Check presence without revealing values, then run only synthesis under the selected
provider's environment. Do not re-search old chats or copy a key into the project
when a configured helper already supplies it. Credentials available on one Mac are
not automatically available to a cloud worker. Never disable TLS validation to fix
an environment issue; select a runtime with a valid CA store.

`provider: "openrouter"` uses `OPENROUTER_API_KEY` and an explicit live catalog slug.
The demonstrated route is `google/gemini-3.1-flash-tts-preview` with `Kore`. Gemini
requires `response_format: pcm` through this endpoint; the adapter wraps its 24 kHz
mono PCM16 output in WAV. Other models request MP3 and validate the content type
and signature. General OpenRouter MP3 examples do not override a model-specific
format requirement. Delivery instructions are mapped only for documented OpenAI
provider options; unsupported instructions fail explicitly rather than being dropped.

OpenRouter model availability differs from direct provider access. Its live speech
catalog did not list OpenAI or ElevenLabs in this review despite documentation
examples; do not promise availability based on a snippet. Verify model/voice access
before generation. Metadata is saved before synthesis so partial takes retain their
provider/model/voice settings. No automatic paid retries occur.

Observed voice profiles, reviewed 2026-09-14. Every one of the model's prebuilt
voices is selectable; these are only the ones someone has listened to and accepted
for a specific brief:

- **Algenib** — accepted over four passes of edits as the single narrator of a
  product walkthrough cut from real screen capture, direct Gemini, calm and even at
  roughly 2.5 to 3 words per second with the delivery instruction held constant
  across every beat so re-synthesised lines splice against earlier ones without an
  audible seam.
- **Algieba** — accepted as a smooth, male-presenting analytical lead in a direct
  Gemini two-speaker interview-preparation series.
- **Sulafat** — used as the warmer, male-presenting conversational co-host in that
  same direct Gemini production.
- **Kore** — accepted through OpenRouter for a firm, female-presenting narration with
  a Southern-inflected product-demo delivery.

These are user-specific listening results from different briefs, not official gender
labels or general quality rankings. Preserve the route and performance direction with
the voice name. For long two-speaker output, split at natural exchanges of roughly
one to three minutes and check speaker continuity; longer direct-Gemini sections in
the accepted production sometimes blended voices and were regenerated in shorter
sections.

Google's own voice list (checked 2026-09-13) describes Algieba as male ("smooth and
pleasant") and Sulafat as female ("warm and welcoming"), and none of the 30 prebuilt
voices carry a quality tier — they differ only by style/character description, all on
the same underlying model. Neither published description overrides an accepted
production's listening result above; note both when a brief cares about a consistent
apparent gender rather than only the delivery style.


## MiniMax speech adapter

Checked 2026-09-06 against the [synchronous speech contract](https://platform.minimax.io/docs/api-reference/speech-t2a-http).
Use `provider: "minimax"`, an explicit model such as `speech-2.8-hd`, and a verified
voice ID. `English_expressive_narrator` is the provider's documented example, not an
auditioned preference. The key variable is `MINIMAX_API_KEY`. The global endpoint
is `https://api.minimax.io/v1/t2a_v2`; a different region/account requires its own
verified configuration and is not silently substituted by this adapter.

The helper sends non-streaming requests, decodes completed hexadecimal MP3 audio,
then uses FFmpeg to create the same `ID.wav` handoff as the other providers. It
validates the response status and audio signature before conversion. A JSON response
or HTTP 200 alone is not successful speech. Requests are limited to nonempty text
under 10,000 characters per beat; all beats are preflighted before the first call.

Supported user fields are `provider`, `model`, `voice`, `quality` and `speed`.
Speed ranges from 0.5 to 2; quality is metadata. Free-form instructions and
ElevenLabs `voice_settings` are rejected rather than silently ignored. Cloning,
voice design, emotional controls, streaming, URL audio and provider timestamps are
not implemented by this helper. Use supported connected tools for those operations
when requested, without implying they have been tested here.

The request/response path and actual MP3-to-WAV decoding were tested offline with
a synthetic tone fixture. That is integration engineering evidence, not a successful
live API call, an audition, or proof of model quality. Keep MiniMax **Unrated** until
real speech is generated and heard.

MiniMax Desktop Design and the speech API are different execution routes. Use the
API for narration inside this workflow; use the named desktop application when the
user wants to work there and its controls are available. Desktop access does not
prove API credentials or shared billing. The local `ai-credentials` helper may not
support MiniMax: inspect its supported providers before proposing a command. Do not
invent `ai-credentials run minimax`, search unrelated files, or change its configuration
as a side effect of narration work.
