#!/bin/bash
# Record priority demos - the ones that matter most for beginners
set -e

DEMOS_DIR="$(dirname "$0")/mp4"
SCRIPTS_DIR="$(dirname "$0")/scripts"
mkdir -p "$DEMOS_DIR"

record() {
    local script="$1"
    local name="$2"
    local cast="/tmp/demo-${name}.cast"
    local gif="/tmp/demo-${name}.gif"
    local mp4="${DEMOS_DIR}/${name}.mp4"
    
    local ext="${script##*.}"
    local cmd="python3 $script"
    [ "$ext" = "sh" ] && cmd="bash $script"
    
    echo "Recording: $name"
    timeout 30 asciinema rec "$cast" --command "$cmd" --overwrite --idle-time-limit 3 2>/dev/null || true
    
    if [ ! -f "$cast" ]; then
        echo "  FAIL (no recording)"
        return
    fi
    
    agg --font-size 16 --cols 100 --rows 30 "$cast" "$gif" 2>/dev/null
    ffmpeg -y -i "$gif" -movflags faststart -pix_fmt yuv420p \
        -vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2' "$mp4" 2>/dev/null
    rm -f "$cast" "$gif"
    
    if [ -f "$mp4" ]; then
        echo "  OK ($(du -k "$mp4" | cut -f1)KB)"
    else
        echo "  FAIL"
    fi
}

echo "=== Recording Priority Demos ==="
echo ""

# Chapter 1 - WHY local (no Ollama needed)
record "$SCRIPTS_DIR/ch01-cost-comparison.py" "ch01-cost-comparison"

# Chapter 2 - Hardware check (no Ollama needed)
record "$SCRIPTS_DIR/ch02-check-hardware.py" "ch02-check-hardware"

# Chapter 4 - First contact with Ollama
record "$SCRIPTS_DIR/ch04-list-models.sh" "ch04-list-models"

# Chapter 5 - API calls (needs Ollama)
record "$SCRIPTS_DIR/ch05-curl-api.sh" "ch05-curl-api"
record "$SCRIPTS_DIR/ch05-first-api-call.py" "ch05-first-api-call"
record "$SCRIPTS_DIR/ch05-streaming.py" "ch05-streaming"

# Chapter 6 - Real patterns (needs Ollama)
record "$SCRIPTS_DIR/ch06-simple-chatbot.py" "ch06-simple-chatbot"
record "$SCRIPTS_DIR/ch06-tool-calling.py" "ch06-tool-calling"

# Chapter 7 - Troubleshooting
record "$SCRIPTS_DIR/ch07-health-check.sh" "ch07-health-check"

echo ""
echo "=== Done ==="
ls -la "$DEMOS_DIR"/*.mp4 2>/dev/null
echo ""
echo "Total: $(ls "$DEMOS_DIR"/*.mp4 2>/dev/null | wc -l) demos"
