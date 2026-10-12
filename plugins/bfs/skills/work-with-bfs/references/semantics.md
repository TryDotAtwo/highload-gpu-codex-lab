# Definitions, layers and shortest paths

## Definitions

Let G=(V,E) be a finite directed graph, E a subset of V x V, and S a nonempty source set. The length of a walk is its number of edges. Let delta_S(v) be the minimum length of an S-to-v walk, or infinity if none exists. A minimum-length walk has no repeated vertex, since deleting a cycle shortens it.

For A subset V, define Succ(A)={v: there exists u in A with (u,v) in E}. Define

- F_0=S, B_0=S;
- F_{d+1}=Succ(F_d) minus B_d;
- B_{d+1}=B_d union F_{d+1}.

## Layer theorem

For every nonnegative integer d,

F_d={v:delta_S(v)=d}, and B_d={v:delta_S(v)<=d}.

Proof. The claim holds at zero. Every v in F_{d+1} has a walk of length d+1, and v not in B_d excludes a shorter walk. Conversely, a shortest walk to a vertex of distance d+1 has a predecessor of distance d; otherwise shortening its prefix would shorten the whole walk. That vertex is therefore in Succ(F_d) minus B_d. Induction proves both equalities.

Corollaries:

- The layers are pairwise disjoint.
- If F_{d+1} is empty, every subsequent layer is empty and B_d is the reachable set.
- If all predecessors at distance less than d have had their successors included, a vertex first found as a successor of F_d has distance d+1. The order within F_d does not change that distance.
- Multi-source distance is delta_S(v)=min_{s in S} delta_s(v); it is not the collection of separate single-source distances.

For an edge u->v with u reachable, delta_S(v)<=delta_S(u)+1, by appending that edge to a shortest walk. In an undirected graph, applying this in both directions gives absolute depth difference at most one. The directed converse fails: a long directed chain with an edge from its last vertex back to S can drop arbitrarily many levels.

## Walk length versus first-arrival distance

Let W_0=S and W_{d+1}=Succ(W_d). Then W_d is the set reachable by a walk of exactly length d, by induction on walk length. Consequently,

F_d = W_d minus the union of W_i for 0<=i<d.

Adding unit-cost self-loops leaves distances unchanged: remove loops from any walk without changing its endpoints. It can change W_d. For example, a single isolated source has W_1 empty; adding its self-loop gives W_1=S while F_1 stays empty.

For a finite directed multigraph, let A_uv be the number of edges u->v. The entry (A^k)_uv counts walks of length k, with different edge sequences counted separately and repeated edges allowed. This follows because multiplication sums the possible last-edge decompositions. The Boolean version of the same product records existence instead of multiplicity.

## Shortest paths and their number

Fix a single source s and a reachable vertex v. Its shortest predecessors are

Pred*(v)={u:(u,v) in E and delta_s(u)+1=delta_s(v)}.

Choosing one shortest predecessor per non-source reachable vertex gives a shortest-path tree: depths strictly decrease along parent edges and terminate at s. For edge-distinct path counts in a multigraph,

c(s)=1; c(v)=sum_u m(u,v)c(u),

where the sum runs over shortest predecessors and m(u,v) is edge multiplicity. Proof: partition shortest paths to v by their last edge. The shortest-path subgraph is acyclic because depth increases on each edge.

In the diamond s->a, s->b, a->t, b->t, the distance to t is 2 but c(t)=2. One incoming shortest path establishes the distance once earlier layers are complete; it does not give the final count. For a target at depth D>0, its count depends on the contributions from depth D-1, not on outgoing edges from depth D. At D=0, the sole shortest path is empty.

## Canonical shortest words

Suppose edges carry labels in a totally ordered alphabet, and each label acts as a partial function on states. Order words first by length, then lexicographically (shortlex).

For a fixed length, a forward extension p followed by a is ordered by the pair (lexicographic rank of p, rank of a). A reverse-built suffix a followed by q is ordered by (rank of a, lexicographic rank of q). These identities follow from the first differing position.

A prefix of a shortest word is shortest to its endpoint; a prefix of the canonical shortest word is also canonical, since replacing it by a shorter or lexicographically smaller word would improve the whole word. Thus the pair comparisons characterize canonical shortest-word recurrences. An arbitrary numerical vertex order has no such implication: renaming vertices leaves word order unchanged.
