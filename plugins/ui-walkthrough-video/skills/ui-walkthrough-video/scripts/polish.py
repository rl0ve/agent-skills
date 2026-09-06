#!/usr/bin/env python3
"""Compose real capture with eased camera framing, a presentation canvas and captions.

Requires Pillow and FFmpeg. Source coordinates remain in capture pixels. This is
explicit keyframed editing, not automatic semantic/word alignment.
"""
import argparse
import json
import math
import os
import re
from pathlib import Path
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import render as media

FPS=30
CANVAS=(1600,1000)
CARD=(144,88,1312,820)
SAFE_ENV={k:v for k,v in os.environ.items() if k not in ('OPENAI_API_KEY','GEMINI_API_KEY','GOOGLE_API_KEY','OPENROUTER_API_KEY','ELEVENLABS_API_KEY')}

def ease(u):
    u=max(0,min(1,u))
    return u*u*u*(u*(u*6-15)+10)

def camera_at(keys,time,width,height):
    if time<=keys[0]['time']:state=keys[0]
    elif time>=keys[-1]['time']:state=keys[-1]
    else:
        a,b=next((a,b) for a,b in zip(keys,keys[1:]) if a['time']<=time<=b['time'])
        u=ease((time-a['time'])/(b['time']-a['time']))
        state={k:a[k]+(b[k]-a[k])*u for k in ('zoom','cx','cy')}
    cw,ch=width/state['zoom'],height/state['zoom']
    x=max(0,min(width-cw,state['cx']-cw/2))
    y=max(0,min(height-ch,state['cy']-ch/2))
    return x,y,cw,ch

def validate_camera(keys,width,height,duration):
    if not keys or keys[0]['time']!=0:raise ValueError('Camera must begin at time 0')
    previous=-1
    for k in keys:
        if not all(math.isfinite(k[x]) for x in ('time','zoom','cx','cy')):raise ValueError('Camera values must be finite')
        if not previous<k['time']<=duration:raise ValueError('Camera times must increase within the beat')
        if not 1<=k['zoom']<=2:raise ValueError('Camera zoom must stay between 1 and 2')
        if not 0<=k['cx']<=width or not 0<=k['cy']<=height:raise ValueError('Camera focus outside source')
        previous=k['time']

def marker_end(video):
    pixels=media.run([media.FFMPEG,'-v','error','-i',video,'-t','15','-vf',f'fps={FPS},crop=12:12:0:0,scale=1:1,format=rgb24','-f','rawvideo','-'])
    flags=[r>180 and g<90 and b>160 for r,g,b in zip(pixels[::3],pixels[1::3],pixels[2::3])]
    for i in range(len(flags)-3):
        if not flags[i] or not flags[i+1]:continue
        end=i+2
        while end<len(flags) and flags[end]:end+=1
        if end+1<len(flags) and not flags[end] and not flags[end+1]:return end
    raise ValueError('Capture sync marker not found with two following clean frames; do not guess timing')


def caption_lines(text,font,max_width):
    draw=ImageDraw.Draw(Image.new('RGB',(1,1)))
    if draw.textlength(text,font=font)<=max_width:return [text]
    sentences=re.split(r'(?<=[.!?])\s+',text.strip())
    if len(sentences)==2 and all(draw.textlength(x,font=font)<=max_width for x in sentences):return sentences
    words=text.split();choices=[]
    for split in range(1,len(words)):
        a,b=' '.join(words[:split]),' '.join(words[split:])
        wa,wb=draw.textlength(a,font=font),draw.textlength(b,font=font)
        if max(wa,wb)<=max_width:choices.append((abs(wa-wb),a,b))
    if not choices:raise ValueError('Caption exceeds two lines; supply shorter timed captions')
    _,a,b=min(choices)
    return [a,b]


def canvas_assets(font_path):
    font=ImageFont.truetype(str(font_path),28)
    small=ImageFont.truetype(str(font_path),22)
    image=Image.new('RGB',CANVAS)
    draw=ImageDraw.Draw(image)
    for y in range(CANVAS[1]):
        u=y/CANVAS[1];draw.line((0,y,CANVAS[0],y),fill=(int(17-6*u),int(32-9*u),int(44-10*u)))
    x,y,w,h=CARD
    shadow=Image.new('RGBA',CANVAS);d=ImageDraw.Draw(shadow)
    d.rounded_rectangle((x-2,y+9,x+w+2,y+h+13),radius=18,fill=(0,0,0,130))
    image=Image.alpha_composite(image.convert('RGBA'),shadow.filter(ImageFilter.GaussianBlur(22))).convert('RGB')
    mask=Image.new('L',(w,h));ImageDraw.Draw(mask).rounded_rectangle((0,0,w-1,h-1),radius=14,fill=255)
    return image,mask,font,small

def read_frame(pipe,n):
    chunks=[];total=0
    while total<n:
        chunk=pipe.read(n-total)
        if not chunk:return None
        chunks.append(chunk);total+=len(chunk)
    return b''.join(chunks)

def build(args):
    manifest=Path(args.manifest).resolve();spec=json.loads(manifest.read_text())
    if spec.get('mode')!='polished-capture':raise ValueError('Expected capture-polished manifest')
    width,height=spec['width'],spec['height']
    ratio=spec.get('pixelRatio',1);raw_width,raw_height=width*ratio,height*ratio
    if ratio not in (1,2):raise ValueError('Unsupported pixelRatio')
    if width/height!=CARD[2]/CARD[3]:raise ValueError('This canvas expects a 16:10 capture; supply 1440x900')
    audio=Path(args.audio).resolve();out=Path(args.out).resolve()
    if out.exists():raise ValueError('Output exists; use a new take')
    font_path=Path(args.font)
    if not font_path.is_file():raise ValueError('Supply an existing TTF font with --font')
    prepared=[]
    for b in spec['beats']:
        source=(manifest.parent/b['video']).resolve();wav=audio/(b['id']+'.wav')
        stream=next(x for x in media.probe(source)['streams'] if x['codec_type']=='video')
        if (stream['width'],stream['height'])!=(raw_width,raw_height):raise ValueError('Capture dimensions differ from declared pixelRatio')
        adur=media.duration(wav);duration=b['duration'];offset=b.get('audioOffset',.5)
        if duration<adur+offset:raise ValueError('Beat would truncate narration; extend capture duration')
        frames=round(duration*FPS);duration=frames/FPS
        keys=b['camera'];validate_camera(keys,width,height,duration)
        start_frame=marker_end(source)
        if media.duration(source)+.05<start_frame/FPS+duration:raise ValueError('Capture shorter than planned visible beat')
        captions=b.get('captions') or [{'start':offset,'end':offset+adur,'text':b['narration']}]
        end=-1
        for cue in captions:
            if not end<=cue['start']<cue['end']<=duration:raise ValueError('Caption intervals overlap or exceed the beat')
            end=cue['end']
        for e in b['events']:
            for name in ('time','start','end'):
                if name in e and not 0<=e[name]<=duration:
                    raise ValueError('Action telemetry falls outside the visible beat')
            if e['type']=='pointer':
                x,y,cw,ch=camera_at(keys,e['end'],width,height);p=e['to']
                if not x<=p['x']<=x+cw or not y<=p['y']<=y+ch:raise ValueError('Camera hides a pointer destination')
            if e['type']=='click':
                p,r=e['point'],e['bounds']
                if not r['x']<=p['x']<=r['x']+r['width'] or not r['y']<=p['y']<=r['y']+r['height']:raise ValueError('Click outside target bounds')
                x,y,cw,ch=camera_at(keys,e['time'],width,height)
                if not x<=p['x']<=x+cw or not y<=p['y']<=y+ch:raise ValueError('Camera hides the click target')
        prepared.append((b,source,wav,adur,frames,duration,start_frame,captions))
    out.mkdir(parents=True)
    base,mask,font,small=canvas_assets(font_path)
    timeline=[];cursor=0;srt=[];cue_id=1
    total=sum(x[5] for x in prepared)
    for index,(b,source,wav,adur,frames,duration,start_frame,captions) in enumerate(prepared):
        label=f'{index+1:02d} / {len(prepared):02d}    {b["title"]}'
        layers=[]
        for cue in captions:
            lines=caption_lines(cue['text'],font,CARD[2]-32)
            layer=Image.new('RGBA',CANVAS);draw=ImageDraw.Draw(layer)
            top=923 if len(lines)==2 else 940
            for n,line in enumerate(lines):draw.text((CANVAS[0]/2,top+n*34),line,font=font,fill='#f4f6f8',anchor='mt')
            layers.append((cue,layer))
        clip=out/f'{index:03}.mp4'
        decoder=subprocess.Popen([media.FFMPEG,'-v','error','-i',str(source),'-vf',f'fps={FPS},trim=start_frame={start_frame},setpts=PTS-STARTPTS','-frames:v',str(frames),'-pix_fmt','rgb24','-f','rawvideo','-'],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,env=SAFE_ENV)
        offset=b.get('audioOffset',.5)
        encoder=subprocess.Popen([media.FFMPEG,'-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{CANVAS[0]}x{CANVAS[1]}','-r',str(FPS),'-i','-',
            '-i',str(wav),'-map','0:v:0','-map','1:a:0','-af',f'adelay={round(offset*1000)}:all=1,apad',
            '-t',str(duration),'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-ar','48000','-ac','2',str(clip)],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL,env=SAFE_ENV)
        try:
            for frame in range(frames):
                data=read_frame(decoder.stdout,raw_width*raw_height*3)
                if data is None:raise ValueError('Raw video ended early; no frame padding was guessed')
                t=frame/FPS;x,y,cw,ch=camera_at(b['camera'],t,width,height)
                raw=Image.frombytes('RGB',(raw_width,raw_height),data)
                view=raw.transform((CARD[2],CARD[3]),Image.Transform.AFFINE,(cw*ratio/CARD[2],0,x*ratio,0,ch*ratio/CARD[3],y*ratio),resample=Image.Resampling.BICUBIC)
                result=base.copy();result.paste(view,(CARD[0],CARD[1]),mask)
                draw=ImageDraw.Draw(result)
                draw.text((CARD[0],35),'UI WALKTHROUGH' if args.brand is None else args.brand,font=small,fill='#b4c4d0')
                draw.text((CARD[0]+CARD[2],35),label,font=small,fill='#edf4f8',anchor='ra')
                for cue,layer in layers:
                    if cue['start']<=t<cue['end']:result.paste(layer,(0,0),layer)
                progress=(cursor+t)/total
                draw=ImageDraw.Draw(result);draw.rectangle((0,997,round(CANVAS[0]*progress),999),fill='#ee8a56')
                encoder.stdin.write(result.tobytes())
                if frame%150==0:print(f'{b["id"]}: frame {frame}/{frames}',flush=True)
        finally:
            decoder.stdout.close();encoder.stdin.close()
            dcode=decoder.wait();ecode=encoder.wait()
        if dcode or ecode:raise ValueError('Video decode/encode failed; inspect dependencies and input media')
        for cue in captions:
            srt.append(f'{cue_id}\n{media.tc(cursor+cue["start"])} --> {media.tc(cursor+cue["end"])}\n{cue["text"]}\n');cue_id+=1
        timeline.append({'id':b['id'],'start':cursor,'duration':duration,'sourceTrimFrames':start_frame,'syncToleranceSeconds':1/FPS,'audioOffset':offset,'audioDuration':adur,'camera':b['camera'],'events':b['events'],'captionTiming':'scene-level; not word aligned'})
        cursor+=duration
    (out/'concat.txt').write_text(''.join(f"file '{i:03}.mp4'\n" for i in range(len(prepared))))
    media.run([media.FFMPEG,'-v','error','-f','concat','-safe','1','-i',out/'concat.txt','-c','copy','-movflags','+faststart',out/'walkthrough.mp4'])
    media.run([media.FFMPEG,'-v','error','-i',out/'walkthrough.mp4','-map','0:v','-an','-c','copy','-movflags','+faststart',out/'silent.mp4'])
    (out/'captions.srt').write_text('\n'.join(srt))
    result={'mode':'polished-demo','voice':spec.get('voice'),'beats':timeline,'expectedDuration':cursor,'actualDuration':media.duration(out/'walkthrough.mp4'),'dimensions':list(CANVAS),'fps':FPS,'review':'Technical render; inspect actual frames and listen before accepting quality'}
    (out/'timeline.json').write_text(json.dumps(result,indent=2))
    media.run([media.FFMPEG,'-v','error','-i',out/'walkthrough.mp4','-f','null','-'])
    if abs(result['actualDuration']-cursor)>.1:raise ValueError('Final duration differs from plan')
    print(str(out/'walkthrough.mp4'))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest');parser.add_argument('audio');parser.add_argument('out')
    parser.add_argument('--font',default='/System/Library/Fonts/Supplemental/Arial.ttf')
    parser.add_argument('--brand',default=None)
    try:build(parser.parse_args())
    except (ValueError,OSError,subprocess.CalledProcessError) as e:print(str(e),file=sys.stderr);sys.exit(1)
