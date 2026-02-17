#!/bin/bash
# Chapter 5: Talk to Ollama with just curl - no Python needed
echo "=== Calling your local AI with curl ==="
echo ""
echo "POST http://localhost:11434/api/generate"
echo ""

curl -s http://localhost:11434/api/generate -d '{
  "model": "gemma2:9b",
  "prompt": "Explain Docker in 2 sentences.",
  "stream": false
}' | python3 -c "import json,sys; r=json.load(sys.stdin); print(r['response'])"

echo ""
echo "That's it. Your local AI, accessible via a simple HTTP API."
