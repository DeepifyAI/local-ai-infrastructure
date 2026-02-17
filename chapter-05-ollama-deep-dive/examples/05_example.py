#!/usr/bin/env python3
for chunk in ollama.chat(model='llama3.1:8b', messages=[
  {'role': 'user', 'content': 'Write a poem about Python'}
], stream=True):
    print(chunk['message']['content'], end='', flush=True)
