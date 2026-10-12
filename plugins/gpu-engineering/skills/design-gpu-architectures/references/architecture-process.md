# Architecture Process

## Goal

Derive an executable GPU architecture from semantics and constraints. Do not begin with a list of streams or favorite CUDA techniques. Begin with what must remain true, what data must exist, and when it is needed.

## 1. Build The Evidence Base

Inspect the current source, configuration, prior architecture records, representative inputs, logs, and target hardware. Record three different states:

- desired design: what the system should become;
- implemented state: what the current code actually does;
- measured state: what current traces and tests demonstrate.

Do not merge these states. A structure appearing in a design document does not prove it exists. A successful build does not prove its runtime semantics. A single-device smoke does not validate a collective.

When a prior discussion is the source of truth, reconstruct its decision history. User confirmations and explicit current artifacts outrank old assistant summaries. A later correction invalidates the earlier proposal.

## 2. Freeze Semantics

Before drawing the execution graph, answer:

- What is one logical input, transition, candidate, result, and iteration?
- Is the result exact or approximate? Which approximation is allowed?
- What makes two logical objects identical?
- If a hash is used, is equality probabilistic or followed by exact comparison?
- What ordering or score relation selects a representative?
- What tie-break makes the result deterministic?
- What must survive for history, reconstruction, retry, or replay?
- What terminates an iteration and the whole run?
- Which overflows must abort rather than change semantics?

If one of these answers is missing, mark it `open`. Scheduling cannot repair undefined semantics.

## 3. Name Dimensions Before Buffers

Define symbols and formulas for every scale. Typical examples:

```text
STATE_BYTES
MOVE_COUNT
PARENT_MICROBATCH
CANDIDATES_PER_PARENT
STAGE_BATCH_CANDIDATES
RING_SLOT_COUNT
RING_COUNT
SHARD_COUNT_PER_RANK
WORLD_SIZE
LOCAL_CAPACITY
GLOBAL_CAPACITY_REQUESTED
GLOBAL_CAPACITY_EFFECTIVE
```

Write every derived relation and divisibility/alignment requirement. Distinguish:

- logical batch size from physical ring storage;
- number of producer microbatches from one consumer job size;
- one ring slot from the entire ring;
- rank ownership from a local work shard;
- requested capacity from aligned effective capacity;
- per-rank counts from global counts.

Ambiguous nouns become buffer and synchronization bugs later.

## 4. Keep A Decision Ledger

Use four states:

```text
confirmed  accepted by the source of truth
proposed   selected by the architect but not yet confirmed or measured
open       genuinely unresolved
rejected   considered and explicitly discarded
```

Each consequential entry should carry:

```text
question
decision state
chosen answer
reason or evidence
affected buffers/jobs/protocols
validation needed
```

In collaborative work, update the canonical architecture after each accepted decision, but elaborate only the part currently under discussion. Leave later stages short. In autonomous work, resolve what can be resolved, retain visible assumptions, and run the audit before promoting a proposal.

## 5. Resolve One Boundary At A Time

For a boundary `producer -> consumer`, establish:

```text
logical input
physical input layout
work performed
physical output layout
valid count/range
writer
publication event or state
consumer
reuse/free condition
capacity and overflow behavior
```

Only then move to the next boundary. This prevents a premature full diagram from concealing undefined ownership or an impossible buffer lifetime.

## 6. Canonical Architecture Order

When enough decisions are known, maintain one canonical document in this order:

1. scope and semantic contract;
2. target hardware and software stack;
3. configuration and derived constants;
4. ABI structures and encoding contracts;
5. memory map and lifetime overlays;
6. scheduler/dispatcher and job-state model;
7. each job or stage: input, work, output, readiness, capacity;
8. cross-rank protocol and collective order;
9. iteration finalization and state transition;
10. failure contracts and diagnostics;
11. validation stages and evidence status;
12. open, proposed, and rejected decisions.

Do not duplicate the same contract in several incompatible summaries. Rewrite the canonical snapshot when a decision changes.

## 7. Architecture Freeze

The design is ready for implementation only when:

- every hot-path datum has an owner and lifetime;
- every job has exact inputs, outputs, and readiness conditions;
- all variable-length regions have an authoritative count;
- all capacities and temporary-storage requirements are computed;
- all rank-local and global semantics are distinguished;
- finalization has an explicit drain condition;
- failure behavior does not silently alter the algorithm;
- unresolved items are non-blocking or explicitly scoped out;
- the validation plan can distinguish a correct implementation from a plausible one.

Do not call a document complete merely because it is long.
