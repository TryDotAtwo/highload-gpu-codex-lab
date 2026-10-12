---
name: benchmark-gpu-inference
description: Use when tuning model microbatch, inference concurrency, execution slots, streams, CUDA Graphs, library backends, or isolated MLP/Transformer throughput.
---

# Benchmark GPU Inference

Load `references/inference-benchmark-contract.md`.

For historical SM120 FFN numbers, also read
`../optimize-transformer-hot-paths/references/ffn-evidence-audit-2026-09.md`.
Verify the timed binary retains both arithmetic and the required output;
instrumented correctness builds can prevent dead-code elimination that still
invalidates an uninstrumented benchmark.

## Freeze The Model Contract

Record model fingerprint, architecture, input/sequence shape, hidden dimensions, layers, activation, head/output dimension, preprocessing, source and execution precision, and exact target GPU/build.

`output_dim=1` and `output_dim=move_count` are different workloads. MLP and Transformer profiles are different until measurements prove otherwise.

## Tune The Inner Loop First

1. Benchmark one model microbatch after warmup.
2. Sweep microbatch across powers and useful intermediate values.
3. Sweep concurrent inference slots/streams at each Pareto microbatch.
4. Record latency, items/s, VRAM, workspace, launch count, utilization, and failures.
5. Integrate the winner into the caller and remeasure the critical path.

Do not confuse model microbatch with an outer candidate batch owned by a search or serving pipeline.

CUDA Graphs are an experiment, not a default win. Compare eager and graph replay on the exact dynamic-shape/launch contract.

Choose a stable Pareto point. Maximum batch may lose latency, overlap, or memory margin without increasing sustained throughput.
