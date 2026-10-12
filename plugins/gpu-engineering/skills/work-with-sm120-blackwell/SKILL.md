---
name: work-with-sm120-blackwell
description: Use when writing, reviewing, compiling, or benchmarking CUDA for compute capability 12.0, SM120/SM120a, RTX 50-series, or NVIDIA RTX PRO 6000 Blackwell GPUs.
---

# Work With SM120 Blackwell

Load `references/sm120-rtx-pro-6000-blackwell.md` before architecture-specific design. For a long optimization campaign also load `references/experiment-method-and-failure-taxonomy.md` so compile, runtime, component, and end-to-end evidence are not conflated.

## First Principles

For custom shared/DSM epilogues or fusion, also read
`references/output-liveness-and-fusion-economics.md` before interpreting
no-store throughput or replacing a faster library control.

1. Probe the exact product, compute capability, driver/runtime, toolkit, CUTLASS commit, memory size, and power mode.
2. Separate SM100 datacenter Blackwell from SM120 RTX Blackwell. Do not copy TMEM, UMMA, multicast, cluster, or schedule assumptions across families.
3. Compile architecture-conditional paths for the exact target and fail closed when feature probes or artifacts do not match.
4. Start from an official CUTLASS example that actually targets SM120, then preserve its operand layouts, scale-factor layouts, alignment, and scheduler contract.
5. Measure native instruction ceiling, real-memory kernel, fused stage, and end-to-end work separately.

## RTX PRO 6000 Reality Check

The product specification advertises FP4/FP8/FP16 peaks, but useful throughput depends on compatible precision, shapes, layout, staging, occupancy, and the surrounding pipeline. Do not use the product peak as proof of achieved performance.

Compute capability 12.0 has tighter shared-memory and warp limits than SM100. Check registers, stack, dynamic shared memory, active blocks/clusters, and launch legality after every topology change.

## Promotion Gates

- deterministic numerical oracle;
- sanitizer or focused race/alignment probes for new synchronization;
- sustained target-hardware A/B with identical workload;
- resource report and failure rows;
- application-level correctness and end-to-end speed.

Retain the last correct measured path. Reject clever schedules that compile but lose useful throughput.
