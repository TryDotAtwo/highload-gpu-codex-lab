---
name: use-compute-sanitizer
description: Use when debugging CUDA memory or race errors.
---

# Use Compute Sanitizer

| Symptom | Tool |
| --- | --- |
| Illegal/out-of-bounds/misaligned access | `memcheck` |
| Shared-memory access hazard | `racecheck` |
| Uninitialized device read | `initcheck` |
| Barrier/warp sync misuse | `synccheck` |

```bash
compute-sanitizer --tool memcheck --leak-check full ./small_repro ...
compute-sanitizer --tool racecheck ./small_repro ...
compute-sanitizer --tool initcheck ./small_repro ...
compute-sanitizer --tool synccheck ./small_repro ...
```

Reduce first: small input, deterministic seed, line info, assertions, capacity checks, focused logs. `cudaStreamSynchronize` often reports an earlier kernel failure.

## Stalls and evidence limits

A timeout is an unresolved result, not a pass or proof of a kernel defect. Before repeating an unchanged timed-out probe, identify its last completed phase with flushed per-rank markers: process startup, communicator initialization, allocation/registration, launch, completion, teardown. Reduce to the first stalled phase and compare plain versus instrumented execution on the same source and hardware. Increase the timeout only when observed progress or measured instrumentation overhead supports it.

For multi-GPU tests, preserve matching collective order and zero-payload participation while reducing the reproducer. Record toolkit, sanitizer and communication-library versions, device topology, command, exit status and raw logs. Keep unrelated validation progressing when a diagnostic stalls.

Kernel filters and disabled CUDA API error reporting can isolate a failure, but narrow the evidence: record these options and retain the unfiltered failure. A filtered pass does not close an unfiltered gate. Racecheck does not establish absence of global-memory or inter-GPU protocol races; verify ownership, visibility and buffer reuse separately. A leaf transport pass does not validate its integration into an application.
