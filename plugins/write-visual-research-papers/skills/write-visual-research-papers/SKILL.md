---
name: write-visual-research-papers
description: Use when drafting, restructuring, editing, or reviewing scientific articles, proof-driven papers, computational certificates, HPC/GPU research, or LaTeX/Prism manuscripts that need rigorous visual explanations, explicit evidence boundaries, time-and-memory scaling, and publication-quality figure QA.
---

# Write Visual Research Papers

Make the result, exact model, assumptions, and strength of evidence clear immediately. Explain the argument with substantive diagrams, equations, tables, and compact prose beside the step they explain. Preserve technical depth; remove repetition rather than mathematical substance.

## Required workflow

1. Read [workflow.md](references/workflow.md). Inspect the actual source, data, code, proof artifacts, and approved examples before editing. Treat examples as presentation references, never as reusable results or fixed figure counts.
2. Build the claim ledger and dependency graph in [claim-ledger.md](references/claim-ledger.md). Draft only the strongest statement supported by the supplied evidence. Keep open premises visible in the abstract, statement, proof map, and conclusion.
3. State the full target and charged operations before reductions. Explain what each projection, quotient, normalization, or compressed representation preserves; prove the bridge back to the original model.
4. Organize the paper as result/model → construction or upper bound → reductions/lemmas → exhaustive or experimental evidence → limitations and reproducibility. Adapt this order when the mathematics requires a different dependency order.
5. Design figures alongside the argument. Give every scheme one precise explanatory job. Prefer native TikZ or SVG for mathematical geometry and exact labels. Use tables for comparisons and counts, equations for identities, diagrams for dependencies and transformations. Put each beside its first substantive explanation.
6. For algorithmic or HPC claims, apply [asymptotics.md](references/asymptotics.md): time AND memory, scaling variables, communication, imbalance, retained history, expected versus worst case, and measured versus modeled quantities.
7. Run [figure-qa.md](references/figure-qa.md) on EVERY figure separately at 100–150% of its final size, then inspect EVERY page of the final PDF. Compilation and a contact sheet do not satisfy visual QA. Fix and rerender defects before claiming readiness.
8. Follow [delivery.md](references/delivery.md). Bind the final source set, build, PDF, and attachments by hashes and version. Distinguish drafted, compiled, visually checked, saved, and published. Obtain publication approval separately from draft approval.

## Evidence boundaries

Use explicit statuses: mathematical proof; recorded computation; independently checked certificate; implementation-correctness proof; kernel-checked conditional theorem; kernel-checked unconditional theorem; conjecture/open obligation. One status does not imply another. A theorem of the form `H → P` proves the implication until `H` is discharged. A witness proves attainability, not minimality. A beam-pruned search cannot supply exhaustive exclusion without a separate coverage proof.

Never invent proof steps, source citations, benchmark numbers, affiliations, author contributions, or completed checks. Preserve missing evidence as a stated limitation. For Ivan Litvak, use `Independent Researcher` when preparing his author block unless he supplies a different current affiliation; derive all other author details from supplied sources.

## Deliverable contract

Deliver the manuscript and editable figure sources, source-bound evidence/claim ledger, reproducible build instructions, final PDF, and a concise QA record identifying any unresolved issues. Keep the scientific narrative readable on its own; move long code, exhaustive logs, and audit records to appendices or ancillary material, with exact references. Do not auto-publish or silently replace an approved artifact.
