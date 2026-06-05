---
name: debug-docker
description: Use when debugging Docker failures.
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

## Docker Desktop Restart Rule

Avoid full Docker Desktop restarts as a first response; inspect status and logs first. If a full reset is necessary on Windows, use this order:

1. Stop or quit Docker Desktop.
2. Run `wsl --shutdown`.
3. Start Docker Desktop again and wait until the daemon is ready.
4. Recheck `docker version`, `docker info`, and the affected Compose services.
