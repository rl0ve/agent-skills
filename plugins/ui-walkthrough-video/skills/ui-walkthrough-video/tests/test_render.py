import importlib.util
from pathlib import Path
import tempfile
import json
import base64
import wave
from types import SimpleNamespace
from unittest.mock import patch
import unittest

s=importlib.util.spec_from_file_location('render',Path(__file__).resolve().parents[1]/'scripts/render.py')
r=importlib.util.module_from_spec(s); s.loader.exec_module(r)

class RenderTests(unittest.TestCase):
    def test_timecode_carry(self):
        self.assertEqual(r.tc(59.9999),'00:01:00,000')
        self.assertEqual(r.tc(3599.9999),'01:00:00,000')

    def test_estimated_captions_cover_speech(self):
        cues,kind=r.cues_for({'narration':'A short sentence. '*20},7.2)
        self.assertEqual(kind,'estimated')
        self.assertAlmostEqual(cues[-1]['end'],7.2)
        self.assertEqual(cues[0]['start'],0)
        self.assertTrue(all(a['end']==b['start'] for a,b in zip(cues,cues[1:])))

    def test_supplied_captions_reject_overlap(self):
        with self.assertRaises(ValueError):
            r.cues_for({'cues':[{'start':0,'end':2,'text':'a'},{'start':1,'end':3,'text':'b'}]},4)

    def test_provider_contracts(self):
        url,key,body=r.request_config({'provider':'openai','model':'gpt-4o-mini-tts','voice':'coral','instructions':'Calm'},'Hello')
        self.assertEqual(key,'OPENAI_API_KEY')
        self.assertEqual(body['instructions'],'Calm')
        self.assertNotIn('quality',body)
        url,key,body=r.request_config({'provider':'elevenlabs','model':'eleven_multilingual_v2','voice':'id','voice_settings':{'stability':.5}},'Hello')
        self.assertEqual(body['model_id'],'eleven_multilingual_v2')
        self.assertEqual(key,'ELEVENLABS_API_KEY')
        self.assertTrue(url.startswith('https://api.elevenlabs.io/'))

    def test_legacy_instructions_not_silently_ignored(self):
        with self.assertRaises(ValueError):
            r.request_config({'provider':'openai','model':'tts-1','voice':'alloy','instructions':'Calm'},'Hello')

    def test_credentials_rejected_before_serializing(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'manifest.json'
            p.write_text(json.dumps({'version':1,'voice':{'provider':'local','api_key':'secret'},'beats':[{'id':'one','narration':'Hello'}]}))
            with self.assertRaises(ValueError): r.load(p)

    def test_media_children_do_not_inherit_provider_keys(self):
        with patch.dict(r.os.environ,{'OPENAI_API_KEY':'private','ELEVENLABS_API_KEY':'private'}):
            with patch.object(r.subprocess,'run') as execute:
                r.run(['ffprobe'])
                self.assertNotIn('OPENAI_API_KEY',execute.call_args.kwargs['env'])
                self.assertNotIn('ELEVENLABS_API_KEY',execute.call_args.kwargs['env'])

    def test_existing_output_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'keep'; p.write_text('existing')
            with self.assertRaises(ValueError): r.fresh(d)
            self.assertEqual(p.read_text(),'existing')

class GeminiTests(unittest.TestCase):
    def response(self, pcm=b'\x00\x00'*240):
        return json.dumps({'candidates':[{'finishReason':'STOP','content':{'parts':[
            {'inlineData':{'mimeType':'audio/L16;codec=pcm;rate=24000','data':base64.b64encode(pcm).decode()}}
        ]}}]})

    def test_request_contract(self):
        url,key,body=r.request_config({'provider':'gemini','model':'gemini-3.1-flash-tts-preview','voice':'Kore','instructions':'Natural'},'Hello')
        self.assertEqual(key,'GEMINI_API_KEY')
        self.assertTrue(url.endswith(':generateContent'))
        self.assertEqual(body['generationConfig']['speechConfig']['voiceConfig']['prebuiltVoiceConfig']['voiceName'],'Kore')
        self.assertIn('Hello',body['contents'][0]['parts'][0]['text'])

    def test_pcm_wrapped_correctly(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'audio.wav'; r.write_gemini_wav(self.response(),p)
            with wave.open(str(p)) as w:
                self.assertEqual((w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getnframes()),(1,2,24000,240))

    def test_bad_responses_write_no_audio(self):
        cases=['{}','not JSON',self.response(b''),self.response(b'x')]
        for field,value in [('finishReason','MAX_TOKENS')]:
            obj=json.loads(self.response()); obj['candidates'][0][field]=value; cases.append(json.dumps(obj))
        for mime in ['audio/mpeg','audio/L16;rate=16000']:
            obj=json.loads(self.response()); obj['candidates'][0]['content']['parts'][0]['inlineData']['mimeType']=mime; cases.append(json.dumps(obj))
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.wav'
            for case in cases:
                with self.subTest(case=case), self.assertRaises(ValueError): r.write_gemini_wav(case,p)
                self.assertFalse(p.exists())

    def test_no_implicit_speech_or_paid_calls(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'manifest.json'; out=Path(d)/'output'
            for voice in [None,{'provider':'local'}, {'provider':'gemini','model':'gemini-3.1-flash-tts-preview','voice':'Kore'}]:
                spec={'version':1,'beats':[{'id':'one','narration':'Hello'}]}
                if voice: spec['voice']=voice
                p.write_text(json.dumps(spec))
                with patch.object(r.urllib.request,'urlopen') as network, self.assertRaises(ValueError):
                    r.voice_command(SimpleNamespace(manifest=p,out=out,allow_paid=False,allow_local_test=False))
                network.assert_not_called(); self.assertFalse(out.exists())

    def test_google_keys_not_in_media_environment(self):
        with patch.dict(r.os.environ,{'GEMINI_API_KEY':'private','GOOGLE_API_KEY':'private'}), patch.object(r.subprocess,'run') as execute:
            r.run(['ffprobe'])
            self.assertNotIn('GEMINI_API_KEY',execute.call_args.kwargs['env'])
            self.assertNotIn('GOOGLE_API_KEY',execute.call_args.kwargs['env'])

if __name__=='__main__': unittest.main()
