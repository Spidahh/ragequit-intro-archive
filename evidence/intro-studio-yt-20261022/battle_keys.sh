#!/bin/bash
cd /e/PROGETTI/ragequit/.verify/intro-studio-yt-20261022
A=E:/PROGETTI/ragequit/art/ui/menu/T_UI_Menu_Arena.png; RP=refs/ref_pyromancer_full.png; RT=refs/ref_tempestblade.png
run(){ n=$1; shift; [ -f keys/$n.png ] && return; for t in 1 2 3; do python -u qedit.py prompts/battle/$n.txt $n "$@" 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-200; [ -f keys/$n.png ] && return; sleep 5; done; }
s=71; for n in b01 b02 b03 b04 b05 b06 b07 b08; do run $n $A $RT $RP --seed $s --lightning; s=$((s+1)); done
echo BATCH-FINE
