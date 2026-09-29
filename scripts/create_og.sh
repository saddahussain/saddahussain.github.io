#!/usr/bin/env bash
# Optional: regenerate the social preview with ImageMagick 6+.
set -euo pipefail
cd "$(dirname "$0")/.."
convert -size 1200x630 xc:'#13191a' \
  -fill '#1a2821' -stroke none -draw 'circle 970,330 970,35' \
  -fill none -stroke '#385441' -strokewidth 1 \
  -draw 'circle 970,330 970,75' -draw 'circle 970,330 970,-5' \
  -stroke '#26342b' -draw 'line 0,90 1200,90' -draw 'line 0,560 1200,560' \
  \( assets/optimized/picture.webp -resize x590 \) -gravity southeast -geometry +5+0 -composite \
  -gravity northwest -font DejaVu-Sans-Bold -fill '#c9f27b' -pointsize 20 \
  -annotate +70+41 's/h' \
  -font DejaVu-Sans -fill '#f6f7f2' -pointsize 19 \
  -annotate +130+44 'SADDA HUSSAIN BUTT' \
  -font DejaVu-Sans-Bold -pointsize 70 \
  -annotate +66+177 'Android built' \
  -annotate +66+265 'for the real' \
  -fill '#c9f27b' -annotate +66+353 'world.' \
  -font DejaVu-Sans -fill '#b8c9ba' -pointsize 16 \
  -annotate +70+515 'KOTLIN  /  JETPACK COMPOSE  /  CONNECTED SYSTEMS' \
  -strip -depth 8 -type TrueColor -define png:compression-level=9 PNG24:assets/og-cover.png
