---
name: choose-stack-boundaries
description: Use when deciding whether GPU-system code belongs in Python, Rust, C++, CUDA, torchrun, dashboards, or FFI.
---

# Choose Stack Boundaries

Use this default split:

| Layer | Owner |
| --- | --- |
| Notebook, dashboard, CLI, torchrun launch | Python |
| Config schema, validation, logs, artifacts, services | Rust |
| Rank startup, CUDA/NCCL setup, memory planning, CPU hot paths | C++ |
| Kernels, graphs, CUB, CUTLASS, NCCL data plane | C++ + CUDA |

## FFI

- Python to Rust: PyO3 + maturin.
- Rust to C++: `cxx` for typed stable boundaries; C ABI + bindgen for narrow low-level APIs.
- Python/Rust to CUDA: prefer calling a native C++/CUDA binary or library.

## Push Back

Do not implement per-candidate, per-shard, tensor-tile, CUDA-event, or rank-exchange loops in Python. Python launches and visualizes; native code computes and communicates.
