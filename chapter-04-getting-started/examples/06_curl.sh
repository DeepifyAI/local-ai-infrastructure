#!/bin/bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma2:2b",
  "prompt": "Explain what a local AI model is in one sentence.",
  "stream": false
}'
