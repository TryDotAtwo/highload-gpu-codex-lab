# Research-to-paper workflow

## 1. Establish the evidence base

Inspect the current manuscript and the actual artifacts it references. Record exact input filenames/versions, hashes when available, source dates, and which results were rerun versus merely inspected. Resolve conflicts before changing claims. Read approved examples for structure, visual density, and level of explanation; do not copy confidential paper content into reusable templates.

Extract:
- Object and question: the full labelled target, optimization objective, or hypothesis
- Model: domains, quantifiers, input conditions, legal operations, costs, resources, symmetries, equivalences
- Result: construction, bound, equality, counterexample, measurement, or conditional claim
- Assumptions and evidence needed for every implication
- Known gaps, competing interpretations, and reproducibility limits
- Verified author names, affiliations, contributions, and venue constraints

Use the user's current sources for article metadata. Do not infer an institutional affiliation from hardware access, a collaborator, prior employment, or the venue. Do not invent a title from an unavailable publication; a new draft title may be clearly proposed.

## 2. Build the argument before polishing prose

Create a statement graph: definitions feed lemmas, lemmas feed reductions, reductions and evidence feed the final claim. Label each edge with its implication and assumptions. Check for circularity, absent coverage, and reductions that change the target. Define symbols where first used and add a notation table only when useful.

For a minimum/optimality result, keep two independent tracks:
- Feasibility: a witness realizes the FULL target under all legal-model constraints
- Exclusion: every cheaper legal candidate is covered and rejected by justified reductions or authenticated exhaustive evidence

For transformations, explicitly distinguish physical state from projection, abstract state from stored key, distinct keys from hash values, and search layer counts from distinct objects. Prove information discarded from the representation cannot alter relevant continuations. List operations that remain paid after normalization, including copies, restores, communication, permutations, initialization, and ancillas when applicable.

## 3. Write in local explanatory units

Each unit contains: a question/claim, essential definitions, the equation or figure that makes the step inspectable, and the justification. Captions explain encodings and the exact scope of the picture. Figures supplement the argument; they do not replace an absent proof.

Aim for high information density with generous visual spacing. Use substantive visual explanations rather than decorative images or a quota of figures. Preserve the user's technical level. Remove repeated motivation, sweeping rhetoric, generic surveys, and redundant restatements. Do not move all diagrams to an appendix while leaving the main argument opaque.

Useful figure roles include operation semantics, target/block structure, representation changes, case partitions, conserved quantities, resource budgets, a proof dependency map, state layout, search coverage, and evidence boundaries. Include only roles that the actual paper needs.

## 4. Validate in separate passes

- Scientific: check model equivalence, quantifiers, dependencies, arithmetic, units, counts, scope of claims, evidence, and citations against primary sources
- Formal/computational: inspect theorem signatures, assumptions, audit/build evidence, algorithms, certificates, and run provenance
- Editorial: remove duplication; keep terminology and notation consistent
- Visual: per-figure inspection and whole-document pagination at final size
- Delivery: confirm the exact reviewed PDF came from the delivered source and build

Mark unresolved checks explicitly. Do not say `verified`, `optimal`, `exhaustive`, `independent`, or `publication-ready` when the corresponding check remains open.
