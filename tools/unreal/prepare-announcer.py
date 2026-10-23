"""D0645: import approved voice lines; no changes to combat data, maps or gameplay.
Run through run-and-quit.py in the full editor. Source: art/audio/announcer.
"""
from pathlib import Path
import os,json,traceback,hashlib
import unreal
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(os.environ['RQ_OUT']);R={'checks':{},'assets':[],'errors':[],'success':False}
try:
    manifest=json.loads((ROOT/'art/audio/announcer/manifest.json').read_text(encoding='utf-8'))
    destination='/Game/Ragequit/Audio/Announcer'
    # D0842: reimport must preserve the narrator's independent route once installed.
    dedicated=unreal.EditorAssetLibrary.does_asset_exist('/Game/Ragequit/Audio/Announcer/SC_Announcer')
    sfx=unreal.load_asset('/Game/Ragequit/Audio/Announcer/SC_Announcer' if dedicated else '/Game/Audio/Classes/SFX')
    submix=unreal.load_asset('/Game/Audio/Submixes/MainSubmix' if dedicated else '/Game/Audio/Submixes/SFXSubmix')
    if not sfx or not submix: raise RuntimeError('Missing existing Lyra SFX routing')
    for clip in manifest['clips']:
        source=ROOT/'art/audio/announcer'/clip['file']
        if hashlib.sha256(source.read_bytes()).hexdigest()!=clip['sha256']: raise RuntimeError('Source hash changed: '+clip['file'])
        task=unreal.AssetImportTask();task.set_editor_property('filename',str(source))
        task.set_editor_property('destination_path',destination)
        task.set_editor_property('destination_name',source.stem)
        task.set_editor_property('automated',True);task.set_editor_property('replace_existing',True);task.set_editor_property('save',False)
        task.set_editor_property('factory',unreal.SoundFactory())
        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
        wave=unreal.load_asset(destination+'/'+source.stem)
        if not isinstance(wave,unreal.SoundWave): raise RuntimeError('Not a SoundWave: '+source.stem)
        for key,value in {'sound_class_object':sfx,'sound_submix_object':submix,'volume':1.0,'pitch':1.0,
            'looping':False,'priority':1000.0 if dedicated else 10.0,'attenuation_settings':None,
            'loading_behavior':unreal.SoundWaveLoadingBehavior.FORCE_INLINE,
            'sound_asset_compression_type':unreal.SoundAssetCompressionType.PCM}.items():
            wave.set_editor_property(key,value)
        unreal.EditorAssetLibrary.save_loaded_asset(wave,only_if_is_dirty=False)
        duration=float(wave.get_editor_property('duration'))
        row={'path':wave.get_path_name(),'seconds':duration,'channels':wave.get_editor_property('num_channels'),
             'rate':wave.get_editor_property('imported_sample_rate'),'class':sfx.get_path_name(),'submix':submix.get_path_name()}
        R['assets'].append(row)
        R['checks'][source.stem]=row['channels']==1 and row['rate']==48000 and abs(duration-clip['seconds'])<.015
    # (21/10 sera: the lines of the manifest, all of them: seven, then thirty-four)
    R['checks']['all_lines']=len(R['assets'])==len(manifest['clips'])
    R['success']=all(R['checks'].values())
except Exception: R['errors'].append(traceback.format_exc())
(OUT/'report.json').write_text(json.dumps(R,indent=2,default=str),encoding='utf-8')
unreal.log('ANNOUNCER_IMPORT '+json.dumps(R))
