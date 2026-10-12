# Native runtime and performance

## Scheduling contract before optimization

Document the order for receptor input/feedback, chemical and graded propagation,
membrane update, spike detection/reset, delay ring, plasticity and physical
advance. Keep neural, body, rendering and rocket clocks explicit with units.
Batching a feed-forward fixture is not proof that batched closed-loop updates
preserve feedback delay. Preserve the continuous neural state across decisions.

Keep the full graph on device, with stable preallocated SoA/CSR storage and
explicit ownership across Rust/C++/CUDA. Python can orchestrate/reference/analyze;
the intended hot loop is native. Do not claim performance because the source is
C++: count transfers, synchronizations, allocations and recording work.

`brain_body_probe.cpp` calls the neural ABI for a single tick and copies all
voltages/conductances/spikes back. This is useful diagnostic observability,
not evidence of a scalable final loop. Profile the actual complete workload
before replacing it with device-resident stepping, selected readouts or bulk
event recording. Preserve full events through a bounded recorder and backpressure;
do not drop evidence to make timing look better.

Use `gpu-architecture` for a system redesign and `highload-gpu` for the specific
kernel/profiler workflow if installed. Give buffer shape/type/bytes, access lanes,
capacity, writer/reader, ready event, lifetime and overflow action. A GPU hash
table/Fenwick proposal needs evidence against flat scans/sorts/compaction and a
dependency analysis; CPU-style serial work per receptor already failed here.

## Numerical validation

The Shiu pilot showed that tiny near-threshold errors can move spikes. FP64
matched the tested author Brian2 events; FP32 was not equivalent on all full-graph
inputs. Do not choose precision from voltage RMSE alone. Use exact events where
the declared deterministic reference permits, state traces, independent equations,
delay/reset/refractory fixtures and long enough representative stimuli.

Published code may contain a numerical problem. Preserve its version, isolate
the mechanism, compare a correction against convergence/independent equations,
then redo the relevant physiological comparison. Silently reproducing a source
bug is not biological fidelity; silently correcting it is not source equivalence.
The HH gate and held-photocurrent investigations are concrete project examples.

Changing RNG changes paths. Counter-RNG test vectors and checkpoint continuation
can be exact for that candidate; source-vs-candidate comparisons need stochastic
law and downstream checks. A changed RNG must not load an incompatible checkpoint.

## Accepting a speed claim

Freeze graph, profile, inputs, output contract, precision and seeds appropriately.
Record actual GPU/toolchain/flags and binary hash. Compare same-session runs with
warmup/repeats and full end-to-end wall time, including body/environment and
required recording. Report simulated seconds per wall second and failure rates.
Small isolated retina timings cannot be extrapolated to training throughput.

Do not restart rejected work without new evidence: grouped hash/Fenwick retina
overflowed/timed out; a paired counter-RNG screen yielded about 1.0048x in its
recorded setting, not a material improvement. Locate these reports instead of
repeating the same design. Approximate sampled/GRU retina is a separate candidate;
it is not authorized as the final fly solely because it is fast.

## Composite continuation

Capture immutable graph/build/profile identity, all neuron/receptor states,
delays, plastic weights/eligibility, RNG, body solver state, rocket/engine/fuel,
clocks and recorder sequence. Resume in a fresh process and compare the declared
continuation interval. A brain-only checkpoint or file checksum does not close
the full-system continuation requirement.
