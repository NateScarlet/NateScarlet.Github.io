---
layout: post
title: 使用单个仓库配置 GitHub Pages + Sphinx
---

这几天开始觉得先写文档再写测试最后实现的流程更合理 所以打算研究下用 [GitHub Pages] 托管项目文档

但是 [GitHub Pages] 用的是 [jekyll]

[jekyll] 不支持输出 docx 格式, 而国内软件著作权申请需要提交的是 docx 格式

在公司我都是用 [Sphinx] 写文档[^1], 习惯了

所以希望在 [GitHub Pages] 上面也能使用 [Sphinx]

最终方案样本从仓库: [WuLiFang/Nuke](https://github.com/WuLiFang/Nuke)

## 需求

- 文档可以托管在 [GitHub Pages] 上
- 文档使用 Sphinx 生成
- 支持自动化构建文档
- 支持 clone 仓库时不克隆文档
- 方便新用户编辑文档

## Sphinx 配置

## 项目管理方案

### 使用单独的文档仓库

### Git 子模块 (submodule)

### Git 工作区 (worktree)

[^1]: [Sphinx] 官方支持输出 epub 格式, 然后 epub 格式用 [pandoc] 就能转成 docx

[sphinx]: https://www.sphinx-doc.org
