# Highload GPU Codex Lab

Codex plugin collection for high-load GPU development with Docker, Kaggle, Molab, CUDA profiling, and agent-driven diagnostics.

## Plugins

| Plugin | Purpose |
| --- | --- |
| Molab | Operate Molab / marimo notebook sessions from Codex. |
| Kaggle | Prepare, launch, monitor, and inspect Kaggle notebook/kernel runs. |
| HighloadGpu | Design, profile, and debug GPU systems and CUDA workloads. |
| Docker | Work with Docker, Compose, BuildKit, GPU containers, and CUDA environments. |

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/
  docker/
  highload-gpu/
  kaggle/
  molab/
```

## Install From GitHub Clone

1. Clone this repository:

```powershell
git clone https://github.com/TryDotAtwo/highload-gpu-codex-lab.git
cd highload-gpu-codex-lab
```

2. Add this repository as a Codex plugin marketplace:

```powershell
codex plugin marketplace add .
```

3. Install selected plugins:

```powershell
codex plugin add molab@highload-gpu-codex-lab
codex plugin add kaggle@highload-gpu-codex-lab
codex plugin add highload-gpu@highload-gpu-codex-lab
codex plugin add docker@highload-gpu-codex-lab
```

4. Restart Codex or open a new Codex thread so new plugin skills and tools are loaded.

## Install All Plugins

```powershell
codex plugin marketplace add .
codex plugin add molab@highload-gpu-codex-lab
codex plugin add kaggle@highload-gpu-codex-lab
codex plugin add highload-gpu@highload-gpu-codex-lab
codex plugin add docker@highload-gpu-codex-lab
```

## Update Existing Install

```powershell
git pull
codex plugin add molab@highload-gpu-codex-lab
codex plugin add kaggle@highload-gpu-codex-lab
codex plugin add highload-gpu@highload-gpu-codex-lab
codex plugin add docker@highload-gpu-codex-lab
```

Then restart Codex or open a new thread.

## Security Notes

This repository should not contain tokens, `.env` files, service credentials, API keys, browser sessions, caches, or logs.

Plugin workflows can use local tools such as Docker, Kaggle CLI, browsers, or GPU drivers. Configure those tools locally on the receiving machine.

## Requirements By Plugin

| Plugin | External Requirements |
| --- | --- |
| Molab | Codex Browser plugin or in-app browser access. |
| Kaggle | Kaggle CLI configured on the receiver machine. |
| HighloadGpu | NVIDIA GPU stack only when executing GPU-specific workflows. |
| Docker | Docker Desktop or Docker Engine; NVIDIA Container Toolkit for GPU containers. |

## Marketplace

Marketplace file: `.agents/plugins/marketplace.json`

Marketplace name: `highload-gpu-codex-lab`
