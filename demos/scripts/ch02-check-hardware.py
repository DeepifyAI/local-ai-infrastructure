#!/usr/bin/env python3
"""Chapter 2: Check what hardware you're working with."""
import subprocess
import os

print("=== Your AI Hardware ===")
print()

# CPU
cpu_count = os.cpu_count()
print(f"CPUs: {cpu_count} cores")

# Memory
with open("/proc/meminfo") as f:
    for line in f:
        if "MemTotal" in line:
            mem_gb = int(line.split()[1]) / 1024 / 1024
            print(f"RAM:  {mem_gb:.1f} GB")
            break

# GPU
try:
    result = subprocess.run(
        ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
        capture_output=True, text=True, timeout=5
    )
    if result.returncode == 0:
        print(f"GPU:  {result.stdout.strip()}")
    else:
        print("GPU:  No NVIDIA GPU detected (CPU inference still works!)")
except FileNotFoundError:
    print("GPU:  nvidia-smi not found (CPU inference still works!)")

# Disk
result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
for line in result.stdout.strip().split("\n")[1:]:
    parts = line.split()
    print(f"Disk: {parts[3]} available of {parts[1]}")

print()

# Can you run local AI?
if mem_gb >= 8:
    print("✅ You have enough RAM for 7B parameter models")
if mem_gb >= 16:
    print("✅ You can run 13B+ parameter models")
if mem_gb >= 32:
    print("✅ You can run 70B parameter models")
if mem_gb < 8:
    print("⚠️  Less than 8GB RAM - you'll need a smaller model (3B)")
