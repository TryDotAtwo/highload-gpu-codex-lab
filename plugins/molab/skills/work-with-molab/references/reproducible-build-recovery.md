# Recover reproducibility before repeating work

Read the latest completed-result ledger before starting a recovered notebook.
A new sandbox is not a reason to rebuild and retime a previously rejected route.
Identify the durable notebook, active execution, source closure and best binary.

Pin nvcc, runtime headers, CCCL and CUTLASS together. nvidia-smi's supported CUDA
version is not the compiler/header version. Record CUDART_VERSION and actual
include paths. A September 2026 recovery observed nvcc 13.3.73 alongside default
13000 runtime headers; this is a dated mismatch example, not an install recipe.

Bundle all required dirty/untracked headers with hashes, not only the main .cu
file. Preserve exact binary hashes and output contracts. A missing source/header
or mismatched SDK is a build failure, not evidence against GPU feasibility.

Keep long work foreground in a durable cell. Do not poll a child with stdout=PIPE
while never draining it: a full pipe can stall the child. Use a log file with
bounded progress reads, or continuously drain with a reader queue, while the
cell waits for completion. Neither method authorizes detached execution.

Persist and retrieve logs after each completed stage. Separate interrupted,
not-built, sampled-correctness and completed measurements. Never infer a fixed
session time limit or platform enforcement from a transport error alone.
Record observed HTTP/runtime/process evidence without tokens. Follow ordinary
authorized UI recovery; do not create retry loops to bypass platform enforcement.
