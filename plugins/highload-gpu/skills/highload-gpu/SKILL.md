---
name: highload-gpu
description: Use when working on high-load GPU, CUDA, multi-GPU, profiling, NVIDIA docs, or Python/Rust/C++/CUDA stack boundaries.
---

# HighloadGpu

Router for high-performance GPU engineering.

## Pick The Sub-Skill

- Multi-GPU streams/shards/NCCL/finalization: `design-multigpu-systems`
- Language ownership: `choose-stack-boundaries`
- CUDA kernels/CUTLASS/CUB/graphs: `write-cuda-hot-paths`
- GPU model, compute capability, CUDA/library docs: `use-nvidia-docs`
- Timeline/stream/NCCL/launch gaps: `use-nsight-systems`
- One-kernel bottleneck: `use-nsight-compute`
- Illegal access/race/init/sync bug: `use-compute-sanitizer`
- Batch/concurrency/shard sweeps: `benchmark-and-sweep-gpu-configs`
- Kaggle/Molab/remote GPU profiling: `profile-remote-gpu-runs`

## Defaults

- Python: wrappers, notebooks, dashboards, CLI/torchrun launch.
- Rust: safe config, validation, artifact/log tooling, host services.
- C++ + CUDA: CPU/GPU hot paths, kernels, CUDA Graphs, NCCL, CUTLASS, CUB.

Do not put high-volume GPU data-plane loops in Python. Check current NVIDIA docs before hardware-specific advice. Require profiling evidence before architecture changes.