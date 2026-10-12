# Method lineage and usable theory

## Own stage17 compiler

`source_snapshot` is immutable provenance. The original compiler constructs useful
physical parity bases shared across transfers, pays preparation once per block,
does the transfer and restores the basis. It uses core popcount as the number of
physical transfers. That fact does not identify it with a Hamming beam over matrices.

Its gradient optimizes the exact expected paid cost over independent local
switches, followed by conditional rounding. The expectation is multilinear, not
generally convex. Wide blocks can use this route; narrow blocks now have an exact
atlas. The useful compiler quantity is total physical price, not just sparse core.

Own additions in `improved/code`:

- `shared_synth.py`: discrete local improvements of rounded basis switches,
  accepted only if true preparation+core cost strictly decreases.
- `exact_basis.py`: GL(4,2) atlas (20,160 elements) and shortest local words;
  optimizes paid block cost exactly inside chosen groups. Grouping remains heuristic.
- `forest_exact.py`: recognize a proved exact forest family. None of the nine
  original BB/HGP goals matched, so this recognizer did not shorten that table.
- `general_macro.py`: Gaussian seed for general invertible matrices, shear
  grouping and dynamic programming, paid basis transition cancellation, reorder
  compatible blocks. Removes the stage17 unit-diagonal applicability restriction.
  Quality still depends on initial decomposition. Historical one-second reorder
  cap survives in this legacy module; policy teacher has a no-time-cap copy.
- `stage28_exact.py`: exact replacement of short windows (up to four gates by
  at most three). This is a restricted implementation of defect repair.
- `defect_repair.py`: two deletions plus a searched single insertion in bounded
  windows. Old helper has wall-time limits; inspect before any new no-time-cap run.
- `neural_large_windows.py`: commuting-window collection on four wires followed
  by learned local search. The same windows with Hamming achieved the same lengths.

## Frontier stages after 17: implementation review, not a theorem certification

This mapping is based on the project's saved synthesis review and implementations.
Before importing a new theorem, read its actual source statement, hypotheses and
normalization. The plugin does not certify every proof in the original chat.

| Stages | Lesson and status |
|---|---|
| 18 | General complexity and exact restricted families; no general cheap exact evaluator. |
| 19–20 | Convex TV/cut action and a central sector require assumptions not proved for arbitrary shared-basis blocks. Do not replace stage17 loss by name alone. |
| 21–22 | Geodesic action / finite eikonal on the full matrix graph motivate value learning. Exact evaluation on the whole graph does not scale. |
| 23 | Convex entropic flow lives on graph flows; exact forest family is implemented. Need a justified projection before applying flow results to local basis parameters. |
| 24–25 | Further exact structured families are candidates for recognizers/labels, conditional on matching hypotheses; not already integrated benefits. |
| 26–27 | Lower bounds and the independent-switch endpoint-penalty trap. Preserve the matrix constructively whenever possible. |
| 28 | Exact defect correction and program rearrangement motivate window/postprocessing mechanisms. Full global insertion transport is not implemented. |
| 29–31 | Small field kernels, mixed channels and Krylov projection suggest representations. They do not directly return a general paid CNOT program. |

## Symmetries and postprocessing

Run the OWN compiler/search on transpose/inverse/relabel targets, map back and
verify; keep the best complete word as UB. Attribute a gain to the symmetry
wrapper separately from the scorer. Use same seeds/transforms and budgets for
paired scorers. Do not relabel a run whose target changed without recording it.

Avoid expensive full orbit canonicalization in every beam step until measured.
Coarse collision keys can merge inequivalent states and silently prune solutions.
Bytewise full-state dedup is the correctness baseline. Exact local windows can
fail to improve already smooth paths; zero replacements is a meaningful outcome.

## Small graph gradient / neural experiments

`global_gradient.py` builds full GL(n,2) only for n<=4 and optimizes a graph field.
Selected tests matched independent BFS, not all-state policy optimality for all
regularization parameters. `neural_global.py` learns exact GL4 distances with a
small MLP: saved review reports 200/200 optimal held-out solutions at beam4,
Hamming173/200, one seed/200 matrices. This is a small-graph result, not evidence
for HGP/BB extrapolation. See current files before reproducing numbers.
