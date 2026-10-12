# SM120 Low-Precision Experiment Ledger

This is a fixed-shape Cube4 output-24 case study. Use it to avoid repeating rejected approaches and to distinguish hardware ceiling from model acceptance.

## Quality contract

- FP32 checkpoint is the oracle.
- Current FP16 is the accepted baseline.
- Low-precision weights and scale tensors are offline encoded in the exact physical layout.
- Runtime may dynamically encode activations, but never weights.
- ReLU is part of the model contract.
- Numerical and ranking metrics are rejection filters.
- Final acceptance is replay-valid solve success and solution length distribution on 10–100 states, followed by a large-beam performance gate.

The accepted performance baseline for the exact Cube4 beam workload was `80.2952 s` at `depth_done=8`.

## Static weight study

| Encoding | Aggregate SNR | Result |
|---|---:|---|
| E4M3 tensor scale | 31.568 dB | candidate foundation |
| MXFP8 E4M3 + E8M0/32 | 31.568 dB | block scaling did not improve static weights alone |
| ideal arbitrary block scales | 32.491 dB | non-native upper bound |
| E5M2 | 25.600 dB | reject |

Sparse top-error values, fixed K-column rescue and rank-16 FP16 residual correction had weak return. Activation distribution, not static weight range, became the main question.

## Real-frontier quality

On 20,480 real states:

| Candidate | Top-1 vs FP32 | Top-8 vs FP32 | Decision |
|---|---:|---:|---|
| FP16 | 0.995605 | 0.992273 | control |
| one-term block FP8 | about 0.954 | about 0.958 | reject |
| three-term decomposition | 0.995166 | 0.992029 | quality close, slower than exact FP16 |
| four-term decomposition | 0.995166 | 0.992334 | no useful gain over three-term |
| MXFP8 | 0.959570 | 0.965190 | reject |
| SmoothQuant alpha 0.5 | 0.968750 | 0.968840 | reject |

A tiny output affine correction did not recover the model: accumulated error is state-dependent inside the Transformer.

## MXFP8 hardware path

Native SM120 MXFP8 MMA was verified. GEMM-only measurements reached roughly 270–548 TFLOP/s depending on shape. When dynamic activation encoding was included, end-to-end operator throughput fell to about 86–218 TFLOP/s, especially for K=1024. This proves that the format/instruction works and that hot activation encoding can dominate.

## NVFP4 ceilings and controls

NVFP4 uses E2M1 values with UE4M3 scale factors. It is a 4-bit path, not an FP8 alias.

| Control | Throughput | Meaning |
|---|---:|---|
| 8192-cube 2:4 sparse NVFP4 | 1.936–**1.937 PFLOP/s** dense-equivalent | hardware roofline only |
| dense square NVFP4 | about 1.431 PFLOP/s | dense native ceiling |
| raw block-scaled MMA | **1.136 PFLOP/s** | isolated instruction control |
| warp-specialized MMA-only | 1.210 PFLOP/s | scheduling control |
| calibrated-scale ReLU + pack | 0.864 PFLOP/s | conversion cost visible |
| exact dynamic amax + pack | 0.557 PFLOP/s | full scale-generation cost |

2:4 sparsity was rejected for the dense production model. It is not required to issue dense native NVFP4 instructions and must not be introduced merely to quote sparse peak.

## Real FFN progression

| Path | Best measured effective throughput | Status |
|---|---:|---|
| global two-kernel transport | about 520 TFLOP/s | component baseline |
| PDL | 516 TFLOP/s at M32768 | positive launch/prologue change |
| two-slot CUTLASS ping-pong, M51072 | **660.03 TFLOP/s** | retained real FFN lineage |
| four/eight slots | 581/524 TFLOP/s | contention, reject |
| larger M65536 x2 | 634 TFLOP/s | below real M51072 optimum |
| persistent M16 numerical oracle | 328 TFLOP/s | ownership proof, not selection |

The 660.03 result is not end-to-end Stream1. Attention, normalization, projection, output and beam integration remain outside its numerator.

## Promotion rule

Require the same immutable candidate to pass:

1. exact pack/unpack and artifact hashes;
2. real-frontier candidate-vs-FP16 ranking gate plus FP32 regression budget;
3. reconstructed frontier gate;
4. native full Stream1 benchmark;
5. contemporaneous FP16 depth-8 comparison;
6. replay-valid same-length solve cohort;
7. no silent fallback to FP16 for a claimed low-precision operator.
