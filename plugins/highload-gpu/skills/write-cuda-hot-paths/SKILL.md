---
name: write-cuda-hot-paths
description: Use when writing CUDA hot paths.
---

# Write CUDA Hot Paths

Hot paths are fixed-capacity, allocation-free, profiler-driven, and explicit about layout, alignment, ownership, and synchronization.

## Rules

- Allocate device memory, CUB temp, NCCL buffers, and graph resources before the repeated loop.
- Use explicit capacity guards; fail loudly on overflow.
- Keep CPU readback out of the steady-state path.
- Use CUDA Graphs for repeated launch templates; keep dynamic dispatch on host.
- Add static asserts for cross-kernel metadata size/alignment.
- Store only downstream-needed data, e.g. score keys instead of global-memory floats.

## Library Defaults

CUTLASS for GEMM/tensor-core kernels; CUB/CCCL for sort/reduce/scan/select; NCCL for GPU exchange/collectives; CUDA Runtime/Driver APIs for memory, streams, events, graphs, devices, and peer access.

## Avoid

Dynamic `cudaMalloc`, Python data-plane loops, per-candidate atomics when partition/sort/scan works, custom sort before checking CUB, and synchronization that hides ownership bugs.
