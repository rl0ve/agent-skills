# earshot review: October 18, 2026

Record behind UI Walkthrough Video 1.7.1. Source: LexnLin's earshot launch, quoted by
[Meng To on October 16](https://x.com/MengTo/status/2110938316162076685), and the
[repository](https://github.com/Leonxlnx/earshot) (MIT, version 0.3.0 on `main`, latest
tag v0.2.0). UI Router 1.19.3 already lists it as a conditional audio aid for 3D scenes.
Facts below come from the README, `docs/LIMITS.md`, `docs/SFX.md` and its own skill,
read on October 18. Nothing was installed or run.

| Capability | Decision | Reason |
| --- | --- | --- |
| Sound-to-cut offsets (`timeline --cues`) | **Conditional** | Fills a gap on the HyperFrames route, whose helper places SFX and music but does not check where they land. Upstream reports a median offset of 0 ms and 96% within a frame for hard hits. Camera moves and crossfades are not detected as cuts, so cues come from the storyboard. |
| Code-built SFX bank (`sfx`, `kit`) | **Conditional** | A local source when SFX are requested and no assets exist: no models, no network, measured onset and peak, and MIT, with the fitted sounds taken from CC0 recordings. |
| LUFS and true peak (`measure`) | **Already covered** | `verify_video.py` measures loudness and true peak. |
| Narration review | **Already covered** | earshot detects voice but not words. The listening reviewer stays. |
| Launch-film critique | **Reference only** | It scores against seven launch films' style. It can hint for a teaser, not for a tutorial. |
| Gemini critique (`llm --yes-upload`) | **Conditional on consent** | Uploads audio with the user's own key, and upstream has not validated it. |

The edit is one paragraph in `hyperframes.md` and a row in `sources.md`. A narrated
walkthrough with no music or SFX does not trigger it. Installing it needs approval:
a git clone, a venv and CPU torch, plus about 1.1 GB of models on the first model call.

A fresh read-only subagent (Claude Sonnet, Claude Code) read only the skill files and
answered two briefs after the edit. For SFX added to an approved HyperFrames take, it
proposed the bank with approval, ran the cue-based offset screen and `verify_video.py`,
and reported listening as pending. For a plain narrated walkthrough, it used
`verify_video.py` and the listening gate and left earshot out. Following its notes,
generated effects now need the user's agreement, and the paragraph carries its review
date. This is a policy walkthrough, not a tool trial.

Revisit when the sound bank is tagged in a release, or a real walkthrough with SFX
shows whether the offset screen catches errors that listening missed.
