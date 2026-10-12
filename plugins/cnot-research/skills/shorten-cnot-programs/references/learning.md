# Whole-matrix learning: architecture, signal and failure modes

## Structural field v4

Six structural blocks; wire width128, ordered-pair width32, four attention heads,
FFN256, 1,523,577 parameters in the scalar model. Inputs include complete M/M^T,
diagonal, row/column weights and overlaps. Shared wire/pair operations give scalar
invariance under simultaneous relabeling; padded and unpadded outputs are tested.
Do not substitute a move classifier for this scalar V_theta(M).

Legacy output LB+softplus(raw) saturated the correction to zero near the LB and
starved gradients. v4 uses softplus(raw+LB), exact terminal zero and bound losses.
This is not a hard LB guarantee: measure violations. Pack row bits contiguously
on CPU with np.unpackbits, transfer one batch to GPU; old per-bit writes were costly.

Replay uses small exact BFS, forest exact states, own walks, paid macro trajectories,
refreshing pools. Models train over selected states and all their local neighbors.
Store optimizer, CPU/GPU RNG, sampler state, configuration and source hashes;
resume into the same mathematical experiment. Preserve last and independently
selected best; do not pick checkpoints by the benchmark you report.

Paid macro losses in the completed v4 experiment were inactive (52 constraints,
zero winners/hinge violations). With/without macro variants ended bitwise equal.
Both variants already contained basis-derived training states. Thus this ablation
tested macro constraints, not the existence of all basis information in training.
Do not increase their weight and call it a useful gradient without measuring activity.

## Own-program imitation and action head

`policy_iteration/data.py` composes 2–4 own paid shears, compiles original/transpose/
inverse/relabel variants, verifies words and stores shortest known certificates
per (state, first action), plus suffixes. Preference soft labels proportional to
exp(-(known_length-min_known)/4) describe the current teacher portfolio. An unseen
action is not thereby known bad. Partial-teacher bias must be measured.

`ActionField` reuses final wire/pair states. Shared MLP on (h_c,h_t,z_ct,z_tc)
predicts all ordered CNOT costs, masks diagonal/padding. Current head Q=V+delta
mixes preference learning and centered field distillation. Centering alone does
not identify state-dependent offsets: a cross-parent beam compares candidates
from different parents, so calibration matters. This is a concrete next-audit risk,
not yet a demonstrated sole cause of failures. Separate calibrated costs and
proposal logits in the next implementation; see plan.

Training v3: warm start v4; two rounds640, seed2700; Bellman every4 updates rotates
n8/13/25/34, full selected-branch gradients; detached centered-Q distillation every16
(auxiliary weight.1). Verified shorter train solutions enter replay after each round.
Held-out targets never enter teacher improvement. v1/v2 prep runs were interrupted
before training; first complete run is v3. A one-round run's final improved teacher
programs have not trained its already finished model.

Direct full-field search pays n(n-1) successor field evaluations per parent.
One-pass head is much faster but is a different approximate ranking. Its old
top8 recall of the field's best action at n34 was only37.5% on eight states. That
tiny diagnostic is not a general estimate; use a larger independent panel.
`policy_shortlist.py` reranks head top32 via direct field: an explicit approximation,
not an all-neighbor field search. Measure recall and field regret, and provide
full-evaluation fallback when the chosen approximation is unreliable.

## Search and engineering lessons

- Check identity among successors BEFORE pruning by heuristic or per-parent cap.
- Filter closed candidates before cap, deduplicate within the new layer, and do
  not mark states closed if they were discarded. Track depth/path cost correctly.
- Compare full words and failure reasons at equal width/depth; separately compare
  equal compute budgets. Width equality is not equality of model evaluation cost.
- A paid macro consumes its expanded CNOT count, not one cheap synthetic edge.
- Complete rollback/resume metadata and output after each benchmark case prevents
  partial/interrupted runs from looking like completed tables.
- First optimize batch inference/packing/host sync, then consider custom kernels
  after profiling. Pair storage scales n² and full successor scanning multiplies it.
- Test symmetry, padding, terminal boundary, gradient equivalence and word orientation.
  Tests mirroring tensor code without checking mathematical behavior are insufficient.

## Stale documents

`STRUCTURED_FIELD_STATUS_RU.md` and `structured_field/README.md` describe v4 and say
action head is absent. That was true for v4. New `policy_iteration` adds it separately.
Use run/package-qualified statements. v4's old baseline HGP34=70 is stage17-gradient,
whereas the later exact-basis incumbent is68. Never merge those columns.
