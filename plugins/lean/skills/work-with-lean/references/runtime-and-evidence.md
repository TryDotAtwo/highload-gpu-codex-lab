# Runtime and evidence

## Local / Docker / Windows

Use the project's launcher and pins. For Docker, inspect the exact bind mounts and named volumes; Mathlib can live only inside the container volume. Search there through an existing authorized runtime. Do not treat a sandbox `permission denied` as proof the engine is broken. Match engine status and timestamped logs before changing anything.

One container's memory cap is not a cap on aggregate WSL memory: several 8 GiB containers can exhaust a 16 GiB VM. Reuse a confirmed live run, avoid duplicate jobs, and collect resource evidence before tuning. A generic script must not hardcode this audit project's CPU/RAM numbers or restart Docker automatically.

On Windows, Markdown backticks inside a PowerShell double-quoted string are escapes (`\e`, `\v` in intent can become control characters when expressed using PowerShell backticks). Use a literal single-quoted here-string or a structured file-writing API. Read the artifact back, including a control-character check. Do not interpolate untrusted source text into shell commands.

Capture native exit codes immediately. A PowerShell pipeline ending in `Select-Object`, a child script's `exit`, or the outer shell's reported status can obscure a failure. Use explicit checking and full saved stdout/stderr. Printed “Build completed” from an earlier run is not fresh evidence.

## Supplied helper

`../scripts/lean_evidence.py` uses Python 3.11+ standard library only. Resolve its actual installed path relative to this skill. It provides:

- `record`: runs the exact argv after `--`, with `shell=False`, saves stdout/stderr and `run.json`, snapshots explicitly selected project inputs before and after, and propagates failure. It does not wrap, restart, or reconfigure Docker. It never overwrites an existing evidence directory.
- `audit`: checks a successful build record and a successful axiom record, unchanged inputs, current source hashes, log hashes, a required declaration list, and all printed transitive axioms. Both run records must include the same input selection, including that declaration list. Handles multiline lists and `does not depend on any axioms`; fails closed on missing, duplicate, malformed, or nonstandard results.
- `coverage`: summarizes recorded statuses separately for current and historical source records. It does not certify the ledger's mathematical claims or count repeated records as independent results.

Create an expected-declaration text file in the project, one fully qualified Lean name per line. Review it against source claims; generate `#print axioms` commands in an audit file importing the verified target. For both run commands include that audit file, expected list, trusted sources, root imports, toolchain and Lake configs/manifest. Include certificate inputs/generators when their identity is part of acceptance.

Example for a local Lake project (substitute actual paths, target, config type):

```text
python lean_evidence.py record --project PROJECT --kind build --out EVIDENCE/build --input Proofs --input Proofs.lean --input AxiomAudit.lean --input expected.txt --input lean-toolchain --input lakefile.toml --input lake-manifest.json -- lake build Proofs
python lean_evidence.py record --project PROJECT --kind axioms --out EVIDENCE/axioms --input Proofs --input Proofs.lean --input AxiomAudit.lean --input expected.txt --input lean-toolchain --input lakefile.toml --input lake-manifest.json -- lake env lean AxiomAudit.lean
python lean_evidence.py audit --project PROJECT --build-run EVIDENCE/build/run.json --axiom-run EVIDENCE/axioms/run.json --expected expected.txt
python lean_evidence.py coverage --ledger CLAIM_LEDGER.json
```

For Docker replace argv after `--` with the established project runner, for example `pwsh -NoProfile -File D:\Project\run.ps1 lake build Proofs`, only when that runner correctly propagates the native exit code. Use the same inputs in both records. Evidence directories should be outside selected input directories. `record` may execute arbitrary code explicitly passed to it; normal task authorization still applies. Do not put credentials in argv.

## Limits of this helper

The record is a reproducibility artifact, not an attestation service. It cannot establish that arbitrary argv really ran Lean, that a remote/container runtime used the host snapshot, that installed dependencies match their manifest, or that no concurrent change occurred and was reverted between snapshots. Inspect the launcher/mounts/tool versions and prevent concurrent edits to the checked target. The human/agent must select every relevant input and required declaration. No parser proves source-to-theorem correspondence. For adversarial or publication acceptance, reproduce with pinned dependencies in an isolated environment.

The audit allowlist is fixed to the strict profile `propext`, `Classical.choice`, `Quot.sound`; a constructive-only project needs a narrower policy. Do not edit an allowlist merely to get green output. A changed trust requirement needs explicit project authorization and a clearly labeled result.
