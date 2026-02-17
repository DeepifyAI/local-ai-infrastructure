#!/usr/bin/env python3
try:
    response = ollama.generate(...)
except Exception as e:
    print(f"Model failed: {e}")
    # Fall back or retry
