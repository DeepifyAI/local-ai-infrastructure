#!/usr/bin/env python3
# BAD: Will fail on long conversations
ollama.chat(model='llama3.1:8b', messages=very_long_history)

# GOOD: Trim to last N messages
def trim_history(messages, max_count=20):
    return messages[-max_count:]
