---
name: tune-gpu-beam-profiles
description: Use when tuning beam width, outer candidate batch, inference microbatch, accumulator chunks, ring slots, shards, concurrency, downstream job count, or automatic beam profiles.
---

# Tune GPU Beam Profiles

## Name Both Batch Levels

Never write only `B_MICRO` in analysis. Record:

- **outer candidate batch:** physical/logical scorer-to-pipeline transaction size;
- **model inference microbatch:** examples processed by one model forward.

For Piece Transformer, `B_MICRO`/outer batch and `BEAM_STREAM1_TRANSFORMER_MICRO`/model microbatch are distinct. A large outer slot can require many small Transformer forwards.

## Sweep Order

1. Freeze puzzle/input, model/head, precision, requested beam, depth, build, and hardware.
2. Tune model inference microbatch and scorer concurrency in isolation.
3. Choose accumulator size to reduce downstream jobs without exceeding memory or delaying overlap.
4. Sweep physical ring slots from two upward using queue-wait evidence.
5. Sweep shards and downstream concurrency.
6. Tune capacity margin, final materialization, history, BFS, and solution buffers separately.
7. Re-run the whole depth loop.

For expanding searches, run through depth 8 and compare the exact `depth_done=8` steady-state row. A target near hundreds of downstream jobs, such as 400, is a hypothesis; choose by wall time and stalls.

## Profile Table

Key profiles by hardware, GPU count, model family, head/output dimension, precision, beam anchor, and search mode. For a user-requested beam choose the nearest compatible anchor, apply only required alignment, and preserve/report the requested and effective values.

Reject OOM, overflow, hidden truncation, unstable, and slower rows. Select the fastest stable row with measured memory margin.
