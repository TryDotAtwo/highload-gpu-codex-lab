# SM120 / RTX PRO 6000 Blackwell Reference

## Verified Hardware Contract

NVIDIA lists the RTX PRO 6000 Blackwell Server Edition with 96 GB GDDR7, 1,597 GB/s memory bandwidth, and marketing peaks of 4 PFLOP/s FP4, 2 PFLOP/s FP8, and 1 PFLOP/s FP16/BF16. Those are precision-specific ceilings, not end-to-end application throughput.

For compute capability 12.0, NVIDIA's Blackwell Tuning Guide states:

- 48 concurrent warps per SM;
- 64K 32-bit registers per SM and at most 255 registers per thread;
- 128 KB shared memory per SM;
- 99 KB maximum shared memory per thread block;
- cluster occupancy should be checked with `cudaOccupancyMaxActiveClusters`;
- DSM accesses should be coalesced and aligned to 32-byte segments when possible.

Sources:

- [RTX PRO 6000 Blackwell Server Edition specifications](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/)
- [CUDA 13 Blackwell Tuning Guide](https://docs.nvidia.com/cuda/archive/13.0.2/pdf/Blackwell_Tuning_Guide.pdf)

## SM100 Is Not SM120

Treat `sm_100*` and `sm_120*` as different execution contracts. An SM100 tutorial may compile substantial host/template code for SM120 yet fail at a TMEM or instruction gate. Verify the emitted path and runtime feature, not only template instantiation.

NVIDIA CUTLASS example 79a is an authoritative SM120 block-scaled NVFP4 starting point. It documents `mma.sync.aligned.block_scale`, warp-specialized persistent schedules, software cluster launch control, and explicitly warns that its RTX/GeForce path has no TMA multicast and uses cluster shape `1x1x1`.

- [CUTLASS example 79a: SM120 NVFP4 GEMM](https://github.com/NVIDIA/cutlass/blob/main/examples/79_blackwell_geforce_gemm/79a_blackwell_geforce_nvfp4_bf16_gemm.cu)

Do not infer that every other CUTLASS collective, dynamic cluster topology, or SM100 feature is supported. Compile and execute a minimal gate on the target device.

## Block-Scaled Operands

Narrow precision is a physical storage and MMA contract:

- quantized values and scale tensors jointly represent the logical operand;
- scale mode determines broadcast granularity;
- scale swizzle is architecture dictated;
- many Blackwell kernels require scale tensors pre-arranged in their physical layout.

Therefore, prepare immutable weights and scale layouts offline. Runtime recoding belongs only where activations are inherently dynamic and its cost must be included in the fused-stage timing.

- [CUTLASS ScaledOperand documentation](https://docs.nvidia.com/cutlass/latest/media/docs/operators/api_reference/arguments.html)

## Evidence Ladder

Use four levels and never collapse them:

1. raw instruction/register microbenchmark;
2. official-layout real-memory kernel;
3. fused producer/consumer stage with transport and synchronization;
4. end-to-end application wall time and correctness.

At each level record exact shapes, useful FLOP convention, precision, accumulation type, warmup/repeats, median and dispersion, registers, stack, shared memory, occupancy, and failure status. A 1+ PFLOP/s raw MMA result can coexist with a much slower fused path because packing, scale generation, TMA/DSM transport, epilogues, barriers, and narrow matrix shapes are real work.

## Persistent And DSM Design

- Use persistent/ping-pong schedules only after proving there is enough repeated work to amortize setup.
- Keep lifetime-scoped shared/DSM buffers small; larger buffers can lower occupancy without reducing traffic.
- Prefer one-way ownership and precise producer-consumer barriers over broad `cluster.sync()`.
- A host timeout does not prove a bad GPU kernel stopped cleanly. Treat a suspected barrier hang as a session-risking experiment and use a bounded, minimal gate.
- Compare cooperative copy, bulk DSM/TMA, and global/L2 paths on the exact shape; no transport is universally fastest.

## Debugging Checklist

- exact `sm_120` versus architecture-conditional `sm_120a` flags;
- 64-byte TMA descriptor alignment and required shared/scaling alignment;
- matching kernel `Params` declarations across translation units;
- static versus dynamic cluster assumptions;
- scale-vector length and packed-value layout;
- registers, local-memory stack, dynamic shared memory, and active blocks;
- numerical oracle before timing.
