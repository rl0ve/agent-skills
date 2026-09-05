# Voice selection

Ask for a quality target or range, budget, language/style and any named provider,
model or voice. Translate a target into a short audition, not a fixed model ranking.
“Premium” means more selection and listening, not simply higher price.

| Target | Reasonable route | Needed |
|---|---|---|
| Free local draft | macOS `say`, installed voice | macOS; no key; visibly label draft |
| Polished | OpenAI TTS or user's preferred provider | API key; model and voice |
| Polished–premium | Audition OpenAI / ElevenLabs or supplied recording | Budget plus named voices; compare the same script |
| Exact model / existing voice | Preserve the user's choice | Verify current account access and supported settings |
| Other provider / human narration | Generate externally, then supplied WAV audio | One audio file per beat |

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
`OPENAI_API_KEY` or `ELEVENLABS_API_KEY`. If missing, ask the user to set the named
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
