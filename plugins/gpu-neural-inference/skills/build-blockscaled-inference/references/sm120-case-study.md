# SM120 Fixed-Shape Case Study

These are project measurements, not portable constants.

For corrections and later completed gates through September3, read
`../../optimize-transformer-hot-paths/references/ffn-evidence-audit-2026-09.md`.

## Measured Ladder

On one RTX PRO 6000 Blackwell Server Edition, a native block-scaled MMA microbenchmark reached about 1.136 PFLOP/s. Real fixed-shape FFN implementations were much lower because scale generation, packing, staging, epilogues, narrow dimensions, and synchronization were included.

An accepted CUTLASS TMA/ping-pong lineage reached about 660.03 dense-equivalent TFLOP/s at a measured concurrency point. Earlier custom fused FFN variants were around 180–238 TFLOP/s; producer/consumer overlap improved some variants into the 500–660 TFLOP/s range. These results proved available instruction throughput but did not prove 1 PFLOP/s end-to-end model inference.

## Retained Lessons

- Offline weight encoding is mandatory; hot weight recoding destroys the intended gain.
- ReLU was the checkpoint activation and had to remain ReLU.
- Global hidden materialization motivated sliced handoff, but its dominant
  causal cost was not established by counters. Later no-global-hidden paths
  remained far slower than the stock global-packed-hidden control.
- More groups, threads, slots, or cluster width could reduce occupancy or add instruction interference and regress throughput.
- 2:4 sparsity was unnecessary for the dense model objective.
- SM120 used a register-accumulating block-scaled MMA path with a warp-specialized TMA kernel lineage; SM100 TMEM assumptions were invalid.
- A full hidden/shared allocation exceeded the useful per-block shared-memory contract; bounded K-slice ping-pong was required.

## Synchronization And ABI Failures

- A cross-translation-unit mismatch between mutable and `const` kernel parameter declarations linked but corrupted TMA descriptors; monolithic compile exposed it.
- A stock collective could hang when placed inside an unsupported physical cluster topology. Compilation success was insufficient.
- DSM-to-local staging and broad cluster synchronization could be slower than the retained CUTLASS path.
- The August prepared-only checkpoint was later followed by numerical gates;
  consult the September audit for their exact two-/eight-slice scopes. Those
  gates did not establish production performance or model-quality acceptance.

## Acceptance Meaning

Intermediate state/score equality is a diagnostic. The ultimate project metric is replay-valid solutions with the same useful solution-length distribution as FP32/FP16 over cheap 10–100-state small-workload cohorts, followed by larger confirmation runs.
