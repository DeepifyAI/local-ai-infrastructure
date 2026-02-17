#!/bin/bash
# Check Ollama logs while making request:
journalctl -u ollama -f
# Then in another terminal:
curl http://localhost:11434/api/generate -d '...'
