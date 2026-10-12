---
name: profile-remote-gpu-runs
description: Use when collecting reproducible GPU performance evidence on remote hardware without taking ownership of a platform-specific notebook or job lifecycle.
---

# Profile Remote GPU Runs

## Routing

Use the platform plugin for login, session lifecycle, uploads, execution, persistence, and downloads. Use HighloadGpu only for architecture and profiling decisions.

## Rules

- Do not interrupt production/no-timeout runs unless asked.
- Probe `nvidia-smi`, RAM, disk, CUDA Toolkit, compiler, and packages.
- Record exact GPU product, compute capability, driver, runtime, toolkit, library commits, build flags, binary hash, clocks/power state when visible, and workload fingerprint.
- If Nsight is unavailable, use internal timers, NVTX where possible, and structured JSONL logs.
- Keep transient build/checkouts in temp; save final logs/CSVs/PNGs to output and project `test_results/`.
- Verify arch flags from docs/environment.

## Integration evidence

Tie each result to the executed source revision, selected backend and actual runtime call path. Configuration parsing, FFI declarations and initialization alone do not prove a backend executes the workload. Verify dispatch and report incomplete wiring explicitly.

Distinguish primitive correctness, full-workload correctness, sanitizer coverage and repeated end-to-end performance. Capture eligibility alone does not establish overlap: use a real workload timeline to inspect host readbacks, waits, launch gaps and collective stalls. Do not infer a CPU-free pipeline from removal of an individual wait or count upload.

Use concurrently available remote jobs for independent checks when authorized; do not duplicate active runs. For repeated timeouts, change the diagnostic hypothesis or add phase evidence before rerunning; keep unaffected validation moving.
