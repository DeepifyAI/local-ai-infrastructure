#!/usr/bin/env python3
"""Demo: Multi-turn conversation via Ollama REST API (matches ch05 02_curl.sh)."""
import requests
import json

print("=== Multi-turn Chat via Ollama REST API ===\n")

payload = {
    "model": "gemma2:9b",
    "messages": [
        {"role": "user",      "content": "What is 2+2?"},
        {"role": "assistant", "content": "4"},
        {"role": "user",      "content": "What about 2+3?"}
    ],
    "stream": False
}

print("Conversation history:")
for msg in payload['messages']:
    role = msg['role'].capitalize()
    print(f"  {role}: {msg['content']}")

print("\nSending to Ollama...")
response = requests.post('http://localhost:11434/api/chat', json=payload)
data = response.json()

reply = data['message']['content']
print(f"\n  Assistant: {reply}")
print(f"\nOllama remembered context from the previous exchange!")
