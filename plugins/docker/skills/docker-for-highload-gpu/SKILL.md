---
name: docker-for-highload-gpu
description: Use when building Docker environments for HighloadGpu, CUDA/C++/Rust/Python stacks, multi-GPU profiling, Nsight, or Compute Sanitizer.
---

# Docker For HighloadGpu

Docker should make the native GPU build reproducible; it must not move hot-path logic into Python.

## Image Design

- Base on an NVIDIA CUDA devel image for builds; use runtime/base image only for final binaries.
- Install CMake/Ninja, compiler, CUDA libraries, Rust toolchain, Python launcher deps, and profiler tools intentionally.
- Mount source and build/output directories; avoid baking large transient build artifacts into final images.
- Use BuildKit/cache mounts for CMake, Cargo, pip/uv, apt, and compiler caches when useful.
- Keep `/tmp`, profiler output, and `test_results/` mapping explicit.

## GPU/Profiler Runs

- Use `--gpus all` or specific device IDs; verify with container `nvidia-smi`.
- Nsight Systems needs enough permissions and writable output paths.
- Nsight Compute/Compute Sanitizer should run on reduced cases when full runs are too slow.
- For multi-GPU, preserve `RANK`, `LOCAL_RANK`, `WORLD_SIZE`, NCCL env, and visible device ordering.

## Boundaries

Use Python only for launch/dashboard/notebook glue, Rust for safe orchestration/log tooling, and C++ + CUDA for CUDA Graphs, NCCL, CUB, CUTLASS, kernels, and CPU/GPU hot paths.
