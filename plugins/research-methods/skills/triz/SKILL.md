---
name: triz
description: Resolve difficult software engineering contradictions with TRIZ while preserving evidence-first coding, implementation, and verification. Use for architecture, performance, reliability, security, API, data, deployment, or UX problems where improving one requirement worsens another, one component needs opposite properties, the team is stuck in a trade-off, or the user asks for TRIZ/ТРИЗ, an ideal final result, inventive principles, or решение противоречия. Do not use for routine bugs, standard refactors, simple optimization, ordinary prioritization, or questions settled by measurement or a known pattern. Keep skill-loading mechanics out of the user-facing result unless they block the task.
---

# Solve Software Contradictions with TRIZ

Use TRIZ as a temporary engineering lens. Preserve the normal agent workflow: inspect the repository, ground claims in evidence, make scoped changes only when authorized, and verify the result.

Match the user's language. Keep TRIZ terminology subordinate to concrete engineering details.

## Choose Depth

- Use a quick pass for one well-defined contradiction: gate, contradiction, ideal final result, separation, recommendation, experiment.
- Use a deep pass when the system boundary or causal mechanism is unclear, several contradictions interact, or implementation is requested. Read [core-method.md](references/core-method.md).
- Skip TRIZ when the gate fails. Continue with debugging, measurement, a standard pattern, or ordinary decision analysis.

## Pass the Gate

1. Inspect available code, tests, logs, metrics, requirements, and prior decisions before generating ideas.
2. Write the candidate causal conflict:

   If we change [action or parameter] to improve [metric or benefit] under [condition], then [mechanism] worsens [metric or harm].

3. Verify that the same intervention causes both effects. A pair of desired qualities alone is not a contradiction.
4. Check whether a cheap measurement, an obvious defect fix, or a known pattern already settles the problem.
5. If the gate fails, use the more direct method. Do not manufacture a TRIZ analysis or expose the gate trace unless the user explicitly asked for it.

## Run the Workflow

### 1. Build the Evidence Base

- Separate facts, constraints, assumptions, and unknowns.
- Quantify both sides when data exists. Never invent targets, load, cost, or failure rates.
- For a coding task, identify the files, components, data flows, tests, and operational surfaces that create the conflict.
- Ask a blocking question only when the missing choice would materially change the solution. Otherwise state the assumption and proceed.

### 2. Model the System and Resources

- Name the useful function, target, harmful or insufficient effect, system boundary, and relevant supersystem.
- Inventory resources already present: data, metadata, time windows, topology, queues, caches, redundancy, idle capacity, control signals, logs, failure modes, and user or client behavior.
- Prefer reusing a resource over introducing a new service, store, dependency, or control plane.

Use [software-patterns.md](references/software-patterns.md) after repository inspection when software-specific mappings or standard patterns would help.

### 3. State the Ideal Final Result

Write:

The [system or existing resource] delivers [useful function] under [conditions] without [harm, permanent compromise, or unnecessary new machinery].

Treat the ideal final result as a direction, not a factual promise. Reject physically, logically, financially, or legally impossible interpretations.

### 4. Formulate the Contradictions

- Technical contradiction: improving X through a named action worsens Y through a named mechanism.
- Inverted technical contradiction: avoiding that action preserves Y but loses X.
- Physical contradiction, when useful: the same element or parameter must be A for one condition and not-A for another condition. Omit this formulation when it does not change concept generation.
- Prioritize one key contradiction. Track secondary contradictions without expanding the analysis indefinitely.

### 5. Generate Resolutions

Try these routes in order:

1. Separate the opposite states in time, space or structure, condition, or scale or system level.
2. Reassign the useful function to an existing resource; remove, trim, or neutralize the harmful interaction.
3. Apply a small set of inventive principles. Read [inventive-principles.md](references/inventive-principles.md) only when separation and resource use do not yield enough concepts.
4. If local knowledge is insufficient and research is allowed, search by function and unwanted effect rather than by product name. Verify analogies with reliable sources and explain the transfer mechanism.

Generate several mechanisms before choosing. Do not display a tour of all 40 principles.

### 6. Converge on Engineering Concepts

Keep two to four distinct concepts. For each, record:

- the separation or inventive move;
- the causal mechanism;
- the existing resource reused;
- the concrete code or system surface that changes;
- both benefits preserved;
- the new risk or secondary contradiction;
- the metric, test, trace, or experiment that could falsify it.

Reject a concept that only renames, hides, or moves the original harm.

### 7. Select and Verify

- Rank concepts by contradiction removal, evidence, feasibility, reversibility, blast radius, and verification cost. Do not reward novelty by itself.
- Select the smallest reversible experiment with a credible path to every hard constraint. Cheapness alone does not make an implausible concept the recommended experiment.
- Keep training and tuning inputs separate from held-out evaluation data. Do not improve a concept on the same examples used to claim its success.
- Keep the recommendation and next experiment consistent. If a test only rules out a weaker concept, label it as a diagnostic rather than the recommended solution.
- If the user requested implementation, make the scoped change and run the repository's normal checks.
- If the user requested advice or diagnosis only, stop at a decision-ready experiment or plan.

### 8. Use One Feedback Loop

After testing or critique, ask:

- Did the selected concept preserve both named benefits?
- Did it introduce a worse contradiction elsewhere?
- Which assumption failed?

Revise the contradiction or concept once when needed. Avoid an open-ended principle cycle.

## Produce the Result

Lead with the engineering decision, not the method trace.

- For implicit skill use, do not name TRIZ, the gate, the ideal final result, or inventive principles. Return the recommendation, its causal rationale, credible alternatives, the falsifiable experiment, and the residual risk.
- When skipping or deferring TRIZ, give at most one sentence of routing rationale and continue with the direct debugging, standard-pattern, or measurement response.
- When the user explicitly requests a TRIZ walkthrough or teaching artifact, return a compact decision record: evidence and unknowns; contradiction and ideal; separations and resources; concept comparison; recommendation, experiment, and residual trade-off.
- For implementation, keep any decision record brief, then lead with changed files, observable behavior, and verification results.

Use [examples.md](references/examples.md) only to calibrate routing or output. Use [sources.md](references/sources.md) when making claims about TRIZ or the evidence behind this workflow.

## Guardrails

- Keep skill discovery, reference loading, and internal tool failures out of the user-facing result unless they prevent a correct task outcome. Fall back to the loaded workflow or the direct engineering route when possible.
- Do not claim that a concept is novel, patentable, optimal, or proven without external evidence.
- Do not invent a contradiction-matrix lookup. If the user supplies a matrix or mapping, report the mapping and its uncertainty.
- Do not force physical TRIZ terminology onto software when the analogy has no causal value.
- Do not substitute brainstorming for code inspection, calculations, benchmarks, tests, or domain review.
- Do not present a midpoint compromise as contradiction resolution. Report an honest residual trade-off when separation is impossible.
- Do not let the TRIZ trace make the answer less specific than a direct engineering response.

## Sustained source-formalization workflow (2026-09-24)

An explicit request to use TRIZ requires considering its applicability, not inventing a contradiction. Ordinary Lean elaboration errors, reversed equalities, missing library lemmas, and routine induction obligations should use the direct proof/debugging workflow. Record a brief applicability decision only when useful or explicitly requested.

If repeated local proof steps leave the central source-to-implementation bridge untouched, inspect the dependency structure and proof representation before generating more helpers. A genuine conflict such as faithful full semantics versus infeasible certificate reduction may justify a separation or representation change. State the causal conflict, preserve every hard mathematical constraint, and validate the chosen approach on the central obligation. Small passing fragments are insufficient evidence that the whole contradiction is resolved.

Do not substitute repeated method narration for implementation. Evidence of application is a concrete decision and its checked consequence; merely loading the skill does not establish application.

## Representative verification before scaling a concept

Before using a passing prototype to resolve a proof-cost conflict, verify that it exercises the required mathematical domain and the expensive mechanism. A prefix of packed states may contain only singular matrices or default/sentinel entries. Measure relevant coverage and reduction cost separately; elapsed time on irrelevant cases does not validate the proposed certificate design.

If exact exhaustive checking is expensive, inspect the resources already present: reachability, rank, component closure, symmetry with proven cost preservation, and a representation-to-semantics theorem. A promising separation is a structural proof for invariant or degenerate cases plus checked certificates for the remaining required instances. Preserve labels, operation costs and all source quantifiers. Verify the bridge and the union of covered cases before declaring the conflict resolved.

Choose a representative next experiment that can falsify the proposed mechanism, such as a nontrivial reachable block plus its semantic bridge. Routine domain mistakes should be fixed directly; they do not need a TRIZ contradiction. A faster but incomplete proof, or a narrowed theorem without source justification, does not satisfy the original hard constraints.
