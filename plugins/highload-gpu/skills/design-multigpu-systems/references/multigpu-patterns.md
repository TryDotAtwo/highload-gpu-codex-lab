# Multi-GPU Patterns

## Design Pattern

- Use one owner and one writer per mutable buffer.
- Use double buffers or rings for producer/consumer overlap. Publish async state only after events or fences make writes visible.
- Avoid global barriers unless correctness requires a global count, threshold, rebalance, checkpoint, or collective.
- Prefer NCCL for collectives and GPU-to-GPU exchange. Verify collective ordering is identical on all ranks.
- Confirm topology: same node vs multi-node, PCIe/NVLink, peer access, NUMA, NIC binding, and container visibility.
- Overlap compute and communication only after the non-overlapped version is correct and measurable.

## Startup, Failure, And Device-Side Exchange

Treat partial construction as part of the distributed protocol. Reserve the
failure-control path before large fallible allocations. If one rank fails before
the next collective, define how peers escape it and how partially constructed
communicators are aborted or destroyed. Ordinary RAII/graceful destruction may
itself wait for peers; an error return is not proof of bounded group termination.
Do not allocate fresh GPU scratch to report an allocation failure.

Inject a one-rank allocation/registration failure in the actual runtime, not only
in a leaf harness. Check peer exit, last phase markers, cleanup, and absence of
leftover processes. Also test empty payloads, a delayed rank, asymmetric batch
counts, and slot reuse across rounds at the supported rank counts.

For device-side NCCL or peer-memory protocols, list every rendezvous's team,
participation rule, visibility guarantees, and ordering relative to owner jobs
and buffer reuse. A peer payload can still use a whole-team barrier. Device-held
counts eliminate a host-size handshake only where runtime dispatch actually
uses them; they do not prove that routing, termination, or fatal votes are
host-independent. Confirm the complete path on a timeline.

## Failure Smells

- Single-GPU passes but multi-GPU fails: suspect ownership, capacity per rank, stale state, or collective ordering.
- Silent stall: inspect rank logs and NCCL/stream progress before adding backpressure.
- Good single-GPU kernels but poor scaling: inspect exchange volume, load imbalance, host launch serialization, topology, and synchronization.
- Backpressure that hides overflow may mask the bug that larger GPU counts need to expose.
