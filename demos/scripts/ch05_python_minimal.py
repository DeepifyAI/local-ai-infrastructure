#!/usr/bin/env python3
"""
The entire local AI stack in 3 lines of Python.
"""
print("# Here's all the code you need:\n")
print("  from ollama import chat")
print("  response = chat(model='gemma2:9b', messages=[{'role':'user','content':'Hello!'}])")
print("  print(response['message']['content'])")
print("\n# Running it now...\n")

from ollama import chat
response = chat(model='gemma2:9b', messages=[{'role': 'user', 'content': 'Say hello in exactly 5 words.'}])
print(f"  → {response['message']['content']}")
print("\n✓  That's the whole API. No account. No rate limits. No $0.01/query.")
