---
name: validate-beam-search-results
description: Use when validating GPU beam-search correctness, first-solution versus collect-all behavior, reflection, BFS-touch solutions, multi-rank output, replay validity, or solution-length quality.
---

# Validate Beam Search Results

## Required Layers

1. **Structural:** both ranks started, expected hardware, no fatal/OOM/overflow, requested/effective beam and capacities logged.
2. **Depth flow:** frontier sizes, per-stage jobs, thresholds, rank exchange, and exact final depth row are coherent.
3. **Semantic:** every reported move sequence replays from initial to target under the puzzle rules.
4. **Mode:** first-solution stops according to contract; collect-all preserves every available solution up to the explicit capacity without silent truncation.
5. **Quality:** compare solve rate and solution-length distribution against the reference scorer/search at the same beam and depth.

Reflection/orientation and BFS-touch must be recorded with the final orientation and touch radius. Validate transformed solutions in the original puzzle frame.

Intermediate score, top-k, frontier-hash, and rank-correlation checks are diagnostic. The final acceptance metric is replay-valid task output and solution quality.

Use cheap 10–100-state small-beam cohorts for regression curves, then a few large-beam/deep confirmations. Preserve all configs, seeds, puzzle IDs, logs, and artifacts needed to reproduce the comparison.
