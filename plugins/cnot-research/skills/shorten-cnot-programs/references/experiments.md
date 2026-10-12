# Evidence ledger — snapshot 2026-09-24

Numbers below belong to their own target files and protocols. Saved legacy
verification flags are not fresh independent rechecks. The plugin checker verifies
the newer comparison words; its report specifies exactly which. No multi-seed
large-matrix neural advantage has been established.

## Own compiler on nine original matrices

| Case | Stage17 no gradient | Stage17 gradient | Exact local basis + short windows | Wider commuting windows, NN = Hamming |
|---|---:|---:|---:|---:|
| hgp_13_1 |19|19|19|19|
| hgp_25_1 |45|41|41|41|
| hgp_34_10 |71|70|68|68|
| hgp_45_9 |93|93|93|93|
| hgp_58_16 |157|157|149|149|
| bb_72_12_6 |383|354|350|350|
| bb_90_8_10 |491|450|426|421|
| bb_108_8_10 |678|608|572|572|
| bb_144_12_12 |1194|1104|1060|1057|
| Sum |3131|2896|2778|2770|

Stage17 archived run:7.82s without /39.64s with gradient for all nine together.
Different compiler configurations, one run, not an equal-quality throughput claim.
New wider-window gain8 gates also obtained with Hamming on the same windows:
evidence for window collection, no isolated neural benefit. Only seven distinct
local target calls in that study. Matrix goals remain held out from neural training.

## Whole-matrix experiments in chronological order

1. Early full neural beam: saved record48298 examples/2300 positives/25epochs;
   NN20/45/72 vs H20/44/69 on13/25/34; BB72 unfinished under historical time cap.
   Not the present no-wall-time protocol.
2. Early scalar neural field: n25 model faileddepth200 vsH44. v2 also failed
   n34depth178 vsH69. Small fixed replay and weak constraints; do not resume these
   runs merely to acquire more epochs before checking label semantics.
3. v3 structured replay:640 updates; macro variants identical. n13=20; n25 failed
   depth120; n34 direct interrupted for batching. Partial benchmark, not a complete table.
4. v4 structured field:1280 updates each, seed1700; macro52 constraints inactive,
   zero winners, state dicts bitwise equal. NN20/51/74 vsH20/44/70, beam4depth120.
   NN2.151/32.193/152.722s vsH.035/.572/2.221s. Identical NN reused in second variant,
   not independently timed. Training approximately387/453s, one overlapped CPU work.
   Replay union9728 unique available states; validation337unique/391records due
   repeated n8 schedule. No direct overlap; neighbors can visit val without labels.
   Exact heldout neighbor selection30/31(n3),26/32(n4), not full-program optimality.
5. Own teacher policy v3: two640-update rounds, seed2700,12train goals,2324states,
   total~429.77s includingdata/selfsearch. Best checkpoint round2step560 chosen on
   validation. Train improvements14→11,13→12,58→55,48→47; not held-out wins.

| Case | Hamming | Policy head | Direct field | Head top32 + field |
|---|---:|---:|---:|---:|
| hgp_13_1 |20|22|22|22|
| hgp_25_1 |44|55|47|51|
| hgp_34_10 |70|101|depth_limit160|91|

Beam4depth160, no wall-time cutoff. Direct times2.181/32.529/356.527s;
head.619/1.625/3.386s; shortlist.950/3.329/9.399s. n25 direct improved over
v4(51→47), n34 regressed: no general gain. Top1 agreement with direct field
75/50/12.5/12.5%, top8 recall100/100/50/37.5% for n8/13/25/34 on eight states each.

## Random walks plus diffusion feature ablation

Same replay/validation/profiles, warm v4, seed2700, one640-update round. Independent
best selection; both step640. Heat-on total~215.34s, off158.37s; single runs.
Both improve four TRAIN goals after training; no second round trains on those gains.
Correction weight norms nonzero, so the tied lengths are not evidence of disconnected
features. Validation loss3.96699/3.96822 nearly same; metric is preference loss.

| Case | Hamming | Heat-off head | Heat-on head | On minus off |
|---|---:|---:|---:|---:|
| hgp_13_1 |20|21|21|0|
| hgp_25_1 |44|54|54|0|
| hgp_34_10 |70|102|102|0|
| hgp_58_16 |159|pending|234|pending|
| bb_72_12_6 |depth_limit480|pending|depth_limit480|pending|

Small depth160, H58depth240, BB72depth480; beam4. Heat-on H58head16.731s,H18.661s;
BB72head70.997s,H119.250s, neither solved. Small on.448/1.486/3.955s vs
off.251/.848/2.645s. Different words but equal small counts. No direct-field
large benchmark for these checkpoints. No time-cutoff claim: depth is finite.

At plugin preparation the heat-on large process finished (exit0); no owned
benchmark remains running. Main agent must check fresh process state before next launch.

## Test evidence already recorded in this conversation

- structured_field/test_contracts.py:10 passed.
- policy_iteration/test_contracts.py:2 passed.
- test_policy_shortlist.py:1 passed (full shortlist equivalence and goal ordering).
- test_diffusion_features.py:2 passed (fullGL3 projection comparison, rates,
  walk certificates, symmetry/padding, new gradients).

These are prior test executions, not automatically rerun when the plugin is read.
Plugin validation and independent JSON word checking have a separate fresh report
in `assets/evidence_check.json` after packaging. Use that scope when quoting evidence.
