# UI Walkthrough Video

A shared Codex and Claude Code plugin with two skills: real UI walkthrough production and reusable voice narration.

Install from the rl0ve-agent-skills marketplace with `codex plugin add ui-walkthrough-video@rl0ve-agent-skills` or `claude plugin install ui-walkthrough-video@rl0ve-agent-skills`.

Use [ui-walkthrough-video](skills/ui-walkthrough-video/SKILL.md) for capture and video assembly, or [voice-narration](skills/voice-narration/SKILL.md) for audio-only work, provider auditions and revoicing. Both share one audio helper; the narration skill does not require a browser or video input. Copy the complete plugin if using the scripts outside the marketplace. Audio requires Python 3.10+, FFmpeg and ffprobe. Browser capture additionally requires Node + Playwright and an installed browser. Google Gemini, OpenAI, ElevenLabs, OpenRouter and MiniMax use their respective API credentials. Technical tests default to silent output; local system speech requires explicit test opt-in. Other providers may supply WAV files.

Start with the [preferred Mac approach and ratings](skills/ui-walkthrough-video/references/preferred-approach.md) for the recommendation, pros/cons, narration status and evidence limits.

Source and fixture checks are in `VALIDATION.md`. The approved Kore audition was reused; these trials did not compare speech providers.

## Preferred approach and ratings — Mac, no NVIDIA

For a repeatable browser demo, **Custom + the approved Kore narration** is the most
fully reproduced end-to-end route here. Choose **Cap + Kore** when an editable native
recording project matters and the target window can stay in front. Use **Recordly**
as an experimental native capture option. Add a composition framework only when
custom motion or reusable video generation warrants the extra work.

These are **workflow-fit ratings**, not a measured visual-quality leaderboard.
“Strong” means preferred for the stated job, “Good” means useful with a clear
constraint, and “Limited” means only part of the production path was demonstrated.
A working export does not establish viewer approval.

| Approach | Preference / fit | Quality demonstrated | Pros | Cons / limits |
|---|---|---|---|---|
| Custom + Kore | **Good — preferred proven complete browser-demo recipe** | Narrated real-UI demo with visible cursor, click cues, camera framing and captions; motion shortened after feedback | Reproducible source, explicit timing, easy revisions | Source UI is 25fps despite 60fps cursor/camera composition; requires authored motion and maintenance |
| Cap + Kore | **Good — preferred native editable project, conditional on foreground control** | Corrected native framed demo with visible arrow; approved narration added with FFmpeg | Supported recording/config/export CLI; editable Cap project | Earlier take captured another Edge window. Keep the target unobscured and verify the whole timeline. Native zoom/cursor/voiceover editing was not demonstrated |
| Recordly + Kore | **Limited for unattended production; good native capture evidence** | Correct isolated-window capture with visible arrow; approved narration added with FFmpeg | Recorded the intended window when the earlier Cap take was contaminated | Uses an internal capture helper; no supported editor automation or native editor voiceover export was proven |
| HyperFrames | **Strong — custom explainer or authored composition** | Actual animated explainer and narrated walkthrough exports | HTML/CSS/JavaScript motion authoring; local rendering | Does not operate or record the product; design work remains. Initial render configuration timed out |
| Remotion | **Strong — reusable videos driven by data** | Actual walkthrough plus two audience editions from one React composition | Reusable components, structured inputs and application logic | More engineering for a single demo; initial render needed a media-component/configuration correction |
| Screen Studio | **Unrated — candidate for a manually finished Mac demo** | No local trial | Documented screen-demo presentation features | No executed comparison or verified agent editing interface here |

HyperFrames and Remotion can produce the same visual result. Prefer HyperFrames
for a custom motion piece; prefer Remotion when maintaining a video-generating
application or using existing React components. Both can generate variants.
Their showcases are separate from the product-demo comparison page.

### Narration preference

| Voice option | Preference / quality status | Pros | Cons / actual test status |
|---|---|---|---|
| Gemini Kore through OpenRouter | **Established baseline for this demo**; opening audition approved | Working generation path; approved audio reused consistently | Hosted generation requires authorization; no comparative listening benchmark or full soundtrack listening review established |
| OpenAI / ElevenLabs / MiniMax | **Unrated in this comparison**; available hosted audition routes | Generation adapters available | No comparable listening test here; MiniMax integration was tested offline, not against a live voice account |
| Chatterbox full model | **Unrated**; first expressive local audition candidate | Official Mac MPS/CPU example; reference-guided voice | Not integrated or auditioned here; runtime setup and an authorized reference need checking |
| Kokoro-82M | **Unrated**; first lightweight local audition candidate | Small model, preset voices, Apple Silicon guidance | Not integrated or auditioned here; pronunciation and naturalness need listening tests |
| Qwen3-TTS CUDA path | **Excluded from the Mac default** | Relevant to a different hardware setup | NVIDIA instructions do not apply here; a Mac implementation would need separate validation |

See the [full recommendation and evidence](skills/ui-walkthrough-video/references/preferred-approach.md)
and [executed trials](skills/ui-walkthrough-video/references/automation-trials.md)
for version details and remaining gaps. No local TTS quality winner has been established.

Version 1.2 includes a working polished capture/composition route and an existing-site
[example recipe](skills/ui-walkthrough-video/references/polished-example.md), with
Google Kore narration through OpenRouter. Camera planning remains explicit.

Version 1.3 separates cursor/camera animation at 60fps from source footage, adds
conservative auto-framing and loudness normalization, and documents effect priorities
and local/no-hosted-API routes. See the skill references for capability boundaries.

Version 1.4 adds [executed automation guidance](skills/ui-walkthrough-video/references/automation-trials.md)
for native recording, programmable composition, and later refinement.

Version 1.5 adds the separate narration skill and MiniMax speech support. MiniMax's
adapter passed offline contract and media-conversion tests; no live voice-quality
comparison was run. [MiniMax routing](skills/ui-walkthrough-video/references/minimax.md)
distinguishes Desktop Design, coding, hosted speech and generated assets.
