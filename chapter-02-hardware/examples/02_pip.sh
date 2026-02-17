#!/bin/bash
# This FAILS on ARM64:
pip install torch

# This WORKS:
pip install torch --index-url https://download.pytorch.org/whl/cpu
# OR use NVIDIA's containers:
docker pull nvcr.io/nvidia/pytorch:24.01-py3
