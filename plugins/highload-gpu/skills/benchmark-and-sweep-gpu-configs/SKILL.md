---
name: benchmark-and-sweep-gpu-configs
description: Use when tuning GPU sweeps.
---

# Benchmark And Sweep GPU Configs

Tune with isolated benchmarks, then production-like runs.

## Rules

- Fix workload, model, GPU, driver, CUDA Toolkit, clocks/power when possible, and build flags.
- Warm up graph, CUTLASS, and setup-heavy paths.
- Sweep one family at a time: batch/concurrency, ring slots, shard count, capacity, active sort slots, topology, history mode.
- Measure isolated throughput and end-to-end critical path.
- Record memory budget: allocated, reserved, free, headroom, static buffers, RAM/disk history.
- Failed OOM/crash/timeout rows are data.

Use table columns like: `config_id, gpu, arch, batch, concurrency, shards, ring_slots, active_sort_slots, memory_gib, stage_ms, wall_s, throughput, status, notes`.

Choose the fastest stable point with margin, not the fragile point that barely fits.
