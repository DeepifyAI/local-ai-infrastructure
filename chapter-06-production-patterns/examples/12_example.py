#!/usr/bin/env python3
# Measure response time
import time
start = time.time()
response = ollama.generate(...)
print(f"Took {time.time() - start:.2f}s")
