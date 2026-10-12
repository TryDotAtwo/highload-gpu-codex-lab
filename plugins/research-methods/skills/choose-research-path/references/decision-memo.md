# Short decision memo

The memo should be as short as the actual decision permits. The labels below are a reusable template, not a requirement to print every field on a trivial question. Keep **evidence_status** explicit for the claims carrying the conclusion.

```text
Decision: continue / bounded test / change method / park [exact claim or path]
Goal and scope: [target result, domain, constraints]
Evidence_status: [claim → status, source/provenance, material limits]
Reason: [decisive structural benefit, objection, or trade-off; separate taste]
Next discriminator: [specific check; strongest live alternative]
Outcome and effort: [if X, then…; if Y, then…; resources justified by this check]
Survives / reopen: [useful residue; what would change the recommendation]
```

If no sensible test is feasible, say so. Name the missing observable, theorem, instrument, or resource instead of inventing a test. If evidence supports several incomparable paths, present the live trade-off and ask the user only for a value or constraint that evidence cannot determine.

## Compact worked memo

**Decision:** change method for n=60; retain the table only as a small-instance candidate.

**Goal and scope:** 100 correct queries per instance, 128 GB RAM, lower total runtime than the 20-second/query baseline.

**Evidence_status:** scenario-reported query speed at n=20; exact storage calculation 16·2^60 = 2^64 bytes = 16 EiB; target speedup unestablished and explicit-table memory requirement infeasible under the stated cap.

**Reason:** compact lookup hides exponential construction and storage. The target baseline totals 2,000 seconds; isolated query latency is not the objective.

**Next discriminator / effort:** establish whether a proposed structural reduction preserves the full required outputs and reduces the state count enough to fit the cap. Account for construction, conversion, verification, and the 100 queries. Do not run the impossible full table as a feasibility test.

**Outcome / survives:** continue a reduced representation only after its correctness and resource bounds support the target; otherwise park it. Small-instance lookup can remain useful if measured end-to-end amortization justifies it. The n=20 evidence stays n=20 evidence.

This is a constructed example; no benchmark is claimed to have been executed.
