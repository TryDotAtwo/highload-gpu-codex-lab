# Software Mappings and Resolution Starters

These mappings help generate questions after code inspection. They are not a canonical software contradiction matrix and do not predict the correct solution.

## Contents

1. Contradiction families
2. Standard-pattern check
3. Software resources
4. Cross-domain bridge test
5. Implementation verification

## 1. Contradiction Families

| Conflict family | Causal question | Separation starters | Common mechanisms to verify |
|---|---|---|---|
| Latency versus result quality | Which expensive step sits on the critical path? | foreground/background, candidate/rerank, confidence condition | precomputation, two-stage retrieval, speculative work, progressive results |
| Throughput versus tail latency | Which shared resource creates queueing? | batch/interactive lanes, tenant or priority class, admission condition | backpressure, bounded queues, workload shaping, concurrency control |
| Freshness versus availability | Which coordination step blocks reads or writes? | local/global, current/eventual, risk or operation type | versioned state, stale-while-revalidate, conflict-free merge, leases |
| Consistency versus availability | Which invariant truly needs global coordination? | per invariant, per region, per operation | escrow, partitioned ownership, sagas, compensating actions |
| Security versus usability | Which action changes risk rather than merely frequency? | low/high risk, known/new device, read/write action | step-up authentication, scoped capability, short-lived privilege, secure detail channel |
| Observability versus overhead | Which events need full fidelity? | sample/full trace, normal/error, canary/general traffic | adaptive sampling, triggered tracing, aggregation, correlation IDs |
| Test speed versus coverage | Which failures correlate with changed surfaces? | pre-merge/post-merge, targeted/full, risk class | change-impact selection, parallel shards, cached artifacts, asynchronous full suite |
| Cache size versus hit rate | Which objects matter under which conditions? | hot/cold, online/offline, predicted/unpredicted | tiered storage, predictive prefetch, adaptive eviction, compressed representation |
| Release speed versus stability | Which exposure level changes the consequence of failure? | canary/general, reversible/irreversible, tenant group | feature flags, progressive delivery, shadowing, automated rollback |
| Schema flexibility versus contract stability | Which boundary must remain stable? | internal/external, write/read, version or epoch | adapters, schema registry, tolerant readers, versioned events |
| Reliability versus operational burden | Which existing durable component can carry state? | request/background, primary/supersystem | transactional outbox, database leases, managed primitives, idempotency |
| Privacy versus analytical utility | Which identity or raw field is necessary for which computation? | raw/derived, secure enclave/general workspace, training/serving | minimization, tokenization, aggregation, synthetic data, audited compute |

Start with the causal question. A listed mechanism is a hypothesis, not an answer.

## 2. Standard-Pattern Check

Before extended ideation:

1. Search the repository for an existing pattern, incomplete implementation, or relevant dependency.
2. Check the platform's normal solution for the verified causal mechanism.
3. Confirm that the pattern preserves both named benefits under the actual constraints.
4. Use the standard name and implementation guidance when it fits.
5. Continue TRIZ only when the pattern leaves the key contradiction unresolved.

Examples of direct resolutions include transactional outbox for atomic event publication, step-up authentication for risk-conditioned friction, feature flags for time or population separation, and background reconciliation for immediate response plus eventual completeness. Their appearance in a TRIZ analysis does not make them new.

## 3. Software Resources

Inspect resources by asking:

- Data: Which identifiers, historical events, access patterns, or transaction records already exist?
- Metadata: Can version, confidence, risk, ownership, or provenance make conditions explicit?
- Time: Can work move to write time, build time, idle time, prefetch, or post-response processing?
- Topology: Can edge, client, database, shard, worker, or replica take one state?
- Control: Can a feature flag, quota, token, lease, or feedback signal select behavior?
- Failure: Can a retry, error, timeout, duplicate, or rejected request become a useful signal?
- Human and client behavior: Can the caller perform safe work, carry a token, retry idempotently, or choose fidelity?
- Existing durability: Can a transaction log, database table, object store, or CI artifact replace new infrastructure?

Account for contention, ownership, privacy, cost, and failure recovery before declaring a resource free.

## 4. Cross-Domain Bridge Test

A usable analogue includes:

| Field | Required content |
|---|---|
| Source function | What the source system actually accomplishes |
| Source contradiction | Which two effects conflict |
| Source mechanism | How the source changes the causal relationship |
| Target mapping | Which target components correspond and why |
| Broken assumptions | Where the analogy may fail |
| Evidence | Reliable source, experiment, or implementation |
| Confidence | High, medium, or low with a reason |

Reject bridges based only on shared vocabulary, shape, or metaphor.

## 5. Implementation Verification

Translate the concept into a normal engineering plan:

1. Name the files, services, schema, interfaces, or deployment controls that change.
2. Preserve explicit invariants and compatibility requirements.
3. Add or update the smallest tests that exercise both sides of the contradiction.
4. Define metrics for benefit X, harm Y, and the new failure mode.
5. Bound exposure with a feature flag, canary, shadow path, or reversible configuration when appropriate.
6. Run the project's existing formatter, static checks, unit tests, and relevant integration or performance tests.
7. Report observed results separately from predicted effects.

If verification cannot distinguish the concept from the baseline, improve the experiment before expanding the implementation.
