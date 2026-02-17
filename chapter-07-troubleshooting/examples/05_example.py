#!/usr/bin/env python3
# Too high (>1.5) = incoherent
ollama.generate(
    model='llama3.1:8b',
    prompt='...',
    options={'temperature': 0.7}  # Lower = more focused
)
