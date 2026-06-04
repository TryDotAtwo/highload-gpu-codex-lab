---
name: use-compute-sanitizer
description: Use when CUDA reports illegal access, race, uninitialized memory, barrier/sync errors, or intermittent corruption.
---

# Use Compute Sanitizer

Correctness first; corrupt memory invalidates performance data.

| Symptom | Tool |
| --- | --- |
| Illegal/out-of-bounds/misaligned access | `memcheck` |
| Shared/global memory race | `racecheck` |
| Uninitialized device read | `initcheck` |
| Barrier/warp sync misuse | `synccheck` |

```bash
compute-sanitizer --tool memcheck --leak-check full ./small_repro ...
compute-sanitizer --tool racecheck ./small_repro ...
compute-sanitizer --tool initcheck ./small_repro ...
compute-sanitizer --tool synccheck ./small_repro ...
```

Reduce first: small input, deterministic seed, line info, assertions, capacity checks, focused phase logs. Remember that `cudaStreamSynchronize` often reports an earlier kernel failure, not the bug site.
