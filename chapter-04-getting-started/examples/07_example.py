#!/usr/bin/env python3
import requests

response = requests.post('http://localhost:11434/api/generate', json={
    "model": "gemma2:2b",
    "prompt": "Say hello",
    "stream": False
})

print(response.json()['response'])
