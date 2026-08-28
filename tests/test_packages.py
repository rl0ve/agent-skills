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
    "ui_installer", ROOT / "plugins" / "ui-router" / "scripts" / "install_optional_skills.py"
)
ai_hook = load_module(
    "ai_hook", ROOT / "plugins" / "work-router" / "scripts" / "block_sudo.py"
)
ui_hook = load_module(
    "ui_hook", ROOT / "plugins" / "ui-router" / "scripts" / "block_sudo.py"
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
        self.assertTrue(any("work-router@rl0ve-agent-skills" in line for line in rendered))
        self.assertTrue(any("ui-router@rl0ve-agent-skills" in line for line in rendered))
        self.assertTrue(any("natural-writing@rl0ve-agent-skills" in line for line in rendered))
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
    def test_every_plugin_version_matches_its_marketplace_entry(self):
        """Derived, not hardcoded: a pinned literal here went stale the first time
        a plugin was bumped, and the test failed for the wrong reason."""
        marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
        for listed in marketplace["plugins"]:
            src = ROOT / listed["source"].lstrip("./")
            manifest = json.loads((src / ".claude-plugin" / "plugin.json").read_text())
            self.assertEqual(
                manifest["version"], listed["version"],
                f"{listed['name']}: plugin.json says {manifest['version']}, "
                f"marketplace.json says {listed['version']}",
            )

    def test_dual_agent_plugins_agree_across_both_manifests(self):
        """A plugin installable by both agents must present the same name, version
        and skills root to each, or the two installs quietly diverge."""
        for plugin_dir in sorted((ROOT / "plugins").iterdir()):
            claude = plugin_dir / ".claude-plugin" / "plugin.json"
            codex = plugin_dir / ".codex-plugin" / "plugin.json"
            if not (claude.exists() and codex.exists()):
                continue
            c, x = json.loads(claude.read_text()), json.loads(codex.read_text())
            self.assertEqual(c["name"], x["name"], plugin_dir.name)
            self.assertEqual(c["version"], x["version"], plugin_dir.name)
            self.assertEqual(
                c.get("skills", "./skills/").rstrip("/"),
                x.get("skills", "./skills/").rstrip("/"),
                plugin_dir.name,
            )

    def test_natural_writing_is_a_verified_companion(self):
        catalog = (
            ROOT
            / "plugins"
            / "ui-router"
            / "skills"
            / "route-ui-work"
            / "references"
            / "catalog.md"
        ).read_text()
        self.assertIn("companion; verify installed", catalog)
        self.assertNotIn("local installed lead", catalog)


if __name__ == "__main__":
    unittest.main()
