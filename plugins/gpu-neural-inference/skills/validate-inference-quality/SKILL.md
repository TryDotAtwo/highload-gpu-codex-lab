---
name: validate-inference-quality
description: Use when comparing FP32, FP16, FP8, NVFP4, MXFP4, or fused inference paths for numerical accuracy, ranking stability, model decisions, or application-level quality.
---

# Validate Inference Quality

## Reference Ladder

- original FP32 weights/execution as oracle where available;
- accepted FP16 implementation as production baseline;
- candidate fused or low-precision implementation.

Use exact model inputs, preprocessing, activation, mask, residual, normalization, and head semantics.

## Cheap Diagnostics

Per operator and whole model record finite/range failures, absolute/relative error, cosine similarity, top-k overlap, rank correlation, class/move agreement, margin changes, and errors near downstream thresholds. Use these to reject bad candidates and localize sensitive layers.

Do not require bitwise state identity across precisions when the application accepts ranking variation. Conversely, good cosine similarity does not prove useful task quality.

## Task-Level Quality

Define the metric the model serves: solve/decision success, replay validity, solution length, score, or another domain outcome. Run paired inputs and seeds:

1. 10–100 cases at cheap settings to build quality-versus-cost curves;
2. larger settings for candidates on the Pareto frontier;
3. report failures and distribution shifts, not only averages.

Promote only when the candidate materially improves the measured critical path and stays within the user-approved task-level quality boundary.
