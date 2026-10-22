# Set up a work account without mixing project data

Use the same public skills for the method, with separate private work records and
work-approved tools. Installing the skills does not transfer personal projects or
configure a work account. Company policy governs models, plugins, data and storage.

## Codex desktop or CLI

1. In the work environment, confirm the active account/workspace, enabled tools and
   permitted instruction location. Check the current client's help and managed
   controls before installing. Do not assume switching sign-in changes local files,
   `CODEX_HOME`, saved connections or permissions. Use an approved separate OS/user
   profile or configuration environment when actual isolation is required.
2. Install Work Router through the permitted marketplace mechanism, or ask the
   administrator to provide the reviewed public package. For clients exposing the
   inspected CLI commands, the following installs the method only:

   ```bash
   codex plugin marketplace add rl0ve/agent-skills
   codex plugin add work-router@rl0ve-agent-skills
   ```

   Add Research Reports only when that work needs evidence-backed reports. UI Router
   and Natural Writing are independent optional packages. An unavailable marketplace
   is not permission to bypass managed installation controls.
3. Select workflow preferences separately. Review
   [portable preferences](portable-preferences.md) and preview any chosen profile.
   The `rl0ve` profile includes a Codex Astra constraint and conditional goal consent;
   applying it requires that user's choice. Verify Astra in the work model catalog.
   If unavailable, report the conflict and obtain a different explicit work choice;
   do not silently substitute a model or alter the personal profile. A company policy
   can restrict a preference. No profile changes the active model or service tier.
4. Choose an approved private root outside all code repositories and a work realm
   such as `work-example`. On a supported POSIX host, preview and then initialize an
   empty project from the trusted source checkout:

   ```bash
   python3 plugins/work-router/skills/route-ai-work/scripts/private_project_state.py init --realm work-example --project example
   python3 plugins/work-router/skills/route-ai-work/scripts/private_project_state.py init --realm work-example --project example --apply
   ```

   The default is `~/.agent-skills/project-state/work-example/example`; use `--root`
   for an approved alternative. The helper copies empty templates only. It does not
   import personal notes, connect accounts or enable remote sharing. On Windows,
   use the templates with approved private ACLs; automatic initialization is POSIX-only.
5. In private work instructions or the task brief, bind this realm/project to its
   actual storage location, name the coordinator and identify permitted participants.
   Avoid publishing that binding in a repository `AGENTS.md`. No repository is needed:
   documents, folders and chats can be the project's only resources. Shared state is
   project-specific; a broader work reference library contains only approved reusable
   findings, not every project's active tasks.
6. Start a fresh task and verify the loaded skill, selected realm, record revision and
   actual tools. Run the local checker and a small read/return/reconcile exercise using
   synthetic data. Confirm another authorized executor's readback before describing
   the record as shared. Keep installation, profile application, session loading and
   cross-environment access as separate results.

For example, a work-only task instruction can say:

> Use Work Router for this project. Read its private project record from the location
> supplied in this task, keep live records outside repositories, and use only the
> selected work realm. Reconcile the current revision before accepting worker returns.

Fill in the actual binding only on the approved private surface. Realm labels and
owner-only file modes help prevent mistakes; they do not isolate two accounts that
share filesystem access or prevent someone copying data into a public artifact.

## ChatGPT Work and remote execution

ChatGPT Work can run in desktop mode with local files and **without a Git repository**.
When that task's tools can reach the private folder, use the local approach above;
Git is relevant only to resources that actually use it. A desktop application alone
does not prove the task has local filesystem access, and a local plugin installation
does not prove every Work surface can load it. Inspect the actual tools and supported
instruction/skill surface.

For a cloud or remote executor that cannot reach the folder, choose a company-approved
shared document/tracker or pass an explicit revisioned snapshot and collect a return.
Use [the state contract](shared-project-state.md) for ownership and reconciliation.
Do not copy personal cloud credentials, mount home folders or add a synchronization
service to make the example work. Any broader sharing must fit the user's authorization
and the organization's access rules.

Obsidian is an optional Markdown reader/editor for the same private project files.
It is unnecessary for Codex, and installing it or enabling its sync/plugins is a
separate choice. Start with the plain files; add retrieval tooling only when actual
project questions show that links and search are insufficient.
