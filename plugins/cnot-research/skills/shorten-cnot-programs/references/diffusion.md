# Random walks from I and diffusion

## Implemented process

Uniform CNOT among n(n-1) physical gates. Continuous-time generator Q=P-I: one
expected gate per unit t. Observe Poissonized walks starting at I at t=n*tau,
tau=(1/4,1,4,16). Inter-observation step counts are independent Poisson increments.
Do not forbid immediate reversals or returns: that would change the process and
invalidate comparison to exp(tQ). A different nonbacktracking data generator is
allowed only as a separately specified sampling process with separate theory.

Every reverse walk is a certificate of UB, not the shortest distance. Deduplicate
states and keep shortest verified certificates. Long walks can mix and make
trajectory length almost unrelated to distance. Stratify length/time and structural
features; do not interpret large diffusion time as a farther exact distance label.

## Exact marginal projection, numerical evaluation

For column j retain a=M[j,j] and k=ones outside its diagonal. w=a+k. State space
has 2n-1 states, excluding (0,0). Nonzero rates:

```
(a,k) -> (1-a,k) : k/[n(n-1)]
(a,k) -> (a,k+1) : (n-1-k)*w/[n(n-1)]
(a,k) -> (a,k-1) : k*(w-1)/[n(n-1)]
```

Diagonal is minus total outgoing rate. Weight-only projection has birth
w(n-w)/[n(n-1)] and death w(w-1)/[n(n-1)]. From initial (1,0), compute
scipy.linalg.expm(n*tau*Q), divide orbit mass by choose(n-1,k) to get a specific
column's marginal. Network feature is (log p + log(2^n-1))/n, p clipped below1e-30.
Clipping hides very small probabilities; it is a numerical implementation choice.

`CNOTColumnProjection.lean`, `ColumnMomentAlgebra.lean`, `CNOTGateKernel.lean` are
local theory pointers. The refined (a,k) projection was numerically checked against
all168 GL3 states at t=.2,3,12 to1e-11; it was not newly formalized in Lean here.

Columns are dependent. Do not multiply these marginals and label the result joint
matrix heat probability. The profile does not uniquely locate a group element.
It is a multiscale descriptor, not geodesic distance. Moreover diagonal/column
weights already enter the encoder: these channels add an analytic parameterization,
not previously missing information. A zero ablation gain is entirely possible.

## Integration and paired study

`DiffusionField(ActionField)` adds zero-initialized value/action correction MLPs,
with the full matrix still available and Bellman still differentiated. Both on/off
experiments get identical own basis replay plus walks and compute/save profiles;
off does not feed the profile to the model. Files replay_initial, validation and
walk_heat_profiles are byte-identical on/off. Forty-eight training and12 validation
walks per size, four times, one640-update round, seed2700, warm v4.

New gradients are nonzero. Small benchmark lengths tie21/54/102 for both models,
versus Hamming20/44/70. This experiment did not show a feature gain. Heat-on HGP58
is234 vs159; BB72 failsdepth480 for both neural and Hamming. Heat-off large pending.
Training curriculum ends n34, so58/72 are out-of-size tests. No broad impossibility
claim follows from this one seed/architecture.

## Next hypotheses (not implemented results)

1. Improve sampling with certified UBs, exact examples and mixing diagnostics.
   Keep the stochastic-process definition and diffusion clock fixed in each ablation.
2. Test diffusion-time classification/reconstruction as auxiliary representation
   tasks, with ambiguous times modeled probabilistically. Time prediction is not
   distance regression. Select any weight on validation, not benchmark lengths.
3. Two-column or mixed channels can contain correlation missing from single-column
   profiles. First derive an actually closed projection, prove/verify rates against
   full small GL graphs, and bound state count/time. If projection is not closed,
   label the approximation and measure its error. Do not assert closure by analogy.
4. Landmark/heat features need enough landmark identity to distinguish regions,
   and an explicit compute/storage budget. Do not silently replace group distance
   by coordinate distance or independent-marginal products.
5. Cache per-(n,tau,device,dtype) heat tables; avoid valid.sum().tolist() and repeated
   host synchronization per forward. Preserve padding invariance and measure impact.
