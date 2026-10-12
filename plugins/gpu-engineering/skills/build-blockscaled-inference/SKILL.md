---
name: build-blockscaled-inference
description: Use when designing offline encoded FP8, MXFP8, MXFP4, or NVFP4 weights/scales and target-specific Blackwell block-scaled neural-inference kernels.
---

# Build Blockscaled Inference

Load `references/sm120-blockscaled-inference.md` and, for the historical fixed-shape case, `references/sm120-case-study.md`. For the complete measured campaign also load `references/sm120-low-precision-experiment-ledger.md` and `references/rejected-paths-and-open-gates.md`.

## Precision Ladder

1. Preserve an FP32 oracle.
2. Establish an accepted FP16 baseline.
3. Build candidate low-precision artifacts offline.
4. Run cheap numerical rejection gates.
5. Benchmark accepted candidates on target hardware.
6. Promote only after task-level quality checks.

NVFP4 is a 4-bit value format paired with scale factors, not "better FP8". MXFP4 and NVFP4 have different scale contracts. Do not add 2:4 sparsity to dense weights merely to quote sparse peak.

## Artifact Contract

Store immutable packed values, scale tensors in the exact hardware/library swizzle, shapes, strides, activation, accumulation/output precision, calibration fingerprint, model fingerprint, toolkit/library version, and artifact hash. The runtime loader validates all fields and fails closed.

Immutable weights are offline encoded. Dynamic activations may require runtime scales; fuse that cost into the producer/consumer stage and avoid a global intermediate.

Never enable a partial pointer/artifact set, silently reinterpret one format as another, or fall through to a low-precision launcher without exact feature and layout gates.
