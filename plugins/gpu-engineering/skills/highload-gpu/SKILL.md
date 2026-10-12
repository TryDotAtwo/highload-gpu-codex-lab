---
name: highload-gpu
description: Use when solving general CUDA, GPU performance, GPU profiling, multi-GPU, NVIDIA-library, throughput-accounting, or Blackwell SM120 hardware tasks. Domain-specific beam-search and neural-inference work belongs in dedicated plugins.
---

# HighloadGpu

Router for general CUDA code-writing and high-performance GPU engineering. Default to a measured single-GPU hot path first. Keep domain algorithms in their dedicated plugins.

## Pick The Sub-Skill

- CUDA kernels, memory layout, CUTLASS/CUB, graphs, native hot paths: `write-cuda-hot-paths`
- Multi-GPU scaling, rank ownership, peer access, NCCL, overlap: `design-multigpu-systems`
- Python/Rust/C++/CUDA ownership boundaries: `choose-stack-boundaries`
- Peak-versus-useful throughput, rooflines, utilization claims: `reason-about-gpu-throughput`
- Blackwell compute capability 12.0 and RTX PRO 6000 tuning: `work-with-sm120-blackwell`
- GPU model, compute capability, CUDA/library docs: `use-nvidia-docs`
- Timeline/stream/NCCL/launch gaps: `use-nsight-systems`
- One-kernel bottleneck: `use-nsight-compute`
- Illegal access/race/init/sync bug: `use-compute-sanitizer`
- Batch/concurrency/shard sweeps: `benchmark-and-sweep-gpu-configs`
- Remote GPU evidence collection independent of platform: `profile-remote-gpu-runs`

## Defaults

- Python: wrappers, notebooks, dashboards, CLI/torchrun launch.
- Rust: safe config, validation, artifact/log tooling, host services.
- C++ + CUDA: CPU/GPU hot paths, kernels, CUDA Graphs, NCCL, CUTLASS, CUB/CCCL.

Check current NVIDIA docs before hardware-specific advice. Require correctness checks and profiling evidence on the target hardware before architecture changes.

For beam/frontier algorithms use the `GpuBeamSearch` plugin. For MLP/Transformer execution, quantization, and fused model kernels use `GpuNeuralInference`. For notebook-session operations use the relevant platform plugin.
