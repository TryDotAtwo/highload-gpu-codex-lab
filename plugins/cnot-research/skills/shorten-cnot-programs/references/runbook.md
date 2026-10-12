# Commands and operational checks

All project commands below run from `synthesis-methods/01_shared_basis_stage17/improved`.
Plugin checker instead takes `--project <absolute project root>`. Do not execute
training merely because a command is listed; follow the active user task/plan.

## Read-only audit

```powershell
python <plugin-root>/scripts/check_evidence.py --project <project-root>
Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Select-Object ProcessId,CommandLine
```

Check current running commands before launching; one owned GPU workload at a time.
The old heat-on large benchmark finished exit0 at plugin preparation. Main must
refresh that observation. No checkpoint unpickling is needed for the JSON checker.

## Targeted mathematical tests

```powershell
python -m pytest structured_field/test_contracts.py policy_iteration/test_contracts.py test_policy_shortlist.py test_diffusion_features.py -q
```

Run the affected subset after an edit; broaden only for a concrete integration risk.
These tests validate contracts, not a neural shortening claim. Run tests without
competing with a timed GPU benchmark, and report if timing was contaminated.

## Pending measurement before new training

```powershell
python benchmark_policy_large.py policy_iteration/runs/walk_heat_off_v1/best.pt policy_iteration/runs/walk_heat_off_v1/large.json
python report_diffusion_ablation.py
```

The reporter currently assumes matching case sets and will KeyError if on contains
large cases and off does not. Either finish off first, or change reporting to show
explicit pending cells; never drop a failed case to make tables align.

## Reproduce established protocols in NEW directories

```powershell
python -m policy_iteration.train policy_iteration/runs/NEW_OWN_POLICY structured_field/runs/replay_basis_seed1700_v4/last.pt --steps 640 --rounds 2
python -m policy_iteration.benchmark policy_iteration/runs/NEW_OWN_POLICY/best.pt policy_iteration/runs/NEW_OWN_POLICY/comparison.json --direct
python train_diffusion_policy.py policy_iteration/runs/NEW_HEAT_ON --diffusion --steps 640
python train_diffusion_policy.py policy_iteration/runs/NEW_HEAT_OFF --steps 640
python benchmark_diffusion_policy.py policy_iteration/runs/NEW_HEAT_ON/best.pt policy_iteration/runs/NEW_HEAT_ON/comparison.json
python benchmark_diffusion_policy.py policy_iteration/runs/NEW_HEAT_OFF/best.pt policy_iteration/runs/NEW_HEAT_OFF/comparison.json
```

Current diffusion wrapper has fixed teacher directory, seed2700, warm v4 and one
round. Merely passing more steps is NOT the multi-round design in the new plan.
Add explicit seed/round/data/config/resume plumbing before claiming a proper sweep.
Legacy exact compiler and defect helpers may carry wall-time budgets; inspect them
before reusing inside a newly promised no-time-cutoff pipeline.

## Result record

Every run needs source/config/data hash, seed, warm checkpoint, architecture,
sizes/curriculum, actual updates, replay refresh, losses/active constraints,
validation selection rule, final checkpoint, end reason, wall times, peak memory,
complete encoder gates, target hash and independent verification. Failure count is
null with a reason, not zero or an omitted table row. Report median/spread only
after actual repeated independent measurements.

For comparison tables keep separate columns: own compiler incumbent, Hamming beam,
direct V beam, action-cost beam, proposal+rerank beam, feature ablation. External
article counts require a permitted independently sourced SAME matrix; code names
alone are insufficient. No archive-derived data may enter the new training.
