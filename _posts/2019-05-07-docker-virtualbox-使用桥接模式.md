---
layout: post
title: Docker + VirtualBox 使用桥接模式
date: 2019-05-07 20:57 +0800
categories: Docker
---

实际使用中发现 VirtualBox NAT 模式的虚拟机中运行的服务没法获取到客户端的 IP

所有的日志中获取到的都是 10.0.2.2 [^1]

为了让日志数据有意义一点则需要给 VirtualBox 添加一个桥接网络 (`docker-machine` 会自动把前两个网卡修改回来, 所以需要添加第三个网卡)

![在 VirtualBox GUI 中添加第三个网卡](/images/VirtualBox_2019-05-07_21-06-55.png)

但是 TinyCore linux 使用默认桥接网卡设置是获取不到 IP 的

所以需要更改桥接网卡的芯片组类型为和前两个网卡一样的类型 [^2]

![修改网卡芯片组类型](/images/VirtualBox_2019-05-07_21-21-07.png)

![修改后的类型](/images/VirtualBox_2019-05-07_21-22-30.png)

如果路由配置了 DHCP 就应该能自动获取到 IP 了

![自动获取到的 IP](/images/Code_2019-05-07_21-34-49.png)

但是服务器自然需要配一个固定 IP

```bash
ifconfig eth2 192.168.1.2 netmask 255.255.255.0
```

可以把命令加到 `/var/lib/boot2docker/bootlocal.sh` 中让他每次开机自动运行

配置完成之后就能在日志中看到客户端的真实 IP 了

[^1]: 来自虚拟机宿主
[^2]: <https://github.com/docker/machine/issues/1491#issuecomment-472617158>
