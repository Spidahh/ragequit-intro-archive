"""Studio capture of only the two changed base bodies; no raster editing or game-data edits."""
from pathlib import Path
import os

root=Path('E:/PROGETTI/ragequit')
os.environ['RQ_CLASSES']='Pyromancer,Tempestblade'
os.environ['RQ_BASE_ONLY']='1'
os.environ['RQ_HQ_PREVIEW']='1'
if os.environ.get('RQ_NATIVE_COLOR') == '1':
    os.environ['RQ_OPAQUE_PREVIEW']='1'
else:
    os.environ.pop('RQ_OPAQUE_PREVIEW',None)
os.environ['RQ_RIM_COLOR']='230,235,255'
source=root/'tools/unreal/capture-hero-skins.py'
code=source.read_text(encoding='utf-8')
old="if case['cls'] == 'Warmaster' or not w or list(lo.get_editor_property('HeroWeaponBones')):"
new="if case['cls'] == 'Warmaster' or not w or (case['cls'] != 'Tempestblade' and list(lo.get_editor_property('HeroWeaponBones'))):"
assert code.count(old)==1
code=code.replace(old,new)
old="body.set_editor_property('disallow_nanite', case['cls'] == 'Warmaster')"
assert code.count(old)==1
code=code.replace(old,"body.set_editor_property('disallow_nanite', case['cls'] in ('Warmaster','Tempestblade'))")
old="            if S['ticks'] == 12:\n                own_weapon(S['bodyc'], CASES[S['i']])"
assert code.count(old)==1
new=old+"""
            if S['ticks'] >= 12 and CASES[S['i']]['cls'] == 'Tempestblade':
                preview_lo = unreal.load_asset(LO + H.HEROES['Tempestblade'][0])
                WM.refresh_native_weapon_hidden(S['bodyc'], preview_lo)
                S['preview_excluded_bones'] = WM.hidden_native_weapon_bones(S['bodyc'], preview_lo)
"""
code=code.replace(old,new)
exec(compile(code,str(source),'exec'),dict(__file__=str(source),__name__='__main__'))
