---
layout: post
title: CentOS7 配置 Docker overlay2 存储引擎
---

单独分区带某个参数格式化之后挂载到 /var/lib/docker

/etc/docker/daemon.json 设置

```json
{
  "storage-driver": "overlay2"
}
```
