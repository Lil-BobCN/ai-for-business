---
type: entity
title: Keepalived
created: 2026-10-12
updated: 2026-10-12
tags: [高可用, 负载均衡, VRRP, LVS]
related: [lvs, 负载均衡, 控制面与数据面分离]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: mixed
---

# Keepalived

Keepalived 是一套常用于 Linux 环境的高可用组件，通常与 LVS 配合，为负载均衡调度器提供故障切换能力。本页记录 [[架构师阿Q]] 第 5 集口播中对 Keepalived 的提及，以及由此暴露的知识缺口。

## 定义

视频作者在该段口播中仅把 Keepalived 作为例证提及：某云以前的四层负载均衡 CLB 是通过「LVS 加 Keepalived」的方式实现。作者未解释 Keepalived 的作用机制。

> 独立可核验背景（非本来源内容）：Keepalived 是开源的高可用与负载均衡工具，常基于 VRRP 协议实现虚拟 IP 漂移，与 LVS／IPVS 配合使用。此句为公开可查的通用背景，不由本来源支持。

## 来源观点（`unknown / 待外部核验`）

- 视频作者称某云四层 CLB 通过 LVS 加 Keepalived 实现。该说法属随厂商架构调整而变化的现状描述，未经独立核验。
- 作者在 ASR 转写中记为「Keep Alive」，整理者按上下文还原为 Keepalived。

## 已核验事实

本页暂无工具直接验证的事实。

## 项目分析

- 本集把 Keepalived 作为厂商实现细节一笔带过，但**没有讨论负载均衡器自身的高可用**（调度器挂掉怎么办）——而这正是 Keepalived 存在的原因。这构成本集主题内最直接的知识缺口。
- 从 [[控制面与数据面分离]] 的视角看，Keepalived 处理的是调度器这一「控制面」节点的存活问题，与数据面转发路径是两件事。

## 反例与边界

- 本集未给出 Keepalived 的配置方式、VRRP 参数或故障切换时间，不能据此评估其切换能力。

## 关联页面

- 配合对象：[[lvs]]
- 上位概念：[[负载均衡]]

## 开放问题

- [[负载均衡器自身高可用本集未展开待补充]]
- [[某云clb用lvs加keepalived实现待核验]]