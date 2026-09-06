// Real browser footage with recorded cursor motion and source-time events.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const [flowPath,outPath]=process.argv.slice(2);
if(!flowPath||!outPath)throw Error('Usage: node capture-polished.mjs FLOW.mjs NEW_OUTPUT');
const {settings={},beats}=await import(pathToFileURL(path.resolve(flowPath)));
const logicalWidth=settings.width??1440,logicalHeight=settings.height??900,scale=settings.captureScale??2;
if(![1,2].includes(scale))throw Error('captureScale must be 1 or 2');
const width=logicalWidth*scale,height=logicalHeight*scale;
if(![width,height].every(n=>Number.isInteger(n)&&n>0&&n%2===0))throw Error('Invalid dimensions');
if(!Array.isArray(beats)||!beats.length)throw Error('No beats');
const seen=new Set();
for(const b of beats){
  if(!/^[a-z0-9][a-z0-9_-]*$/.test(b.id)||seen.has(b.id)||typeof b.setup!=='function'||typeof b.perform!=='function'||!b.narration?.trim()||!Number.isFinite(b.duration)||b.duration<=0)throw Error('Invalid beat');
  seen.add(b.id);
}
const require=createRequire(path.resolve(process.env.PLAYWRIGHT_PACKAGE||'package.json'));
const {chromium}=require('playwright');
const allowedVoice=new Set(['provider','model','voice','quality','rate','instructions','speed','voice_settings']);
if(settings.voice&&Object.keys(settings.voice).some(k=>!allowedVoice.has(k)))throw Error('Unknown voice field; keep credentials out of manifests');
const out=path.resolve(outPath);
if(fs.existsSync(out))throw Error('Output exists; use a new take');
fs.mkdirSync(out,{recursive:true});
const report={version:1,mode:'polished-capture',width,height,captureScale:scale,pixelRatio:1,fps:30,source:settings.source??'local interface',voice:settings.voice??{provider:'provided'},beats:[]};
const browser=await chromium.launch({channel:settings.channel??'msedge',headless:settings.headless??true});
try{
  for(const beat of beats){
    const dir=path.join(out,beat.id);fs.mkdirSync(dir);
    const context=await browser.newContext({viewport:{width,height},deviceScaleFactor:1,reducedMotion:'reduce',recordVideo:{dir,size:{width,height}}});
    await context.addInitScript(({scale})=>{document.addEventListener('DOMContentLoaded',()=>{document.documentElement.style.zoom=String(scale)},{once:true})},{scale});
    const page=await context.newPage(),video=page.video();
    const events=[];let evidenceCapturedAt=null;
    try{
      await beat.setup(page);
      await page.evaluate(()=>document.fonts.ready);
      // Let the video encoder settle before the visible timing marker.
      await page.waitForTimeout(3000);
      await page.evaluate(({scale})=>{
        const style=document.createElement('style');style.textContent='*{cursor:none!important}html{scroll-behavior:auto!important}';document.head.append(style);
        const pointer=document.createElement('div');pointer.id='walkthrough-pointer';
        pointer.style.cssText='position:fixed;left:0;top:0;width:30px;height:38px;pointer-events:none;z-index:2147483646;filter:drop-shadow(0px 2px 2px #0008);transform:translate(680px,700px)';
        pointer.style.zoom=String(1/scale);pointer.style.width=`${30*scale}px`;pointer.style.height=`${38*scale}px`;
        pointer.innerHTML='<svg width="100%" height="100%" viewBox="0 0 30 38"><path d="M2 2L2 29L9 22L15 35L21 32L15 20L26 20Z" fill="white" stroke="#152330" stroke-width="2" stroke-linejoin="round"/></svg>';
        document.body.append(pointer);
        window.addEventListener('mousemove',e=>{pointer.style.transform=`translate(${e.clientX}px,${e.clientY}px)`},{capture:true});
        window.addEventListener('mousedown',e=>{
          const pulse=document.createElement('div');pulse.style.cssText=`position:fixed;zoom:${1/scale};left:${e.clientX-22*scale}px;top:${e.clientY-22*scale}px;width:${44*scale}px;height:${44*scale}px;border:${3*scale}px solid #e9783c;background:#e9783c30;border-radius:50%;box-sizing:border-box;pointer-events:none;z-index:2147483645`;
          document.body.append(pulse);
          pulse.animate([{transform:'scale(.35)',opacity:1},{transform:'scale(1.45)',opacity:0}],{duration:550,easing:'cubic-bezier(.2,.8,.2,1)'}).finished.then(()=>pulse.remove());
        },{capture:true});
        const marker=document.createElement('div');marker.id='walkthrough-sync';marker.style.cssText='position:fixed;left:0;top:0;width:12px;height:12px;background:#ff00ff;z-index:2147483647;pointer-events:none';marker.style.zoom=String(1/scale);document.body.append(marker);
      },{scale});
      await page.mouse.move(680*scale,700*scale);
      await page.waitForTimeout(400);
      await page.evaluate(()=>{document.querySelector('#walkthrough-sync').remove();window.walkthroughStart=performance.now();});
      const now=()=>page.evaluate(()=>(performance.now()-window.walkthroughStart)/1000);
      let cursor={x:680*scale,y:700*scale};
      const at=async time=>{const remaining=time-await now();if(remaining>0)await page.waitForTimeout(remaining*1000);};
      const point=async(locator,{seconds=.85,click=false,label='target'}={})=>{
        await locator.waitFor({state:'visible'});
        const box=await locator.boundingBox();
        if(!box||box.width<=0||box.height<=0)throw Error('Target has no visible bounds');
        const target={x:box.x+box.width/2,y:box.y+box.height/2};
        if(target.x<0||target.x>=width||target.y<0||target.y>=height)throw Error('Target outside viewport; explicitly scroll before pointing');
        const unobscured=await locator.evaluate((el,p)=>{const hit=document.elementFromPoint(p.x,p.y);return el===hit||el.contains(hit);},target);
        if(!unobscured)throw Error('Target is obscured');
        const origin={...cursor},start=await now(),steps=Math.max(2,Math.ceil(seconds*30));
        for(let i=1;i<=steps;i++){
          const u=i/steps,e=u*u*u*(u*(u*6-15)+10);
          await page.mouse.move(origin.x+(target.x-origin.x)*e,origin.y+(target.y-origin.y)*e);
          await at(start+(i/steps)*seconds);
        }
        cursor=target;events.push({type:'pointer',label,start,end:await now(),from:origin,to:target,bounds:box});
        if(click){
          await page.waitForTimeout(180);
          const current=await locator.boundingBox();
          if(!current||target.x<current.x||target.x>current.x+current.width||target.y<current.y||target.y>current.y+current.height)throw Error('Target moved before click');
          const stillVisible=await locator.evaluate((el,p)=>{const hit=document.elementFromPoint(p.x,p.y);return el===hit||el.contains(hit);},target);
          if(!stillVisible)throw Error('Target became obscured before click');
          events.push({type:'click',label,time:await now(),point:target,bounds:current});
          await page.mouse.click(target.x,target.y);
        }
        return box;
      };
      const scroll=async(y,seconds=.9)=>{
        const from=await page.evaluate(()=>scrollY),start=await now();
        const steps=Math.max(2,Math.ceil(seconds*30));
        for(let i=1;i<=steps;i++){
          const u=i/steps,e=u*u*u*(u*(u*6-15)+10);
          await page.evaluate(value=>window.scrollTo(0,value),from+(y-from)*e);await at(start+(i/steps)*seconds);
        }
        events.push({type:'scroll',start,end:await now(),from,to:await page.evaluate(()=>scrollY)});
      };
      await beat.perform({page,at,point,scroll,now,events});
      const finished=await now();
      if(finished>beat.duration+.1)throw Error('Actions exceed planned beat duration; extend the narration/edit plan');
      events.push({type:'verified-result',time:finished});
      await at(beat.duration+1); // capture tail for encoder/paint latency; not part of the edit
      await page.screenshot({path:path.join(dir,'evidence.png')});
      evidenceCapturedAt=await now();
    }finally{await context.close();}
    await video.saveAs(path.join(dir,'capture.webm'));await video.delete();
    report.beats.push({id:beat.id,title:beat.title??beat.id,narration:beat.narration,duration:beat.duration,audioOffset:beat.audioOffset??.5,video:`${beat.id}/capture.webm`,screenshot:`${beat.id}/evidence.png`,evidenceCapturedAt,events,camera:(beat.camera??[{time:0,zoom:1,cx:logicalWidth/2,cy:logicalHeight/2}]).map(k=>({...k,cx:k.cx*scale,cy:k.cy*scale})),captions:beat.captions??null});
    fs.writeFileSync(path.join(out,'manifest.partial.json'),JSON.stringify(report,null,2));
    console.log(`Captured ${beat.id}: ${beat.duration}s, ${events.length} events`);
  }
  fs.renameSync(path.join(out,'manifest.partial.json'),path.join(out,'manifest.json'));
}catch(error){
  fs.writeFileSync(path.join(out,'failure.json'),JSON.stringify({status:'failed',completed:report.beats.map(b=>b.id),nextBeat:beats[report.beats.length]?.id,note:'Preserve raw footage for diagnosis. A partial take is not a finished demo.'},null,2));
  throw error;
}finally{await browser.close();}
