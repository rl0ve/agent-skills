# AI Work Routing

Choose the task, then the harness, then the model and reasoning effort.

## Choose a Timeliness Mode First

- Fast: minimize wall-clock time. Use Sol Medium.
- Balanced: optimize quality per minute. Use Sol High.
- Economy/background: minimize cost and tolerate delay. Use Luna Max.
- Simple + fast: use Luna High for narrow, verifiable work.
- Quality-first: use Sol Max, or hand off bounded judgment/review to Opus 5.
- Never infer completion time from steps, tokens, time to first token, or output speed.

## Primary Defaults

- Interactive coding, planning, research, and analysis: GPT-5.6 Sol at Medium.
- Consequential implementation, architecture, debugging, or review: Sol at High.
- Difficult asynchronous engineering: Sol at XHigh.
- Final visual artifact generation or last-resort escalation: Sol at Max.
- High-volume scoped work, tests, extraction, triage, and small fixes: Luna at High.
- Cost-dominant background work with clear acceptance criteria: Luna at Max.
- Four-agent Ultra mode: only for independent workstreams with separate ownership.

## Delegation

- Keep the parent focused on requirements, decisions, integration, and final verification.
- Delegate exploration, tests, log analysis, documentation checks, and independent review.
- Prefer Luna High for narrow workers and Sol High for reviewers or planners.
- Parallelize read-heavy work.
- Serialize edits when agents may touch overlapping files.
- Require every subagent to return a concise evidence-based summary, not raw transcripts.

## Task Rules

- Executive narrative: use Sol High. Use Max only for the final critical pass.
- Presentations, documents, and spreadsheets: use Sol Max for the final rendered artifact.
- Frontend: use Sol High, run the app, inspect desktop and mobile, and verify the rendered result.
- Data transforms: Luna Medium or High is acceptable when the task is deterministic and verifiable.
- Large-context synthesis: never use Luna; use Sol or a dedicated research workflow.
- Long-running OpenAI workflows: use the Responses API, pass the previous response ID, and compact instead of truncating.

## Harness Rules

- Keep Codex as the native OpenAI execution harness.
- Do not call Claude through an OpenAI-compatible shim as the default.
- A mixed workflow is allowed for a bounded asynchronous implementation, second review, independent test, or Anthropic-content-to-Sol-render handoff.
- Use one parent harness and one bounded specialist in an isolated worktree.
- Every handoff must specify objective, inputs, allowed files, acceptance criteria, and the required return: diff, tests, summary, and risks.
- Never allow overlapping edits, repeated full-context transfer, or recursive Codex-to-Claude-to-Codex delegation.
- Stay native when the user needs an interactive answer or one reasoning-effort increase would solve the task.
- Document model, effort, harness, and relevant settings when reporting benchmark results.

## Quality Gates

- Coding: run relevant tests and report exact results.
- Frontend: inspect the rendered UI at desktop and mobile widths.
- Documents and presentations: render and visually inspect every page or slide.
- Research: attach sources to factual claims.
- Executive writing: surface the decision, rationale, tradeoffs, risks, and explicit ask.
