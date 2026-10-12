---
name: gpu-neural-inference
description: Use when optimizing, benchmarking, quantizing, exporting, or validating MLP or Transformer inference on NVIDIA GPUs, including fixed-shape scorer models and Blackwell low-precision paths.
---

# GpuNeuralInference

Router for model execution. Use HighloadGpu for generic CUDA/profiling and GpuBeamSearch for frontier/search pipeline semantics.

## Route

- Model microbatch, execution slots, CUDA streams, and isolated throughput: `benchmark-gpu-inference`
- QKV/attention/FFN/residual/LayerNorm fusion and persistent scheduling: `optimize-transformer-hot-paths`
- FP32/FP16/NVFP4/MXFP4 artifacts and SM120 kernels: `build-blockscaled-inference`
- Numerical diagnostics and task-level quality: `validate-inference-quality`

## Invariants

- Preserve model architecture, source activation, head semantics, preprocessing, and output ordering.
- Quantized weights are offline encoded; do not quantize immutable weights in the hot path.
- A fast isolated GEMM is evidence, not end-to-end inference proof.
- Promote only target-hardware paths that pass both numerical and task-level quality gates.
