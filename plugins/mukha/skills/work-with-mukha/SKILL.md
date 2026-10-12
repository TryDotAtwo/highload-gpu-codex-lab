---
name: work-with-mukha
description: Develop, diagnose, or review the MaleCNS faithful-fly project, including biological model transfer, local plasticity, visual and body sensory loops, Rust/C++/CUDA execution, Molab recovery, cockpit contact and the three-seed KSP Mun evaluation. Use for this project and its experiments, not unrelated insects or generic KSP autopilots.
---

# Муха / full MaleCNS embodied research

Help complete the user's actual fly project. This skill supplies decision rules,
source pointers and read-only helpers; it is not a model, validation certificate,
permission grant or replacement for the user's current scope.

## Mandatory execution boundary (2026-10-04)

For this project, ALL computation runs in MoLab, including CPU/GPU work, tests, builds, project helpers, artifact hashing, training and rendering. Locally only read/edit text source, instructions and reports, and use the remote transport. Never download datasets, models, binaries, checkpoints or recordings to Ivan's computer. Publish each completed immutable shard/condition/checkpoint/log segment immediately to the private HF archive; verify commit/manifest receipt BEFORE the next dependent stage. Failed HF persistence stops progression; unavailable MoLab is not permission for local fallback. Read [execution-policy.md](references/execution-policy.md) before execution. Historical local runbooks are superseded. Do not use subagents.

## First useful action

1. Locate the actual workspace. Read the current user objective, `WORK_PLAN.md`
   gates and the source/report for the active experiment. In MoLab only, use
   `python <plugin>/scripts/project_snapshot.py --workspace <root>` to locate
   relevant files without scanning all artifacts. Snapshot flags are leads,
   not verified results. Reuse the established context on subsequent turns.
2. Resolve live work before launching: inspect the authoritative process/job/cell
   handle. A timeout, old PID text, lock file or open notebook alone is not
   proof of completion or liveness. Reuse the same live run. Avoid duplicate jobs.
3. Choose the unfinished experiment that most directly resolves the current
   biological/interface uncertainty. State its question, fixed conditions,
   observation, acceptance criterion and next action on failure. Use the existing
   config/report rather than inventing another schema. Then execute through a
   terminal result or a verified wait; a status rewrite is not an experiment.

Read only the relevant guide:

| Need | Guide |
|---|---|
| Locate authoritative implementations / stale plans | [project-map.md](references/project-map.md) |
| Cell identity, chemistry, physiological readouts, learning | [biology.md](references/biology.md) |
| Native boundaries, numerics, CUDA and speed | [runtime.md](references/runtime.md) |
| Large data, resume, Molab/HF and provenance | [artifacts.md](references/artifacts.md) |
| Body/cockpit causal path, curriculum, KSP/videos | [embodiment.md](references/embodiment.md) |
| Decide the next high-value experiment | [experiment-selection.md](references/experiment-selection.md) |

## Contract that historical shortcuts must not override

The accepted project goal is full published MaleCNS neuronal coverage, biological
reactions and local plasticity, physical fly body, vision and contact-based
cockpit operation, learning to land on Mun without hidden autopilot, at least
90/100 KSP landings for each of three training runs, and synchronized reproducible
recordings. Keep each requirement open until its own evidence passes.

- Preserve the declared neural population and all its internal source rows.
  Keep source/excluded/boundary records. The 167216-object candidate export is a
  declared reconstruction policy, not proof that every object is a complete neuron.
- Keep privileged rocket state for scoring/reset/calibration outside policy
  observations. Ordinary flight commands must originate from measured physical
  cockpit positions. A direct neural decoder to throttle or scripted pose is not
  this goal. Diagnostic direct drive must remain explicit and separate.
- Unknown cell parameters may be studied as falsifiable hypotheses with stated
  uncertainty. Do not call them measured biology or adjust them solely until a
  desired landing/contact appears. Do not freeze all research until every unknown
  biological quantity is known; choose a discriminating experiment instead.
- Exact source-code reproduction, numerical validity, biological transfer,
  learning, and KSP success are different evidence layers. A `passed` field or
  checksum proves only the operation actually checked. A negative result can
  complete an experiment while leaving the overall goal incomplete.

## Use the available domain skills concretely

The plugin is useful without these optional companions. If available, read and
apply the appropriate SKILL.md when the work reaches that domain:

- `molab:work-with-molab` for pairing, live execution, recovery, persistence;
  follow its marimo-pair reference and keep heavy work visible in its live cell.
- `gpu-architecture:design-gpu-architectures` for an entire runtime redesign;
  `highload-gpu` selects profiling, kernels, sanitizer or target-hardware guidance.
- `hugging-face:hf-cli` only for Hub CLI operations; existing verified project
  archive tooling should be reused instead of rebuilding authentication.
- PDF/document skills when the primary experimental source requires them.

If a companion is unavailable, use verified project tooling for its task and
state the limit. Do not invent tools, install unrelated plugins or load every
skill. Record once which actual skill/source changed the chosen action. A name
drop or installation flag is not evidence that instructions were applied.

## Deliver work that changes the next action

Prefer one complete scientific/engineering slice over many small green checks:
for example, verified synapse extraction + pair-level reconciliation + answer
about compartment resolution. Keep scripts, executed build/input hashes,
terminal logs and negative results. Once a relevant check passes, stop repeating
it unless a new change invalidates it. Do not substitute a full report rewrite,
another source inventory or an unrelated unit test for the unresolved experiment.

The read-only helpers in `<plugin>/scripts` inspect a workspace, check an explicit
manifest, and summarize skill-read requests from one specified session log. They
never launch GPU work, inspect credentials, upload, delete, edit models or mark
the goal achieved. In a running task after installation, read this absolute file
directly; newly installed skills may only auto-discover in a fresh task.
