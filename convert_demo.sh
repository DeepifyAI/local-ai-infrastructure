#!/bin/bash
# convert_demo.sh CASTFILE OUTMP4
CAST="$1"
MP4="$2"
GIF="${CAST%.cast}.gif"

echo "Converting $CAST → $MP4"
agg --font-size 16 --cols 100 --rows 30 "$CAST" "$GIF" && \
ffmpeg -y -i "$GIF" -movflags faststart -pix_fmt yuv420p \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "$MP4" -loglevel quiet && \
rm -f "$GIF" "$CAST" && \
echo "Done: $MP4"
