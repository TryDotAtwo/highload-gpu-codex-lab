# Compact notebook bootstrap and recovery

Use this procedure when a historical notebook fails before pairing or opening it
can trigger old downloads/builds/runs. Do not replace a confirmed live workload.
Inspect the exact notebook, active cells and authoritative process/job handles
first; delayed output alone is not proof of a dead sandbox.

## Isolate startup before rebuilding the experiment

1. Keep the original notebook as history. Record its identity and export/hash
   using the approved transport. Never include tokens or private pairing state.
2. If the sandbox was lost or the notebook cannot start, use a small notebook
   with a harmless first cell to test Python, actual GPU availability, disk space
   and required environment-variable presence. Report only presence/access,
   never values. A successful minimal notebook establishes service availability;
   it does not identify the failing old cell or dependency.
3. Treat secrets, workspace files, toolchains and GPU assignment as unverified in
   a new session. A copied notebook need not carry them. Recheck after changes;
   old cell outputs can be stale. A missing device path early in startup alone
   is not decisive if a later actual GPU query succeeds.
4. Add restore, build, bounded experiment and export as distinct, explicitly
   invoked stages. Use supported marimo execution/gating semantics, checked in
   the actual installed version. Opening the notebook or changing an unrelated
   dependency must not rerun heavy stages. Do not invent an unsupported API.

## Restore a pinned closure, then execute once

Keep implementation in source files/artifacts rather than growing a notebook
into hundreds of enabled historical experiment cells. Resolve the exact archive
revision, manifest, input, source and binary hashes before restore. Verify bytes
in a fresh destination. If source/build closure is missing, say so; a runnable
binary does not prove reproducible rebuilding.

After checking that no equivalent workload is live, run one bounded replay or
discriminating experiment in its foreground cell with visible progress and a
saved full log. Prefer the existing project's verified archive/build tooling.
Do not re-download unchanged objects or rebuild a restored identical binary
merely to obtain another green status. Build when the actual dependency/source
change or scientific question requires it.

Persist a completed result or supported checkpoint with immutable receipts;
test restoration at a meaningful boundary before relying on it. A one-receptor,
few-tick replay proves only that narrow replay, not biological validity, full
model speed, or end-to-end application success.

The MaleCNS incident of 2026-09-24 motivates this procedure: a 255-cell historical
notebook repeatedly failed before pairing, a minimal notebook ran, and a compact
opt-in recovery later reproduced a pinned one-receptor replay. The exact original
startup fault remained unidentified. These are historical observations, not
universal size limits or evidence that every startup failure has this cause.
