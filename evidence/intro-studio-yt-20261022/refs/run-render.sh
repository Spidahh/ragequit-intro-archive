#!/bin/bash
# aspetta che Unreal sia libero (un solo editor alla volta), poi fotografa Pyromancer e Tempestblade come sono oggi
while powershell -NoProfile -Command "if (Get-Process UnrealEditor -ErrorAction SilentlyContinue) {exit 0} else {exit 1}"; do sleep 20; done
cd /e/PROGETTI/ragequit
export RQ_CLASSES='Pyromancer,Tempestblade' RQ_BASE_ONLY=1 RQ_HQ_PREVIEW=1 RQ_RIM_COLOR='230,235,255' RQ_OUT='E:/PROGETTI/ragequit/.verify/intro-studio-yt-20261022/refs/render'
powershell -NoProfile -ExecutionPolicy Bypass -File tools/run-unreal-python.ps1 -Script tools/unreal/capture-hero-skins.py -Name intro-refs 2>&1 | tail -15
ls -la "$RQ_OUT"
