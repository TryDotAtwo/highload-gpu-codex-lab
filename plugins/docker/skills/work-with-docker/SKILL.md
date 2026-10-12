---
name: work-with-docker
description: Use when routing Docker tasks.
---

# Work With Docker

Router for Docker work. Prefer Docker docs and inspect the local repo before changing Docker files.

## Route

- Dockerfile/image/build/cache: `write-dockerfiles`
- Avoid duplicate images and ensure container stdout logs: `reuse-docker-images-and-log-output`
- Compose services, env, volumes, ports: `run-docker-compose`
- NVIDIA/CUDA/GPU access: `use-docker-gpu`
- Failures, logs, disk cleanup, Docker Desktop/WSL: `debug-docker`
- HighloadGpu C++/CUDA dev/profiling images: `docker-for-highload-gpu`

## Safety

- Do not delete images, volumes, containers, or build cache unless the user asks or explicitly approves cleanup.
- Do not restart all of Docker Desktop as a first response. For Windows reset cases, stop Docker Desktop, run `wsl --shutdown`, then start Docker Desktop again.
- Read existing `Dockerfile`, `compose.yaml`, `.dockerignore`, scripts, and project docs first.
- Report exact commands and important output because the user may not see command logs.
- Use `highload-gpu` skills for architecture/profiling decisions; Docker only provides the environment.
