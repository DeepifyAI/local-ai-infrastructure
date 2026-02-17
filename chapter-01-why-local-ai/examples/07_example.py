#!/usr/bin/env python3
# local_inference.py
from ollama import chat

response = chat(
    model='gemma2:9b',
    messages=[{
        'role': 'user',
        'content': 'Explain why local AI is better for privacy in one sentence.'
    }]
)

print(response['message']['content'])
