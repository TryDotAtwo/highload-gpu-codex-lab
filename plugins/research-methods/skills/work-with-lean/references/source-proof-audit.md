# Source-to-proof audit boundaries

Use this guide for substantial source formalization, finite certificates, or a review of reported proof coverage. Follow the project's actual target and trust policy. The examples illustrate failure mechanisms; their sizes and domain conventions are not universal requirements.

## 1. Audit the mathematical target before the proof engine

Write the proposition in notation with every quantified variable. Compare source, registry, final Lean theorem, and the definitions/helpers on which it depends. Check:

- domain and admissible parameters, including empty or boundary cases;
- a function of one state versus a relation on two states;
- action side, matrix multiplication order, coordinate labels, and terminal state;
- the equality being proved: full operator, prepared-input isometry, code subspace, or a quotient;
- total paid cost, including compilation, permutations and restoration when required;
- whether each premise is supplied by the source, part of a declared model, or still a proof obligation.

For example, word-length symmetry `length(M^-1) = length(M)` does not imply inversion is an isometry of a left-action word metric `d(A,B) = length(B*A^-1)`. In three-wire CNOT semantics, with rows encoded as low-bit-first masks, `A=[1,3,4]`, `B=[1,3,7]` have distances 1 and 2 after simultaneous inversion. The inverted relative matrix has rows `[1,2,7]`: two CNOTs implement it, while it is neither identity nor a single CNOT. This challenges the stronger interpretation, not the source's correct length statement. State the exact theorem in the registry and report a wording defect separately from a false proof.

A definition imposing a gate-by-gate protocol mask is a modeling premise. Preservation of a remote row/column is a consequence. Do not report the consequence as a derivation of the physical premise. A counterexample showing endpoint equality fails to enforce the mask is another distinct result.

When a helper assumes a desired property, trace who supplies that assumption in the final theorem. Conditional infrastructure is useful if its outstanding hypothesis remains explicit. Check that the accepted final result discharges it rather than silently treating it as established.

## 2. Measure the requested domain of a finite certificate

Before timing or expanding a pilot block, determine its mathematical domain. Count separately:

1. encoded objects examined;
2. objects belonging to the requested domain;
3. distinct required instances or transitions actually checked;
4. remaining required instances and how the blocks will cover them.

Inspect rank, reachability, boundary cases, sentinel/default values, and duplicate entries where applicable. A fast prefix can consist entirely of irrelevant or trivial cases. For packed 4-by-4 binary matrices whose low four bits encode row 0, integers 0..255 have two zero rows. Thus a 256-state pilot has no invertible matrix. If absent states receive distance label 255, all its row-addition checks can be `255 <= 255 + 1`. Those checks may be correct but contribute zero required GL(4,2) edges and are not a representative timing sample for that component.

Choose representatives from the actual domain, including cases that exercise the expensive reduction. If the source theorem concerns invertible/reachable states, a theorem on that explicitly stated domain is appropriate. Prove representation correspondence, transition closure and coverage. If an existing certificate lemma quantifies over a larger encoding space, either establish its extra cases by an invariant or use a correctly stated reachable-domain version. Never omit cases that the source theorem requires.

For an exact shortest-distance table, keep these obligations distinct:

- each stored word reaches its full labeled target with its literal paid length (upper bound);
- the potential is zero at the terminal and satisfies the step inequality on every relevant transition (lower bound);
- the encoding denotes the specified objects and transitions;
- the checked list covers the requested domain with the necessary distinctness;
- histogram, maximum, and target values follow from the certified table.

A correct generic soundness theorem does not discharge its table-specific hypotheses. Many witness blocks do not by themselves prove optimality or exhaustive coverage. A separate Python BFS is useful independent evidence for finding data errors; retain its evidence class and do not promote it to kernel acceptance.

## 3. Test the evidence gate as well as the proof

Distinguish a live verifier from standalone bookkeeping scripts. A live build and axiom audit may be sound while saved ledger evidence is weak. Identify exactly which component enforces each property before calling a result invalid.

For accepted historical evidence, retain command argv and exit codes for every required gate, stdout/stderr hashes, the exact declaration set, selected source/certificate/config hashes, toolchain/dependency pins, and runtime identity. For containers check actual source mounts, image identity and mounted dependency revisions; a host manifest and a mutable image tag do not alone identify the executed environment.

A hash of the log only binds the record to that log. It says nothing about which proof source produced it. A line such as `Build completed successfully` can precede a failed later gate. A nonempty path or status string is not proof evidence. If source files change during an audit, retain the checked snapshot and record drift before applying conclusions to live files. Avoid parallel builds or edits in another agent's active checkout.

Where the risk warrants it, use small negative checks on an isolated copy or in-memory fixture:

- replace an accepted record's evidence field with nonexistent/nonsensical evidence;
- change a proof source while keeping its old evidence;
- omit a required declaration or supply a failed gate's record;
- include a disallowed transitive axiom or malformed audit output.

An acceptance gate should reject cases within its advertised remit. If a provenance-only checker intentionally accepts them, document that limited remit and ensure the full acceptance path enforces the missing gate. Do not mutate the active project to test failures. Existing `scripts/lean_evidence.py` supports source/log binding; read its runtime limitations before relying on it.

## 4. Audit coverage and report evidence without inflation

Count current source records separately from historical versions and overlapping supplementary ledgers. Declaration counts, build job counts and line coverage are not counts of independent mathematical results. A source paragraph may contain multiple claims, corrections, examples or caveats; classifying every line does not prove the claim inventory exhaustive.

Keep partial declarations linked to their parent claim with the exact sub-obligation and evidence. Keep the central claim open until its full acceptance conditions hold. Record open research separately from implementation work and from source claims later refuted.

For each finding, give the file/theorem, mechanism, scope, reproducer or inspected evidence, requested correction, and validation limit. A registry wording mismatch, a weak evidence gate, a bad pilot domain, and an invalid Lean theorem are different defects. Recheck the live files before finalizing a review of an active project; acknowledge fixes made during the review.
