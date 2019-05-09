---
layout: post
title: 在 VSCode 中不靠插件使用 Vue 单文件组件 + TSLint
date: 2019-05-09 20:05 +0800
categories: VSCode Vue Typescript
---

今天发现 [VSCode] Intellisense 特别卡是 [TSLint Vue] 这个插件造成的

去官方仓库看 Issue 时发现这个项目已经 18 个月没更新了

所以就开始寻找备用方案

## 方案选择

### Vetur

首先看的是 [VSCode] 商店中安装数量最多的 [Vetur]

但是 [Vetur] 的 [TSLint] 支持还没实现 [^1] [^2]

### typescript-tslint-plugin

[Vetur] 的 Issue [^2] 中提到了 [TypeScript] 插件 [typescript-tslint-plugin]

但是这个项目还很新

作为微软的项目 Star 才不到 200

所以不准备试用

### Vue CLI TypeScript 插件

之后想起 [Vue CLI TypeScript 插件] 虽然文档没写但其实是有 [TSLint] 支持的

之前禁用它是因为功能和 [TSLint Vue] 插件重复了

而且 [TSLint] 准备在 [ESLint] 添加 [TypeScript] 支持后废弃 [^3]

所以不太可能有基于 [TSLint] 的新项目

于是决定用整合 [Vue CLI] 功能到 [VSCode] 的方法

## 配置 Vue CLI

项目中添加 [Vue CLI TypeScript 插件] 后

在 vue.config.js 中配置 lintOnSave [^4]\ (也可以不配置, 默认值为总是启用)

```js
module.exports = {
  lintOnSave: process.env.NODE_ENV !== 'production',
};
```

## 配置 VSCode

在 VSCode 中

F1 - 运行任务 - 选择 `npm: serve` 运行一次之后 VSCode 会自动生成任务配置

然后在 .vscode/tasks.json 中配置任务[^5]:

```json
{
  "type": "npm",
  "script": "serve",
  "isBackground": true,
  // 从命令输出内容中匹配问题
  "problemMatcher": [
    {
      "owner": "typescript",
      "fileLocation": "absolute",
      "applyTo": "allDocuments",
      "pattern": [
        {
          "regexp": "^(ERROR) in (.+)$",
          "severity": 1,
          "file": 2
        },
        {
          "regexp": "^(\\d+):(\\d+) (.+)$",
          "line": 1,
          "column": 2,
          "message": 3
        }
      ],
      "background": {
        "beginsPattern": "^Type checking and linting in progress...$",
        "endsPattern": "^Time: \\d+ms$"
      }
    }
  ],
  "runOptions": {
    // 打开文件夹自动启用
    "runOn": "folderOpen"
  }
}
```

最后就能在 [VSCode] 中直观地看到检查结果了

![效果](/images/Code_2019-05-10_00-08-11.png)

更新会有些延迟但是不会拖慢 VSCode 的 Intellisense

[tslint vue]: https://github.com/prograhammer/vscode-tslint-vue
[vetur]: https://github.com/vuejs/vetur
[tslint]: https://palantir.github.io/tslint/
[typescript-tslint-plugin]: https://github.com/Microsoft/typescript-tslint-plugin
[eslint]: https://eslint.org/
[vue cli typescript 插件]: https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-typescript
[vscode]: https://code.visualstudio.com/
[typescript]: https://www.typescriptlang.org/

[^1]: <https://github.com/vuejs/vetur/issues/170>
[^2]: <https://github.com/vuejs/vetur/issues/873>
[^3]: <https://github.com/palantir/tslint/issues/4534>
[^4]: <https://cli.vuejs.org/config/#lintonsave>
[^5]: <https://code.visualstudio.com/docs/editor/tasks#_background-watching-tasks>
