#!/usr/bin/env python3
import ollama

response = ollama.chat(model='llama3.1:8b', messages=[
  {'role': 'user', 'content': 'Why is local AI better?'}
])

print(response['message']['content'])
