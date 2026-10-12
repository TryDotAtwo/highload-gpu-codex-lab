# Inference Benchmark Contract

## Required Metadata

`model_sha, export_sha, binary_sha, gpu, cc, driver, runtime, toolkit, library_commit, arch_flags, batch, slots, streams, input_shape, output_dim, precision, warmup, repeats, median_ms, p95_ms, items_s, memory_bytes, status`.

## Levels

1. single operator;
2. fused block;
3. one model forward;
4. repeated in-process model forwards;
5. caller-integrated stage;
6. end-to-end application.

At each level include data preparation and conversion only if production includes it. Report excluded work explicitly.

## Transformer Versus MLP

MLP inference often supports a much larger model microbatch because it has no sequence-wide attention activation/workspace. Transformer activation and attention workspace can make a batch safe for an MLP fail immediately. Never copy batch/concurrency profiles across model families.

Keep at least two execution buffers only when the caller can fill one while another is consumed. More slots require timeline evidence; each may duplicate activations, descriptors, graphs, or workspace.

## Correctness Before Speed

- deterministic input corpus and FP32 oracle;
- FP16 baseline;
- output finite/range checks;
- rank/top-k diagnostics appropriate to the caller;
- exact artifact fingerprints.

A backend that changes activation, preprocessing, class ordering, or head interpretation is a different model, not an optimization.
