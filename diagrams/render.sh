#!/bin/bash
# Render all Mermaid diagrams to SVG and PNG via Kroki API
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$DIR/src"
SVG="$DIR/svg"
PNG="$DIR/png"

mkdir -p "$SVG" "$PNG"

echo "=== Rendering Mermaid Diagrams (via Kroki) ==="

for mmd in "$SRC"/*.mmd; do
    name=$(basename "$mmd" .mmd)
    echo -n "  $name... "
    
    # Encode diagram for Kroki API
    ENCODED=$(cat "$mmd" | python3 -c "
import sys, base64, zlib
data = sys.stdin.read().encode('utf-8')
compressed = zlib.compress(data, 9)
encoded = base64.urlsafe_b64encode(compressed).decode('ascii')
print(encoded)
")
    
    # SVG
    curl -s "https://kroki.io/mermaid/svg/${ENCODED}" -o "$SVG/${name}.svg" 2>/dev/null
    
    # PNG  
    curl -s "https://kroki.io/mermaid/png/${ENCODED}" -o "$PNG/${name}.png" 2>/dev/null
    
    if [ -f "$SVG/${name}.svg" ] && [ -s "$SVG/${name}.svg" ]; then
        svg_kb=$(($(stat -c%s "$SVG/${name}.svg") / 1024))
        png_kb=$(($(stat -c%s "$PNG/${name}.png") / 1024))
        echo "✅ SVG(${svg_kb}KB) PNG(${png_kb}KB)"
    else
        echo "⚠️ Failed"
    fi
done

echo ""
echo "=== Done ==="
echo "SVGs: $(ls $SVG/*.svg 2>/dev/null | wc -l)"
echo "PNGs: $(ls $PNG/*.png 2>/dev/null | wc -l)"
