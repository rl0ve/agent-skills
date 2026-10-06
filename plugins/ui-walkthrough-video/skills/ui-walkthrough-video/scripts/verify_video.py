#!/usr/bin/env python3
"""Decode, measure and export review frames; never substitutes for watching/listening."""
import argparse
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import render as media


def review_times(duration, fps, timeline=None):
    step = 1/fps
    times = {0, max(0, duration-step)}
    if timeline:
        for scene in timeline.get('scenes', timeline.get('beats', [])):
            a, b = scene['start'], scene['start']+scene['duration']
            times.update((max(0,a-step), a, min(duration-step,a+step), (a+b)/2, min(duration-step,b-step)))
            for key in scene.get('cameraTransforms', []):
                times.add(a+key['time'])
    # Sample long idle intervals as well as planned transitions.
    times.update(range(5, math.ceil(duration), 5))
    return sorted(t for t in times if math.isfinite(t) and 0 <= t < duration)


def verify(video, out, timeline=None):
    video = Path(video).resolve()
    if Path(out).exists():
        raise ValueError('Review output exists; use a new directory')
    probe = media.probe(video)
    stream = next(s for s in probe['streams'] if s['codec_type']=='video')
    numerator, denominator = stream['avg_frame_rate'].split('/')
    fps = float(numerator)/float(denominator)
    duration = media.duration(video)
    if fps <= 0 or not math.isfinite(fps):
        raise ValueError('Invalid measured frame rate')
    plan = json.loads(Path(timeline).read_text()) if timeline else None
    media.run([media.FFMPEG,'-v','error','-i',video,'-enc_time_base','demux','-fps_mode','passthrough','-f','null','-'])
    has_audio = any(s['codec_type']=='audio' for s in probe['streams'])
    cmd = [media.FFMPEG,'-hide_banner','-i',str(video),'-vf','blackdetect=d=0.2:pix_th=0.1,freezedetect=n=-60dB:d=1.5']
    if has_audio:
        cmd += ['-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json']
    cmd += ['-f','null','-']
    env = {k:v for k,v in media.os.environ.items() if k not in ('OPENAI_API_KEY','ELEVENLABS_API_KEY','GEMINI_API_KEY','GOOGLE_API_KEY','OPENROUTER_API_KEY','MINIMAX_API_KEY')}
    result = subprocess.run(cmd, capture_output=True, check=True, env=env, text=True)
    intervals = [line.strip() for line in result.stderr.splitlines() if 'black_start:' in line or 'lavfi.freezedetect.' in line]
    loudness = None
    if has_audio:
        matches = re.findall(r'\{\s*"input_i".*?\}', result.stderr, re.DOTALL)
        if not matches:
            raise ValueError('Audio loudness measurement missing')
        loudness = json.loads(matches[-1])
    warnings = []
    if intervals:
        warnings.append('Inspect detected black/frozen intervals; static UI holds may be intentional')
    if plan and abs(plan.get('duration',plan.get('expectedDuration',duration))-duration) > .1:
        warnings.append('Final duration differs from plan by over 0.1s')
    if loudness:
        peak = float(loudness['input_tp'])
        if peak > -1:
            warnings.append('True peak exceeds -1 dBTP; reduce/limit and remeasure')
        if not math.isfinite(float(loudness['input_i'])):
            warnings.append('Audio is silent or unmeasurable; verify whether silence was intended')
    out = media.fresh(out)
    samples = []
    for index, time in enumerate(review_times(duration, fps, plan)):
        name = f'{index:03}-at-{time:.3f}.png'
        media.run([media.FFMPEG,'-v','error','-ss',f'{time:.6f}','-i',video,'-frames:v','1',out/name])
        if not (out/name).is_file():
            raise ValueError('Review frame was not decoded')
        samples.append({'time':time,'file':name})
    report = {'decode':'passed','dimensions':[stream['width'],stream['height']], 'fps':fps, 'duration':duration,
              'audioPresent':has_audio,'loudness':loudness,'detectedIntervals':intervals,'warnings':warnings,'frames':samples,
              'visualReview':'pending; inspect frames and motion in playback', 'listeningReview':'pending' if has_audio else 'silent technical output'}
    (out/'review.json').write_text(json.dumps(report,indent=2))
    return report


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video'); parser.add_argument('out'); parser.add_argument('--timeline')
    args=parser.parse_args()
    try:
        verify(args.video,args.out,args.timeline)
        print(str(Path(args.out).resolve()/'review.json'))
    except (ValueError,OSError,KeyError,StopIteration,ZeroDivisionError,subprocess.CalledProcessError) as error:
        print(str(error),file=sys.stderr);sys.exit(1)
