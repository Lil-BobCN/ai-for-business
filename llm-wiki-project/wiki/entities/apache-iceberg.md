---
type: entity
title: Apache Iceberg
created: 2026-10-12
updated: 2026-10-12
tags: [表格式, 数据湖, 湖仓一体]
related: [湖仓一体, 数据湖与数据沼泽, 数据仓库]
sources: ["架构师阿Q/第 3 集｜一口气讲透大数据、数据库、数据仓库、数据湖、数据中台的底层原理.md"]
evidence_status: unknown
---

# Apache Iceberg

Apache Iceberg 是一种开放表格式（table format），用于在数据湖存储之上提供表级元数据与事务能力。视频作者在《第 3 集｜一口气讲透大数据、数据库、数据仓库、数据湖、数据中台的底层原理》中提到，靠 Data Lake、Apache Iceberg 这类表格式引擎就能实现"一份数据两种用法"。

## 定义

视频作者在该段口播中把 Apache Iceberg 归为"表格式引擎"，并把它与湖仓一体的"一份数据两种用法"能力关联起来。本集未展开其具体机制。

## 已核验事实

无。本集口播中的名称记为"Apache Ice Bird"，本页标题"Apache Iceberg"为按上下文推断的结果，尚未以原视频核验。详见 [[queries/airflow-与-apache-iceberg-名称-asr-转写待核验]]。Apache Iceberg 作为 Apache 软件基金会项目属于公开技术事实（可独立核验的背景知识），但本集未提供其具体能力细节。

## 来源观点

作者把 Apache Iceberg 作为 [[concepts/湖仓一体]] 的实现组件之一提及，认为它能实现"一份数据两种用法"，完美平衡性能与成本。该判断为作者口播主张，`unknown / 待外部核验`。

## 项目分析

Apache Iceberg 在本集叙事中承担"湖仓互通"的技术支撑角色。本集未讨论表格式引擎的选型差异、迁移成本与元数据一致性维护。

## 反例或边界

- 名称存在 ASR 转写风险，需以原视频核验。
- 本集未提供湖仓一体落地的真实案例或性能数据。

## 关联页面

- [[concepts/湖仓一体]]
- [[concepts/数据湖与数据沼泽]]
- [[concepts/数据仓库]]
- [[sources/5-架构师阿q--32-第-3-集一口气讲透大数据数据库数据仓库数据湖数据中台的底层原理--13hl5sh]]

## 开放问题

- 作者口播中的"Apache Ice Bird"是否确为 Apache Iceberg？