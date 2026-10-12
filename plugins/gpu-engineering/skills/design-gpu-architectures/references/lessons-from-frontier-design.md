# Lessons From Frontier Architecture Design

These lessons came from iteratively designing a large GPU frontier/search system. They are patterns, not mandatory choices for every workload.

## Premature Full Architecture Hides Errors

An early complete-looking proposal invented downstream buffers and synchronization before their semantics were known. The effective method was to keep the currently discussed producer/consumer boundary detailed and leave later jobs skeletal. The canonical document was rewritten after each accepted correction.

General rule: completeness is earned boundary by boundary. Unknowns remain explicit rather than being filled with plausible CUDA vocabulary.

## One Name Must Mean One Physical Unit

“Slot,” “batch,” and “ring” were initially conflated. The corrected model separated:

- one logical parent state;
- an inference microbatch of parents;
- candidates per parent;
- several microbatches accumulated for one downstream job;
- one physical ring bank;
- the number of banks used for overlap.

General rule: define formulas and counts before declaring arrays or CUDA Graph shapes.

## Bulk Arrays Beat Accidental CPU Data Structures

A first deduplication proposal used a global open-address table with probes and atomics. The accepted direction for the batched stage used preallocated arrays and bulk primitives: compact, radix sort, reduce adjacent equal keys, and select. This converted scattered mutation into full, predictable passes and made temporary memory calculable.

General rule: when data already arrives in large batches, compare sort/partition/scan against fine-grained mutation before choosing the latter. Atomics are a measured option, not a default ideology.

## Materialize Only What The Next Consumer Needs

The initial design allocated full child states for all raw candidates. The corrected search path carried a compact recipe and hash through filtering and deduplication, then materialized full states only for the next frontier. This removed a dominant write and buffer.

The opposite workload also exists: when almost every child survives, carrying both compact metadata and repeated reconstruction may lose. The architecture must model survival ratio, frontier shape, state bytes, and reconstruction cost, then select a fixed profile or define an explicit transition.

General rule: materialization point is an architectural decision, not a kernel detail.

## Streams Form A Readiness Graph, Not A Story

Calling stages a “pipeline” encouraged a false sequential picture. The corrected design had independent jobs:

- tensor-heavy scoring runs whenever a parent microbatch is available;
- key/state transformation can run concurrently on the same logical range;
- a bulk consumer starts when a complete ring bank is ready;
- exchange starts when destination ranges are ready;
- local shard work starts when a shard job is eligible.

Only finalization requires the full depth to drain.

General rule: specify launch predicates, events, ownership, and reuse. Stream numbers alone are not architecture.

## Tensor Cores Do Not Need To Own Every Operation

Dense scoring belonged to CUTLASS/tensor-core work. Hashing, permutation, comparison, radix sort, reduction, scan, and compaction belonged to CUDA/CCCL work. The useful optimization was concurrent use of different execution resources, not disguising sorting as GEMM.

General rule: map operations naturally, then use timeline evidence to prove overlap. A tensor-core kernel still competes for bandwidth, cache, registers, schedulers, and supporting CUDA-core work.

## Rank Ownership And Local Shards Solve Different Problems

Owner rank established where a key receives global deduplication semantics. Many shards inside one rank supplied bounded jobs and enough ready work for roulette scheduling. Treating shard count as GPU count would have coupled scale-out to local scheduling and produced giant jobs.

General rule: owner mapping routes correctness; shards expose concurrency and bound work.

## Contention Can Be Removed By Ownership, Not More Locks

Several producers writing directly into mutable shard regions would have required contested append counters. The corrected pattern used one collector as the shard writer and separated clean, dirty, processing, and spill regions. A shard being processed did not stop unrelated shards or incoming work.

General rule: prefer disjoint ranges or one-writer collection. Add locks/atomics only when their contention and ordering contract is demonstrably acceptable.

## Lifetime Overlays Save More Than Tiny Encodings

Instead of independently allocating every maximum-size buffer, mutually exclusive steady-state and finalization layouts shared one preallocated scratch pool. The current frontier and solution/control state remained outside because their lifetimes crossed the phase boundary.

General rule: draw lifetimes before chasing field-level byte savings. Overlay only after a provable drain.

## Compact Identifiers Must Survive Compaction

A compacted array index was briefly treated as candidate identity. That breaks parent/move reconstruction after filters remove earlier records. The corrected representation retained the original payload identifier and used explicit deterministic tie-breaking during deduplication.

General rule: preserve the identifier of the logical source, not merely the current physical position.

## Implementation Follows Dependency Gates

The architecture was made implementable through isolated stages: ABI and memory, transformation/reference tests, final materialization, local deduplication, shard merge, exchange, dispatcher/graphs, then full execution. Each stage declared excluded work and its evidence level.

General rule: a green local stage unlocks its dependent stage; it does not validate the whole system. Real multi-GPU exchange becomes green only on multiple devices with asymmetric traffic.
