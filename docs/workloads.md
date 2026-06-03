# Workloads

This document explains the workload direction for the repository.

## 1. CPU baseline workload

A simple CPU matrix benchmark is included so the repo already has a reproducible baseline.

## 2. HIP hello workload

A minimal HIP example is included to show the intention of moving toward AMD GPU execution.

## 3. Planned ROCm workloads

If access to AMD Developer Cloud is granted, the next targets are:
- HIP matrix multiply
- memory bandwidth check
- simple compute-bound kernel
- PyTorch ROCm smoke test

## 4. Why this matters

These workloads are intentionally simple, but they are enough to show:
- setup readiness
- benchmark intent
- environment validation needs
