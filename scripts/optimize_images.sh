#!/usr/bin/env bash
# Recreate lightweight WebP presentation images from the original PNG sources.
# Requires ImageMagick with WebP support. The original assets remain untouched.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/optimized
for image in assets/*.png; do
  name=$(basename "$image" .png)
  case "$name" in
    og-cover) continue ;;
    picture) convert "$image" -strip -quality 88 -define webp:method=5 "assets/optimized/$name.webp" ;;
    *) convert "$image" -resize '980x1300>' -strip -quality 80 -define webp:method=5 "assets/optimized/$name.webp" ;;
  esac
done
