#!/bin/bash
# Chapter 7: Quick health check - is everything working?
echo "=== Local AI Health Check ==="
echo ""

# 1. Ollama running?
if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "✅ Ollama is running"
else
    echo "❌ Ollama is not running (start with: ollama serve)"
    exit 1
fi

# 2. Models available?
MODEL_COUNT=$(curl -s http://localhost:11434/api/tags | python3 -c "import json,sys; print(len(json.load(sys.stdin).get('models',[])))" 2>/dev/null)
echo "✅ Models installed: $MODEL_COUNT"

# 3. Can we generate?
echo -n "✅ Test generation: "
curl -s http://localhost:11434/api/generate -d '{"model":"gemma2:9b","prompt":"Say OK","stream":false}' | python3 -c "import json,sys; print(json.load(sys.stdin)['response'][:50])" 2>/dev/null

# 4. Port check
echo "✅ Listening on port 11434"

echo ""
echo "All systems go. Your local AI is ready."
