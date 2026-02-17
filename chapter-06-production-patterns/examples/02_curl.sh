#!/bin/bash
curl http://localhost:8000/v1/chat/completions -d '{
  "model": "llama3.1:8b",
  "messages": [{"role": "user", "content": "Hello"}]
}'
