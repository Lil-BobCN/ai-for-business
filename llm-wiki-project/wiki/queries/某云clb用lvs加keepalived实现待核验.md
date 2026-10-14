---
type: query
title: 某云 CLB 用 LVS 加 Keepalived 实现待核验
created: 2026-10-12
updated: 2026-10-12
tags: [云厂商, CLB, LVS, Keepalived, 待核验]
related: [lvs, keepalived]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: unknown
---

# 某云 CLB 用 LVS 加 Keepalived 实现待核验

## 问题

[[架构师阿Q]] 第 5 集称「某云以前的四层负载均衡 CLB 就是通过 LVS 加 Keepalived 的方式实现」。该说法属随厂商架构调整而变化的现状描述，且来源未具名具体厂商，需要外部核验。

## 当前已知

- 视频作者在该段口播中称：很多大厂的负载均衡产品底层都有基于 LVS 做开发，并举例某云以前的四层负载均衡 CLB 通过 LVS 加 Keepalived 实现。
- 来源未具名厂商，也未给出时间范围或官方文档出处。

## 冲突来源

暂无来源间冲突，属单一来源的未具名现状描述。

## 缺口

- 具体是哪家云厂商、哪个时期的产品。
- 该实现方式是否仍在使用，或已被自研方案替换。
- 是否有官方文档或技术博客可佐证。

## 建议搜索式

- 云厂商 四层负载均衡 CLB LVS Keepalived 实现
- cloud provider layer 4 load balancer LVS keepalived architecture
- 阿里云 SLB 腾讯云 CLB 底层实现 LVS

## 下一步研究动作

查找主流云厂商关于四层负载均衡底层实现的官方文档或技术博客；在未获证据前，该说法在 [[lvs]] 与 [[keepalived]] 页面保持 `unknown` 状态。