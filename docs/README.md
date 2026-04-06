# Starlight 入门模板：基础版

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

```
npm create astro@latest -- --template starlight
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/starlight/tree/main/examples/basics)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/starlight/tree/main/examples/basics)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/withastro/starlight&create_from_path=examples/basics)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwithastro%2Fstarlight%2Ftree%2Fmain%2Fexamples%2Fbasics&project-name=my-starlight-docs&repository-name=my-starlight-docs)

> 🧑‍🚀 **已经很熟悉这套工具链了？** 那就直接删掉这个文件，玩得开心。

## 🚀 项目结构

在这个 Astro + Starlight 项目中，你会看到如下目录和文件结构：

```
.
├── public/
├── src/
│   ├── assets/
│   ├── content/
│   │   ├── docs/
│   │   └── config.ts
│   └── env.d.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

Starlight 会在 `src/content/docs/` 目录中查找 `.md` 或 `.mdx` 文件。每个文件都会根据文件名暴露为对应的路由。

图片可以放在 `src/assets/` 中，并通过相对路径在 Markdown 中引用。

像 favicon 这类静态资源可以放在 `public/` 目录中。

## 🧞 命令

所有命令都需要在项目根目录的终端中执行：

| 命令                       | 作用                                  |
| :------------------------- | :------------------------------------ |
| `npm install`              | 安装依赖                              |
| `npm run dev`              | 在 `localhost:4321` 启动本地开发服务器 |
| `npm run build`            | 将生产环境站点构建到 `./dist/`        |
| `npm run preview`          | 在本地预览构建结果，便于部署前检查    |
| `npm run astro ...`        | 运行 `astro add`、`astro check` 等 CLI 命令 |
| `npm run astro -- --help`  | 查看 Astro CLI 帮助信息               |

## 👀 想了解更多？

可以查看 [Starlight 文档](https://starlight.astro.build/)、阅读 [Astro 官方文档](https://docs.astro.build)，或者加入 [Astro Discord 社区](https://astro.build/chat)。
