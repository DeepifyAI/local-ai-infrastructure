#!/usr/bin/env python3
import ollama

print("Streaming response from local model:\n")
for chunk in ollama.chat(model='gemma2:9b', messages=[
  {'role': 'user', 'content': 'Write a short 4-line poem about Python programming'}
], stream=True):
    print(chunk['message']['content'], end='', flush=True)
print()  # newline at end
