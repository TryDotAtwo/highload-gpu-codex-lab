---
name: profile-remote-gpu-runs
description: Use when profiling or monitoring remote GPU runs on Kaggle, Molab, H100, T4, RTX PRO Blackwell, or notebook sandboxes.
---

# Profile Remote GPU Runs

Remote profiling must preserve the run, collect artifacts, and respect platform limits.

## Routing

Use `work-with-kaggle` for Kaggle CLI push/status/downloads and `work-with-molab` for Molab browser/marimo operation when available. Use HighloadGpu for architecture/profiling decisions.

## Rules

- Do not leak tokenized session URLs.
- Do not interrupt production/no-timeout runs unless asked.
- Probe `nvidia-smi`, RAM, disk, CUDA Toolkit, compiler, and package versions.
- If Nsight is unavailable, use internal timers, NVTX where possible, and structured JSONL logs.
- Keep transient build/checkouts in temp; save final logs/CSVs/PNGs to output and project `test_results/`.
- Verify arch flags from docs/environment: T4 usually `sm_75`, H100 `sm_90`, RTX PRO 6000 Blackwell Server Edition `sm_120`.
