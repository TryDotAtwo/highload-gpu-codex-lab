---
name: work-with-lean
description: Formalize mathematics in Lean 4, debug Lean/Mathlib proofs, verify exact finite certificates, and audit proof coverage and transitive axioms in existing local or Docker projects.
---

# Work with Lean

Preserve the requested mathematical statement and produce evidence that the pinned Lean kernel accepts its proof. For a narrow proof edit, use the proof loop below. For a large source corpus, also use the claim contract. This skill does not authorize installing/upgrading Lean, restarting Docker, changing resource limits, deleting data, or delegating work.

## Establish the real boundary

- Read the actual `lean-toolchain`, Lake config/manifest, root imports, verification command, and relevant project instructions. Use the existing runtime and dependency revisions. Do not upgrade to make a proof easier.
- Determine where `.lake`, source bind mounts, toolchains, caches, and Docker data actually live. Windows host paths and container paths are different. A named volume can hide the host `.lake` directory.
- Check current source and process state after interruption; inherited history is a locator, not proof that a job stopped. Do not launch another expensive check when the original is still live.
- Keep unrelated active work intact. In a side conversation, review read-only until the user requests the particular mutation.

## Preserve mathematical scope

For source-based formalization, record source locator/hash/message or page ID, exact statement and quantifiers, hypotheses, edge cases, conventions, and the intended declarations. Trace assumptions through helpers. A statement is not closed by assuming its conclusion, restricting its domain silently, or using a numeric experiment for a quantified theorem.

- Separate statement correspondence, Lean acceptance, and source authenticity. Lean proves the proposition that was written; human review must check it is the proposition requested.
- Keep open research, false claims, missing sources, experiments, intermediate infrastructure, and verified source claims distinct. A counterexample must refute the original quantified statement with matching semantics.
- Do not add `sorry`, `admit`, `sorryAx`, or new axioms to trusted proofs. If experiments temporarily use placeholders, isolate them outside root imports and accepted evidence; never promote or report them as proved.
- For strict kernel checking, inspect the transitive axioms. `native_decide` and native reduction may introduce trust such as `Lean.ofReduceBool`; do not substitute them silently for kernel reduction.
- Read [formalization-contract.md](references/formalization-contract.md) for large corpora and exact finite computations.

## Proof loop

1. Read the installed Mathlib definition and nearby lemmas before guessing a name or shape. Use `rg` in the runtime that actually contains dependencies. Batch independent searches; do not scan the whole library when a module is known.
2. Write a small probe in an explicitly temporary directory. Use `#check`, `#print`, and `#synth` for uncertain declarations, constructors, instances, and imports. Do not treat a probe as a completed source theorem.
3. Compile the changed module with the project launcher, preserving its exit code and complete diagnostics. Group tightly related lemmas into a coherent module; avoid a full build and final report after every trivial lemma.
4. Debug from the exact goal and first causal error. Read [lean-debugging.md](references/lean-debugging.md) for concrete failures observed in the audit. If a tactic variant leaves the same goal, change the diagnosis: inspect reduction, types, binders, or the induction invariant instead of cycling through broad `simp` calls.
5. After the module passes, connect its intended declarations to root imports, the source ledger if applicable, and the axiom audit. Run the required full target and audit once per integrated milestone; repeat when code changes or a concrete risk requires it.
6. If the source changes during or after a check, that check is evidence for the recorded snapshot only. Never attribute it to a newer snapshot.

## Resources and long computations

Search for an existing general theorem before reproving library mathematics. Distinguish qualitative generation/existence from constructive algorithms and quantitative cost bounds. A Mathlib decomposition may prove reachability without proving the claimed Gaussian gate bound.

For large finite checks, prove a correspondence between the efficient representation and the original semantics, then use manageable certificates. Estimate cost on a representative case. Chunk a proof around reusable invariants, not just arbitrary syntax if each chunk still unfolds the whole computation. Do not respond to repeated OOM/heartbeat failures by increasing every limit or starting parallel copies. See [runtime-and-evidence.md](references/runtime-and-evidence.md).

## Acceptance and reporting

- Preserve raw logs, command argv, exit code, source hashes, toolchain and dependency pins, and the exact declaration list. Prefer the project's established verifier; use the supplied evidence helper to close missing provenance, not to replace mathematical review.
- The helper [lean_evidence.py](scripts/lean_evidence.py) can record a command and validate build/axiom evidence. It runs only the command explicitly supplied. Its `audit` mode checks saved evidence without invoking Lean or Docker. Read the command examples and limitations in [runtime-and-evidence.md](references/runtime-and-evidence.md).
- Audit every declaration needed by accepted claims. The default allowed set is `propext`, `Classical.choice`, `Quot.sound`. Stricter project requirements take precedence. Any different trust model must be explicit, not silently allowed by the parser.
- Report the mathematical milestone, source claims newly closed/refuted, remaining obligations, and validation boundary. Lake's job count includes dependencies and is not a proof count, coverage percentage, performance result, or full clean rebuild count.
- Counts of historical records are not counts of independent mathematical results. Coverage reporting is bookkeeping; it cannot determine whether a source claim was faithfully translated.

For why these rules exist, see the bounded case study [agent-audit.md](references/agent-audit.md). Do not copy that project's paths, limits, or domain conventions into unrelated projects.

## Sustained source-formalization workflow (2026-09-24)

For a sustained source-formalization task, organize work around a named source theorem and its full acceptance conditions. Write the intended final proposition and the missing dependency chain before choosing helper lemmas. Each helper should remove a named gap in that chain. Do not select easy lemmas merely to produce another passing turn.

- Continue through a coherent mathematical milestone when execution remains available. A completed helper is progress, but is not by itself a reason to end an otherwise productive turn. If interrupted or genuinely blocked, preserve the exact remaining goal and working state; never weaken the source statement to manufacture a milestone.
- Compile changed modules during the proof loop. Run all project-required gates at the required boundaries; otherwise integrate related changes before the full build. Do not repeatedly run an unchanged full verifier merely to support a new progress report.
- Keep the source claim open while its central theorem is incomplete, and still link every verified partial result to its source claim: exact sub-obligation, declaration, hypotheses, snapshot/build evidence, and transitive-axiom evidence. Use an existing partial-results field or a linked companion record if the ledger schema cannot represent partial verification. Do not leave successful partial proofs discoverable only through a prose diary, and do not promote the parent claim prematurely.
- Maintain one current-status summary. Move superseded statements into dated history; do not append mutually contradictory present-tense status paragraphs. Distinguish a last passing snapshot from newer unverified edits.
- Coverage counters and exclusion counts must be computed from the classified records with enforceable checks. A literal zero, a configured policy, or a successful provenance hash check does not prove that excluded material is absent from accepted claims. Report unknown when the check does not establish the claimed property.
- For explicitly requested skills, read their actual applicable instructions once and retain a compact application note across continuation: which rule informed which decision and which artifact demonstrates it. Reading, announcing, and applying are different facts. Re-read changed instructions when notified; do not reload unchanged skills on every tiny proof step.

## Audit finite certificates and source correspondence

For a source-to-proof audit, a large finite certificate, or a progress claim based on checked chunks, read [source-proof-audit.md](references/source-proof-audit.md). It covers relevant-domain coverage, sentinel cases, one-point versus two-point metric statements, modeling premises, and negative checks of evidence gates. Apply the relevant checks; a routine local lemma does not require a new audit framework.

Before counting a chunk as progress, identify which requested instances it covers. Before trusting a saved build, establish which source snapshot and runtime it checked. Use the existing evidence helper when those records are missing; a log hash alone cannot bind a theorem to its source.
