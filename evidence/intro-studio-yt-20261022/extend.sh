#!/bin/bash
# un unico combattimento continuo: ogni pezzo parte dall'ultimo fotogramma del pezzo precedente
cd /e/PROGETTI/ragequit/.verify/intro-studio-yt-20261022
start=keys/b01.png
for n in 1 2 3 4; do
  if [ ! -f clips/s$n.mp4 ]; then
    for t in 1 2 3; do python -u wangen.py prompts/battle/s$n.txt s$n $start --frames 81 --w 960 --h 544 --seed 5$n 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-160; [ -f clips/s$n.mp4 ] && break; sleep 5; done
  fi
  ffmpeg -hide_banner -loglevel error -y -sseof -0.1 -i clips/s$n.mp4 -frames:v 1 keys/s${n}_last.png
  start=keys/s${n}_last.png
  echo "PEZZO s$n"
done
echo ESTENSIONE-FINE
