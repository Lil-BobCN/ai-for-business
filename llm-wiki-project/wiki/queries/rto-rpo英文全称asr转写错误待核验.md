---
type: query
title: RTO／RPO 英文全称 ASR 转写错误待核验
created: 2026-10-12
updated: 2026-10-12
tags: [ASR, RTO, RPO, 待核验]
related: [rto与rpo]
sources: ["架构师阿Q/第 4 集｜容灾，我用一个故事讲清楚.md"]
evidence_status: partial
---

# RTO／RPO 英文全称 ASR 转写错误待核验

## 问题本身

本集 ASR 把 RTO 与 RPO 的英文全称都转写成了 RTO，整理稿按两个指标的通行含义分别还原为 Recovery Time Objective 与 Recovery Point Objective。该还原需以原视频为准。

## 当前已知

- 来源无平台字幕，由本地 Whisper ASR 转写。
- 整理稿已在正文就地标注该处 `〔待确认〕`。
- 通行含义：RTO 关注可用性（多久恢复），RPO 关注数据完整性（丢多久的数据）。

## 冲突来源

ASR 转写文本与通行术语定义不一致。

## 缺口

缺少原视频口播的逐字核对。

## 建议搜索式

- RTO RPO 区别 恢复时间目标 恢复点目标
- Recovery Time Objective Recovery Point Objective 定义

## 下一步研究动作

回看原视频对应片段，确认作者口播的英文全称与中文解释是否与整理稿一致。