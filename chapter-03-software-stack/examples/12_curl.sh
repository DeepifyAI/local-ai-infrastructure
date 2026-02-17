#!/bin/bash
# One-line install
curl -fsSL https://ollama.com/install.sh | sh

# Verify
ollama --version

# Start service (automatically runs on boot)
sudo systemctl enable ollama
sudo systemctl start ollama

# Check status
sudo systemctl status ollama
