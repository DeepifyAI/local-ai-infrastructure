#!/usr/bin/env python3
"""Chapter 6: A minimal chatbot with conversation memory."""
from ollama import chat

print("=== Local Chatbot with Memory ===")
print()

history = []
questions = [
    "My name is Jake. What's the capital of France?",
    "What's its population?",
    "Do you remember my name?",
]

for q in questions:
    print(f"You: {q}")
    history.append({"role": "user", "content": q})
    
    response = chat(model="gemma2:9b", messages=history)
    answer = response["message"]["content"]
    history.append({"role": "assistant", "content": answer})
    
    # Truncate long answers for demo
    if len(answer) > 200:
        answer = answer[:200] + "..."
    print(f"AI:  {answer}")
    print()

print(f"Conversation history: {len(history)} messages")
print("The model remembers context across turns. All local.")
