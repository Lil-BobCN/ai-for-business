---
type: query
title: LVS 性能是软件负载均衡中最高主张待核验
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, 性能排名, 软件负载均衡, 待核验]
related: [lvs, 软件负载均衡, 四层与七层负载均衡]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: unknown
---

# LVS 性能是软件负载均衡中最高主张待核验

## 问题

[[架构师阿Q]] 第 5 集称 LVS「性能是软件负载均衡中最高的」，理由是纯四层、工作在内核态。该性能排名断言需要外部核验。

## 当前已知

- 视频作者在该段口播中称：LVS 是纯四层的负载均衡，运行在内核态，性能是软件负载均衡中最高的；因为是在四层，所以也更通用一些。
- 作者同时称 Nginx 与 HAProxy 是七层负载均衡，HAProxy 性能也很不错。
- 本集未给出任何压测数据或量级对比。

## 冲突来源

暂无来源间冲突。需注意该断言与 Wiki 中其他来源对负载均衡性能的表述可能口径不一，若后续来源出现不同结论，应在本页记录冲突。

## 缺口

- 在何种流量模型与硬件条件下，LVS 性能高于 Nginx／HAProxy。
- 四层与七层方案是否可直接比较（七层需解析应用层内容，工作量本就不同）。
- 是否存在 Nginx 或 HAProxy 在特定场景下性能更优的反例。

## 建议搜索式

- LVS vs Nginx vs HAProxy performance benchmark comparison
- layer 4 vs layer 7 load balancer throughput comparison
- IPVS kernel load balancing performance test results

## 下一步研究动作

查找第三方压测报告或官方性能文档，补充量级数据；在获得证据前，该断言在 [[lvs]] 与 [[软件负载均衡]] 页面保持 `unknown` 状态。