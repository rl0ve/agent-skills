# Voice selection evidence — checked 2026-09-05

The first release checked API contracts, not current model benchmarks. This review
adds a dated shortlist; refresh it for a new model choice. Avoid search snippets
when a live table is available: the cached ranking differed from the opened table.

[Artificial Analysis native-voice arena](https://artificialanalysis.ai/text-to-speech/leaderboard/provider-voice?tab=leaderboard)
compares blind listener preferences using providers' own voices. Opened snapshot:

| Rank | Model | Elo | 95% interval half-width |
|---|---|---:|---:|
| 1 | Cartesia Sonic 3.6 | 1282 | 17 |
| 2 | Inworld Realtime TTS-2 | 1252 | 18 |
| 3 | Alibaba Qwen-Audio-3.0-TTS-Plus | 1241 | 14 |
| 4 | Speechify Simba 3.2 | 1240 | 14 |
| 5 | VUI Labs Luna TTS | 1228 | 14 |
| 8 | ElevenLabs v3 Conversational | 1210 | 15 |
| 9 | Google Gemini 3.1 Flash TTS | 1208 | 12 |

This ranks sampled model-plus-voice combinations, not every voice, accent or long
narration. Overlapping intervals discourage overreading adjacent ranks. The
[controlled-voice arena](https://artificialanalysis.ai/text-to-speech/leaderboard/controlled-voice)
uses eight cloned US/UK voices; it answers a different question. No second independent
TTS ranking was verified in this pass; DesignArena's TTS navigation did not resolve.
No paid A/B listening benchmark was run.

Selection method: include the user's preferred voice, one currently strong challenger,
and optionally OpenAI's current steerable TTS. Compare identical 10–20 second copy
with a difficult name, number and UI transition. Listen for cadence, prosody, metallic
sound, acting, pronunciation and scene-join consistency. User preference is a hard
gate; model rank cannot override rejection of robotic speech. Realtime latency is
secondary for offline demos. Check provider docs, access and actual billing before
calling any model. Never put a leaderboard's display name into an API blindly.

Sources: [Google TTS](https://ai.google.dev/gemini-api/docs/speech-generation),
[Google legacy REST contract](https://ai.google.dev/gemini-api/docs/generate-content/speech-generation),
[Cartesia pricing/model availability](https://www.cartesia.ai/pricing),
[Inworld TTS-2](https://inworld.ai/blog/realtime-tts-2).
