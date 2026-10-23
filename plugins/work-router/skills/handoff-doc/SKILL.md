---
name: handoff-doc
description: Create or update a project handoff or decision record with an asset index, sourced decisions, verified artifact state, open questions and next actions. Use before a context switch or when the user asks for a handoff, decision record, or instructions for the next chat or teammate. Update the existing record rather than creating a competing one.
---

# Handoff and decision record

Leave a record a cold reader can act on without this conversation. Find and update the
existing handoff, preserving its name and useful structure. Otherwise use one Markdown
file, normally `RESEARCH-ASSETS.md`, in the authorized project location. Keep private
project information outside public Git history; use an approved private record when needed.

## Build the record

Scale to the work. A short documentation handoff may need only assets, decisions and
next actions. Do not add empty sections or deployment bookkeeping to a prose-only task.

1. **Where everything lives:** exact paths or URLs for source, assets, designs, tickets,
   exports and deployed surfaces. If a needed asset exists only in chat, save it within
   the authorized scope and link the file. Identify the authoritative copy for each item;
   do not assume a local checkout is newer than a cloud editor or that either is a superset.
2. **Standing decisions and precedence:** who decided what, when and from which source.
   Use a short exact quote when available and useful; distinguish paraphrase and inference.
   Resolve authority by field or purpose rather than declaring one source universally right.
3. **Decisions applied:** what changed, where and why. Record reversals with their reason;
   retain useful history without reproducing the conversation.
4. **Deferred work and open questions:** what remains, why, its owner or decision forum,
   and the evidence or access needed to proceed. Preserve unknowns.
5. **Work queue:** ordered next actions with status and a concrete finish condition.
6. **Operational notes:** relevant prerequisites, broken tooling, running jobs and handles,
   workarounds, and release or environment traps.

## Verify artifact state when delivery has several surfaces

For software, demos, workshops or other work with saved, exported or deployed copies,
add a compact table to that same record. Combine columns when it improves readability.

| Artifact | Authoritative surface and revision | Saved / packaged / published / deployed | Last verified behavior | Remaining action |
|---|---|---|---|---|
| Exact name or path | Local or cloud path/URL; commit, version or export time when available | State of each relevant copy, with its revision; unknown stays unknown | What actually passed, where, on which revision and when; otherwise untested | Exact next action and prerequisite |

Use only applicable states. A local edit, saved cloud edit, packed export, pushed commit,
published package, deployed build and successful live run establish different facts.
Do not label the overall delivery complete while a required state remains unverified.
An older export remains stale until regenerated from the current authoritative source.
If copies diverge, name the unresolved differences and the reconciliation action.

For a demo or workshop, include starter/completed variants, resource bindings and runtime
prerequisites only where relevant. Record which performers or paths ran end to end and
which still require rehearsal. A successful local check does not establish a live run.
Recording that a run is needed does not authorize executing or deploying it.

## Finish and maintain

- Refresh the record after the final relevant mutation; recheck a saved/exported revision
  if subsequent edits could have made it stale. Update the same record in the same turn.
- Read it as a cold reader: can you locate the current source, distinguish verified from
  assumed state, and perform the next action with the stated prerequisites?
- Cite the evidence that establishes a decision or state. Do not invent timestamps,
  versions, quotes, successful checks or ownership to fill the table.
- Follow current host and user permissions for memory writes. Create or update a memory
  pointer only when authorized; creating a handoff is not consent to write memory.
- Work Router retains coordination and acceptance ownership. This skill records accepted
  decisions and delivery state; it does not create another coordinator or change authority.
