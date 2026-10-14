---
type: entity
title: Nginx
created: 2026-10-12
updated: 2026-10-12
tags: [Nginx, 反向代理, 负载均衡, ASR疑误]
related: [架构和原理合集, 四层与七层负载均衡, lvs]
sources: ["架构师阿Q/00-系列索引.md"]
evidence_status: partial
---

# Nginx

Nginx 是一款广泛使用的开源 Web 服务器与反向代理软件，也常被用作七层负载均衡器。（以上为可独立核验的公开背景知识，非本来源所提供。）

## 一、在本来源中的出现

在「架构师阿Q」《架构和原理》合集中，Nginx 跨两集出现，且存在 ASR 写法冲突：

- 第 1 集（`BV1M15Q6eEhL`）：ASR 记为「Nime」。
- 第 5 集（`BV1BDVzzZE4G`）：ASR 记为「Engines」。
- 系列索引页判定两处同指 Nginx，属按上下文推断的还原。

## 二、来源观点

- 第 1 集把 Nginx 作为集群的配套组件（反向代理／负载均衡）一笔带过。
- 第 5 集在负载均衡方案比较中涉及 Nginx，并给出四层与七层的分工。

## 三、已核验事实

- 两处 ASR 写法（「Nime」「Engines」）来自系列索引页的术语待确认表，属 `partial` 证据。
- Nginx 的还原为上下文推断，存在误判风险，需外部核验。

## 四、项目分析

Nginx 是跨两集出现且存在 ASR 写法冲突的高频词，具备独立核验价值。建议优先核验其还原是否正确。

## 五、关联页面

- 系列容器：[[entities/架构和原理合集]]
- 相关概念：[[concepts/四层与七层负载均衡]]
- 来源页：[[sources/5-架构师阿q--7-00-系列索引--1fl2d59]]

## 六、开放问题

- 「Nime」「Engines」是否确为 Nginx，需核对原视频音频。