---
name: write-dockerfiles
description: Use when creating or editing Dockerfiles, BuildKit builds, multi-stage images, cache, .dockerignore, or CUDA build images.
---

# Write Dockerfiles

Use official Dockerfile reference: https://docs.docker.com/reference/dockerfile/

## Rules

- Start with `# syntax=docker/dockerfile:1` unless the repo already standardizes otherwise.
- Use `.dockerignore`; do not send huge build contexts accidentally.
- Prefer multi-stage builds for compiled artifacts.
- Put stable dependency layers before frequently changing source layers.
- Use BuildKit cache mounts for package managers and compiler caches when appropriate.
- Pin base image families enough for reproducibility, especially CUDA/toolkit images.
- Keep runtime images smaller than build images when practical.
- Do not bake secrets, tokens, Kaggle keys, SSH keys, or notebook auth URLs into images.

## Highload GPU Notes

For C++/CUDA projects, separate dependency/toolchain image layers from source. Keep `build/`, `target/`, CUDA caches, and profiler outputs out of final runtime layers unless explicitly needed.