# GPU Dataflow And Memory

## Transaction-First Memory Model

Reason from the physical layout consumed by warps:

- field widths and encodings;
- byte offsets, alignment, and padding;
- contiguous ranges and memory-transaction boundaries;
- which lanes read or write adjacent addresses;
- cache reuse and whether it is likely rather than guaranteed;
- the number of full passes over each byte;
- read/write amplification caused by materialization or repacking.

Count passes over a whole iteration, not only one incoming batch. If each of
R batches scans the same H historical records, the cost includes R*H. If each
batch appends b survivors by rewriting the entire accepted prefix, total prefix
output is b*R*(R+1)/2 records. Coalescing does not remove this amplification.
Compare indexed membership, bounded sorted runs, and bulk merging under the
actual batch-to-history ratio, duplicate rate, load factor, and memory budget.

Across library boundaries, inventory buffer identities: borrowed view, necessary
layout conversion, ownership copy, and redundant same-layout copy. Removing a
copy requires a proved lifetime/reuse contract. Count GEMM intermediates and
adapter buffers as well as final outputs. Logical bytes read/written are not
measured DRAM bytes; caches and repeated probes require hardware counters.

Do not begin with CPU-style pages, linked nodes, per-object allocation, or pointer chasing. GPU global memory is byte-addressable, but performance is governed by coalesced transactions, locality, and bulk work. A random access is not automatically fatal; it must be isolated, bounded, and measured. A design that can first partition or sort work into contiguous ranges is usually easier to reason about and exchange.

## Buffer Contract

Specify every buffer with this record:

```text
name
element type and ABI size/alignment
shape and stride
capacity formula and exact bytes
memory space and allocation owner
lifetime: persistent / iteration / job / temporary
mutability by phase
single writer or writer arbitration
readers
authoritative valid count/range
publication event/state
reuse/free event/state
overflow response
initialization and reset rule
```

If a consumer cannot identify the valid range without a host readback, hidden scan, or convention, the contract is incomplete.

## Representation And Materialization

For each stage ask what the next consumer truly needs. Possible representations include:

- full state;
- exact compact state encoding;
- hash or routing key;
- score plus original index;
- parent identifier plus transition;
- count/offset metadata.

Delay full materialization when compact metadata is enough, especially when most candidates die. Materialize earlier when most candidates survive and repeated reconstruction, random parent gathers, or communication of recipes costs more than storing full states. These are separate workload profiles; do not force one architecture to switch secretly during a run. Select the profile before launch or make the transition an explicit, tested design feature.

Preserve the original logical identity through compaction. An index created after filtering is not a substitute for the original candidate identifier when reconstruction depends on the original location.

## Lifetime Reuse And Overlays

Classify memory as:

```text
persistent state needed by the next iteration
read-only tables and weights
steady-state rings or queues
stage-local sort/scan/select temporary storage
communication send/receive regions
finalization-only regions
solution, error, and telemetry state
```

Two layouts may share one scratch pool only if their active lifetimes cannot overlap. State the drain event that ends the first lifetime and permits the overlay. Compute the pool as the maximum of mutually exclusive layouts, not their sum. Never overlay solved/error/control state that must survive phase changes.

Preallocate stable addresses for repeated kernels, CUDA Graphs, library workspaces, communication, and host staging. Query CUB/CCCL or other library temporary-storage sizes before entering the hot loop. If a fixed profile runs out of capacity, publish exact required/available counts and fail rather than truncate.

## Work Granularity And Rings

A ring is storage, not an algorithmic batch. Define separately:

```text
producer microbatch
number of producer slots accumulated
consumer batch
number of physical rings or ping-pong banks
candidate count in a partial tail
```

Use at least two banks when a producer must fill one while a consumer owns another. Add more only when a timeline proves starvation and the memory cost is justified. Every bank needs an explicit state such as `FREE`, `FILLING`, `READY`, `PROCESSING`, and a legal transition table.

## Readiness-Driven Jobs

Model the runtime as an asynchronous dependency graph, not as prose saying “stream 1, then stream 2, then stream 3.” Jobs may run concurrently when their exact inputs are ready.

For each job define:

```text
launch condition
input ownership
output ownership
CUDA stream or execution lane
wait events
completion event
resource returned on completion
```

Use a single writer for a mutable region whenever possible. When several producers feed one store, insert a collector/partition job or allocate disjoint ranges with an explicit prefix/count protocol. Avoid accidental multi-writer append counters.

Ping-pong uses two banks with alternating producer/consumer ownership. Roulette uses several independent ready jobs or shards so the dispatcher always selects useful work without imposing a global barrier. Both require bounded capacities and observable state transitions.

## CUDA Graph Boundary

Capture repeated fixed topology with stable pointers and launch shapes. Put variable valid counts, offsets, or flags in preallocated metadata read by fixed-shape kernels. Keep graph construction, uncommon control decisions, and semantically global finalization outside the repeated graph unless the device-side design explicitly handles them.

Do not assume CUDA Graphs remove the need for ownership or readiness. Graph nodes still need correct data lifetimes and cross-stream dependencies.

## Resource Mapping

Use the hardware unit that matches the operation:

- CUTLASS/cuBLAS or another dense library for tensor-core GEMM and dense transforms;
- CUDA kernels and CCCL/CUB for permutation, hashing, comparison, radix sort, reduce, scan, select, and compact;
- copy engines and pinned staging for transfers;
- NCCL for supported collectives and rank exchange.

Do not reformulate irregular work as GEMM merely to occupy tensor cores. Instead, overlap a tensor-heavy job with CUDA-core/memory/communication work when the dependency graph permits it. Validate overlap with a timeline because GEMM also consumes shared bandwidth, cache, registers, schedulers, and CUDA-core work.

Fuse jobs only when it removes material traffic or shares loaded data without creating excessive register pressure, occupancy loss, or a worse synchronization boundary. Cache reuse across separate kernels is a hypothesis, not a guarantee.

## Bulk Selection, Deduplication, And Routing

Prefer deterministic bulk transformations when the data is already batched:

```text
filter by a semantically safe threshold
compact valid records
sort or radix-partition by the necessary key
reduce adjacent equal keys with a deterministic representative rule
partition by destination
scan counts into offsets
write contiguous output ranges
```

This replaces many fine-grained random reads/writes and contested atomics with a small number of full array passes. Atomics remain valid when contention is demonstrably low or they express a simpler bounded primitive; do not ban or choose them without a workload argument.

Avoid sorting on fields that are not yet needed. For example, local deduplication may happen before calculating rank ownership if ownership is a pure function of the deduplication key. Conversely, routing first may be better if it shrinks local memory pressure. Treat both as measured architecture profiles.

## Multi-GPU Ownership

Keep these concepts separate:

- owner rank: the device responsible for global semantics for a key/state;
- local shard: a work partition inside one owner used for bounded jobs and concurrency;
- source rank: where a candidate or parent currently exists;
- target rank: where a materialized result must end up after balancing.

Define the owner function, seed/version, manual mapping controls if required, and reproducibility contract. Route by bulk partitioning into `count + offset + contiguous payload` regions. Define message ABI, maximum bytes, empty-peer behavior, ordering, and identical collective sequence across ranks.

Global deduplication, selection, thresholds, and balancing must retain their global meaning. A per-shard capacity is not silently a global top-k. Log local and global counts separately.

## Host And Disk

Keep Python, CPU reconstruction, logging, and disk writes outside the GPU data plane unless the architecture explicitly needs them. Use preallocated pinned host buffers and asynchronous copies for archival or history. Measure the full drain rate. If the chosen contract forbids backpressure, capacity exhaustion must be an explicit failure, not an unnoticed GPU stall or data loss.

Track archival ownership separately: GPU source may be reused after D2H ends;
the pinned slot remains owned until its downstream consumer is finished. A
successful pipe write/flush is a handoff, not evidence of disk or remote-service
durability. Name timers and commit markers for the boundary actually observed.

For a finite no-backpressure ring, budget maximum outstanding bytes: the maximum
cumulative production minus cumulative completed consumption over the run,
including bursts and downstream stalls. A background worker hides latency only
within this budget; sustained production above consumption eventually exhausts
any finite ring. Check final drain and failed/stalled-consumer shutdown too.
