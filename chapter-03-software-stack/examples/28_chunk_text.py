#!/usr/bin/env python3
# embedding_pipeline.py
"""
Document embedding pipeline.
"""

import os
from typing import List
from ollama import embeddings

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)
    
    return chunks

def embed_chunks(chunks: List[str], model: str = 'nomic-embed-text') -> List[List[float]]:
    """Generate embeddings for chunks."""
    vectors = []
    
    for chunk in chunks:
        response = embeddings(model=model, prompt=chunk)
        vectors.append(response['embedding'])
    
    return vectors

def process_document(file_path: str) -> dict:
    """Process a document into embeddings."""
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Chunk
    chunks = chunk_text(text)
    
    # Embed
    vectors = embed_chunks(chunks)
    
    return {
        'file': file_path,
        'chunks': chunks,
        'embeddings': vectors
    }

if __name__ == '__main__':
    # First, pull embedding model
    os.system('ollama pull nomic-embed-text')
    
    # Example
    with open('test_doc.txt', 'w') as f:
        f.write("This is a test document about AI. " * 100)
    
    result = process_document('test_doc.txt')
    
    print(f"Processed {len(result['chunks'])} chunks")
    print(f"Embedding dimension: {len(result['embeddings'][0])}")
