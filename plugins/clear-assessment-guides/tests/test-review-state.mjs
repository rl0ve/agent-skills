import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const html=fs.readFileSync(new URL('../skills/clear-assessment-guides/assets/review-template.html',import.meta.url),'utf8');
const data=JSON.parse(html.match(/<script type="application\/json" id="assessment-data">([\s\S]*?)<\/script>/)[1]);
const core=html.match(/<script id="review-core">([\s\S]*?)<\/script>/)[1];
const ctx=vm.createContext({});vm.runInContext(core+'\nthis.api=ReviewState;',ctx);const {api}=ctx;
api.validateAssessment(data);
const initial=api.empty(data);
initial.set('ISSUE-01',{id:'ISSUE-01',decision:'accept proposal',comment:'Line one\nLine two <script>alert(1)</script>'});
const exported=JSON.parse(JSON.stringify(api.envelope(data,initial)));
const imported=api.validateFeedback(exported,data);
assert.equal(imported.get('ISSUE-01').decision,'accept proposal');
assert.equal(imported.get('ISSUE-01').comment,initial.get('ISSUE-01').comment);
assert.equal(data.issues[0].execution.state,'not started','review acceptance must not change execution');
for(const mutate of [x=>x.assessmentId='other',x=>x.revision='new',x=>x.schemaVersion=2,x=>x.reviews.pop(),x=>x.reviews[1].id='ISSUE-01',x=>x.reviews[0].id='unknown',x=>x.reviews[0].decision='publish',x=>x.reviews[0].comment=15,x=>x.reviews[0].comment='x'.repeat(20001)]){
 const bad=structuredClone(exported);mutate(bad);assert.throws(()=>api.validateFeedback(bad,data));assert.equal(initial.get('ISSUE-01').decision,'accept proposal');
}
const extra=structuredClone(exported);extra.reviews[0].execution={state:'verified live'};assert.equal(api.validateFeedback(extra,data).get('ISSUE-01').execution,undefined,'ignore feedback execution claims');
const duplicate=structuredClone(data);duplicate.issues[1].id=duplicate.issues[0].id;assert.throws(()=>api.validateAssessment(duplicate));
const badEvidence=structuredClone(data);badEvidence.issues[0].evidence=[{src:15,alt:'Example',caption:'Example'}];assert.throws(()=>api.validateAssessment(badEvidence));
for(const script of [...html.matchAll(/<script(?: id="review-core")?>([\s\S]*?)<\/script>/g)]) new vm.Script(script[1]);
console.log('Review feedback: valid round-trip, multiline text, nine invalid-import cases, ignored execution claims, duplicate assessment IDs and invalid evidence verified. Script syntax valid.');
