import sys
from pathlib import Path
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import polish as p

class PolishTests(unittest.TestCase):
    def test_camera_clamps_extreme_focus_without_exposing_canvas(self):
        keys=[{'time':0,'zoom':1,'cx':720,'cy':450},{'time':2,'zoom':2,'cx':1440,'cy':0}]
        p.validate_camera(keys,1440,900,3)
        for frame in range(91):
            x,y,w,h=p.camera_at(keys,frame/30,1440,900)
            self.assertGreaterEqual(x,0);self.assertGreaterEqual(y,0)
            self.assertLessEqual(x+w,1440);self.assertLessEqual(y+h,900)
        self.assertEqual(p.camera_at(keys,2,1440,900),(720,0,720,450))

    def test_camera_rejects_ambiguous_keyframe_order(self):
        with self.assertRaises(ValueError):p.validate_camera([{'time':0,'zoom':1,'cx':0,'cy':0},{'time':0,'zoom':1,'cx':0,'cy':0}],1440,900,2)

    def test_marker_trim_removes_marker_and_keeps_first_clean_frame(self):
        data=bytes([0,0,0]*3+[250,5,250]*4+[0,0,0]*5)
        with patch.object(p.media,'run',return_value=data):self.assertEqual(p.marker_end('synthetic.webm'),7)

    def test_missing_marker_fails_instead_of_guessing(self):
        with patch.object(p.media,'run',return_value=bytes(30)),self.assertRaises(ValueError):p.marker_end('synthetic.webm')

    def test_openrouter_gemini_requires_pcm(self):
        _,env,body=p.media.request_config({'provider':'openrouter','model':'google/gemini-3.1-flash-tts-preview','voice':'Kore'},'Hello')
        self.assertEqual(env,'OPENROUTER_API_KEY');self.assertEqual(body['response_format'],'pcm')

    def test_openrouter_does_not_silently_drop_instructions(self):
        with self.assertRaises(ValueError):p.media.request_config({'provider':'openrouter','model':'google/gemini-3.1-flash-tts-preview','voice':'Kore','instructions':'Calm'},'Hello')
        _,_,body=p.media.request_config({'provider':'openrouter','model':'openai/gpt-4o-mini-tts-2025-12-15','voice':'marin','instructions':'Calm'},'Hello')
        self.assertEqual(body['provider']['options']['openai']['instructions'],'Calm')

if __name__=='__main__':unittest.main()
