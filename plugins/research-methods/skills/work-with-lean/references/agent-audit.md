# Case study: observed Lean agent workflow

Review date: 2026-09-23. Scope: the inherited visible agent/tool transcript and read-only snapshots of `D:\Lean4\QuantumGraph` plus the active candidate in the conversation workspace. No new Lean/Docker execution was performed in this review, and the main project was not edited. This is a bounded review, not a retrospective audit of all reported 703k tokens or the entire Frontier source corpus. Current files may advance concurrently in the main task.

## Confirmed failures and their consequences

| Observation | Evidence | Action distilled into the plugin |
|---|---|---|
| Guessed Mathlib API | `Matrix.transvection_apply` was unknown; definition was actually `1 + Matrix.single ...`. `Matrix.isUnit_iff_isUnit_det` needed its import. | Search installed source and probe signatures before implementation. |
| Confused data and propositions | Candidate used `theorem programWalk` with result `Walk ... : Type`; Lean rejected it. | Check result sort; use `def` for data construction. |
| Guessed typeclass/structure shape | Missing `Field (ZMod 2)` import, `intro` attempted on `Std.Symm`, calling `loopless` as a function. | `#synth`/`#print` plus nearby examples in the pinned version. |
| Repeated broad tactic retries | `simp` left dependent `Walk.copy`/length goals; opaque `have hwalk` hid a term; an existential hypothesis was used after destructuring. | Inspect local context and reduction; explicit transport/length invariants and small reduction proofs. |
| Expensive decision proofs overloaded runtime | Historical status records report 10.6 GiB use and Docker hangs; a subsequent snapshot showed five Lean containers alongside services. This does not prove all five were abandoned or establish one exclusive crash cause. | Budget aggregate resources; inspect liveness before duplication; prove compact-representation semantics and use bounded certificates. |
| Per-lemma full integration churn | Visible turns repeatedly added one or two lemmas, ran full target+audit, and produced a final status. | Integrate coherent mathematical milestones, targeted compile during iteration, full gates when required at integration. |
| Axiom parser originally rejected a valid empty dependency set | `swapProgram_length` printed `does not depend on any axioms`, while regex initially handled only a list. | Parse both forms and test missing/extra/multiline/unsafe results. |
| Logs were often truncated in tool responses | `Select-Object -Last` and low output budgets still emitted truncated audit output; raw persistent log identity was not shown. | Save full logs and codes; show a compact result backed by saved evidence. |
| Evidence strings were not source-bound | Ledger entries used strings such as `verify.ps1 passed ...; Lake ... jobs`; the checker tested their presence, not matching build/source hashes. | Bind build/audit to an explicit input snapshot and required declaration list. |
| One module's successful build was repeatedly foregrounded while coverage stayed flat | Reports progressed from 70 to 86 audited declarations while 428 source records remained 8 verified, 7 refuted, 63 specified, 350 unreviewed. Some records repeat historical claims. | Report mathematical milestones and source coverage separately from dependency job counts. |
| PowerShell escaping corrupted documentation | Read-only status snapshot contained U+001B before `xactCost_paid_inverse` and U+000B before `erify.ps1`; inherited command used Markdown backticks inside a double-quoted PS string. | Literal structured writing plus readback/control-character validation. |
| Stale append-only status | Earlier “latest” sections remained after GL generation and Cayley results were added. | Maintain a current summary with dated evidence history. |

The pending graph-distance candidate had advanced in the live files beyond the last inherited error output. This review does not claim its current proof is still broken or already accepted; that belongs to the main task's current compile evidence.

## Practices worth retaining

- Full labeled F₂ semantics, chronological multiplication order, and paid inverse/swap steps were represented explicitly.
- False historical pure-CNOT operator claims were refuted with exact entries; prepared-state/isometry claims were not silently equated with full operators.
- Python recomputation was identified as discovery/triage until Lean certificates were available.
- A compact BitVec semantics bridge was proved before using efficient row certificates.
- Pending candidates were kept outside trusted imports until compilation succeeded.
- Source hashes, message IDs, historical records, explicit hypotheses, and open research boundaries were retained.
- Transitive axiom allowlisting and generation of the required audit set from accepted claims improved the gate.
- Mathlib's existing diagonal/transvection induction eventually replaced the need to rebuild qualitative GL generation from scratch. Quantitative gate bounds remained explicitly open.
- Live Docker checks distinguished sandbox access failure from engine failure; timestamps showed a prior socket crash followed by successful startup, avoiding an unnecessary restart.

## What this plugin changes

It packages precise error diagnosis, scope/provenance discipline, runtime restraint, and executable evidence checks. It does not repair the main formalization or claim that these instructions have already accelerated future Lean work. Script tests establish helper behavior; a future real Lean task is needed to measure behavioral improvement.
