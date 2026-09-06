# Preferred approach for a Mac walkthrough

Reviewed 2026-09-06. This recommendation assumes macOS with no NVIDIA GPU.
Apple Silicon acceleration is conditional on the actual machine and runtime.
It combines executed trials, review of rendered frames, user feedback, and current
upstream documentation. It is not a controlled quality benchmark.

## Recommendation

Use **Cap for agent-controlled recording of real UI**, keep its native export when
that meets the brief, and add **HyperFrames only when custom composition is useful**.
Use **Gemini Kore through OpenRouter for narration when the approved voice and
hosted generation are appropriate**. Reuse approved audio across visual revisions.

This is the preferred production direction, with a remaining integration boundary:
Cap recording/export and HyperFrames composition were tested separately. The
HyperFrames trial used browser-captured source clips; a Cap-to-HyperFrames narrated
pipeline has not yet been exercised as one complete workflow. The bundled custom
compositor plus Kore is the most directly reproduced complete narrated example.
It remains the fallback when that known recipe is the quickest suitable answer.

Choose **Remotion** when the deliverable is a reusable video system: one composition,
many data inputs, audiences or formats. Choose **HyperFrames** for a custom explainer
or motion piece authored in HTML/CSS/JavaScript. Both can do either job; the distinction
is workflow fit, not an inherent difference in image quality.

## Ratings and tradeoffs

Ratings are editorial judgments about the tested workflow, not product-wide scores:
**Strong** = preferred for the named job; **Good** = useful with a clear constraint;
**Limited** = demonstrated only part of the production path; **Unrated** = insufficient
trial evidence. Visual quality describes the actual outputs reviewed. A successful
render or 60fps export does not establish viewer approval.

| Approach | Fit rating and best use | Quality demonstrated here | Main advantage | Main drawback / evidence limit |
|---|---|---|---|---|
| Cap | **Strong** for agent-controlled native capture | Basic framed native export with a visible moving arrow; full decode and action/result frame review passed | Supported CLI produced an editable recording project and export | Native zoom/cursor editing was not demonstrated. The repaired arrow is baked into footage. Raw capture is not a finished narrated demo. |
| HyperFrames | **Strong** for a custom explainer or authored composition | Framed narrated walkthrough with cursor/camera/captions; separate animated explainer also rendered | Flexible HTML/CSS/JavaScript composition and local rendering | Motion and layout still need direction. It is not a recorder or automatic editor. An initial render timed out before a working configuration was found. |
| Remotion | **Strong** for reusable videos driven by data; **Good** for a single walkthrough | Narrated walkthrough plus two audience editions rendered from one React composition | Reusable React logic, parameterized content and predictable variants | More setup for a single recording. An initial render timed out; the FFmpeg-backed media component and sequential rendering succeeded. |
| Recordly bundled capture engine | **Limited** for unattended production; **Good** as capture evidence | Native raw recording with moving arrow and real UI changes | Real desktop capture worked | Trial used an internal helper, not a supported editor automation interface. No finished editor export or editable native cursor layer was proven. |
| Bundled Playwright + Pillow/FFmpeg helper | **Good** as a reproducible fallback | Complete narrated 1600×1000 demo with composed 60fps cursor/camera | Explicit timing and editable source; works with the existing recipe | Source UI remains 25fps. Custom maintenance and editorial work; earlier motion was too slow and needed correction. |
| Screen Studio | **Unrated** in these trials; candidate for a manually finished Mac demo | No local trial | Documented automatic zoom/cursor presentation tools | No executed comparison or verified general agent editing interface here; cannot call it the quality winner. |

Cap is preferred for the supported automation path, not because the trial proved
that it makes prettier videos than Recordly or Screen Studio. The native examples
and authored framework examples differed in narration and editing scope, so their
finish must not be treated as a fair product quality comparison.

## Narration on a Mac

Use [voice-narration](../../voice-narration/SKILL.md) for audio production and the
current evidence-qualified provider comparison. [MiniMax routing](minimax.md) covers
its desktop workspace versus API and its role in this pipeline.

| Option | Current standing | Benefit | Cost / limitation | What was actually tested |
|---|---|---|---|---|
| Gemini Kore through OpenRouter | **Preferred established voice for this example** | Opening audition was approved and the same voice was used for the demo | Hosted generation requires an authorized account/budget; subjective acceptance is script-specific | Three clips generated. Opening audition approved; no cross-provider listening benchmark or complete soundtrack listening review established. |
| MiniMax Speech | **Unrated; hosted audition candidate** | Speech can be generated within the existing workflow | API account/budget required; Desktop Design access is separate | Adapter and real media conversion tested offline; no live call or listening comparison. |
| Chatterbox full model | **Unrated; first expressive local audition candidate** | Official Mac example selects MPS or CPU; reference-guided generation | Model/runtime setup and a suitable authorized voice reference; speed and naturalness on this machine unknown | Documentation reviewed only. No installed adapter, generated sample or listening comparison in this plugin. The Turbo CUDA example is a different path. |
| Kokoro-82M | **Unrated; first lightweight local audition candidate** | Small model, preset voices and documented Apple Silicon guidance | Dependency/phonemizer setup; delivery and product-name pronunciation need listening review | Documentation reviewed only. No installed adapter, generated sample or listening comparison in this plugin. |
| Qwen3-TTS CUDA deployment | **Excluded from this Mac default** | May suit a different hardware environment | NVIDIA/CUDA instructions do not apply to this setup; any Mac port requires a separate check | No local trial or adapter. This does not assert that every possible Mac implementation is unsupported. |

Chatterbox and Kokoro are documented options, not integrated providers. The existing
`provided` WAV route can assemble audio generated elsewhere, but it does not generate
speech from either model. Do not label them installed, working or better than Kore
until a real local run and listening comparison establish that status.

A useful future audition uses the same 10–20 second passage with a product name,
number and transition. Record hardware/runtime, startup and synthesis time, compare
level-matched output, and assess naturalness, pronunciation, artifacts and consistency.
Keep quality **Unrated** until heard. No new local models or paid speech calls were
run for this recommendation update.

## Motion and acceptance criteria

Use ordinary mouse pace. For this example, the revised composition uses **0.4-second
cursor journeys** and **0.6-second camera transitions**, replacing cursor glides of
about 1.2 seconds and camera moves of 2–3.2 seconds. These are starting values for
similar distances, not fixed timings for every gesture. Keep longer pauses for
reading after a move, rather than making the move itself float slowly.

The revision preserved actual click/result times and narration; AAC audio packets
matched the earlier render. Actual frames and full decoding were checked. It has
not yet received explicit viewer acceptance. The packaged helper's timing code was
not changed by this documentation release; apply timing choices to the scene plan.

Before calling a demo finished, inspect the recorded pixels for the right window,
a visible ordinary arrow, menus that actually close, readable framing and correct UI
results. Check pointer/camera travel in playback, and listen to the narration.
A valid project, passing page assertion or nominal frame rate is insufficient.

## Evidence and sources

- [Executed automation trials](automation-trials.md): configurations, rejected takes,
  cursor correction, source cadence and native-editor boundaries.
- [Validation history](../../../VALIDATION.md): dated tests and remaining gaps.
- [Cap agent interface](https://cap.so/docs/agents): supported agent workflow.
- [HyperFrames](https://github.com/heygen-com/hyperframes): HTML composition and local rendering.
- [Remotion parameterized rendering](https://www.remotion.dev/docs/parameterized-rendering): input-driven compositions.
- [Recordly](https://github.com/webadderallorg/Recordly) and [Screen Studio](https://screen.studio/): product capabilities, distinct from local trial evidence.
- [Chatterbox Mac example](https://github.com/resemble-ai/chatterbox/blob/master/example_for_mac.py) and [Kokoro](https://github.com/hexgrad/kokoro#macos-apple-silicon-gpu-acceleration): platform documentation, not voice-quality ratings.

Revisit the recommendation after a complete Cap-to-compositor export, supported
native editor automation, a comparable Mac speech audition, or viewer rejection
of the current result. A new model or advertised feature alone is not proof of a
better workflow.
