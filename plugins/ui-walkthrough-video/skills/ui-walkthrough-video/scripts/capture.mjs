import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';

const [flowPath, outPath] = process.argv.slice(2);
if (!flowPath || !outPath) throw Error('Usage: node capture.mjs flow.mjs NEW_OUTPUT_DIRECTORY');
const {settings = {}, beats} = await import(pathToFileURL(path.resolve(flowPath)).href);
if (!Array.isArray(beats) || !beats.length) throw Error('No beats');
const ids = new Set();
for (const b of beats) {
  if (!/^[a-z0-9][a-z0-9_-]*$/.test(b.id) || ids.has(b.id) || typeof b.run !== 'function' || !b.narration?.trim()) throw Error('Invalid or duplicate beat');
  ids.add(b.id);
}
const allowedVoice = new Set(['provider','model','voice','quality','rate','instructions','speed','voice_settings']);
if (settings.voice && Object.keys(settings.voice).some(k => !allowedVoice.has(k))) throw Error('Unknown voice field; credentials belong in environment variables');
if (settings.voice?.voice_settings && Object.keys(settings.voice.voice_settings).some(k => !['stability','similarity_boost','style','use_speaker_boost','speed'].includes(k))) throw Error('Unknown voice_settings field');
const width = settings.width ?? 1440, height = settings.height ?? 900;
if (![width,height].every(n => Number.isInteger(n) && n > 0 && n % 2 === 0)) throw Error('Dimensions must be positive even integers');
const require = createRequire(path.resolve(process.env.PLAYWRIGHT_PACKAGE || 'package.json'));
const {chromium} = require('playwright');
const out = path.resolve(outPath);
if (fs.existsSync(out)) throw Error('Output exists; choose a new take');
const browser = await chromium.launch({channel: settings.channel ?? 'msedge', headless: settings.headless ?? true});
fs.mkdirSync(out, {recursive:true});
const manifest = {version:1, width, height, fps:30, voice:settings.voice ?? {provider:'local',quality:'draft'}, beats:[]};
fs.writeFileSync(path.join(out,'manifest.partial.json'),JSON.stringify(manifest,null,2));
try {
  for (const beat of beats) {
    const dir = path.join(out, beat.id);
    fs.mkdirSync(dir);
    const context = await browser.newContext({viewport:{width,height},recordVideo:{dir,size:{width,height}}});
    const page = await context.newPage();
    const video = page.video();
    try {
      await beat.run(page);
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({path:path.join(dir,'evidence.png')});
      await page.waitForTimeout(beat.holdMs ?? 1500);
    } finally { await context.close(); }
    await video.saveAs(path.join(dir,'capture.webm'));
    await video.delete();
    manifest.beats.push({id:beat.id,narration:beat.narration,video:`${beat.id}/capture.webm`,screenshot:`${beat.id}/evidence.png`,...(beat.cues ? {cues:beat.cues} : {})});
    // Partial progress is useful, but marked incomplete until every beat succeeds.
    fs.writeFileSync(path.join(out,'manifest.partial.json'),JSON.stringify(manifest,null,2));
    console.log(`Captured ${beat.id}`);
  }
  fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2));
  fs.unlinkSync(path.join(out,'manifest.partial.json'));
} catch (error) {
  fs.writeFileSync(path.join(out,'failure.json'),JSON.stringify({status:'failed',completed:manifest.beats.map(b=>b.id),nextBeat:beats[manifest.beats.length]?.id,note:'Raw media may remain in the failing beat directory. Correct the flow and use a new take; do not treat partial footage as complete.'},null,2));
  throw error;
} finally { await browser.close(); }
