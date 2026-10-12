# Inventive Principles for Software

Use this catalog for divergence after separation and resource analysis. The software prompts are heuristic translations, not entries in Altshuller's classical contradiction matrix. Select only principles that change a causal mechanism.

| # | Principle | Software generation prompt |
|---:|---|---|
| 1 | Segmentation | Split by responsibility, workload, lifecycle, risk, or data locality. Can each part take a different state? |
| 2 | Taking out | Remove the harmful work, data, dependency, or privilege from the critical path. |
| 3 | Local quality | Give hot and cold, trusted and untrusted, or read and write regions different behavior. |
| 4 | Asymmetry | Replace a uniform design with specialized paths, replicas, indexes, or policies. |
| 5 | Merging | Co-locate related work, batch operations, deduplicate requests, or share a lifecycle. |
| 6 | Universality | Make an existing component or artifact perform another required function. |
| 7 | Nested doll | Encapsulate state or behavior in layers; place a local mechanism inside a broader one. |
| 8 | Counterweight | Compensate load or risk with credits, redundancy, backpressure, reservations, or balancing work. |
| 9 | Preliminary counteraction | Pre-validate, reserve, isolate, or prepare rollback before the harmful action occurs. |
| 10 | Preliminary action | Precompute, prefetch, warm, index, compile, or allocate before the critical request. |
| 11 | Beforehand cushioning | Add a bounded fallback, circuit breaker, backup, feature flag, or recovery point. |
| 12 | Equipotentiality | Remove costly boundaries, conversions, privilege transitions, or network hops. |
| 13 | The other way round | Invert push and pull, ownership, control flow, dependency direction, or success criteria. |
| 14 | Curvature | Replace a rigid linear flow with a tree, ring, hierarchy, feedback curve, or non-linear policy. |
| 15 | Dynamics | Adapt configuration, capacity, fidelity, or policy to observed conditions. |
| 16 | Partial or excessive action | Use bounded approximation, overfetch, safety margin, speculative work, or staged completeness. |
| 17 | Another dimension | Add a version, epoch, priority, confidence, provenance, or side channel instead of overloading one value. |
| 18 | Vibration | Use jitter, probing, retries with variation, or small reversible perturbations to reveal or avoid lockstep failure. |
| 19 | Periodic action | Replace continuous work with sampling, batching, scheduled reconciliation, or pulsed control. |
| 20 | Continuity of useful action | Stream, pipeline, overlap stages, or use background work to remove idle gaps. |
| 21 | Skipping | Create a fast path, shorten a transaction, or pass rapidly through a dangerous intermediate state. |
| 22 | Blessing in disguise | Turn errors, retries, contention, or excess traffic into a signal, test input, or control mechanism. |
| 23 | Feedback | Measure outcomes and adjust limits, routing, fidelity, or recovery automatically. |
| 24 | Intermediary | Introduce a queue, proxy, adapter, lease, token, or translation boundary. |
| 25 | Self-service | Let components validate, heal, expire, rebalance, clean up, or report their own state. |
| 26 | Copying | Use replicas, snapshots, simulations, shadow traffic, synthetic data, or cached representations. |
| 27 | Cheap short-lived objects | Use ephemeral workers, disposable environments, temporary indexes, or rebuildable caches. |
| 28 | Mechanism substitution | Replace manual or centralized coordination with signals, declarative policy, or automation. |
| 29 | Pneumatics and hydraulics | Model flow explicitly with buffers, queues, pressure limits, admission control, and backpressure. |
| 30 | Flexible shells and thin films | Add a lightweight façade, compatibility layer, virtualization boundary, or policy wrapper. |
| 31 | Porous materials | Use sparse representation, filters, progressive loading, sampling, or selective visibility. |
| 32 | Color changes | Add tags, states, correlation IDs, health signals, or observability metadata. |
| 33 | Homogeneity | Standardize interacting components on one protocol, schema, representation, or runtime contract. |
| 34 | Discarding and recovering | Expire, garbage-collect, rebuild, replay, rotate, or regenerate state after use. |
| 35 | Parameter changes | Change encoding, compression, consistency mode, precision, representation, or data shape. |
| 36 | Phase transitions | Exploit lifecycle boundaries such as build versus run, warm-up versus steady state, or epoch cutover. |
| 37 | Expansion | Use elastic headroom, pre-allocated capacity, or controlled scaling when demand changes. |
| 38 | Strong interaction | Apply intensive validation, computation, or concurrency inside an isolated and bounded context. |
| 39 | Inert environment | Use a sandbox, read-only mode, canary, quarantine, deterministic replay, or isolated tenant. |
| 40 | Composite materials | Combine complementary storage, models, algorithms, consistency levels, or execution tiers. |

## Application Rule

For each selected principle:

1. Name the causal link it changes.
2. Translate the principle into at least two domain mechanisms.
3. Discard mechanisms that lack a concrete code or system surface.
4. Combine principles only when the combination removes a remaining harm.
5. Call a known pattern by its normal engineering name. Do not present rediscovery as novelty.
