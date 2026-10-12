# Reviewing the claim behind a formal proof

Use this reference when a source claim, a registry entry, and a formal theorem are being compared. It supplements the language-specific logical-review instructions; it does not make Lean kernel acceptance a substitute for reading the intended proposition.

## Normalize the proposition

Write the source and theorem in explicit notation before judging equivalence. List all quantified variables, domains, premises, action sides, equality notions and cost conventions. A singular noun in prose can conceal extra quantifiers. For example, invariance of `length(M)` under inversion is not invariance of `d(A,B)` under simultaneous inversion. The latter requires a separate argument and can be false for a word metric. Correct the registry to the source's actual claim; do not describe an accurate weaker source result as refuted by a counterexample to an invented stronger result.

Distinguish three roles for statements: a model definition, an assumed constraint, and a derived proposition. Defining allowed circuits to avoid a remote wire does not prove why the wire is physically inaccessible. A theorem about every allowed circuit can prove an invariant under that explicit premise. An endpoint-equality counterexample addresses a different implication: final equality need not enforce intermediate legality.

## Trace conditional arguments to their use

A shortest-path certificate theorem may assume a local potential inequality. It proves a valid implication; an exact-distance claim additionally needs every required inequality, a terminal value, a reaching witness and the semantic/coverage bridge. Check the final application supplies them. Do not flag a conditional helper as circular merely because the condition is unfinished; keep the corresponding source claim open.

Look for vacuous or irrelevant coverage. If a finite checker runs over encodings, verify which encodings denote the source's mathematical domain. Rank-deficient matrices, unreachable states, empty fibers, sentinels and repeated records can inflate counts while proving no requested instance. Counts and progress reports should expose this distinction. A pilot outside the domain gives no basis for predicting proof cost inside it.

## Classify the finding precisely

- Source correspondence defect: the proved proposition and the intended proposition differ.
- Modeling boundary: a declared assumption is being described as a derived fact.
- Incomplete proof chain: a necessary hypothesis or bridge has not yet been discharged.
- Evidence defect: saved build/axiom records do not establish the claimed snapshot or gate outcome.
- Coverage defect: checked records or instances do not establish the claimed domain coverage.

These findings can coexist with correct Lean proofs. Support each with a concrete example or dependency chain. Separate observed defects from remaining unknowns. Read a checker before treating its status as evidence, and recheck changing files before reporting an old defect as current.
