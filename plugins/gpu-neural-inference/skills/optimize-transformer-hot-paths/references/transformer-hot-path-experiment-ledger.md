# Transformer Hot-Path Experiment Ledger

Historical checkpoint. Read `ffn-evidence-audit-2026-09.md` before reusing
shared-output timing or prepared-only status below; subsequent native callback,
payload-liveness and numerical audits narrowed or superseded those claims.

## Exact FP16 progression

Case: Cube4 Piece Transformer, output-24, ReLU, SM120, beam `2^25`, exact `depth_done=8`.

| Change | Depth-8 result | Decision |
|---|---:|---|
| initial SM120 CUDA profile | 124.367 s | control |
| measured m128n128 auto policies | 111.024 s | accept |
| compact57 + final CLS/Q=1 | 84.2199 s | accept |
| final CLS split QKV | **80.2952 s** | accepted baseline |
| incomplete profile without final-CLS flags | 128.046 s | reject as comparator |
| cuBLASLt immutable profile | 150.125 s | reject |
| separate-ReLU in-process control | 103.374 s | control for fused-ReLU A/B |
| fused ReLU | 83.4427 s | positive, 19.28% on its matched control |

Do not compare 83.4427 directly with 80.2952 as if they were one paired run; process/build conditions differed.

## Accepted exact-shape changes

- `compact57` preserved a byte-identical score dump and reduced scratch 12.56%.
- final CLS Q=1 `q32k64` beat full-query final attention in repeated processes.
- split final Q from full K/V gave another 1.046x integrated speedup.
- fused ReLU removed one full hidden-tensor read/write pass and preserved frontier, threshold and jobs.

## Rejected exact-FP16 paths

- larger FF1/FF2/attention-output tiles regressed 0.4–3.2%; removed;
- exact32 attention lost the repeated gate despite a promising screen;
- persistent LayerNorm changed the score digest;
- raw cuBLAS FF1 omitted fused bias/activation and FF2 lost to CUTLASS;
- fused residual rounded to FP16 before LayerNorm and changed arithmetic semantics;
- CUDA Graph did not beat eager in one accepted fixed-shape screen, proving launch overhead was not the primary bottleneck.

## FFN and intermediate traffic

The measured warm-stage profile assigned about 37% of three-layer time to FF1+FF2, but full Stream1 also contains attention, normalization and output. FFN-only fusion cannot make the entire Transformer equal to its raw MMA ceiling.

The retained direction is:

```text
FF1 accumulation
  -> ReLU + block scale + packed hidden
  -> CTA/shared or DSM handoff
  -> FF2 accumulation
  -> residual + exact LayerNorm + next-layer emission
```

Removing global hidden is an experiment, not an unconditional speed guarantee.
Persisting-L2 policy gave only noise at M51072 and regressed at larger working
sets. Actual cache residency was not measured; retain the fast global-handoff
control until a correct replacement wins at the same boundary.

## Persistent and DSM progression

- two-slot CUTLASS ping-pong real FFN: 660.03 TFLOP/s;
- FA4-style nine-stage ownership oracle: pass;
- remote DSM A/SFA + TMA B/SFB numerical gates: pass;
- bulk DSM and one-way mbarrier reduced remote eight-slice latency;
- manual one-warpgroup DSM scheduler was far below stock and rejected;
- an early native register-D seam screen reported `8.23056 us` versus stock
  `8.23648 us`; do not use it as a complete-output throughput certificate:
  subsequent audits required proving hook forwarding and payload liveness in
  the exact timed binary;
- complete persistent consumer compile gate passed;
- final physical-cluster/logical-singleton fused binary was prepared but not executed after session loss.

## FlashAttention-4 lessons

Use FlashAttention-4 as a scheduling reference:

- persistent work distribution;
- warp-role specialization;
- explicit producer/consumer lifetime;
- ping-pong buffers;
- overlap current compute with previous consumption;
- minimal synchronization at ownership boundaries.

Do not copy SM100 TMEM/UMMA machinery to SM120. The working SM120 path uses TMA/shared staging plus register-accumulating warp MMA.

## End-to-end boundary

Raw >1 PFLOP/s MMA and a 660 TFLOP/s FFN component do not prove 1 PFLOP/s end-to-end Stream1. Promotion requires full four-layer timing, same model/workload fingerprint and task-level solve quality.
