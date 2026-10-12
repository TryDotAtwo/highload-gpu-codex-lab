---
name: choose-stack-boundaries
description: Use when choosing GPU stack boundaries.
---

# Choose Stack Boundaries

Default split:

| Layer | Owner |
| --- | --- |
| Notebook, dashboard, CLI, torchrun launch | Python |
| Config schema, validation, logs, artifacts, services | Rust |
| Rank startup, CUDA/NCCL setup, memory planning, CPU hot paths | C++ |
| Kernels, graphs, CUB, CUTLASS, NCCL data plane | C++ + CUDA |

FFI defaults: PyO3 + maturin for Python/Rust, `cxx` for Rust/C++, C ABI + bindgen for narrow low-level APIs, and native C++/CUDA libraries for GPU work.

## Push Back

Do not implement per-element, per-shard, tensor-tile, CUDA-event, or rank-exchange loops in Python. Python launches and visualizes; native code computes and communicates.

The implementation language is not the synchronization contract: Rust/C++ can
serialize the same pipeline through host-returned counts, blocking wrappers,
or per-shard launch decisions. Audit callers through the FFI boundary.

When adopting a library or database, check whether its real API accepts
device-held valid counts, stable borrowed buffers, caller-provided scratch and
streams, and explicit completion events. Include adapter copies, pool reserve,
reset/rebuild cost, and result materialization in the comparison. A fixed memory
pool does not by itself establish allocation-free execution or stable addresses.
Prefer the smallest suitable primitive; judge it by matched end-to-end semantics
and measurements, not by a database/library label.
