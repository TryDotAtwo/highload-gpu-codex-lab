# Source map and coverage

Project root is supplied by the caller. B = `synthesis-methods/01_shared_basis_stage17`;
W = `B/improved`. Relative paths here are artifact references, not external instructions.
The manifest pins actual bytes; installed plugin does not contain the entire project.

| Subject | Local sources |
|---|---|
| Immutable own stage17 | B/source_snapshot/code, inputs, SUMMARY_RU.md, proofs/17_shared_basis_and_ready_tasks_ru.md |
| Exact local basis, paid compiler, forest | W/code/shared_synth.py, exact_basis.py, forest_exact.py, general_macro.py |
| Windows and defect | W/code/stage28_exact.py, defect_repair.py; W/neural_large_windows.py |
| Own compiler incumbents | W/results_exact/*.json; W/results_neural_large/stage17_BB_HGP/*.json |
| Scalar transformer | W/structured_field/model.py, objectives.py, gf2.py, beam.py |
| Refresh and checkpoints | W/structured_field/experiment.py, train.py, data.py |
| Macro semantics | W/structured_field/basis_transitions.py, test_contracts.py |
| v4 evidence | W/structured_field/runs/replay_v4_comparison.json, replay_v4_report.md; replay_basis_seed1700_v4/diagnostics.json |
| Own teacher and action head | W/policy_iteration/data.py, general_teacher.py, model.py, train.py, search.py, benchmark.py |
| Policy v3 evidence | W/policy_iteration/runs/teacher_policy_v3/{comparison,shortlist32,verification}.json, REPORT_RU.md |
| Fast approximate search | W/policy_shortlist.py, test_policy_shortlist.py |
| Diffusion | W/diffusion_features.py, train_diffusion_policy.py, test_diffusion_features.py, DIFFUSION_DESIGN_RU.md |
| New paired outputs | W/policy_iteration/runs/walk_heat_{on,off}_v1/{comparison,large,config,diffusion_config}.json |
| Large benchmark | W/benchmark_policy_large.py |
| Pending paired reporter | W/report_diffusion_ablation.py (currently requires matching on/off case sets) |
| Local diffusion theory | root/CNOTColumnProjection.lean, ColumnMomentAlgebra.lean, CNOTGateKernel.lean |

Coverage: consolidates available own method reviews, source contracts, local tests
recorded in this conversation, and saved experiments through the first diffusion
ablation. It does not claim a fresh proof audit of every Frontier stage, all remote
files, every old run, or all chat messages. Detailed old mixed-source README is
hash-indexed but not copied into the evidence bundle. Historical EA outputs are
excluded. Current snapshots contain full own solution words where present.

Staleness: read metadata and failure fields, not just a file named summary. A file
can be partial. Compare matching source/config/data/checkpoint hashes. A changed
source after training does not retroactively describe the trained checkpoint.
Interrupted v1/v2 policy prep and incomplete v3 scalar benchmarks are not completed
runs. Old v4 status saying action head absent refers only to that package/version.
