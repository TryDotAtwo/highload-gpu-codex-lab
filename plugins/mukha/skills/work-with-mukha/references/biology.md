# Biological inference and model transfer

## Preserve the chain of evidence

For an enabled boundary retain: source/specimen/version and identity -> measured
quantity and units -> model equation/observation operator -> fitted versus fixed
parameters -> calibration split -> held-out condition and interventions. If a link
is missing, call the mapping a candidate and test the uncertainty. Do not silently
drop its cells or invent a parameter from a similarly named type.

Source contact count is not conductance. Neurotransmitter consensus is not a
postsynaptic receptor/reversal map. A zero electrical weight for a modulatory
cell does not implement dopamine. Prediction, curated group, biological assay,
and soma/effector side are different fields. For MaleCNS motor mapping inspect
`mancGroup` separately from predicted `mancBodyid`; preserve competing matches.

The accepted population is `Traced OR nonempty superclass`. Verify graph hashes,
original IDs, weak/parallel source rows and boundary accounting when changing
execution layouts. Never equate source table segments with known whole neurons.
Extracting a view for analysis is fine; a view must not replace the full runtime.

## Plasticity: choose a falsifiable local mechanism

Huang/Luo reference reproduces an aggregate recurrent MB equation model. Saved
figure agreement does not make its effective weights a per-spike rule on
MaleCNS. Reuse it for its documented memory protocol, not as a direct controller.

Before implementing a local candidate, name the original synapses affected,
local state variables, teaching signal, allowed update times, time constants,
bounds and decay. Explain which source identifies each quantity and which is a
hypothesis. No global task gradient or rocket telemetry may silently become a
local biological signal in the accepted main path.

A useful discriminating protocol includes paired and unpaired stimuli, timing
reversal, stimulus specificity, persistence/decay and learning-disabled controls.
Freeze calibration/assessment separation before fitting. A previously inspected
test set is exploratory thereafter; obtain a new independent condition for a
confirmation claim. Post-learning sensory/motor biology must be rechecked.

The audit located Handler et al., Cell 2019, DOI 10.1016/j.cell.2019.05.040:
https://pubmed.ncbi.nlm.nih.gov/31230716/ . Its abstract/figure descriptions
support timing-dependent opposing KC–MBON plasticity. They are a lead for a
protocol, not enough to implement quantitative kinetics. Retrieve full methods
and suitable data before fitting. Huang 2024 DOI 10.1038/s41586-024-07819-w is
the source associated with the existing pinned author code.

Coordinates can establish anatomical localization. `primary_post` neuropil labels
may be coarser than the required MB compartment. KC→MBON coordinates alone do not
locate all relevant DAN release sites. Decide the necessary anatomical query
before rescanning a multi-GB source; receptor availability and a learning rule
still require physiological evidence. Avoid automatic spatial-nearest teaching
signals without a supported localization/range model.

## Match the observation, not a convenient array

- Calcium/GCaMP != raw voltage or spike count. Include the observation dynamics,
  exposure integration, sampling, baseline and normalization used by the source.
- Frame-averaged joint angles do not recover instantaneous high-rate velocities.
  The rejected linear FeCO velocity pilot is not a native sensory encoder.
- RGB coefficients, absorbed photons, irradiance and calibrated in-vivo dose are
  different quantities. Preserve units and specimen/temperature assumptions.
- Preserve graded signaling and recurrent receptor input where represented by
  the source. Uniform spiking LIF is a tested numerical hypothesis, not universal
  biological coverage of every class.

For stochastic models distinguish same-stream reproducibility from equality in
distribution. Test means, variability, temporal correlation, tails and downstream
response on declared independent seeds. A finite sample cannot prove all-input
biological identity; report its scope and planned falsification.
