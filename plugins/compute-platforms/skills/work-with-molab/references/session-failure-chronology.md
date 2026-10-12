# Molab Session Failure Chronology

For later corrections and complete-versus-partial run evidence, read
`notebook-identity-and-partial-runs.md`. Foreground mitigation does not prove
the server's termination cause or guarantee that a session survives.

This catalog separates transport, notebook lifecycle, build, GPU and platform failures. It contains no session URL or auth token.

## Native transport on Windows

The official shell helper used curl/Schannel and repeatedly timed out even when:

- DNS and TCP 443 worked;
- PowerShell/.NET returned HTTP 200;
- Python `requests` listed the active session;
- a Python/OpenSSL SSE adapter produced ordered stdout/done events and a toast.

On that host, use the verified Python 3.11 requests adapter rather than assuming the sandbox is dead. Do not invoke it through a launcher that only prints the shebang interpreter name.

## Detached/non-interactive work

A detached subprocess can leave the notebook apparently idle and is incompatible with the intended interactive lifecycle. Long work must remain attached to the foreground cell and SSE stream. Do not use an external supervisor to evade enforcement.

## Silent foreground compiler

`capture_output=True` on a heavy compiler emitted no notebook events for over a minute. The SSE path closed and scratch execution was interrupted. The fix is a foreground wrapper that streams bounded progress or a heartbeat while preserving the full log.

## HTTP 410

HTTP 410 means the sandbox has been destroyed. It is terminal for that URL/token. Stop retries, preserve local evidence and request/create a fresh session through the supported UI. Native pairing cannot resurrect it.

Several sessions disappeared during correct foreground work. Without a terminal CUDA error this is **platform loss**, not automatically OOM. In one relevant run observed VRAM was only about **3.2 GiB**, which contradicted a blanket OOM diagnosis.

## EventSource errors

`EventSource connection failed` often appeared after the runtime had disappeared. Treat it as a consequence until independent evidence proves a network root cause.

## Persistent storage `noexec`

Molab persistent storage retained artifacts but was mounted `noexec` in the observed runtime. Copy a verified binary to `/tmp`, re-hash it, mark the copy executable, and run there. Store logs/results back persistently.

## GPU/context wedge

A known-hanging CUDA control can poison the context and make subsequent host timeouts meaningless. A killed Python call does not reset the GPU. Run safe bounded stage gates first; use a fresh sandbox after an unrecoverable device hang.

## Long-lived process symbol state

Loading multiple production CUDA shared objects into one Python process caused symbol interposition. `RTLD_DEEPBIND` was insufficient; `dlmopen` duplicated CUDA runtime state and hung. Use a clean marimo kernel and load exactly one production library for an A/B.

## Toolchain sequence encountered

The campaign exposed missing CMake, hidden nvcc, mixed CUDA 13.3 compiler with 13.0 headers/runtime, missing CCCL `nv/target`, NVTX, CURAND and PyTorch-local NCCL paths. Record the complete matching toolchain rather than fixing headers one at a time without a manifest.
