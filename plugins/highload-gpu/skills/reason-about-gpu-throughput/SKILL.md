---
name: reason-about-gpu-throughput
description: Use when interpreting GPU TFLOP/s, utilization, rooflines, theoretical peak, isolated-kernel speed, useful throughput, or end-to-end performance claims.
---

# Reason About GPU Throughput

Do not optimize a ratio before defining its numerator and denominator.

For stalled optimization campaigns or feasibility claims, read
`references/optimization-stop-rules.md` before launching another experiment.

## Name Every Metric

- **Instruction/native throughput:** operations executed by the chosen hardware instruction.
- **Dense-equivalent throughput:** logical dense FLOPs divided by measured time; label sparsity or quantization multipliers.
- **Kernel throughput:** useful operations inside one measured kernel interval.
- **Stage throughput:** work completed by one pipeline stage including its transport and synchronization.
- **End-to-end throughput:** accepted application work divided by wall time.

Never present one as another. Theoretical peak is a ceiling for a compatible instruction mix, not an application result.

## Measurement Order

1. Freeze hardware, clocks/power when possible, driver, toolkit, library commit, binary hash, shapes, precision, and warmup.
2. Verify correctness before timing.
3. Time native instruction, real-memory kernel, stage, then end-to-end path.
4. Collect launch count, occupancy/resource limits, achieved bandwidth, tensor-pipe activity, stalls, and synchronization gaps.
5. Explain the gap between levels using measured bytes, instructions, launches, or idle intervals.

## Common Traps

For incremental deduplication/merge, derive the cost over the complete layer:
R scans of H historical records cost O(R*H), and rewriting a prefix growing by
b records per batch writes b*R*(R+1)/2 records. Sequential access can still lose
to an indexed lookup because it does much more total work. Measure the relevant
batch/history ratio, duplicate rate, index load factor, and memory footprint;
do not declare either sorted merging or random-access hashing universally best.

For GEMM pipelines, list padded instruction work, useful application work,
intermediate accumulators, epilogue traffic, and library-adapter copies. Occupied
tensor cores do not establish an end-to-end gain. Label static byte-pass counts
as logical traffic until hardware counters establish cache/DRAM behavior.

Attribute stalls using a matched search interval and critical-path timeline.
Summed CUDA API durations across threads/ranks can overlap and are not a
percentage of BFS wall time. A timeout is censored, not a measured runtime.

- Losing the fastest eligible incumbent while reporting incremental wins on a
  much slower prototype. Keep both comparisons visible with matched scope.
- Dead-code-eliminated MMA or output stores in an uninstrumented timing build.
- Equating no global stores, cache-sized allocation or ptxas spill counts with
  measured DRAM traffic. See
  `../work-with-sm120-blackwell/references/output-liveness-and-fusion-economics.md`.

- Counting two operations per FMA while comparing with a source that counts one.
- Applying sparse or low-precision marketing multipliers to dense useful work.
- Counting padded tiles or rejected candidates as useful work.
- Treating a short-window maximum as sustained performance.
- Assuming more concurrency improves throughput after occupancy, cache, or memory traffic saturates.
- Assuming a faster microkernel improves the critical path.

State uncertainty. A peak estimate can prioritize experiments; only target-hardware evidence can validate them.
