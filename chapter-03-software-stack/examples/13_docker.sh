#!/bin/bash
# Run Ollama in Docker
docker run -d \
    --name ollama \
    --gpus all \
    -v ollama_data:/root/.ollama \
    -p 11434:11434 \
    --restart unless-stopped \
    ollama/ollama:latest

# Check logs
docker logs -f ollama

# Use it
docker exec -it ollama ollama run gemma2:2b
