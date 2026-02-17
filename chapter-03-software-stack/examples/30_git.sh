#!/bin/bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make LLAMA_CUDA=1  # With GPU support

# Download a model (GGUF format)
wget https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf

# Run
./main -m llama-2-7b.Q4_K_M.gguf -p "Hello world"
