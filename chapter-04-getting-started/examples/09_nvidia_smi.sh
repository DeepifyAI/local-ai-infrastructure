#!/bin/bash
# Check CUDA
nvidia-smi

# Check architecture
uname -m
# Should show: aarch64

# Use NVIDIA's ARM64 wheels:
pip3 install --index-url https://pypi.nvidia.com nvidia-pyindex
