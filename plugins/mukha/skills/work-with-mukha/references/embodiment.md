# Embodiment, learning and final evaluation

## Causal loop

The intended chain is cabin/world light + body senses -> full CNS -> identified
motor units -> bounded muscle/body mechanics -> actual foot/control contact ->
passive cockpit position -> applied rocket control -> sensed consequences.
Each bypass must be explicit diagnostic input and excluded from final trials.
Privileged state is allowed for assessment/reset/physics calibration, not hidden
policy features or reward-to-DAN injection without a declared embodied mechanism.

Check disconnected motor output, disabled specific foot/control contact, and
sensory intervention while keeping comparable initial state and stimuli. Count
the exact geometry pair: all contacts involving a pad can include other body
parts. Preserve unperturbed controls and pre-intervention equality. A contact
chosen after viewing motion is exploratory until independently confirmed.

Muscle XML is evidence of a mechanical reference, not cell-to-muscle identity or
spike gain. `mancBodyid` prediction, curated group, nerve/target side, motor-unit
type and action about MuJoCo axes need distinct checks. Keep units (body may
use mm, rocket SI), passivity, limits and source uncertainty explicit. Sensitivity
of contact to arbitrary gain is a reason to calibrate, not to choose the winning
gain and call it physiology.

One passive slider is not a three-axis stick plus throttle, and a restrained
diagnostic body is not a validated seated cabin. Radial physics is not full 6-DOF
flight or ten seconds of supported ground stability. Enable and verify the
missing degrees of freedom/contact physics for the accepted mission.

## Curriculum and biological regression

Only after a local mechanism has a declared validation basis, develop body-sense,
visual-cue and physical-control curriculum. Preserve full CNS and report which
weights/state actually changed, their local inputs, training seed and checkpoint.
Motor competence, learning on training cases, generalization, and biological
retention after learning need separate tests. Do not replace difficult CNS learning
with an external controller to produce the requested success number.

## Three training runs and KSP

Lock the mission, craft, target, start states, success criteria and stability
thresholds before assessment. Three distinct labels are not proof of independent
training; link each to its training run, seed, source, protocol and checkpoint.
Evaluate 100 withheld starts for EACH run; require >=90 in each, not pooled.
Document whether shared starts are used across seeds and keep calibration data
outside this set. Repeated trials or selection of the best attempt must be visible.

Bind episode identity to plan/start/checkpoint before launch, then to complete
physics/control records and terminal outcome. Reject missing/unfinished pairs,
mixed environments and contradictory identity. Repeated file paths are errors;
identical trace hashes trigger provenance inspection, not a claim that every
identical deterministic trace is fraudulent. Per-trace configurable thresholds
must not silently weaken the locked series definition.

For KSP collect actual applied controls and SAS/trim/autopilot/action-group
state, clocks, impacts before contact-solver velocity clamping, breakage and
continuous stable contact. Prove the bridge's control origin and scale. Synthetic
trace labels cannot authenticate KSP, a neural controller or independent training.

Record measured neural activity, physical poses, cockpit and KSP views with common
episode/tick/time identities, explicit frame-to-tick mapping and dropped-frame
accounting. Preserve complete events under backpressure plus the reproduction
manifest. Video is evidence only when tied to the actual run; animation or selected
successful clips do not prove 3x100 evaluation.
