---
name: run-docker-compose
description: Use when working with Compose services, compose.yaml, service dependencies, ports, volumes, env files, profiles, or GPU reservations.
---

# Run Docker Compose

Use Compose docs: https://docs.docker.com/compose/ and GPU Compose docs: https://docs.docker.com/compose/how-tos/gpu-support/

## Rules

- Prefer `docker compose` over legacy `docker-compose` unless the repo requires legacy.
- Read existing compose files and `.env` before changing ports, volumes, or profiles.
- Use named volumes for durable service data and bind mounts for active source trees.
- Keep secrets out of committed compose files; use env files or secret stores.
- For GPUs, set device reservations with `capabilities: [gpu]`; `count` and `device_ids` are mutually exclusive.
- For local dev, make service names, health checks, and logs easy to inspect.

## Verification

Use `docker compose config` to validate merged config, `docker compose ps` for state, and `docker compose logs <service>` for failures.