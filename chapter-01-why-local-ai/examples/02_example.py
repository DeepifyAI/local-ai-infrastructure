#!/usr/bin/env python3
# latency_test.py
import time
import requests
from ollama import chat

# Test 1: OpenAI API (GPT-4o)
start = time.time()
response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {OPENAI_KEY}"},
    json={
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": "Say hello"}]
    }
)
cloud_latency = time.time() - start

# Test 2: Local Ollama (Gemma2 9B)
start = time.time()
response = chat(model='gemma2:9b', messages=[
    {'role': 'user', 'content': 'Say hello'}
])
local_latency = time.time() - start

print(f"Cloud: {cloud_latency*1000:.0f}ms")
print(f"Local: {local_latency*1000:.0f}ms")
