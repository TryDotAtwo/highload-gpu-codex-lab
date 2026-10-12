# Output liveness and fusion economics

Workload-independent lessons from SM120 target experiments, audited2026-09-03.
Neural-network shapes and benchmark history belong in GpuNeuralInference.

## Prove what the timed binary executes

Removing an output can remove upstream arithmetic. A diagnostic build that
reads shared output may retain instructions absent from its timing sibling.
For custom callbacks, trace the actual instantiated call chain: a valid
requires-expression can silently skip an unforwarded optional hook.

Before accepting a store-free or no-global-output measurement:

- identify the exact timed symbol and binary hash;
- establish that required MMA, conversion and real output writes remain;
- give every required output an observable consumer, without replacing the
  production contract by a cheap checksum and calling it the same workload;
- verify bytes/ownership on nonuniform inputs, not only addresses or scale data;
- report validation snapshot traffic separately and recheck timing-build liveness.

An observable checksum is useful as an ablation, not a replacement for full
payload. A static opcode count proves emitted code exists, not its dynamic
frequency. Code from unrelated kernels in the executable proves nothing
about the measured symbol. Uniform checksum success can hide permutations,
partial coverage or scale saturation.

## Global addresses are not DRAM transactions

No STG proves no emitted global stores in that symbol, not no VRAM traffic.
LDL/STL, stack/local storage and global reads can still access device-backed
memory. Conversely a global-addressed handoff can hit cache. L2-fit arithmetic
and access-policy settings do not guarantee residency.

Distinguish ptxas spill bytes, static instruction counts, live allocations and
measured L1/L2/DRAM transactions. If Nsight counters are unavailable, retain
that limitation. Do not infer DRAM bandwidth or stalls from a static SASS count.

## Fusion must win on time, not storage ideology

Estimate removed traffic and launches against added packing, lane gathers,
barriers, tile setup, lost occupancy and spills. Keep the fastest eligible
unfused/library path as a measured comparator. Retain an immediate-parent
baseline only as a second diagnostic control.

Wide writes can cost more instructions: leader-only stores do not necessarily
reduce issued instructions; shuffle/shift/index expansion can dominate.
Isolate synchronization from gather work before blaming a barrier. Lower
register/spill counts or shared bytes are not sufficient acceptance criteria.

Persistent reuse helps only when lifetimes actually span work items. Rebuilding
and draining a short-K pipeline per output slice can erase TMA/MMA efficiency.
Do not remove drain/ack fences blindly: pipeline barriers, shared inputs and
outputs each have separate lifetimes.

## Producer/consumer overlap invariants

Separate source-free from destination-ready. A producer may compute into its
own storage before a destination becomes ready only if prior source readers
have finished and the compute touches no consumer-owned state. It must still
wait for destination readiness before writes and preserve phase/generation
counts. Topology tests, full-value tests and performance tests certify different
things; a multi-generation ring test is not a full application racecheck.

## Packed subbyte correctness

Validate logical coordinate, physical byte/nibble offset, swizzle units,
pointer stepping, scale layout, alignment and writer ownership separately.
A normal typed byte pointer is not a subbyte iterator. A swizzle expressed in
bytes cannot simply receive nibble coordinates. Per-lane ownership may allow
only byte pairs rather than a desired wider vector. Shared read-modify-write
of independent nibbles requires explicit ownership/synchronization.

## Tool failures are not device diagnoses

Missing profiler, unsupported sanitizer device, failed injection-library load,
compile failure and numerical failure need different labels. Record the exact
versions and errors. A reported Device not supported is neither a clean
sanitizer pass nor proof that the tested kernel caused the tool failure.
