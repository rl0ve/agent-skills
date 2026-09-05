// Synthetic fixture: replace with your actual observed interface and assertions.
export const settings = {
  channel: 'msedge', width: 1440, height: 900,
  voice: {provider: 'local', voice: 'Samantha', quality: 'draft', rate: 165},
};
const html = `<!doctype html><html><style>
body{margin:0;background:#eef2f6;font:24px system-ui;color:#14243b}
main{margin:100px auto;padding:56px;background:white;border-radius:20px;width:900px}
h1{font-size:48px}button{font:inherit;padding:16px 28px;background:#185bd1;color:white;border:0;border-radius:8px}
#detail{padding:28px;background:#e7f4ed;margin-top:28px}
</style><main><p>PRODUCT WALKTHROUGH · SYNTHETIC FIXTURE</p><h1>Review queue</h1>
<p>One request is ready for review.</p><button onclick="document.querySelector('#detail').hidden=false">Open request</button>
<div id="detail" hidden><h2>Request details</h2><p>Evidence is ready. A reviewer makes the next decision.</p></div></main>`;
async function open(page) { await page.setContent(html); }
export const beats = [
  {id:'queue', narration:'The review queue shows a request ready for attention.',
   async run(page) { await open(page); await page.getByRole('heading',{name:'Review queue'}).waitFor(); }},
  {id:'details', narration:'Open the request to see the evidence before making a decision.',
   async run(page) { await open(page); await page.getByRole('button',{name:'Open request'}).click();
     await page.getByRole('heading',{name:'Request details'}).waitFor(); }},
];
