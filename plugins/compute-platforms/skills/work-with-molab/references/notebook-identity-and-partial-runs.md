# Notebook identity and partial-run recovery

Lessons audited2026-09-03; no session IDs, tokens or user-specific notebook
addresses are embedded as reusable connection defaults.

## Identify the right document

A title such as Copy or untitled is not version evidence. Compare exact
notebook IDs and the most recent saved experiment cells, source/binary hashes,
and reports. Browser tab recency is not notebook modification time. Say
"latest among the documents inspected" unless the full inventory was checked.
Do not claim ownership based on a matching title or assume every GPU notebook
belongs to this task. Preserve unrelated notebooks and running cells.

When recovering through a browser, distinguish agent-owned tabs from user tabs.
An agent-tab list may be empty while the user already has the notebook open.
Use the supported fresh user-tab inventory and claim that exact tab. A prior
Debugger unattached does not establish that Molab is down. A successful DOM
read is not proof that the kernel or an old /tmp binary still exists.

Use the supported Pair UI or authorized notebook iframe connection to obtain
fresh pairing details; keep credentials only in the transport. Do not inspect
unrelated browser secrets or replay an expired token. Old output marked stale
is historical evidence, not a fresh execution. Never click Run all merely to
inspect an unfamiliar notebook: old cells can launch missing or unsafe jobs.

## One execution owner

Scratch execution is not an independent background job slot. Another pair
execution can interrupt it. Do not overlap pair calls to the same kernel,
including status/upload calls during heavy execution. Coordinate ownership
when other tasks share the notebook. Use code-mode durable cells, keep the
foreground SSE request attached, and poll the local request handle rather
than issue competing kernel executions.

Durable cells improve visibility and recoverability, not immunity to platform
loss. Foreground subprocess.run/Popen whose parent reads/waits is acceptable;
detached jobs are not. No fixed60/80/120-second lifetime was established.
Do not turn a temporal coincidence into an enforcement diagnosis or promise
that heartbeats prevent shutdown. Heartbeats report real progress, not idle evasion.

## Preserve evidence before the endpoint disappears

Print one structured result row after each completed seed or timing trial and
capture that stream locally. Save the remote structured report too, then
download immediately after completion. A remote file path is not durable
evidence until persistence or export has been verified.

Track requested and completed counts separately. If a seven-pair experiment
ends after five pairs, label five and retain the rows; do not silently pad,
merge another session or present a seven-pair median. A completed downloaded
experiment remains valid if a later independent experiment loses the sandbox.
Conversely completion markers without the promised files do not prove download.

After SSE closes without done, perform one bounded session/artifact check.
HTTP410 is terminal for that endpoint: stop retries. Preserve last completed
row, current unverified stage and terminal transport error. Without device/OS
failure evidence the cause is unknown platform loss, not automatically OOM,
barrier failure, idle timeout or regional enforcement. Use authorized normal
UI recovery; do not automate unlimited restarts to evade service limits.

## Source and binary continuity

After recovery, inspect cell state and GPU processes, verify architecture and
hash uploaded executables. The notebook can survive while /tmp does not.
Archive the cell body and producing source/build fingerprints without auth.
Use the same scoped notebook and retained artifacts instead of multiplying
clones or rebuilding the whole campaign after each lost sandbox.
