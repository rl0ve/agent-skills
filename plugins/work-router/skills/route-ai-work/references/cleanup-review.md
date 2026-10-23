# Review cleanup and preservation

Use when the user requests cleanup or a branch, checkout, chat or project is being
retired. This is a scoped extension of the retirement checks in
[execution locations](execution-locations.md#accept-integrate-and-retire), not an audit
to run during ordinary work. Inspect first; make a removal only within the actual
cleanup authority. A request for candidates authorizes a review, not their deletion.

## Identify the resource and the action

| Resource | Establish before recommending removal |
|---|---|
| Chat or archived history | Useful decisions, unique artifacts and links are preserved and accessible. Archiving a chat does not remove its checkout or project entry. |
| Saved project entry | Which actual directory and chats it refers to, including archived history. A stale or empty directory does not establish that its project history is disposable. Use the host's supported project controls. |
| Branch or worktree | Exact current tip, unpublished commits, dirty/untracked files and content preservation under the existing retirement contract. Recheck immediately before removal. |
| Ignored local data | Databases, uploads, generated assets, local configuration and other files outside Git: what is unique, what recovery requires, and which backup actually contains it. |
| Cache or marketplace staging | Measured size, canonical source, active use, supported eviction method and the cost or prerequisites of regeneration. Its name alone does not prove it is disposable. |

Treat each as a separate action. A merged branch, archived chat, removed project entry
and deleted checkout are not evidence that the other actions happened or are authorized.
Remote deployments and service folders remain with their platform's lifecycle owner;
local cleanup does not authorize deleting remote resources.

## Preserve work outside Git

Inventory ignored as well as untracked files in each candidate checkout. Inspect the
purpose of local databases and assets before calling them caches. Regenerable build
output differs from a database containing unique imported or edited records.

Check the exact host archive contract. A recoverable Git snapshot may retain commits
and non-ignored files while excluding ignored data. Preserve needed excluded files in
an authorized private location, keep permissions and a source-to-backup mapping, and
verify recovery by reading or opening the copy. Do not print credentials or publish
private configuration in the cleanup report. If preservation remains uncertain, retain
the resource and state the unresolved requirement.

For a stale Git worktree registration or broken `.git` pointer, map the registration
to its real directory and recover access to unique work before pruning metadata or
removing folders. An inaccessible checkout is not proof that it contains nothing useful.

## Measure disk use separately

If reclaiming space is the outcome, measure actual consumers within the requested scope
before choosing actions. Include relevant caches and staging as well as worktrees; do
not assume the Git checkout is the dominant consumer. Exclude shared/aliased paths from
double counting, note measurement limits, and check for running processes or active
installs before removing files they use. Prefer supported cache controls to ad hoc
deletion. Do not preserve historical machine sizes as permanent thresholds.

Return a short plan: resource, proposed action, measured benefit when relevant, unique
material to preserve, recovery location/check, and any authority still needed. After
authorized cleanup, verify the intended resource changed and retained history and
artifacts remain accessible; report unresolved resources separately.
