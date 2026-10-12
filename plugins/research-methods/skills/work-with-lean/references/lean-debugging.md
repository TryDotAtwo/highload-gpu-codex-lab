# Lean debugging from actual failure modes

Use the installed revision's source or a small compile probe. These examples were observed on Lean 4.34.0; they are not promises about every Mathlib release.

## Data versus proofs

`SimpleGraph.Walk A B : Type`, so a function constructing a walk is a `def` (possibly `noncomputable def`), not a `theorem`. A theorem may state an existential proposition about a walk. Check the result sort before writing the declaration. Avoid putting computational data into an opaque theorem and then trying to reduce it.

## Instances and imports

Importing basic `ZMod` definitions does not necessarily import the field instance. In the inspected revision, `Mathlib.Algebra.Field.ZMod` supplies `Field (ZMod p)` under primality; `Fact (Nat.Prime 2)` already exists. Verify with `#synth Field (ZMod 2)` before adding redundant instances.

The inspected `Matrix.isUnit_iff_isUnit_det` is in `Mathlib.LinearAlgebra.Matrix.NonsingularInverse`. Searching an imported name and adding its actual module is better than inventing a synonym. Check namespaces and explicit versus implicit arguments.

## Structured relations

In the inspected revision, `SimpleGraph.symm` expects `Std.Symm Adj` and `loopless` expects `Std.Irrefl Adj`. They are structures, not bare propositions with visible binders. Use the constructor first, or define fields `symm.symm` / `loopless.irrefl` directly. Projection `G.loopless.irrefl` is callable; `G.loopless` itself is not a function. `#print SimpleGraph` and nearby examples settle this before editing.

## Finite enumeration

`fin_cases` in the observed failures expected a variable reference, not `D i` or `t.c`. Prove a small reusable lemma on `x : ZMod 2`, then apply it to the expression. If enumeration produces two obvious constructor cases, `Or.inl rfl` / `Or.inr rfl` may close them while broad simplification or decision synthesis fails. Read the actual goal; do not assume the printed numeral exposes all elaborated types.

## Dependent endpoints, transport, and opacity

For a walk whose endpoints are equal propositionally, use `Walk.copy` with those equalities. Prove a length invariant separately with `Walk.length_copy`. Inspect reduction before unfolding the entire recursive constructor.

A local `have hwalk : Walk A B := ...` hides the chosen walk behind an opaque local declaration for later rewriting. If you need to calculate its length, prefer `let`, inline the construction in `dist_le`, or save an explicit equality/length fact when introducing it. Do not repeatedly rewrite inside an opaque hypothesis expecting the defining term to reappear.

After `simp only [programWalk, Walk.length_copy]`, a remaining equality may be definitional and close with `rfl`. Alternatively use `change` to state the definitionally equal arithmetic goal and apply `congrArg`. Check that `change` succeeds; it does not justify replacing an arbitrary unequal expression.

`obtain ⟨g, hg⟩ := h` may consume `h`. Retain it explicitly if needed, or reconstruct the existential `⟨g, hg⟩`. Read the local context instead of using an identifier that is gone.

## Algebra conventions

Before using a generic multiplication theorem, write a two-step example in the project's convention. Chronological left action has `programMatrix (p ++ q) = programMatrix q * programMatrix p`. Reversing this order can produce a compiling proof of the wrong definition. Keep matrix labels and operational costs in the statement.

## Efficient verification loop

Use a probe for uncertain API, then compile the coherent changed module. Once fixed, remove obsolete experiments only after checking the authoritative copy and exact target path. Use one saved full integration build for the milestone and audit the relevant declarations. Never infer mathematical completion from the fact that all loaded dependencies compiled.
