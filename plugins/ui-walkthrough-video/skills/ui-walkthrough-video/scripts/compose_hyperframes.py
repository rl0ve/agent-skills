#!/usr/bin/env python3
"""Build an explicitly chosen HyperFrames project from measured footage and a storyboard.

No installation, generation, recording, rendering or publishing occurs here.
"""
import argparse
import html
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import render as media

ASSETS = Path(__file__).resolve().parent.parent / 'assets' / 'hyperframes'


def number(value, name, minimum=0):
    if type(value) not in (int, float) or not math.isfinite(value) or value < minimum:
        raise ValueError(f'{name} must be finite and >= {minimum}')
    return value


def rectangle(value, width, height):
    if not isinstance(value, list) or len(value) != 4:
        raise ValueError('Rectangles use [x, y, width, height] pixels')
    x, y, w, h = [number(v, 'rectangle') for v in value]
    if w <= 0 or h <= 0 or x + w > width or y + h > height:
        raise ValueError('Rectangle is empty or outside its canvas/source')
    return value


def prepare(storyboard):
    path = Path(storyboard).resolve()
    spec = json.loads(path.read_text())
    if spec.get('version') != 1 or spec.get('treatment') not in ('tutorial', 'demo', 'teaser') or not spec.get('scenes'):
        raise ValueError('Expected storyboard version 1, treatment and nonempty scenes')
    width, height = spec['width'], spec['height']
    if any(type(v) is not int or v <= 0 or v % 2 for v in (width, height)):
        raise ValueError('Canvas dimensions must be positive even integers')
    if spec.get('fps', 60) not in (24, 25, 30, 60):
        raise ValueError('Use 24, 25, 30 or 60 fps')
    total = number(spec['duration'], 'duration', .01)
    if 'bpm' in spec:
        number(spec['bpm'], 'bpm', 1)
    scenes, tracks, ids, cursor = [], [], set(), 0
    for index, scene in enumerate(spec['scenes']):
        sid = scene['id']
        if not re.fullmatch(r'[a-z][a-z0-9_-]*', sid) or sid in ids:
            raise ValueError('Scene IDs must be unique lowercase identifiers')
        ids.add(sid)
        start = number(scene['start'], 'scene start')
        length = number(scene['duration'], 'scene duration', .01)
        if abs(start - cursor) > .001 or start + length > total + .001:
            raise ValueError('Scenes must be contiguous, ordered and within the final duration')
        cursor = start + length
        rect = rectangle(scene['rect'], width, height)
        source = (path.parent / scene['video']).resolve()
        probe = media.probe(source)
        stream = next((s for s in probe['streams'] if s['codec_type'] == 'video'), None)
        if stream is None:
            raise ValueError('Scene source has no video stream')
        sw, sh = stream['width'], stream['height']
        trim = number(scene.get('sourceStart', 0), 'sourceStart')
        if trim + length > media.duration(source) + .02:
            raise ValueError('Scene would exceed real footage; extend capture or explicitly re-edit')
        title = scene['title']
        if not isinstance(title, str) or not title.strip():
            raise ValueError('Scene needs a title')
        title_rect = rectangle(scene['titleRect'], width, height)
        caption_rect = rectangle(scene['captionRect'], width, height)
        cameras = scene.get('camera', [{'time': 0, 'zoom': 1, 'cx': sw/2, 'cy': sh/2}])
        if not cameras:
            raise ValueError('Camera keys cannot be empty')
        previous = -1
        for camera in cameras:
            t = number(camera['time'], 'camera time')
            zoom = number(camera['zoom'], 'zoom', 1)
            if not previous < t <= length or zoom > 3 or (previous == -1 and t != 0):
                raise ValueError('Camera must start at 0, increase within the scene and use zoom 1..3')
            for key, limit in [('cx', sw), ('cy', sh)]:
                if number(camera[key], key) > limit:
                    raise ValueError('Camera focus is outside the source')
            previous = t
        # Fit real footage; framing is authored separately for each output aspect ratio.
        scale = min(rect[2]/sw, rect[3]/sh)
        transforms = []
        for camera in cameras:
            z = scale * camera['zoom']
            def axis(center, source_size, target_size):
                if source_size*z <= target_size:
                    return (target_size-source_size*z)/2
                return max(target_size-source_size*z, min(0, target_size/2-center*z))
            transforms.append({'time': camera['time'], 'scale': z,
                               'x': axis(camera['cx'], sw, rect[2]), 'y': axis(camera['cy'], sh, rect[3])})
        prepared = dict(scene, source=source, sourceSize=[sw, sh], sourceStart=trim,
                        cameraTransforms=transforms, captions=[], cueOverlays=[], captionTiming='none')
        words = None
        offset = number(scene.get('audioOffset', 0), 'audioOffset')
        if scene.get('audio'):
            audio = (path.parent / scene['audio']).resolve()
            adur = media.duration(audio)
            if not any(s['codec_type'] == 'audio' for s in media.probe(audio)['streams']):
                raise ValueError('Narration source has no audio stream')
            if offset + adur > length + .001:
                raise ValueError('Scene would truncate narration')
            tracks.append({'kind': 'voice', 'scene': sid, 'source': audio, 'start': start+offset, 'duration': adur, 'volume': 1})
            if scene.get('words'):
                words = media.load_words(path.parent / scene['words'], adur)
            if 'captions' in scene:
                captions, timing = media.cues_for({'cues': scene['captions']}, adur)
            elif words:
                captions, timing = media.cues_for({}, adur, words)
            else:
                # No silent proportional fallback in an authored composition.
                captions, timing = [], 'none; alignment or explicit cues required'
            prepared['captions'] = [dict(c, start=start+offset+c['start'], end=start+offset+c['end']) for c in captions]
            prepared['captionTiming'] = timing
        elif scene.get('words') or scene.get('captions') or scene.get('cueOverlays'):
            raise ValueError('Speech captions and word anchors require narration audio')
        for cue in scene.get('cueOverlays', []):
            if not words or type(cue['wordIndex']) is not int or not 0 <= cue['wordIndex'] < len(words['words']):
                raise ValueError('Cue overlay needs a valid aligned wordIndex')
            cue_start = start + offset + words['words'][cue['wordIndex']]['start']
            cue_length = number(cue['duration'], 'cue duration', .01)
            if cue_start + cue_length > start + length:
                raise ValueError('Cue extends beyond its scene')
            prepared['cueOverlays'].append(dict(cue, start=cue_start, rect=rectangle(cue['rect'], sw, sh)))
        scenes.append(prepared)
    if abs(cursor - total) > .001:
        raise ValueError('Final scene must end at the declared duration')
    for track in spec.get('audioTracks', []):
        if track.get('kind') not in ('music', 'sfx'):
            raise ValueError('Optional tracks must be music or sfx')
        start = number(track['start'], 'audio start')
        length = number(track['duration'], 'audio duration', .01)
        trim = number(track.get('sourceStart', 0), 'audio sourceStart')
        volume = number(track.get('volume', .1), 'audio volume')
        if start + length > total + .001 or volume > 1:
            raise ValueError('Optional audio exceeds timeline or gain 1')
        source = (path.parent / track['file']).resolve()
        if trim + length > media.duration(source) + .02 or not any(s['codec_type']=='audio' for s in media.probe(source)['streams']):
            raise ValueError('Optional audio has no adequate source audio')
        tracks.append(dict(track, source=source, start=start, duration=length, sourceStart=trim, volume=volume))
        if 'duckGain' in track:
            if track['kind'] != 'music' or number(track['duckGain'], 'duckGain') > 1:
                raise ValueError('duckGain must be 0..1 on a music track')
    return spec, scenes, tracks


def attrs(start, duration, track, css=''):
    return f'class="clip {css}" data-start="{start}" data-duration="{duration}" data-track-index="{track}"'


def box(rect):
    x, y, w, h = rect
    return f'left:{x}px;top:{y}px;width:{w}px;height:{h}px;'


def duck_expression(track, voices):
    """An explicit attack/hold/release envelope, referenced to the music clip."""
    expressions = []
    gain = track['duckGain']
    for voice in voices:
        a = voice['start'] - track['start']
        b = a + voice['duration']
        if b + .4 <= 0 or a - .2 >= track['duration']:
            continue
        expressions.append(f'if(lt(t,{a-.2}),1,if(lt(t,{a}),1+({gain}-1)*(t-({a-.2}))/.2,if(lte(t,{b}),{gain},if(lt(t,{b+.4}),{gain}+(1-{gain})*(t-{b})/.4,1))))')
    result = '1'
    for expression in expressions:
        result = f'min({result},{expression})'
    return result


def build(storyboard, out, opt_in=False):
    if not opt_in:
        raise ValueError('HyperFrames is optional: obtain the user\'s choice, then pass --opt-in')
    out = Path(out).resolve()
    if out.exists():
        raise ValueError('Output exists; choose a new project')
    spec, scenes, tracks = prepare(storyboard)
    fragments, subtitle_cues = [], []
    portable = json.loads(json.dumps(spec))
    portable_scenes = {s['id']:s for s in portable['scenes']}
    out.mkdir(parents=True)
    (out / 'media').mkdir()
    (out / 'scenes').mkdir()
    def document(content, animations, composition_id, length, child=False):
        template = (ASSETS / 'index.template.html').read_text()
        replacements = {'WIDTH':str(spec['width']), 'HEIGHT':str(spec['height']), 'DURATION':str(length),
                        'FPS':str(spec.get('fps',60)), 'COMPOSITION_ID':composition_id,
                        'CONTENT':'\n'.join(content), 'ANIMATION':'\n'.join(animations),
                        'TITLE_SIZE':str(48 if spec['width'] >= spec['height'] else 56),
                        'CAPTION_SIZE':str(32 if spec['width'] >= spec['height'] else 40)}
        for key, value in replacements.items():
            template = template.replace('@@'+key+'@@', value)
        if child:
            template = template.replace('./node_modules/', '../node_modules/')
        return template
    def copy(source, name):
        target = Path('media') / (name + source.suffix.lower())
        shutil.copy2(source, out / target)
        return target.as_posix()
    for index, scene in enumerate(scenes):
        sid, start, length = scene['id'], scene['start'], scene['duration']
        video = copy(scene['source'], f'{index:03}-video')
        portable_scenes[sid]['video'] = video
        if scene.get('words'):
            portable_scenes[sid]['words'] = copy((Path(storyboard).resolve().parent/scene['words']).resolve(), f'{index:03}-words')
        sw, sh = scene['sourceSize']
        content, animations = [], []
        content.append(f'<h1 id="title-{sid}" {attrs(0,length,0)} style="{box(scene["titleRect"])}">{html.escape(scene["title"])}</h1>')
        # Intentional camera overscan is clipped by the authored frame.
        content.append(f'<div class="frame" style="{box(scene["rect"])}"><div id="footage-{sid}" class="footage" data-layout-allow-overflow style="width:{sw}px;height:{sh}px">')
        content.append(f'<video id="video-{sid}" src="../{video}" {attrs(0,length,1)} data-media-start="{scene["sourceStart"]}" muted playsinline style="width:{sw}px;height:{sh}px"></video>')
        for n, cue in enumerate(scene['cueOverlays']):
            content.append(f'<div id="focus-{sid}-{n}" {attrs(cue["start"]-start,cue["duration"],2,"focus")} style="{box(cue["rect"])}"></div>')
        content.append('</div></div>')
        for n, cue in enumerate(scene['captions']):
            subtitle_cues.append(cue)
            content.append(f'<div id="caption-{sid}-{n}" {attrs(cue["start"]-start,cue["end"]-cue["start"],3,"caption")} style="{box(scene["captionRect"])}">{html.escape(cue["text"])}</div>')
        keys = scene['cameraTransforms']
        animations.append(f'tl.set("#footage-{sid}", {json.dumps({k:keys[0][k] for k in ("x","y","scale")})}, 0);')
        for a, b in zip(keys, keys[1:]):
            initial = {k:a[k] for k in ('x','y','scale')}
            final = {k:b[k] for k in ('x','y','scale')}
            final.update(duration=b['time']-a['time'], ease='power2.inOut')
            animations.append(f'tl.fromTo("#footage-{sid}", {json.dumps(initial)}, {json.dumps(final)}, {a["time"]});')
        (out/'scenes'/f'{sid}.html').write_text(document(content, animations, f'scene-{sid}', length, True))
        fragments.append(f'<div id="host-{sid}" data-composition-id="scene-{sid}" data-composition-src="scenes/{sid}.html" {attrs(start,length,index)} style="position:absolute;inset:0"></div>')
    optional_index = 0
    rendered_tracks = []
    for index, track in enumerate(tracks):
        trim = track.get('sourceStart', 0)
        if 'duckGain' in track:
            audio = f'media/{index:03}-audio.wav'
            expression = duck_expression(track, [t for t in tracks if t['kind'] == 'voice'])
            media.run([media.FFMPEG, '-v', 'error', '-ss', trim, '-i', track['source'], '-t', track['duration'],
                       '-af', f"volume='{expression}':eval=frame", '-ar', '48000', '-ac', '2', out/audio])
            original = copy(track['source'], f'{index:03}-original-audio')
            trim = 0
        else:
            audio = copy(track['source'], f'{index:03}-audio')
            original = audio
        if track['kind'] == 'voice':
            portable_scenes[track['scene']]['audio'] = audio
        else:
            portable['audioTracks'][optional_index]['file'] = original
            optional_index += 1
        rendered_tracks.append(dict({k:v for k,v in track.items() if k != 'source'}, file=audio, sourceStart=trim))
        fragments.append(f'<audio id="audio-{index}" src="{audio}" {attrs(track["start"],track["duration"],10+index)} data-media-start="{trim}" data-volume="{track["volume"]}"></audio>')
    (out / 'index.html').write_text(document(fragments, [], 'walkthrough', spec['duration']))
    shutil.copy2(ASSETS / 'package.json', out / 'package.json')
    if (ASSETS / 'package-lock.json').is_file():
        shutil.copy2(ASSETS / 'package-lock.json', out / 'package-lock.json')
    (out / 'storyboard.json').write_text(json.dumps(portable, indent=2))
    (out / 'captions.srt').write_text('\n'.join(f'{i}\n{media.tc(c["start"])} --> {media.tc(c["end"])}\n{c["text"]}\n' for i,c in enumerate(subtitle_cues,1)))
    report = {'renderer':'hyperframes', 'version':'0.8.137', 'duration':spec['duration'], 'fps':spec.get('fps',60),
              'scenes':[{k:s[k] for k in ('id','start','duration','sourceStart','sourceSize','rect','titleRect','captionRect','captionTiming','cameraTransforms')} for s in scenes],
              'audioTracks':rendered_tracks,
              'audioProcessing':'explicit track gains; optional music ducking with 0.2s attack / 0.4s release; final loudness/peak review required',
              'review':'Project built only; render, inspect motion/frames and listen before delivery'}
    (out / 'timeline.json').write_text(json.dumps(report, indent=2))
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('storyboard'); parser.add_argument('out')
    parser.add_argument('--opt-in', action='store_true', help='Records a prior user choice; is not authorization by itself')
    args = parser.parse_args()
    try:
        build(args.storyboard, args.out, args.opt_in)
        print(str(Path(args.out).resolve()))
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr); sys.exit(1)
