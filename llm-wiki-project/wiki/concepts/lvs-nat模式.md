---
type: concept
title: LVS NAT 模式
created: 2026-10-12
updated: 2026-10-12
tags: [LVS, NAT, 负载均衡, 报文流转]
related: [lvs, ipvs, lvs-dr模式, lvs-tun模式, 控制面与数据面分离]
sources: ["架构师阿Q/第 5 集｜负载均衡是什么？LVS的三种模式有什么区别？.md"]
evidence_status: partial
---

# LVS NAT 模式

LVS NAT 模式是 LVS 三种工作模式之一，全称 Network Address Translation（网络地址翻译）。其核心特征是调度器修改请求报文的目标 IP，且请求与响应双向流量都经过调度器。本页记录 [[架构师阿Q]] 第 5 集口播中的报文流转描述。

## 定义

视频作者在该段口播中说明角色：**客户端 Client**、**负载调度器 Director Server**（实际是安装了 LVS 模块的服务器）、**真实服务器 Real Server**。NAT 模式即通过修改目标 IP 完成请求转发。

## 报文流转（视频作者口播，`unknown / 待外部核验`）

1. 客户端 Client 访问负载调度器 Director：源 IP = Client IP（CIP），目标 IP = LVS 主机的 VIP。
2. 基于 Linux 内核的四层负载均衡技术 [[ipvs]] 在 LVS 上把数据包的目标 IP 修改为后端服务器 Real Server IP（RIP），源 IP 仍为 CIP——此过程完成目标 IP 转换。
3. 数据包发送给 Real Server 后，Real Server 构建响应报文发回 Director：源 IP = RIP，目标 IP = CIP。
4. Director 在响应客户端前，将源 IP 修改为自己的 VIP，然后响应客户端：源 IP = VIP，目标 IP = CIP。

## 特点（视频作者口播）

- 后端服务器无需暴露真实 IP。
- 负载均衡器需处理双向流量，所以容易成为性能瓶颈。

## 已核验事实

本页暂无工具直接验证的事实。报文流转描述来自本地 ASR 转写，证据状态 `partial`。

## 项目分析

- 用「三问」记法定位 NAT 模式：改了**三层目标 IP**；响应报文**走过**调度器；拓扑约束是后端网关需指向调度器。
- 双向流量经过调度器，使调度器同时承担转发与回程压力，这是其成为瓶颈的直接原因，也与 [[控制面与数据面分离]] 视角中「双向都走可控但易成瓶颈」的判断一致。

## 反例与边界

- 本集未给出 NAT 模式的配置示例、连接数上限或压测数据。
- 本集未讨论 NAT 模式下调度器自身故障时的后果。

## 关联页面

- 上位实体：[[lvs]]
- 执行组件：[[ipvs]]
- 对照模式：[[lvs-dr模式]]、[[lvs-tun模式]]

## 开放问题

- [[lvs三种模式性能对比缺乏量级数据待核验]]
- [[dr模式特点被误记为nat模式口误待核验]]