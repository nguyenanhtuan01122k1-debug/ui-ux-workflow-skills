"""Observable contracts for safe creation, Unicode and evidence state."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "skills" / "ui-ux-workflow" / "scripts" / "new_project.py"
spec = importlib.util.spec_from_file_location("new_project", MODULE)
new_project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(new_project)


class NewProjectTests(unittest.TestCase):
    def test_unicode_and_initial_evidence_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "dự án mới"
            new_project.create_project(out, "Làng Hoạt Hình Việt")
            state = json.loads((out / "project.json").read_text(encoding="utf-8"))
            self.assertEqual(state["project_name"], "Làng Hoạt Hình Việt")
            self.assertEqual(len(state["documents"]), 9)
            self.assertTrue(all(s["status"] == "not_started" and not s["evidence"]
                                for s in state["stages"].values()))
            for filename in state["documents"]:
                body = (out / filename).read_text(encoding="utf-8")
                self.assertIn("Làng Hoạt Hình Việt", body)
                self.assertNotIn("{{PROJECT_NAME}}", body)

    def test_existing_directory_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "existing"
            out.mkdir()
            sentinel = out / "user-data.txt"
            sentinel.write_bytes(b"keep-this")
            with self.assertRaises(FileExistsError):
                new_project.create_project(out, "New")
            self.assertEqual(list(out.iterdir()), [sentinel])
            self.assertEqual(sentinel.read_bytes(), b"keep-this")

    def test_existing_file_is_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "user.txt"
            out.write_bytes(b"keep")
            with self.assertRaises(FileExistsError):
                new_project.create_project(out, "New")
            self.assertEqual(out.read_bytes(), b"keep")

    def test_rejects_writes_inside_skill(self):
        with self.assertRaises(ValueError):
            new_project.create_project(new_project.SKILL_ROOT / "should-not-be-created", "New")
        self.assertFalse((new_project.SKILL_ROOT / "should-not-be-created").exists())

    def test_bad_templates_fail_before_creation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            templates = root / "templates"
            templates.mkdir()
            out = root / "new-project"
            with self.assertRaises(FileNotFoundError):
                new_project.create_project(out, "New", templates)
            self.assertFalse(out.exists())

    def test_invalid_names_do_not_create_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "new-project"
            for name in ("", "   ", "one\ntwo", "one\rtwo", "bad\x00name"):
                with self.subTest(name=repr(name)):
                    with self.assertRaises(ValueError):
                        new_project.create_project(out, name)
                    self.assertFalse(out.exists())


if __name__ == "__main__":
    unittest.main()
