# Foreground Molab Experiment Runbook

## Before execution

1. Connect natively and send a toast.
2. Probe GPU identity, compute capability, VRAM, driver, CUDA and process list.
3. Confirm there is one heavy job at most.
4. Pin source commit, dirty patch hash, model/artifact hashes and toolchain versions.
5. Choose a bounded first gate that cannot monopolize the session indefinitely.

## Foreground cell contract

- Start work from one foreground cell and keep the foreground SSE request alive.
- A child compiler/runner may run synchronously inside the cell; never detach it.
- Emit a heartbeat every 5–30 seconds when the tool may otherwise be silent.
- Stream bounded progress lines while writing a complete log to disk.
- Add an explicit timeout only when the device operation can recover safely; a host timeout is not a GPU reset.

## Incremental persistence

After every seed, sweep row, depth or compile stage, atomically store:

- current status and stage;
- exact config/workload fingerprint;
- stdout/stderr log path;
- artifact hash and byte size;
- completed metrics rows;
- terminal reason.

Use persistent storage for source bundles, checkpoints, logs and results. Because the observed mount is `noexec`, copy executables to `/tmp` for launch and verify the copied artifact hash.

## Benchmark sequence

1. Harmless import/device probe.
2. Compile gate with heartbeat.
3. Tiny runtime correctness launch.
4. Numerical oracle.
5. Short performance screen.
6. Repeated control/candidate medians.
7. Integrated benchmark.
8. Task-level acceptance.

Do not run a known-hanging negative control before the safe candidate. Keep each experiment bounded and preserve the last correct binary.

## Session-loss handling

- If pair transport fails, independently check HTTPS/session listing with the verified transport.
- If the endpoint returns HTTP 410, stop retrying.
- Mark the current experiment `platform_loss` unless a terminal compiler/CUDA/OS line proves a narrower cause.
- Record the exact last completed stage and the first unverified gate.
- Resume from persistent artifacts in a fresh session; do not rerun the whole matrix blindly.

## Local/Docker compilation

Local container compilation is acceptable when toolkit, target architecture, CUTLASS revision, ABI and compile flags match. It is only a build step. Link/run/profile on Molab and compare the uploaded artifact hash before claiming target-hardware evidence.

## Final report checklist

- foreground execution and heartbeat confirmed;
- exact hardware/toolchain/source/artifact identity;
- one heavy job policy observed;
- correctness and benchmark scopes named separately;
- repetitions/statistic and control recorded;
- memory/resource/failure evidence captured;
- persistent artifact hash present;
- prepared versus runtime-verified work stated explicitly.
