#!/bin/bash
# un solo combattimento continuo: ogni fotogramma chiave nasce dal precedente, ogni pezzo va dal chiave n al chiave n+1
cd /e/PROGETTI/ragequit/.verify/intro-studio-yt-20261022
A=E:/PROGETTI/ragequit/art/ui/menu/T_UI_Menu_Arena.png; RP=refs/ref_pyromancer_full.png; RT=refs/ref_tempestblade.png
key(){ n=$1; shift; [ -f keys/$n.png ] && return; for t in 1 2 3; do python -u qedit.py prompts/battle/$n.txt $n "$@" --lightning 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-160; [ -f keys/$n.png ] && return; sleep 5; done; }
anim(){ n=$1; shift; [ -f clips/c$n.mp4 ] && return; for t in 1 2 3; do python -u wangen.py prompts/battle/m$n.txt c$n "$@" --frames 33 --w 960 --h 544 --seed 4$n 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-160; [ -f clips/c$n.mp4 ] && return; sleep 5; done; }
key b01 $A $RT $RP --seed 71
prev=01
for n in 02 03 04 05 06 07 08; do
  key b$n keys/b$prev.png $RT $RP --seed 7$n
  echo "CHIAVE b$n"
  anim $prev keys/b$prev.png --end keys/b$n.png
  echo "PEZZO c$prev"
  prev=$n
done
anim 08 keys/b08.png
echo "PEZZO c08"; echo CATENA-FINE
