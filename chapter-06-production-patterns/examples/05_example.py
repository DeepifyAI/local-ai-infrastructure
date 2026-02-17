#!/usr/bin/env python3
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Embed your documents
docs = [
    "The DGX Spark runs on ARM64 architecture.",
    "Ollama supports local model inference.",
    "Python is great for AI development."
]

embeddings = []
for doc in docs:
    emb = ollama.embeddings(model='nomic-embed-text', prompt=doc)
    embeddings.append(emb['embedding'])

# 2. User asks a question
question = "What architecture does DGX Spark use?"
q_emb = ollama.embeddings(model='nomic-embed-text', prompt=question)['embedding']

# 3. Find most similar document
similarities = cosine_similarity([q_emb], embeddings)[0]
best_match_idx = np.argmax(similarities)
context = docs[best_match_idx]

# 4. Ask model with context
prompt = f"Context: {context}\n\nQuestion: {question}"
response = ollama.generate(model='llama3.1:8b', prompt=prompt)
print(response['response'])
