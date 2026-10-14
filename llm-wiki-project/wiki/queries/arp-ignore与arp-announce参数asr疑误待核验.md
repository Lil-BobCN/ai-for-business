---
type: query
title: arp_ignore 与 arp_announce 参数 ASR 疑误待核验
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, DR, ARP, ASR, 待核验]
related: [lvs-dr模式]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: partial
---

# arp_ignore 与 arp_announce 参数 ASR 疑误待核验

## 问题

[[架构师阿Q]] 第 5 集 DR 模式一段中，作者提到通过配置 ARP 参数使只有 Director Server 响应 ARP 请求，ASR 转写为「ARP 的 ignal 参数」。整理者按上下文还原为 `arp_ignore`／`arp_announce` 一类参数，需确认。

## 当前已知

- 视频作者在该段口播中称：因为 Director Server 和 Real Server 配置同一个 VIP，通过配置 ARP 的 `ignore` 参数来实现只有 Director Server 响应该请求。
- ASR 原文记为「ARP 的 ignal 参数」，无法直接对应到确定的内核参数名。
- 整理者判断应为 `arp_ignore`／`arp_announce` 一类参数。

## 冲突来源

ASR 转写与整理者还原之间的差异，非来源间冲突。

## 缺口

- 作者原话中提到的确切参数名。
- DR 模式实际需要配置哪些 ARP 相关内核参数及其取值。

## 建议搜索式

- LVS DR mode arp_ignore arp_announce configuration
- Linux kernel arp_ignore arp_announce parameters meaning
- LVS 直接路由 模式 ARP 参数 配置

## 下一步研究动作

查阅 LVS 官方文档或 Linux 内核文档确认参数名与取值；回看原视频对应时间点确认口播原文。