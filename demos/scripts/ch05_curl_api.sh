#!/bin/bash
# Local AI is just an HTTP API.
# You can call it with curl — same as any web API.

echo "Calling local AI with curl..."
echo ""
echo 'curl http://localhost:11434/api/generate -d '"'"'{"model":"gemma2:9b","prompt":"Name one benefit of local AI","stream":false}'"'"
echo ""

RESPONSE=$(curl -s http://localhost:11434/api/generate \
  -d '{"model":"gemma2:9b","prompt":"Name one benefit of local AI in 10 words or less","stream":false}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['response'].strip())")

echo "Response: $RESPONSE"
echo ""
echo "✓  Local AI = a plain HTTP API running on localhost."
