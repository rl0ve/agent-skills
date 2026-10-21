# Haiku 5.5 routing review

Reviewed October 20, 2026. Claude Haiku 5.5 was released October 7, 2026. This
assessment changes how the `haiku` alias is read and adds one opt-in agent. It does
not change any default route: `work-router:fast-scout` stays at `effort: low`, and
defined implementation stays on `work-router:sonnet-builder`.

## What changed

- **Price.** $0.10 / $0.50 per million input/output tokens for prompts up to 100k
  tokens; $0.50 / $2.50 above 100k. Haiku 4.5 was $1.00 / $5.00 and Sonnet 5.5 is
  $2.00 / $10.00 ([Anthropic](https://www.anthropic.com/claude-haiku-5-5)). The
  up-to-100k rate matches GPT-6 Luna ([Artificial Analysis](https://artificialanalysis.ai/articles/claude-haiku-5-5)).
- **Effort.** First Haiku-class model with adjustable effort: low, medium, high,
  xhigh and max ([Anthropic](https://www.anthropic.com/claude-haiku-5-5)).
- **Alias resolution.** In Claude Code v2.1.293 or later, `haiku` resolves to Haiku
  5.5 on the Anthropic API only. Amazon Bedrock, Google Cloud's Agent Platform
  (Vertex) and Microsoft Foundry still resolve `haiku` to Haiku 4.5
  ([Claude Code model config](https://code.claude.com/docs/en/model-config)).

## Evidence

Vendor figures from [Anthropic](https://www.anthropic.com/claude-haiku-5-5); index
and token figures from [Artificial Analysis](https://artificialanalysis.ai/articles/claude-haiku-5-5).

| Benchmark | Haiku 5.5 | Haiku 4.5 | GPT-6 Luna | Sonnet 5.5 |
|---|---:|---:|---:|---:|
| Terminal-Bench 4.0 | 39.2% | 0.0% | 16.4% | 70.6% |
| OSWorld 2.1 (offline subset) | 72.4% | 15.7% | 48.9% | 83.9% |
| GDPval-AA v2.1 | 1620 | 735 | 1437 | 1840 |
| AA Intelligence Index | 43 (max) / 38 (high) | n.a. | 38 (max) | 56 (max) |

- **Token use.** Haiku 5.5 at max uses about 162k output tokens per index task,
  roughly 3x GPT-6 Luna at max (about 50k). At high it matches Luna's score at about
  55k. Moving from xhigh to max adds 2 index points for about 1.8x the tokens.
- **Long prompts.** Prices step up 5x above 100k tokens. Provisional Artificial
  Analysis cost figures do not include that step-up.

## Routing implications

1. **Read the provider before reading the alias.** A `haiku` route is Haiku 5.5 only
   on the Anthropic API with Claude Code 2.1.293+. On Bedrock, Vertex or Foundry, or an
   older client, it is Haiku 4.5; report that rather than claiming 5.5. Request
   `claude-haiku-5-5` explicitly when revision fidelity matters and the provider offers it.
2. **Scouting stays at low effort.** Narrow lookups and evidence collection are
   latency-bound. Haiku 5.5's gains do not justify raising `fast-scout` effort, and
   high/max token use erodes the price advantage.
3. **General coding stays on Sonnet.** Terminal-Bench 4.0 at 39.2% versus Sonnet 5.5's
   70.6% fails the completed-task economics bar: retries and review would exceed the
   token savings on ordinary implementation.
4. **Opt-in mechanical edits.** `work-router:haiku-builder` (Haiku, high) exists for
   bounded mechanical edits with objective checks: renames, format migrations,
   fixture regeneration, lint-rule fixes. It is **untested in this repository** and is
   used only when the user asks for it or a routing override names it. Do not add it
   to the default table until paired runs against `sonnet-builder` show equal accepted
   output at lower total cost or time.
5. **Browser and computer use.** OSWorld 2.1 at 72.4% makes Haiku 5.5 credible for
   bounded browser checks under supervision. It does not replace a capable parent's
   judgment on what a capture shows.

## Not established

- No matched local Claude Code timing for Haiku 5.5 versus Sonnet 5.5.
- No subscription-burn comparison; API price does not establish plan usage.
- All performance figures are vendor or Artificial Analysis numbers, not repository runs.
