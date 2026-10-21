"""Structural checks for Visual Version Review; not an agent behavior benchmark."""

from pathlib import Path
import json
import re
import unittest

from test_packages import root_installer

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "visual-version-review"
SKILL = PLUGIN / "skills" / "visual-version-review"


class VisualVersionReviewTests(unittest.TestCase):
    def test_installer_alias_and_all(self):
        self.assertEqual(
            root_installer.normalize_plugins(["versions"]), ["visual-version-review"]
        )
        self.assertIn("visual-version-review", root_installer.normalize_plugins(["all"]))

    def test_hub_references_resolve(self):
        text = (SKILL / "SKILL.md").read_text()
        references = re.findall(r"`(references/[^`]+)`", text)
        self.assertEqual(len(references), 2)
        for reference in references:
            self.assertTrue((SKILL / reference).is_file(), reference)

    def test_description_is_single_line_quoted_yaml_scalar_and_bounded(self):
        text = (SKILL / "SKILL.md").read_text()
        description = re.search(r'^description: "(.+)"$', text, re.M)
        self.assertIsNotNone(description)
        self.assertLessEqual(len(description.group(1).split()), 50)
        self.assertTrue(text.startswith("---\nname: visual-version-review\n"))

    def test_capture_example_is_parseable_and_has_provenance(self):
        text = (SKILL / "references" / "capture-contract.md").read_text()
        block = re.search(r"```json\n(.*?)\n```", text, re.S)
        self.assertIsNotNone(block)
        version = json.loads(block.group(1))["versions"][0]
        for field in ("id", "branch", "commit", "entry_path", "evidence_type", "dirty_worktree"):
            self.assertIn(field, version)
        capture = version["captures"][0]
        for field in ("state", "file", "viewport", "captured_at", "crop", "interaction_verified"):
            self.assertIn(field, capture)

    def test_no_project_capture_assets_in_skill(self):
        for path in SKILL.rglob("*"):
            if path.is_file():
                self.assertIn(path.suffix, (".md", ".yaml"), str(path))
                self.assertNotIn("world-at-a-glance", path.read_text().lower())

    def test_scope_and_missing_visual_regressions_remain_explicit(self):
        hub = (SKILL / "SKILL.md").read_text()
        verification = (SKILL / "references" / "verification.md").read_text()
        for phrase in ("Do not change the products", "globes separately from flat maps",
                       "never switch publishing providers", "entry path"):
            self.assertIn(phrase, hub)
        for phrase in ("Flat-map captures hide a globe", "One branch contains several approaches",
                       "Should not trigger alone", "disable networking"):
            self.assertIn(phrase, verification)

    def test_codex_discovery_points_to_skill(self):
        manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertIn("$visual-version-review", (SKILL / "agents" / "openai.yaml").read_text())


if __name__ == "__main__":
    unittest.main()
