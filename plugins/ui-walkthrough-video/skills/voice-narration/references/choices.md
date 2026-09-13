# Narration choices and evidence

Reviewed 2026-09-13. These are routes to audition, not a naturalness leaderboard.
The package's [validation record](../../../VALIDATION.md) owns executed test claims.

| Choice | Useful when | Main tradeoff | Evidence in this package |
|---|---|---|---|
| Direct Gemini with Algieba + Sulafat | Continue an accepted two-host, male-presenting conversational profile | Native multi-speaker prompting is richer than the package's single-voice-per-beat helper; long sections can lose speaker separation | Four interview-preparation episodes used this pair. Algieba was the smooth analytical lead and Sulafat the warmer co-host. Episodes 3 and 4 were repaired with shorter sections after muddled speaker output. |
| Gemini Kore through OpenRouter | Continue the accepted female-presenting, Southern-inflected product-demo profile | Hosted generation and provider-specific PCM response format; package adapter is single-speaker | Three clips generated; opening audition approved and reused across walkthrough variants. This does not establish a universal winner or complete soundtrack listening review. |
| MiniMax Speech | Audition another hosted narrator; optional native voice-design tooling | Account/voice access and paid inference; adapter maps a narrow control set | MiniMax request/response and media conversion tested offline. Live generation and naturalness remain **Unrated**. |
| Direct Gemini / OpenAI / ElevenLabs | A named provider, voice or supported delivery control fits the brief | Different controls and catalogs; access is not interchangeable | Request construction tests are not live-account or listening tests. Check the dated validation record for actual use. |
| Chatterbox full model | An expressive local candidate on an appropriate Mac | Runtime/model setup and a suitable authorized reference | Official Mac example reviewed; not integrated or auditioned here. **Unrated**. |
| Kokoro-82M | A lightweight local preset-voice candidate | Dependencies, pronunciation and prosody still need a real trial | Official Mac guidance reviewed; not integrated or auditioned here. **Unrated**. |
| Human/provided WAV | Use an existing approved recording or a provider outside the helper | Caller supplies accurate origin/settings and clip mapping | Video assembler accepts `ID.wav`; this does not imply any additional generator is implemented. |
| macOS Siri system voices (Voice 1–5, any accent) | Ruling out a free built-in narrator before hosted generation | Not reachable by any local synthesis API, regardless of download state | Checked 2026-09-13 on one Mac: Voice 1 and Voice 4 downloaded and selected as System Voice/Live Speech voice, machine restarted. Still absent from both `say -v '?'` (legacy NSSpeechSynthesizer) and `AVSpeechSynthesisVoice.speechVoices()` (current AVFoundation). Only "Voice 3" and one India-accent entry surface in `say`, and neither the Siri sample greeting nor a "siri" identifier appears anywhere in the AVFoundation list. Treat as a closed API, not a caching bug — do not spend another session re-downloading or restarting to chase this. |

No NVIDIA hardware is assumed for a Mac workflow. Qwen CUDA deployment is excluded
from that default; any compatible Mac port would be a distinct, untested route.
Creating this skill did not install local weights or enable an MCP server.

For the non-Siri macOS system voices that *are* reachable (Samantha, Alex, Zoe, Daniel,
etc.), `AVSpeechSynthesisVoice.speechVoices()` reports a `quality` field (1 = default/
compact, 2 = enhanced, 3 = premium) that is a faster ground-truth than the tier label
shown in System Settings. Checked 2026-09-13: on one Mac, "Zoe (Premium)" was the only
installed en-US voice at quality 3; the classic "Alex" voice (885 MB) and "Daniel"
(en-GB) were both quality 2 and, after listening, the user rejected both as a default —
size and legacy reputation did not predict a preferred outcome here. This is one
listener's result on one script, not a general ranking of Apple's voices.

Algieba, Sulafat and Kore are Gemini prebuilt voices. Either direct Gemini or
OpenRouter can expose them when the same Gemini TTS model and voice catalog are live.
Do not treat that shared catalog as feature parity: verify model access, voice access,
prompt controls, multi-speaker support and output format for the chosen route.

## Choosing the next audition

Preserve an accepted voice unless there is a reason to change. Compare MiniMax with
that baseline when evaluating hosted narration. For offline work, choose Kokoro for
a smaller initial trial or Chatterbox when reference-guided expression matters.
Verify the actual runtime and download requirements before installing either.

Report observed quality separately from synthesis time, setup effort and cost.
A production recommendation needs both a voice the user accepts and a repeatable
execution path. A low latency claim, a model leaderboard or promotional audio does
not establish either for the user's script.

## Sources

- [MiniMax speech API](https://platform.minimax.io/docs/api-reference/speech-t2a-http) and [official MCP](https://github.com/MiniMax-AI/MiniMax-MCP): synthesis tools and supported controls.
- [Chatterbox Mac example](https://github.com/resemble-ai/chatterbox/blob/master/example_for_mac.py): MPS/CPU route for the full model.
- [Kokoro Mac guidance](https://github.com/hexgrad/kokoro#macos-apple-silicon-gpu-acceleration): local runtime guidance.
- [Existing speech benchmark snapshot](../../ui-walkthrough-video/references/benchmarks.md): dated external context, not local listening evidence.
