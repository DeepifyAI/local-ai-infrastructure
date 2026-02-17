#!/bin/bash
# Quick Ollama health check — run this if something seems broken

echo "=== Ollama Health Check ==="; echo ""

# 1. Is Ollama running?
echo -n "  Ollama service:  "
curl -sf http://localhost:11434 > /dev/null && echo "✓  running" || echo "✗  not running (run: ollama serve)"

# 2. GPU
echo -n "  GPU:             "
GPU=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null)
[ -n "$GPU" ] && echo "✓  $GPU" || echo "CPU mode (no NVIDIA GPU detected)"

# 3. Models downloaded?
echo -n "  Models ready:    "
COUNT=$(ollama list 2>/dev/null | tail -n +2 | wc -l)
echo "✓  $COUNT model(s) installed"

# 4. Quick inference test
echo -n "  Inference test:  "
RESP=$(curl -sf http://localhost:11434/api/generate \
  -d '{"model":"gemma2:9b","prompt":"Reply with OK","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'].strip())" 2>/dev/null)
[ -n "$RESP" ] && echo "✓  model responded" || echo "✗  no response"

echo ""
echo "All good? You're ready to build."
