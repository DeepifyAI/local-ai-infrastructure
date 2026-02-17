#!/bin/bash
# Kill old Ollama process
pkill ollama

# Or change port
OLLAMA_HOST=0.0.0.0:11435 ollama serve
