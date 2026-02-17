#!/usr/bin/env python3
"""
How much VRAM does a model need?
Pick your GPU — see what you can run.
"""

MODELS = [
    # (name,          params_B,  note)
    ("Gemma 2B",          2,    "fast, lightweight"),
    ("Phi-3 Mini 3.8B",   3.8,  "Microsoft, very efficient"),
    ("Llama 3 8B",        8,    "Meta's workhorse"),
    ("Gemma 2 9B",        9,    "great instruction following"),
    ("Mistral 7B",        7,    "fast, excellent reasoning"),
    ("Qwen 2.5 14B",     14,    "multilingual"),
    ("Llama 3.1 70B",    70,    "near frontier quality"),
]

def vram_needed(params, bits=4):
    bytes_per = {4: 0.5, 8: 1.0, 16: 2.0}[bits]
    return params * bytes_per * 1.2   # +20% overhead

GPUS = [
    ("Laptop GPU (8 GB)",     8),
    ("RTX 4070 (12 GB)",     12),
    ("RTX 4090 (24 GB)",     24),
    ("DGX Spark (128 GB)",  128),
]

print("=== What models fit your GPU? (4-bit quantised) ===\n")

for gpu_name, vram in GPUS:
    fits = [name for name, params, _ in MODELS if vram_needed(params) <= vram]
    print(f"  {gpu_name:<25} → {', '.join(fits)}")

print()
print("Rule of thumb: params × 0.6 GB ≈ VRAM needed (4-bit).")
