#!/bin/bash
# Use native ARM64 Python
python3 -m venv venv
source venv/bin/activate
pip install ollama numpy pandas

# Everything should have ARM64 wheels now (2026)
