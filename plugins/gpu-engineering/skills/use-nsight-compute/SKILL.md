---
name: use-nsight-compute
description: Use when profiling one CUDA kernel.
---

# Use Nsight Compute

Use Nsight Compute after evidence points to one kernel.

```bash
ncu --set full --target-processes all --kernel-name regex:kernel_name --launch-skip 5 --launch-count 10 --force-overwrite -o ncu_kernel ./runner ...
```

Prefer small reproductions. Check critical-path kernel, occupancy limiter, memory throughput/load efficiency, stalls, tensor-core use, and register/shared-memory pressure.

Do not use NCU first for whole-pipeline scheduling; use Nsight Systems.
