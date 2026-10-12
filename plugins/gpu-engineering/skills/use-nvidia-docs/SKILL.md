---
name: use-nvidia-docs
description: Use when checking NVIDIA docs.
---

# Use NVIDIA Docs

Use official current docs before hardware-specific CUDA or NVIDIA-library advice.

## Lookup Workflow

1. Identify GPU model, driver, CUDA Toolkit, platform, and container image.
2. Map GPU model to compute capability with the official compute capability table.
3. Match arch flags and docs to installed or target toolkit version.
4. Check CUDA guide, architecture tuning guide, and library guide before specific claims.

## Source Map

Load `references/nvidia-docs-map.md` only when exact source links are needed.

## Avoid

- Guessing compute capability from architecture name without checking the table.
- Using old CUDA docs when the installed CUDA Toolkit is newer.
- Treating blog posts, forum answers, or model cards as stronger than official API docs.
- Recommending CUTLASS, CUB, NCCL, or profiler details from memory when signatures may differ.
