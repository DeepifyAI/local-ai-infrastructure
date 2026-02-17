#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
import ollama

def process_document(doc):
    summary = ollama.generate(
        model='llama3.1:8b',
        prompt=f'Summarize in 2 sentences:\n\n{doc}'
    )
    return summary['response']

documents = [...]  # Your 1000 documents

# Process 4 at a time
with ThreadPoolExecutor(max_workers=4) as executor:
    summaries = list(executor.map(process_document, documents))
