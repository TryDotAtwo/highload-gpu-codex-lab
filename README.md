# Highload GPU Codex Lab

Personal Codex plugin collection by Ivan Litvak: GPU engineering, beam search, BFS, compute platforms, Docker, formal proofs, scientific writing, and research workflows.

This repository publishes the local plugin collection as of 2026-10-12: **22 plugins**. The original Molab, Kaggle, Highload GPU and Docker names remain available. Newer grouped plugins coexist with the older focused plugins; install the ones you need to avoid loading overlapping instructions.

## Plugins

| Plugin | Skills | Purpose |
| --- | ---: | --- |
| `beam-search` | 5 | GPU beam-search pipelines, frontier memory planning, tuning, and correctness validation skills. |
| `beautiful-science` | 1 | Evidence-based choices for scientific research paths: continue, test, redirect, or park with scope and costs explicit. |
| `bfs` | 1 | Mathematics of breadth-first search: distance layers, shortest paths, reverse balls, graph quotients and group actions. |
| `cnot-research` | 1 | Project knowledge and evidence for paid shared-basis CNOT synthesis, full-matrix transformers, verified search and diffusion experiments. |
| `compute-platforms` | 3 | Workflows for Molab, Kaggle, and TPU compute platforms. |
| `docker` | 7 | Docker, Compose, BuildKit, and GPU container guidance. |
| `docker-workflows` | 7 | Docker images, Compose workflows, GPU containers, and debugging skills. |
| `gpu-architecture` | 1 | Design and audit complete GPU execution architectures from algorithm semantics through memory, concurrency, communication, and staged validation. |
| `gpu-beam-search` | 5 | Design, tune, and validate fixed-capacity GPU beam-search pipelines. |
| `gpu-engineering` | 18 | GPU architecture, CUDA implementation, inference quality, profiling, and performance measurement skills. |
| `gpu-neural-inference` | 5 | Optimize and validate MLP and Transformer inference on NVIDIA GPUs. |
| `highload-gpu` | 12 | General CUDA and high-performance GPU engineering guidance, including Blackwell SM120. |
| `kaggle` | 1 | Codex workflows for working with Kaggle notebooks, kernels, datasets, logs, and GPU validation runs. |
| `lean` | 1 | Lean 4 and Mathlib formalization, proof debugging, exact certificates, and source-bound verification evidence. |
| `molab` | 1 | Operate Molab notebooks through native marimo pairing with safe foreground jobs and artifact persistence. |
| `mukha` | 1 | Develop and validate the full MaleCNS embodied fly: biological hypotheses, native execution, reproducible experiments, physical cockpit control and KSP evaluation. |
| `research-methods` | 5 | Научное мышление: выбор исследовательского пути, логика, ТРИЗ, Lean и рекурсивное планирование решений. |
| `scientific-writing` | 4 | Clear explanations across languages and source-bound scientific writing with Prism. |
| `tpu-builder` | 1 | Prepare evidence-backed TPU Builders activity reports and Google Cloud credit requests. |
| `tpu-coding` | 1 | Evidence-backed TPU coding with JAX and Pallas: layout, pipelines, numerical validation and benchmarking. |
| `triz` | 1 | Resolve software engineering contradictions with a testable, evidence-first TRIZ workflow. |
| `write-visual-research-papers` | 1 | Rigorous visual-first scientific manuscripts with explicit proof boundaries, HPC scaling, and rendered figure QA. |

## Installation

Clone this repository and register its marketplace using the plugin commands supported by your Codex version:

```powershell
git clone https://github.com/TryDotAtwo/highload-gpu-codex-lab.git
cd highload-gpu-codex-lab
codex plugin marketplace add .
codex plugin add gpu-engineering@highload-gpu-codex-lab
codex plugin add beam-search@highload-gpu-codex-lab
codex plugin add research-methods@highload-gpu-codex-lab
codex plugin add scientific-writing@highload-gpu-codex-lab
```

Use any plugin name from the table instead of these examples. If your Codex version manages plugins through the desktop interface, add this repository as a marketplace there. Reopen the chat after installation so its skills can be loaded. Run `git pull` to update the clone.

## Layout

- `.agents/plugins/marketplace.json`: installable marketplace, preserving the `highload-gpu-codex-lab` name.
- `plugins/<name>/.codex-plugin/plugin.json`: plugin metadata.
- `plugins/<name>/skills/`: instructions, references and supporting files.
- `PLUGIN_FILES_SHA256.json`: hashes of published plugin files.

## Local configuration

Credentials, API keys, browser sessions, SSH keys, datasets and model weights are not bundled. Configure external services and hardware on your own machine. Instructions about project-specific evidence are historical records, not a claim that another machine has those projects or artifacts. Some plugins include packaged research snapshots and constructed test examples.

Structural checks and the included helper tests do not validate GPU performance, remote service availability, scientific conclusions or full Codex installation.

## Related working conversations

The owner-approved sanitized conversation dataset is available at [Hugging Face](https://huggingface.co/datasets/TryDotAtwo/codex-working-chats-2026-10-12).
