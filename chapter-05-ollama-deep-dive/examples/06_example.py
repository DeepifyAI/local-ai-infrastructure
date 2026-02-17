#!/usr/bin/env python3
response = ollama.chat(
    model='llama3.1:8b',
    messages=[
        {'role': 'system', 'content': 'You are a concise technical writer.'},
        {'role': 'user', 'content': 'Explain CUDA in one sentence.'}
    ]
)
