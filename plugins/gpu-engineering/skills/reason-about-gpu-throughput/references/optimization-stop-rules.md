# Optimization decision gates

Before another experiment, maintain a ledger of the fastest eligible incumbent,
rejected variants, exact workload, output contract, and evidence needed to reopen
each rejected route. A recovered session is not new evidence for a rejected kernel.

## Comparable measurements

Freeze useful FLOPs, shape, input/output precision, observable outputs, concurrency,
warmup, compiler and binary. Aggregate throughput of two concurrent requests is
not single-request latency. Dividing elapsed time by request count is amortization.
An output-free or fixed-input ablation is not an application replacement.

Distinguish theoretical peak, achieved synthetic throughput and validated stage
throughput. An achieved synthetic rate is neither a universal ceiling nor a
physical lower bound on latency. Enlarged/padded/sparse physical FLOPs must not
inflate the useful numerator.

## Quantitative feasibility

For target speedup S, an infinitely accelerated fraction must be at least 1-1/S.
Use a matched critical-path profile to estimate that fraction; never subtract
unrelated microbenchmarks from whole-model timings. For concurrent stages use the
critical path, not a blind sum of overlapping durations.

Global addresses do not imply DRAM misses. Cache-sized allocation does not prove
L2 residency. Bytes/bandwidth estimates are conditional bounds, not measured
recoverable stalls. Fusion can lose more to spills, barriers, occupancy and
repeated short-reduction setup than it saves in transport.

## Stop or continue

Continue only with a named, measurable bottleneck and a falsifiable change large
enough to close the relevant gap. Predeclare a bounded experiment budget and an
improvement threshold; do not invent a universal percentage.

Report separately: (1) this candidate lost, (2) this engineering route has no
supported next change, (3) a physical impossibility was established. Neither (1)
nor (2) proves (3). User-desired throughput is a target, not evidence it is feasible.
Retain the fastest quality-validated implementation when a speculative route loses.
