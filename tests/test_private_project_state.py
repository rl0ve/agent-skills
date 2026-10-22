from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "plugins/work-router/skills/route-ai-work/scripts/private_project_state.py"
SPEC = importlib.util.spec_from_file_location("private_project_state", SCRIPT)
STATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(STATE)


@unittest.skipUnless(os.name == "posix" and os.geteuid() != 0, "POSIX user-mode initialization")
class PrivateProjectStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.storage = self.root / "private"
        self.folder = self.storage / "work-example" / "research"

    def initialize(self):
        return STATE.initialize(self.storage, "work-example", "research", apply=True)

    def inspect(self, **kwargs):
        return STATE.inspect_state(self.folder, "work-example", "research", **kwargs)

    def write_record(self, change):
        path = self.folder / "STATE.json"
        record = json.loads(path.read_text())
        change(record)
        path.write_text(json.dumps(record))

    def task(self, task_id="T1", **changes):
        return {"task_id": task_id, "attempt_id": "A1", "owner": "worker",
                "status": "returned", "input_revision": 0, "dependencies": [], **changes}

    def put_tasks(self, tasks):
        self.write_record(lambda r: r.update(coordinator="coordinator", tasks=tasks))

    def test_preview_makes_no_directories(self):
        result = STATE.initialize(self.storage, "work-example", "research")
        self.assertFalse(result["writes"])
        self.assertFalse(self.storage.exists())

    def test_repo_free_desktop_work_project_initializes_privately(self):
        result = self.initialize()
        self.assertEqual(result["status"], "initialized")
        record = json.loads((self.folder / "STATE.json").read_text())
        self.assertEqual(record["resources"], [])
        self.assertFalse(result["coordinator_assigned"])
        self.assertEqual(result["sync"], "not-provided")
        self.assertEqual(stat.S_IMODE(self.folder.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(self.folder.parent.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(self.storage.stat().st_mode), 0o700)
        for name in ("STATE.json", "INDEX.md", "DECISIONS.md", "KNOWLEDGE.md"):
            self.assertEqual(stat.S_IMODE((self.folder / name).stat().st_mode), 0o600)

    def test_project_can_link_multiple_repositories_and_non_git_resources(self):
        self.initialize()
        self.write_record(lambda r: r.update(resources=[
            {"kind": "repository", "reference": "private-repository-one"},
            {"kind": "repository", "reference": "private-repository-two"},
            {"kind": "document", "reference": "private-document-reference"},
        ]))
        self.assertEqual(self.inspect()["status"], "local-layout-checked")

    def test_existing_state_is_never_overwritten(self):
        self.initialize()
        path = self.folder / "KNOWLEDGE.md"
        path.write_text("Retain this private finding.")
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.initialize()
        self.assertEqual(path.read_text(), "Retain this private finding.")

    def test_git_checkout_and_ignored_subdirectory_are_refused_before_writing(self):
        for marker_type in ("directory", "file"):
            with self.subTest(marker_type=marker_type):
                repo = self.root / marker_type
                repo.mkdir()
                if marker_type == "directory":
                    (repo / ".git").mkdir()
                else:
                    (repo / ".git").write_text("gitdir: elsewhere")
                (repo / ".gitignore").write_text("private/\n")
                with self.assertRaisesRegex(ValueError, "Git placement requires"):
                    STATE.initialize(repo / "private", "personal", "project", apply=True)
                self.assertFalse((repo / "private").exists())

    def test_bare_repository_is_refused(self):
        (self.root / "HEAD").write_text("ref: refs/heads/main")
        (self.root / "objects").mkdir()
        (self.root / "refs").mkdir()
        with self.assertRaisesRegex(ValueError, "bare repository"):
            self.initialize()
        with self.assertRaisesRegex(ValueError, "bare repository"):
            STATE.initialize(self.storage, "work-example", "research", apply=True, allow_git=True)

    def test_state_copied_into_checkout_is_detected(self):
        self.initialize()
        (self.storage / ".git").mkdir()
        with self.assertRaisesRegex(ValueError, "Git placement requires"):
            self.inspect()

    def test_explicit_git_placement_does_not_claim_visibility_or_sync(self):
        self.storage.mkdir()
        (self.storage / ".git").mkdir()
        preview = STATE.initialize(self.storage, "work-example", "research", allow_git=True)
        self.assertEqual(preview["git_placement"], "checkout-explicitly-selected")
        self.assertEqual(preview["repository_visibility"], "not-verified")
        self.assertFalse(self.folder.exists())
        result = STATE.initialize(self.storage, "work-example", "research", apply=True, allow_git=True)
        self.assertEqual(result["repository_visibility"], "not-verified")
        self.assertEqual(result["permissions_scope"], "state-directory-only")
        self.assertEqual(result["git_storage_permissions"], "not-verified")
        self.assertEqual(result["sync"], "not-provided")
        self.assertEqual(list((self.storage / ".git").iterdir()), [])
        self.assertEqual(self.inspect(allow_git=True, expected_revision=0)["revision"], 0)
        with self.assertRaisesRegex(ValueError, "Git placement requires"):
            self.inspect()

    def test_explicit_git_option_preserves_link_and_permission_checks(self):
        self.storage.mkdir()
        (self.storage / ".git").mkdir()
        STATE.initialize(self.storage, "work-example", "research", apply=True, allow_git=True)
        (self.folder / "STATE.json").chmod(0o644)
        with self.assertRaisesRegex(ValueError, "group/other"):
            self.inspect(allow_git=True)
        alias = self.root / "alias"
        alias.symlink_to(self.storage, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "canonical path"):
            STATE.initialize(alias, "work-example", "other", apply=True, allow_git=True)

    def test_cli_git_option_is_explicit_and_does_not_publish(self):
        self.storage.mkdir()
        (self.storage / ".git").write_text("gitdir: synthetic-worktree-metadata")
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(output):
            code = STATE.main(["init", "--root", str(self.storage), "--realm", "work-example",
                               "--project", "research", "--allow-git", "--apply"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["repository_visibility"], "not-verified")
        self.assertEqual((self.storage / ".git").read_text(), "gitdir: synthetic-worktree-metadata")

    @unittest.skipUnless(shutil.which("git"), "Git is needed for the local transfer fixture")
    def test_fresh_git_state_survives_commit_and_local_clone(self):
        repository = self.root / "source-repo"
        clone = self.root / "cloned-repo"
        git_env = {**os.environ, "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}
        def git(*args):
            subprocess.run(["git", *map(str, args)], env=git_env, check=True,
                           capture_output=True, text=True)
        git("init", "-q", repository)
        STATE.initialize(repository / "context", "work-example", "research", apply=True, allow_git=True)
        git("-C", repository, "add", "context")
        git("-C", repository, "-c", "user.name=State Fixture", "-c",
            "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false",
            "commit", "-qm", "Synthetic empty project")
        git("clone", "--quiet", repository, clone)
        folder = clone / "context" / "work-example" / "research"
        # Git does not carry owner-only mode bits; check the documented destination setup.
        for path in [folder, *folder.rglob("*")]:
            path.chmod(0o700 if path.is_dir() else 0o600)
        self.assertTrue((folder / "returns" / ".gitkeep").is_file())
        result = STATE.inspect_state(folder, "work-example", "research", 0, allow_git=True)
        self.assertEqual(result["status"], "local-layout-checked")
        self.assertEqual(result["repository_visibility"], "not-verified")

    def test_symlinked_root_is_refused(self):
        target = self.root / "real"
        target.mkdir()
        self.storage.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "canonical path"):
            self.initialize()
        self.assertEqual(list(target.iterdir()), [])

    def test_symlinked_return_and_hardlinked_state_are_refused(self):
        self.initialize()
        other = self.root / "external"
        other.write_text("private")
        linked = self.folder / "returns" / "result.md"
        linked.symlink_to(other)
        with self.assertRaisesRegex(ValueError, "link"):
            self.inspect()
        linked.unlink()
        os.link(self.folder / "STATE.json", self.root / "copy.json")
        with self.assertRaisesRegex(ValueError, "hard links"):
            self.inspect()

    def test_nested_repository_is_refused(self):
        self.initialize()
        nested = self.folder / "returns" / ".git"
        nested.mkdir(mode=0o700)
        with self.assertRaisesRegex(ValueError, "nested Git"):
            self.inspect()

    def test_group_readable_record_is_reported_without_chmod(self):
        self.initialize()
        path = self.folder / "DECISIONS.md"
        path.chmod(0o640)
        with self.assertRaisesRegex(ValueError, "group/other"):
            self.inspect()
        self.assertEqual(stat.S_IMODE(path.stat().st_mode), 0o640)

    def test_realm_project_and_revision_mismatches_are_rejected(self):
        self.initialize()
        for realm, project, revision in (("personal", "research", None),
                                         ("work-example", "other", None),
                                         ("work-example", "research", 1)):
            with self.subTest(realm=realm, project=project, revision=revision):
                with self.assertRaises(ValueError):
                    STATE.inspect_state(self.folder, realm, project, revision)

    def test_revision_zero_is_a_valid_expected_revision(self):
        self.initialize()
        self.assertEqual(self.inspect(expected_revision=0)["revision"], 0)

    def test_changed_revision_invalidates_an_older_expected_snapshot(self):
        self.initialize()
        self.write_record(lambda r: r.update(revision=1))
        with self.assertRaisesRegex(ValueError, "differs"):
            self.inspect(expected_revision=0)

    def test_accepted_task_requires_evidence_and_acceptance_owner(self):
        self.initialize()
        self.put_tasks([self.task(status="accepted")])
        with self.assertRaisesRegex(ValueError, "result evidence"):
            self.inspect()
        self.put_tasks([self.task(status="accepted", result="returns/T1-A1.md", accepted_by="coordinator")])
        self.assertEqual(self.inspect()["task_count"], 1)

    def test_duplicate_task_records_and_invalid_dependencies_are_rejected(self):
        self.initialize()
        cases = [
            [self.task(), self.task(attempt_id="A2")],
            [self.task(dependencies=["unknown"])],
            [self.task(dependencies=["T1"])],
            [self.task(dependencies=["T2"]), self.task("T2", dependencies=["T1"])],
        ]
        for tasks in cases:
            with self.subTest(tasks=tasks):
                self.put_tasks(tasks)
                with self.assertRaises(ValueError):
                    self.inspect()

    def test_valid_dependency_chain_passes(self):
        self.initialize()
        self.put_tasks([self.task(), self.task("T2", dependencies=["T1"])])
        self.assertEqual(self.inspect()["task_count"], 2)

    def test_assignment_requires_coordinator(self):
        self.initialize()
        self.write_record(lambda r: r.update(tasks=[self.task()]))
        with self.assertRaisesRegex(ValueError, "coordinator"):
            self.inspect()

    def test_missing_coordinator_field_is_a_controlled_schema_error(self):
        self.initialize()
        self.write_record(lambda r: r.pop("coordinator"))
        output = io.StringIO()
        with redirect_stderr(output):
            code = STATE.main(["check", "--state-dir", str(self.folder),
                               "--realm", "work-example", "--project", "research"])
        self.assertEqual(code, 2)
        self.assertIn("declare a coordinator", output.getvalue())
        self.assertNotIn("Traceback", output.getvalue())

    def test_schema_future_inputs_and_duplicate_json_keys_fail(self):
        self.initialize()
        self.put_tasks([self.task(input_revision=1)])
        with self.assertRaisesRegex(ValueError, "ahead"):
            self.inspect()
        self.put_tasks([])
        self.write_record(lambda r: r.update(schema_version=True))
        with self.assertRaisesRegex(ValueError, "schema"):
            self.inspect()
        (self.folder / "STATE.json").write_text('{"revision":0,"revision":1}')
        with self.assertRaisesRegex(ValueError, "duplicate keys"):
            self.inspect()

    def test_incomplete_initialization_is_detected(self):
        self.initialize()
        (self.folder / "INDEX.md").unlink()
        with self.assertRaisesRegex(ValueError, "incomplete"):
            self.inspect()

    def test_deeply_nested_invalid_record_reports_failure_without_payload(self):
        self.initialize()
        (self.folder / "STATE.json").write_text('[' * 1500 + '0' + ']' * 1500)
        output = io.StringIO()
        with redirect_stderr(output):
            code = STATE.main(["check", "--state-dir", str(self.folder),
                               "--realm", "work-example", "--project", "research"])
        self.assertEqual(code, 2)
        self.assertNotIn("Traceback", output.getvalue())

    def test_check_is_read_only_and_does_not_print_private_payload(self):
        self.initialize()
        secret = "PRIVATE-CONTENT-NOT-FOR-OUTPUT"
        self.put_tasks([self.task(owner=secret, result=secret)])
        path = self.folder / "STATE.json"
        before = path.read_bytes(), path.stat().st_mtime_ns
        output = io.StringIO()
        with redirect_stdout(output), redirect_stderr(output):
            code = STATE.main(["check", "--state-dir", str(self.folder),
                               "--realm", "work-example", "--project", "research"])
        self.assertEqual(code, 0)
        self.assertNotIn(secret, output.getvalue())
        self.assertEqual((path.read_bytes(), path.stat().st_mtime_ns), before)

    def test_path_identifiers_are_rejected_without_writing(self):
        for realm, project in (("../public", "project"), ("work", "/tmp/elsewhere")):
            with self.assertRaisesRegex(ValueError, "slugs"):
                STATE.initialize(self.storage, realm, project, apply=True)
        self.assertFalse(self.storage.exists())


if __name__ == "__main__":
    unittest.main()
