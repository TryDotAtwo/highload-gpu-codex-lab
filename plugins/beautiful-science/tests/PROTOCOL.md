# Behavioral test protocol (frozen before authoring)

The prompts are synthetic, anonymized research decisions, not records of anyone's project. They were written before the plugin instructions. The rubric is not supplied to the tested agents.

## Conditions

- Five fresh-context baseline agents receive only `scenarios.json` and the instruction to answer each scenario in 100–160 words.
- Five fresh-context guided agents receive the same prompts plus the finished skill and its linked references, with the same response-length request.
- Each agent answers eight independent scenarios in a single response file. Scenario order is fixed in this small development test; order effects are a limitation.
- The same inherited model configuration and xhigh reasoning effort are used. The exact deployment model identifier and random seed are not exposed to this test harness; no claim of seed-level reproducibility is made.
- Raw artifacts retain the complete decision text. A human-readable manual assessment records any concrete failure and exact supporting excerpt.
- No external state is changed by test decisions. Agents read specified local files and write a JSON response artifact only.

## Judging

Read every response, not just regex matches. Assess each case's substantive criteria and the global criteria in `rubric.json`. Assign pass, fail, or not assessable with a concrete reason. Preserve mixed outcomes and ambiguity. Do not average the criteria into a scientific-quality or beauty score.

A baseline that already passes is a genuine result, not a reason to invent a deficiency. In that event this package can still standardize an explicitly requested decision protocol, but the test does not demonstrate that the skill improved correctness. Report ceiling effects and limited sample size.

## Reproduction

Run the two conditions in fresh agents without history from the other condition. Never show the expected rubric to the tested agent, earlier responses, the intended answer, or the final test report. The canonical runner prompt is in `runner_prompt.txt`; replace CONDITION and OUTPUT exactly as described there.

Structural and exact-witness tests are separately reproducible with Python. They do not replace behavioral tests and do not measure scientific judgment. First-run missing files are ordinary pre-scaffold setup status, not a demonstrated behavioral failure.

Stop this evaluation after the five matched repetitions and inspection of every response, unless a concrete observed defect requires a targeted revision and regression check. This sample size follows the instruction-authoring micro-test protocol; it is not a research budget rule for plugin users, nor a statistical validation sample.
