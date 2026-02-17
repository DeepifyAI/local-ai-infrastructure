#!/usr/bin/env python3
import ollama

response = ollama.chat(
    model='gemma2:9b',
    messages=[
        {'role': 'system', 'content': 'You are a concise technical writer. Give one-sentence answers.'},
        {'role': 'user', 'content': 'Explain CUDA in one sentence.'}
    ]
)

print("System prompt demo — asking model with role:")
print(f"Q: Explain CUDA in one sentence.")
print(f"A: {response['message']['content']}")
