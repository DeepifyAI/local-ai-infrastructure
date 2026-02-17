#!/usr/bin/env python3
from openai import OpenAI

# Point at Ollama instead of OpenAI
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama'  # Required but not used
)

response = client.chat.completions.create(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
