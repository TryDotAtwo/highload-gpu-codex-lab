---
name: benchmark-and-sweep-gpu-configs
description: Use when tuning GPU sweeps.
---

# Benchmark And Sweep GPU Configs

## Rules

- Fix workload, GPU, driver, CUDA Toolkit, clocks/power when possible, and build flags.
- Warm up graphs, libraries, and setup-heavy paths.
- Sweep one family at a time: batch, concurrency, shards, capacity, topology, or algorithm parameter.
- For domain-specific sweeps, load the corresponding plugin and keep this skill responsible for experimental hygiene.
- Measure isolated throughput and end-to-end critical path.
- Report useful work separately from hardware-equivalent or marketing-peak FLOP/s.
- Record memory budget and failed OOM/crash/timeout rows.

Useful columns: `config_id, gpu, arch, batch, concurrency, shards, memory_gib, stage_ms, wall_s, throughput, status, notes`.

Choose the fastest stable point with margin, not the fragile point that barely fits.
