import ctypes, datetime, hashlib, json, subprocess, sys, time
from pathlib import Path
ROOT=Path('E:/PROGETTI/ragequit')
sys.path.insert(0,str(ROOT/'.verify/window-capture-runtime'))
from windows_capture import WindowsCapture,Frame,InternalCaptureControl
RUN=ROOT/'.verify/ragequit-unreal'/('intro-window-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
RUN.mkdir(); (RUN/'frames').mkdir()
STAGE=ROOT/'unreal/Saved/ShippingBuilds/Windows'
EXE=STAGE/'RAGEQUIT/Binaries/Win64/Ragequit-Win64-Shipping.exe'
U=ctypes.windll.user32
INFO={'runtime_sha256':hashlib.sha256(EXE.read_bytes()).hexdigest(),'method':'Windows Graphics Capture, exact owned HWND, no desktop capture','frames':[]}
startup=subprocess.STARTUPINFO();startup.dwFlags|=subprocess.STARTF_USESHOWWINDOW;startup.wShowWindow=0
p=subprocess.Popen([str(EXE),'-windowed','-ResX=1280','-ResY=720','-culture=en','-UserDir='+str(RUN/'user')],cwd=STAGE,startupinfo=startup)
hwnd=None
callback_type=ctypes.WINFUNCTYPE(ctypes.c_bool,ctypes.c_void_p,ctypes.c_void_p)
def enum(h,l):
 global hwnd
 pid=ctypes.c_ulong(); U.GetWindowThreadProcessId(ctypes.c_void_p(h),ctypes.byref(pid))
 title=ctypes.create_unicode_buffer(512);U.GetWindowTextW(ctypes.c_void_p(h),title,512)
 if pid.value==p.pid and title.value.startswith('RAGEQUIT'): hwnd=h
 return True
try:
 deadline=time.monotonic()+30
 while hwnd is None and p.poll() is None and time.monotonic()<deadline:
  U.EnumWindows(callback_type(enum),0);time.sleep(.05)
 if hwnd is None: raise RuntimeError('Own game window not found')
 U.ShowWindow(ctypes.c_void_p(hwnd),4)
 capture=WindowsCapture(cursor_capture=False,draw_border=False,window_hwnd=hwnd,minimum_update_interval=33)
 started=time.monotonic();last=-1
 @capture.event
 def on_frame_arrived(frame:Frame,control:InternalCaptureControl):
  global last
  at=time.monotonic()-started
  if at-last>=.09:
   name='f%04d.jpg'%len(INFO['frames']);frame.save_as_image(str(RUN/'frames'/name))
   INFO['frames'].append({'file':name,'time':round(at,4),'size':[frame.width,frame.height]});last=at
  if at>=20: control.stop()
 @capture.event
 def on_closed(): INFO['window_closed']=True
 control=capture.start_free_threaded()
 while time.monotonic()-started<22 and p.poll() is None: time.sleep(.1)
 control.stop()
 INFO['success']=len(INFO['frames'])>30
except Exception as e:
 INFO['success']=False;INFO['error']=repr(e)
finally:
 if p.poll() is None: p.terminate();p.wait(timeout=10)
 (RUN/'report.json').write_text(json.dumps(INFO,indent=2),encoding='utf-8')
 print(json.dumps({'run':str(RUN),'success':INFO.get('success'),'frames':len(INFO['frames']),'error':INFO.get('error')}))
