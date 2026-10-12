---
name: gpu-beam-search
description: Use when designing, implementing, tuning, debugging, or validating GPU beam search, frontier expansion, candidate selection, beam deduplication, BFS-touch solving, or collect-all solution pipelines.
---

# GpuBeamSearch

Router for the beam-search domain. Use HighloadGpu for generic CUDA profiling and GpuNeuralInference for model execution.

## Route

- Stage ownership, accumulators, rings, selection, dedup, and multi-rank flow: `design-gpu-beam-pipelines`
- Beam width, batching, slots, shards, jobs, and profile sweeps: `tune-gpu-beam-profiles`
- Frontier/history/BFS/solution-capacity budgeting: `plan-beam-memory`
- Replay, first/collect semantics, reflection, and final acceptance: `validate-beam-search-results`
- CayleyPy/MultiGPUBeamSearch invariants: load `design-gpu-beam-pipelines/references/cayleypy-stream-contract.md`

## Domain Boundary

The model scorer is a replaceable producer. Tune its inner execution in GpuNeuralInference; tune how the beam pipeline feeds and drains it here. Keep platform session operations in the Kaggle, Molab, or HPC plugin.

Never change search semantics to improve a benchmark unless the user explicitly authorizes that algorithmic change.
