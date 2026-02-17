#!/bin/bash
# Check GPU is detected:
nvidia-smi

# Restart Ollama:
systemctl restart ollama
