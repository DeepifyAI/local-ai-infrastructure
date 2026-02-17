#!/bin/bash
lsof -i :11434
# If something else is using it:
OLLAMA_HOST=0.0.0.0:11435 ollama serve
