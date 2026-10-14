---
type: query
title: 一个 Object Type 只能对应一张表规则待核验
tags: [Palantir, Object Type, 宽表, 建模规则]
related: [宽表拆分规则, 干净表到本体的映射]
sources: ["零点未来：AI+企业/第 4 集｜14分钟揭秘Palantir一堆文件如何变成Ontology.md"]
evidence_status: unknown
created: 2026-10-11
updated: 2026-10-11
---

# 一个 Object Type 只能对应一张表规则待核验

## 问题本身

本来源视频作者称 Palantir 有一条硬性规则：一个 Object Type 只能对应一张表，因此宽表必须先拆成聚焦小表再映射。该规则是否为硬性约束待核验。

## 当前已知

- 作者称宽表不能直接映射，必须在 Pipeline 里拆成订单表、商品表、物流表等，各自映射到对应 Object Type，再用 link 连接。
- 作者称 Pipeline Builder 内置 AI 可辅助写拆分代码，但列归属判断仍需人为完成。

## 冲突来源

- 无直接冲突来源，但均为作者口播，无一手文档佐证。

## 缺口

- 缺少 Palantir 官方文档中 Object Type 与 backing dataset 对应关系的原文。
- 不确定该规则是硬性约束还是最佳实践。

## 建议搜索式

- Palantir Foundry Object Type backing datasource one table
- Palantir Ontology object type mapping dataset documentation
- Palantir 宽表 拆分 Object Type 映射

## 下一步研究动作

查阅 Palantir 官方 Ontology 建模文档，核对 Object Type 与数据源的对应约束。