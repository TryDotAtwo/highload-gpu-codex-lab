# Claim ledger and evidence graph

Use one row per substantive claim. Keep the ledger with the deliverable, not necessarily in the main narrative.

| ID | Exact statement and quantifiers | Model/assumptions | Depends on | Evidence kind | Exact source/version | Verification performed | Open obligations | Permitted manuscript wording |
|---|---|---|---|---|---|---|---|---|
| C1 | Target is reachable at cost k | legal operations, arbitrary inputs | witness semantics | construction | witness/source hash | full target recomputed or not rerun | list any gaps | upper bound only |
| C2 | No legal candidate costs less than k | all cases covered | reduction, complete enumeration, sound pruning, run/certificate | computational exclusion | code + log/certificate hashes | describe exact checks | implementation/result bridge if open | scope to authenticated evidence |
| C3 | H implies exact minimum k | H stated literally | theorem dependencies | kernel-checked conditional theorem | module/toolchain + audit | build/audit seen or rerun | prove concrete H | conditional until H is discharged |

These rows are examples of distinct evidence roles, not evidence for any particular problem.

## Evidence types do not collapse

- Mathematical proof: inspect the actual argument, hypotheses, and coverage
- Recorded computation: state which program ran, when, how, and whether raw outputs are available; a report about a run is weaker than inspected raw evidence
- Computational certificate: give its format, provenance, checking algorithm, trust base, and whether an independent checker ran
- Algorithm correctness: specify successor completeness, pruning soundness, state identity/deduplication, termination, overflow/sentinel semantics, and extraction of the conclusion
- Formal proof: inspect exact theorem type, hypotheses, transitive axioms, admitted obligations, version/toolchain, and build/audit provenance
- Benchmark: bind a measurement to workload, system, configuration, repetitions, and units

A successful execution is not a proof of its implementation. A verified abstract model is not automatically a verified C++ program, standard library, compiler, or machine run. A hash authenticates byte identity; it does not establish mathematical correctness. Multiple runs of the same implementation are not an independent algorithm.

If a Lean theorem takes `regular`, `bound`, `frontiers`, `NoShortProgram`, or an equivalent premise, show the premise and its status wherever claiming the endpoint. Distinguish checked model lemmas from concrete data authentication, code refinement, and result transfer. Do not erase an open obligation with an axiom, `sorry`, a theorem name, a narrative claim, or a green diagram box.

## Required edges for a finite exclusion

Original candidate → valid normalized candidate → covered case → represented initial state → complete successors → sound filtering → faithful state storage/deduplication → terminal criterion → authenticated result → exclusion.

Label all assumptions on these edges. Explain how one candidate maps through the chain. Where only part is formalized, give separate endpoints for the manuscript's computer-assisted claim and its current formalization status.

## Counts and proof maps

Use text status labels as well as color; neither dashed borders nor color alone establish proof status. Explain edge direction and border meanings in the caption. A roadmap is an index to arguments, not a certificate. State whether numbers count layers, retained labels, generated candidates, distinct keys, unique objects, terminal records, or cases; do not interchange them.

For a finite search, record success conditions, exit code, completeness assumptions, interruptions, pruning/capping, sentinels, and exact bound. `No terminal found` differs from a terminal with a large sentinel cost. Partial runs and heuristic truncation cannot establish exhaustive exclusion without a separate proof.
