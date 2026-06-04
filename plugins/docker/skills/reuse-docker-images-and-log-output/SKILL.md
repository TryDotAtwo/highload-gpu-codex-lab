---
name: reuse-docker-images-and-log-output
description: Use when Docker work should avoid duplicate images, reuse existing tags/cache, control build artifacts, or ensure container logs appear in docker logs/stdout/stderr.
---

# Reuse Docker Images And Log Output

Use this skill to keep Docker workspaces clean and observable.

## Image Reuse Policy

Before building a new image:

- Inspect existing images/tags: `docker images`, project scripts, `compose.yaml`, and current Dockerfiles.
- Reuse the repo's existing dev/build/runtime image names unless there is a concrete reason to add a new one.
- Prefer stable explicit tags like `project-gpu-dev:cuda12.8-sm120` over random or timestamp tags for iterative work.
- Keep toolchain/dependency layers stable; put source copies late so builds reuse cache.
- Use BuildKit cache mounts for apt, pip/uv, Cargo, CMake/Ninja, ccache/sccache when the repo supports it.
- Use multi-stage builds so temporary build layers do not become runtime images.
- Do not change base CUDA/toolchain image just to test unrelated code.
- Do not run broad cleanup after builds. If cleanup is needed, show `docker system df` and remove only targeted temporary images/containers after approval.

## Container Log Rule

Long-running containers must write useful progress to stdout/stderr so `docker logs` and Compose logs work.

- Prefer foreground processes over daemonizing inside the container.
- Avoid redirecting all output only to a file. If writing a file log, also stream key lines to stdout/stderr.
- Python: use unbuffered mode (`python -u`) or `PYTHONUNBUFFERED=1` for live logs.
- C++/CUDA runners: flush progress lines at depth/stage boundaries and on fatal errors.
- Shell entrypoints: use `exec "$@"` so signals and exit codes reach the main process.
- Compose services should have enough logs for `docker compose logs -f <service>` to show startup, config, progress, and failure reason.

## Review Checklist

- Did this add a new image name? If yes, why could the existing image not be reused?
- Will the next build hit cache for dependency/toolchain layers?
- Are transient build outputs excluded from final images and `.dockerignore`?
- Can the user see progress with `docker logs -f` without entering the container?
- Are logs available both live and, when needed, as saved artifacts?