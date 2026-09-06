#!/usr/bin/env python3
"""Dependency-light narration and assembly. No keys in files or subprocess arguments."""
import argparse
import base64
import binascii
import wave
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
    env = {k:v for k,v in os.environ.items() if k not in ('OPENAI_API_KEY','ELEVENLABS_API_KEY','GEMINI_API_KEY','GOOGLE_API_KEY','OPENROUTER_API_KEY')}
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
    if provider == 'openrouter':
        if not re.fullmatch(r'[a-zA-Z0-9._:-]+/[a-zA-Z0-9._:-]+', voice['model']):
            raise ValueError('OpenRouter needs an explicit provider/model slug from its live speech catalog')
        payload = {'model':voice['model'], 'voice':voice['voice'], 'input':text,
                   'response_format':'pcm' if voice['model'].startswith('google/gemini-') else 'mp3'}
        if 'speed' in voice:
            payload['speed'] = voice['speed']
        if voice.get('instructions'):
            if not voice['model'].startswith('openai/'):
                raise ValueError('This adapter only maps OpenRouter delivery instructions for OpenAI; use documented provider options or a direct adapter for other models')
            payload['provider'] = {'options':{'openai':{'instructions':voice['instructions']}}}
        return 'https://openrouter.ai/api/v1/audio/speech', 'OPENROUTER_API_KEY', payload
    if provider == 'gemini':
        if not re.fullmatch(r'[a-zA-Z0-9._-]+', voice['model']):
            raise ValueError('Invalid Gemini model identifier')
        prompt = text
        if voice.get('instructions'):
            prompt = voice['instructions'] + '\nRead only the following transcript, without adding words:\n' + text
        payload = {'contents':[{'parts':[{'text':prompt}]}],
                   'generationConfig':{'responseModalities':['AUDIO'],
                     'speechConfig':{'voiceConfig':{'prebuiltVoiceConfig':{'voiceName':voice['voice']}}}}}
        return ('https://generativelanguage.googleapis.com/v1beta/models/' + voice['model'] + ':generateContent',
                'GEMINI_API_KEY', payload)
    raise ValueError('Unknown network provider')


def write_gemini_wav(response_data, source):
    # generateContent's documented output is PCM16 little-endian mono, 24 kHz.
    try:
        response = json.loads(response_data)
        candidates = response.get('candidates', [])
        candidate = candidates[0] if candidates else {}
        if candidate.get('finishReason') != 'STOP':
            raise ValueError('Gemini returned incomplete/blocked speech; no automatic retry')
        parts = candidate.get('content', {}).get('parts', [])
        clips = [p['inlineData'] for p in parts if p.get('inlineData',{}).get('mimeType','').startswith('audio/')]
        if len(clips) != 1:
            raise ValueError('Gemini returned no single audio payload; no automatic retry')
        clip = clips[0]
        mime = clip['mimeType']
        if not mime.startswith('audio/L16') or 'rate=24000' not in mime:
            raise ValueError('Unexpected Gemini audio format; verify current API docs before conversion')
        pcm = base64.b64decode(clip['data'], validate=True)
        if not pcm or len(pcm) % 2:
            raise ValueError('Gemini returned empty or invalid PCM audio')
    except (json.JSONDecodeError, KeyError, TypeError, AttributeError, binascii.Error):
        raise ValueError('Invalid Gemini response; provider payload not logged') from None
    with wave.open(str(source),'wb') as wav:
        wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(24000)
        wav.writeframes(pcm)


def voice_command(args):
    spec = load(args.manifest)
    voice = spec.get('voice')
    if not voice:
        raise ValueError('Choose and audition a voice provider first; there is no automatic speech fallback')
    provider = voice['provider']
    if provider not in ('local','openai','elevenlabs','gemini','openrouter','provided'):
        raise ValueError('Use gemini, openai, elevenlabs, openrouter, provided, or explicitly authorized local test audio')
    if provider == 'provided':
        raise ValueError('Put ID.wav files in an audio directory and use assemble directly')
    if provider == 'local' and not args.allow_local_test:
        raise ValueError('System speech is test-only and may sound robotic; use silent for technical tests or explicitly pass --allow-local-test')
    if provider == 'local' and not shutil.which('say'):
        raise ValueError('Local speech needs macOS say; supply WAV audio on other systems')
    if provider in ('openai','elevenlabs','gemini','openrouter'):
        if not args.allow_paid:
            raise ValueError('Paid voice requires prior budget/provider authorization and --allow-paid')
        _, env, _ = request_config(voice, spec['beats'][0]['narration'])
        if not os.environ.get(env):
            raise ValueError(f'Set {env} securely in the environment; never paste the key into chat')
    out = fresh(args.out)
    (out/'voice.json').write_text(json.dumps(voice,indent=2))
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
            header = {'openai':'Authorization','elevenlabs':'xi-api-key','gemini':'x-goog-api-key','openrouter':'Authorization'}[provider]
            headers[header] = 'Bearer '+key if provider in ('openai','openrouter') else key
            request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method='POST')
            router_pcm = provider == 'openrouter' and payload.get('response_format') == 'pcm'
            source = out / (b['id']+('.source.wav' if provider == 'gemini' or router_pcm else '.mp3'))
            try:
                with urllib.request.urlopen(request,timeout=120) as response:
                    response_data = response.read()
                    if provider == 'gemini':
                        write_gemini_wav(response_data,source)
                    elif router_pcm:
                        if response.headers.get_content_type().lower() not in ('audio/pcm','audio/l16','audio/x-pcm','application/octet-stream'):
                            raise ValueError('OpenRouter returned a non-PCM content type')
                        if not response_data or len(response_data) % 2:
                            raise ValueError('OpenRouter returned invalid PCM audio')
                        with wave.open(str(source),'wb') as wav:
                            wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(24000)
                            wav.writeframes(response_data)
                    else:
                        mime = response.headers.get_content_type().lower()
                        mp3 = response_data.startswith(b'ID3') or (len(response_data)>2 and response_data[0]==255 and response_data[1]&224==224)
                        if mime not in ('audio/mpeg','audio/mp3','application/octet-stream') or not mp3:
                            raise ValueError('Provider returned unexpected audio format; inspect usage before retrying')
                        source.write_bytes(response_data)
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


def silent(args):
    """Technical capture proof with no generated speech or audio track."""
    manifest = Path(args.manifest).resolve()
    spec = load(manifest)
    inputs = [(manifest.parent / b['video']).resolve() for b in spec['beats']]
    for video in inputs:
        duration(video)
        if not any(x['codec_type']=='video' for x in probe(video)['streams']):
            raise ValueError('Capture has no video stream')
    out = fresh(args.out)
    width,height,fps = spec.get('width',1440),spec.get('height',900),spec.get('fps',30)
    norm = f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=white,setsar=1,fps={fps}'
    for i,video in enumerate(inputs):
        run([FFMPEG,'-v','error','-i',video,'-map','0:v:0','-vf',norm,'-c:v','libx264',
             '-preset','fast','-crf','18','-pix_fmt','yuv420p','-an',out/f'{i:03}.mp4'])
    (out/'concat.txt').write_text(''.join(f"file '{i:03}.mp4'\n" for i in range(len(inputs))))
    run([FFMPEG,'-v','error','-f','concat','-safe','1','-i',out/'concat.txt','-c','copy',
         '-an','-movflags','+faststart',out/'silent.mp4'])
    if any(x['codec_type']=='audio' for x in probe(out/'silent.mp4')['streams']):
        raise ValueError('Silent proof unexpectedly has audio')
    (out/'review.json').write_text(json.dumps({'mode':'silent-technical-proof','duration':duration(out/'silent.mp4'),
        'quality':'Basic capture assembly; no narration audition or polished camera/cursor treatment'},indent=2))
    print(str(out/'silent.mp4'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command',required=True)
    v = sub.add_parser('voice')
    v.add_argument('manifest'); v.add_argument('out'); v.add_argument('--allow-paid',action='store_true')
    v.add_argument('--allow-local-test',action='store_true')
    a = sub.add_parser('assemble')
    a.add_argument('manifest'); a.add_argument('audio'); a.add_argument('out')
    t = sub.add_parser('silent')
    t.add_argument('manifest'); t.add_argument('out')
    args = parser.parse_args()
    try:
        {'voice':voice_command,'assemble':assemble,'silent':silent}[args.command](args)
    except subprocess.CalledProcessError as e:
        print(f'Media command failed ({e.returncode}); verify installed tools and input files',file=sys.stderr)
        sys.exit(1)
    except (ValueError,KeyError,OSError) as e:
        print(str(e),file=sys.stderr); sys.exit(1)

if __name__ == '__main__':
    main()
