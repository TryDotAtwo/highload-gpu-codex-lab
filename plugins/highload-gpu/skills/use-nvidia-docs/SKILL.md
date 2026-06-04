---
name: use-nvidia-docs
description: Use when the task needs current NVIDIA GPU, CUDA, CUTLASS, CUB, NCCL, Nsight, Compute Sanitizer, CUDA architecture, compute capability, driver/toolkit, or GPU-library documentation.
---

# Use NVIDIA Docs

Use official, current documentation before giving hardware-specific CUDA or NVIDIA-library advice. GPU capabilities, architecture targets, profiler behavior, and library APIs change over time.

## Lookup Workflow

1. Identify the GPU model, driver, CUDA Toolkit, and target platform from `nvidia-smi`, build logs, container image, or user-provided environment.
2. Map GPU model to compute capability with the official compute capability table.
3. Choose arch flags from evidence: for example `sm_75` for Turing T4, `sm_90` for H100, and `sm_120` for RTX PRO 6000 Blackwell Server Edition.
4. Check the CUDA guide for programming-model behavior, the tuning guide for architecture-specific risks, and the library guide for API details.
5. Cite exact docs used when the answer relies on current hardware/library facts.

## Source Map

NVIDIA core docs:

- CUDA Programming Guide: https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- CUDA Programming Guide PDF: https://docs.nvidia.com/cuda/pdf/CUDA_C_Programming_Guide.pdf
- CUDA Best Practices Guide: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html
- CUDA Best Practices Guide PDF: https://docs.nvidia.com/cuda/pdf/CUDA_C_Best_Practices_Guide.pdf
- CUDA Runtime API: https://docs.nvidia.com/cuda/cuda-runtime-api/
- CUDA Driver API: https://docs.nvidia.com/cuda/cuda-driver-api/
- NVCC Compiler Guide: https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/
- CUDA Binary Utilities: https://docs.nvidia.com/cuda/cuda-binary-utilities/
- CUDA GPU compute capability table: https://developer.nvidia.com/cuda-gpus
- CUDA Toolkit docs index: https://docs.nvidia.com/cuda/

NVIDIA architecture and tuning:

- Turing Tuning Guide: https://docs.nvidia.com/cuda/turing-tuning-guide/
- Ampere Tuning Guide: https://docs.nvidia.com/cuda/ampere-tuning-guide/
- Hopper Tuning Guide: https://docs.nvidia.com/cuda/hopper-tuning-guide/
- Blackwell architecture overview: https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
- Blackwell CUDA architecture features blog: https://developer.nvidia.com/blog/nvidia-blackwell-and-nvidia-cuda-12-9-introduce-family-specific-architecture-features/

NVIDIA libraries:

- CUTLASS docs: https://docs.nvidia.com/cutlass/
- CUTLASS GitHub: https://github.com/NVIDIA/cutlass
- CUB / CCCL docs: https://nvidia.github.io/cccl/
- CUB API docs: https://nvidia.github.io/cccl/cub/api.html
- Thrust / CCCL docs: https://nvidia.github.io/cccl/thrust/
- NCCL User Guide: https://docs.nvidia.com/deeplearning/nccl/user-guide/index.html
- NCCL API docs: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api.html
- cuBLAS docs: https://docs.nvidia.com/cuda/cublas/
- cuBLASLt docs: https://docs.nvidia.com/cuda/cublas/#using-the-cublaslt-api
- cuDNN docs: https://docs.nvidia.com/deeplearning/cudnn/
- TensorRT docs: https://docs.nvidia.com/deeplearning/tensorrt/
- Transformer Engine docs: https://docs.nvidia.com/deeplearning/transformer-engine/

NVIDIA profiling and debugging:

- Nsight Systems User Guide: https://docs.nvidia.com/nsight-systems/UserGuide/index.html
- Nsight Systems CLI: https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cli
- Nsight Compute User Guide: https://docs.nvidia.com/nsight-compute/NsightCompute/index.html
- Nsight Compute Profiling Guide: https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html
- Compute Sanitizer: https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html
- NVTX docs: https://nvidia.github.io/NVTX/
- CUPTI docs: https://docs.nvidia.com/cupti/

NVIDIA deployment and runtime:

- NVIDIA Container Toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/
- NVIDIA GPU Operator: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/
- DCGM docs: https://docs.nvidia.com/datacenter/dcgm/
- MIG User Guide: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/
- CUDA Compatibility: https://docs.nvidia.com/deploy/cuda-compatibility/
- Fabric Manager User Guide: https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/

Rust/Python/C++ boundary docs:

- Rust book: https://doc.rust-lang.org/book/
- Rustonomicon FFI: https://doc.rust-lang.org/nomicon/ffi.html
- cxx.rs: https://cxx.rs/
- cxx docs.rs: https://docs.rs/cxx/latest/cxx/
- bindgen guide: https://rust-lang.github.io/rust-bindgen/
- PyO3 guide: https://pyo3.rs/
- maturin guide: https://www.maturin.rs/
- Cargo build scripts: https://doc.rust-lang.org/cargo/reference/build-scripts.html
- CMake CUDA language docs: https://cmake.org/cmake/help/latest/manual/cmake-cuda.7.html
- pybind11 docs: https://pybind11.readthedocs.io/

Remote/runtime platforms:

- PyTorch distributed / torchrun: https://docs.pytorch.org/docs/stable/elastic/run.html
- PyTorch CUDA semantics: https://docs.pytorch.org/docs/stable/notes/cuda.html
- Kaggle API docs: https://github.com/Kaggle/kaggle-api
- marimo docs: https://docs.marimo.io/

## Common Mistakes

- Guessing compute capability from architecture name without checking the table.
- Using old CUDA docs when the installed CUDA Toolkit is newer.
- Treating blog posts, forum answers, or model cards as stronger than official API docs.
- Recommending CUTLASS, CUB, or NCCL API shapes from memory when current signatures may differ.
- Assuming PyTorch CUDA behavior proves native C++/CUDA behavior.