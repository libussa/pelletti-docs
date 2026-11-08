# Documentation chaudière Pelletti II

Site statique (MkDocs Material) de la documentation technique de la
chaudière à granulés Paradigma Pelletti II R 203 et du régulateur
SystaComfort, reconstruite à partir des manuels papier numérisés.

- Contenu : `docs/` (Markdown), schémas dans `docs/assets/schemas/`.
- Pour les agents : `/llms.txt`, `/llms-full.txt`, et chaque page en
  `.md` brut (générés par `hooks/llms.py`).
- Construction locale : `uv run mkdocs serve` (dépendances dans
  `pyproject.toml` / `uv.lock`).
- Netlify : `netlify.toml` (installe uv, `uv sync --frozen`, puis
  `mkdocs build --strict`, publie `site/`).

`scripts/assemble.py` a généré les pages thématiques à partir des notes
d'extraction (non versionnées) ; les pages de `docs/` sont désormais la
source à modifier directement. `uv run scripts/crop.py` découpe un schéma dans
un PDF.
