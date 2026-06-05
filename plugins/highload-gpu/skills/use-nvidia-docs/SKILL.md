---
name: use-nvidia-docs
description: Use when checking NVIDIA docs.
---

# Use NVIDIA Docs

Use official, current documentation before giving hardware-specific CUDA or NVIDIA-library advice. GPU capabilities, architecture targets, profiler behavior, and library APIs change over time.

## Lookup Workflow

1. Identify the GPU model, driver, CUDA Toolkit, and target platform from `nvidia-smi`, build logs, container image, or user-provided environment.
2. Map GPU model to compute capability with the official compute capability table.
3. Choose arch flags from evidence: for example `sm_75` for Turing T4, `sm_90` for H100, and `sm_120` for RTX PRO 6000 Blackwell Server Edition.
4. Check the CUDA guide for programming-model behavior, the tuning guide for architecture-specific risks, and the library guide for API details.
5. Cite exact docs used when the answer relies on current hardware/library facts.

## Source Map

Load `references/nvidia-docs-map.md` only when exact source links are needed.

## Common Mistakes

- Guessing compute capability from architecture name without checking the table.
- Using old CUDA docs when the installed CUDA Toolkit is newer.
- Treating blog posts, forum answers, or model cards as stronger than official API docs.
- Recommending CUTLASS, CUB, or NCCL API shapes from memory when current signatures may differ.
- Assuming PyTorch CUDA behavior proves native C++/CUDA behavior.
