# Manifest and commands

Each capture output contains a portable version-1 manifest. Video and screenshot
paths resolve relative to the manifest; audio is named ID.wav in a separate folder.
IDs use lowercase letters, numbers, hyphens and underscores. Width/height are even
positive integers. Node resolves Playwright from the current project package.json,
or the package.json given by `PLAYWRIGHT_PACKAGE`. This is a package location, not
a browser executable. `settings.channel` chooses an installed Playwright channel;
the example uses `msedge`. Explicit `channel: "chromium"` needs the Playwright browser
installed. Respect host restrictions and the user's browser choice.

```json
{
  "version": 1,
  "width": 1440,
  "height": 900,
  "fps": 30,
  "voice": {
    "provider": "openai",
    "quality": "polished",
    "model": "gpt-4o-mini-tts",
    "voice": "coral",
    "instructions": "Clear, calm, conversational product walkthrough."
  },
  "beats": [{
    "id": "open-request",
    "narration": "Open the request to review its evidence.",
    "video": "open-request/capture.webm",
    "screenshot": "open-request/evidence.png"
  }]
}
```

Use provider `elevenlabs` with explicit `model`, `voice` (voice ID), and optional
`voice_settings` object. Use `local` with optional installed `voice` and words-per-
minute `rate` (default 165). Use `provided` for another provider or human narration.
The included adapter does not interpret `quality` as an API parameter; it records
the target. It supports OpenAI `instructions` and `speed`, or ElevenLabs
`voice_settings`, without claiming these are interchangeable.

Optional `cues` per beat: `[{"start":0,"end":2.1,"text":"Open the request."}]`.
Times are seconds relative to that beat's narration. Supply aligned cues from a
provider or transcription tool for final caption accuracy. Without cues the renderer
proportionally estimates phrase timing and flags this in the timeline. It does not
perform speech recognition. Empty or overlapping supplied cues fail validation.

Custom capture backends may populate this manifest with actual video paths. The
assembler accepts footage with any FFmpeg-decodable video format. A snapshot-only
backend must first render stills into clips and explicitly label the resulting
walkthrough as a slideshow. It must not claim continuous UI navigation was filmed.

Outputs are non-destructive: commands refuse existing destination directories.
For voice revisions, keep capture and create another audio/render directory. For
partial paid failures, successful ID.wav files remain; generate only missing IDs
with a reduced manifest in a fresh directory, then combine the WAVs for assembly.
Never blindly repeat a failed paid request without checking whether it was billed.

Audio settings in timeline.json come from the manifest. When supplying external
WAVs, change `voice` to describe their actual origin. Keep private scripts, recordings,
API responses and credentials out of distributable skill packages.

Failed captures retain manifest.partial.json and failure.json identifying the last
completed beat and failing beat. Inspect raw footage only for diagnosis; fix the
flow and capture into a new directory. Supplied beat.cues survive capture and are
validated by the assembler against measured narration.
