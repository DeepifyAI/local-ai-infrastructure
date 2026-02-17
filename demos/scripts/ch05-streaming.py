#!/usr/bin/env python3
"""Chapter 5: Watch tokens stream in real-time from your local model."""
from ollama import chat
import sys

print("=== Streaming Response (watch it think!) ===")
print()
print("Q: Write a haiku about running AI locally")
print()
print("A: ", end="", flush=True)

for chunk in chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "Write a haiku about running AI locally. Just the haiku, nothing else."}],
    stream=True
):
    token = chunk["message"]["content"]
    print(token, end="", flush=True)

print()
print()
print("Each token generated on YOUR GPU. No latency to the cloud.")
