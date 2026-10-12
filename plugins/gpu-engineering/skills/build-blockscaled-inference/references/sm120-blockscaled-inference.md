# SM120 Block-Scaled Neural Inference

Use HighloadGpu's SM120 reference for general hardware limits. This reference covers model-specific execution.

## Encoding

- Keep the source checkpoint or FP32 materialization as the immutable oracle.
- Calibrate on real model inputs, including states near downstream decision thresholds; random inputs alone are insufficient.
- Search scale/rounding candidates per supported block, then encode values and scale factors directly into the runtime's physical layout.
- Hash the source, corpus, calibration policy, values, scales, and manifest.

Blackwell block-scaled MMA consumes quantized values and separate scale tensors. Scale vector length, scale type, alignment, and swizzle are part of correctness.

## Autotuning Funnel

1. tensor statistics and outlier audit;
2. layer/operator sensitivity sweep;
3. cosine, relative error, top-k/rank, and threshold-neighborhood diagnostics;
4. partial low-precision candidates before whole-model conversion;
5. target-hardware throughput;
6. task-level solve/decision quality.

Use activation-aware or Hessian-aware rounding only if simpler calibrated scaling misses quality. Preserve a manifest that states which operators remain FP16.

## Hot Path

- Prepacked weights/scales are loaded once.
- Dynamic activation quantization happens adjacent to its producer.
- Avoid writing a full low-precision hidden tensor to VRAM only to read it immediately.
- Keep CUTLASS TMA/shared staging and its tested persistent scheduler unless a replacement wins end to end.
- Use DSM/mbarrier only with exact layout and lifetime ownership; compare against local shared and L2/global controls.

SM120 RTX does not inherit SM100 TMEM/UMMA capabilities. Select an actual SM120 MMA/CUTLASS path and compile for the required architecture-conditional feature set.
