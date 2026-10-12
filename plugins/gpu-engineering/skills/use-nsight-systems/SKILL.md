---
name: use-nsight-systems
description: Use when analyzing GPU timelines.
---

# Use Nsight Systems

Use Nsight Systems for stream idle gaps, CPU launch/sync blocks, and NCCL/compute overlap.

```bash
nsys profile --trace=cuda,nvtx,osrt,cublas,nccl --stats=true --force-overwrite=true -o nsys_run ./runner ...
nsys stats nsys_run.nsys-rep
nsys export --type sqlite --force-overwrite=true -o nsys_run.sqlite nsys_run.nsys-rep
```

Profile a bounded window. Add NVTX around batch, stage, stream, rank, shard, communication, and pipeline phase.

Inspect stream overlap, idle gaps, long CUDA API calls, graph replay/instantiation, NCCL order, host blocking, and log alignment.
