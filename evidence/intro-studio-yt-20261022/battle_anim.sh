#!/bin/bash
cd /e/PROGETTI/ragequit/.verify/intro-studio-yt-20261022
for n in 01 02 03 04 05 06 07 08; do
  until [ -f keys/b$n.png ]; do sleep 15; done
  [ -f clips/b$n.mp4 ] && continue
  for t in 1 2 3; do python -u wangen.py prompts/battle/m$n.txt b$n keys/b$n.png --frames 33 --w 960 --h 544 --seed 3$n 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-200; [ -f clips/b$n.mp4 ] && break; sleep 5; done
  echo "CLIP b$n pronta"
done
echo ANIM-FINE
