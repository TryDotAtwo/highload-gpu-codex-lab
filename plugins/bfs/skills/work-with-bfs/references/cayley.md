# Group actions and graph quotients

## Cayley graphs

Let G be a finite group with identity e and an allowed set A of generators. The directed right Cayley graph has edges g->ga for a in A, all of cost one.

Left multiplication by h preserves every labeled edge:

g->ga becomes hg->(hg)a.

It is a bijection, so delta(x,y)=delta(e,x^{-1}y). If A is inverse-closed, the underlying graph is undirected. Reverse traversal uses g->ga^{-1}; reversing an edge does not require a^{-1} to belong to the forward alphabet.

If A is enlarged to A', every A-walk is also an A'-walk. Thus delta_{A'}(x,y)<=delta_A(x,y). Equality is not automatic. For a cyclic group of order 6, the word a a has length 2 under {a}, but a^2 is one move under {a,a^2}. The order of a alone does not determine geodesicity in a larger alphabet.

## Right actions and Schreier graphs

Let G act transitively on a finite set X on the right, with (x g)h=x(gh). Fix x0 and its stabilizer H={g:x0 g=x0}. Then

x0 g=x0 k iff gk^{-1} is in H iff Hg=Hk.

Proof. Apply k^{-1} to the equality of states; the converse follows by multiplying back by k. This also proves the coset equivalence.

Hence X is identified with the right cosets Hg, written H\G, and the transition by a is Hg->Hga. It is well-defined: replacing g by hg with h in H leaves the resulting right coset unchanged. This is the Schreier graph of the action and alphabet.

Transitivity of the action alone does not imply equal distance-layer sizes from all vertices. The map x->xb turns an a-labeled edge into an edge with action b^{-1}ab. Conjugation need not preserve A.

Counterexample. On {1,2,3}, define the right action of S3 by x g=g^{-1}(x) and take A={(12),(23)}. Apart from endpoint loops, the graph is 1-2-3. The layer sizes are (1,1,1) from an endpoint and (1,2) from the middle, although the action is transitive.

## Left and right cosets are different objects

For left cosets gH, the element ga belongs to gH exactly when a belongs to H, by cancellation of g.

The rule gH->gaH defines a permutation of left cosets exactly when a normalizes H:

a^{-1}Ha=H.

Proof. Independence of the representative g requires haH=aH for every h in H, equivalently a^{-1}Ha subset H. Since G is finite, containment is equality. Equality also makes the inverse rule gH->ga^{-1}H well-defined.

This is distinct from Hg->Hga, which is well-defined for every a. The identification x0 g <-> g^{-1}H uses left cosets instead, but the transition then becomes g^{-1}H -> a^{-1}g^{-1}H.

## Quotient distances

Let ~ be an equivalence relation on vertices of a finite directed graph. Its quotient has classes as vertices and an edge C->D whenever some original edge joins those classes.

Projection sends every original path to a quotient walk of the same length. Therefore

delta_Q([x],[y])<=delta_G(x,y).

A stronger identity holds if equivalent vertices have identical sets of successor classes:

u~v implies { [z]:u->z }={ [z]:v->z }.

Under this hypothesis, for any class C,

delta_Q([x],C)=min_{y in C} delta_G(x,y).

Proof. Projection gives one inequality. For the other, lift a quotient path one edge at a time, starting at the particular vertex x. The successor-class hypothesis guarantees the next class can be reached from every current representative. The lifted path ends at some y in C and has the same length. The argument also proves equivalence of reachability.

For labeled-word lifting the same hypothesis is imposed separately for each label. For distances to a target set T that is a union of classes, the identity gives exact distance to T.

It does not give distance to a selected representative. With only the edge x->a and classes {x},{a,b}, the successor-class hypothesis holds, but the quotient distance to [b] is 1 while delta(x,b)=infinity.

Nor does it preserve path counts: identifying a and b in the diamond s->a,s->b,a->t,b->t gives a quotient with one length-2 path, although the original graph has two.
