---
name: superposition-planning
description: Use when the user requests Superposition Planning, Суперпозиция решений, or recursive alternatives-first planning with user-confirmed criteria, options, and selection. Do not trigger for ordinary scientific questions or routine execution.
---

# Superposition Planning

Plan a decision tree through three separate phases at every scope. This is a planning aid, not a truth test. Use the user's language, stable path IDs (`[1]`, `[1.1]`, `[1.1.1]`), and the following state contract. Read [the worked example](references/example.md) when a nested transition needs clarification.

## State and response contract

Track each node's scope, parent, phase, confirmed criteria, live options, chosen option, children, and confirmation status. A selection can be provisional; a node is resolved only after its COLLAPSE is confirmed and all children are resolved. Preserve completed decisions separately.

Every protocol response contains, in order:
1. Current path and phase, in the user's language
2. Only that phase's content and one appropriate question
3. Full unresolved tree at every depth, with ancestor context and the current node marked

Show every unresolved sibling and descendant, including a node awaiting confirmation. Resolved nodes may be omitted or shown as resolved context; never silently drop pending branches. Announce pending siblings when starting a new scope, not during revisions. If there are none, say so explicitly. If state is missing, reconstruct from available conversation or ask; never invent past approvals.

## Three phases

| Phase | Output and required transition |
|---|---|
| CRITERIA | Propose evaluation axes, reasons, direction of preference, and hard constraints. Ask the user to confirm. On edits, show the revised criteria and ask again; edits are not confirmation. |
| OPTIONS | After criteria confirmation, present **at least three substantively different feasible paths**, more when the decision space warrants. Evaluate each against every confirmed criterion, explain trade-offs, and give a compact comparison. Ask the user to choose. |
| COLLAPSE | After an unambiguous choice, record it and decide whether this is an actionable leaf or needs child decisions. Show proposed children if needed. Ask for explicit confirmation to proceed; stop. |

Never combine phases, begin the next scope inside COLLAPSE, or emit the merged plan before the final COLLAPSE is confirmed. A deadline or request to “do everything now” does not replace the phase confirmations. Ask whether the user wants to leave this protocol if they explicitly request a conflicting workflow; do not silently reinterpret its gates. “Proceed” advances only the pending gate. An ambiguous option response requires clarification in OPTIONS, not an inferred selection.

## Real alternatives and honest comparison

Three is a minimum, not a cap. Renamings and cosmetic parameter changes are not distinct paths. If the fixed domain genuinely has fewer than three possibilities, state the incompatibility and ask for permission to broaden it or an explicit exception. Do not invent a third choice or silently take the exception.

Use measured values with sources where available. Label unsupported numeric scores as subjective expert estimates; use qualitative comparisons or “unknown” when evidence is missing. State the score direction and uncertainty. Do not invent measurements, availability, vendors, or precise confidence. Do not aggregate axes without confirmed weights. A recommendation is not a user selection.

## Recursion, closure, and refinement

A leaf has no unresolved choice material to direct execution. Otherwise add stable child IDs and keep the parent unresolved. After COLLAPSE confirmation, start the next pending node's CRITERIA in a new response, normally depth-first or at the user's named pending node. Confirmed parents resolve only when their descendants do.

When all nodes are confirmed and resolved, produce one merged execution plan linking steps to decisions, ordering dependencies and identifying remaining operational prerequisites. Include the empty unresolved tree. Ask whether any step needs refinement. Reopen step 3 as `[1.R3]` (use a fresh suffix on repeated refinements), begin CRITERIA, preserve unrelated decisions, and revalidate affected dependencies before issuing the updated plan.

Planning approval is not authorization to execute, purchase, publish, book, install, or change access. An “execute” request ends planning and enters the separately authorized execution workflow; obtain any missing action-specific approval. Never claim an action occurred because it appeared in the plan.
