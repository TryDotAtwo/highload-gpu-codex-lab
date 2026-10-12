---
name: reuse-docker-images-and-log-output
description: Use when reusing Docker images or logs.
---

# Reuse Docker Images And Log Output

Use this skill to keep Docker workspaces clean and observable. Load
`references/reuse-and-logs.md` when a detailed checklist is needed.

## Image Reuse Policy

- Inspect existing images/tags, project scripts, Compose files, and Dockerfiles.
- Reuse existing repo image names unless there is a concrete reason to add one.
- Keep dependency/toolchain layers stable and source copies late for cache reuse.
- Do not run broad cleanup after builds; ask before targeted cleanup.

## Container Log Rule

Long-running containers must write useful progress to stdout/stderr so `docker logs` and Compose logs work.

- Prefer foreground processes.
- Stream key progress and failure lines to stdout/stderr.
- Use unbuffered Python or explicit flushing for live logs.
- Use `exec "$@"` in shell entrypoints.

## Review Checklist

- Explain any new image name.
- Confirm dependency/toolchain cache reuse.
- Confirm progress is visible through `docker logs` or Compose logs.
