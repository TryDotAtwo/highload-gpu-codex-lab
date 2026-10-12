# Plugin Eval Start Here: beautiful-science

## At a Glance
- Recommended path: Evaluate Plugin
- Benchmark config present: no
- Usage log present: no
- Quick local entrypoint: `plugin-eval start plugins/beautiful-science --request 'Evaluate this plugin.' --format markdown`
- First local command: `plugin-eval analyze plugins/beautiful-science --format markdown`

## Why It Matters
- Start with a natural chat request, then let plugin-eval show the exact local command sequence behind it.
- Plugin Eval routed "Evaluate this plugin." to Evaluate Plugin because it asks for the overall evaluation report or prioritized findings from it.

## Fix First
- Start with the recommended path before branching into secondary workflows.

## Recommended Next Step
- Evaluate Plugin
- Why: Plugin Eval routed "Evaluate this plugin." to Evaluate Plugin because it asks for the overall evaluation report or prioritized findings from it.
- Chat request: "Evaluate this plugin."
- Local command: `plugin-eval analyze plugins/beautiful-science --format markdown`

## Details
<details>
<summary>Full local sequence</summary>

- plugin-eval analyze plugins/beautiful-science --format markdown
</details>
<details>
<summary>Other chat requests</summary>

- Full Plugin Analysis: "Give me a full analysis of this plugin, including benchmark setup." -> plugin-eval analyze plugins/beautiful-science --format markdown
- Evaluate Plugin: "Evaluate this plugin." -> plugin-eval analyze plugins/beautiful-science --format markdown
- Explain Token Budget: "Explain the token budget for this plugin." -> plugin-eval explain-budget plugins/beautiful-science --format markdown
- Measure Real Token Usage: "Measure the real token usage of this plugin." -> plugin-eval init-benchmark plugins/beautiful-science
- Benchmark With Starter Scenarios: "Help me benchmark this plugin." -> plugin-eval init-benchmark plugins/beautiful-science
- Start Here: "What should I run next?" -> plugin-eval analyze plugins/beautiful-science --format markdown
</details>
