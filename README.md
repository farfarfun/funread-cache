# funread-cache

funread 的书源与 RSS 快照数据仓库，提供可直接下载或同步到阅读应用的数据文件。

## 使用

```bash
git clone https://github.com/farfarfun/funread-cache.git
cd funread-cache
python -m json.tool funread/legado/snapshot/lasted/rss/progress-1000.json >/dev/null
```

快照是静态 JSON 数据，不需要安装运行时依赖；提交前可运行 `python -m pytest` 校验所有快照。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
