# Beam Pipeline Patterns

## Decouple Logical Accumulation From Physical Storage

A Transformer may score hundreds of small inference microbatches before one large downstream selection job is ready. That does not require hundreds of full pipeline buffers. Maintain:

1. a small physical ring, commonly beginning with two ping-pong slots;
2. an accumulator cursor inside the current producer slot;
3. an accumulation-chunk count independent of ring-slot count;
4. a ready event only when the logical accumulator is complete or depth input ends.

While downstream work consumes slot A, inference fills slot B. Add slots only when a timeline proves producer or consumer starvation and the memory cost is acceptable.

## Selection And Dedup

Prefer deterministic bulk primitives:

1. threshold/filter;
2. compact;
3. sort or radix partition with fixed temporary storage;
4. reduce/select unique representatives;
5. compact accepted outputs.

Fine-grained global hash insertion can combine random traffic, contention, capacity ambiguity, and nondeterminism. Use it only with evidence and an explicit overflow contract.

## GPU-Native Frontier Layout

- Keep frontier states, keys, payload indices, and candidates in a few flat, aligned SoA arenas. A logical shard or bucket is a sorted or radix-partitioned range, not a page list or pointer-linked container.
- Prefer deterministic bulk sort, partition, scan, and compaction even when this adds another linear pass. Do not avoid a cheap GPU sort by importing CPU container or allocator patterns.
- Sort compact keys and indices when moving full states through every radix pass would waste bandwidth; gather the chosen states once afterward.
- Read offsets or other metadata once per grouped run or tile and reuse them across the work unit. A directory fitting in L2 does not justify per-candidate scattered reads.
- Accept indirection or random traffic only after target-hardware profiling shows memory transaction efficiency and an end-to-end win.

## Multi-Rank Meaning

Log both local and global values. In an even two-rank split, a local frontier of `beam / 2` can be exactly correct. Verify the all-rank sum and ownership mapping before diagnosing underfill.

Shard count is a work-partition parameter, not permission to apply shard-local semantic caps. Global selection must implement the requested beam semantics.

## Final Materialization

The final materialization chunk bounds request/response/history exchange memory. It is not necessarily the same size as the large scorer accumulator. Large values often spend memory without accelerating the final path. A measured 88,064-candidate chunk was a stable 2xT4 CayleyPy profile across small and large beam anchors; treat it as an empirical starting point, not a universal constant.

## Failure Contracts

- fixed capacities and preallocated temporary storage;
- explicit overflow/fail-closed status;
- no silent frontier or solution truncation;
- deterministic ownership and event reuse;
- exact requested/effective beam reporting after alignment.
