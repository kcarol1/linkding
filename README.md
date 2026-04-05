<div align="center">
    <br>
    <a href="https://github.com/sissbruecker/linkding">
        <img src="assets/header.svg" height="50">
    </a>
    <br>
</div>

## 简介

linkding 是一个可自行托管的书签管理器。
它的设计目标是简洁、快速，并且能够通过 Docker 轻松完成部署。

名字的来源是：
- *link*，在日常表达里经常被用作 URL 和书签的同义词
- *Ding*，德语里表示“东西”
- 所以组合起来，大致就是“管理链接的东西”

**功能概览：**
- 简洁、注重可读性的界面
- 使用标签整理书签
- 支持批量编辑、Markdown 笔记和稍后读功能
- 可与其他用户或访客共享书签
- 自动获取已收藏网站的标题、描述和图标
- 自动归档网页，可保存为本地 HTML 文件或存入 Internet Archive
- 支持以 Netscape HTML 格式导入和导出书签
- 可安装为渐进式 Web 应用（PWA）
- 提供 [Firefox](https://addons.mozilla.org/firefox/addon/linkding-extension/) 和 [Chrome](https://chrome.google.com/webstore/detail/linkding-extension/beakmhbijpdhipnjhnclmhgjlddhidpe) 扩展，以及书签小工具（bookmarklet）
- 支持基于 OIDC 或认证代理的单点登录
- 提供 REST API 供第三方应用开发使用
- 提供管理后台，方便用户自助管理与查看原始数据

**演示地址：** https://demo.linkding.link/

**截图：**

![Screenshot](/docs/public/linkding-screenshot.png?raw=true "Screenshot")

## 快速开始

下面这些链接可以帮助你快速上手 linkding：
- [在自己的服务器上安装 linkding](https://linkding.link/installation) 或 [查看托管服务选项](https://linkding.link/managed-hosting)
- [安装浏览器扩展](https://linkding.link/browser-extension)
- [查看社区项目](https://linkding.link/community)，其中包括移动应用、浏览器扩展、库等内容

## 文档

完整文档现已发布在 [linkding.link](https://linkding.link/)。

如果你想参与文档贡献，可以在 `docs` 目录中找到文档源文件。

如果你想为社区项目页面补充内容，也欢迎 [提交 PR](https://github.com/sissbruecker/linkding/edit/master/docs/src/content/docs/community.md)。

## 贡献

欢迎提交小改进、Bug 修复和文档优化。如果你想贡献较大的功能，建议先开一个 issue 讨论。我可能会忽略与项目目标不一致，或我不打算长期维护的功能 PR。

## 开发

这个应用基于 Django Web 框架构建。你可以先阅读非常优秀的 [Django 文档](https://docs.djangoproject.com/en/4.1/)。`bookmarks` 目录包含了实际的书签应用代码，除此之外整体基本都是比较标准的 Django 结构 🙂。

### 前置要求
- Python 3.13
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Node.js

### 初始化

使用下面的命令初始化开发环境：
```
make init
```
这会使用 `uv` 创建虚拟环境、安装 NPM 依赖，并运行迁移以创建初始数据库。

为前端创建一个用户：
```
uv run manage.py createsuperuser --username=joe --email=joe@example.com
```

运行前端构建，用于打包前端组件：
```
make frontend
```

然后启动 Django 开发服务器：
```
make serve
```
前端随后会运行在 http://localhost:8000

### 测试

使用 pytest 运行全部测试：
```
make test
```

### 代码检查

使用 ruff 运行静态检查：
```
make lint
```

### 代码格式化

使用 ruff 格式化 Python，使用 djlint 格式化 Django 模板，使用 prettier 格式化 JavaScript：
```
make format
```

### DevContainers

这个仓库也支持 DevContainers：[![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/sissbruecker/linkding.git)

代码拉取完成后，只需要执行以下命令即可开始：

为前端创建一个用户：
```
uv run manage.py createsuperuser --username=joe --email=joe@example.com
```

启动 Node.js 开发服务器（用于编译标签自动补全等 JavaScript 组件）：
```
make frontend
```

启动 Django 开发服务器：
```
make serve
```
前端随后会运行在 http://localhost:8000
