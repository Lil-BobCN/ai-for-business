---
type: query
title: Foundry 连接器数量与拉取方式待核验
tags: [Palantir, Foundry, 连接器, snapshot, 增量拉取]
related: [palantir-foundry, 增量更新三层与两个坑]
sources: ["零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# Foundry 连接器数量与拉取方式待核验

## 问题本身

本来源视频作者称 Foundry 有 200 种连接器，拉取方式分 snapshot（全量替换）与只追加新数据 `upam`〔待确认〕两类。这些数字与命名均未经独立核实。

## 当前已知

- 作者称 Foundry 有 200 种连接器对接不同数据源，格式涵盖文件、PDF、PPT、视频、图片。
- 作者称拉取方式主要有 snapshot 与只追加新数据两类，并强调这一区别对增量更新很重要。

## 冲突来源

- 无直接冲突来源，但均为作者口播，无一手文档佐证。

## 缺口

- 缺少 Palantir 官方文档中连接器数量与拉取方式命名的原文。
- `upam` 的准确拼写与含义不明。

## 建议搜索式

- Palantir Foundry connectors number official documentation
- Palantir Foundry data connection snapshot incremental sync
- Palantir Foundry 增量拉取 连接器

## 下一步研究动作

查阅 Palantir 官方文档 Data Connection 章节，核对连接器数量与同步模式命名。