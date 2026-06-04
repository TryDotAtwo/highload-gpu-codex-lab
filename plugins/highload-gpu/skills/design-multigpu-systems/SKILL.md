---
name: design-multigpu-systems
description: Use when designing multi-GPU streams, sharding, NCCL exchange, static memory, thresholds, or final materialization.
---

# Design Multi-GPU Systems

Design around explicit ownership, bounded memory, asynchronous progress, and profiling evidence.

## Pattern

- One owner and one writer per mutable buffer.
- Keep local stream work local; use NCCL only at exchange/collective boundaries.
- Preallocate repeated-loop memory, CUB temp, NCCL buffers, and graph resources.
- Publish async state with double buffers: write inactive, complete/fence, commit active index.
- Use resident A/B buffers when producers and consumers overlap.
- Avoid global barriers unless global counts, thresholds, or final balancing require them.

## Finalization

Drain active work before switching scratch layouts. Keep final-select and materialization lifetimes separate; do not overlay live inputs. CPU may store selected history, but GPU-to-GPU request/response exchange should stay native.

## Smells

- Only multi-rank fails: suspect capacity, stale state, or collective ordering.
- Full/small frontier alternation: suspect stale histograms/threshold/reset state.
- Silent stall: inspect rank logs and NCCL/stream progress before adding backpressure.
- Backpressure that hides overflow may mask the bug that larger GPU counts need to expose.