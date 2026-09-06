# Narration choices and evidence

Reviewed 2026-09-06. These are routes to audition, not a naturalness leaderboard.
The package's [validation record](../../../VALIDATION.md) owns executed test claims.

| Choice | Useful when | Main tradeoff | Evidence in this package |
|---|---|---|---|
| Gemini Kore through OpenRouter | Continue the accepted example voice | Hosted generation and provider-specific response format | Three clips generated; opening audition approved. This does not establish a universal winner or complete soundtrack listening review. |
| MiniMax Speech | Audition another hosted narrator; optional native voice-design tooling | Account/voice access and paid inference; adapter maps a narrow control set | MiniMax request/response and media conversion tested offline. Live generation and naturalness remain **Unrated**. |
| Direct Gemini / OpenAI / ElevenLabs | A named provider, voice or supported delivery control fits the brief | Different controls and catalogs; access is not interchangeable | Request construction tests are not live-account or listening tests. Check the dated validation record for actual use. |
| Chatterbox full model | An expressive local candidate on an appropriate Mac | Runtime/model setup and a suitable authorized reference | Official Mac example reviewed; not integrated or auditioned here. **Unrated**. |
| Kokoro-82M | A lightweight local preset-voice candidate | Dependencies, pronunciation and prosody still need a real trial | Official Mac guidance reviewed; not integrated or auditioned here. **Unrated**. |
| Human/provided WAV | Use an existing approved recording or a provider outside the helper | Caller supplies accurate origin/settings and clip mapping | Video assembler accepts `ID.wav`; this does not imply any additional generator is implemented. |

No NVIDIA hardware is assumed for a Mac workflow. Qwen CUDA deployment is excluded
from that default; any compatible Mac port would be a distinct, untested route.
Creating this skill did not install local weights or enable an MCP server.

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
