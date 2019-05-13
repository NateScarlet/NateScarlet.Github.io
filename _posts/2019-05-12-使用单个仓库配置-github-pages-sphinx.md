---
layout: post
title: 使用单个仓库配置 GitHub Pages + Sphinx
date: 2019-05-12 01:19:35 +0800
categories: web Git
---

这几天开始觉得先写文档再写测试最后实现的流程更合理，
所以打算研究下用 [GitHub Pages] 托管项目文档。

但是 [GitHub Pages] 用的是 [jekyll]，
[jekyll] 不支持输出 docx 格式，
而国内软件著作权申请需要提交 docx 格式。
因此我都是用 [Sphinx] 写[^1]。

所以希望在 [GitHub Pages] 上面也能使用 [Sphinx]。

最终方案样本仓库: [WuLiFang/Nuke](https://github.com/WuLiFang/Nuke)

## 需求

- 文档可以托管在 [GitHub Pages] 上
- 文档使用 [Sphinx] 生成
- 支持自动化构建文档
- 支持 clone 仓库时不克隆文档
- 方便新用户编辑文档

## 托管位置选择

使用 [Sphinx] 就不能提供 [GitHub Pages] 的自动构建了，
需要把构建好的文件放到 GitHub 支持的托管位置[^2]:

- master 分支
- master 分支的 docs 文件夹
- gh-pages 分支

### master 分支

如果使用 master 分支就需要将文档源码和构建好的文档分成两个仓库。

其中构建好的文档和文档源码的数据会有很多是重复的, 比如图片。
将造成存储空间的浪费。

把文档源码放在其他分支也是个解决方案, 但是这样比较反直觉。
所以不选择用 master 分支托管。

### master 分支的 docs 文件夹

需要在文档源码仓库中用 docs 放构建好的文档,
这样文档源码就不能用 `docs` 了，
造成命名不清晰。

应该只适合使用 [jekyll] 构建的文档使用，
所以不选择用 master 分支的 docs 文件夹。

### gh-pages 分支

用 gh-pages 分支托管需要实现从一个分支构建到另一个分支，
看上去没什么问题,
所以最后决定使用 gh-pages 分支来托管。

## Sphinx 配置

直接 `sphinx-quickstart` 创建项目，
然后在 `conf.py` 中添加 [Sphinx Github Pages 插件]。

```python
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages'] # <- 这个
```

这个插件会为生成后的文档添加 `.nojekyll` 文件，
也会为 [GitHub Pages] 自定义域名添加 `CNAME` 文件。
如果没有 `.nojekyll`，
[GitHub Pages] 会认为 `_` 开头的文件夹是 `jekyll` 内部文件夹，
然后将它过滤掉。[^3]

配置好插件后把 `build/html` 和 `gh-pages` 关联就行了。

> **注意:** [Sphinx] 文档的文件名不能使用大写字母。
> 因为 [Sphinx] 在 windows 上输出时会把的文件名转成小写,
> 而 [GitHub Pages] 的路由是大小写敏感的。
> 无法正确链接到使用了大写字母作为文件名的文件。

## 关联 build/html 到 gh-pages 分支

推荐单独创建一个 docs 分支存储文档，
因为文档不是运行源码必须的。

master 分支除非确实需要否则尽量不存放二进制文件，
如果文件大还应该使用 [Git LFS]。

之前克隆一个实际代码 300KB 的插件仓库，
结果它在 master 分支用 74MB 的演示素材浪费我的时间和带宽,
让我被迫分支了一个仓库。[^4]

而在克隆仓库的时候如果 docs 存放到单独分支的话，
就可以只克隆源码分支:

```shell
git clone --single-branch --depth 1 <url>
```

> 虽说不用 docs 分支也能关联,
> 不过以下的示例都是以使用 docs 分支为前提的。

先需要创建一个孤儿 gh-pages 分支:

```shell
git checkout --orphan gh-pages
git reset
echo '' > .gitignore
git add .gitignore
git commit -m init
# 返回 docs 分支
git checkout -f docs
```

然后就是关联这个 gh-pages 分支到文件夹了。

### Git 子模块 (submodule)

首先想到的关联文件夹到 Git 仓库的方法是用 git 子模块。

创建子模块:

```shell
git submodule add -b gh-pages <仓库 URL> build/html
git submodule update --remote
```

然后正常构建推送就行了。

Github 检测到 `gh-pages` 分支会自动启用 [GitHub Pages] 托管。

但是这个方案有几个缺点:

- 子模块必须有一个远程仓库才能使用。
- 子模块的数据处理和父仓库是分离的， 同样的仓库数据同时存在两份， 浪费硬盘。
- 子模块需要作为一个额外仓库管理， 比如更新远程 URL 时要同时更新子模块和父仓库的设置。
- 包管理器在直接从仓库安装时会初始化子仓库, 例如 pip, 但是不会初始化工作树

### Git 工作树 (worktree)

由于想要避免硬盘浪费的问题，
我搜索了一下 Git 单个仓库多个工作树的方法。

发现 Git 有这个功能，
就是 `git worktree` 命令。

由于 Git 工作树是本地设置，
官方没有提供像 `.gitmodule` 那样的版本管理功能。

不过因为源码运行不依赖文档，不需要在源码分支管理文档。

只要在 README.md 里面说明怎么配置就行了， 还更灵活，

在 master 分支创建工作树并且关联分支:

```shell
git worktree add --checkout docs docs
git worktree add --checkout docs/build/html gh-pages
# 添加文件夹到 .gitignore
echo /docs  >> .gitignore
echo /build/html  >> docs/.gitignore
```

然后也是正常构建推送就行了。

不过 [VSCode] 当前只支持工作树作为根目录，
不支持检测多个工作树。
需要手动敲命令或者不断切换文件夹来管理源代码。

[^1]: [Sphinx] 官方支持输出 epub 格式, 然后 epub 格式用 [pandoc] 就能转成 docx
[^2]: <https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages>
[^3]: <https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/>
[^4]: <https://github.com/Psyop/Cryptomatte>

[sphinx]: https://www.sphinx-doc.org
[sphinx github pages 插件]: https://www.sphinx-doc.org/en/master/usage/extensions/githubpages.html
[vscode]: https://code.visualstudio.com/
[github pages]: https://pages.github.com/
[git lfs]: https://git-lfs.github.com/
[pandoc]: https://pandoc.org/
[jekyll]: https://jekyllrb.com/
