#!/bin/bash
pip install vllm

# Serve a model
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000

# Use like OpenAI
curl http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "prompt": "Hello world",
    "max_tokens": 50
  }'
