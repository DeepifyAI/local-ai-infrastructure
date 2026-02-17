#!/usr/bin/env python3
import ollama

response = ollama.chat(model='gemma2:9b', messages=[
  {'role': 'user', 'content': 'Why is local AI better for privacy? Answer in 2 sentences.'}
])

print(response['message']['content'])
