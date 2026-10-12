# Set identities, multiplicities and equality

All families and sets here are finite.

## Decomposition of a layer

Let A_1,...,A_m be subsets of V and B subset V. Distributivity gives

(union_i A_i) minus B = union_i (A_i minus B).

If P_1,...,P_n partition V, then

(union_i A_i) minus B
= disjoint union_j ((union_i A_i) intersect P_j minus B).

Proof. Membership on either side means membership in some A_i and not in B. Every such vertex belongs to exactly one P_j. This proves both equality and disjointness.

Since Succ(union_i F_i)=union_i Succ(F_i), any decomposition F=union_i F_i gives

Succ(F) minus B = union_i (Succ(F_i) minus B).

The union on the right need not be disjoint. In the diamond s->a,s->b,a->t,b->t, the successor sets of {a} and {b} both contain t.

## Occurrences versus distinct elements

A finite multiset is a multiplicity function mu:V->nonnegative integers. Let

C=sum_v mu(v), and U={v:mu(v)>0}.

For any B subset V,

C=(C-|U|)+|U intersect B|+|U minus B|.

Proof. U is the disjoint union of U intersect B and U minus B. Add C-|U| to this cardinality identity. Also C-|U|=sum_{v in U}(mu(v)-1).

The term |U intersect B| counts distinct elements, not occurrences. Replacing it by sum_{v in U intersect B}mu(v) increases the right side by sum_{v in U intersect B}(mu(v)-1).

Union and minimum are idempotent: X union X=X, and min(a,a)=a. Addition of nonnegative integer multiplicities is not idempotent for a>0: a+a differs from a. Thus the support of a multiset determines existence but not multiplicity.

## Injectivity and images of sets

For a map f:V->K, the following are equivalent:

1. f is injective.
2. For all subsets X,Y of V, f(X)=f(Y) implies X=Y.

Proof. If f is injective, every image element identifies one original element. Conversely, if f(u)=f(v), then the images of {u} and {v} coincide, so condition 2 implies u=v.

The tuple (cardinality, sum, bitwise xor) is not injective on finite sets of nonnegative integers: {0,3} and {1,2} both have cardinality 2, sum 3 and xor 3.

The exact indexed BFS layers determine the distance function by delta(v)=d for v in F_d and infinity for vertices in no layer. Conversely, the distance function determines each F_d. Layer cardinalities alone do not: the graphs with sole edges s->a and s->b have the same layer cardinalities but different distance functions on the common vertex set {s,a,b}.
