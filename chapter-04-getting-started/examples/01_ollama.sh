#!/bin/bash
# macOS/Linux (usually auto-starts)
ollama serve

# Check it's running:
curl http://localhost:11434
# Should respond with: "Ollama is running"
