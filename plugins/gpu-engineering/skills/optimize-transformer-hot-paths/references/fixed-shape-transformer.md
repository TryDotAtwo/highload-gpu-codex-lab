# Fixed-Shape Transformer Lessons

## Representative Scorer Shape

A verified Cube4/Piece Transformer case used sequence length 57, model width 256, 4 layers, 8 heads, head dimension 32, FF width 1024, and output dimension 24. Another audited path used sequence length 51 with the same width/head/FF sizes. Treat shape as an artifact field, never a global assumption.

## Attention

Decomposed QK, softmax, and PV kernels can lose to launch and global-memory overhead even if each GEMM is fast. A fused strided-QKV/FMHA path can win on one GPU while a scalar `Q=1` warp reduction changes ordering on another. Require exact score-dump or bounded numerical checks before performance promotion.

Final-CLS-only paths are valid only when earlier tokens are no longer needed by the model graph. Preserve LayerNorm, residual, attention mask, positional/piece encoding, and head ordering.

## FFN Handoff

For `256 -> 1024 -> 256`, materializing the full hidden tensor in global memory can dominate a low-precision MMA path. A production design can slice hidden K, then:

- FF1 produces one slice;
- applies the checkpoint activation;
- encodes dynamic activation values/scales;
- publishes a bounded shared/DSM slot;
- FF2 consumes that slot while FF1 prepares the next.

Weights and their scales stay offline encoded. Dynamic activation encoding is included in stage timing.

## Synchronization

Use ownership and generation/phase-tagged barriers. Avoid broad synchronization when a one-way producer/consumer handoff suffices. A timeout does not make a barrier bug safe; isolate new cluster/mbarrier protocols behind small correctness gates.

## Residual And Next Layer

The residual stream may require a higher-precision persistent value even when MMA operands are low precision. LayerNorm must consume the graph-specified value, not an accidentally rounded storage boundary. Generate the next layer's quantized input only after the correct residual/normalization semantics.
