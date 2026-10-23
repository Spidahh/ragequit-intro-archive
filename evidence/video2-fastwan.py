from pathlib import Path
import torch, json, gc, argparse
from diffusers import WanImageToVideoPipeline,AutoencoderKLWan,WanTransformer3DModel,FlowMatchEulerDiscreteScheduler
from diffusers.utils import load_image,export_to_video
from transformers import UMT5EncoderModel,AutoTokenizer

# Three-step flow DMD: official FastVideo dmd.py clean estimate and re-noising.
class DMDScheduler(FlowMatchEulerDiscreteScheduler):
 def set_timesteps(self,num_inference_steps=None,device=None,**kwargs):
  self.timesteps=torch.tensor([1000.,757.,522.],device=device)
  self.sigmas=torch.tensor([1.,.757,.522,0.],device=device)
  self._step_index=0; self._begin_index=None; self.num_inference_steps=3
 def step(self,model_output,timestep,sample,return_dict=False,**kwargs):
  i=self._step_index; sigma=self.sigmas[i]
  clean=sample-sigma*model_output
  nxt=self.sigmas[i+1]
  result=(1-nxt)*clean+nxt*torch.randn_like(clean) if i<2 else clean
  self._step_index+=1
  return (result,)

p=argparse.ArgumentParser();p.add_argument('--image',required=True);p.add_argument('--prompt',required=True);p.add_argument('--out',required=True);p.add_argument('--seed',type=int,default=311);args=p.parse_args()
model='FastVideo/FastWan2.2-TI2V-5B-FullAttn-Diffusers'
print('Loading components',flush=True)
vae=AutoencoderKLWan.from_pretrained(model,subfolder='vae',torch_dtype=torch.float32)
transformer=WanTransformer3DModel.from_pretrained(model,subfolder='transformer',torch_dtype=torch.bfloat16)
transformer.enable_layerwise_casting(storage_dtype=torch.float8_e4m3fn,compute_dtype=torch.bfloat16)
encoder=UMT5EncoderModel.from_pretrained(model,subfolder='text_encoder',torch_dtype=torch.bfloat16)
tokenizer=AutoTokenizer.from_pretrained(model,subfolder='tokenizer')
pipe=WanImageToVideoPipeline(tokenizer=tokenizer,text_encoder=encoder,vae=vae,transformer=transformer,scheduler=DMDScheduler(),expand_timesteps=True)
print('Encoding prompt on CPU',flush=True)
with torch.no_grad():
 embed,_=pipe.encode_prompt(prompt=Path(args.prompt).read_text(encoding='utf-8'),device=torch.device('cpu'),num_videos_per_prompt=1,do_classifier_free_guidance=False,max_sequence_length=128)
pipe.text_encoder=None;del encoder;gc.collect()
pipe.enable_model_cpu_offload();pipe.vae.enable_tiling()
print('Generating motion',flush=True)
torch.manual_seed(args.seed)
r=pipe(image=load_image(args.image),prompt_embeds=embed,height=384,width=672,num_frames=49,num_inference_steps=3,guidance_scale=1.0,generator=torch.Generator(device='cuda').manual_seed(args.seed),output_type='pil').frames[0]
export_to_video(r,args.out,fps=24)
print(json.dumps({'file':args.out,'frames':len(r)}),flush=True)
