---
name: optimize-transformer-hot-paths
description: Use when optimizing fixed-shape Transformer QKV, attention, FFN, residual, LayerNorm, final-token/CLS, persistent, TMA, shared-memory, or DSM inference paths.
---

# Optimize Transformer Hot Paths

Load `references/fixed-shape-transformer.md`. For the measured SM120 progression and negative branches also load `references/transformer-hot-path-experiment-ledger.md` and `../build-blockscaled-inference/references/rejected-paths-and-open-gates.md`.

## Work From The Graph

For the SM120 FF1/FF2 campaign, first read
`references/ffn-decision-gates-2026-09-05.md` for the current decision gates, then
`references/ffn-evidence-audit-2026-09.md`; it supersedes stale benchmark and
open-gate claims in the older ledgers. Keep both the fastest eligible baseline
and the experiment's immediate parent visible. A faster slow prototype is not
a replacement for a substantially faster incumbent.

Write the exact operator graph and tensor lifetimes first. Preserve the source activation; if the checkpoint uses ReLU, do not substitute SiLU.

## Priority Order

1. Fuse QKV projection and remove avoidable layout transforms.
2. Fuse attention score/softmax/value so temporary score/probability tensors do not round-trip through global memory.
3. Specialize final-token/CLS work only after proving the reduced query path matches the model's reduction semantics.
4. Fuse FF1 activation/quantization into FF2 consumption.
5. Fuse residual, LayerNorm, and next-layer emission while preserving unrounded residual semantics.
6. Use persistent/ping-pong scheduling to overlap producer slice N with consumer slice N-1.

Treat FlashAttention-style ideas as scheduling mechanisms: warp specialization, lifetime-scoped buffers, persistent work distribution, and overlapping data movement with math. Do not copy architecture-specific primitives blindly.

Minimize intermediate global-memory traffic. Prefer registers, shared memory, DSM, or cache-resident handoff only when the exact layout, lifetime, synchronization, and occupancy remain valid.

Benchmark every retained step on the real fixed shape; narrow layers and epilogues can dominate despite a fast large GEMM.
