---
name: shorten-cnot-programs
description: Use when improving this project's own shared-basis CNOT synthesizer, training a full-matrix structural transformer or action head, generating random walks and diffusion features, or comparing verified full-program lengths. Carries the project's mathematical contracts, failed experiments, provenance boundaries and reproducible next steps.
---

# Shorten CNOT programs

## Start with evidence

1. Locate `synthesis-methods/01_shared_basis_stage17/improved` under the supplied
   project root. Do not assume cwd is the plugin folder or hardcode a username.
2. Read [contracts](references/contracts.md) and [experiment ledger](references/experiments.md).
3. Run `python <plugin-root>/scripts/check_evidence.py --project <project-root>`.
   Changed hashes mean the snapshot is older; inspect the actual changes before
   reusing a conclusion. Do not overwrite current code with the snapshot.
4. Read [implementation plan](references/implementation-plan.md) for current work.
   Inspect processes/run files before launching any training; never duplicate an
   existing run. Respect the user's current scope and compute authorization.

## Route to the relevant knowledge

| Work | Read |
|---|---|
| Basis compiler, stages 17–31, symmetries | [Methods](references/methods.md) |
| Transformer, Bellman gradient, replay, action approximation | [Learning](references/learning.md) |
| Random walks from I and location in the group | [Diffusion](references/diffusion.md) |
| Reproduce or audit a result | [Runbook](references/runbook.md), [source map](references/source-map.md) |
| Decide which improvement to implement next | [Plan](references/implementation-plan.md) |

## Non-negotiable mathematical meaning

- State is the complete invertible GF(2) matrix. CNOT(c,t) means row_t ^= row_c.
- Every reported encoder word must map I to the original M exactly. A reduction
  M→I must be reversed to obtain the encoder. Record n, M hash, conventions.
- Known program lengths, including reversed random walks, are upper bounds.
  Exact labels require BFS or a proved matching lower bound. Never restore the
  invalid certificate-suffix distance ranking (`basis_rank_weight`).
- Preserve exact V(I)=0, full-matrix inputs and gradients through both sides of
  the selected Bellman branch. Full local backup is not enumeration of GL(n,2).
- Paid basis preparation/core/uncompute, neural scalar field, action proposal,
  and Hamming control are different mechanisms. Attribute improvements separately.
- No code, chains, data or training labels from the Kelipaev archive. Use the
  original nine stage17 target files for held-out testing, not training. Other
  targets require independently established allowed provenance.
- No wall-clock cutoff hidden in teacher helpers. Finite update/depth/width
  budgets remain explicit. Preserve old sources/results; create new run dirs.

## Before claiming progress

Report complete verified lengths, solved fraction/failure reason, search budget,
runtime and training cost. Compare same matrices and conventions. A lower loss,
active gradient, improved training goal, or faster action head is not evidence
of shorter held-out programs. Report inactive macro constraints and failed
ablations explicitly. Best-known verified program remains the incumbent.

Snapshot status: paid-basis/local-window compiler shortened own programs;
whole-matrix neural models have not beaten the Hamming controls on the measured
larger targets. The first paired diffusion-feature test tied on HGP13/25/34;
heat-on large test gave HGP58=234 vs Hamming159; BB72 failed at depth480 for both.
Heat-off large test remains pending. Read the ledger before quoting these numbers.

## Maintain the knowledge

When the user authorizes updating this plugin, add a dated experiment row with
source/checkpoint/data hashes, full-word verification and explicit evidence limits.
Keep historical negative results. Update the source manifest using the project
packaging script and validate the plugin. Do not silently turn proposed work into
completed work or modify unrelated personal memories.
