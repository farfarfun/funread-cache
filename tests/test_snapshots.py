import json
import re
import unittest
from pathlib import Path

# 匹配 HTML 中出现的、相对仓库根目录的 funread/.../*.json 引用，
# 用来校验 Legado 导入页面链接到的 JSON 文件在仓库里确实存在。
_JSON_REF_PATTERN = re.compile(r"funread/legado/[A-Za-z0-9_./-]+\.json")


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

    def test_html_json_links_point_to_existing_files(self):
        """Legado 导入页面（index.html）里引用的 JSON 路径必须在仓库中真实存在。"""
        html_paths = list(Path("funread").rglob("*.html"))
        self.assertTrue(html_paths)
        for html_path in html_paths:
            content = html_path.read_text(encoding="utf-8")
            for ref in set(_JSON_REF_PATTERN.findall(content)):
                with self.subTest(html=html_path, ref=ref):
                    self.assertTrue(
                        Path(ref).is_file(),
                        f"{html_path} 引用的 {ref} 在仓库中不存在",
                    )

    def test_no_untracked_placeholder_files(self):
        """禁止提交文件名为 'None' 之类明显的误生成占位产物。"""
        repo_root = Path(".")
        forbidden_names = {"None", "null", "undefined"}
        offenders = [
            path
            for path in repo_root.iterdir()
            if path.is_file() and path.name in forbidden_names
        ]
        self.assertEqual(offenders, [], f"发现疑似误生成的占位文件: {offenders}")
