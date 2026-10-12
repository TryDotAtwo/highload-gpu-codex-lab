# Rejected Paths And Open Gates

This is the August checkpoint. The September audit at
`ffn-evidence-audit-2026-09.md`
supersedes its prepared-only statuses and records new numerical/performance
results. Kernel numerical gates1–3 below have partial and eight-slice evidence;
production/model acceptance remains open. Do not rerun obsolete failed paths
merely because this historical list still calls them next steps.

## Rejected low-precision quality paths

- E5M2 forward weights: materially worse SNR than E4M3.
- naïve one-term MXFP8/NVFP4: large real-frontier ranking loss.
- SmoothQuant alpha 0.5: insufficient recovery in the measured model.
- dense three-/four-term E4M3 decomposition: quality close to FP16 but more arithmetic and slower than exact FP16.
- small output-head correction: internal state-dependent error remained.
- sparse/outlier/low-rank corrections: weak static return; not a default without a new task-level win.
- 2:4 sparse production weights: rejected because the model is dense.

## Rejected topology/performance paths

- more than two physical FFN slots: contention/regression;
- larger M alone: throughput fell; cache escape is a hypothesis, not measured
  traffic attribution;
- persisting L2 window: no useful gain and large-window regression;
- giant N1024 CTA and cluster multicast: unsupported on the selected SM120 builder;
- SM100 TMEM/UMMA route: architecture mismatch;
- generic M64/N256/larger-CTA assumptions: several exact implementations were resource-limited or slower;
- one-consumer-warpgroup DSM oracle: transport proof only, much slower than stock persistent CUTLASS;
- manual nibble read-modify-write hidden writer: correct but too slow;
- `dlmopen` for isolating a second CUDA library: second runtime initialization hung.

## Important root causes

### Split-TU ABI mismatch

One shared-only kernel fault was not caused by TMA or DSM. Kernel definition used mutable by-value `Params`; host declaration used `GRID_CONSTANT Params const`. The **mutable** versus **const** mismatch corrupted the launch ABI. A monolithic compile exposed it.

### Unsupported physical cluster assumption

Running a stock logical 1x1 SM120 block-scaled wrapper inside a physical 2-CTA cluster hung before FF2. CUTLASS also rejected runtime cluster/multicast with `no programmatic multicast on this arch`. A logical-singleton adaptation was compiled but remains prepared but not runtime-verified.

### Arithmetic-boundary mismatch

LayerNorm must consume the unrounded FP32 residual sum while persistent tokens may store an FP16 copy. An epilogue that rounds first is incorrect even if the difference appears small.

## Open gates

1. Run the corrected physical-cluster/logical-singleton FF1 binary in a fresh target session.
2. Run the complete FF1 native-register-D -> DSM -> FF2 fused numerical kernel.
3. Prove no global hidden writes and exact scale/value layout.
4. Beat the retained 660.03-TFLOP/s component on identical shape and repeats.
5. Integrate all four Transformer layers and measure exact depth-8 against 80.2952 s.
6. Evaluate FP32, FP16 and candidate on real frontier states.
7. Run 10–100 small-beam replay-valid solves and compare same-length solution outcomes.
8. Only then enable an immutable low-precision profile; until then the selector must fail closed.

Compile success, policy tests, an isolated checksum and a prepared binary are not substitutes for these gates.
