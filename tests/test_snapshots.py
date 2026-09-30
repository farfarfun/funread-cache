import json
import unittest
from pathlib import Path


class SnapshotTests(unittest.TestCase):
    def test_snapshots_are_valid_json(self):
        paths = list(Path("funread").rglob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(path=path):
                json.loads(path.read_text(encoding="utf-8"))

    def test_readme_documents_project_and_license(self):
        readme = Path("README.md").read_text(encoding="utf-8")
        self.assertIn("## 关于 farfarfun", readme)
        self.assertIn("[MIT](LICENSE)", readme)
