---
title: 'Processing 官方教程'
categories: 教程翻译
---

[原文](https://processing.org/tutorials/gettingstarted/)

## 你的第一个程序

你现在应该正运行着 Processing 开发环境(PDE)。 这里没多少东西; 较大的区域是文本编辑器, 顶部横向的一行是工具栏。在文本编辑器底部是信息区, 更底下是控制台。 信息区用来显示单行信息, 控制台显示更多技术细节。

在编辑器中,输入以下内容:

```C++
ellipse(50, 50, 80, 80);
```

这一行代表"画一个椭圆, 从左起 50 像素, 从上起 50 像素, 画一个宽高都是 80 像素的椭圆。" 单击运行按钮(工具栏上的三角按钮)。

如果你的输入没错的话, 你将在你的显示器上看到一个圆圈。 如果你的输入有误, 信息栏将会变红并且提示有一个错误。 如果发生这种情况, 确认你和示例的代码完全一样: 数字应该在括号内并且用逗号分割, 并且行应由分号结束。

编程最困难的事情之一就是你必须使用非常精确的语法, Processing 程序不总是能够足够聪明地理解你的意思, 而且对标点符号的放置非常挑剔。进行一些练习你将会习惯的。

接下来, 我们将会跳到一个更有趣的速写。 删除上个例子中的文本, 然后试试这个:

![示例图像](/images/Ex_02_02.gif)

```C++
void setup() {
  size(480, 120);
}

void draw() {
  if (mousePressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}
```

这个程序创建一个宽 480 像素, 高 120 像素的窗口, 并且在鼠标所处位置画圆。 当鼠标按下时, 圆的颜色将会变成黑色。 我们将稍后解释更多关于程序的细节。 现在, 先运行这些代码, 移动鼠标, 并且点击鼠标看会发生什么。 当草图运行时, 运行按钮将会变成方块的"停止"图标, 你能单击它来停止速写。

## 展示

如果你不想使用按钮, 你可以随时使用速写本菜单, 它提供了快捷键 Ctrl-R(或者 Mac 的 Cmd-R)来运行, 展示模式在程序运行时清空屏幕的其余部分来展示速写本。 你也可以按住 Shift 再点击开始按钮来使用展示模式。

## 保存和新建

保存是下一个重要的命令。 你能够在文件菜单下找到它。 默认情况下, 你的程序将会被保存到"速写本", 它的意义在于快速访问你保存的程序。 在文件菜单中选择速写本, 将能列出速写本中的所有速写。

经常保存你的速写是一个好主意。 当你尝试不同的东西时, 不停用不同的名字保存, 便于你回到早期的版本。这当有什么东西不对劲时非常有用。你能使用在速写本菜单中的展示程序文件命令来查看速写放在哪里。

你能通过文件菜单中的新建命令来创建新的速写。 它将在新的窗口中创建。

## 分享

Processing 的速写本就是设计用来分享的。 文件菜单中的导出能将你的代码打包到单个文件夹中。 输出程序命令将按你的选择创建 Mac, Windows 和/或 Linux 的应用。 这是创建你工程的能窗口或者全屏运行,自我打包, 可双击运行程序版本的简单方法。

每次你使用输出程序命令时应用文件夹都会清空并重新创建, 所以如果你不想在下次导出时丢失现在这个版本一定要把它放到别的地方去。

## 示例和参考文档

学习如何编程将涉及到在代码上探索许多: 运行, 更改, 损坏和增强它直到你将它变成了什么新的东西。 在这种想法的指引下, Processing 软件在下载时就附带了许多演示软件不同特性的例子。

要打开例子, 在文件菜单中选择范例程序并双击名称打开它。 范例程序以它的功能分类, 例如 Form, Motion 和 Image。 在列表中找到你感兴趣的主题并尝试一下。

当在编辑器中查看代码时, 你将发现像是`ellipse()`或者`fill()`的颜色和其他文本不同。 如果你看到一个你不熟悉的函数, 选择其文本, 然后右键单击(在 Mac 上是按住 Ctrl 单击)并在出现的菜单中选择"在参考文档中搜索"。 它将打开浏览器显示相关的参考文档。 或者你能更进一步地通过使用帮助菜单中的参考文档命令查看整个文档。

Processing 参考文档中用描述和例子展示了每一个代码元素。 参考文档的程序将更加简短(通常是四到五行)并比范例程序中的长程序更容易理解。 我们建议当你阅读这本书或者编程时保持它的开启。 它能使用字母排序, 有时这比使用搜索要快。

参考文档是意为初学者编写的; 我们希望我们有让它清楚易懂。 我们非常感谢那些发现错误并且提交的人。 如果你认为你能优化一个参考文档的表达或者找到了错误, 请通过点击每个参考文档页面顶部的链接来告知我们。
