import json
from pathlib import Path


def test_snapshots_are_valid_json():
    paths = list(Path("funread").rglob("*.json"))
    assert paths
    for path in paths:
        json.loads(path.read_text(encoding="utf-8"))


def test_readme_documents_project_and_license():
    readme = Path("README.md").read_text(encoding="utf-8")
    assert "## 关于 farfarfun" in readme
    assert "[MIT](LICENSE)" in readme
