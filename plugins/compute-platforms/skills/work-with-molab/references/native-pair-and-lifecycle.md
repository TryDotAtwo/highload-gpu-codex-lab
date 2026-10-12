# Native Pair And Session Lifecycle

## Connect

Use the bundled marimo-pair `execute-code.sh --url ... --token ...`. The live kernel is the source of truth. After a probe, send a fun toast with `mo.status.toast(...)`.

Never store the URL/token in notebook code. Pass them only as local transport arguments and redact them from command output.

## Windows Transport Diagnosis

If the shell helper appears stuck:

1. resolve DNS and test TCP;
2. query `/api/sessions` with the supplied token;
3. if HTTP 200 succeeds but `curl/Schannel` hangs, use an equivalent Python `requests`/OpenSSL client that preserves session discovery, execution request, and SSE streaming through `done`;
4. call the real Python interpreter, not a Unix-shebang script through an ambiguous Windows launcher;
5. re-prove the path with a harmless expression and toast.

This is a transport fallback, not browser automation or remote shell access.

## Foreground SSE

Keep long execution attached to the current marimo cell and SSE request. Print a heartbeat at bounded intervals and stage markers that prove progress. If the request disconnects, first inspect the live session and outputs; do not assume the kernel stopped.

Do not use detached supervisors, `nohup`, or background processes to turn the notebook into a non-interactive batch host. Molab's official restrictions warn that notebooks used for non-interactive jobs may be terminated without warning. They also prohibit remote-control mechanisms such as SSH and circumvention of enforcement.

Source: [Molab restrictions on use](https://molab.marimo.io/pages/molab/restrictions).

## Terminal States

- `HTTP 410`: endpoint expired or terminated; stop retries and obtain a fresh session.
- SSE transport failure with live `/api/sessions`: repair local transport and reconnect.
- no advancing heartbeat/log/output: inspect active cells and OS process before launching anything else.
- suspected wedged GPU: do not stack more probes. A host timeout cannot repair a device-side deadlock; the sandbox may require replacement.

Native pairing cannot create a new Molab sandbox or invent a fresh token.

## Marimo Reactivity

Cells cannot redefine public top-level names from other cells. For user-pasteable fallbacks, wrap work in one uniquely named function with local imports. Use code mode for durable edits; do not mutate the notebook artifact behind the running editor. Run `marimo check` when a durable notebook has changed.
