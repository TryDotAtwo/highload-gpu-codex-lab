---
name: design-gpu-beam-pipelines
description: Use when designing GPU frontier expansion, scorer-to-selection flow, accumulator/ring ownership, deduplication, top-k, multi-rank exchange, or persistent beam-search stages.
---

# Design GPU Beam Pipelines

Load `references/beam-pipeline-patterns.md`. For CayleyPy/MultiGPUBeamSearch also load `references/cayleypy-stream-contract.md`, `references/beam-experiment-ledger.md`, and `references/beam-failure-catalog.md`.

## Define Ownership First

For every buffer and event state who allocates, writes, publishes, consumes, reuses, and frees it. Separate:

- outer candidate batch;
- inference microbatch;
- accumulator target;
- physical ring slots;
- final materialization chunk;
- exchange/history/solution buffers.

One counter must not silently control several physical resources.

## Pipeline Rules

- Let a slow scorer append many inference microbatches into a large accumulator.
- Use a small measured pool of physical ring slots for overlap; do not allocate one full slot per microtransaction.
- Keep threshold, compaction, sort/reduce, and global selection semantics explicit.
- Preserve original candidate identity through compaction.
- Avoid host readback and dynamic allocation in the depth loop.
- Treat the per-rank frontier size and global beam size as different metrics.

Add instrumentation before redesign: per-stage jobs, queue depth, slot wait, stage time, frontier size, threshold updates, overflow, memory high-water marks, and rank imbalance.
