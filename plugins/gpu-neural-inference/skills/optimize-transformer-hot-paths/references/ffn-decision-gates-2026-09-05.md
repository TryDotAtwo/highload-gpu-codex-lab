# SM120 FFN decision audit, 2026-09-05

Supersedes the next-experiment recommendation in the September evidence audit,
not its historical observations. Scope: Cube4 FFN M=51072, D=256, H=1024.

## Retained evidence

- Historical stock CUTLASS FF1 + ReLU/NVFP4 pack + FF2: 660.03 TFLOP/s,
  two concurrent batches, global-addressed packed hidden and BF16 final output.
  This was neither zero-global-hidden fusion nor whole Stream1.
- Recovered identical binary SHA256
  `06d39d910b6e71fb29086289d7185a27c76042d60de8ccfa09813c7ff81b71b4`:
  September 5 one-slot 95.463 us / 560.980 TFLOP/s; two-slot aggregate
  175.086 us / 611.731 TFLOP/s. These are screens, not seven alternating trials.
  M1024 seeds 1/7/42 scalar-oracle hidden/scales/final checks had zero mismatches.
- September 4 already rejected role4 at approximately 612.649 us / 87.412 TFLOP/s.
  September 5 repeated full serial-pair result: 615.618 us / 86.9904 TFLOP/s.
  FP32 final output differs from stock BF16: do not present the ratio as an
  isolated causal measurement. Resource report: 168 registers, 416 local bytes,
  87040 shared bytes. Spills/setup/barriers remain hypotheses without counters.
- 733 TFLOP/s FF1 omitted output conversion/payload; not an eligible baseline.
- Enlarged coded-sparse physical FLOPs are not useful dense FFN FLOPs.
- Historical full Stream1 B896: 1.50765 ms / 221.04 TFLOP/s. Do not equate
  FFN or aggregate two-batch throughput with this end-to-end metric.

## Feasibility, not promises

Useful FFN work is 53,552,873,472 FLOPs per batch. 1 PFLOP/s requires
53.552873472 us per batch, or 107.105746944 us for two batches. Relative to the
fresh screens this requires approximately 44% single-slot or 39% aggregate
latency reduction. Aggregate time divided by two is not request latency.

Whole Stream1 needs about 4.52x versus its historical point. Even eliminating
one stage entirely cannot provide that unless it owns at least 77.9% of the
matched critical path. No current matched stage profile establishes that.
Synthetic 1.21 PFLOP/s does not prove either feasibility or impossibility for
the complete fixed-shape operator graph.

## Required next decision

1. Recover the eligible stock incumbent, not the latest slow source by date.
2. Profile matched output/shape/concurrency: FF1, pack/epilogue, FF2, handoff,
   launch gaps and actual traffic. Retain unprofiled timing independently.
3. Permit at most two new counter-backed changes before reviewing the route;
   this is a proposed campaign budget, not an architectural law.
4. Compare with seven alternating baseline/candidate trials and complete output
   semantics. Whole-model solve-quality gates remain separate and open.
5. Do not repeat role4, transpose, giant-CTA or cache-policy failures without a
   specific new mechanism. Faster-than-slow-prototype is insufficient.

Sources in stream1-generic-seq-align worktree: test_results/
molab_recovered_fast_control_20260905.log, molab_ffn_recovery_20260905.md,
sm120_ffn_control_and_persistent_candidate_2026-09-04.md,
sm120_campaign_decision_audit_20260905.md. These are dated observations, not
portable performance guarantees. A physical no-go for substantial speedup has
not been established; an unconditional 1 PFLOP/s commitment is also unsupported.
