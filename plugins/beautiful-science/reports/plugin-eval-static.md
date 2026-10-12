# Plugin Eval Report: beautiful-science

## At a Glance
- Score: 39/100
- Grade: F
- Risk: high
- Checks: 4 fail, 1 warn, 2 info
- Active budget: 1637 tokens (heavy)
- Observed usage: not supplied

## Why It Matters
- 4 failing error checks are driving the highest-confidence problems.
- 1 warning signal still need cleanup before this feels polished.
- manifest is the largest source of score loss at -42 points.
- Active budget pressure is high enough that token cost may dominate the user experience.
- No observed usage is attached yet, so budget conclusions are still based on static estimates.

## Fix First
- [fail/error] plugin.json interface is missing `privacyPolicyURL`. Why: Manifest issues reduce trust because Codex may not discover or represent the plugin correctly. Fix: Add interface.privacyPolicyURL to plugin.json.
- [fail/error] plugin.json interface is missing `termsOfServiceURL`. Why: Manifest issues reduce trust because Codex may not discover or represent the plugin correctly. Fix: Add interface.termsOfServiceURL to plugin.json.
- [fail/error] plugin.json interface is missing `websiteURL`. Why: Manifest issues reduce trust because Codex may not discover or represent the plugin correctly. Fix: Add interface.websiteURL to plugin.json.

## Recommended Next Step
- Fix structural issues first
- Why: Failing manifest or skill structure issues reduce trust and can invalidate later measurements.
- Chat request: "What should I fix first?"
- Local command: `plugin-eval start plugins/beautiful-science --request 'What should I fix first?' --format markdown`

## Details
<details>
<summary>Watch next</summary>

- [fail/error] deferred_cost_tokens is excessive relative to the current Codex baseline. Why: Budget pressure matters because always-loaded or frequently-loaded text can make the workflow feel expensive fast. Fix: Reduce repeated instruction text and move detail into deferred supporting files.
- [warn/warning] invoke_cost_tokens is heavy relative to the current Codex baseline. Why: Budget pressure matters because always-loaded or frequently-loaded text can make the workflow feel expensive fast. Fix: Reduce repeated instruction text and move detail into deferred supporting files.
</details>
<details>
<summary>Improvement brief</summary>

- Raise the evaluation from grade F (39/100) with a focus on the highest-signal structural and budget issues first.
- Goal: Add interface.websiteURL to plugin.json.
- Goal: Add interface.privacyPolicyURL to plugin.json.
- Goal: Add interface.termsOfServiceURL to plugin.json.
- Goal: Reduce repeated instruction text and move detail into deferred supporting files.
- Measure: token-usage-observer
- Measure: task-outcome-scorecard
- Measure: tool-call-audit
- Measure: latency-efficiency
- Suggested prompt: Use the skill-creator guidance to improve beautiful-science. Keep the structure compact and move bulky details into references or scripts. Define success measures with these toolsets: token-usage-observer, task-outcome-scorecard, tool-call-audit, latency-efficiency. Address interface-missing-websiteURL: plugin.json interface is missing `websiteURL`. Address interface-missing-privacyPolicyURL: plugin.json interface is missing `privacyPolicyURL`. Address interface-missing-termsOfServiceURL: plugin.json interface is missing `termsOfServiceURL`. Address deferred_cost_tokens-budget-high: deferred_cost_tokens is excessive relative to the current Codex baseline. Address invoke_cost_tokens-budget-high: invoke_cost_tokens is heavy relative to the current Codex baseline.
</details>
<details>
<summary>Budgets and observed usage</summary>

- trigger_cost_tokens: 142 (moderate)
- invoke_cost_tokens: 1495 (heavy)
- deferred_cost_tokens: 50290 (excessive)
- explicit_only_invoke_cost_tokens: 0 (good, unscored)
- total_tokens: 51927 (excessive)

- No observed usage supplied.
</details>
<details>
<summary>Measurement plan</summary>

Combine cost, outcome, and trust signals so you can tell whether the skill or plugin is genuinely helping instead of only looking well-structured on paper.

- Token Usage Observer [high] Measure how many tokens the skill or plugin actually burns in representative runs. Signals: observed_usage_sample_count, observed_input_tokens_avg, observed_total_tokens_avg, estimate_vs_observed_input_ratio. Evidence: Responses API usage logs, Codex-like session exports, JSONL traces captured from local benchmarking harnesses.
- Task Outcome Scorecard [high] Measure whether the skill helps users finish the intended job with fewer retries and less cleanup. Signals: task_success_rate, first_pass_success_rate, retry_rate, human_override_rate. Evidence: Task run logs, Structured user acceptance checklist, Before/after comparison runs on the same prompts.
- Tool Call Audit [high] Check whether the agent uses the right tools, arguments, and sequencing when the skill is active. Signals: tool_call_success_rate, invalid_tool_argument_rate, recoverable_tool_failure_rate. Evidence: Tool invocation traces, Recorded sessions, Golden-path scenario replays.
- Latency And Efficiency [high] Track whether the skill speeds users up enough to justify its cost. Signals: p50_time_to_first_acceptable_answer_seconds, p95_time_to_task_completion_seconds, tokens_per_successful_run. Evidence: Benchmark harness timings, Manual stopwatch runs on canonical tasks, Responses API timestamps combined with usage logs.
- Human Rubric Review [medium] Capture clarity, trust, and usefulness signals that automated checks will miss. Signals: clarity_score_avg, confidence_score_avg, follow_up_question_rate. Evidence: Reviewer scorecards, Team rubric sheets, Annotated transcripts.
- Regression Suite [medium] Protect the repository behavior that the skill is supposed to improve. Signals: test_pass_rate, lint_pass_rate, regression_escape_count. Evidence: Unit and integration test runs, Coverage deltas, Snapshot or golden-file checks.
</details>
<details>
<summary>Use From Codex Chat</summary>

Start with a natural chat request, then let plugin-eval show the exact local command sequence behind it.

Start with this chat request: "Evaluate this plugin."
Why this path: Plugin Eval recommended Evaluate Plugin from the current local state for this plugin.
Quick local entrypoint: plugin-eval start plugins/beautiful-science --request 'Evaluate this plugin.' --format markdown
Plugin Eval will run first: plugin-eval analyze plugins/beautiful-science --format markdown

Other chat requests you can use:
- Full Plugin Analysis: say "Give me a full analysis of this plugin, including benchmark setup." -> plugin-eval analyze plugins/beautiful-science --format markdown
- Evaluate Plugin: say "Evaluate this plugin." -> plugin-eval analyze plugins/beautiful-science --format markdown
- Explain Token Budget: say "Explain the token budget for this plugin." -> plugin-eval explain-budget plugins/beautiful-science --format markdown
- Measure Real Token Usage: say "Measure the real token usage of this plugin." -> plugin-eval init-benchmark plugins/beautiful-science
- Benchmark With Starter Scenarios: say "Help me benchmark this plugin." -> plugin-eval init-benchmark plugins/beautiful-science
- Start Here: say "What should I run next?" -> plugin-eval analyze plugins/beautiful-science --format markdown
</details>
<details>
<summary>Checks</summary>

- [FAIL] interface-missing-websiteURL: plugin.json interface is missing `websiteURL`. Evidence: <plugin-root>/.codex-plugin/plugin.json Remediation: Add interface.websiteURL to plugin.json.
- [FAIL] interface-missing-privacyPolicyURL: plugin.json interface is missing `privacyPolicyURL`. Evidence: <plugin-root>/.codex-plugin/plugin.json Remediation: Add interface.privacyPolicyURL to plugin.json.
- [FAIL] interface-missing-termsOfServiceURL: plugin.json interface is missing `termsOfServiceURL`. Evidence: <plugin-root>/.codex-plugin/plugin.json Remediation: Add interface.termsOfServiceURL to plugin.json.
- [WARN] invoke_cost_tokens-budget-high: invoke_cost_tokens is heavy relative to the current Codex baseline. Evidence: Value: 1495 tokens Baseline samples: skills=0, plugins=0 Remediation: Reduce repeated instruction text and move detail into deferred supporting files.
- [FAIL] deferred_cost_tokens-budget-high: deferred_cost_tokens is excessive relative to the current Codex baseline. Evidence: Value: 50290 tokens Baseline samples: skills=0, plugins=0 Remediation: Reduce repeated instruction text and move detail into deferred supporting files.
- [INFO] coverage-artifacts-unavailable: No coverage artifacts were found for this target. Evidence: plugins/beautiful-science Remediation: Generate `lcov.info`, `coverage.xml`, or an Istanbul coverage JSON file if you want coverage scoring.
</details>
<details>
<summary>Metrics</summary>

- skill:choose-research-path:skill_line_count: 56 lines (good)
- skill:choose-research-path:description_length_chars: 283 chars (good)
- skill:choose-research-path:relative_link_count: 7 links (good)
- skill:choose-research-path:code_fence_count: 0 blocks (good)
- skill:choose-research-path:support_file_count: 8 files (good)
- plugin_skill_count: 1 skills (good)
- plugin_keyword_count: 6 keywords (good)
- plugin_default_prompt_count: 3 prompts (good)
- trigger_cost_tokens: 142 tokens (moderate)
- invoke_cost_tokens: 1495 tokens (heavy)
- deferred_cost_tokens: 50290 tokens (excessive)
- explicit_only_invoke_cost_tokens: 0 tokens (good)
- py_file_count: 1 files (good)
- py_function_count: 12 functions (good)
- py_max_cyclomatic_complexity: 13 score (moderate)
- py_average_function_length: 5.42 lines (good)
- py_max_nesting_depth: 4 levels (moderate)
- py_comment_ratio: 0.09 ratio (good)
- py_test_file_count: 1 files (good)
- coverage_artifact_count: 0 files (info)
</details>
<details>
<summary>Score details</summary>

- Starting score: 100
- Total deductions: -60.75
- Final score: 39
- Risk: Contains 4 failing error checks (deferred_cost_tokens-budget-high, interface-missing-privacyPolicyURL, interface-missing-termsOfServiceURL).
- Risk: Overall score is below 70, which the evaluator treats as high risk.

- -14 points: deferred_cost_tokens-budget-high [fail/error] deferred_cost_tokens is excessive relative to the current Codex baseline.
- -14 points: interface-missing-privacyPolicyURL [fail/error] plugin.json interface is missing `privacyPolicyURL`.
- -14 points: interface-missing-termsOfServiceURL [fail/error] plugin.json interface is missing `termsOfServiceURL`.
- -14 points: interface-missing-websiteURL [fail/error] plugin.json interface is missing `websiteURL`.
- -4.5 points: invoke_cost_tokens-budget-high [warn/warning] invoke_cost_tokens is heavy relative to the current Codex baseline.
- -0.25 points: coverage-artifacts-unavailable [info/info] No coverage artifacts were found for this target.

- manifest: -42 points across 3 checks
- budget: -18.5 points across 2 checks
- coverage: -0.25 points across 1 check
</details>
