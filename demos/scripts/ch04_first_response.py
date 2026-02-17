#!/usr/bin/env python3
"""
Your first local AI response.
That's it. 3 lines of Python.
"""
from ollama import chat

print("Sending your first question to a local AI...\n")

response = chat(
    model='gemma2:9b',
    messages=[{'role': 'user', 'content': 'In one sentence: what is a local AI model?'}]
)

print(f"AI: {response['message']['content']}")
print("\n✓  Ran entirely on this machine. Zero internet. Zero cost per query.")
