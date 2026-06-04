---
name: debug-docker
description: Use when Docker build/run/compose fails, Docker Desktop or daemon is unavailable, logs are needed, disk is high, or cleanup is requested.
---

# Debug Docker

Start with facts before changing files.

## Inspect

- `docker version`, `docker info`
- `docker compose ps`, `docker compose logs --tail=200 <service>`
- `docker ps -a`, `docker images`, `docker volume ls`
- `docker inspect <container>` when env, mounts, entrypoint, or GPU device wiring is unclear
- `docker system df` before cleanup

## Cleanup Rule

Never run destructive cleanup by default. Ask before `docker system prune`, `docker volume rm`, `docker builder prune`, or removing containers/images. Prefer targeted cleanup over broad prune.

## Windows/WSL Notes

Check Docker Desktop status, WSL integration, path mounts, line endings, and whether commands are running in PowerShell vs WSL. For GPU containers on Windows, confirm WSL2 + NVIDIA driver support and test `nvidia-smi` inside a Linux container.
