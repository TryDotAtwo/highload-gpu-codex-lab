# GPU Jobs And Artifacts In Molab

## Preflight

Capture GPU name, compute capability, driver, CUDA runtime/toolkit, compiler, library commits, CPU/RAM, disk, and current GPU/process state. Keep exactly one heavy job active.

For expensive builds, a local container may compile the artifact only when its toolkit, architecture flags, ABI, dependencies, and linker/runtime contract match the target. Record the local build environment and artifact hash. Upload the ready binary/source bundle, then execute and profile on Molab; local compilation is never target-runtime validation.

## Stage-Gated Foreground Run

Use one foreground cell/SSE request with bounded stages:

1. environment and artifact verification;
2. compile/link smoke if needed;
3. minimal correctness gate;
4. short benchmark;
5. sustained benchmark;
6. artifact export.

Do not deliberately run a known-hanging or unsupported control before the safe candidate. Isolate new barriers, clusters, or custom kernels in the smallest useful gate. Print stage, elapsed time, last-log timestamp, PID when applicable, GPU memory, and output paths.

A foreground `subprocess.Popen` is acceptable when the cell reads its output, writes a complete log, waits for termination, and remains attached. Detached execution is not.

## Persistence Policy

Molab announced on August 26, 2026 that new notebooks retain files uploaded or created through the marimo file browser, rather than every sandbox file. Use:

- file-browser-managed files for notebook persistence;
- `mo.persistent_cache` for bounded expensive downloads, acknowledging TTL/size limits;
- supported remote storage for large datasets/checkpoints;
- external versioned storage for irreplaceable results.

Source: [Seamless storage in Molab](https://molab.marimo.io/blog/seamless-storage-in-molab).

Temporary build products may live under `/tmp`, but final reports, logs, binaries, plots, and checkpoints need an explicit persistence/export step. For every retained artifact record path, size, artifact hash, producing config, and validation status.

## Evidence

Process exit zero is not enough. Verify expected files, parse the final result marker, inspect the last stage, and confirm that logs/checkpoints advanced. For images/plots prefer source data plus a deterministic export. Never expose secrets from logs or notebook DOM.
