---
name: chaudiere-pelletti
description: Answer questions about the user's pellet boiler (chaudière à granulés Paradigma Pelletti II R 203, burner control PFA II, heating regulator SystaComfort) from its documentation site systa.libussa.net. Use for any question about this boiler or its heating installation - fault codes (code panne), cleaning and maintenance (entretien, décendrage), parameters and menus, heating curve, sensors (sondes, Pt1000, NTC), wiring, combustion, installation. French or English.
---

# Chaudière Pelletti II

The user's boiler: **Paradigma Pelletti II R 203**, 20 kW, built 2010,
types FC 43x / FC 53x, burner control **PFA II**, heating regulator
**SystaComfort**. Its full technical documentation, rebuilt in French
from the original manuals, is at https://systa.libussa.net.

## How to read the docs

1. Fetch https://systa.libussa.net/llms.txt: one line per page with a
   summary.
2. Fetch only the pages you need as raw Markdown: same path with `.md`,
   e.g. https://systa.libussa.net/depannage/codes-panne.md.
3. Avoid `llms-full.txt` (whole site, ~100k tokens) unless your fetch
   tool handles large files without truncating or summarising.

Shortcuts:

| Question | Page |
|---|---|
| Fault code on the boiler display | `depannage/codes-panne.md` |
| Fault code on the SystaComfort | `regulation/fonctionnement-pannes.md` |
| Boiler parameters (codes 12 / 42), defaults | `parametres/chaudiere.md` |
| Boiler menus and display | `utilisation/module-commande.md` |
| Heating curve, time programmes | `regulation/fonctions.md`, `regulation/apercu-commandes.md` |
| Cleaning / maintenance | `entretien/entretien.md`, `utilisation/instructions-simplifiees.md` |
| Sensor resistance check | `depannage/sondes.md` |
| Wiring, terminals, fuses | `installation/electricite.md`, `depannage/cablage-pfa.md` |

## Rules

- Answer from the docs only. Quote values exactly (units, ranges,
  defaults) and cite the page URL and the source the page gives
  (manual code THFxxxx + page).
- When manuals disagree, the technician manuals (THF1849, THF1751,
  THF1777) take precedence over the user manual (THF1848), but say
  that they disagree.
- Notes marked « sic » or « Écart » flag errors in the original
  manuals: mention them instead of silently picking a value.
- If the docs do not cover the question, say so; do not fill in from
  general knowledge without labelling it as such.
- For electrical work or the safety thermostat (STB), repeat the
  manual's safety warning: work by a qualified technician.
