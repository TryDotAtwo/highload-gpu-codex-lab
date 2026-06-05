---
name: use-docker-gpu
description: Use when enabling Docker GPU access.
---

# Use Docker GPU

Use official docs:

- Docker GPU access: https://docs.docker.com/engine/containers/gpu/
- Compose GPU support: https://docs.docker.com/compose/how-tos/gpu-support/
- NVIDIA Container Toolkit install: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
- NVIDIA Container Toolkit docs: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/

## Checks

- Host driver works: `nvidia-smi` on host.
- Docker sees GPU: `docker run --rm --gpus all nvidia/cuda:12.8.0-base-ubuntu22.04 nvidia-smi` or project-approved CUDA tag.
- Container CUDA toolkit can be older/newer than host driver only within NVIDIA compatibility rules.
- Choose `--gpus all`, `--gpus device=...`, or Compose `device_ids` deliberately.
- In containers, compile for the target arch (`sm_75`, `sm_90`, `sm_120`, etc.) based on actual GPU and CUDA toolkit support.

## Failure Smells

- `could not select device driver` or missing `libnvidia-ml.so`: toolkit/runtime/driver wiring issue.
- `nvidia-smi` works on host but not container: Docker daemon runtime config or toolkit install issue.
- Build works but runtime is slow: wrong arch flags, PTX JIT fallback, missing native cubin, or volume/cache bottleneck.
