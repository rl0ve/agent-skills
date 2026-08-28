from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


root_installer = load_module("root_installer", ROOT / "install.py")
ui_installer = load_module(
    "ui_installer", ROOT / "plugins" / "claude-ui-router" / "scripts" / "install_optional_skills.py"
)
ai_hook = load_module(
    "ai_hook", ROOT / "plugins" / "claude-ai-work-router" / "scripts" / "block_sudo.py"
)
ui_hook = load_module(
    "ui_hook", ROOT / "plugins" / "claude-ui-router" / "scripts" / "block_sudo.py"
)


class RootInstallerTests(unittest.TestCase):
    def test_refuses_root_and_sudo(self):
        with self.assertRaises(SystemExit):
            root_installer.refuse_elevated_execution(0, None)
        with self.assertRaises(SystemExit):
            root_installer.refuse_elevated_execution(501, "501")

    def test_plan_installs_all_plugins_without_sudo(self):
        plugins = root_installer.normalize_plugins(["all"])
        commands = root_installer.build_plan(plugins, "user")
        rendered = [" ".join(command) for command in commands]
        self.assertEqual(len(commands), 4)
        self.assertTrue(any("claude-ai-work-router@rlove-claude-routers" in line for line in rendered))
        self.assertTrue(any("claude-ui-router@rlove-claude-routers" in line for line in rendered))
        self.assertTrue(any("natural-writing@rlove-claude-routers" in line for line in rendered))
        self.assertFalse(any("sudo" in command for line in rendered for command in line.split()))


class SudoHookTests(unittest.TestCase):
    def test_both_hooks_deny_sudo(self):
        payload = {"tool_name": "Bash", "tool_input": {"command": "git status && sudo make install"}}
        for hook in (ai_hook, ui_hook):
            decision = hook.decision_for(payload)
            self.assertIsNotNone(decision)
            self.assertEqual(
                decision["hookSpecificOutput"]["permissionDecision"],
                "deny",
            )

    def test_path_qualified_sudo_is_denied(self):
        payload = {"tool_name": "Bash", "tool_input": {"command": "/usr/bin/sudo launchctl load thing"}}
        self.assertIsNotNone(ai_hook.decision_for(payload))

    def test_safe_command_is_unchanged(self):
        payload = {"tool_name": "Bash", "tool_input": {"command": "npm test"}}
        self.assertIsNone(ai_hook.decision_for(payload))
        self.assertIsNone(ui_hook.decision_for(payload))


class UiInstallerTests(unittest.TestCase):
    def test_refuses_root_and_sudo(self):
        with self.assertRaises(SystemExit):
            ui_installer.refuse_elevated_execution(0, None)
        with self.assertRaises(SystemExit):
            ui_installer.refuse_elevated_execution(501, "501")

    def test_product_profile_preserves_named_stack(self):
        catalog = ui_installer.load_catalog()
        items = ui_installer.resolve_selection(catalog, [], ["product"])
        keys = [item["key"] for item in items]
        self.assertEqual(
            keys,
            [
                "interface-design",
                "impeccable",
                "shadcn-official",
                "jakub-better-stack",
                "ibelick-ui",
                "addy-web-quality",
            ],
        )

    def test_skills_command_targets_claude_code(self):
        catalog = ui_installer.load_catalog()
        item = ui_installer.skill_index(catalog)["interface-design"]
        command = ui_installer.build_command(item, "user", False, False)
        self.assertIn("claude-code", command)
        self.assertIn("--global", command)
        self.assertNotIn("sudo", command)

    def test_impeccable_hooks_are_opt_in(self):
        catalog = ui_installer.load_catalog()
        item = ui_installer.skill_index(catalog)["impeccable"]
        safe_command = ui_installer.build_command(item, "user", False, False)
        hooks_command = ui_installer.build_command(item, "user", False, True)
        self.assertEqual(safe_command[-2:], ["skills", "install"])
        self.assertEqual(hooks_command[-1], "install")
        self.assertNotIn("skills", hooks_command[-2:])


class PackageParityTests(unittest.TestCase):
    def test_ui_router_and_marketplace_versions_match(self):
        plugin_manifest = json.loads(
            (ROOT / "plugins" / "claude-ui-router" / ".claude-plugin" / "plugin.json").read_text()
        )
        marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        listed = next(item for item in marketplace["plugins"] if item["name"] == "claude-ui-router")
        self.assertEqual(plugin_manifest["version"], "1.2.0")
        self.assertEqual(listed["version"], "1.2.0")

    def test_natural_writing_is_a_verified_companion(self):
        catalog = (
            ROOT
            / "plugins"
            / "claude-ui-router"
            / "skills"
            / "route-ui-work"
            / "references"
            / "catalog.md"
        ).read_text()
        self.assertIn("companion; verify installed", catalog)
        self.assertNotIn("local installed lead", catalog)


if __name__ == "__main__":
    unittest.main()
