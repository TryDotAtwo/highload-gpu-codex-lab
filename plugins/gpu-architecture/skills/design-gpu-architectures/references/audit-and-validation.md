# Architecture Audit And Validation

## Pre-Implementation Audit

Run the audit against the canonical architecture, not a paraphrased summary.

### Semantic audit

- Is exactness versus approximation explicit?
- Does deduplication compare the intended identity rather than merely a convenient key?
- Are hash collisions, score ties, ordering, and determinism defined?
- Can filtering be moved earlier without changing semantics?
- Is termination visible and safe while asynchronous work is in flight?

### Data audit

- Can every field be traced from its producer to its final consumer?
- Does compaction retain the original identifier needed for reconstruction?
- Are requested, aligned effective, rank-local, and global counts distinct?
- Does each partial tail carry an authoritative valid count?
- Are padding and reserved bits initialized before hashing, comparison, transport, and persistence?

### Memory audit

- Are exact ABI sizes and alignments enforced with static assertions?
- Does the byte budget include all replicas, rings, ping-pong banks, CUB/CCCL temporary storage, NCCL buffers, graph state, host pinned buffers, allocator/runtime reserve, and finalization overlays?
- Are overlay lifetimes truly disjoint and protected by a drain event?
- Are there hidden allocations, implicit framework temporaries, or fallback copies?
- Does every capacity guard fail before an out-of-bounds write?

Use checked arithmetic for byte formulas. Report both required and available capacity. A percentage estimate is not a memory proof.

### Concurrency audit

- Is the job graph acyclic within an iteration, aside from explicit reusable resource loops?
- Is every publication event recorded after all writes it protects?
- Can a bank be reused while a consumer still owns it?
- Does each mutable region have one writer or an exact arbitration protocol?
- Can one slow job starve all work, and does roulette/ping-pong actually provide another ready unit?
- Is finalization entered only after all producers, collectors, communication, and shard jobs drain?

### Multi-GPU audit

- Is owner mapping deterministic and identical on all ranks?
- Are send/receive counts and offsets bounded independently on every rank?
- Do all ranks issue collectives in the same order, including empty ranges and early termination?
- Is load balance a semantic stage rather than an accidental result of hashing?
- Are one-rank shortcuts behaviorally equivalent to the multi-rank protocol?

### Resource audit

- Which job is tensor-core, CUDA-core, bandwidth, latency, copy-engine, or network dominated?
- Which jobs are expected to overlap, and what shared resources can invalidate that expectation?
- Are sort, scans, compaction, routing, and materialization counted as full byte passes?
- Is fusion supported by data-reuse evidence rather than launch-count aesthetics?

### Failure and observability audit

- Are overflow, invalid count, collective mismatch, graph capture failure, unsupported hardware, and disk/host staging exhaustion explicit?
- Are silent truncation, implicit reallocations, and unlogged fallback forbidden where they would change behavior?
- Can logs reconstruct job state, capacities, local/global counts, and the first failing rank without synchronizing the hot path?

## Implementation Slices

Implement in dependency order. A useful order for complex streaming systems is:

1. configuration, derived dimensions, ABI structures, static assertions, and byte-accurate memory layout;
2. small deterministic leaf transformations with CPU/reference oracles;
3. reconstruction/final materialization path, because it proves compact metadata is sufficient;
4. one isolated local bulk stage such as filter/compact/sort/dedup;
5. one isolated persistent/sharded merge stage;
6. one-rank exchange semantics, then real multi-rank exchange;
7. dispatcher state machine and CUDA Graph templates;
8. one complete iteration with tails, empty inputs, and capacity guards;
9. several iterations with history/termination;
10. target-hardware scaling and profiling.

Change this order when dependencies require it, but keep every slice independently testable. Do not implement an entire asynchronous system before proving its representation and boundary contracts.

## Acceptance Ledger

For an existing system, first trace one real execution path:

```text
user configuration -> executable/feature flags -> runtime dispatch
-> library/kernel calls -> completion/output contract -> matching test
```

Record the source revision, dirty-file scope, and binary/config used by each
test. A scheduler model, implemented leaf kernel, captured owner graph, and
production dispatcher are different acceptance scopes. Search actual callers;
the presence of a type, option, or passing isolated test does not prove runtime
integration. Recheck findings when another worker changes the inspected code.

Audit synchronization transitively through FFI and utility wrappers, including
host-returned counts and buffer uploads. Classify semantic layer boundaries,
host waits, GPU event dependencies, and device-team rendezvous separately.
Moving a collective onto the GPU removes neither its participants nor its
ordering constraints. Capture success is not proof of overlap in a real run.

For every slice record:

```text
scope implemented
scope deliberately excluded
tests run with exact commands
target device, rank count, and software versions
observable pass/fail markers
generated artifacts
remaining unverified claims
next dependency now unlocked
```

Use evidence states such as:

```text
static-green
single-gpu-green
multi-gpu-green
scale-green
profiled
partial
blocked
```

Never shorten `single-gpu-green, multi-gpu pending` to `green`.

## Validation Matrix

At minimum cover:

- compile and link on the target architecture;
- ABI, alignment, and scratch-offset assertions;
- CPU/reference comparison for small deterministic inputs;
- zero, one, partial-tail, full-capacity, and overflow inputs;
- duplicated keys, score ties, collision policy, and deterministic replay;
- event visibility, bank reuse, and stale metadata across iterations;
- one-rank protocol path;
- at least two ranks with asymmetric and empty-peer traffic;
- asymmetric startup/allocation failures, a delayed rank, and repeated slot reuse;
- complete iteration and multi-iteration semantics;
- maximum intended capacity or an analytically justified scaled test;
- Nsight Systems timeline for overlap, gaps, collectives, and host stalls;
- Nsight Compute for the actual hot kernel only after system correctness.

The target hardware matters. A local RTX build may validate CUDA code generation but not a two-T4 NCCL path, an NVLink topology, or a Blackwell-specific kernel.

When an output crosses a process or service boundary, test the named completion
contract: GPU source reusable, host copy complete, local file durable, and remote
artifact committed are different events. Checksums establish byte integrity;
layer histograms establish counts; neither alone establishes full-state BFS
identity or uniqueness. Keep those evidence claims separate.

## Architecture Review Result

Return findings in dependency order. For each blocker state:

```text
missing or contradictory contract
why implementation cannot be proven correct
smallest decision that resolves it
affected structures/jobs
required validation
```

Do not inflate the audit with generic optimization ideas. A finding must change correctness, implementability, boundedness, or a measurable performance hypothesis.
