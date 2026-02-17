#!/usr/bin/env python3
from ollama import chat

response = chat(
    model='gemma2:2b',
    messages=[{'role': 'user', 'content': 'Hello!'}]
)

print(response['message']['content'])
