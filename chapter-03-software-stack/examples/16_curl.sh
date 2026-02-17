#!/bin/bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma2:2b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
