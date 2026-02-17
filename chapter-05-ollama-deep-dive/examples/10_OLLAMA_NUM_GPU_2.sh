#!/bin/bash
# Use all GPUs
OLLAMA_NUM_GPU=2 ollama serve

# Specific GPU
CUDA_VISIBLE_DEVICES=0 ollama serve
