---
type: query
title: DNS 负载均衡只支持轮询主张待核验
created: 2026-10-12
updated: 2026-10-12
tags: [DNS, 负载均衡, 调度算法, 待核验]
related: [dns负载均衡, 控制权边界]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: unknown
---

# DNS 负载均衡只支持轮询主张待核验

## 问题

[[架构师阿Q]] 第 5 集称「DNS 一般只支持轮询方式」〔ASR 记为「只支持 R2 的轮巡方式」，整理者按上下文还原为「轮询」〕。该算法能力断言需要外部核验。

## 当前已知

- 视频作者在该段口播中称：DNS 的流量调度策略简单，支持的算法较少，一般只支持轮询方式。
- 作者同时称大公司会用 DNS 实现地理级别的负载均衡，实现就近访问。

## 冲突来源

暂无来源间冲突，属单一来源的概括性断言。

## 缺口

- DNS 层面可用的调度策略实际有哪些（轮询、加权、地理位置、延迟探测等）。
- 「一般只支持轮询」是否指基础 DNS 解析，还是包含智能 DNS／GSLB 方案。
- 与作者同时提到的「地理级负载均衡」是否自相矛盾。

## 建议搜索式

- DNS load balancing algorithms round robin weighted geo
- GSLB global server load balancing scheduling methods
- DNS 轮询 加权 智能解析 调度策略

## 下一步研究动作

查阅 DNS 负载均衡与 GSLB 的公开资料，确认可用调度策略范围；据此更新 [[dns负载均衡]] 与 [[控制权边界]] 页面。