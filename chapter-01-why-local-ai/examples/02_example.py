#!/usr/bin/env python3
# latency_test.py
import time
import requests
from ollama import chat

# Test 1: Cloud API (simulated — no key required for demo)
print("Simulating cloud API latency (typical: 500-2000ms)...")
import random
cloud_latency = random.uniform(0.5, 1.8)  # realistic cloud latency simulation
time.sleep(0.2)  # brief pause

# Test 2: Local Ollama (Gemma2 9B)
print("Testing local Ollama (Gemma2 9B)...")
start = time.time()
response = chat(model='gemma2:9b', messages=[
    {'role': 'user', 'content': 'Say hello in one word.'}
])
local_latency = time.time() - start

print(f"\nResults:")
print(f"  Cloud (GPT-4o simulated): {cloud_latency*1000:.0f}ms")
print(f"  Local (Gemma2 9B):        {local_latency*1000:.0f}ms")
speedup = cloud_latency / local_latency if local_latency > 0 else 0
if speedup >= 1:
    print(f"  Local is {speedup:.1f}x faster (no network round-trip!)")
else:
    print(f"  Note: First inference includes model load time")
