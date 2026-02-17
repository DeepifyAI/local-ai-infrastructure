#!/usr/bin/env python3
"""
Streaming: watch the AI generate tokens in real time.
Each word arrives the moment it's computed.
"""
import ollama

print("Watch the AI generate tokens as they arrive:\n")
print("─" * 50)

for chunk in ollama.chat(
    model='gemma2:9b',
    messages=[{'role': 'user', 'content': 'Write a 3-line haiku about running AI locally. Just the haiku, no title.'}],
    stream=True
):
    print(chunk['message']['content'], end='', flush=True)

print("\n" + "─" * 50)
print("\n✓  Each token streamed directly from your GPU — no cloud latency.")
