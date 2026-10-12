# FF1/FF2 evidence audit, through 2026-09-03

Read this before reusing the older SM120 ledgers. These are dated case-study
observations, not portable performance constants. Later corrections below
supersede earlier claims, not the archived raw measurements themselves.

## Scope map: the numbers are not interchangeable

Cube4 case: seq57, D256, H1024, four layers, ReLU, output24. GPU was RTX PRO
6000 Blackwell Server Edition, 188 SM; September runs used driver595.71.05,
CUDA13.3.73, CUTLASS7107b055 plus local patches. Earlier runs had other drivers.

| Result | Actual scope | Interpretation |
|---|---|---|
| 221.04 TF/s, 1.50765ms | Full Stream1 B896 FA4-AOT control | Not FFN; no 1PF achievement |
| 660.03 TF/s | Historical CUTLASS two-GEMM FF1/ReLU/pack/FF2, M51072, two concurrent slots, global packed hidden, BF16 final output | Real FFN lineage; not zero-global-hidden or whole Transformer |
| 613.320 TF/s | Sept2 two-slot rebaseline of retained FFN binary | New-session control, not a new optimization |
| 614.816 TF/s | Sept3 same-session two-slot control median, five completed process pairs | Planned seven pairs interrupted; do not report seven |
| 590.733 TF/s | Complete standalone FF1 shared-payload writer, M51072 | Component; copied payload checked; uniform timing fixture |
| 573–574 TF/s | Same standalone FF1 family in later within-session comparisons | Do not interpret cross-session drift as regression |
| 709.615 TF/s | Observable checksum diagnostic instead of production payload | MMA retained, but output contract different |
| 719.447 TF/s | Early fixed-affine timing | Withdrawn as complete FF1: bias allocation OOB and missing callback/payload |
| 732.754 TF/s | Payload/conversion deliberately omitted, MMA retained | Ablation, not usable FF1 or pure store-cost estimate |
| about921 TF/s | Old discard/values-only executables | Invalid compute claim: target SASS has zero MMA |
| 21.399 TF/s | Serial two-CTA FFN including residual/LN/next-pack, M32768 | Correctness reference, far too slow |
| 120.899 TF/s | Four-CTA role-separated FF1/DSM/FF2 FP32, M32768 | No residual/LN, cannot use ratio to serial as matched speedup |
| 122.301 ->130.765 TF/s | Same-session four-CTA precompute A/B | +6.92% throughput, still far behind stock FFN |

The target is delivered work, not satisfying a number by changing the numerator.
FF1 useful work is 2*M*256*1024. FF1+FF2 is 4*M*256*1024. Two concurrent
slots count two completed batches and use aggregate latency. Do not divide
aggregate time by one batch or present throughput-normalized latency as request latency.
For M32768 FFN, 1PF requires34.359738368us; for M51072 it requires53.552873472us
per batch. Full Stream1 has a separate numerator371933184 FLOP/parent.

## The major process error: improving the wrong baseline

Zero-global-hidden fusion was treated as intrinsically superior. It was not:
role separation improved a very slow correctness scaffold without restoring
the fast scheduler. The repeated local wins distracted from the retained
stock component, which still delivered roughly615TF/s in the same session.

Keep two controls visible: the best eligible implementation for the target
boundary, and the immediate parent of an experiment. Report both. A local
6.9% gain is useful diagnosis, not project-level performance progress when
the candidate remains several times slower than the eligible incumbent.
Do not promote DSM because it satisfies a storage preference. Either preserve
the fast collective schedule while changing transport, or justify a rewrite
with a measured, bounded path back to incumbent latency.

M32768/FP32/one-launch and M51072/BF16/two-slot results are not exact A/B arms.
Their large gap justifies investigation; its exact causal factor requires
matched shape, output boundary and concurrency, not a ratio alone.

## Chronology of the retained and rejected paths

### Before the shared-only producer audit

- Exact FP16 depth8:124.367 ->111.024 ->84.2199 ->80.2952 seconds; compact57,
  final CLS and split final QKV were useful. These are completed depth8 times,
  not full solve or isolated Stream1 timings.
- FP8 static SNR/ranking studies did not establish task-level quality for the
  NVFP4 model. Offline weight encoding remained required; activation scales
  can be dynamic and their cost must remain in timing.
- Raw NVFP4 MMA1.136/1.210PF, calibrated-pack0.864PF and dynamic-pack0.557PF
  were synthetic ceilings. None certified full model throughput.
- Real hand-written fused FFN sustained182.8 ->187.12TF/s with A staging;
  larger per-warp groups lost occupancy. M16 persistent reached328TF/s, but
  larger M64/giant-CTA topologies regressed or failed launch resource limits.
- Stock CUTLASS global packed-hidden two-slot FFN reached660.03TF/s. More
  slots, larger M, and persisting-L2 policies did not improve that workload.
  Larger working-set slowdown is consistent with cache effects, not a counter-
  measured proof of L2 eviction or a proof that global handoff dominates.

### Sparse/coded expansion: useful work, not padded shape

Sept2 direct physical fragment packing improved a separate M16 persistent
path140.559 ->130.119us at M51072 (about412TF/s), seven exact A/B pairs.
It removed row-major scratch/repack, reduced registers78 ->66 and shared
bytes6784 ->4736. This is a retained alternate baseline, not the four-CTA
130TF/s result: similar numbers in microseconds and TF/s can mislead.
Eight producer warps lost residency (411.59 ->319.06TF/s); two consumers
instead of four raised register pressure and more than doubled latency.
Hoisting A/SFA loads reduced registers but slowed157.491 ->165.461us.
Reduced resources alone therefore did not select a winner.

Pair/width4/width8 experiments reached physical dense-equivalent615/1126/1339
TF/s, but useful FF1 was308/281/167TF/s. Encoding and unused/mixed products
cannot be credited as original work. Exact N-packed orientation measured334
TF/s versus296 for coded K512; these are particular sparse/control contracts,
not validation of arbitrary dense-model sparsification.

Sparse metadata selects contraction positions, not separate C destinations.
A Latin-square placement cannot split u+v already summed in an accumulator.
Independent tasks belong in free M/N coordinates or separate accumulators;
a scheduler macro-panel K_work is not enlarged physical reduction K.
Do not revive coded K2048 merely because physical TF/s exceeds1PF.

### Aug31 numerical audit (two-slice scope)

- Incorrect FF1 consumer count:128 actual MMA threads versus256 assumed.
- Byte-addressed swizzle used with nibble coordinates:75% FF2 mismatch.
- FP4 helper used ordinary byte-stepped pointer instead of subbyte iterator.
- Independent writer/reader RED-to-GREEN plus400 two-slice O3 launches passed.
- Arena reuse requires producer load_tail and consumer mma_tail completion.
- Sanitizer13.3/13.0 reported Device not supported. This is missing coverage,
  not proof of race freedom. Later eight-slice tests were separate evidence.

### Sept2–3 standalone FF1 audit

| Experiment | Within-session result | Decision / caveat |
|---|---|---|
| Native SFA partition | 466.9 ->576.1TF/s | Scale ownership improvement; later payload liveness audit limits old full-FF1 interpretation |
| Producer56/consumer224 regs | 576.1 ->563.2 | Reject; moving regs to producer hurt |
| Producer24/consumer240 regs | 576.2 ->586.4 | Positive limited component; same aggregate register budget |
| Fixed affine early719 | Missing forwarded register_d_ready hook; bias[N] with row stride reads bias[M] | Invalid complete-output benchmark |
| Explicit volatile byte writer | 590.733 | Retains genuine packed payload; copied values and hashes checked |
| Batched compiler clobber | 590.566 ->589.810 | No gain; separate candidate readback not run |
| Quartet word writer | 590.147 ->204.650 | Correct payload, severe instruction expansion |
| syncwarp isolation | byte574.079, byte+sync575.972, quartet197.726 | sync alone does not explain collapse |
| XOR gather | 573.814 ->470.426 | Better than rejected gather, still reject |
| Paired words | 573.821 ->567.237 | Fewer stores/spills did not win |
| Omit payload | 574.033 ->732.754 | Diagnostic only; removes conversion and stores plus changes scheduling |
| Direct FP32 pack + real byte stores | 573.713 ->564.351 | Exact copied payload, slower; reject |

The exact timed binary must retain the computation and production output.
Readback instrumentation can make dead stores live, so passing an instrumented
build does not certify the uninstrumented binary. Inspect the target kernel's
SASS, not unrelated kernels. Zero STG does not prove zero DRAM: reads and local
memory remain. Scale-only checks do not validate payload; a varied fixture
that quantizes to one scale byte is not a meaningful scale-diversity test.

### Native FF1 into FF2

- Native scale normalization was norm=1 for the chosen oracle, not stale6:
  callback already applied norm/6. This is a specific API contract, not a
  universal scale constant.
- Raw FF1 matched but7/8 scale coverage was missing. Passing subtile_idx=0
  to the epilogue stored only one subtile; -1 meant all in this instantiated API.
- Source-versus-destination partition was tested and did not explain failure.
- Serial full path passed seeds1/7/42 then measured1605.67us. Keeping FF2
  totals live across FF1 caused severe compiler spill/resource pressure;
  the dynamic time contribution was not separately profiled.
- Four-CTA roles isolated producers and consumers and passed full M128/M512
  gates. M32768 timing checked128 rows only; runtime success is not full-size
  all-output verification or sanitizer coverage.
- Early FF1 computes into producer-owned arena before destination armed wait.
  Prior source-free acknowledgement still protects reuse; destination armed
  is still awaited before DSM writes. Seven alternating pairs:280.945 ->
  262.759us, exact full small gates and sampled timed checks. No promotion.

The next bottleneck hypothesis is repeated creation/drain/invalidation of a
two-K-tile FF1 pipeline four times per producer, plus cluster/resource costs.
This is source evidence and a hypothesis, not measured stall attribution.
First isolate it or preserve the fast stock mainloop across slices. Do not
remove required barriers to chase an assumed synchronization cost.

## Evidence pointers

Project artifacts live under `test_results/` in the existing Stream1 worktree.
Keep this reference usable without that checkout; pointers provide provenance,
not required runtime dependencies. Main records reviewed for this audit:

- `molab_sm120_nvfp4_fused_ffn_2026-08-27.md` (read later corrections before reuse)
- `sm120_fused_correctness_audit_2026-08-31.md`
- `sm120_stream1_1pf_implementation_2026-09-02.md`
- `molab_sm120_pair_packed_ff1_2026-09-02.md`
- `ff1_sass_comparison_2026-09-02/REPORT.md`
- `ff1_native_partition_review_2026-09-02.md`
- `ff1_{spills_register_budget,regs24_240,fixed_affine,checksum_control}_2026-09-02.md`
- `ff1_{explicit_shared_store,quad_store,sync_isolation,xor_gather,pair_store,payload_ablation,direct_pack}_2026-09-03.md`
- `ff1_native_ff2_{integration,roles}_2026-09-03.md`
- `ffn_precompute_results_2026-09-03.md` and downloaded `ffn_precompute_ab_2026-09-03.json`
- `sm120_cutlass_nvfp4_ffn_rebaseline_2026-09-02.json`

Open: arbitrary model bias, complete-model low-precision quality, matched
full FFN promotion, sanitizer coverage and1PF full Stream1. Do not turn
synthetic exactness, a proposed persistent schema or a compiled binary into
completion of those gates.
