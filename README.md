# funread-cache

funread 的书源与 RSS 快照数据仓库，提供可直接下载或同步到阅读应用的数据文件。

## 使用快照

在 Legado「阅读」中打开对应页面，点击 GitHub 或 Gitee 链接即可导入：

- [书源快照](https://farfarfun.github.io/funread-cache/funread/legado/snapshot/lasted/book/index.html)
- [RSS 订阅源快照](https://farfarfun.github.io/funread-cache/funread/legado/snapshot/lasted/rss/index.html)

也可以直接下载 JSON。例如：

```bash
curl -LO https://raw.githubusercontent.com/farfarfun/funread-cache/master/funread/legado/snapshot/lasted/book/progress-1000.json
curl -LO https://raw.githubusercontent.com/farfarfun/funread-cache/master/funread/legado/snapshot/lasted/rss/progress-1000.json
```

`book/` 保存书源分片，`rss/` 保存 RSS 订阅源分片，`funread.json` 是 Legado 订阅源入口，`source.json` 是其索引数据。

## 维护验证

```bash
git clone https://github.com/farfarfun/funread-cache.git
cd funread-cache
python -m unittest discover -s tests
```

快照是静态 JSON 数据，验证仅使用 Python 标准库，不需要安装依赖。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
