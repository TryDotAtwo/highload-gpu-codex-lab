---
name: write-cuda-hot-paths
description: Use when writing or optimizing CUDA kernels, memory layouts, and GPU hot paths.
---

# Write CUDA Hot Paths

Primary skill for CUDA code-writing. Hot paths are fixed-capacity, allocation-free, profiler-driven, and explicit about layout, alignment, ownership, and synchronization.

## Workflow

1. State shapes, precision, target GPU, correctness oracle, and measured bottleneck.
2. Choose library vs custom kernel; use custom CUDA where layout, fusion, or control flow makes it worthwhile.
3. Design layout first, implement a small deterministic path, then profile.

## Rules

- Allocate device memory, library temp, NCCL buffers, and graph resources before repeated loops.
- Use explicit capacity guards; fail loudly on overflow.
- Keep CPU readback out of the steady-state path.
- Use CUDA Graphs for repeated launch templates; keep dynamic dispatch on host.
- Add static asserts for cross-kernel metadata size/alignment.
- Store only downstream-needed data; avoid materializing large intermediates when compact keys, indices, or reductions are enough.

## Library Defaults

CUTLASS/cuBLAS for GEMM/tensor-core kernels; CUB/CCCL for sort/reduce/scan/select; NCCL for GPU exchange/collectives; CUDA Runtime/Driver APIs for memory, streams, events, graphs, devices, and peer access.

## Avoid

Dynamic `cudaMalloc`, Python data-plane loops, fine-grained atomics when partition/sort/scan works, custom sort before checking CUB/CCCL, and synchronization that hides ownership bugs.
