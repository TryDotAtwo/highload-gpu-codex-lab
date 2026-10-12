---
name: work-with-molab
description: Use when connecting to, editing, executing, monitoring, recovering, or collecting artifacts from a Molab-hosted marimo notebook or GPU sandbox.
---

# Work With Molab

Molab work is interactive live-notebook work. Read these references before a long or GPU-heavy run:

- `references/native-pair-and-lifecycle.md`
- `references/gpu-jobs-and-artifacts.md`
- `references/session-failure-chronology.md`
- `references/foreground-experiment-runbook.md`
- `references/notebook-identity-and-partial-runs.md` for multiple notebook
  copies, browser recovery, competing scratch execution or incomplete results.
- `references/reproducible-build-recovery.md` before rebuilding a recovered session.
- `references/compact-notebook-bootstrap.md` when an old notebook fails at
  startup, has accumulated automatic heavy cells, or a fresh session needs recovery.

## Primary Path

1. Read the `marimo-pair` skill completely.
2. Connect to the exact sandbox URL/token with its `execute-code.sh` transport.
3. Run a harmless probe and send `mo.status.toast(...)` so the user sees that pairing works.
4. Inspect active cells and OS processes before starting work.
5. Use scratchpad execution for probes and marimo code mode for durable cells.

Native pairing is the execution path. Use browser automation only to create or locate a session when pairing details are unavailable.

## Long Work

Keep long work attached to a foreground notebook cell and the foreground SSE request. A foreground subprocess inside that active cell is acceptable; a detached/background job that makes the notebook appear idle is not. Stream bounded progress and write a full log.

One heavy GPU job per sandbox. Do not run a known-hanging control first. A Python timeout or killed host process does not guarantee recovery from a wedged GPU kernel or broken barrier.

HTTP 410 means the sandbox is gone. Stop retrying and request a fresh pair URL/token; native pairing cannot create a new sandbox.

## Boundaries

- Never expose the tokenized URL or auth token in cells, logs, commits, commentary, or final responses.
- Do not stop or interrupt existing work unless authorized.
- Do not bypass enforcement. Molab warns that non-interactive jobs and other prohibited use can terminate a notebook.
- Keep CUDA/model/search design in their domain plugins; this plugin owns Molab transport, lifecycle, storage, and execution discipline.

Report exactly what ran, what was only prepared, and which artifacts were verified.
