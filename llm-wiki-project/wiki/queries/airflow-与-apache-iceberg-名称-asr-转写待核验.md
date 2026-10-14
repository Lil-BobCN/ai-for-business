---
type: query
title: Airflow 与 Apache Iceberg 名称 ASR 转写待核验
created: 2026-10-12
updated: 2026-10-12
tags: [ASR, 待核验, 工具名]
related: [airflow, apache-iceberg, 任务调度, 湖仓一体]
sources: ["架构师阿Q/第 3 集｜一口气讲透大数据、数据库、数据仓库、数据湖、数据中台的底层原理.md"]
evidence_status: partial
---

# Airflow 与 Apache Iceberg 名称 ASR 转写待核验

## 问题本身

《第 3 集｜一口气讲透大数据、数据库、数据仓库、数据湖、数据中台的底层原理》为本地 Whisper ASR 转写，无平台字幕。其中两处工具名按上下文推断，尚未以原视频核验：

1. 任务调度工具：口播记为"PireFlow"，本 Wiki 推断为 Airflow。
2. 湖仓一体表格式引擎：口播记为"Apache Ice Bird"，本 Wiki 推断为 Apache Iceberg。

## 当前已知

- 两处均出现在技术名词密集段落，上下文分别指向"任务调度工具"与"表格式引擎"。
- 整理时已还原其他明显属于同音误听的技术名词（如"行事存储／劣势层处"→ 行式存储／列式存储、"数据壶／壶仓一体"→ 数据湖／湖仓一体、"Data Load／Beta Load"→ DataNode、"Name Load"→ NameNode、"封控系统"→ 风控系统等）。
- 这两处无法仅凭上下文可靠判断原意，因此保留 ASR 内容并标注 `〔待确认〕`。

## 冲突来源

无外部来源冲突；问题在于 ASR 转写本身不可靠。

## 缺口

- 原视频音频中作者实际说出的工具名。
- 作者是否在同一段落中还提到其他调度工具或表格式引擎。

## 建议搜索式

- Apache Airflow 任务调度 依赖编排 定时触发
- Apache Iceberg 表格式 湖仓一体 一份数据两种用法
- 大数据 任务调度工具 对比 Airflow DolphinScheduler

## 下一步研究动作

以原视频（https://www.bilibili.com/video/BV12qKq6PETb）核对这两处口播，确认后更新 [[entities/airflow]] 与 [[entities/apache-iceberg]] 两页的标题与定义。