# Reverse balls and distance bounds

All radii below are nonnegative integers; edges have unit cost.

## Reverse distance

Let G^op contain v->u exactly when G contains u->v. Then

delta_{G^op}(t,v)=delta_G(v,t).

Proof. Reversing a walk reverses its endpoints and preserves its length; reversing twice is the identity. Thus walks of each length correspond bijectively.

Define the forward ball B_K(x)={v:delta(x,v)<=K} and the reverse ball T_R(t)={v:delta(v,t)<=R}.

## Two-ball theorem

B_K(x) intersect T_R(t) is nonempty if and only if D=delta(x,t)<=K+R.

When the intersection is nonempty,

D=min_{v in B_K(x) intersect T_R(t)} (delta(x,v)+delta(v,t)).

Proof. An intersection vertex gives a concatenated walk of length at most K+R. Conversely, on a shortest path of length D<=K+R, choose an integer i with

max(0,D-R)<=i<=min(K,D).

The vertex at position i belongs to both balls. Every concatenation has length at least D, and this one has length D, proving the minimum formula.

The formula for the minimum is conditional on nonempty intersection. Empty finite-radius intersection implies D>K+R, not necessarily D=infinity. For example, a directed chain of length K+R+1 has finite distance and empty intersection.

## First hit in an exact reverse ball

Enumerate all directed walks from x of lengths 0 through K, including the empty walk, in nondecreasing length. Membership is in exactly T_R(t). For finite D, the minimum length j of any walk ending in T_R(t) is

j=max(0,D-R).

Proof. A hit after j steps gives D<=j+R. If D<=R, the empty walk attains zero. If D>R, the prefix of length D-R of a shortest path attains the lower bound.

Therefore a hit occurs in the enumeration if and only if D<=K+R. The first hit, concatenated with a shortest suffix to t, is a shortest x-to-t path:

- For D<=R, its prefix is empty and its suffix has length D.
- For R<D<=K+R, its prefix has length D-R. Its shortest suffix has length exactly R, since a shorter suffix would contradict the definition of D.

Ties among prefixes of the same length do not affect the conclusion. At D=0 the result is the empty path. At K=0 only the empty prefix is considered; at R=0 the reverse ball is {t}. If D=infinity, there is no hit.

## Which hypotheses support which conclusions?

A complete miss over lengths 0 through K gives D>K+R regardless of enumeration order or stored suffix lengths. This is the two-ball theorem, and suffix witnesses do not enter its proof.

For an arbitrary hitting prefix of length j<=K and a valid suffix of length l, concatenation gives D<=j+l. If membership is in the exact ball, it also gives D<=j+R<=K+R, even when that particular suffix is longer than R. Without length order and shortest suffixes, first-hit optimality does not hold in general.

Counterexample to arbitrary order: in the graph with paths x->a->t and x->b->c->d->e->t and no other edges, take R=4 and K=1. Checking x->b before the empty prefix returns length 5 with a shortest suffix, whereas D=2 and the empty prefix already lies in T_R.

If a set Q contains T_R but also other vertices, a complete miss against Q still implies D>K+R, by inclusion. First-hit optimality need not hold, even with shortest suffixes and length order. Take x->a->t and x->b->c->t, R=K=1, and Q=T_1 union {b}. Checking x->b before x->a returns 3 instead of 2. Both prefixes have length one and x is not in Q.

Q may even contain a vertex from which t is unreachable; a membership hit then provides no path unless a valid suffix exists. Conversely, an incomplete subset of T_R can miss x when D<=R, so its miss does not certify the original radius.

## Unequal edge costs

Ordinary hop distance is not general weighted distance. With edges s->t of weight 10 and s->a, a->t of weight 1, the one-edge path is hop-shortest but not weight-shortest.

For a finite graph with nonnegative weights w, let L_k(v) be the minimum cost of a source-to-v walk using at most k edges. Set L_0(s)=0 and L_0(v)=infinity elsewhere. Last-edge decomposition gives

L_{k+1}(v)=min(L_k(v), min_{u->v}(L_k(u)+w(u,v))).

Removing a cycle does not increase cost, so L_{|V|-1} equals the shortest weighted distance, including when zero-weight cycles exist. For unit weights this distance agrees with the BFS layer index.
