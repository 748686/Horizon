---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
---

> 从 4 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [块层新增按磁盘错误注入接口](#item-tech-news-1) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [块层新增按磁盘错误注入接口](https://lwn.net/Articles/1086344/) ⭐️ 7.0/10

LWN 报道了 Christoph Hellwig 提出的 Linux 块层错误注入补丁系列。该系列新增 CONFIG\_BLK\_ERROR\_INJECTION 选项，并为每个 gendisk 在 debugfs 下创建 error\_injection 文件。通过向该文件写入 add 规则，可以按操作类型（READ、WRITE、DISCARD、zone 操作等）、返回状态（IOERR、TIMEOUT、TRANSPORT 等）、起始扇区、扇区数和概率 1/N 精确注入错误；读取文件可查看规则，写入 removeall 可清除规则。这弥补了现有 fail\_make\_request、should\_fail\_bio 和 device-mapper 目标在选择性、状态码选择和直接作用于目标磁盘等方面的不足。该机制让开发者无需堆叠 device-mapper 设备，就能直接对真实磁盘测试超时、传输错误等不同恢复路径。

rss · LWN.net · 8月12日 18:34

**「背景」** Linux 块层负责把文件系统等提交的 bio 请求递交给磁盘驱动，并定义 BLK\_STS\_IOERR、BLK\_STS\_TIMEOUT 等状态码表示不同错误。此前内核从 2006 年开始提供 fail\_make\_request 故障注入，但它对所有请求一视同仁且只能返回 IOERR；2018 年加入的 should\_fail\_bio\(\) 允许 BPF 程序选择要失败的 bio，但同样只能让块层按 IOERR 完成请求。device-mapper 的 dm-error、dm-flakey、dm-dust 目标虽然可模拟坏块或间歇故障，但需要在被测设备上堆叠 mapper 设备，且受对齐和状态码限制。

**「影响」** 该补丁系列若合入，存储与内核开发者将能直接在真实磁盘上按操作、状态码、扇区范围和概率注入块层错误，从而更真实地测试超时、传输错误等恢复路径，避免 device-mapper 堆叠设备带来的偏差。

**标签**: `#Linux kernel`, `#storage`, `#error injection`, `#debugfs`, `#block layer`

---