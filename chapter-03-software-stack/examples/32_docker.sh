#!/bin/bash
docker run -p 8080:80 \
  --gpus all \
  ghcr.io/huggingface/text-generation-inference:latest \
  --model-id meta-llama/Llama-3.1-8B-Instruct
