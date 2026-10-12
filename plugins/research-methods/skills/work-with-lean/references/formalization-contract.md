# Source to theorem contract

For a long conversation or paper corpus, freeze/version the source scope. Record a stable claim ID, source SHA256, message/page locator, verbatim locator or concise exact statement, all quantifiers and hypotheses, conventions, Lean declarations, certificate inputs, and verification evidence. Track current claims and historical corrections separately; do not merge equal-looking IDs without reviewing their statements.

Useful statuses: unreviewed, specified, in_progress, kernel_verified, refuted, experiment_only, source_gap, superseded, open. Do not mark an infrastructure lemma as a completed source claim unless it proves that full claim.

Before accepting a result, review:

- Is the Lean conclusion the requested one with the same domain, labels, ordering, normalization and cost model?
- Do helper assumptions hide the desired conclusion, a missing general theorem, positivity, invertibility, or existence of a minimum?
- Are degenerate cases covered or explicitly excluded in the source: empty type/program, n=0/1/2, zero distance, zero denominator, minimum versus infimum?
- Did the proof preserve all operations whose costs the source counts? Basis changes, permutations, inverse steps, ancillas and state preparation are not free unless the original model says so.
- Does a finite certificate address the original full operator, a restricted action, or a reconstructed target? State the exact boundary.
- Are all accepted source declarations in the verified root and the axiom list? Is the list complete relative to the claim ledger?
- Do build and axiom evidence refer to the same source/config snapshot, and does that snapshot still match the files being reported?

## Exact computation without changing the claim

A Python search can discover a witness, counterexample, or gate list. It is not a Lean proof. Save exact integer/rational/bit data, regenerate deterministically, hash the source, and verify a proposition whose semantics are independently connected to the original model.

When function-valued matrix reduction is too large, a compact representation such as bit rows may help. First prove the conversion respects one operation and iteration. Then let the kernel check manageable row/chunk certificates. Cross-check the generator's transcription of source inputs; a Lean theorem about a wrongly transcribed matrix does not authenticate the source.

Never silently replace kernel checking with `native_decide` under a strict axiom contract. Increase heartbeats only when the proof strategy is sound and cost is understood. A source-specific reflection bridge is often more valuable than rerunning an OOM-prone whole-program reduction.

## Completion is about source scope

The report should distinguish newly closed independent claims, supporting declarations, retained source records, and open mathematical dependencies. A source hash check proves provenance consistency, not theorem truth. A successful build proves elaboration/kernel acceptance of its imports, not that every promised source result is present.

Prefer a current summary plus timestamped evidence/history. Do not append many contradictory paragraphs each labeled “latest”. Keep pending candidates visibly separate from trusted imports. Record false source claims with exact counterexamples, and preserve genuinely open research goals as open.
