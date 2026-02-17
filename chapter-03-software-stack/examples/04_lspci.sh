#!/bin/bash
# Check if GPU is visible
lspci | grep -i nvidia

# You should see something like:
# 01:00.0 VGA compatible controller: NVIDIA Corporation AD102 [GeForce RTX 4090]
