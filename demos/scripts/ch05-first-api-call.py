#!/usr/bin/env python3
"""Chapter 5: Your first API call to a local LLM."""
from ollama import chat

print("=== Asking your LOCAL AI a question ===")
print()

response = chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "What is machine learning in one sentence?"}]
)

print(f"Question: What is machine learning in one sentence?")
print()
print(f"Answer: {response['message']['content']}")
print()
print("That response came from YOUR machine. Zero cloud. Zero cost.")
