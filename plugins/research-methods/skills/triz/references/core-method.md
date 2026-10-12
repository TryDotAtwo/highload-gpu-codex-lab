# Core Method

Use this reference for a deep pass, an ambiguous causal model, interacting contradictions, or an implementation task.

## Contents

1. Evidence model
2. System and function model
3. Resource inventory
4. Ideal final result
5. Contradiction models
6. Resolution routes
7. Concept checks
8. Feedback and stopping rules

## 1. Evidence Model

Create four internal buckets before ideation:

| Bucket | Meaning | Examples |
|---|---|---|
| Fact | Directly observed or sourced | benchmark output, test failure, code path, documented limit |
| Constraint | Must hold for the proposed solution | compliance rule, API contract, memory ceiling |
| Assumption | Plausible but unverified | traffic distribution, cache locality, user tolerance |
| Unknown | Missing information that can change the decision | peak cardinality, consistency window, vendor quota |

Quantify only from evidence. When a value matters but is unknown, design a measurement or sensitivity range instead of fabricating a point estimate.

## 2. System and Function Model

Set a boundary narrow enough to change and wide enough to include the cause:

- system: the components under direct design control;
- subsystem: the component where the conflict manifests;
- supersystem: clients, operators, infrastructure, external services, regulations, and environment;
- target: the component or actor receiving the useful function.

Describe each relevant interaction as:

Source component -- action -- target component -- effect

Classify the effect:

- useful and sufficient;
- useful but insufficient;
- useful but excessive;
- harmful;
- missing.

For a causal chain, start at the observed harm and follow three to five evidence-supported links toward controllable causes. Stop when the next link is speculation. Do not label a politically convenient cause as a root cause without evidence.

## 3. Resource Inventory

Search the current system before adding machinery.

| Resource type | Software examples | Questions |
|---|---|---|
| Data | request fields, history, transaction log, cache keys | Can existing data choose the state or predict work? |
| Information | versions, confidence, risk score, provenance | Can metadata carry a distinction now hidden? |
| Time | idle periods, write time, pre-deploy, asynchronous window | Can work move earlier, later, or off the critical path? |
| Space or structure | edge, client, shard, tier, process, region | Can opposite states live in different places or layers? |
| Capacity | spare CPU, replicas, browser compute, batching window | Can existing capacity absorb the function conditionally? |
| Control | feature flags, feedback signals, quotas, backpressure | Can behavior adapt rather than stay fixed? |
| Harm | errors, heat, retries, duplicate traffic, contention | Can the harmful effect become a signal or useful input? |
| Supersystem | CDN, database, CI scheduler, client retry logic | Can a surrounding component perform the function? |

Prefer a resource that is already observable and testable. Account for its ownership and operational cost; an existing component is not automatically free.

## 4. Ideal Final Result

Use this form:

The [existing component or resource] itself provides [useful function] under [operating condition], while [harm] does not occur and no unnecessary component is added.

Use ideality qualitatively:

Ideality = useful effects / (costs + harms)

Do not compute this ratio unless the terms share a justified numerical model. Improve ideality by increasing useful effects, removing harm, lowering cost, or transferring a function to an existing resource.

An ideal final result frames search; it does not override hard constraints. Mark any impossible element as an aspiration and derive a reachable direction from it.

## 5. Contradiction Models

### Technical contradiction

Write both directions:

- If we perform action A, benefit X improves because of mechanism M1, but harm Y worsens because of mechanism M2.
- If we avoid or invert action A, harm Y is controlled, but benefit X is lost.

The two mechanisms expose possible separation points. Qualities such as fast and reliable do not form a technical contradiction until a specific intervention and causal link connect them.

### Physical contradiction

Derive a physical contradiction only when the same element or parameter needs opposite states:

The [element or parameter] must be [state A] under [condition A] to provide [benefit A], and must be [opposite state] under [condition B] to provide [benefit B].

In software, physical means a structurally opposite state, not a material property. Examples include strict and flexible validation, fresh and cached data, verbose and opaque errors, or mutable and immutable configuration.

### Administrative problem

We need a result but do not know how is an inventive situation, not yet a usable contradiction. Gather evidence and identify the action that produces the trade-off.

## 6. Resolution Routes

### Separation

Test all applicable axes:

- time: different lifecycle phases, foreground versus background, immediate versus eventual;
- space or structure: different components, layers, tenants, regions, paths, or replicas;
- condition: risk, identity, load, query type, confidence, feature flag, or failure state selects behavior;
- scale or system level: item versus aggregate, interface versus implementation, local versus global, subsystem versus supersystem.

Name where each state holds. Adaptive behavior without a selection condition is not a complete separation.

### Function reassignment and trimming

Ask:

1. Which component currently performs the useful function?
2. Can the target, an existing neighbor, or the supersystem perform it?
3. Can the harmful component disappear while its useful function remains?
4. Can the harmful interaction be blocked, transformed, or used as feedback?

Do not trim a component until another mechanism carries every required function and invariant.

### Inventive principles

Use the catalog to generate mechanisms after separation and resource analysis. Select principles that alter the causal link, not principles whose names merely resemble the problem.

### Function-oriented search

Abstract the task as:

How does another technical system perform [function] under [condition] without [unwanted effect]?

Search mechanisms, not metaphors. A valid bridge names source mechanism, target mapping, changed assumptions, evidence, and confidence. Reject surface analogies.

## 7. Concept Checks

For every candidate, answer:

1. Which causal link changes?
2. Where do the opposite states now live?
3. Which existing resource carries the change?
4. Which invariant remains true?
5. What new component or operational burden appears?
6. Which failure mode becomes more likely?
7. What observation would prove the concept wrong?

Use a simple comparison:

| Criterion | Prefer |
|---|---|
| Contradiction removal | both benefits preserved under named conditions |
| Evidence | mechanism supported by code, measurements, or a verified analogue |
| Feasibility | current stack and team can build and operate it |
| Reversibility | experiment can be disabled or rolled back |
| Blast radius | failure stays bounded |
| Verification | a test or metric distinguishes success from wishful thinking |

Novelty is not a selection criterion unless the user explicitly needs exploratory invention.

## 8. Feedback and Stopping Rules

Run at most one normal revision loop:

1. Critique the leading concept against both sides of the contradiction.
2. Identify a transferred or newly created harm.
3. Adjust the concept or reformulate the key contradiction.
4. Re-run the concept checks.

Stop when one of these conditions holds:

- a concrete design preserves both benefits and has a falsifiable experiment;
- a standard pattern directly resolves the verified mechanism;
- evidence shows that one side is not a real requirement;
- every feasible concept retains a residual trade-off, which is documented;
- missing data prevents a responsible choice, so measurement becomes the next action.

Avoid repeated cycles that only relabel the same architecture with additional TRIZ terms.
