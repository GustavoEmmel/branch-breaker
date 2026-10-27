"""Installer regression checks; all filesystem mutations stay in temporary homes."""

import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


INSTALLER_PATH = Path(__file__).resolve().parents[1] / "install.py"
SPEC = importlib.util.spec_from_file_location("branch_breaker_install", INSTALLER_PATH)
INSTALLER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = INSTALLER
SPEC.loader.exec_module(INSTALLER)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="branch-breaker-install-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        # Spaces are intentional: paths must not be interpreted as shell arguments.
        self.home = self.root / "home directory"
        self.home.mkdir()
        self.source = self.root / "source checkout"
        self.make_source(self.source)
        self.shared = self.home / ".agents/skills/branch-breaker"
        self.codex = self.home / ".codex/skills/branch-breaker"
        self.claude = self.home / ".claude/skills/branch-breaker"
        self.cursor = self.home / ".cursor/skills/branch-breaker"
        self.backups = self.home / ".local/state/branch-breaker/backups"

    @staticmethod
    def make_source(path):
        (path / "agents").mkdir(parents=True)
        (path / "references").mkdir()
        (path / "SKILL.md").write_text(
            "---\nname: branch-breaker\ndescription: Test fixture\n---\n# Skill\n"
        )
        (path / "agents/openai.yaml").write_text(
            'interface:\n  display_name: "Branch Breaker"\n'
        )
        (path / "references/probes.md").write_text("Fixture reference\n")
        (path / "references/report-contract.md").write_text("Fixture report contract\n")
        for name in ("adversarial-probes", "web-execution", "mobile-execution", "pr-reporting",
                     "full-stack-quality", "learning-sources"):
            (path / f"references/{name}.md").write_text("Fixture execution reference\n")

    def paths(self, codex=None):
        return [self.shared, codex or self.codex, self.claude, self.cursor]

    def assert_installed(self, source=None, codex=None):
        source = (source or self.source).resolve()
        for path in self.paths(codex):
            with self.subTest(path=path):
                self.assertEqual(path.resolve(strict=True), source)
                self.assertEqual(
                    (path / "SKILL.md").read_bytes(), (source / "SKILL.md").read_bytes()
                )
                self.assertEqual(
                    (path / "references/probes.md").read_bytes(),
                    (source / "references/probes.md").read_bytes(),
                )
        self.assertFalse(os.path.lexists(source / "branch-breaker"))

    def backup_entries(self):
        """List entries without following potentially cyclic backed-up links."""
        if not self.backups.exists():
            return []
        entries = []
        for root, dirs, files in os.walk(self.backups, followlinks=False):
            entries.extend(Path(root) / name for name in dirs + files)
        return entries

    def assert_backed_up_text(self, text):
        copies = [
            path
            for path in self.backup_entries()
            if not path.is_symlink() and path.is_file() and path.read_text() == text
        ]
        self.assertTrue(copies, "The displaced user's content must survive in backups")

    def test_fresh_install_links_all_agents_and_shared_directory(self):
        INSTALLER.install(self.source, self.home)
        self.assert_installed()
        for path in self.paths():
            self.assertTrue(path.is_symlink())
        self.assertEqual(self.backup_entries(), [])

    def test_rerun_preserves_working_links_and_creates_no_backups(self):
        INSTALLER.install(self.source, self.home)
        original_inodes = {path: path.lstat().st_ino for path in self.paths()}

        INSTALLER.install(self.source, self.home)
        # The installer also works when invoked through an installed skill path.
        INSTALLER.install(self.shared, self.home)
        INSTALLER.install(self.claude, self.home)

        self.assert_installed()
        self.assertEqual(
            {path: path.lstat().st_ino for path in self.paths()}, original_inodes
        )
        self.assertEqual(self.backup_entries(), [])

    def test_migrates_plain_copy_preserving_user_content_and_existing_links(self):
        shutil.copytree(self.source, self.shared)
        (self.shared / "local-notes.txt").write_text("Preserve my local notes")
        self.codex.parent.mkdir(parents=True)
        self.codex.symlink_to(self.shared, target_is_directory=True)
        self.claude.parent.mkdir(parents=True)
        self.claude.symlink_to("../../.agents/skills/branch-breaker", target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        self.assert_backed_up_text("Preserve my local notes")
        self.assertFalse((self.source / "local-notes.txt").exists())

    def test_preserves_displaced_real_agent_directory(self):
        self.cursor.mkdir(parents=True)
        (self.cursor / "work.txt").write_text("User's existing Cursor skill")

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        self.assert_backed_up_text("User's existing Cursor skill")

    def test_replaces_wrong_link_without_changing_its_target(self):
        valuable = self.root / "unrelated skill"
        valuable.mkdir()
        (valuable / "data.txt").write_text("Keep this target untouched")
        self.cursor.parent.mkdir(parents=True)
        self.cursor.symlink_to(valuable, target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        self.assertEqual((valuable / "data.txt").read_text(), "Keep this target untouched")
        self.assertEqual(list(valuable.iterdir()), [valuable / "data.txt"])
        self.assertTrue(
            any(p.is_symlink() and os.readlink(p) == str(valuable) for p in self.backup_entries())
        )

    def test_repairs_dangling_and_self_referencing_destination_links(self):
        self.shared.parent.mkdir(parents=True)
        self.shared.symlink_to("branch-breaker", target_is_directory=True)
        self.codex.parent.mkdir(parents=True)
        self.codex.symlink_to(self.root / "missing checkout", target_is_directory=True)
        self.claude.parent.mkdir(parents=True)
        self.claude.symlink_to("branch-breaker", target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        backed_links = [p for p in self.backup_entries() if p.is_symlink()]
        self.assertGreaterEqual(len(backed_links), 3)

    def test_repairs_nested_link_to_source_and_preserves_the_link_entry(self):
        nested = self.source / "branch-breaker"
        nested.symlink_to(self.source, target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        self.assertTrue(
            any(p.is_symlink() and os.readlink(p) == str(self.source) for p in self.backup_entries())
        )

    def test_repairs_nested_self_loop(self):
        nested = self.source / "branch-breaker"
        nested.symlink_to("branch-breaker", target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assert_installed()
        self.assertTrue(
            any(p.is_symlink() and os.readlink(p) == "branch-breaker" for p in self.backup_entries())
        )

    def test_source_at_shared_install_location_remains_a_real_directory(self):
        shutil.copytree(self.source, self.shared)
        original_inode = self.shared.stat().st_ino

        INSTALLER.install(self.shared, self.home)
        INSTALLER.install(self.shared, self.home)

        self.assert_installed(source=self.shared)
        self.assertFalse(self.shared.is_symlink())
        self.assertEqual(self.shared.stat().st_ino, original_inode)
        self.assertEqual(self.backup_entries(), [])

    def test_codex_home_override_leaves_default_codex_directory_unused(self):
        custom = self.root / "custom codex home"
        custom_skill = custom / "skills/branch-breaker"

        INSTALLER.install(self.source, self.home, codex_home=custom)

        self.assert_installed(codex=custom_skill)
        self.assertFalse(os.path.lexists(self.codex))
        self.assertFalse((self.home / ".codex").exists())

    def test_cli_installs_without_input_and_reruns_through_installed_path(self):
        shutil.copy2(INSTALLER_PATH, self.source / "install.py")
        environment = os.environ.copy()
        environment["HOME"] = str(self.home)
        environment.pop("CODEX_HOME", None)

        for entry in [self.source / "install.py", self.claude / "install.py"]:
            with self.subTest(entry=entry):
                result = subprocess.run(
                    [sys.executable, str(entry)],
                    env=environment,
                    stdin=subprocess.DEVNULL,
                    capture_output=True,
                    text=True,
                    timeout=10,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assert_installed()

        self.assertEqual(self.backup_entries(), [])

    def test_unrelated_nested_link_is_not_removed_by_loop_repair(self):
        unrelated = self.root / "related documentation"
        unrelated.mkdir()
        (unrelated / "keep.txt").write_text("Not an installer-created loop")
        nested = self.source / "branch-breaker"
        nested.symlink_to(unrelated, target_is_directory=True)

        INSTALLER.install(self.source, self.home)

        self.assertTrue(nested.is_symlink())
        self.assertEqual(nested.resolve(), unrelated.resolve())
        self.assertEqual((nested / "keep.txt").read_text(), "Not an installer-created loop")
        self.assertEqual(self.backup_entries(), [])
        for path in self.paths():
            self.assertEqual(path.resolve(strict=True), self.source.resolve())

    def test_invalid_source_fails_before_replacing_existing_install(self):
        shutil.copytree(self.source, self.shared)
        marker = self.shared / "keep.txt"
        marker.write_text("Existing install survives validation failure")
        for missing in ["SKILL.md", "agents/openai.yaml", "references", "references/report-contract.md",
                        "references/adversarial-probes.md", "references/web-execution.md",
                        "references/mobile-execution.md", "references/pr-reporting.md",
                        "references/full-stack-quality.md", "references/learning-sources.md"]:
            with self.subTest(missing=missing):
                invalid = self.root / ("invalid " + missing.replace("/", "-"))
                self.make_source(invalid)
                item = invalid / missing
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

                with self.assertRaises(ValueError):
                    INSTALLER.install(invalid, self.home)

                self.assertEqual(marker.read_text(), "Existing install survives validation failure")
                self.assertFalse(self.shared.is_symlink())
                self.assertEqual(self.backup_entries(), [])
                self.assertFalse(self.codex.parent.exists())

    def test_nested_source_is_rejected_before_any_install_mutation(self):
        nested = self.shared / "checkout"
        self.make_source(nested)
        marker = self.shared / "keep.txt"
        marker.write_text("Do not move the source's parent")

        with self.assertRaises(ValueError):
            INSTALLER.install(nested, self.home)

        self.assertEqual(marker.read_text(), "Do not move the source's parent")
        self.assertTrue((nested / "SKILL.md").is_file())
        self.assertFalse(self.shared.is_symlink())
        self.assertFalse(self.codex.parent.exists())
        self.assertFalse(self.claude.parent.exists())
        self.assertFalse(self.cursor.parent.exists())
        self.assertEqual(self.backup_entries(), [])

    def test_source_inside_agent_destination_is_rejected_before_mutation(self):
        nested = self.cursor / "checkout"
        self.make_source(nested)

        with self.assertRaises(ValueError):
            INSTALLER.install(nested, self.home)

        self.assertFalse(self.shared.parent.exists())
        self.assertFalse(self.codex.parent.exists())
        self.assertFalse(self.claude.parent.exists())
        self.assertTrue((nested / "SKILL.md").is_file())
        self.assertEqual(self.backup_entries(), [])

    @staticmethod
    def tree_snapshot(root):
        snapshot = {}
        for path in root.rglob("*"):
            relative = str(path.relative_to(root))
            if path.is_symlink():
                snapshot[relative] = ("link", os.readlink(path))
            elif path.is_dir():
                snapshot[relative] = ("directory", None)
            else:
                snapshot[relative] = ("file", path.read_bytes())
        return snapshot

    def test_source_containing_shared_destination_is_rejected_before_mutation(self):
        containing_source = self.home / ".agents"
        self.make_source(containing_source)
        before = self.tree_snapshot(self.root)

        with self.assertRaises(ValueError):
            INSTALLER.install(containing_source, self.home)

        self.assertEqual(self.tree_snapshot(self.root), before)
        self.assertFalse(self.shared.parent.exists())
        self.assertEqual(self.backup_entries(), [])

    def test_codex_home_inside_source_is_rejected_before_mutation(self):
        configured = self.source / "codex configuration"
        before = self.tree_snapshot(self.root)

        with self.assertRaises(ValueError):
            INSTALLER.install(self.source, self.home, codex_home=configured)

        self.assertEqual(self.tree_snapshot(self.root), before)
        self.assertFalse(configured.exists())
        self.assertFalse(self.shared.parent.exists())
        self.assertEqual(self.backup_entries(), [])


if __name__ == "__main__":
    unittest.main()
