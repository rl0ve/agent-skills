# Choose and audit a capability's distribution

Use when choosing how to install a capability, checking an installed package against
upstream, or auditing plugin freshness. This is not a global audit on ordinary work.

## Prefer a maintained plugin

Honor the user's packaging preference. When the user prefers plugins, keep a coherent
capability in a creator-maintained, host-supported plugin rather than unpacking it into
many independently managed skills. Check for an upstream plugin before recommending
standalone skills. A stale directory copy is a reason to inspect the upstream plugin,
not evidence that the host's plugins are generally stale or that skills are preferable.

Choose among these routes using verified coverage and maintenance:

| Route | Choose it when |
|---|---|
| Keep the directory plugin | It provides the needed behavior and its supported update path is adequate; a different source offers no material benefit |
| Update the existing plugin | A newer compatible release is available through its current publisher or marketplace |
| Move to the creator's upstream plugin | The directory copy materially lags and a supported upstream plugin preserves the required contributions |
| Use a narrow standalone skill | No suitable plugin exists, the plugin is incompatible or adds unwanted scope, or a required specialist is available only as a skill |
| Defer | Provenance, parity, access, maintenance, or the host's installation support remains unresolved |

A plugin may include skills, tools, authenticated apps, hooks, runtimes and assets.
Standalone instructions do not replace a connector or reproduce its authentication.
Host-bundled document/browser/runtime packages can depend on private host APIs; retain
their supported distribution unless a tested replacement preserves those capabilities.

## Establish what is installed and where updates come from

Record the review date, host, exact plugin IDs, installed versions, enabled state,
current-session visibility and source/ref. Inspect the selected package's manifest,
skill entrypoints, supporting files and declared contributions. Do not dump private
configuration or credentials. Cached folders and a source checkout are not proof of
installation; the newest cache folder is not proof of the selected version.

On Codex, inspect the current executable's help and use its supported inventory tools.
If a combined listing fails, query known marketplaces separately, for example:

```bash
codex plugin list --marketplace <marketplace> --json
```

Preserve stderr and distinguish a failed catalogue, a configured-but-unlisted package,
an inaccessible source and an out-of-date package. Cross-check config, exact paths
visible in the session and manifests when a listing omits an entry. Report that bounded
fallback; do not present it as a successful catalogue or infer a version from filenames.
Use [deduplicate-skills](../../deduplicate-skills/SKILL.md) for deeper alias/overlap checks.

Verify upstream using the creator's repository, release/tag and host instructions.
Compare versions only within the same release lineage. Compare relevant files or bundle
hashes as well: a wrapper version may differ from the engine version, and skill counts
can change through reorganization. Identify the useful behavior missing or changed.
Do not label an inaccessible source stale or current.

Check the actual publication path. A directory submission, npm release, GitHub branch,
versioned plugin and skills registry may update separately. A plugin manifest in a repo
does not by itself establish a marketplace install path. Verify host support, marketplace
metadata and the selected plugin root before proposing a command. Do not invent public
listings, automatic updates or release synchronization from a manifest or fresh commit.

### Codex and ChatGPT publication paths

Checked October 20, 2026. Three paths update separately; verify each before claiming it.

- **Workspace import.** A ChatGPT workspace admin can import a public or private
  GitHub marketplace (Admin Console, Plugins, Import marketplace). Import reads
  `.agents/plugins/marketplace.json` or `.claude-plugin/marketplace.json`, syncs daily,
  and can add new plugins on sync without per-plugin approval. Repository `policy`
  values such as `AVAILABLE` are **not** applied; the admin sets installation policy
  per plugin ([OpenAI](https://help.openai.com/articles/20001504)). A member cannot
  complete this path; it needs the workspace admin.
- **Portable manifest.** OpenAI recommends a root `plugin.json` (Agent Plugins 1.0
  schema) with skills under `skills/`; `.codex-plugin/plugin.json` remains a
  compatibility overlay for OpenAI-specific settings when the root manifest has no
  `extensions.com.openai` object
  ([OpenAI plugin docs](https://developers.openai.com/plugins/build/plugins.md)).
  Claude Code still reads `.claude-plugin/plugin.json`; keep all three in version parity.
- **Public directory.** Plugins with lifecycle hooks cannot be submitted to OpenAI's
  public directory; distribute them for manual install in Codex desktop instead.
  Claude marketplace listings and approvals do not transfer
  ([submission guide](https://developers.openai.com/plugins/guides/submit-claude-plugin)).
  Plugin-bundled hooks also stay inactive until the user reviews and trusts them.

## Recommend before migrating

For an audit, return an actionable table with exact ID, installed state/source, upstream
evidence, material delta, recommended distribution, contribution/customization risks,
confidence and unresolved checks. Cover all inventoried entries, grouping equivalent
decisions where useful. Keep private machine inventories out of public skill repositories.

An audit authorizes recommendations, not bulk replacement. When migration is authorized,
make the new package concrete and verify it before retiring the old source. Preserve
local modifications and sibling skills, tools, hooks and app connections. Target exact
plugin IDs; similarly named plugins from different marketplaces may be complementary.
Use the smallest supported reversible control that meets the request. Do not interpret
a feature flag such as `--disable` as a plugin-disable command, or assume local config
controls an account-managed remote plugin; verify the resulting state.

Keep one active distribution per interchangeable capability. Do not install standalone
copies alongside the plugin as a freshness workaround, modify managed cache files, or
remove an entire marketplace to replace one package. Retain an explicit restore path.

## Verify and maintain

Verify the package version, source/ref, required files and contributions, then use a
representative low-impact check. A CLI version check proves launch, not rendered quality
or authenticated tool access. Re-read old and new installation/enabled state. Keep
source published, package installed, plugin enabled, session loaded and workflow tested
as separate outcomes; a reload or new session may be needed for discovery.

Document the supported update command and whether checks are manual, automatic or
unknown. Do not create a monitor or schedule unless requested. Revisit the decision
when the directory catches up, the upstream changes its package layout, a required
capability diverges, or an update changes hooks/tools/runtime compatibility.

## Sources and review cases

- [HyperFrames plugin guide](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/plugins.mdx)
  documents separate Codex directory publication and plugin-managed bundled workflows.
- [OpenAI plugin documentation](https://developers.openai.com/codex/plugins/)
  describes plugin packaging; verify the current host's commands locally.

Check these cases when changing this guidance:

- A stale directory video plugin has a compatible maintained upstream plugin: compare
  contributions and move the plugin when authorized, rather than installing every skill.
- A connected calendar plugin has no public skill repository: keep its authenticated
  connector; the absence of a public source is not a freshness defect.
- A uniquely useful standalone specialist has no suitable plugin: retain it rather than
  forcing all skills into a new wrapper or deleting it for visual tidiness.
- A source repo advances but installed files are identical: report no material gap;
  newer commit/version numbers alone do not justify migration.
