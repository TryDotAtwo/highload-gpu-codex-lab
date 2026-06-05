---
name: use-nsight-systems
description: Use when analyzing GPU timelines.
---

# Use Nsight Systems

Use Nsight Systems for timeline questions: what ran when, why streams are idle, whether CPU launch/sync blocks the GPU, and whether NCCL overlaps compute.

```bash
nsys profile --trace=cuda,nvtx,osrt,cublas,nccl --stats=true --force-overwrite=true -o nsys_run ./runner ...
nsys stats nsys_run.nsys-rep
nsys export --type sqlite --force-overwrite=true -o nsys_run.sqlite nsys_run.nsys-rep
```

Profile a bounded representative window. Add NVTX ranges around depth, stage, rank, shard, and finalization.

Inspect: stream overlap, idle gaps, long CUDA API calls, graph replay/instantiation, NCCL duration/order, host thread blocking, and timeline alignment with logs. If the timeline shows pipeline idle, do not tune a single kernel first.
