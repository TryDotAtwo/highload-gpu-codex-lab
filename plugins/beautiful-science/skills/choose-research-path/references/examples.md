# Constructed examples and their limits

These are generic analytical examples, not reports of real experiments. The executable witnesses in the plugin's tests verify small arithmetic/logical facts, not the general effectiveness of this method.

## A symmetric problem need not have a symmetric solution

For f(x) = (x² − 1)² on the real line, f(x) = f(−x), but the global minimizers are +1 and −1. The reflection-fixed point x=0 is not a minimizer.

A preference for a “symmetric optimum” becomes a testable claim only with additional conditions. The example refutes the implication from invariant objective to reflection-fixed minimizer. It does not refute symmetry methods, nor does it rule out sufficient conditions in another problem.

**Next work:** identify the needed existence/uniqueness/convexity conditions and prove their role. Preserve the symmetry reduction when it is actually valid.

## Simple decay versus multiple mechanisms

A(t)=exp(−kt); B(t)=w exp(−k1 t)+(1−w) exp(−k2 t), with 0<w<1.

At k1=k2=k these outputs coincide exactly for all t. Repeated measurement of the same output cannot identify one versus two mechanisms at that parameter point. For unequal rates, the second derivative of log B at t=0 is w(1−w)(k1−k2)²; the single exponential's log curvature is zero. This gives a potential contrast, not a guarantee that noisy short-window data can estimate it.

**Decision depends on goal:** a single exponential may be adequate for short-horizon prediction while mechanism identification remains unresolved. A longer window may expose a slow component but reduce signal-to-noise. A different observable or selective intervention needs its own validation. Rejection of A does not uniquely prove B.

## An expensive honest proof versus a short unsupported shortcut

A long reduction has explicit finite obligations and independently checked certificates for most of them. A one-line symmetry shortcut works only on selected small symmetric objects. Length is not the right discriminator.

**Continue:** the long route if its reduction covers the actual class and the remaining obligations are meaningful targets. Mark the general theorem unproved until they close. **Bounded test:** examine the shortcut's arbitrary-to-symmetric bridge before treating it as a competitor for the universal goal. A certificate pipeline can be scientifically strong even if nobody finds every line beautiful.

## A plateau without an optimization hypothesis

The objective is at least 5% latency reduction. An unchanged comparison yields 0.4% with interval [−0.8%, 1.6%], under assumptions still needing a measurement audit. The interval includes zero and lies below the practical target. These are distinct facts.

**Next work:** diagnose a named concern such as drift or dependence; establish whether the interval is valid. If it is, repeated unchanged runs are not a route to the required effect. A changed bottleneck hypothesis or implementation can justify another comparison. No universal “ten runs” or “two-hour” stopping rule follows from these numbers.

## A useful empirical model with no satisfying mechanism

A complicated predictor generalizes to prespecified held-out settings and has calibrated uncertainty within the operating regime. A compact mechanistic model misses a transition.

**Continue prediction:** favor the evidence-supported predictor for the predictive objective, with appropriate monitoring and boundaries. **Continue explanation separately:** use the mechanistic failure to form discriminating scientific questions. Fitted interactions are not physical mechanisms. Neither aesthetics nor complexity alone chooses the winner.
