#!/bin/bash
# CPU usage
top

# GPU usage (NVIDIA)
nvidia-smi -l 1

# Watch Ollama logs
journalctl -u ollama -f
