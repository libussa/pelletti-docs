# Extraction style guide (for staging notes)

Goal: clean French technical documentation for a Paradigma Pelletti II
pellet boiler with SystaComfort regulator, rebuilt from scanned manuals.
Output is later merged by topic into a MkDocs Material site.

Rules:
- Read every assigned page IMAGE (the OCR text layer is noisy; use
  `pdftotext -f N -l N` only as a hint for spelling numbers).
- French only. Keep the manual's wording and every technical fact:
  values, units, ranges, defaults, parameter names, menu paths, terminal
  names, fault codes, procedures, warnings. Never invent, guess or
  "improve" a value. Illegible → write `[illisible]`.
- Fix OCR garbage, line breaks, hyphenation. Drop page headers/footers,
  copyright lines, distributor logos, blank pages, tables of contents.
- Structure: `##` per manual chapter, `###` per sub-chapter, keeping
  the manual's numbering in the heading (e.g. `## 7.6 Schéma de câblage
  des sorties PFA II`). After each sub-chapter add a line
  `<small>Source : THFxxxx p. N</small>`.
- Tables → Markdown tables (complete, every row). Lists of parameters →
  table with columns as in the manual (e.g. Paramètre | Plage | Réglage
  usine | Description).
- Warnings/notes → MkDocs admonitions: `!!! danger "Danger"`,
  `!!! warning "Attention"`, `!!! note "Remarque"` (4-space indented body).
- Figures:
  - Wiring/terminal diagrams, menu trees, simple flows that are fully
    expressible as a table or Mermaid → rebuild them (table or
    ```mermaid block).
  - Drawings (dimensions, exploded views, photos, hydraulic schemes,
    board layouts) → crop them:
    `uv run scripts/crop.py "<pdf>" <page> x0 y0 x1 y1 <name>`
    (fractions of page size; look at the page image to choose the box,
    include the figure's legend/numbers; check the result by Reading
    `docs/assets/schemas/<name>.webp`). Name: `<doc>-p<page>-<slug>`
    (lowercase, ascii, dashes). Reference it as
    `![Légende en français](../assets/schemas/<name>.webp)` and
    transcribe the legend (numbered items) as a list under it.
- Write only your staging file and your crops. Do not edit other files.
