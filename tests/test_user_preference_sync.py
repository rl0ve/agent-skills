from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
import os
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'plugins/work-router/skills/route-ai-work/scripts/sync_user_preferences.py'
SPEC = importlib.util.spec_from_file_location('user_preferences', SCRIPT)
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


class UserPreferenceSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.target = self.root / 'config' / 'AGENTS.md'
        self.backups = self.root / 'private-backups'
        self.metadata, self.blocks = SYNC.load_profile('rl0ve', 'codex')

    def run_cli(self, *options, host='codex', destination=None):
        args = ['--profile', 'rl0ve', '--host', host,
                '--destination', str(destination or self.target),
                '--backup-dir', str(self.backups), *options]
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(output):
            code = SYNC.main(args)
        return code, output.getvalue()

    def write(self, content):
        self.target.parent.mkdir(parents=True, exist_ok=True)
        self.target.write_bytes(content)

    def test_dry_run_does_not_create_parent_or_backup(self):
        self.assertEqual(self.run_cli()[0], 0)
        self.assertFalse(self.target.parent.exists())
        self.assertFalse(self.backups.exists())

    def test_apply_and_check_are_idempotent(self):
        self.assertEqual(self.run_cli('--check')[0], 1)
        self.assertEqual(self.run_cli('--apply')[0], 0)
        content = self.target.read_bytes()
        modified = self.target.stat().st_mtime_ns
        self.assertEqual(self.run_cli('--check')[0], 0)
        self.assertEqual(self.run_cli('--apply')[0], 0)
        self.assertEqual(self.target.read_bytes(), content)
        self.assertEqual(self.target.stat().st_mtime_ns, modified)
        self.assertFalse(self.backups.exists())
        self.assertEqual(set(SYNC.block_spans(content)), set(self.blocks))

    def test_existing_blocks_update_without_duplication_and_preserve_private_bytes(self):
        prefix = b'Local instructions: keep exact spacing  \r\n'
        middle = b'\r\n<!-- shared-ai-credentials:begin -->\r\nprivate local helper\r\n<!-- shared-ai-credentials:end -->\r\n'
        suffix = b'\r\nUnrelated ending without a newline'
        old = b'<!-- work-router native-goals:begin -->\r\nold goal policy\r\n<!-- work-router native-goals:end -->'
        original = prefix + old + middle + suffix
        self.write(original)
        self.assertEqual(self.run_cli('--apply')[0], 0)
        updated = self.target.read_bytes()
        self.assertTrue(updated.startswith(prefix))
        self.assertIn(middle + suffix, updated)
        self.assertEqual(updated.count(b'<!-- work-router native-goals:begin -->'), 1)
        self.assertNotIn(b'\n', updated.replace(b'\r\n', b''))
        saved = list(self.backups.glob('*.bak'))
        self.assertEqual(len(saved), 1)
        self.assertEqual(saved[0].read_bytes(), original)
        self.assertNotIn('private local helper', self.run_cli('--check')[1])

    def test_update_existing_complete_profile_preserves_outside_bytes_exactly(self):
        blocks = list(self.blocks.values())
        original = b'prefix\x00\n' + b'\nPRIVATE BETWEEN\n'.join(blocks) + b'\ntrailing  '
        changed = dict(self.blocks)
        changed['native-goals'] = changed['native-goals'].replace(b'Conditional native goals', b'Updated native goals')
        result = SYNC.merge_blocks(original, changed)
        self.assertEqual(result, original.replace(b'Conditional native goals', b'Updated native goals'))

    def test_windows_profile_checkout_and_destination_preserve_crlf(self):
        import shutil
        profiles = self.root / 'profiles'
        shutil.copytree(SYNC.PROFILE_ROOT, profiles)
        for template in (profiles / 'rl0ve').glob('*.md'):
            template.write_bytes(template.read_bytes().replace(b'\n', b'\r\n'))
        self.write(b'Private Windows instructions\r\n')
        with patch.object(SYNC, 'PROFILE_ROOT', profiles):
            self.assertEqual(self.run_cli('--apply')[0], 0)
            content = self.target.read_bytes()
            self.assertNotIn(b'\r\r\n', content)
            self.assertNotIn(b'\n', content.replace(b'\r\n', b''))
            self.assertEqual(self.run_cli('--check')[0], 0)

    def test_remove_only_selected_blocks(self):
        original = b'private prefix\n' + b'\n'.join(self.blocks.values()) + b'\nprivate suffix'
        self.write(original)
        self.assertEqual(self.run_cli('--remove')[0], 0)
        self.assertEqual(self.target.read_bytes(), original)
        self.assertEqual(self.run_cli('--remove', '--apply')[0], 0)
        self.assertEqual(self.target.read_bytes(), b'private prefix\n\n\n\nprivate suffix')

    def test_malformed_duplicate_and_nested_markers_fail_without_writing(self):
        start = b'<!-- work-router native-goals:begin -->'
        end = b'<!-- work-router native-goals:end -->'
        malformed = [start, end, start + start + end + end,
                     start + end + start + end,
                     start + b'<!-- work-router override:end -->',
                     b'<!--  work-router native-goals:begin -->\nold\n<!--  work-router native-goals:end -->',
                     b'<!-- Work-Router native-goals:begin -->',
                     b'<!-- work-router native-goals:begin',
                     b'<!-- work-router native-goals:begin\r\nold\r\n',
                     b'<!-- work-router native_goals:begin -->']
        for content in malformed:
            with self.subTest(content=content):
                self.write(content)
                self.assertEqual(self.run_cli('--apply')[0], 2)
                self.assertEqual(self.target.read_bytes(), content)
                self.assertFalse(self.backups.exists())

    def test_file_and_ancestor_symlinks_are_rejected(self):
        real = self.root / 'real'
        real.mkdir()
        other = real / 'AGENTS.md'
        other.write_text('private')
        link = self.root / 'linked'
        link.symlink_to(real, target_is_directory=True)
        self.assertEqual(self.run_cli('--apply', destination=link / 'nested' / 'AGENTS.md')[0], 2)
        self.target.parent.mkdir()
        self.target.symlink_to(other)
        self.assertEqual(self.run_cli('--apply')[0], 2)
        self.assertEqual(other.read_text(), 'private')

    def test_hardlinked_instruction_file_is_rejected(self):
        self.write(b'private')
        os.link(self.target, self.root / 'second-link')
        self.assertEqual(self.run_cli('--apply')[0], 2)
        self.assertEqual(self.target.read_bytes(), b'private')

    def test_atomic_replace_failure_leaves_original_and_backup(self):
        self.write(b'original')
        with patch.object(SYNC.os, 'replace', side_effect=PermissionError('denied')):
            self.assertEqual(self.run_cli('--apply')[0], 2)
        self.assertEqual(self.target.read_bytes(), b'original')
        self.assertEqual(list(self.backups.glob('*.bak'))[0].read_bytes(), b'original')
        self.assertEqual(list(self.target.parent.iterdir()), [self.target])

    def test_changed_original_is_not_overwritten(self):
        self.write(b'newer concurrent content')
        with self.assertRaisesRegex(ValueError, 'changed after preview'):
            SYNC.apply_change(self.target, b'older content', b'replacement', True, self.backups)
        self.assertEqual(self.target.read_bytes(), b'newer concurrent content')
        self.assertFalse(self.backups.exists())

    def test_permission_mode_is_preserved(self):
        self.write(b'private')
        self.target.chmod(0o640)
        self.assertEqual(self.run_cli('--apply')[0], 0)
        self.assertEqual(stat.S_IMODE(self.target.stat().st_mode), 0o640)
        self.assertEqual(stat.S_IMODE(list(self.backups.glob('*.bak'))[0].stat().st_mode), 0o600)

    def test_custom_codex_home_and_active_override(self):
        with patch.dict(os.environ, {'CODEX_HOME': str(self.root / 'custom-codex')}):
            expected = self.root / 'custom-codex' / 'AGENTS.md'
            self.assertEqual(SYNC.default_destination('codex'), expected)
            expected.parent.mkdir()
            override = expected.with_name('AGENTS.override.md')
            override.write_text('temporary preference')
            self.assertEqual(SYNC.default_destination('codex'), override)
            self.assertEqual(self.run_cli('--apply', destination=expected)[0], 2)
            self.assertFalse(expected.exists())
            self.assertEqual(override.read_text(), 'temporary preference')

    def test_custom_claude_home_and_host_specific_model_scope(self):
        with patch.dict(os.environ, {'CLAUDE_CONFIG_DIR': str(self.root / 'custom-claude')}):
            self.assertEqual(SYNC.default_destination('claude-code'), self.root / 'custom-claude' / 'CLAUDE.md')
        _, claude = SYNC.load_profile('rl0ve', 'claude-code')
        self.assertEqual(claude['native-goals'], self.blocks['native-goals'])
        self.assertNotIn('override', claude)
        self.assertNotIn(b'gpt-6-astra', b'\n'.join(claude.values()))
        self.assertIn(b'gpt-6-astra', self.blocks['override'])

    def test_print_does_not_read_or_modify_destination(self):
        self.write(b'LOCAL SECRET DO NOT PRINT')
        code, output = self.run_cli('--print')
        self.assertEqual(code, 0)
        self.assertNotIn('LOCAL SECRET', output)
        self.assertEqual(self.target.read_bytes(), b'LOCAL SECRET DO NOT PRINT')
        self.assertFalse(self.backups.exists())

    def test_profile_path_escape_and_unknown_host_cannot_load(self):
        for name in ['../rl0ve', '/tmp/profile', 'missing-profile']:
            with self.subTest(name=name), self.assertRaises((ValueError, OSError)):
                SYNC.load_profile(name, 'codex')
        with self.assertRaises(ValueError):
            SYNC.load_profile('rl0ve', 'unknown')

    def test_root_or_sudo_execution_is_refused(self):
        with patch.object(SYNC.os, 'geteuid', return_value=0, create=True):
            self.assertEqual(self.run_cli('--apply')[0], 2)
        with patch.dict(os.environ, {'SUDO_UID': '123'}):
            self.assertEqual(self.run_cli('--apply')[0], 2)
        self.assertFalse(self.target.parent.exists())


if __name__ == '__main__':
    unittest.main()
