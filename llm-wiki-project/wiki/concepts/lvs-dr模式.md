---
type: concept
title: LVS DR 模式
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, Direct Routing, 负载均衡, 报文流转, ARP]
related: [lvs, lvs-nat模式, lvs-tun模式, 控制面与数据面分离]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: partial
---

# LVS DR 模式

LVS DR 模式是 LVS 三种工作模式之一，全称 Direct Routing（直接路由技术）。其核心特征是调度器只改写二层 MAC 地址，响应报文由 Real Server 直接返回客户端，不经过调度器。本页记录 [[架构师阿Q]] 第 5 集口播中的报文流转描述。

## 定义

视频作者在该段口播中说明：实现 LVS 的 DR 模式，首先 Director Server 和 Real Server 都要配置同一个 IP，都为 VIP——Director Server 将该 IP 配置到对外的网卡上，Real Server 将该 IP 配置到本地回环网卡（lo 网卡）上。

## 报文流转（视频作者口播，`unknown / 待外部核验`）

1. 因为同一个 VIP，通过配置 ARP 的 `arp_ignore`／`arp_announce` 一类参数来实现：数据包发出 ARP 请求时，只有 Director Server 会响应该请求。
2. 客户端访问 Director Server：源 IP = CIP，目标 IP = VIP。
3. Director Server 收到数据包后，根据调度算法找出对应的 Real Server，并把目的 MAC 地址改为 Real Server 的 MAC（即 RIP 的 MAC），源 MAC 为 Director Server 的 MAC（即 DIP 的 MAC）。
4. Real Server 通过网卡 ETH0 收到数据包，由于 Real Server 上的 lo 网卡也配置了 VIP，所以 Real Server 接收数据包并处理后**直接返回给客户端**。

## 特点（视频作者口播）

- 要对二层包头进行改写，所以 Director Server 和 Real Server 必须在一个广播域，也可以简单理解为在同一台交换机上。
- 需要 Real Server 配置 VIP 并禁用 ARP 响应。

## 已核验事实

本页暂无工具直接验证的事实。报文流转描述来自本地 ASR 转写，证据状态 `partial`；ARP 参数名称为整理者按上下文还原。

## 项目分析

- 用「三问」记法定位 DR 模式：改了**二层 MAC**；响应报文**不走过**调度器；拓扑约束是同一广播域 + 禁用 ARP 响应。
- 响应直达客户端使调度器不承担回程流量，这是其性能优于 NAT 模式的直接原因。
- 与 [[控制面与数据面分离]] 视角呼应：只走请求的架构性能好，但调度器看不到完整会话，对限流、审计、连接数统计这类功能有影响。

## 反例与边界

- 本集未给出 DR 模式的配置示例、压测数据或真实故障案例。
- 本集未讨论「响应不经过调度器」对可观测性与会话保持的影响。

## 关联页面

- 上位实体：[[lvs]]
- 对照模式：[[lvs-nat模式]]、[[lvs-tun模式]]

## 开放问题

- [[dr模式特点被误记为nat模式口误待核验]]
- [[arp-ignore与arp-announce参数asr疑误待核验]]
- [[lvs三种模式性能对比缺乏量级数据待核验]]