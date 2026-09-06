"""Offline MiniMax contract and real media conversion; no paid generation."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import urllib.error

spec=importlib.util.spec_from_file_location('render',Path(__file__).resolve().parents[1]/'scripts/render.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
VOICE={'provider':'minimax','model':'speech-2.8-hd','voice':'English_expressive_narrator'}


def response(audio=b'ID3fixture'):
    return {'base_resp':{'status_code':0},'data':{'status':2,'audio':audio.hex()},'extra_info':{'audio_format':'mp3'}}


def write_manifest(path, beats=None, voice=None):
    path.write_text(json.dumps({'version':1,'voice':voice or VOICE,'beats':beats or [{'id':'intro','narration':'The example has 3 steps.'}]}))


class MiniMaxTests(unittest.TestCase):
    def test_explicit_model_voice_format_and_no_unsupported_fields(self):
        url,key,body=r.request_config(dict(VOICE,speed=.9,quality='audition'),'Exact text')
        self.assertEqual((url,key),('https://api.minimax.io/v1/t2a_v2','MINIMAX_API_KEY'))
        self.assertEqual(body['text'],'Exact text')
        self.assertEqual(body['model'],'speech-2.8-hd')
        self.assertEqual(body['voice_setting']['voice_id'],VOICE['voice'])
        self.assertEqual(body['voice_setting']['speed'],.9)
        self.assertEqual((body['stream'],body['output_format'],body['audio_setting']['format']),(False,'hex','mp3'))
        self.assertNotIn('quality',body)
        for field in ('instructions','voice_settings','rate'):
            with self.subTest(field=field),self.assertRaises(ValueError):
                r.request_config(dict(VOICE,**{field:'unsupported'}),'Hello')

    def test_invalid_requests_fail_before_generation(self):
        for speed in (0,3,float('nan'),True,'1'):
            with self.subTest(speed=speed),self.assertRaises(ValueError):
                r.request_config(dict(VOICE,speed=speed),'Hello')
        for text in ('',' ', 'x'*10000):
            with self.assertRaises(ValueError): r.request_config(VOICE,text)
        for field in ('model','voice'):
            v=dict(VOICE);del v[field]
            with self.assertRaises(ValueError):r.request_config(v,'Hello')

    def test_hex_bytes_are_preserved(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'speech.mp3'
            r.write_minimax_mp3(json.dumps(response()),path)
            self.assertEqual(path.read_bytes(),b'ID3fixture')

    def test_failures_do_not_write_audio_or_echo_response(self):
        cases=[b'not-json',b'\xff',b'null',b'[]',b'{}']
        for code in (1004,False,None):
            obj=response();obj['base_resp']['status_code']=code;obj['base_resp']['status_msg']='private-provider-message';cases.append(json.dumps(obj))
        for data in (None, {'status':1,'audio':'494433'}, {'status':2,'audio':''}, {'status':2,'audio':'xyz'}, {'status':2,'audio':'0'}, {'status':2,'audio':'52494646'}):
            obj=response();obj['data']=data;cases.append(json.dumps(obj))
        obj=response();obj['extra_info']['audio_format']='wav';cases.append(json.dumps(obj))
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'bad.mp3'
            for item in cases:
                with self.subTest(item=item):
                    with self.assertRaises(ValueError) as failure:r.write_minimax_mp3(item,path)
                    self.assertNotIn('private-provider-message',str(failure.exception))
                    self.assertFalse(path.exists())

    def test_permission_key_and_entire_batch_are_preflighted(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'manifest.json';out=Path(d)/'audio';write_manifest(path)
            args=SimpleNamespace(manifest=path,out=out,allow_paid=False,allow_local_test=False)
            with patch.dict(os.environ,{'MINIMAX_API_KEY':'test-key'}),patch.object(r.urllib.request,'urlopen') as network:
                with self.assertRaises(ValueError):r.voice_command(args)
                network.assert_not_called();self.assertFalse(out.exists())
            args.allow_paid=True
            with patch.dict(os.environ,{},clear=True),patch.object(r.urllib.request,'urlopen') as network:
                with self.assertRaises(ValueError):r.voice_command(args)
                network.assert_not_called();self.assertFalse(out.exists())
            write_manifest(path,[{'id':'one','narration':'valid'},{'id':'two','narration':'x'*10000}])
            with patch.dict(os.environ,{'MINIMAX_API_KEY':'test-key'}),patch.object(r.urllib.request,'urlopen') as network:
                with self.assertRaises(ValueError):r.voice_command(args)
                network.assert_not_called();self.assertFalse(out.exists())

    def test_media_processes_do_not_receive_minimax_key(self):
        with patch.dict(os.environ,{'MINIMAX_API_KEY':'private'}),patch.object(r.subprocess,'run') as execute:
            r.run(['ffprobe'])
            self.assertNotIn('MINIMAX_API_KEY',execute.call_args.kwargs['env'])

    def test_http_failure_has_no_automatic_retry(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'manifest.json';out=Path(d)/'audio';write_manifest(path)
            args=SimpleNamespace(manifest=path,out=out,allow_paid=True,allow_local_test=False)
            error=urllib.error.HTTPError('https://api.minimax.io/v1/t2a_v2',429,'private-provider-message',None,None)
            with patch.dict(os.environ,{'MINIMAX_API_KEY':'test-key'}),patch.object(r.urllib.request,'urlopen',side_effect=error) as network:
                with self.assertRaisesRegex(ValueError,'HTTP 429') as failure:r.voice_command(args)
                self.assertEqual(network.call_count,1)
                self.assertNotIn('private-provider-message',str(failure.exception))
                self.assertEqual(json.loads((out/'voice.json').read_text()),VOICE)
                self.assertFalse((out/'intro.wav').exists())

    @unittest.skipUnless(shutil.which(r.FFMPEG) and shutil.which(r.FFPROBE),'FFmpeg/ffprobe required for real decode')
    def test_audio_only_workflow_converts_fixture_with_real_ffmpeg(self):
        # A generated tone tests transport/decoding, not speech quality.
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);mp3=folder/'fixture.mp3'
            subprocess.run([r.FFMPEG,'-v','error','-f','lavfi','-i','sine=frequency=440:duration=0.25','-c:a','libmp3lame',str(mp3)],check=True,capture_output=True)
            raw=mp3.read_bytes();payload=json.dumps(response(raw)).encode()
            path=folder/'manifest.json';out=folder/'audio';write_manifest(path)
            seen=[]
            def fake_network(request,timeout):
                seen.append(request)
                self.assertEqual(request.get_header('Authorization'),'Bearer test-key')
                self.assertEqual(json.loads(request.data)['text'],'The example has 3 steps.')
                return contextlib.closing(io.BytesIO(payload))
            args=SimpleNamespace(manifest=path,out=out,allow_paid=True,allow_local_test=False)
            with patch.dict(os.environ,{'MINIMAX_API_KEY':'test-key'}),patch.object(r.urllib.request,'urlopen',side_effect=fake_network),contextlib.redirect_stdout(io.StringIO()):
                r.voice_command(args)
            self.assertEqual(len(seen),1)
            self.assertEqual((out/'intro.mp3').read_bytes(),raw)
            streams=r.probe(out/'intro.wav')['streams']
            self.assertEqual((streams[0]['codec_type'],streams[0]['sample_rate'],streams[0]['channels']),('audio','48000',2))
            self.assertGreater(r.duration(out/'intro.wav'),.2)
            self.assertNotIn('test-key',(out/'voice.json').read_text())


if __name__=='__main__':unittest.main()
