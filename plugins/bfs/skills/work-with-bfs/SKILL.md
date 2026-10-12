---
name: work-with-bfs
description: Use when reasoning mathematically about breadth-first search (BFS), exact distance layers, shortest paths and their counts, reverse balls, Cayley or Schreier graphs, graph quotients, or set decompositions of a BFS layer.
---

# Mathematics of BFS

A mathematical reference: definitions, propositions with explicit hypotheses, proofs and counterexamples. The subject is the graph defined by those hypotheses.

Unless a section states otherwise, the graph is finite and directed, every edge has cost one, distances to unreachable vertices are infinity, and all sets and equalities are exact.

Read the references relevant to the mathematical question:

| Topic | Reference |
|---|---|
| Distance layers, walks, shortest paths and canonical words | [Definitions and layers](references/semantics.md) |
| Reverse distance, two balls, first intersection and weighted-distance recurrence | [Balls and distance bounds](references/variants.md) |
| Cayley/Schreier graphs, cosets and quotient distances | [Group actions and quotients](references/cayley.md) |
| Unions, partitions, multiplicities and injectivity | [Set identities](references/identities.md) |
| Path bounds, exact-distance certificates and unreachability | [Distance certificates](references/certificates.md) |

Apply each proposition only under its stated hypotheses. The proofs are ordinary mathematical arguments, not machine-checked formal proofs.
