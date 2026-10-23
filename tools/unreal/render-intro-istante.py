"""Render the author's option 02 (D0930) in an unsaved, isolated editor world.

Real Paragon meshes/clips stay inside Unreal. No game asset, map, loadout or movie
is saved or replaced. Output is a deterministic PNG sequence plus provenance.
RQ_INTRO_MODE=layout renders editorial keyframes; final renders every frame.
"""
import json
import math
import os
import random
import time
import traceback
from pathlib import Path
import unreal as U

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(os.environ['RQ_OUT'])
FRAMES = OUT / 'frames'
FRAMES.mkdir(exist_ok=True)
FPS, SECONDS = 24, 10.0
MODE = os.environ.get('RQ_INTRO_MODE', 'layout')
INDICES = [0, 38, 60, 96, 132, 155, 174, 190, 214, 239] if MODE == 'layout' else list(range(240))
ACT = U.get_editor_subsystem(U.EditorActorSubsystem)
MEL = U.MaterialEditingLibrary
R = {'success': False, 'mode': MODE, 'fps': FPS, 'size': [1920, 1080],
     'author_request': 'D0930, correction D0931', 'version': 2,
     'game_assets_saved': False, 'errors': [], 'frames': [], 'sources': {}, 'pose_samples': []}
S = {'busy': False, 'done': False, 'phase': 'setup', 'ticks': 0, 'i': 0,
     'started': time.monotonic(), 'keep': []}


def vec(*v):
    return U.Vector(*v)


def lerp(a, b, f):
    return tuple(x + (y-x)*f for x, y in zip(a, b))


def ease(x):
    x = max(0., min(1., x))
    return x*x*(3.-2.*x)


def rot_at(a, b):
    d = [y-x for x, y in zip(a, b)]
    return U.Rotator(pitch=math.degrees(math.atan2(d[2], math.hypot(*d[:2]))),
                     yaw=math.degrees(math.atan2(d[1], d[0])), roll=0)


def spawn(cls, p, rot=None):
    a = ACT.spawn_actor_from_class(cls, vec(*p), rot or U.Rotator(), True)
    S['keep'].append(a)
    return a


def material(name, color, metallic=.0, rough=.65, glow=0.):
    # This package remains in editor memory; no save_loaded_asset is used.
    m = U.AssetToolsHelpers.get_asset_tools().create_asset(name, '/Game/__RQIntroMemoryOnly', U.Material, U.MaterialFactoryNew())
    m.set_editor_property('two_sided', False)
    c = MEL.create_material_expression(m, U.MaterialExpressionConstant3Vector)
    c.set_editor_property('constant', U.LinearColor(*color, 1))
    MEL.connect_material_property(c, '', U.MaterialProperty.MP_BASE_COLOR)
    for prop, value in ((U.MaterialProperty.MP_METALLIC, metallic), (U.MaterialProperty.MP_ROUGHNESS, rough)):
        n = MEL.create_material_expression(m, U.MaterialExpressionConstant)
        n.set_editor_property('r', value)
        MEL.connect_material_property(n, '', prop)
    if glow:
        mult = MEL.create_material_expression(m, U.MaterialExpressionMultiply)
        mult.set_editor_property('const_b', glow)
        MEL.connect_material_expressions(c, '', mult, 'A')
        MEL.connect_material_property(mult, '', U.MaterialProperty.MP_EMISSIVE_COLOR)
    else:
        noise = MEL.create_material_expression(m, U.MaterialExpressionNoise)
        noise.set_editor_property('scale', .22)
        noise.set_editor_property('levels', 2)
        amount = MEL.create_material_expression(m, U.MaterialExpressionMultiply)
        amount.set_editor_property('const_b', .012)
        MEL.connect_material_expressions(noise, '', amount, 'A')
        tinted = MEL.create_material_expression(m, U.MaterialExpressionAdd)
        MEL.connect_material_expressions(c, '', tinted, 'A')
        MEL.connect_material_expressions(amount, '', tinted, 'B')
        MEL.connect_material_property(tinted, '', U.MaterialProperty.MP_BASE_COLOR)
    if name=='M_Ivory':
        normal=MEL.create_material_expression(m,U.MaterialExpressionTextureSampleParameter2D)
        normal.set_editor_property('parameter_name','DetailNormal')
        normal.set_editor_property('texture',U.load_asset('/Engine/EngineMaterials/DefaultNormal'))
        normal.set_editor_property('sampler_type',U.MaterialSamplerType.SAMPLERTYPE_NORMAL)
        MEL.connect_material_property(normal,'RGB',U.MaterialProperty.MP_NORMAL)
    MEL.recompile_material(m)
    S['keep'].append(m)
    return m


def mesh_actor(path, p, scale, mat, rotation=None):
    a = spawn(U.StaticMeshActor, p, rotation)
    c = a.static_mesh_component
    c.set_mobility(U.ComponentMobility.MOVABLE)
    c.set_static_mesh(U.load_asset(path))
    for i in range(c.get_num_materials()):
        c.set_material(i, mat)
    a.set_actor_scale3d(vec(*scale))
    return a


def hero(cls, loadout, hero_name, p, yaw, clip_name, at):
    lo = U.load_asset('/Game/Ragequit/Loadouts/' + loadout)
    if not lo:
        raise RuntimeError('Missing loadout: ' + loadout)
    mesh = lo.get_editor_property('HeroMesh')
    a = spawn(U.SkeletalMeshActor, p, U.Rotator(yaw=yaw-90., pitch=0, roll=0))
    k = float(lo.get_editor_property('HeroScale')) or 1.
    a.set_actor_scale3d(vec(k, k, k))
    c = a.get_component_by_class(U.SkeletalMeshComponent)
    c.set_skeletal_mesh_asset(mesh)
    c.set_animation_mode(U.AnimationMode.ANIMATION_SINGLE_NODE)
    c.set_update_animation_in_editor(True)
    c.set_editor_property('visibility_based_anim_tick_option',U.VisibilityBasedAnimTickOption.ALWAYS_TICK_POSE_AND_REFRESH_BONES)
    c.set_forced_lod(1)
    c.set_anim_instance_class(U.RagequitHeroRetarget)
    slots=list(mesh.get_editor_property('materials'))
    normal_names={
        'Terra': [('shield','T_Terra_Shield_Demo_N'),('axe','T_Terra_Weapon_Demo_N'),('weapon','T_Terra_Weapon_Demo_N'),
                  ('shoulder','T_Terra_ShoulderKnee_Demo_N'),('knee','T_Terra_ShoulderKnee_Demo_N'),
                  ('head','T_Terra_Head_N'),('helmet','T_Terra_Helmet_Demo_N'),('cloth','T_Terra_Cloth_Demo_N'),
                  ('leg','T_Terra_Legs_N'),('body','T_Terra_Body_Demo_N')],
        'Gideon':[('head','T_LP_Rift_Head_N'),('ring','T_Gideon_OuterRing_Normals'),('leg','T_Gideon_Legs_normals'),
                  ('body','T_Gideon_Upperbody_Normal')]}
    for i in range(c.get_num_materials()):
        slot=slots[i]
        source=str(slot.material_slot_name)+' '+str(slot.material_interface.get_name() if slot.material_interface else '')
        normal_name=next((n for key,n in normal_names[hero_name] if key in source.lower()),None)
        texture=U.load_asset('/Game/Paragon%s/Characters/Heroes/%s/Textures/%s'%(hero_name,hero_name,normal_name)) if normal_name else None
        mi=U.AssetToolsHelpers.get_asset_tools().create_asset('MI_%s_%d'%(cls,i),'/Game/__RQIntroMemoryOnly',U.MaterialInstanceConstant,U.MaterialInstanceConstantFactoryNew())
        MEL.set_material_instance_parent(mi,S['stone'])
        if texture:
            MEL.set_material_instance_texture_parameter_value(mi,'DetailNormal',texture)
        c.set_material(i,mi)
        S['keep'].append(mi)
    idle=U.load_asset('/Game/Paragon{0}/Characters/Heroes/{0}/Animations/Idle'.format(hero_name))
    S[cls] = {'actor': a, 'body': c, 'hero': hero_name, 'pos': p, 'anim': None,'loadout':lo,'idle':idle}
    pose(cls, clip_name, at)
    R['sources'][cls] = {'mesh': mesh.get_path_name(), 'scale': k, 'loadout': lo.get_path_name()}


def pose(cls, clip_name, at):
    h = S[cls]
    path = '/Game/Paragon{0}/Characters/Heroes/{0}/Animations/{1}'.format(h['hero'], clip_name)
    if h['anim'] != path:
        clip = U.load_asset(path)
        if not isinstance(clip, U.AnimSequence):
            raise RuntimeError('Missing animation sequence: ' + path)
        if clip.get_editor_property('additive_anim_type') != U.AdditiveAnimationType.AAT_NONE:
            raise RuntimeError('Held cinematic pose requires a full-body clip: ' + path)
        h['anim'] = path
        h['clip'] = clip
        R['sources'].setdefault('animations', {})[path] = float(clip.get_play_length())
    inst=h['body'].get_anim_instance()
    if not isinstance(inst,U.RagequitHeroRetarget):
        raise RuntimeError('Native held-pose animator unavailable')
    inst.hold_emote(h['loadout'],h['clip'],min(at,h['clip'].get_play_length()-.001),h['idle'],.4)


def light(cls, p, aim, intensity, color, size=180):
    a = spawn(cls, p, rot_at(p, aim))
    c = a.get_component_by_class(U.LightComponent)
    c.set_mobility(U.ComponentMobility.MOVABLE)
    c.set_intensity(intensity)
    c.set_light_color(U.LinearColor(*color, 1.))
    if cls == U.RectLight:
        c.set_editor_property('source_width', float(size))
        c.set_editor_property('source_height', float(size))
        c.set_attenuation_radius(2200.)
    return a


def setup():
    U.EditorLoadingAndSavingUtils.new_blank_map(False)
    world = U.get_editor_subsystem(U.UnrealEditorSubsystem).get_editor_world()
    for cmd in ('r.HighResScreenshotDelay 8', 'r.AntiAliasingMethod 2', 'r.ScreenPercentage 100',
                'r.SSR.Quality 2', 'r.MotionBlurQuality 0', 'r.EyeAdaptationQuality 0',
                'r.Tonemapper.Sharpen 0.4', 'r.Streaming.PoolSize 2500', 'r.Nanite 1'):
        U.SystemLibrary.execute_console_command(world, cmd)
    S['stone'] = material('M_Ivory', (.46,.405,.32), .03, .72)
    S['basalt'] = material('M_Basalt', (.014,.011,.014), .22, .5)
    S['garnet'] = material('M_Garnet', (.12,.005,.013), .58, .32)
    S['void'] = material('M_Void', (.035,.008,.055), .5, .28, .3)
    S['shine'] = material('M_Impact', (.46,.24,.13), .15, .4, 2.8)
    # Broad seamless dark stage. The real heroes supply every character shape.
    # A black void removes the horizon and keeps attention on the sculpture.
    hero('sentinel', 'LO_Guardian_Sentinel', 'Terra', (-145,0,0), 0, 'RMB_intro', .38)
    hero('voidseer', 'LO_Mage_Voidseer', 'Gideon', (210,10,0), 180, 'Primary_Attack_A_Medium', .22)
    S['cam'] = spawn(U.CineCameraActor, (-300,-420,150))
    cc = S['cam'].get_cine_camera_component()
    cc.set_editor_property('current_aperture', 5.6)
    pp = spawn(U.PostProcessVolume, (0,0,0))
    pp.set_editor_property('unbound', True)
    st = pp.get_editor_property('settings')
    for prop, value in (('auto_exposure_method', U.AutoExposureMethod.AEM_MANUAL),
                        ('auto_exposure_bias', -.5), ('bloom_intensity', .12),
                        ('vignette_intensity', .24), ('motion_blur_amount', 0.)):
        st.set_editor_property('override_'+prop, True)
        st.set_editor_property(prop, value)
    pp.set_editor_property('settings', st)
    # Lux-based directional key/fill is stable under manual zero EV exposure.
    light(U.DirectionalLight, (-250,400,400), (0,0,90), 3.0, (1.,.91,.78))
    light(U.DirectionalLight, (300,-400,350), (0,0,100), 2.2, (.82,.83,.87))
    light(U.DirectionalLight, (300,300,180), (0,0,140), .7, (.90,.86,.83))
    S['shards'] = []
    random.seed(930)
    # Suspended physical debris, distinct from any in-game time-stop ability.
    for i in range(24):
        p = (-85+random.uniform(-65,60), random.uniform(-58,65), 105+random.uniform(-45,90))
        k = random.uniform(.009,.035)
        a = mesh_actor('/Game/Rock_Collection_04/Meshes/Rock_03/StaticMeshes/SM_Rock_03', p, (k,k*.4,k*1.6), S['stone'] if i%4 else S['garnet'],
                       U.Rotator(pitch=random.uniform(0,180), yaw=random.uniform(0,180), roll=random.uniform(0,180)))
        S['shards'].append((a,p,k))
    S['energy'] = []
    for i in range(3):
        p = (-65+i*15,6,123)
        a = mesh_actor('/Game/ParagonGideon/FX/Meshes/Shapes/SM_Burden_Projectile_Wisps', p, (.28,.28,.28), S['void'],
                       U.Rotator(pitch=i*21, yaw=180, roll=i*60))
        S['energy'].append(a)
    S['impact'] = light(U.PointLight, (-75,-10,125), (0,0,0), .12, (.63,.30,.16))
    # Keep a complete provenance record, but never save the world/materials.
    R['method'] = 'Native Unreal 3D; real skeletal meshes, evaluated native animation, physical camera transforms; no image-to-video'
    R['licensing'] = 'Paragon source remains inside Unreal; only rendered film is delivered. See CREDITI-UNREAL.md.'
    write()


def action(cls, name, fraction):
    h=S[cls]
    path='/Game/Paragon{0}/Characters/Heroes/{0}/Animations/{1}'.format(h['hero'],name)
    clip=U.load_asset(path)
    if not clip:
        raise RuntimeError('Missing cinematic action: '+path)
    pose(cls,name,max(0.,min(.999,fraction))*clip.get_play_length())


def frame(n):
    t=n/FPS
    # Six frames of suspension INSIDE an already moving action. The rejected
    # v1 held the bodies still for 6.5 seconds; that structure is removed.
    u=t if t<1.1 else 1.1 if t<1.35 else t-.25
    sa,va=S['sentinel']['actor'],S['voidseer']['actor']
    sx=-145 if u<1.5 else -145+185*ease((u-1.5)/.9)
    if u>=4.4:
        sx=40+125*ease((u-4.4)/1.1)
    if u>=6.6:
        sx=165-70*ease((u-6.95)/.45)
    if u>=7.4:
        sx=95+80*ease((u-7.4)/1.1)
    vx=210 if u<2.85 else 315
    vy=0 if u<2.85 else 75
    if u>=5.85:
        vx+=35*ease((u-5.85)/.5)
    sa.set_actor_location(vec(sx,0,0),False,True)
    va.set_actor_location(vec(vx,vy,0),False,True)
    syaw=math.degrees(math.atan2(vy,vx-sx))
    sa.set_actor_rotation(U.Rotator(pitch=0,yaw=syaw-90,roll=0),True)
    va.set_actor_rotation(U.Rotator(pitch=0,yaw=syaw+90,roll=0),True)
    if u<1.1:
        action('sentinel','RMB_intro',u/1.1)
        action('voidseer','Primary_Attack_A_Medium',u/1.1)
    elif u<1.5:
        action('sentinel','RMB_HitReact',(u-1.1)/.4)
        action('voidseer','Primary_Attack_B_Medium',(u-1.1)/.4)
    elif u<2.4:
        action('sentinel','RMB_melee',(u-1.5)/.9)
        action('voidseer','Torn_Space_intro',(u-1.5)/.9)
    elif u<3.4:
        action('sentinel','Primary_Melee_B_slow',(u-2.4))
        action('voidseer','Torn_Space_Outro',(u-2.4))
    elif u<4.4:
        action('sentinel','RMB_intro',(u-3.4))
        action('voidseer','Primary_Attack_B_Medium',(u-3.4))
    elif u<5.5:
        action('sentinel','RMB_melee',(u-4.4)/1.1)
        action('voidseer','Primary_Attack_C_Medium',(u-4.4)/1.1)
    elif u<6.6:
        action('sentinel','Primary_Melee_C_slow',(u-5.5)/1.1)
        if u<5.85:
            action('voidseer','Idle',(u-5.5)/.35)
        else:
            action('voidseer','Stun_Start',(u-5.85)/.75)
    elif u<7.4:
        if u<6.95:
            action('sentinel','RMB_intro',(u-6.6)/.6)
        else:
            action('sentinel','Knockback_back',(u-6.95)/.45)
        action('voidseer','Cosmic_Rift',(u-6.6)/.8)
    elif u<8.55:
        action('sentinel','Primary_Melee_D_slow',(u-7.4)/1.15)
        action('voidseer','Torn_Space',(u-7.4)/1.15)
    else:
        action('sentinel','Primary_Melee_B_slow',(u-8.55)/1.2)
        action('voidseer','Primary_Attack_A_Medium',(u-8.55)/1.2)
    hand=S['sentinel']['body'].get_socket_location('hand_l')
    contact=(hand.x+24,hand.y,hand.z+8)
    cast=S['voidseer']['body'].get_socket_location('hand_r')
    start=(cast.x-28,cast.y,cast.z)
    flight=(.5<=u<=1.1) or (3.8<=u<=4.15) or (9.1<=u<=9.55)
    launch=.5 if u<2 else 3.8 if u<6 else 9.1
    travel=.6 if u<2 else .35 if u<6 else .45
    for i,a in enumerate(S['energy']):
        a.set_is_temporarily_hidden_in_editor(not flight)
        p=lerp(start,contact,max(0.,min(1.,(u-launch)/travel-i*.065)))
        a.set_actor_location(vec(*p),False,True)
        a.set_actor_scale3d(vec(.13,.13,.13))
    impact_time=1.1 if u<3 else 4.15 if u<7 else 9.55
    d=u-impact_time
    debris=0<=d<.55
    for i,(a,p,k) in enumerate(S['shards']):
        a.set_is_temporarily_hidden_in_editor(not debris)
        a.set_actor_location(vec(contact[0]+(i%5-2)*12*d,contact[1]+(i%7-3)*20*d,
                                  contact[2]+(i%6-1)*35*d-90*d*d),False,True)
    S['impact'].set_is_temporarily_hidden_in_editor(not (0<=d<.18))
    S['impact'].set_actor_location(vec(*contact),False,True)
    # Edit on actions and reactions: bodies carry every shot, with no static
    # introductory portraits. Cameras keep both sides of a contact readable.
    if t<1.0:
        f=ease(t)
        p=lerp((32,790,160),(12,750,155),f)
        aim=(32,0,112);focal=36.
    elif t<1.75:
        p=(sx+120,340,175);aim=(sx+10,0,150);focal=42.
    elif t<3.65:
        f=ease((t-1.75)/1.9)
        p=lerp((-30,720,168),(115,710,163),f)
        aim=((sx+vx)/2,vy/2,115);focal=36.
    elif t<4.65:
        p=(vx-190,vy+430,143);aim=(vx-20,vy,133);focal=44.
    elif t<6.85:
        p=(145,790,165);aim=((sx+vx)/2,vy/2,115);focal=38.
    elif t<7.65:
        p=(sx+70,430,150);aim=(sx,0,125);focal=40.
    else:
        f=ease((t-7.65)/2.35)
        p=lerp((200,810,175),(245,735,162),f)
        aim=((sx+vx)/2,vy/2,118);focal=37.
    cam=S['cam']
    cam.set_actor_location_and_rotation(vec(*p),rot_at(p,aim),False,True)
    cc=cam.get_cine_camera_component()
    cc.set_editor_property('current_focal_length',focal)
    fs=cc.get_editor_property('focus_settings')
    fs.set_editor_property('focus_method',U.CameraFocusMethod.MANUAL)
    fs.set_editor_property('manual_focus_distance',math.dist(p,aim))
    cc.set_editor_property('focus_settings',fs)
    sample={'frame':n,'time':t,'action_time':u}
    for cls in ('sentinel','voidseer'):
        root=S[cls]['actor'].get_actor_location()
        q=S[cls]['body'].get_socket_location('hand_r')
        sample[cls]=[q.x-root.x,q.y-root.y,q.z-root.z]
    R['pose_samples'].append(sample)


def write():
    (OUT/'report.json').write_text(json.dumps(R,indent=2),encoding='utf-8')


def finish(error=None):
    if S['done']:
        return
    S['done']=True
    if error:
        R['errors'].append(error)
    R['success']=not R['errors'] and len(R['frames'])==len(INDICES)
    samples=R['pose_samples']
    changed=sum(any(math.dist(a[c],b[c])>.1 for c in ('sentinel','voidseer')) for a,b in zip(samples,samples[1:]))
    R['body_animation']={'changing_body_frames':changed,'transitions':max(0,len(samples)-1),
                         'pause_seconds':.25,'measurement':'right-hand positions relative to actor roots; camera excluded'}
    if MODE=='final' and changed<180:
        R['errors'].append('Body animation did not change on enough frames: '+str(changed))
        R['success']=False
    write()
    U.unregister_slate_post_tick_callback(S['handle'])
    U.EditorPythonScripting.set_keep_python_script_alive(False)
    U.SystemLibrary.quit_editor()


def tick(dt):
    if S['busy'] or S['done']:
        return
    S['busy']=True
    try:
        if time.monotonic()-S['started']>6600:
            raise RuntimeError('Render timeout')
        if S['phase']=='setup':
            setup()
            S['phase']='warm';S['ticks']=0
        elif S['phase']=='warm':
            S['ticks']+=1
            if S['ticks']<180 or U.RagequitCombatAssets.get_remaining_shader_jobs()>0:
                return
            hand=S['sentinel']['body'].get_socket_location('hand_l')
            contact=(hand.x+24,hand.y,hand.z+8)
            shift=tuple(contact[i]-(-75,6,123)[i] for i in range(3))
            S['contact_shift']=shift
            R['contact']={'hand_l':[hand.x,hand.y,hand.z],'impact':contact}
            for cls in ('sentinel','voidseer'):
                h=S[cls]['body'].get_socket_location('head')
                R['sources'][cls]['head_world']=[h.x,h.y,h.z]
            for i,(a,p,k) in enumerate(S['shards']):
                S['shards'][i]=(a,tuple(p[j]+shift[j] for j in range(3)),k)
            for i,a in enumerate(S['energy']):
                a.set_actor_location(vec(contact[0]+i*12,contact[1]+i*3,contact[2]+i*2),False,True)
            S['impact'].set_actor_location(vec(*contact),False,True)
            S['phase']='pose'
        elif S['phase']=='pose':
            if S['i']==len(INDICES):
                if MODE=='layout' and not S.get('reviewed'):
                    R['success']=True
                    R['awaiting_visual_review']=True
                    write()
                    S['phase']='review';S['review_started']=time.monotonic()
                    U.log('RQ_INTRO_LAYOUT_READY: create render-final.request in output directory to render film')
                    return
                finish();return
            frame(INDICES[S['i']])
            S['ticks']=0;S['phase']='settle'
        elif S['phase']=='settle':
            S['ticks']+=1
            if S['ticks']<4:
                return
            f=FRAMES/('frame_%04d.png'%INDICES[S['i']])
            S['file']=f
            S['task']=U.AutomationLibrary.take_high_res_screenshot(1920,1080,str(f),S['cam'],False)
            S['phase']='capture'
        elif S['phase']=='capture':
            if not S['task'].is_task_done() or not S['file'].exists():
                return
            R['frames'].append({'frame':INDICES[S['i']],'file':str(S['file'])})
            S['i']+=1
            if S['i']%12==0 or MODE=='layout':
                write();U.log('RQ_INTRO_FRAME %d/%d'%(S['i'],len(INDICES)))
            S['phase']='pose'
        elif S['phase']=='review':
            if (OUT/'render-final.request').exists():
                INDICES[:]=list(range(240))
                S['i']=0;S['reviewed']=True;S['phase']='pose'
                R['frames']=[];R['success']=False;R['mode']='final'
                R['awaiting_visual_review']=False
                write()
            elif time.monotonic()-S['review_started']>300:
                finish()
    except Exception:
        finish(traceback.format_exc())
    finally:
        S['busy']=False


U.EditorPythonScripting.set_keep_python_script_alive(True)
S['handle']=U.register_slate_post_tick_callback(tick)
