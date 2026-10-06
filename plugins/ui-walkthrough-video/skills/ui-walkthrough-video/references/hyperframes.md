# Optional HyperFrames production

Reviewed 2026-10-06. HyperFrames renders HTML/CSS and seek-safe GSAP alongside real
footage. It supplies composition, not evidence that a product action was performed.
Ask for the user's choice before installation, project creation or rendering.
An earlier choice for another video is not blanket opt-in; reuse the choice for
revisions of the same project. Composition does not authorize paid media or publishing.

## Plan before picture

| Treatment | Direction |
| --- | --- |
| Tutorial | Establish context, show a complete action, hold its result, explain the next step. Speech and reading time govern cuts. |
| Product demo | Move between overview and details, reveal what explains the task, and finish on its observed outcome. |
| Teaser | Short product moments with a measured music grid and a clear final action. Music is separately requested; 128 BPM is an example, not a default. |

Keep accepted wording in SCRIPT.md. Generate/audition narration first, measure
its length and import alignment before binding visual time. Reuse approved audio
for visual revisions. For an unnarrated teaser, choose the score first and measure
its beats rather than trusting a BPM prompt.

Copy [STORYBOARD.template.md](../assets/STORYBOARD.template.md) and
[storyboard.example.json](../assets/storyboard.example.json). Bind global time to
real source ranges, speech cues, audio offsets, focal rectangles and transition seams.
The example's coordinates assume 1920×1080 footage; replace them with measured
source dimensions and observed targets. Startup markers need an explicit `sourceStart`.
The bundled template hard-cuts scenes. Custom match cuts require authored motion
and inspection on both sides of the editorial cut-rectangle contract.

The builder supports contiguous scenes, measured media, camera paths, phrase captions
and word-triggered highlights. A `cueOverlays` entry is
`{"wordIndex":2,"duration":1.2,"rect":[620,120,420,200]}`. Its word index references
the scene's sidecar and its rectangle uses source pixels. A highlight does not
retime a real action. Use captured cursor motion or separately verified telemetry;
never invent hover states or overlay a duplicate pointer.

## Build and iterate

After the user selects HyperFrames, run from a project containing the real sources:

```sh
python3 /path/to/skill/scripts/compose_hyperframes.py storyboard.json composition-01 --opt-in
cd composition-01
# Requires Node >=22, an available Chrome and FFmpeg.
export HYPERFRAMES_NO_UPDATE_CHECK=1 HYPERFRAMES_SKIP_SKILLS=1
npm ci --ignore-scripts --no-audit --no-fund
npm run lint
npm run check -- --at 0,1,11.983,12,12.017,23.983 --at-transitions
npm run snapshot -- --at 0,1,11.983,12,12.017,23.983
npm run render -- --output draft.mp4 --quality draft
python3 /path/to/skill/scripts/verify_video.py draft.mp4 review-01 --timeline timeline.json
```

`--opt-in` records a prior choice; the flag cannot grant permission by itself. The
builder never installs, records, renders or generates paid media. It validates
source length, speech duration, scene continuity, layout and timing before creating
a fresh project. It cannot infer whether the footage establishes a product claim.
The template pins HyperFrames 0.8.137 and GSAP 3.14.2 with a lockfile. Repeat the
proof when deliberately upgrading. The earlier 0.8.29 trials remain historical.
Consult the installed CLI `--help`/`doctor` before changing browser/GPU settings;
do not install another browser implicitly. Begin with one render worker.
Check browser availability before rendering: the CLI may otherwise download its
preferred headless shell. For existing compatible installations it supports
`HYPERFRAMES_BROWSER_PATH`. Inspect compiler warnings about sparse keyframes;
prepare a separate seek-friendly footage derivative when needed (for example
H.264 with one-second keyframes), preserving the original and source-time mapping.

Snapshot's optional cloud description is disabled in the package script. Do not
enable paid/cloud analysis incidentally during local QA. No preview server, upload
or publication is required for lint/check/snapshot/render.

## Speech, music and portrait

ElevenLabs `voice.timestamps: true` requests character timing and saves `ID.words.json`.
The helper prefers normalized alignment and groups real boundaries into words.
It does not force-align existing audio. Other providers/human narration can supply
a version-1 sidecar with `timing: "forced-alignment"` or `"supplied-alignment"` and
`words: [{"word":"Review","start":0.2,"end":0.6}]`. These times reference the
unchanged audio file. Revoicing/trimming requires updated alignment. Check normalized
wording against the approved script, especially numbers and respellings. Explicit
captions take precedence. Without alignment/cues the authored template emits no
estimated captions; the older renderers retain their labeled fallback.

Music/SFX require a separate request and authorized local assets in `audioTracks`:

```json
[
  {"kind":"music","file":"audio/score.wav","start":0,"duration":24,
   "volume":0.12,"duckGain":0.25},
  {"kind":"sfx","file":"audio/reveal.wav","start":12,"duration":0.4,"volume":0.2}
]
```

Gains are linear. Optional music ducking creates a derivative with a 0.2s attack
and 0.4s release around speech, preserving the original. Values above are starting
points, not perceptual balancing. The helper does not generate assets, detect beats,
EQ or limit the final mix. Listen and measure final loudness/true peak. Choose a
delivery target (for example -16 LUFS and <=-1 dBTP); finish a separate derivative
when needed and disclose edits baked into the MP4 rather than editable source.

Author landscape and portrait as separate storyboards. Change canvas size and
`rect/titleRect/captionRect` plus focal points for actual viewing size. Portrait
may need split surfaces or reconstructed panels: extend HTML deliberately and
verify it. An aspect-ratio switch alone does not establish readable portrait UI.

## Fidelity and acceptance

Use captured UI for actions/results. Reconstruction is conditional on faithful
assets, exact strings and recorded provenance/coverage. Label reconstructed and
illustrative scenes; do not represent them as live navigation. Reuse real product
components/tokens/logos. Avoid decorative HUD, invented counters or product behavior.

For elaborate scenes, consult upstream core/keyframe/animation skills rather than
guessing. Keep paused, registered timelines with explicit positions and `fromTo`
endpoints. HyperFrames owns media playback/visibility. No wall-clock motion,
random state or manual media seeking. Compare forward/backward/random-seek frames.

Draft a short proof first. Inspect UI readability, camera edges, caption zones,
motion midpoints, action/results, both sides of cuts and the ending. The verifier
fully decodes, measures specs/loudness/true peak, flags black/frozen intervals and
extracts seam/idle frames. Flags need inspection: a static UI hold may be deliberate.
Visual and listening reviews remain pending in its report. A successful render
does not prove natural speech or cinematic quality; compare identical footage/audio.

Package index.html, scenes/, package/lock files, storyboard.json, timeline.json, SRT, all
media/ and additional brand/script assets, review evidence and MP4. The packaged
storyboard points to copied assets for rebuilding a new take. Reopen, seek and
rerender the packaged copy. HTML source is editable; Cap/Recordly native tracks
require a separate verified handoff.

Public sources reviewed 2026-10-06: [HyperFrames](https://github.com/heygen-com/hyperframes),
[GSAP](https://hyperframes.heygen.com/guides/gsap-animation),
[media schema](https://hyperframes.heygen.com/reference/html-schema),
[ElevenLabs timing](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps),
[music plans](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans).
Local trial evidence is recorded separately in VALIDATION.md. Private thread
content and external prompts are not packaged.
