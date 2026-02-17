#!/usr/bin/env python3
def answer_with_fallback(query):
    # Try small/fast model first
    response = ollama.generate(model='gemma2:2b', prompt=query)
    answer = response['response']
    
    # Check if confident (simple heuristic)
    if len(answer) < 50 or 'not sure' in answer.lower():
        # Fall back to larger model
        response = ollama.generate(model='llama3.1:70b', prompt=query)
        answer = response['response']
    
    return answer
