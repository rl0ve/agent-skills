#!/usr/bin/env python3
"""Dependency-light narration and assembly. No keys in files or subprocess arguments."""
import argparse
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

FFMPEG = os.environ.get('FFMPEG', 'ffmpeg')
FFPROBE = os.environ.get('FFPROBE', 'ffprobe')


def run(args):
    env = {k:v for k,v in os.environ.items() if k not in ('OPENAI_API_KEY','ELEVENLABS_API_KEY')}
    return subprocess.run([str(a) for a in args], check=True, capture_output=True, env=env).stdout


def probe(file):
    return json.loads(run([FFPROBE, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', file]))


def duration(file):
    raw = probe(file).get('format', {}).get('duration')
    if raw is None or raw == 'N/A':
        raise ValueError(f'Empty or unmeasurable media: {Path(file).name}; check synthesis permissions or source media')
    n = float(raw)
    if not math.isfinite(n) or n <= 0:
        raise ValueError('Invalid media duration')
    return n


def load(file):
    spec = json.loads(Path(file).read_text())
    if spec.get('version') != 1 or not spec.get('beats'):
        raise ValueError('Expected manifest version 1 and nonempty beats')
    voice = spec.get('voice', {})
    allowed = {'provider','model','voice','quality','rate','instructions','speed','voice_settings'}
    if set(voice) - allowed:
        raise ValueError('Unknown voice field; credentials belong in environment variables')
    if set(voice.get('voice_settings', {})) - {'stability','similarity_boost','style','use_speaker_boost','speed'}:
        raise ValueError('Unknown voice_settings field')
    seen = set()
    for b in spec['beats']:
        if not re.fullmatch(r'[a-z0-9][a-z0-9_-]*', b['id']) or b['id'] in seen or not b['narration'].strip():
            raise ValueError('Invalid or duplicate beat')
        seen.add(b['id'])
    for key, default in [('width',1440),('height',900)]:
        n = spec.get(key, default)
        if type(n) is not int or n <= 0 or n % 2:
            raise ValueError('Dimensions must be positive even integers')
    fps = spec.get('fps',30)
    if type(fps) is not int or not 1 <= fps <= 60:
        raise ValueError('fps must be an integer from 1 to 60')
    return spec


def fresh(out):
    out = Path(out).resolve()
    if out.exists():
        raise ValueError('Output exists; choose a new take')
    out.mkdir(parents=True)
    return out


def request_config(voice, text):
    provider = voice['provider']
    if provider == 'openai':
        payload = {'model':voice['model'], 'voice':voice['voice'], 'input':text, 'response_format':'mp3'}
        if voice.get('instructions'):
            if voice['model'] in ('tts-1','tts-1-hd'):
                raise ValueError('This OpenAI model does not support instructions')
            payload['instructions'] = voice['instructions']
        if 'speed' in voice:
            payload['speed'] = voice['speed']
        return 'https://api.openai.com/v1/audio/speech', 'OPENAI_API_KEY', payload
    if provider == 'elevenlabs':
        payload = {'model_id':voice['model'], 'text':text}
        if 'voice_settings' in voice:
            payload['voice_settings'] = voice['voice_settings']
        return ('https://api.elevenlabs.io/v1/text-to-speech/' + urllib.parse.quote(voice['voice'],safe='') + '?output_format=mp3_44100_128',
                'ELEVENLABS_API_KEY', payload)
    raise ValueError('Unknown network provider')


def voice_command(args):
    spec = load(args.manifest)
    voice = spec.get('voice', {'provider':'local'})
    provider = voice['provider']
    if provider not in ('local','openai','elevenlabs','provided'):
        raise ValueError('Use local, openai, elevenlabs, or provided audio')
    if provider == 'provided':
        raise ValueError('Put ID.wav files in an audio directory and use assemble directly')
    if provider == 'local' and not shutil.which('say'):
        raise ValueError('Local speech needs macOS say; supply WAV audio on other systems')
    if provider in ('openai','elevenlabs'):
        if not args.allow_paid:
            raise ValueError('Paid voice requires prior budget/provider authorization and --allow-paid')
        _, env, _ = request_config(voice, spec['beats'][0]['narration'])
        if not os.environ.get(env):
            raise ValueError(f'Set {env} securely in the environment; never paste the key into chat')
    out = fresh(args.out)
    for b in spec['beats']:
        target = out / (b['id'] + '.wav')
        if provider == 'local':
            source = out / (b['id'] + '.aiff')
            textfile = out / (b['id'] + '.txt')
            textfile.write_text(b['narration'])
            cmd = ['say','-r',str(voice.get('rate',165)),'-f',textfile,'-o',source]
            if voice.get('voice'):
                cmd += ['-v',voice['voice']]
            run(cmd)
        else:
            url, env, payload = request_config(voice,b['narration'])
            key = os.environ[env]
            headers = {'Content-Type':'application/json'}
            headers['Authorization' if provider == 'openai' else 'xi-api-key'] = 'Bearer '+key if provider == 'openai' else key
            request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method='POST')
            source = out / (b['id']+'.mp3')
            try:
                with urllib.request.urlopen(request,timeout=120) as response:
                    source.write_bytes(response.read())
            except urllib.error.HTTPError as e:
                # Never print provider response bodies, headers, request objects or keys.
                raise ValueError(f'{b["id"]}: provider returned HTTP {e.code}; no automatic retry') from None
            except urllib.error.URLError:
                raise ValueError(f'{b["id"]}: network failed; check provider usage before retrying') from None
        run([FFMPEG,'-v','error','-i',source,'-ar','48000','-ac','2',target])
        print(f'{b["id"]}: {duration(target):.2f}s')
    (out/'voice.json').write_text(json.dumps(voice,indent=2))


def tc(seconds):
    ms = round(seconds*1000)
    h, ms = divmod(ms,3600000)
    m, ms = divmod(ms,60000)
    s, ms = divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def cues_for(beat, audio_duration):
    if 'cues' in beat:
        cues = beat['cues']
        end = 0
        for cue in cues:
            a, b = cue['start'], cue['end']
            if not (math.isfinite(a) and math.isfinite(b) and end <= a < b <= audio_duration + .01) or not cue['text'].strip():
                raise ValueError('Invalid/overlapping subtitle cues')
            end = b
        if not cues:
            raise ValueError('Explicit cues cannot be empty')
        return cues, 'supplied'
    words = beat['narration'].split()
    chunks, current = [], []
    for word in words:
        if current and len(' '.join(current+[word])) > 80:
            chunks.append(' '.join(current)); current=[]
        current.append(word)
    if current:
        chunks.append(' '.join(current))
    total = sum(len(c) for c in chunks)
    cursor, cues = 0, []
    for c in chunks:
        end = cursor + len(c)/total*audio_duration
        cues.append({'start':cursor,'end':end,'text':c})
        cursor = end
    return cues, 'estimated'


def assemble(args):
    manifest = Path(args.manifest).resolve()
    spec = load(manifest)
    audio = Path(args.audio).resolve()
    width,height,fps = spec.get('width',1440),spec.get('height',900),spec.get('fps',30)
    items = []
    # Validate all inputs and timing before writing any output.
    for b in spec['beats']:
        video = (manifest.parent / b['video']).resolve()
        wav = audio / (b['id']+'.wav')
        vdur, adur = duration(video), duration(wav)
        if not any(s['codec_type']=='video' for s in probe(video)['streams']):
            raise ValueError('Capture has no video stream')
        if not any(s['codec_type']=='audio' for s in probe(wav)['streams']):
            raise ValueError('Narration has no audio stream')
        cues, kind = cues_for(b,adur)
        items.append((b,video,wav,vdur,adur,cues,kind))
    out = fresh(args.out)
    timeline, srt, built, cursor, cue_id = [], [], [], 0, 1
    norm = f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps={fps}'
    for i,(b,video,wav,vdur,adur,cues,kind) in enumerate(items):
        length = math.ceil((max(vdur,adur)+.25)*fps)/fps
        clip = out/f'{i:03}.mp4'
        run([FFMPEG,'-v','error','-i',video,'-i',wav,'-map','0:v:0','-map','1:a:0',
             '-vf',norm+f',tpad=stop_mode=clone:stop_duration={length}',
             '-af',f'apad=pad_dur={length}', '-t',f'{length:.6f}',
             '-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',
             '-c:a','aac','-b:a','192k','-ar','48000','-ac','2',clip])
        encoded = duration(clip)
        warnings=[]
        if abs(vdur-adur)>2:
            warnings.append('Timing mismatch over 2s: inspect pacing or split/recapture beat')
        for cue in cues:
            srt.append(f'{cue_id}\n{tc(cursor+cue["start"])} --> {tc(cursor+cue["end"])}\n{cue["text"]}\n')
            cue_id += 1
        timeline.append({'id':b['id'],'start':cursor,'duration':encoded,'videoDuration':vdur,'audioDuration':adur,'captionTiming':kind,'warnings':warnings})
        cursor += encoded
        built.append(clip)
    # Relative generated numeric names avoid concat path quoting hazards.
    (out/'concat.txt').write_text(''.join(f"file '{p.name}'\n" for p in built))
    (out/'captions.srt').write_text('\n'.join(srt))
    base = out/'base.mp4'
    run([FFMPEG,'-v','error','-f','concat','-safe','1','-i',out/'concat.txt','-c','copy',base])
    run([FFMPEG,'-v','error','-i',base,'-i',out/'captions.srt','-map','0:v','-map','0:a','-map','1:0',
         '-c','copy','-c:s','mov_text','-movflags','+faststart',out/'walkthrough.mp4'])
    run([FFMPEG,'-v','error','-i',base,'-map','0:v','-c','copy','-an','-movflags','+faststart',out/'silent.mp4'])
    base.unlink()
    report = {'beats':timeline,'expectedDuration':cursor,'actualDuration':duration(out/'walkthrough.mp4'),
              'voice':spec.get('voice'), 'review':'Technical assembly only; inspect video and listen before delivery'}
    (out/'timeline.json').write_text(json.dumps(report,indent=2))
    run([FFMPEG,'-v','error','-i',out/'walkthrough.mp4','-f','null','-'])
    if abs(report['actualDuration']-cursor) > .5:
        raise ValueError('Final duration differs from planned timeline by over 0.5s')
    print(json.dumps(report,indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command',required=True)
    v = sub.add_parser('voice')
    v.add_argument('manifest'); v.add_argument('out'); v.add_argument('--allow-paid',action='store_true')
    a = sub.add_parser('assemble')
    a.add_argument('manifest'); a.add_argument('audio'); a.add_argument('out')
    args = parser.parse_args()
    try:
        (voice_command if args.command == 'voice' else assemble)(args)
    except subprocess.CalledProcessError as e:
        print(f'Media command failed ({e.returncode}); verify installed tools and input files',file=sys.stderr)
        sys.exit(1)
    except (ValueError,KeyError,OSError) as e:
        print(str(e),file=sys.stderr); sys.exit(1)

if __name__ == '__main__':
    main()
