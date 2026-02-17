#!/bin/bash
# example_modelfile
# Save as: Modelfile.assistant

FROM gemma2:9b

# Set system prompt
SYSTEM """
You are a helpful AI assistant specialized in Python programming.
You provide concise, working code examples with clear explanations.
You never make up information - if you don't know, you say so.
"""

# Set parameters
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER num_ctx 4096

# Set template (optional)
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}<|end|>
{{ end }}{{ if .Prompt }}<|user|>
{{ .Prompt }}<|end|>
{{ end }}<|assistant|>
{{ .Response }}<|end|>
"""
