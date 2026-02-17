#!/bin/bash
# Download Gemma 2B (small, fast)
ollama pull gemma2:2b

# Check downloaded models
ollama list

# Output:
# NAME            ID              SIZE    MODIFIED
# gemma2:2b       abc123def       1.6 GB  2 minutes ago
