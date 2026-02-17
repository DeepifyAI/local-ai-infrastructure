#!/bin/bash
# On machine A (export)
ollama push mymodel

# On machine B (import)
ollama pull mymodel
