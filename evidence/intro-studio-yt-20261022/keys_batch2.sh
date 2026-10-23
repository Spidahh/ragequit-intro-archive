#!/bin/bash
cd /e/PROGETTI/ragequit/.verify/intro-studio-yt-20261022
A=E:/PROGETTI/ragequit/art/ui/menu/T_UI_Menu_Arena.png; K2=keys/key02_tempest_land_b.png; RP=refs/ref_pyromancer_full.png; RT=refs/ref_tempestblade.png
run(){ n=$1; shift; [ -f keys/$n.png ] && return; for t in 1 2 3; do python -u qedit.py prompts/$n.txt $n "$@" 2>&1 | grep -E "^(OUT|done|ERROR)" | cut -c1-200; [ -f keys/$n.png ] && return; sleep 5; done; }
run key01_pyro_ritual $A $RP --seed 61
K1=keys/key01_pyro_ritual.png
run key03_pyro_eyes $K1 $RP --seed 51
run key04_tb_grip $K2 $RT --seed 52
run key05_pyro_throw $K1 $RP --seed 53
run key06_tb_cut $K2 $RT --seed 54
run key07_dodge $K2 $RT $RP --seed 55
run key08_hit $K2 $RT $RP --seed 56
run key09_pyro_rise $K1 $RP --seed 57
run key10_standoff $K2 $RT $RP --seed 58
run key11_clash $K2 $RT $RP --seed 59
echo BATCH-FINE
