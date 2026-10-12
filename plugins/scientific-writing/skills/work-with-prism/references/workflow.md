# Source-bound project workflow

## Minimum receipt

Keep a concise evidence record outside the manuscript with:
- Project URL/title and observed session date; actual model/reasoning labels
- Requested task, allowed editing boundary, frozen baseline identifier
- Input paths, bytes, SHA-256; request and final response artifact identities
- How the input reached the project/assistant, and what source identification was actually confirmed
- Reviewed snapshot, accepted/rejected suggestions and their reasons
- Final source snapshot, checked diff, and new material not covered by the previous review
- Save/readback status, build source identity, PDF hash if retrieved, actual figure/page QA scope
- Unresolved scientific, editorial, access, export, and reader-feedback limitations

Use tool observations and saved artifacts. An assistant's claim that it read a file is reported evidence, not an independent proof that its reasoning is correct. A local hash identifies bytes; it does not establish that remote bytes matched. Readback or a retrieved export provides the comparison.

## Request shape

Give the project assistant the reader/purpose, exact source filenames and version identifiers, requested operation, and invariants to preserve. Ask for a complete reading first, then separate clarity findings from claim/condition checks. Request actionable changes tied to passages. State whether the agent should propose edits only or modify files within an approved scope. Do not turn an editorial map or a PASS count into proof that a reader understands the text.

## Integrate without surrendering ownership

Work chapter by chapter and section by section. Reuse the authorized existing project rather than duplicating the entire baseline. Keep approved sources frozen and create the next candidate. Resolve disagreements against evidence, not majority vote. The authoring agent remains responsible for scientific assertions, logical qualifiers, prose, figures, and delivery.

If Prism reviewed A and integration produced B, report “Prism reviewed A; the coordinator checked the A→B diff” only when true. If B adds a new argument or substantially rewritten passage, supply that changed content and relevant context for a new version-bound review before calling B fully Prism-reviewed. Tiny accepted mechanical edits can be covered by a recorded diff check, but not described as a second Prism reading.

## Build and visual QA

A saved project, an assistant-reported build, a live preview, and an exported PDF are separate evidence. A local build of retrieved sources is a local artifact; it may differ byte-for-byte from the remote PDF. Preserve both identities when available. If export fails, report that boundary instead of assigning the remote QA status to the local PDF. Once the real Prism assistant has completed the required work on the relevant source version, a source-bound local build and independent local QA may provide the final PDF; a remotely generated PDF is not mandatory unless the user requested it. If Prism never worked on the source, local compilation cannot replace that missing stage.

Check changed diagrams individually at 100–150% of final size: geometry, labels, clipping, source correctness, caption role, contrast, and argument correspondence. At final delivery inspect every page, including page breaks, equations, citations, tables, and figure placement. A compilation success or contact sheet alone is not complete visual QA. Apply the companion research-paper skill's evidence ledger for proof/experimental claims.

## Failure handling

Keep the last good source snapshot. Classify whether a failure is authorization, unavailable feature/model, transient browser state, compilation, or export. Correct a known recoverable cause only within authorization; retry only with a reason to expect a changed result. Stop dependent work when no authorized recovery remains. Request the smallest missing access/action and continue safe local preparation separately. Do not create another identity, switch browser routes to evade denial, accept unexpected permissions, or repeatedly upload duplicate projects.
