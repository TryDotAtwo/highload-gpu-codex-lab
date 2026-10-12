# GPU Architecture Specification Template

Use this only when a full architecture artifact is requested. During incremental design, emit only the current boundary and update the artifact after confirmation.

```markdown
# <System> GPU Architecture

## Status

- Design version:
- Source of truth:
- Interaction mode: collaborative | autonomous
- Evidence state:
- Target hardware/software:

## Decision ledger

### Confirmed

### Proposed assumptions

### Open

### Rejected

## Semantic contract

- Logical input and output:
- Exactness/approximation:
- Identity and deduplication:
- Ordering and deterministic tie-break:
- Termination:
- Failure behavior:
- Correctness oracle:

## Configuration and derived dimensions

| Symbol | Meaning | Value/formula | Runtime or compile-time | Constraint |
|---|---|---|---|---|

## ABI and encodings

For each structure:

- fields and bit encoding;
- size and alignment;
- padding initialization;
- producer and consumers;
- persistent or transport form;
- static assertions.

## Memory map

| Region | Type/shape | Exact bytes | Location | Lifetime | Writer | Readers | Valid count | Ready/free | Overflow |
|---|---|---:|---|---|---|---|---|---|---|

Include persistent memory, read-only data, rings, scratch layouts, library temporary storage, communication, finalization, host staging, and reserve. State all legal overlays and their drain event.

## Dispatcher and asynchronous job graph

For each job:

| Job | Launch predicate | Inputs | Outputs | Execution lane | Waits | Completion | Released resource |
|---|---|---|---|---|---|---|---|

State the legal resource-state transitions and CUDA Graph template boundaries.

## Job contracts

For each job:

### <Job name>

- Input representation and valid range:
- Work and semantic invariant:
- Output representation and count:
- Memory-access pattern:
- Library/custom-kernel choice:
- Capacity and failure:
- Reference test:

## Multi-GPU protocol

- Owner function and reproducibility:
- Local shard mapping:
- Message ABI:
- Partition/sort order:
- Send/receive count and offset protocol:
- Collective sequence including empty traffic:
- Capacity guards:
- Global semantics and load balancing:
- Termination protocol:

## Finalization and iteration transition

- Drain condition:
- Final global operations:
- History/host/disk transfer:
- Materialization:
- Persistent-state swap:
- Reset for the next iteration:

## Failure and diagnostic contract

- Overflow:
- Invalid metadata:
- CUDA/graph/library failure:
- Rank or collective mismatch:
- Unsupported profile/hardware:
- Host/disk staging exhaustion:
- Required counters and logs:

## Capacity proof

- Exact per-region byte formulas:
- Per-rank total:
- Replicated/global total:
- Runtime reserve:
- Maximum safe requested size:
- Requested-to-effective alignment rule:

## Validation plan and evidence

| Slice | Correctness oracle | Hardware/ranks | Acceptance marker | Current status |
|---|---|---|---|---|

## Performance hypotheses

For each hypothesis give the expected bottleneck, byte/operation model, competing resources, profiler evidence required, and alternative if disproved.
```

Do not populate an unknown section with generic filler. Mark it `open`, explain why it blocks implementation, and state the smallest decision or measurement that resolves it.
