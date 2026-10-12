---
name: plan-beam-memory
description: Use when sizing GPU/host/disk memory for beam frontier, capacities, shards, history, BFS-touch tables, solution collection, model workspace, or final exchange buffers.
---

# Plan Beam Memory

Build an exact `StaticMemoryPlan` before launching the production depth loop.

## Separate Budgets

- current and next frontier by rank;
- expanded candidates and metadata;
- scorer activations/workspace;
- accumulator and physical ring slots;
- sort/reduce/scan temporary storage;
- final materialization and rank exchange;
- BFS-touch tables;
- history RAM/disk staging;
- solved-result capacity and collect-all payloads;
- library/runtime reserve.

Use checked integer arithmetic and actual struct sizes/alignment. Account for double buffering and per-rank replication. Gate both static allocation and non-static runtime reserve against real free memory.

## Policy

- At very large beams, capacity scale can approach one only when measured overflow statistics and a safety margin support it.
- Do not buy safety by multiplying every buffer by the same factor.
- Measure BFS enumeration size; branching makes radius cost exponential and puzzle dependent.
- History and collect-all limits are user-visible semantics. Fail clearly instead of silently pruning or truncating.
- Report bytes/GiB by category and the largest sensitivity terms.
