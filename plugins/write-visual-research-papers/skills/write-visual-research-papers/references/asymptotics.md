# Time and memory for search, algorithms, and HPC papers

## Define the variables and regime

Choose symbols suited to the actual algorithm. At minimum define input/state dimension n, retained frontier F_d at depth d, branching b_d, generated candidates N_d, survivor count U_d, depth limit D, GPU/device count p, per-state bytes s(n), model weight bytes W, inference microbatch B, workspace A(B,n), and retained history H_d. Distinguish generated, scored, deduplicated, selected, and stored populations.

Write N_d = F_d b_d only when every parent generates exactly b_d candidates; otherwise use a sum over parents or N_d ≤ F_d b_max. Beam width is an upper bound on retained states, not on candidate population or earlier-depth history. State whether rejected candidates are materialized, streamed, or regenerated.

## Work and wall time

Account separately for generation, state construction, feature encoding, scoring/model evaluation, hashing, exact comparison/deduplication, selection/sorting, communication, I/O, and synchronization. Define per-state scoring/model work C_model(n, precision, architecture), feature/state construction work, and batch efficiency separately; weight bytes W do not determine inference work. Give operation counts or cost functions before reducing to big-O.

A useful accounting form is:

T_total = T_setup + Σ_d T_layer,d + T_output,

T_layer,d = T_critical_path({T_stage,d,i}, transfer schedule, dependencies).

For sequential stages, stage costs add; for genuinely overlapped stages, use the measured or justified overlap/critical path. Do not add everything and then call the result a tight bound; do not use `max` without proving overlap.

Let N_d,i be work owned by device i. Wall time depends on the maximum assigned work and hardware differences, not just N_d/p. Define imbalance κ_d = p max_i N_d,i / N_d for equal-cost work. For unequal-cost items, define imbalance from estimated/observed work, not item count. Distinguish a balance assumption from a guarantee.

Communication requires bytes/messages per phase, topology, latency/bandwidth assumptions, contention, and skew. Replicated inference does not imply communication-free selection or deduplication. Distinguish strong scaling at fixed workload from weak scaling at growing workload. Identify serial/setup costs and report the workload range where a claimed approximation applies.

## Peak memory is a maximum of live allocations

For device i, enumerate simultaneously live allocations. A generic accounting template is:

M_i,peak = max_phase [W_i + S_frontier,i + S_candidates,i + S_keys/index,i + A_i(B,n) + S_history,i + S_comm,i + S_runtime,i].

Replace every term with actual layouts, capacities, data types, alignment, allocator overhead, double/ring buffering, scratch space, and lifetimes. Include headroom explicitly rather than hiding it in a big-O term. Account for host RAM, pinned buffers, checkpoint/storage volume, and total cluster memory separately from per-device memory.

Replicated model weights cost W per device, pW in aggregate. Partitioning states does not automatically divide W or global metadata by p. State whether history is O(F_d), O(Σ_{j≤d} F_j), a parent-pointer chain, compressed trace, or recomputed. Include trace reconstruction and its tradeoffs. Candidate chunking may lower peak memory while adding passes or synchronization; describe both effects.

## Expected, worst-case, and measured claims

Expected O(1) hashing needs its assumptions; worst-case collisions, rehashing, and exact equality checks may differ. Sorting, top-k, and deduplication costs depend on implementation and the relevant N/U/k, not only beam width. Separate proven bounds, estimates, capacity limits, and benchmarks.

Benchmark records must identify hardware/count, model and precision, input shapes, batch/concurrency, software versions, warmup, repeats, variability, included stages, and timing method. State exactly what is unavailable. A single-device measurement does not establish multi-device speedup. Theoretical FLOP/s, bandwidth rooflines, perfect load balance, and ideal p-fold scaling are modeled ceilings, not measurements.

When evidence is incomplete, provide a parameterized formula and mark missing measurements. Do not manufacture constants, invent scaling curves, extrapolate a single timing into a guarantee, or silently substitute average memory/work for peak/worst-case bounds.
