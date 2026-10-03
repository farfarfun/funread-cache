# 更新日志

## 未发布

### 新增

- 增加零依赖的快照与仓库文档验证。
- 新增测试：校验 Legado 导入页面（`index.html`）里引用的 JSON 路径在仓库中真实存在，
  并禁止提交 `None`/`null`/`undefined` 这类误生成的占位文件。

### 修复

- CI 现在会执行仓库测试。
- 修正 `book/index.html`、`rss/index.html` 中「订阅源」导入链接：原先指向不存在的
  `funread/legado/rss/rss-main.json`，改为指向实际存在的
  `funread/legado/snapshot/lasted/funread.json`。
- 删除仓库根目录误提交的占位文件 `None`（未被任何 README/HTML/索引引用的单条 JSON 快照）。

### 变更

- README 补充书源和 RSS 快照的下载、导入说明。

### 废弃

- 暂无。
