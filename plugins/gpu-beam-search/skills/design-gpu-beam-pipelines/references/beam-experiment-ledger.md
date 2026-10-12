# Beam Pipeline Experiment Ledger

This ledger captures reusable measurements from the CayleyPy 2xT4 and SM120 campaigns. Treat the numbers as hardware/workload evidence, not universal constants.

## Two batching levels

- **Outer candidate batch** controls one pipeline transaction.
- **Inference microbatch** controls one model forward.
- For output-24 Transformer on T4, one measured microtransaction was `384 * 24 = 9,216` candidates.
- A large logical accumulation may contain many microtransactions while using only a small physical ring.

Never bind logical accumulation count, graph templates, Stream5 exchange buffers and physical ring allocation to one integer.

## Kaggle 2xT4, global beam 2^26

Workload: Cube4 Transformer output-24, global beam `67,108,864`, local frontier `33,554,432` per rank, exact `depth_done=8`.

| Profile | Logical Stream3 batch | Physical ring | Final chunk | Depth-8 seconds | Peak MiB/GPU | Decision |
|---|---:|---:|---:|---:|---:|---|
| small control | 18,432 | 2 | coupled | 3,304.95 | 13,535 | control |
| prior Stream4 winner | 18,432 | small pool | coupled | 3,157.70 | 13,295 | superseded |
| accumulator 88 | 811,008 | 2 | coupled | 3,001.40 | 14,587 | positive |
| accumulator 192 | **1,769,472** | **2** | **88,064** | **2,765.04** | **13,003** | accepted |
| accumulator 192 | 1,769,472 | 2 | 98,304 | 3,302.62 | 13,025 | reject |

The small `18,432` batch implied about **43,691** Stream3 jobs per depth/rank. `192 * 9,216 = 1,769,472` reduced that to a few hundred while retaining two physical buffers. A larger `98,304` final chunk was 19.44% slower than `88,064` despite similar memory.

## Molab beam 2^25 profile shape

A later single-GPU Cube4 output-24 profile used:

- outer parent batch `3,584`;
- Transformer inference microbatch `896`;
- inference concurrency `4`;
- two inference rings/windows;
- 24 logical Stream3 accumulation slots;
- Stream3 batch `2,064,384` candidates;
- 16 shards;
- final materialization `88,064`;
- **391** Stream3 jobs at full frontier.

Reducing Stream3 jobs from 2,341 to 391 changed full-depth time by only about 0.4–0.6% in the first comparison. Therefore “about 400 jobs” is a useful scheduling target, not the objective; exact depth-8 wall time remains the selection metric.

## Final materialization policy

`88,064` was explicitly validated across 31 public 2xT4 profiles and a private beam `2^16` acceptance. It is an empirical T4 profile value. Keep final materialization independent from the large accumulator because final request/response/history exchange buffers scale differently and may provide no speedup when enlarged.

## Rank accounting

Logs are usually per rank:

```text
global beam ~= world_size * per-rank frontier
```

A `524,288` frontier in each of two rank logs can represent a global `1,048,576` beam. Report both values; do not diagnose a missing half-beam from one rank line.

## Profile selection rule

1. Tune model microbatch/concurrency independently.
2. Choose logical accumulation to reduce downstream job overhead.
3. Sweep a small physical slot pool for overlap and memory.
4. Tune shards/capacity with exact fit and overflow evidence.
5. Keep final materialization separate.
6. Compare exact steady-state depth rows on identical frontier/model/hardware.
7. Retain rejected rows; never infer a smooth monotonic scaling law.
