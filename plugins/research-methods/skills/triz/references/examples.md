# Examples and Routing Boundaries

Use these examples to calibrate the gate and output. Do not copy a solution without checking the repository and constraints.

## Contents

1. Latency and ranking quality
2. Fast and complete CI
3. Reliable webhooks with low operational burden
4. Routine bug: skip TRIZ
5. Missing evidence: measure first
6. Compact output pattern

## 1. Latency and Ranking Quality

Request:

An autocomplete API must respond under 50 ms, while the best ranking model takes 250 ms. The team is choosing between latency and relevance.

Gate:

- Evidence needed: latency distribution by stage, candidate count, QPS, cacheability, model throughput.
- Candidate contradiction: running the heavy model per request improves ranking quality but worsens response latency because inference sits on the critical path.
- The causal link is explicit, so TRIZ applies.

Physical contradiction:

Ranking must be lightweight during an interactive request and heavyweight when enough time or reusable context exists.

Separation and resources:

- Time: compute stable features or popular-prefix results before the request.
- Structure: use a fast candidate path, then a heavyweight reranker where the latency budget permits.
- Condition: use confidence to decide whether the fast result is sufficient.
- Resources: prefix history, write-time events, cached embeddings, client typing cadence.

Concept:

Return a fast candidate set from precomputed or lightweight features. Run the heavyweight model ahead of likely requests or asynchronously for a subsequent refinement. Measure first-result p95, refinement delay, ranking metric, model saturation, and cache hit rate.

Do not claim success until the workload and product behavior confirm that refinement is useful and stable.

## 2. Fast and Complete CI

Request:

Developers need feedback in five minutes, but the full compliance suite takes forty minutes and cannot be removed.

Contradiction:

Running the full suite before feedback preserves coverage but worsens feedback latency because all tests block the first result.

Resolution:

- Separate in time: return targeted feedback immediately and continue the full suite.
- Separate by condition: use change impact and risk class to choose early tests.
- Keep the full suite as a merge or release invariant rather than pretending the targeted suite is complete.

Experiment:

Replay historical changes. Compare time to first actionable failure, escaped failures, selection recall, full-suite completion, compute cost, and merge delay. A design that merely moves the forty-minute gate without improving developer flow has not preserved both benefits.

## 3. Reliable Webhooks with Low Operational Burden

Request:

A small team needs ordered, retryable webhooks but cannot operate a new event platform.

Resource check:

Inspect the current database, transaction boundaries, background workers, retry facilities, idempotency keys, and per-customer ordering requirements.

Likely direct pattern:

A transactional outbox can reuse database durability: the business write and outbox record commit together, while an existing worker delivers and retries. Per-destination sequence or partitioning can preserve the required ordering scope.

TRIZ value:

The resource inventory reframes the problem from build a new reliable service to reassign reliability to an existing durable resource. Use the normal pattern name. Verify database growth, locking, poison messages, retry policy, ordering scope, observability, cleanup, and operator workflow.

## 4. Routine Bug: Skip TRIZ

Request:

A Go handler panics when an optional request field is absent. Fix it and add a regression test.

Gate result:

No technical contradiction is established. Inspect the stack trace and handler, reproduce the nil path, implement the smallest correct guard or validation, and run tests. A TRIZ record would add overhead without changing the solution.

## 5. Missing Evidence: Measure First

Request:

Make this cache much faster without using more memory.

Gate result:

The desired qualities resemble a contradiction, but the causal intervention and current bottleneck are unknown. Measure hit rate, object sizes, eviction causes, latency by hit and miss, key distribution, and memory overhead. Apply TRIZ only after a specific action is shown to improve latency while increasing memory or another harm.

## 6. Compact Output Pattern

Evidence:

- Facts: named observations with source.
- Unknowns: values that can change the decision.

Gate:

- Apply or skip, with one causal reason.

Contradiction and ideal:

- Technical: named action, benefit, harm, and mechanism.
- Physical: same element, opposite states, and conditions, when applicable.
- Ideal final result: directional statement.

Concepts:

| Concept | Mechanism and separation | Existing resource | Risk | Falsifying check |
|---|---|---|---|---|
| A | concrete mechanism | named resource | new harm | metric or test |
| B | concrete mechanism | named resource | new harm | metric or test |

Recommendation:

- Selected concept and reason.
- Smallest reversible experiment.
- Residual trade-off or none demonstrated yet.
