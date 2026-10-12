# Project map and authority

Use paths relative to the actual workspace, commonly `Documents/ChatGPT/Муха`.
This map records the audit on 2026-09-24. Recheck files and live state; it is not
a claim that older reports describe today's binaries.

## Read the smallest relevant set

| Concern | Current entry points / evidence leads |
|---|---|
| Goal and experiments | `WORK_PLAN.md`, `README.md`, most recent protocol/report |
| Source population | `tools/build_connectome.py`, `reports/malecns_source_lock.json`, `data/derived/malecns_v1_candidates/manifest.json` |
| Chemistry uncertainty | `docs/NEUROCHEMISTRY.md`, `reports/full_graph_chemistry_coverage.json` |
| Native model | `native/cuda_state.inc`, `native/lif.cpp`, `src/cuda.rs`, `src/pilot.rs` |
| Numerical comparison | `reports/shiu_native64_comparison.json`, `reports/malecns_cpu_equivalence.json`, `docs/NUMERICAL_CONTRACT.md` |
| Visual path | `src/visual_input.rs`, `native/photon.cu`, `docs/VISUAL_INPUT_PIPELINE.md`, `docs/VISUAL_CAUSALITY.md` |
| Optical identities | `docs/VISION_MAPPING.md`, `docs/R16_COLUMN_INFERENCE.md`, `docs/VISUAL_BOUNDARY.md` |
| Plasticity | `native/huang.cpp`, `docs/PLASTICITY_REFERENCE.md`, `tools/audit_mb_plasticity_boundary.py` |
| Contact coordinates | `tools/extract_mb_synapse_locations.py`, `data/derived/mb_synapse_locations_v1/progress.json` |
| Muscle identities | `docs/MOTOR_MAPPING_EVIDENCE.md`, `docs/MUSCLE_REFERENCE.md`, `configs/knee_interface_draft.json` |
| Body sense | `docs/PROPRIOCEPTIVE_INPUT.md`, `docs/FECO_INHIBITION_REFERENCE.md`, `native/exposure_observation.h` |
| Native coupling | `native/brain_body_probe.cpp`, `native/motor_filter.h`, `native/body.cpp` |
| Environment / evaluation | `native/rocket_vertical.h`, `src/landing.rs`, `docs/ROCKET_ENVIRONMENT.md`, `docs/LANDING_ASSESSMENT.md` |
| Remote recovery | `docs/HF_ARCHIVE.md`, `docs/MOLAB_NATIVE.md`, `reports/molab_startup_diagnosis_2026-09-24.md` |
| Rejected retina optimizations | `docs/GROUPED_RETINA_ARCHITECTURE_REVIEW.md`, `docs/RETINA_RNG_MEMORY_DESIGN.md`, `docs/PHOTON_SURROGATE.md` |

## Authority and stale records

Current user intent and accepted gates govern. Old `FEASIBILITY.md` and
`NATIVE_ARCHITECTURE.md` contain exploratory telemetry/decoder/backpropagation
routes and stale implementation status. Do not turn them into permission to
change the current biological/contact-control goal. Follow the current code and
immutable evidence for implementation facts; preserve superseded results with
their original conditions.

Some later visual executables and source closures are stored in HF/Molab, not
the visible local tree. Check the referenced archive before rewriting missing
code. A local notebook can be orchestration; it need not be the authoritative
source of each runtime component. Never dump `build/` broadly: private pairing
files can live there. Fetch only the explicitly required public source/receipt.

At the audit snapshot there were no git commits in the checkout. This is a
reproducibility gap, not permission to publish or commit everything. Use normal
scoped Git work if authorized; exclude data, credentials, private sessions and
large generated recordings. Archive restoration and Git history prove different
things and must both identify the executed source.


## Workspace correction, 2026-10-04

The inspected implementation is at D:/Муха. Documents/ChatGPT/Муха contains historical audits and recovery context; do not mistake these snapshots for current source. Recheck the exact workspace before edits. Read docs/AUDIT_2026-10-04.md and docs/EXECUTION_POLICY.md in the actual project. Current small reports describe 10852 SWCs, repaired near-equal LIF arithmetic, series v3 checkpoint/start bindings, and an unvalidated conductance candidate; verify these again rather than treating this map as live evidence. All gates remain open in the inspected ledger. No remote liveness or HF inventory was verified in this static audit.
