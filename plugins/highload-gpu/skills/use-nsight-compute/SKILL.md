---
name: use-nsight-compute
description: Use when profiling one CUDA/CUTLASS/CUB kernel, occupancy, memory throughput, warp stalls, or register/shared memory pressure.
---

# Use Nsight Compute

Use Nsight Compute after evidence points to a specific kernel.

```bash
ncu --set full --target-processes all --kernel-name regex:kernel_name --launch-skip 5 --launch-count 10 --force-overwrite -o ncu_kernel ./runner ...
```

Prefer small reproductions or isolated microbenchmarks. Check, in order: actual critical-path kernel, occupancy limiter, memory throughput/load efficiency, dominant stall reasons, tensor-core utilization for GEMM, register/shared-memory pressure. Change one variable and re-profile.

Do not use NCU first for whole-pipeline scheduling; use Nsight Systems.