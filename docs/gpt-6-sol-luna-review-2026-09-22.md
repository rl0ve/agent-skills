# GPT-6 Sol and GPT-6 Luna routing review

Historical release review. Its Sol-default direction is refined by the
[current four-model assessment](gpt-6-family-routing-review-2026-09-22.md) and active
Work Router policy; retain this file as the record of the earlier release.

Reviewed September 22, 2026 for Work Router 1.8.0 and UI Router 1.17.0. In this
repository, **UI Router is the design router**; there is no separate `design-router`
plugin. Work Router owns model, effort, delegation, and service-tier choices. UI Router
owns design-lead selection, specialist chains, visual references, and acceptance.

## Sources and evidence boundary

The current source set is OpenAI's [latest-model guidance](https://developers.openai.com/api/docs/guides/latest-model),
[GPT-6 Sol model page](https://developers.openai.com/api/docs/models/gpt-6-sol), and
[GPT-6 Luna model page](https://developers.openai.com/api/docs/models/gpt-6-luna), plus
the host catalog that must be checked at routing time. Release positioning supports a
task-fit policy; it does not by itself establish comparative visual taste, wall-clock
latency, cost per completed task, or the best effort setting for every workload.

Keep GPT-5.6 benchmark tables as historical evidence rather than relabeling them as
GPT-6 measurements. Astra remains a valid explicit or already-running route because a
release is not a reason to discard useful loaded context. Terra remains conditional on current host
availability rather than being silently renamed or removed.

## Decisions

| Question | Decision | Why |
|---|---|---|
| Default for new demanding Codex work | GPT-6 Sol | It owns ambiguous judgment, broad implementation, integration, and final verification. |
| Narrow implementation | GPT-6 Luna high | Use only with stable scope and objective acceptance criteria. |
| Cost-first background work | GPT-6 Luna max | Retains the named economy exception; do not turn it into the interactive default. |
| Existing Astra work | Preserve it when progressing | Family switches duplicate context and can erase useful momentum. |
| Independent reading | Terra when currently available, otherwise a bounded read-only Sol route | The role matters more than preserving a stale family assumption. |
| UI and design work | Sol for direction and broad builds; Luna only for bounded mechanical work | Model choice does not replace the selected design lead, rendered inspection, responsive checks, or exercised interaction. |
| Installed GPT-5.6 profiles | Refresh explicitly with the sync workflow | Updating the repository does not mutate user or project profile directories. |

## UI-specific implications

GPT-6 Sol may own consequential design synthesis or a broad implementation, but UI
Router still composes the canonical design chain first. A Sol route must inspect the
rendered result and compare it with the brief; the model name is not acceptance
evidence. GPT-6 Luna fits token renames, scoped component changes, focused tests, and
other work where both the intended result and checks are explicit. It is not the route
for unresolved art direction, product decisions, accessibility tradeoffs, or final
visual judgment.

The Claude fallback agents remain unchanged. UI Router does not impose a second model
ladder, and neither release justifies automatic subagents, image generation, 3D, or a
service-tier change.

## Applicable and non-trigger cases

| Case | Expected route |
|---|---|
| New cross-system UI redesign with unresolved hierarchy and interaction | GPT-6 Sol owns synthesis and broad implementation; UI Router supplies the design chain and rendered acceptance. |
| One established component needs a deterministic token migration | Keep it in the parent when trivial, or use GPT-6 Luna high as sole writer when delegation pays. |
| Luna encounters an unresolved product-state decision | Stop the bounded worker and return the decision to the Sol parent. |
| An Astra parent already holds the brief and is implementing successfully | Continue in Astra; do not switch merely because GPT-6 Sol is newer. |
| A polished screenshot has not exercised the primary action | Leave acceptance incomplete regardless of model. |
| The user explicitly chooses a supported model | Honor that choice across children; do not silently substitute the new defaults. |

## What would justify another change

Revisit these defaults when current official guidance changes, the host catalog changes
model or effort support, or comparable end-to-end measurements cover the actual task
shape. Keep model availability, benchmark results, UI quality evidence, and routing
policy as separate claims.
