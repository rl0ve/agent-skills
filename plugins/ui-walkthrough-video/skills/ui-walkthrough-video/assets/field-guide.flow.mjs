import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
const url=process.env.DEMO_URL;
const audio=process.env.DEMO_AUDIO_DIR;
if(!url||!audio)throw Error('Set DEMO_URL to the existing field-guide URL and DEMO_AUDIO_DIR to its narration WAV directory');
const plan=JSON.parse(fs.readFileSync(process.env.DEMO_PLAN??new URL('./field-guide-narration.example.json',import.meta.url)));
const env={...process.env};
for(const key of ['OPENAI_API_KEY','OPENROUTER_API_KEY','GEMINI_API_KEY','GOOGLE_API_KEY','ELEVENLABS_API_KEY'])delete env[key];
for(const beat of plan.beats){
  const duration=Number(execFileSync(process.env.FFPROBE??'ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',path.resolve(audio,beat.id+'.wav')],{encoding:'utf8',env}));
  if(!Number.isFinite(duration)||duration<=0)throw Error('Invalid narration duration');
  beat.duration=Math.ceil((duration+1.2)*30)/30;
}
export const settings={channel:'msedge',width:1440,height:900,source:'Existing Design Router Field Guide; real controls',voice:plan.voice};
const frame=(time,zoom=1,cx=720,cy=450)=>({time,zoom,cx,cy});
async function setup(page,surface='product-app',audience='b2b-saas'){
  await page.goto(url);await page.locator('#surface-select option').first().waitFor({state:'attached'});
  await page.locator('#surface-select').selectOption(surface);await page.locator('#audience-select').selectOption(audience);
  await page.evaluate(()=>window.scrollTo(0,scrollY+document.querySelector('#route').getBoundingClientRect().top-40*Number(document.documentElement.style.zoom||1)));
}
export const beats=plan.beats.map(b=>{
  if(b.id==='surface')return {...b,setup:page=>setup(page),
    camera:[frame(0),frame(.7),frame(2.7,1.2,650,430),frame(b.duration,1.2,650,430)],
    async perform({page,at,point}){
      await at(3.1);await point(page.locator('#surface-select'),{click:true,label:'Surface selector'});
      await page.waitForTimeout(260);await page.keyboard.press('Escape');await page.locator('#surface-select').selectOption('creative-expressive');
      if(await page.locator('#surface-select').inputValue()!=='creative-expressive')throw Error('Surface choice failed');
      await page.locator('#route-line').filter({hasText:'creative-expressive'}).waitFor();
    }};
  if(b.id==='audience')return {...b,setup:page=>setup(page,'creative-expressive'),
    camera:[frame(0,1.2,650,430),frame(3.7,1.2,650,430),frame(5.9,1.12,1000,480),frame(b.duration,1.12,1000,480)],
    async perform({page,at,point}){
      await at(1.0);await point(page.locator('#audience-select'),{click:true,label:'Audience selector'});
      await page.waitForTimeout(250);await page.keyboard.press('Escape');await page.locator('#audience-select').selectOption('portfolio-personal');
      if(await page.locator('#audience-select').inputValue()!=='portfolio-personal')throw Error('Audience choice failed');
      await page.locator('#route-line').filter({hasText:'portfolio-personal'}).waitFor();
    }};
  return {...b,cursor:false,async setup(page){
      await setup(page,'creative-expressive','portfolio-personal');
      await page.evaluate(()=>window.scrollBy(0,290*Number(document.documentElement.style.zoom||1)));
    },
    camera:[frame(0,1.08,1000,455),frame(1,1.08,1000,455),frame(4.2,1.16,1030,455),frame(b.duration,1.16,1030,455)],
    async perform({page}){
      await page.locator('#route-detail').getByRole('heading',{name:'Substitutions',exact:true}).waitFor();
    }};
});
