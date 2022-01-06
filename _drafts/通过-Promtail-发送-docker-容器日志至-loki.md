---
layout: post
title: 通过 Promtail 发送 docker 容器日志至 loki
---


docker 使用 journald 日志引擎。

promtail 发送 journald 日志，journald 里面有容器名称的标签。
