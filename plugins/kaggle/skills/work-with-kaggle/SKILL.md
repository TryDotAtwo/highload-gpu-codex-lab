---
name: work-with-kaggle
description: Use when the user asks Codex to work with Kaggle, kaggle.com, Kaggle notebooks/kernels/datasets, Kaggle CLI, 2xT4/H100 notebook validation, kernel push/status/output/downloads, or Kaggle run diagnostics. This includes requests like "запусти на кагле", "проверь Kaggle logs", "push kernel", "download Kaggle output", "сделай T4x2 notebook", "опубликуй notebook", or "watch Kaggle status".
---

# Work With Kaggle

Use this skill whenever the task involves Kaggle notebooks, kernels, datasets, or GPU validation runs.

## Project Memory First

For project repositories, read local project guidance before changing notebooks or source:

- `AGENTS.md`
- `memory/PROMPTS.md` and `memory/CHANGELOG.md`, especially recent Kaggle entries
- relevant `test_results/kaggle_*` reports for the same failure/config family

This project has many Kaggle-specific decisions preserved in memory. Do not assume a generic Kaggle workflow is correct when project memory says otherwise.

## Safety And Scope

- Do not upload or publish current uncommitted source to a Kaggle dataset unless the user explicitly approves external export.
- Prefer GitHub-backed Kaggle source when the user has selected GitHub as source of truth.
- Do not push a public Kaggle notebook/kernel unless the user explicitly approves publication or public push.
- Do not make C++/CUDA algorithmic changes while diagnosing Kaggle failures unless the user explicitly approves code changes. Config-only notebook changes are acceptable when useful and consistent with the request.
- Do not revert unrelated local changes. Kaggle notebook edits often coexist with dirty source changes.
- For multi-rank validation, do not fake `WORLD_SIZE=2` on one GPU with both ranks on `LOCAL_RANK=0` unless the user explicitly approves that limited smoke. Real multi-rank validation should use real multi-GPU hardware such as Kaggle 2xT4.

## Kaggle CLI Workflow

Prefer Kaggle CLI for authenticated Kaggle work:

- Check metadata before pushing: `kaggle/kernel-metadata.json` or the selected push package metadata.
- Validate notebooks locally before push: JSON parse and Python AST parse for code cells.
- Push with the intended package directory, then monitor with `kaggle kernels status <owner/slug>`.
- Download outputs/logs after completion or failure and store them under `test_results/`.
- If CLI network/proxy behavior is project-specific, inspect existing scripts/config and preserve local proxy-bypass behavior instead of switching tools silently.

When reporting command output to the user, summarize the important status/version/error lines. The user does not see raw command output.

## Notebook Preparation Rules

For solver notebooks in this project:

- Keep a first config cell with the main run parameters such as beam, depth, puzzle range, model weights URL/path, history mode, and torchrun topology.
- Keep build/checkouts and large transient trees under `/tmp` where possible. Use `/kaggle/working` for logs, CSVs, summaries, and final artifacts.
- Add a preflight cell for large runs: compute local/global beam, world size, shard capacity, Stream1/3/4 guards, static history RAM/disk budgets, and free disk under `/tmp` before clone/build/run.
- Clean stale `/tmp/beam_history_*` and configured history disk paths before runs and between puzzles when static-hybrid history is used.
- For long multi-rank runs, stream selected rank logs live while writing full rank logs to disk.
- Final cells should summarize results and produce user-useful CSV/PNG artifacts, for example solved counts and solution-length histograms.

## Torchrun And Multi-GPU Rules

- Torchrun notebooks should launch the existing binary/processes through explicit topology settings, not implicit GPU auto-detection.
- Expose `TORCHRUN_NPROC_PER_NODE`, `TORCHRUN_NNODES`, `TORCHRUN_NODE_RANK`, and rendezvous endpoint/port in config.
- Derive `WORLD_SIZE` from torchrun topology settings, not from `torch.cuda.device_count()` alone.
- For C++ multi-rank runs, torchrun or Python launchers should only start processes. C++ reads `RANK`, `LOCAL_RANK`, and `WORLD_SIZE`, calls `cudaSetDevice(LOCAL_RANK)`, and creates NCCL communicators itself.
- H100 and T4 notebooks may differ by CUDA architecture/build directory and hardware-specific config, but should otherwise stay comparable when the user asks for paired notebooks.

## Monitoring And Stop Rules

- For diagnostic Kaggle runs, if the user has asked Codex to watch logs and no new logs appear for about 120 seconds, stop the run and inspect downloaded logs. This rule came from project memory and applies to diagnostic/watch tasks.
- Do not stop production/no-timeout runs unless the user explicitly asks or the notebook itself has a configured timeout.
- If a run appears hung because stdout is redirected, check rank log files and whether live-rank streaming is enabled before assuming a stall.
- Preserve logs even when stopping: terminate gracefully when possible, then download output files.

## Failure Diagnosis Checklist

After a Kaggle failure, collect and scan:

- Kaggle worker status and kernel version
- notebook stdout tail
- rank logs under the notebook output directory
- result JSONL/CSV summaries
- GPU budget/preflight output
- explicit Kaggle messages such as disk quota failures

Common patterns in this project:

- `KernelWorkerStatus.ERROR` plus "more disk space than is available" usually means disk quota/static history arena pressure.
- `return_code=-9` can indicate host RAM OOM.
- `code=3002` / `STREAM_FATAL_STREAM3_DOUBLE_BUFFER_OVERFLOW` points to Stream3/Stream4/threshold/capacity flow diagnostics.
- `final selected count does not match score phase counts` points to final selection/histogram/exact-count mismatch.
- `cudaGraphInstantiate: out of memory` may require config-only headroom/shard-capacity changes before deeper code work.
- Silent output after build may simply mean rank stdout is redirected and live rank logging is disabled.

Write a short report under `test_results/` for meaningful Kaggle validations, sweeps, failures, or launches.

## Response Style

- Be explicit about whether you changed source code, notebook config only, or only launched/monitored a run.
- Include Kaggle kernel slug/version/status when known.
- Include exact local report/log paths in `test_results/`.
- Keep recommendations tied to evidence from logs, not guesses.
- If the next step requires exporting source or publishing publicly, ask for explicit approval first.