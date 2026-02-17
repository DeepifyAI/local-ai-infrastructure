#!/bin/bash
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.1:8b",
  "messages": [
    {"role": "user", "content": "What is 2+2?"},
    {"role": "assistant", "content": "4"},
    {"role": "user", "content": "What about 2+3?"}
  ],
  "stream": false
}'
