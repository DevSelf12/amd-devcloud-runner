# amd-devcloud-runner

A small benchmark runner prepared for the **AMD Developer Cloud** application.

## Purpose

This repository shows a simple, repeatable harness for benchmarking compute workloads that are intended to run on AMD GPUs through ROCm/HIP.

The goal is to demonstrate:
- a clean benchmark structure
- reproducible local runs
- readiness for ROCm / HIP / PyTorch ROCm evaluation
- why access to AMD Developer Cloud would be useful

## Why AMD Developer Cloud?

I want to move beyond local assumptions and validate workloads against a proper AMD environment.

Specifically, I want to:
- verify ROCm compatibility
- measure CPU vs GPU-bound differences
- prepare workloads for HIP execution
- create a benchmark baseline that can be repeated later

## Repository layout

```
amd-devcloud-runner/
├── README.md
├── LICENSE
├── .gitignore
├── benchmarks/
│   └── README.md
├── docs/
│   └── workloads.md
├── examples/
│   └── hip_hello.cpp
├── scripts/
│   ├── run_all.sh
│   └── bench.py
```

## Quick start

### 1. Run the local CPU benchmark

```bash
python scripts/bench.py --mode matrix --n 512 --steps 3
```

### 2. Run the simple HIP example (requires ROCm/HIP toolchain)

```bash
hipcc examples/hip_hello.cpp -o hip_hello
./hip_hello
```

## Expected outputs

- benchmark summary printed to stdout
- optional placeholder notes under `benchmarks/`

## Notes

This repo is intentionally kept minimal so a reviewer can quickly see the:
- workload intent
- benchmark approach
- readiness for AMD Developer Cloud experimentation
