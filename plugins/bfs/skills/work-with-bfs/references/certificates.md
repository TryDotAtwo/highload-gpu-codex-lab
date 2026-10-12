# Certificates for distances and reachability

Let G=(V,E) be a finite directed unit-cost graph, and S a nonempty set of sources.

## Path upper bounds

A walk of length L from S to t proves delta_S(t)<=L, by the definition of a minimum. It does not prove equality. In the graph s->a->t together with s->t, the length-2 path exists but delta_s(t)=1.

## Full distance certificate

Let S subset U subset V and d:U->nonnegative integers. Suppose:

1. d(s)=0 for every s in S.
2. For every v in U, an original-graph walk from S to v of length d(v) exists.
3. Every original-graph successor v of every u in U lies in U, and d(v)<=d(u)+1.

Then U is exactly the reachable set and d(v)=delta_S(v) for every v in U.

Proof. The witnesses in condition 2 give U subset Reach(S) and delta_S(v)<=d(v). Successor closure and S subset U imply Reach(S) subset U by induction on walk length. Along any shortest source-to-v path of length k, condition 3 gives d(v)<=d(s)+k=k. Combining the inequalities proves equality.

A sufficient witness for condition 2 is a predecessor chain along original edges whose labels decrease by exactly one at each step and whose depth-zero endpoint belongs to S. Reversing this chain gives a walk of exactly d(v) edges from S to v.

## Radius certificate

Fix a nonnegative integer r. Keep conditions 1 and 2, require d(v)<=r for all v in U, and replace condition 3 by:

For every u in U with d(u)<r, every original-graph successor v of u is in U and satisfies d(v)<=d(u)+1.

Then U=B_r(S)={v:delta_S(v)<=r}, and d equals delta_S on U.

Proof. Witnesses of length at most r give U subset B_r(S). On any source walk of length k<=r, induction shows that its i-th vertex is in U with label at most i. For i<k the label is below r, so the next edge is covered by the hypothesis. Thus B_r(S) subset U. Applying the same induction to shortest paths proves d(v)<=delta_S(v), and witnesses prove the reverse inequality.

No successor condition is needed at vertices labeled exactly r. At r=0, the witness condition forces U=S. A target outside a certified B_r has distance greater than r, possibly infinity.

## Unreachability certificates

If a set U contains S, is successor-closed, and excludes t, then t is unreachable from S. Proof: induction on walk length keeps every reachable vertex inside U.

A useful special case is an invariant I:V->K with I(u)=I(v) on every edge. If I(s)=c for all sources and I(t) differs from c, no source-to-t walk exists, since I is constant along every walk.

A finite-radius miss alone does not supply such a certificate: a chain of length r+1 reaches a target outside B_r.
