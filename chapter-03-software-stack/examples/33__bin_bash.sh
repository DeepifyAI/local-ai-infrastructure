#!/bin/bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ollama
brew install ollama

# Or download from ollama.com

# Start Ollama
ollama serve
