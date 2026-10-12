# Mathematical and provenance contracts

## State, word and accounting

We work with the finite group GL(n,2), all ordered CNOT pairs c != t, unit gate
cost, no connectivity restriction. Applying a list [G1,...,GL] from left to right
to rows produces GL...G1 M. Check a reported encoder by applying its list to I;
check a reduction by applying its list to M and obtaining I. All CNOTs are
self-inverse, but the inverse of a word reverses its order.

Use full binary arrays or a specified little-endian row-bit encoding; store both
file SHA-256 and the named canonical matrix-hash convention. Two serialization
hashes may differ for the same matrix; never compare hashes with unknown encoding.
The parameters [[n,k;c]] do not determine a unique encoder or its wire order.

Paid shared-basis compilation has D=T B S^-1 and gate price
2 L_S + 2 L_T + popcount(D). Preparation is shared over a block, then uncomputed.
For adjacent blocks count the actual concatenated program after valid cancellations.
No arbitrary GL(n,2) basis change is free. All-to-all unit-cost symmetries include
simultaneous wire relabeling, inverse and transpose with the correct word mapping.
For encoder words: inverse reverses; transpose reverses and swaps (c,t); a wire
permutation relabels both indices. Always recheck the mapped-back full word.

## Exact labels, bounds and losses

A known word of length U proves d(M,I) <= U. Take the minimum over verified
certificates. It does not prove d=U, nor that the first action is optimal.
Even removing a suffix step need not lower true distance: a word followed by its
reverse returns to I. Uncertified monotonic ranking was removed after this
counterexample; old `s128_brank_seed1700_v1` is invalid for distance-field claims.

Valid cheap LB: max(rank(M-I), changed rows, changed columns). Exact labels require
independent exact BFS or LB=verified UB. Exact forest targets have a constructive
word matching the changed-row LB. Rank alone is usually weaker than these counts.

For a paid macro M→N of cost c, d(M)<=c+d(N) and |d(M)-d(N)|<=c. A macro yields a
valid constraint, but a loose inactive constraint supplies no training signal.
Ranking M above N is justified only by a separating certificate, e.g. LB(M)>UB(N).

V(I)=0 exactly; other outputs nonnegative. The Bellman residual is
V(M) - min_a(1+V(aM)) for nonterminal M. To obtain its full active-branch gradient,
choose argmin over all allowed successors under no_grad, then recompute V(M)
and selected V(aM) under autograd at identical weights. Do not detach the second
value, update weights in between, or change dropout masks. Test against naive
all-neighbor autograd, including tie handling. Terminal has a boundary condition,
not a cost-one self-loop backup. A detached target is allowed in separately named
auxiliary distillation; it is not the same objective.

## Claims we must not make

- Hamming distance is not the CNOT word metric. A transvection I+E has E²=0;
  this does not supply a general exp/log chart over F2 or differentiable states.
- Convex objectives in free graph fields/flows need not remain convex after a
  nonlinear neural parameterization or restriction to a different sector.
- Full gradients on sampled states are not training on the entire finite group.
- One-column heat marginals are not the joint matrix heat density, unique
  coordinates, an optimal policy, or a certified distance lower bound.
- A checked exact local atlas/window optimizer does not make the global
  heuristic compiler optimal.
- Passing tests establishes specified contracts, not benchmark superiority.

## Data boundary

The allowed benchmark matrix source is `01_shared_basis_stage17/source_snapshot/inputs`.
Generate training goals independently using own walks, exact families and paid
basis compiler. Record all seeds, generator versions and certificate lineages.
Exclude direct validation/benchmark state overlap at each replay refresh;
check symmetry-related overlap when claiming symmetry generalization. Exact
canonicalization is not assumed cheap; finite known augmentations can be checked.

Do not use `03_kelipaev_handoff`, its archive, chains or derived labels, or copy
its search implementation. Historical mixed comparison reports are not new data
authorization. EA results in old reports came from a different input collection;
do not reuse those matrices without independently allowed provenance. Installation
cleanup, unrelated chats and personal information are outside this plugin.
