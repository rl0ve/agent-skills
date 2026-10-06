import base64
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import render as r
import compose_hyperframes as c
import verify_video as v


def alignment(text='Open it.'):
    return {'characters':list(text), 'character_start_times_seconds':[i*.1 for i in range(len(text))],
            'character_end_times_seconds':[(i+1)*.1 for i in range(len(text))]}


class TimingTests(unittest.TestCase):
    def test_word_timing_preserves_provider_gaps_and_punctuation(self):
        words=r.alignment_words(alignment())
        self.assertEqual([w['word'] for w in words['words']],['Open','it.'])
        self.assertAlmostEqual(words['words'][1]['start'],.5)
        self.assertEqual(r.word_cues(words['words']),[{'start':0,'end':.8,'text':'Open it.'}])

    def test_unsupported_timestamps_fail_before_generation(self):
        for voice in [{'provider':'openai','timestamps':True}, {'provider':'elevenlabs','timestamps':'yes'}]:
            with self.assertRaises(ValueError):r.request_config(voice,'Hello')

    def test_timed_endpoint_only_when_selected(self):
        voice={'provider':'elevenlabs','model':'chosen-model','voice':'chosen-voice'}
        self.assertNotIn('with-timestamps',r.request_config(voice,'Hello')[0])
        self.assertIn('/with-timestamps?',r.request_config(dict(voice,timestamps=True),'Hello')[0])

    def test_invalid_timed_response_writes_no_audio(self):
        with tempfile.TemporaryDirectory() as d:
            source=Path(d)/'source.mp3'
            bad={'audio_base64':base64.b64encode(b'ID3fake').decode(),'alignment':alignment()}
            bad['alignment']['character_end_times_seconds'][0]=-1
            for response in ['{}',json.dumps(bad)]:
                with self.assertRaises(ValueError):r.write_elevenlabs_timed(response,source)
                self.assertFalse(source.exists())

    def test_normalized_text_and_supplied_cues_are_preserved(self):
        response={'audio_base64':base64.b64encode(b'ID3fake').decode(),'alignment':alignment('bad'),
                  'normalized_alignment':alignment('Two items.')}
        with tempfile.TemporaryDirectory() as d:
            words=r.write_elevenlabs_timed(json.dumps(response),Path(d)/'source.mp3')
            self.assertEqual(words['text'],'Two items.')
            cues=[{'start':.1,'end':.9,'text':'Two items.'}]
            self.assertEqual(r.cues_for({'cues':cues},1.1,words),(cues,'supplied'))

    def test_out_of_range_or_overlapping_word_cues_fail(self):
        for words in [[None], [{}], [{'word':'a','start':0,'end':2}], [{'word':'a','start':0,'end':.5},{'word':'b','start':.4,'end':.8}]]:
            with self.assertRaises(ValueError):r.validate_words(words,1)

    @unittest.skipUnless(shutil.which(r.FFMPEG) and shutil.which(r.FFPROBE),'FFmpeg/ffprobe required')
    def test_timed_voice_workflow_writes_decodable_audio_and_measured_sidecar(self):
        # A tone verifies the timed API transport, not generated speech quality.
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); mp3=root/'tone.mp3'
            subprocess.run([r.FFMPEG,'-v','error','-f','lavfi','-i','sine=frequency=440:duration=1.2','-c:a','libmp3lame',str(mp3)],check=True,capture_output=True)
            payload=json.dumps({'audio_base64':base64.b64encode(mp3.read_bytes()).decode(),
                                'normalized_alignment':alignment()}).encode()
            manifest=root/'manifest.json'
            manifest.write_text(json.dumps({'version':1,'voice':{'provider':'elevenlabs','model':'chosen-model','voice':'chosen-voice','timestamps':True},
                                            'beats':[{'id':'intro','narration':'Open it.'}]}))
            args=SimpleNamespace(manifest=manifest,out=root/'audio',allow_paid=False,allow_local_test=False)
            def response(request,timeout):
                self.assertIn('/with-timestamps?',request.full_url)
                self.assertEqual(json.loads(request.data)['text'],'Open it.')
                return contextlib.closing(io.BytesIO(payload))
            with patch.dict(os.environ,{'ELEVENLABS_API_KEY':'test-key'}),patch.object(r.urllib.request,'urlopen',side_effect=response) as network,contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(ValueError):r.voice_command(args)
                network.assert_not_called();self.assertFalse(args.out.exists())
                args.allow_paid=True;r.voice_command(args);self.assertEqual(network.call_count,1)
            stream=r.probe(args.out/'intro.wav')['streams'][0]
            self.assertEqual((stream['sample_rate'],stream['channels']),('48000',2))
            words=r.load_words(args.out/'intro.words.json',r.duration(args.out/'intro.wav'))
            self.assertEqual(r.cues_for({},1.2,words)[1],'provider-character-alignment')
            self.assertNotIn('test-key',(args.out/'voice.json').read_text())


class CompositionTests(unittest.TestCase):
    def storyboard(self, root, portrait=False):
        (root/'video.mp4').write_bytes(b'fixture')
        (root/'voice.wav').write_bytes(b'fixture')
        (root/'words.json').write_text(json.dumps(r.alignment_words(alignment())))
        spec={'version':1,'treatment':'demo','width':1080 if portrait else 1920,'height':1920 if portrait else 1080,
              'duration':4,'scenes':[{'id':'result','start':0,'duration':4,'title':'Result <observed>',
              'video':'video.mp4','sourceStart':2,'rect':[40,160,1000,600], 'titleRect':[40,40,1000,100],
              'captionRect':[40,800,1000,150],'audio':'voice.wav','audioOffset':.5,'words':'words.json',
              'cueOverlays':[{'wordIndex':1,'duration':1,'rect':[10,10,200,100]}]}]}
        path=root/'storyboard.json';path.write_text(json.dumps(spec));return path

    def probe(self, path):
        return {'streams':[{'codec_type':'video','width':1440,'height':900}] if str(path).endswith('.mp4') else [{'codec_type':'audio'}]}

    def duration(self, path):return 10 if str(path).endswith('.mp4') else 1

    def test_missing_opt_in_has_no_side_effects(self):
        with tempfile.TemporaryDirectory() as d, patch.object(c,'prepare') as prepare:
            out=Path(d)/'project'
            with self.assertRaises(ValueError):c.build('unused',out)
            prepare.assert_not_called();self.assertFalse(out.exists())

    def test_both_layouts_preserve_trim_audio_offset_and_word_anchor(self):
        for portrait in (False,True):
            with tempfile.TemporaryDirectory() as d, patch.object(r,'probe',side_effect=self.probe), patch.object(r,'duration',side_effect=self.duration):
                root=Path(d);path=self.storyboard(root,portrait)
                spec,scenes,tracks=c.prepare(path)
                self.assertEqual(scenes[0]['cueOverlays'][0]['start'],1)
                self.assertEqual(scenes[0]['captions'][0]['start'],.5)
                report=c.build(path,root/'project',True)
                page=(root/'project/scenes/result.html').read_text()
                self.assertIn('data-media-start="2"',page)
                self.assertIn('Result &lt;observed&gt;',page)
                self.assertIn('paused: true',page)
                self.assertEqual(report['scenes'][0]['captionTiming'],'provider-character-alignment')
                packaged=json.loads((root/'project/storyboard.json').read_text())
                self.assertTrue((root/'project'/packaged['scenes'][0]['words']).is_file())
                self.assertIn('00:00:00,500',(root/'project/captions.srt').read_text())

    def test_invalid_layout_or_short_source_writes_no_project(self):
        with tempfile.TemporaryDirectory() as d, patch.object(r,'probe',side_effect=self.probe), patch.object(r,'duration',return_value=1):
            root=Path(d);path=self.storyboard(root)
            with self.assertRaises(ValueError):c.build(path,root/'out',True)
            self.assertFalse((root/'out').exists())
            with self.assertRaises(ValueError):c.rectangle([1000,0,100,100],1080,1920)

    def test_review_samples_both_sides_of_cuts_and_camera_endpoints(self):
        times=v.review_times(8,60,{'scenes':[{'start':0,'duration':4,'cameraTransforms':[{'time':1}]},{'start':4,'duration':4}]})
        self.assertIn(4-1/60,times);self.assertIn(4,times);self.assertIn(4+1/60,times);self.assertIn(1,times)
        self.assertTrue(all(0<=t<8 for t in times))


if __name__=='__main__':unittest.main()
