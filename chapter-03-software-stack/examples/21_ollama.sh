#!/bin/bash
ollama create python-assistant -f Modelfile.assistant

# Use it:
ollama run python-assistant
