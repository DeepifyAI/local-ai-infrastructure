#!/usr/bin/env python3
"""
A chatbot that remembers what you said.
Conversation history = just a Python list.
"""
import ollama

history = []

def ask(question):
    history.append({'role': 'user', 'content': question})
    response = ollama.chat(model='gemma2:9b', messages=history)
    answer = response['message']['content'].strip()
    history.append({'role': 'assistant', 'content': answer})
    print(f"  You: {question}")
    print(f"  AI:  {answer}\n")

print("=== Local Chatbot — remembers everything you say ===\n")

ask("My name is Alex and I work in fintech. Say hi!")
ask("What industry do I work in?")  # Tests memory

print("✓  Two separate API calls — the AI remembered because we kept the history list.")
