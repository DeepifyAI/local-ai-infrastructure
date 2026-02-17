#!/usr/bin/env python3
"""
RAG: Answer questions from YOUR private documents.
Everything stays on your machine.
"""
import ollama
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Your private documents (example: internal company notes)
docs = [
    "Product launch is scheduled for March 15th, 2026.",
    "The engineering team meets every Tuesday at 2pm GMT.",
    "Q1 revenue target is £500k. Current pipeline: £340k.",
]

print("=== RAG: Answer from Private Documents ===\n")
print("Your documents:")
for i, doc in enumerate(docs, 1):
    print(f"  {i}. {doc}")

question = "When is the product launch?"
print(f"\nQuestion: {question}")
print("\nStep 1: Embedding documents locally...", end='', flush=True)

doc_embeddings = [ollama.embeddings(model='nomic-embed-text', prompt=d)['embedding'] for d in docs]
q_embedding = ollama.embeddings(model='nomic-embed-text', prompt=question)['embedding']
print(" done")

sims = cosine_similarity([q_embedding], doc_embeddings)[0]
best_doc = docs[np.argmax(sims)]
print(f"Step 2: Most relevant doc: \"{best_doc}\"")
print("Step 3: Generating answer...", end='', flush=True)

response = ollama.generate(
    model='gemma2:9b',
    prompt=f"Answer in one sentence using only this context: {best_doc}\nQuestion: {question}"
)
print()
print(f"\nAnswer: {response['response'].strip()}")
print("\n✓  Your documents never left your machine.")
