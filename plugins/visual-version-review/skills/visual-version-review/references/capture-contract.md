# Capture contract

Before capturing, create a project-local manifest. Keep human labels stable across later refreshes; append or update revision identity instead of reusing A for an unrelated approach.

## Minimum manifest fields

```json
{
  "versions": [{
    "id": "B",
    "label": "Geographic approach",
    "repository": "verified repository URL or local identifier",
    "branch": "exact branch",
    "commit": "full resolved commit",
    "entry_path": "prototype/index.html",
    "preview_url": null,
    "evidence_type": "fresh-local",
    "dirty_worktree": false,
    "data_note": "Archived draft content",
    "captures": [{
      "state": "opening",
      "file": "captures/B-opening.png",
      "captured_at": "actual ISO timestamp",
      "viewport": {"width": 1440, "height": 900, "dpr": 1},
      "motion": "reduced",
      "readiness": "fonts, content and globe rendered",
      "crop": null,
      "interaction_verified": false
    }]
  }]
}
```

The example values describe a shape, not facts to copy. Unknown values remain null with an explanation. If a worktree has relevant uncommitted changes, record them or a patch hash; do not attribute the entire render solely to its HEAD commit.

## Select states deliberately

- Opening: initial viewport at a consistent size and scroll position.
- Browsing: comparable list/grid state, not arbitrary full-page offsets.
- Reading: the same detail depth where feasible; distinguish drawer, modal and page.
- Distinctive visual: globe, chart, canvas, timeline or media at a visibly useful state.
- Alternate navigation: flat map versus globe, list versus graph, expanded versus collapsed.
- Responsive: the actual mobile opening and reader; missing historical mobile evidence stays missing.

Use isolated worktrees or existing equivalent folders where safe. Verify folder equivalence rather than assuming matching names imply identical code. Do not launch a backend that regenerates content, calls paid APIs or mutates production just to obtain screenshots.

Preserve original captures and identify crop coordinates. Cropped close-ups help inspect detail but cannot establish relative prominence; include the complete viewport for that comparison. If content differs, explain what can still be compared.

Historical screenshots may be associated with a recovered source version without proving they came from its exact commit. Label that association explicitly. Do not report today's capture date as the historical capture date.
