#!/bin/bash
# BAD:
curl ... -d '{"model": "llama3.1:8b", "prompt": "test}'

# GOOD:
curl ... -d '{"model": "llama3.1:8b", "prompt": "test"}'
