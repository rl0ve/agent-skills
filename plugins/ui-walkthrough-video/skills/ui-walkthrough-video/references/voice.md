# Voice selection

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
`instructions`, and `GEMINI_API_KEY`. Example model checked 2026-09-05:
`gemini-3.1-flash-tts-preview`, voice `Kore`. The adapter uses Google's documented
legacy generateContent endpoint, validates returned PCM and wraps it in WAV. It
is separate from Google Cloud Chirp/Studio/WaveNet and from Gemini Live. Do not infer
a model from the voice name alone. Preview models may change or have rate limits.

Verified API examples on 2026-09-05, not permanent defaults or quality guarantees:
OpenAI `gpt-4o-mini-tts` supports delivery instructions; legacy `tts-1` / `tts-1-hd`
do not support that control. ElevenLabs uses a voice ID and `model_id`; options
include Multilingual v2, Flash v2.5 and v3 with different latency/expressiveness
tradeoffs. Check current model/voice availability and prices before paid generation.

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
