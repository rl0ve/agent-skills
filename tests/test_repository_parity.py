"""Marketplace, manifest and context-budget parity checks."""

from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"

# Skill descriptions load into every session; keep them short.
DESCRIPTION_WORD_LIMIT = 60
# route-ui-work is the largest auto-invocable entrypoint; detail belongs in references.
ROUTE_UI_WORK_WORD_LIMIT = 2400


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def plugin_dirs() -> list[Path]:
    return sorted(p for p in PLUGINS.iterdir() if p.is_dir())


def skill_description(skill_md: Path) -> str:
    text = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError(f"{skill_md} has no frontmatter")
    for line in match.group(1).splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    raise AssertionError(f"{skill_md} has no single-line description")


class MarketplaceParityTests(unittest.TestCase):
    def setUp(self):
        self.claude = load(ROOT / ".claude-plugin" / "marketplace.json")
        self.codex = load(ROOT / ".agents" / "plugins" / "marketplace.json")

    def test_both_marketplaces_list_every_plugin_directory(self):
        on_disk = [p.name for p in plugin_dirs()]
        self.assertEqual(sorted(e["name"] for e in self.claude["plugins"]), on_disk)
        self.assertEqual(sorted(e["name"] for e in self.codex["plugins"]), on_disk)

    def test_claude_entries_point_at_plugin_and_match_version(self):
        for entry in self.claude["plugins"]:
            name = entry["name"]
            self.assertEqual(entry["source"], f"./plugins/{name}", name)
            manifest = load(PLUGINS / name / ".claude-plugin" / "plugin.json")
            self.assertEqual(entry["version"], manifest["version"], name)

    def test_codex_entries_share_one_shape(self):
        for entry in self.codex["plugins"]:
            name = entry["name"]
            self.assertEqual(
                entry["source"], {"source": "local", "path": f"./plugins/{name}"}, name
            )
            self.assertEqual(entry["policy"], {"installation": "AVAILABLE"}, name)
            self.assertIn("category", entry, name)

    def test_marketplace_metadata_version_tracks_ui_router(self):
        ui_router = load(PLUGINS / "ui-router" / ".claude-plugin" / "plugin.json")
        self.assertEqual(self.claude["metadata"]["version"], ui_router["version"])


class ManifestParityTests(unittest.TestCase):
    def test_three_manifests_agree_on_identity(self):
        for plugin in plugin_dirs():
            claude = load(plugin / ".claude-plugin" / "plugin.json")
            codex = load(plugin / ".codex-plugin" / "plugin.json")
            root = load(plugin / "plugin.json")
            for field in ("name", "version", "description"):
                self.assertEqual(claude[field], codex[field], f"{plugin.name} {field}")
                self.assertEqual(claude[field], root[field], f"{plugin.name} {field}")
            self.assertEqual(claude["name"], plugin.name)

    def test_root_manifest_is_portable(self):
        for plugin in plugin_dirs():
            root = load(plugin / "plugin.json")
            self.assertEqual(root.get("$schema"), AGENT_PLUGINS_SCHEMA, plugin.name)
            # The .codex-plugin overlay supplies OpenAI settings only while this is absent.
            self.assertNotIn("extensions", root, plugin.name)
            self.assertNotIn("skills", root, plugin.name)
            self.assertTrue(any((plugin / "skills").glob("*/SKILL.md")), plugin.name)


class ContextBudgetTests(unittest.TestCase):
    def test_skill_descriptions_stay_within_budget(self):
        for skill_md in sorted(PLUGINS.glob("*/skills/*/SKILL.md")):
            words = len(skill_description(skill_md).split())
            self.assertLessEqual(
                words, DESCRIPTION_WORD_LIMIT, f"{skill_md.relative_to(ROOT)}: {words} words"
            )

    def test_route_ui_work_entrypoint_stays_within_budget(self):
        path = PLUGINS / "ui-router" / "skills" / "route-ui-work" / "SKILL.md"
        words = len(path.read_text().split())
        self.assertLessEqual(words, ROUTE_UI_WORK_WORD_LIMIT, f"{words} words")


class InstallerCoverageTests(unittest.TestCase):
    def test_readme_names_every_plugin(self):
        readme = (ROOT / "README.md").read_text()
        for plugin in plugin_dirs():
            self.assertIn(plugin.name, readme, plugin.name)


if __name__ == "__main__":
    unittest.main()
