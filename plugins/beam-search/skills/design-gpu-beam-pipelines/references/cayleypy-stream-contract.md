# CayleyPy / MultiGPUBeamSearch Stream Contract

Use this reference only for the CayleyPy-style pipeline.

## Current Invariants

- `State128` logical bytes are `v[0..119]`; padding is `v[120..127]`.
- Persistent frontier padding is zero.
- `FinalResponse` may temporarily store `target_local_idx` in `v[120..123]`.
- `Hash128` is one logical 128-bit key `{lo, hi}`.
- `CandidateMeta` remains 32 bytes and 32-byte aligned.
- Stream 3 payload ID is the original candidate ID, not the compact index.
- Stream 4 uses threshold + compact + fixed-temp CUB sort/reduce + compact.
- Stream 4 does not use hash-table dedup, shard top-k, or a semantic shard cap.

## Stream Boundaries

- Stream 1 expands/scores candidates and may fill one outer slot through many model microbatches.
- Stream 3 consumes logical accumulators in bulk; its job count is a tuning signal, not a semantic target.
- Stream 4 performs global threshold/unique/selection work without weakening the global beam.
- Final materialization and Stream 5 exchange use separately bounded buffers.

Architecture changes require explicit approval when the project owner reserves the beam-search algorithm boundary.
