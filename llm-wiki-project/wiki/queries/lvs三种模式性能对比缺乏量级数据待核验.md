---
type: query
title: LVS 三种模式性能对比缺乏量级数据待核验
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, 性能, 待核验, 开放问题]
related: [lvs, lvs-nat模式, lvs-dr模式, lvs-tun模式]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: unknown
---

# LVS 三种模式性能对比缺乏量级数据待核验

## 问题

[[架构师阿Q]] 第 5 集对 LVS 三种模式的性能只给出定性结论（NAT「容易成为性能瓶颈」、DR／TUN「性能极高」），未给出任何量级数据。这些定性结论在什么条件下成立、差距有多大，需要外部核验。

## 当前已知

- 视频作者在该段口播中称：NAT 模式因负载均衡器需处理双向流量，容易成为性能瓶颈；DR 与 TUN 模式响应直达客户端，性能高。
- 本集约 7 分 11 秒，无配置示例、无压测数据、无真实故障案例。

## 冲突来源

暂无来源间冲突，属单一来源的定性断言。

## 缺口

- 三种模式在相同硬件与流量模型下的吞吐、延迟、连接数上限对比数据。
- 封装／解封装开销（TUN）与二层改写开销（DR）的实际量级。
- NAT 模式调度器成为瓶颈的具体阈值条件。

## 建议搜索式

- LVS NAT DR TUN mode performance benchmark comparison
- LVS direct routing vs NAT throughput latency test
- IPVS forwarding mode performance overhead measurement

## 下一步研究动作

查找 LVS 官方文档、内核 IPVS 文档或第三方压测报告，补充量级数据后再更新 [[lvs]] 与三种模式页面。