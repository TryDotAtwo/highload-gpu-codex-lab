# Beam Search Failure Catalog

## Memory and capacity

### StaticMemoryPlan rejects before launch

This is a safety result, not an arbitrary notebook failure. The exact plan can include frontier, capacity, sort/reduce scratch, history, exchange, solved snapshots and non-static reserve. If the plan reports required bytes above available device bytes, change configuration or data lifetime; do not bypass the gate.

### Capacity is not beam width alone

Large `capacity_scale` wastes VRAM. A scale close to 1 may be valid for a large stable frontier only after exact shard fit, overflow and memory-margin checks. Stream3 batch must fit the computed shard capacity.

### Silent truncation is forbidden

First-solution and collect-all modes have different result volumes. Fixed solution capacity must fail explicitly on overflow or spill to a designed bounded store. Never present a truncated solution set as “all.”

## Batch/ring coupling

**Symptom:** increasing accumulation creates tens or hundreds of full physical buffers and OOMs.

**Cause:** one setting controls logical accumulation and physical ring allocation.

**Fix:** accumulate many inference microbatches into a few reusable physical buffers. Track logical chunks, physical ring slots and graph-template window separately.

## Final phase coupling

**Symptom:** a larger Stream3 accumulator unexpectedly inflates final exchange/history buffers.

**Cause:** final materialization chunk is derived from Stream3 batch.

**Fix:** use an independent bounded final materialization setting. Treat changes as configuration-only only when no CUDA semantics or dataflow changed.

## Misleading job-count optimization

Reducing jobs is useful only if exact depth time improves. A target such as 400 Stream3 jobs is a scheduling heuristic. Always compare the same `depth_done=8` frontier and report Stream1/ring, Stream3 and Stream4 job counts together.

## Per-rank versus global metrics

**Symptom:** frontier appears half the requested beam.

**Cause:** rank log is local.

**Fix:** record world size, rank and global aggregate. A local frontier must not be compared directly to a global request.

## BFS touch-neighborhood memory

For the observed cuckoo representation:

```text
slot_count = bucket_count * bucket_size
device_bytes = slot_count * (4-byte occupancy + 16-byte Hash128)
```

Bucket count may grow to the next power of two or retry at a larger size. Use runtime `solved_neighborhood_device_bytes`, entries and bucket count; radius alone cannot provide an exact GiB figure across puzzles.

## Wrong acceptance evidence

- `RUNNING` is not success.
- one rank returning zero is not two-rank proof.
- build/AST success is not solve proof.
- a fast depth before frontier saturation is not steady-state performance.
- an isolated scorer win is not beam-pipeline speedup.
- a replay-valid path is required; length and orientation must be checked under the intended original/reflected contract.

## Debug procedure

1. Save exact config and selected profile.
2. Confirm real GPU count and rank/device mapping.
3. Inspect StaticMemoryPlan and capacity fit.
4. Capture per-depth frontier, threshold, jobs, overflow and high-water memory.
5. Download both rank logs and output artifacts.
6. Replay every accepted solution on CPU.
7. Compare exact terminal depth rows before changing architecture.
