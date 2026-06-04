---
name: work-with-molab
description: Use when the user asks Codex to work with Molab, molab.marimo.io, a Molab sandbox/session, marimo GPU notebooks hosted by Molab, or to run/monitor/download notebook outputs from Molab. This includes requests like "open Molab", "run this in Molab", "check the Molab error", "download Molab plots/logs", "make a cell for Molab", or "use the current Molab browser session".
---

# Work With Molab

Use this skill whenever the user wants Codex to operate Molab or a Molab-hosted marimo notebook.

## Core Intent

Molab work is browser-session work. Prefer the Codex in-app Browser so user login cookies and Molab session state are preserved. Do not use generic web browsing for an authenticated Molab session unless the user only asks a conceptual question.

## Safety And Privacy

- Do not repeat full Molab sandbox/session URLs in final answers because they include auth tokens.
- When summarizing, refer to "the current Molab session" or paths inside the sandbox such as `/tmp/...`.
- Do not shut down, restart, stop, or interrupt a Molab kernel/job unless the user explicitly asks.
- Before adding/running a new cell, check whether another long-running cell is active. If active, prefer preparing code for the user or adding a non-running cell.
- Molab output and browser DOM may expose secrets/logs; quote only the relevant error lines or metrics.

## Browser Workflow

1. Use the Browser plugin / in-app browser control skill first.
2. Connect to the existing Molab tab when present; do not open a new login flow unnecessarily.
3. If the visible page is `molab.marimo.io/notebooks/...`, inspect if the actual notebook is inside a sandbox iframe. If direct DOM text is unavailable, use the iframe `src` only internally; do not paste the full tokenized URL to the user.
4. If the browser bridge cannot read cross-origin iframe content, ask the user to paste the visible error/output, or provide code for them to run in a cell.
5. Keep updates short and explicit: what context is being read, whether a job is running, and whether a cell will be executed or only prepared.

## Marimo Notebook Constraints

Molab notebooks are marimo notebooks, so cells cannot redefine top-level names defined in other cells. When giving code for the user to paste:

- Wrap substantial code in one uniquely named function and call it once at the bottom.
- Put imports inside the function when possible.
- Use unique function names with a version suffix, for example `run_molab_task_v3()`.
- Avoid common top-level names such as `json`, `os`, `pathlib`, `subprocess`, `df`, `results`, `lines`, and `p`.
- If a cell errors with "This cell redefines variables from other cells", provide a wrapped replacement cell rather than asking the user to edit many names.
- For long code blocks, prefer giving the user a complete replacement cell rather than trying to paste through the browser if CodeMirror virtualization is unreliable.

## Running Jobs

When preparing a Molab run cell:

- Print the executable, command, key env vars, output paths, and log paths before running.
- Stream only important progress lines for long jobs.
- For subprocess jobs, write a full text log to `/tmp` or a user-specified path.
- For GPU jobs, include VRAM/RAM/disk probes when useful: `nvidia-smi`, `torch.cuda.mem_get_info()`, `/proc/meminfo`, and `df -h`.
- For torchrun jobs, distinguish launch mode from algorithm branch. A `torchrun --nproc_per_node=1` launch proves `RANK/WORLD_SIZE/LOCAL_RANK` exist, but not necessarily that the library avoids its legacy branch.

## Downloading Plots And Logs

Molab/marimo image outputs may be cropped by the browser display layer. Prefer source-backed exports:

- If the plot was generated from JSONL/CSV/log lines, pull or reconstruct the underlying data and re-render locally with a large figure and `bbox_inches="tight"`.
- Hide sentinel threshold values when plotting scores if they are not real scores, for example threshold values around `4.19e6` from `UINT32_MAX / 1024`.
- Save downloaded/re-rendered artifacts under the current workspace `test_results/` when working inside a project repo.
- Validate image dimensions and byte size after saving.

## Molab Code Cell Patterns

For user-pasteable cells, prefer this shape:

```python
def run_molab_example_v1():
    import json
    import pathlib
    import subprocess

    base = pathlib.Path("/tmp/molab_example")
    base.mkdir(parents=True, exist_ok=True)
    print("BASE", base)
    # work here

run_molab_example_v1()
```

For subprocess logging:

```python
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
for line in proc.stdout:
    log_file.write(line)
    if line.startswith(("depth_start=", "depth_done=", "RESULT_JSON=", "RANK_EXCEPTION_JSON=")):
        print(line, end="", flush=True)
rc = proc.wait()
print("RC", rc)
```

## Response Style

- Be direct about whether Codex actually ran something, only prepared a cell, or needs the user to paste output.
- Include exact sandbox file paths for logs/artifacts, but not tokenized Molab URLs.
- If a Molab operation fails due browser tooling limitations, switch to a user-pasteable cell quickly.
