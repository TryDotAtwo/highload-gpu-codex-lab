# Evidence status and discriminating tests

## Evidence status belongs to claims

Always distinguish the decisive claims, rather than applying one flattering status to the whole project. Use compact labels in ordinary language or the following vocabulary:

| Status | What it licenses | What to retain |
|---|---|---|
| proved / derivation checked | A conclusion follows under stated assumptions | The exact statement, assumptions, proof/checker and limits of the verification |
| finite checked | Enumerated or tested instances passed | Range, completeness, exactness, verifier, and any search exclusions |
| empirically supported | A claim has support under a specified design | Data origin, regime, uncertainty, alternatives and controls |
| contradicted / counterexample | A specific implication fails in the checked scope | Exact violated claim and the validity of the counterexample or measurement |
| conjectural | A proposed property remains unestablished | Supporting clues and the missing implication |
| heuristic preference | Taste, familiarity, simplicity, or an expected payoff guided attention | The property admired, with no promotion to proof or data |
| unknown / unassessed | The evidence is absent, inaccessible, or not yet inspected | What is needed to settle it |

Attach provenance as needed: **supplied/reported**, **inspected**, **reproduced**, or **independently checked**. For example: “evidence_status: reported finite checks through n=8; tree theorem reported proved; general claim conjectural; induction step unverified.” Supplied scenario facts are not experiments you performed. A planned check remains planned.

“Proved” is not a universal blessing. A formally verified theorem may have the wrong specification, an unfulfilled hypothesis, or a trust-boundary gap. An empirical model may predict accurately without identifying its physical mechanism.

## Proof and counterexample

Write the exact quantifiers and dependencies. In H ⇒ P, the proof of the implication does not establish H. A proof for a subclass does not establish the general case without a justified transfer.

For a suspect bridge, look for the smallest instance where its assumptions break: an articulation point after deletion, a degenerate parameter, a singular limit, a boundary condition, or an omitted orbit. First establish whether this refutes the theorem, only the proof step, or only the implementation.

For computational work, separate generator, certificate, checker, exhaustive coverage, and connection to the intended proposition. A small independent checker can establish a certificate while the generator remains opaque. A list of successful search results is not automatically a complete search or a universal proof.

## Empirical falsification

A failed prediction implicates the hypothesis together with auxiliary assumptions, calibration, and design. Test plausible shared artifacts when they could explain the result; do not indefinitely demand unspecified confounds to protect a favorite model. A constrained repair must make new risky predictions and disclose its extra assumptions. Independent fitted constants for every observation can remove predictive content.

An alternative fitting better does not uniquely establish it. Consider third mechanisms, nuisance effects, and observationally equivalent parameterizations. State whether the goal is accurate prediction, discrimination among a fixed candidate set, or causal/mechanistic identification; the same evidence can be sufficient for one and insufficient for another.

## Design the discriminator

A useful plan specifies:
- the alternatives and their different predicted observations or proof consequences
- the measurement, instance, intervention, or artifact that exposes that difference
- noise, nuisance, selection, and scope conditions under which the difference is detectable
- outcome branches: which claim is weakened, what remains unresolved, and what work follows

Possible designs include a minimal counterexample, boundary case, invariant check, negative control, perturbation, intervention, ablation, matched baseline, held-out data, alternative implementation, or an exact resource lower bound. Select by the question, not by dramatic presentation.

Structural equivalence is stronger than low statistical power. If the candidates predict exactly the same observable, improved precision or more of that observable cannot separate them. Change the observable or the scientific claim. Near-equivalence may instead require a calibrated power or sensitivity analysis.

## What “independent” means here

Identify the actual source of separation:
- logical: different lemma or checker, without reusing the disputed inference
- statistical: genuinely held-out units, avoiding leakage and dependent pseudo-replication
- instrumental: different measurement channel, with shared confounds considered
- implementation: distinct implementation/specification audits, not merely rerunning the same binary
- social: review without the desired answer, while recognizing shared assumptions

Do not infer independence merely from two agent names, two libraries, two machines, or two plots. If independence cannot be established, retain the evidence with a narrower description.
