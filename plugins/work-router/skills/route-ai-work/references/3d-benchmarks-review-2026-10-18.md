# 3D benchmark review: October 18, 2026

Record behind Work Router 1.9.1. The question was whether the
[benchmark source policy](benchmark-sources.md) should name 3D-specific model
evaluations. The leads were four benchmarks posted on X between September 30 and
October 12. The
[UI Router three.js review](https://github.com/rl0ve/agent-skills/blob/main/plugins/ui-router/docs/threejs-builders-review-2026-10-18.md)
declined them as 3D routing policy because model choice belongs to Work Router.
Each was checked at its primary source on October 18. Nothing was run, purchased or
submitted.

## Decisions

| Benchmark | What the primary source shows | Decision |
| --- | --- | --- |
| AA-3D, Artificial Analysis ([launch, Oct 12](https://x.com/ArtificialAnlys/status/2109791341802885209); [board](https://artificialanalysis.ai/evaluations/aa-3d); [methodology](https://artificialanalysis.ai/methodology/aa-3d)) | Version 1.0 has 55 briefs in seven domains. The agent runs in Stirrup in an offline sandbox: 4 CPUs, 8 GB, no GPU, software WebGL. Tools are three.js 0.186.0, optional Rapier 0.20.0 and Blender 4.5, Python 3, Node 22, headless Chromium and CC0 assets. Each brief gets one attempt, up to 250 turns and 3 hours. A scene must load, render and pass review before voting. A recruited panel views each scene for at least 30 seconds, and about one comparison in four is a validation check. Ratings come from a Bradley-Terry fit on an Elo-like scale with 95% sandwich intervals; public votes are excluded. At launch: more than 10,000 counted votes from more than 1,000 panelists across 21 models, the top four statistically tied, and $0.20 to $32.08 per scene. | **Conditional.** Added to the source table for model and effort choices on agent-built interactive three.js scenes. |
| 3JSBench, General Context Labs ([launch, Oct 8](https://x.com/generalcontext_/status/2108313483293147292); [repo](https://github.com/GeneralContext/3jsbench), MIT) | 100 briefs. Each attempt is one request with no tools and no second turn. The output is a three.js 0.184.0 module that returns a `THREE.Group` within mesh and triangle caps. Reasoning effort is high, with a 64K output budget and three attempts through OpenRouter. The grader source "will be released with a forthcoming paper"; the README shows results for one example brief. | **Defer.** Revisit when the grader and full results are published. Even then it measures one-shot generated assets, not agent-built scenes. |
| Blender Bench v1, Refresh ([launch, Sep 30](https://x.com/refresh_dev/status/2105359734287249559); [write-up](https://refresh.dev/blenderbench)) | 20 Blender workflows across 10 task types. Versioned verifiers use numeric checks and, where specified, model-based visual assessment, giving a 0 to 1 reward with partial credit. Only two models: GPT-6 Astra averaged 0.686 for an estimated $55.23 over 20 runs, Claude Opus 5.5 0.642 for $20.54. Effort, harness version and cost basis are not stated. The thread names the Harbor framework, and access to the results is by request. | **Reference only.** A lead for Blender production work. Two models with unstated effort cannot support a route. |
| LuminaBench 3D Seaplane ([scores, Oct 4](https://x.com/LuminaBench/status/2106850337592328658); [test page](https://luminabench.com/tests/3d-seaplane/)) | One seaplane brief and 31 configurations, run in Claude Code, Codex, Antigravity and Grok Build across effort levels, with two stills per run. The brief, scorer, raters, blinding, sample count and index formula are not published. | **Reject** as a routing source. The native-harness and effort spread is unusual; revisit if the scoring method and more briefs are published. |

## What AA-3D does not settle

The board on October 18 put four configurations within overlapping intervals at the
top. Values have moved since launch, so cite the board date.

| Configuration as printed | Elo | 95% interval |
| --- | ---: | --- |
| Claude Sonnet 5.5 (Max, Default Fallback) | 1197 | 1163-1230 |
| Claude Opus 5.5 (Max, Default Fallback) | 1191 | 1157-1225 |
| GPT-6 Astra (Max) | 1166 | 1133-1199 |
| Gemini 4 Argon (High) | 1154 | 1120-1188 |

- **Effort.** Most leading rows are Max. The page does not define "Default Fallback".
  These rows say nothing measured about medium or high effort.
- **Harness.** The Stirrup version is not published, and Stirrup is neither Claude Code
  nor Codex. Results do not transfer to native-harness time or behavior.
- **Runtime.** Software WebGL without a GPU gives no frame-rate or device evidence.
- **Cost.** The board reports average token cost per task, split by token type; the
  methodology page does not state the pricing basis. It is not subscription usage or
  the cost of an accepted result.
- **Variance.** One attempt per brief gives no spread within a brief.
- **Independence.** Artificial Analysis reports that AA-3D Elo tracks its Intelligence
  Index (Pearson 0.92). The two have the same publisher, and the index is still not a
  3D test.

No default route changes. The current Claude Code and Codex starts stay as they are
because AA-3D measures Max-effort preference in another harness. Use it when a 3D
scene build needs a model or effort choice, alongside a bounded local comparison
when the choice is consequential. UI Router keeps the build method, fidelity loop
and acceptance checks.

## Check

A fresh read-only subagent (Claude Sonnet 5.5, Claude Code) read the edited
`benchmark-sources.md` and `SKILL.md` and answered three briefs. This is a policy
walkthrough, not a build or comparative trial.

| Brief | Source it used | Reading |
| --- | --- | --- |
| Claude Code, playable three.js pinball scene, cost matters; AA-3D snapshot with Sonnet 5.5 and Opus 5.5 overlapping at Max | AA-3D | Called the leaders tied, kept the label "Max, Default Fallback" as printed, made no medium-effort claim, and read cost as harness token cost rather than accepted-task cost. Left 3D build method with UI Router. |
| Codex, headless Blender rigging and animation scripts, citing a post that one model "won Blender Bench" | None | AA-3D excludes Blender production. It treated the post as a lead and Blender Bench as not adopted, stated the gap and kept the Codex table route. |
| Claude Code, React analytics dashboard with no 3D | Arena WebDev, as already applied | AA-3D does not apply; table default unchanged. |

Open points it raised: "Default Fallback" is undefined (recorded above), and an
AA-3D snapshot needs its board date to judge whether it is current.

Not measured: whether naming AA-3D changes accepted results, cost or time on a real
3D build.
