---
type: query
title: DR 模式特点被误记为 NAT 模式口误待核验
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, DR, NAT, 口误, ASR, 待核验]
related: [lvs-dr模式, lvs-nat模式, lvs]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: partial
---

# DR 模式特点被误记为 NAT 模式口误待核验

## 问题

[[架构师阿Q]] 第 5 集 DR 模式一段中，作者将 DR 模式的特点误记为「NAT 模式的特点是仅请求流量经过负载均衡器，响应流量直达客户端，性能极高」，与 NAT 一节「双向流量」的结论直接冲突。需确认这是口误还是转写错误。

## 当前已知

- NAT 一节作者明确称：负载均衡器需处理双向流量，所以容易成为性能瓶颈。
- DR 模式一段作者称：Real Server 处理数据包后直接返回给客户端。
- 整理者判断：按上下文，被误记为「NAT 模式特点」的那句话应为 DR 模式的特点。

## 冲突来源

同一来源内部的口播矛盾（NAT 一节 vs DR 一节），非来源间冲突。

## 缺口

- 无法从本地 ASR 转写判断是作者口误还是 ASR 误听。
- 需要回看原视频对应时间点确认。

## 建议搜索式

- LVS DR mode request only response direct to client
- LVS NAT mode bidirectional traffic director bottleneck
- LVS 三种模式 请求响应流量路径 区别

## 下一步研究动作

回看原视频 DR 模式段落确认口播原文；若确为口误，在 [[lvs-dr模式]] 与 [[lvs-nat模式]] 页面保留该标注。