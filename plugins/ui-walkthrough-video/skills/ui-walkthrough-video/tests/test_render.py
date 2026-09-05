import importlib.util
from pathlib import Path
import tempfile
import json
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

if __name__=='__main__': unittest.main()
