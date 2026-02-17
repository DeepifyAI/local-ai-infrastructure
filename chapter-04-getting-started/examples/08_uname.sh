#!/bin/bash
# Check architecture
uname -m
# Should show: arm64

# Ollama uses Metal (Apple's GPU framework) automatically
# Models run fast even without NVIDIA GPU
