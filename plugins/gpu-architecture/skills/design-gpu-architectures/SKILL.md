---
name: design-gpu-architectures
description: Design or audit a complete CUDA/GPU execution architecture before implementation, including exact data layouts, buffer ownership and lifetimes, asynchronous jobs, CUDA Graph boundaries, bulk primitives, multi-GPU routing, capacity failures, and staged validation. Use for whole-system design; use a kernel or profiler skill for an isolated hot path.
---

# Design GPU Architectures

Build an architecture that can be implemented without inventing missing semantics. The result must be explicit about data, ownership, readiness, capacity, and evidence. Do not confuse a plausible proposal with an accepted design or an implemented system.

## Read The Relevant Guidance

- Always read [architecture-process.md](references/architecture-process.md) and [dataflow-and-memory.md](references/dataflow-and-memory.md).
- Before approving a design or turning it into code, read [audit-and-validation.md](references/audit-and-validation.md).
- When producing a complete architecture document, use [architecture-spec-template.md](references/architecture-spec-template.md). Do not dump that full structure during a one-question design discussion.
- For large frontier, search, deduplication, or multi-stage streaming systems, also read [lessons-from-frontier-design.md](references/lessons-from-frontier-design.md).

## Establish The Mode

- In collaborative mode, discuss exactly one unresolved boundary at a time. Keep downstream stages skeletal. Add a decision to the accepted architecture only after the user confirms it.
- In autonomous mode, make the missing choices, but label evidence, assumptions, proposals, and unresolved risks. Run the full audit before presenting the result. Autonomous authority does not turn assumptions into facts.
- Default user-facing discussion to concise answers. Put the complete architecture in an artifact when it is large.

## Core Workflow

1. Inspect the algorithm, current code, prior decisions, logs, target hardware, and correctness oracle. Treat prior assistant suggestions as proposals unless the user or current source of truth accepted them.
2. Freeze semantics before scheduling: exact output, approximation policy, duplicate identity, ordering, determinism, collision policy, termination, and failure behavior.
3. Name every unit of work and give its formula: logical element, model microbatch, producer slot, downstream batch, ring, shard job, rank-local frontier, global frontier, and finalization unit. Never let one name or counter silently mean two physical resources.
4. Design one producer-consumer boundary at a time. For every boundary define the representation, valid range, producer, publication event, consumer, reuse condition, and overflow behavior.
5. Lay out all persistent and scratch memory before choosing kernels. Compute exact bytes using real ABI sizes, alignment, library temporary storage, replication, and double buffering.
6. Map work to resources: dense algebra to tensor-core libraries; irregular transforms, sort, scan, select, and compaction to CUDA/CCCL; transfers to copy engines and NCCL. Overlap jobs only where their resource demands and dependencies permit it.
7. Define the readiness-driven job graph, its CUDA Graph templates, host/device dispatcher responsibilities, and the single point where a global barrier or finalization is semantically required.
8. Define rank ownership separately from local sharding. Group communication into contiguous destination ranges and make collective ordering and capacities explicit.
9. Audit the design, then implement it as dependency-ordered vertical slices. A slice is complete only when its own correctness oracle and target-relevant runtime gate pass.

## Non-Negotiable Output Rules

- Maintain a decision ledger with `confirmed`, `proposed`, `open`, and `rejected` states. Do not silently resurrect rejected designs.
- Separate the desired architecture, current implementation, and measured runtime state.
- For every array or pool give type, shape, alignment, capacity, memory location, lifetime, writer, readers, valid-count source, readiness, reuse, and overflow contract.
- Prefer stable-address, preallocated hot paths. If the chosen profile forbids fallback or dynamic growth, fail loudly instead of silently truncating, reallocating, or switching algorithms.
- Reason from byte layout, bit fields, alignment, warp access, and memory transactions. Do not import CPU-style page lists, pointer-rich containers, or fine-grained random mutation without evidence.
- Preserve logical identity through filter, compact, sort, deduplication, routing, and materialization. Define deterministic tie-breaking.
- Never claim multi-GPU correctness from a one-GPU test, or performance from compilation and smoke tests.
- Check current official CUDA, CUTLASS, CCCL/CUB, and NCCL documentation for hardware- or version-sensitive claims.
