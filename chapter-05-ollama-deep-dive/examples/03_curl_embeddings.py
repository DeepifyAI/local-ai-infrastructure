#!/usr/bin/env python3
"""Demo: Generate embeddings via Ollama REST API."""
import requests
import json

print("Generating embedding via Ollama REST API...")
print("Model: nomic-embed-text (768-dim)\n")

text = "The quick brown fox jumps over the lazy dog."
print(f"Input text: {text!r}\n")

response = requests.post(
    'http://localhost:11434/api/embeddings',
    json={"model": "nomic-embed-text", "prompt": text}
)

data = response.json()
embedding = data['embedding']

print(f"Embedding dimensions: {len(embedding)}")
print(f"First 5 values: {[round(v, 4) for v in embedding[:5]]}")
print(f"Last 5 values:  {[round(v, 4) for v in embedding[-5:]]}")
print(f"\nStatus: {response.status_code} OK")
print("Embedding generated locally — no data left your machine.")
