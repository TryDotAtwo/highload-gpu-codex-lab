---
name: design-multigpu-systems
description: Use when scaling CUDA workloads across multiple GPUs, ranks, or nodes.
---

# Design Multi-GPU Systems

Use only when a workload needs multiple devices, ranks, or nodes. Keep domain algorithms in their dedicated plugins. Load `references/multigpu-patterns.md` when implementation details are needed.

## Core Rules

- Define rank/device ownership before writing kernels: inputs, outputs, scratch, streams, communicators, and host control state.
- Choose the split: data parallel, model/tensor parallel, pipeline parallel, task sharding, or replicated workers.
- Keep local GPU work local; cross-device exchange should happen at explicit boundaries.
- Preallocate device memory, CUB temp, NCCL buffers, graph resources, and host pinned buffers before steady-state loops.
- Verify NCCL ordering is identical on all ranks and log rank/device/collective sequence numbers.
- Inspect topology, exchange volume, load balance, host launch serialization, and synchronization before changing kernels.
