# GPU Experiment Method And Failure Taxonomy

Use this reference for long target-hardware optimization campaigns. It is deliberately workload-agnostic; model and search details belong in their domain plugins.

## Evidence ladder

Record each result at exactly one level:

1. **Source contract** — layouts, shapes, precision and invariants are explicit.
2. **Compile gate** — the exact target translation unit and architecture compile.
3. **Runtime gate** — a bounded launch exits cleanly on the target GPU.
4. **Numerical gate** — deterministic output matches the chosen oracle/tolerance.
5. **Component benchmark** — one real stage is timed with warmup, repeats and resource data.
6. **Integrated benchmark** — the component runs in the real surrounding pipeline.
7. **End-to-end acceptance** — useful application output and wall time improve on an identical workload.

A higher-looking TFLOP/s number at a lower level does not supersede a lower integrated number.

## Status vocabulary

Use stable words in reports:

- **accepted**: all required gates for the claimed scope passed;
- **positive component**: reusable measured improvement, not yet an application promotion;
- **negative result**: measured regression, incorrect output, illegal launch or invalid architecture assumption;
- **superseded**: a later, more exact experiment replaces the interpretation;
- **prepared**: source, contract or binary exists;
- **unverified**: the required target runtime gate did not run;
- **platform loss**: the remote environment disappeared without a terminal device result.

Prefer the explicit phrase **prepared but not runtime-verified** to vague claims such as “almost done.”

## Throughput naming

Always name the numerator and timed interval:

- raw instruction throughput;
- dense-equivalent sparse throughput;
- GEMM-only throughput;
- encode + GEMM throughput;
- fused-stage throughput;
- useful throughput for the complete stage;
- end-to-end application throughput.

Theoretical peak is a ceiling for a matching precision/instruction contract. It is not a target-hardware measurement. Raw instruction throughput may exceed 1 PFLOP/s while real narrow-shape kernels remain far below it because of operand movement, conversion, epilogues, synchronization and occupancy.

## Required experiment record

Every retained row should include:

- exact GPU product, compute capability, clocks/power state when relevant;
- driver, CUDA toolkit, compiler and library/CUTLASS commit;
- source commit plus dirty-patch/artifact hash;
- exact shapes, layouts, precision and scale-factor format;
- warmup, iterations, repeats and statistic used for selection;
- latency, useful work numerator, throughput and memory traffic definition;
- registers, stack, shared memory, active blocks/clusters and spills;
- correctness oracle and output digest/quality result;
- fatal/OOM/illegal-access/overflow evidence;
- contemporaneous control on the same runtime.

## Failure classification

Do not collapse these into “CUDA failed”:

| Class | Typical evidence | Correct response |
|---|---|---|
| architecture mismatch | unsupported instruction, builder assertion | return to an official example for the exact SM |
| launch/resource failure | too many resources, invalid cluster | record resources and reduce/repartition topology |
| correctness failure | digest or oracle mismatch | bisect arithmetic/layout semantics before timing |
| synchronization failure | deadlock, barrier phase error | run a bounded ownership/lifetime oracle |
| ABI failure | declaration/definition disagreement | compare complete parameter types across TUs |
| performance regression | correct but slower sustained median | retain the old path and record the negative result |
| platform loss | endpoint gone, no terminal CUDA line | mark unverified; never invent OOM/pass |

## Long-campaign discipline

- Keep the last correct measured executable and log immutable.
- Change one independent variable per A/B whenever possible.
- Use coarse screens, then repeated medians near the Pareto boundary.
- Save every negative row that rules out a topology.
- Re-run accepted controls after long-lived process state, symbol interposition, power state or toolchain changes.
- A compile gate never authorizes production dispatch.
- A component win must survive identical integrated and end-to-end gates.
