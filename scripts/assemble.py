"""Assemble topic pages in docs/ from staging/*.md section slices."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ST = ROOT / "staging"
DOCS = ROOT / "docs"
DOCNAME = {"inst": "THF1849", "regul": "THF1777", "tech": "THF1751", "user": "THF1848"}


def load(prefix):
    text = "\n".join((ST / f).read_text() for f in sorted(p.name for p in ST.glob(prefix + "*.md")))
    secs, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^(##|###) (\d+(?:\.\d+)?)\.? ", line)
        if m and cur == "simplifiees" and line.startswith("### "):
            secs[cur].append(line)  # numbered steps inside the quick guide
        elif m:
            cur = m.group(2)
            if "(suite)" in line and cur in secs:
                continue  # continuation heading of an already open section
            secs.setdefault(cur, [])
            secs[cur].append(line)
        elif re.match(r"^##? ", line) and not line.startswith("## Instructions simplifiées"):
            cur = None if line.startswith("# ") else line
            if cur:
                secs.setdefault(cur, []).append(line)
        elif line.startswith("## Instructions simplifiées"):
            cur = "simplifiees"
            secs.setdefault(cur, []).append(line)
        elif cur:
            secs[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in secs.items()}


S = {k: load(k) for k in DOCNAME}


def pick(doc, *keys, demote=0, chapters=True):
    """Return sections; a chapter key 'N' also pulls every 'N.x' unless chapters=False."""
    out = []
    for k in keys:
        names = [k] + ([n for n in S[doc] if n.startswith(k + ".")] if chapters and "." not in k else [])
        for n in names:
            if n not in S[doc]:
                raise SystemExit(f"missing {doc} {n}")
            body = S[doc][n]
            if demote:
                body = re.sub(r"^(#+)", lambda m: m.group(1)[:-demote] if len(m.group(1)) > 2 else m.group(1), body, flags=re.M)
            out.append(body)
    return "\n\n".join(out)


def page(path, title, desc, sources, *parts, intro=""):
    fm = f"---\ntitle: {json.dumps(title, ensure_ascii=False)}\ndescription: {json.dumps(desc, ensure_ascii=False)}\nsources: [{', '.join(sources)}]\n---\n\n# {title}\n\n"
    if intro:
        fm += intro.strip() + "\n\n"
    p = DOCS / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm + "\n\n".join(x for x in parts if x) + "\n")


KEYS_PFA = S["inst"]["9"].split("\n")[0] if False else ""
NOTE_KEYS_PFA = ('!!! note "Notation des touches"\n'
                 "    Le manuel représente les touches du module de commande par des pictogrammes. "
                 "Notation utilisée ici : **OK** = niveau de menu inférieur, **ESC** = niveau de menu "
                 "supérieur, **▼ / ▲** = se déplacer dans un menu, **− / +** = modifier les valeurs.")


def dup(note):
    return f'!!! info "Voir aussi"\n    {note}'


# --- Chaudière Pelletti II --------------------------------------------------
page("chaudiere/description.md", "Description de la chaudière",
     "Structure de la Pelletti II, variantes d'alimentation en granulés, combustible.",
     ["THF1849 p. 7-10", "THF1848 p. 10"],
     pick("inst", "5.1", "5.2", "5.3", "5.4", "5.5", "5.6"), pick("user", "4.7"))
page("chaudiere/caracteristiques.md", "Dimensions et données techniques",
     "Fiches de dimensions et tableaux de données techniques Pelletti II (vis sans fin et aspiration).",
     ["THF1849 p. 10-14"],
     pick("inst", "5.7", "5.8", "5.9", "5.10", "5.11", "5.12", "5.13"))

# --- Installation ------------------------------------------------------------
page("installation/mise-en-place.md", "Mise en place et montage",
     "Distances minimales, convoyeur ascendant, montage chaudière, habillages, inversion brûleur, dispositif de nettoyage.",
     ["THF1849 p. 15-24"], pick("inst", "6"))
page("installation/electricite.md", "Installation électrique (PFA II)",
     "Commande automatique du brûleur PFA II : fusibles, câblage, plots de connexion, entrées/sorties, liaison LON.",
     ["THF1849 p. 24-36"],
     pick("inst", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "7.10", "7.11", "7.12"),
     dup("Schémas de câblage détaillés par connecteur : [Câblage PFA II](../depannage/cablage-pfa.md). "
         "Tables des sondes : [Sondes de température](../depannage/sondes.md)."))
page("installation/fumees.md", "Système de gaz d'échappement et air de combustion",
     "Dimensionnement du conduit, exemples de montage, fonctionnement indépendant de l'air ambiant.",
     ["THF1849 p. 36-40"], pick("inst", "8"))
page("installation/hydraulique.md", "Système hydraulique",
     "Réglage du débit volumétrique et relevage de la température de retour.",
     ["THF1849 p. 40-41"], pick("inst", "9"))
page("installation/mise-en-service.md", "Première mise en service",
     "Mise en service de la chaudière (vis sans fin, aspiration) et réglage de la sonde de capacité.",
     ["THF1849 p. 57-59"], pick("inst", "22"))

# --- Utilisation -------------------------------------------------------------
page("utilisation/instructions-simplifiees.md", "Instructions simplifiées",
     "Fiche rapide : commande, marche/arrêt du brûleur, fonction Entretien, décendrage.",
     ["THF1848 p. 2"], re.sub(r"^###", "##", S["user"]["simplifiees"].split("\n", 1)[1], flags=re.M))
page("utilisation/fonctionnement.md", "Fonctionnement au quotidien",
     "Fonctionnement normal, absence prolongée, coupure de courant, pannes, mise hors service, décendrage.",
     ["THF1848 p. 10-13"], pick("user", "5"), pick("user", "4.8"))
page("utilisation/module-commande.md", "Module de commande de la chaudière",
     "Menus du module de commande Pelletti II : affichage, fonction Entretien, températures, compteurs, heure, paramètres de l'installation.",
     ["THF1849 p. 41-47, 56"],
     pick("inst", "10", "11", "12", "13", "14", "15", "16"), pick("inst", "21"), intro=NOTE_KEYS_PFA)

# --- Paramètres ---------------------------------------------------------------
page("parametres/chaudiere.md", "Paramètres de la chaudière (niveaux de service)",
     "Niveau de service Code 12 et niveau avancé Code 42 : tous les paramètres avec plage et réglage usine.",
     ["THF1849 p. 48-55", "THF1848 p. 19"],
     pick("inst", "17"), pick("inst", "20"),
     "## Aperçu des paramètres (instructions utilisateur)\n\n" + pick("user", "16", demote=1).split("\n", 1)[1]
     + '\n\n!!! note "Remarque"\n    Écart entre manuels : les instructions utilisateur (THF1848) donnent '
       '`Vitesse KP` 33 % (plage 33 - 100 %), les manuels technicien THF1849 et THF1751 '
       'donnent 100 % (plage 25 - 100 %).',
     intro=NOTE_KEYS_PFA)

# --- Entretien ----------------------------------------------------------------
page("entretien/entretien.md", "Entretien de la chaudière",
     "Kit de nettoyage, pièces concernées, entretien de la chaudière, du brûleur, du convoyeur et du système d'aspiration.",
     ["THF1751 p. 3-11"], pick("tech", "2.2"), pick("tech", "3"))
page("entretien/combustion.md", "Analyse des gaz d'échappement et réglage de la combustion",
     "Mesure des émissions, réglage qualité de combustion et température des fumées, valeurs de référence.",
     ["THF1751 p. 11-13"], pick("tech", "4"))

# --- Dépannage ----------------------------------------------------------------
page("depannage/codes-panne.md", "Codes de panne de la chaudière",
     "Déblocage, historique des pannes, tableau des codes de panne PFA II avec causes et remèdes détaillés, pannes sans affichage.",
     ["THF1849 p. 51-53", "THF1751 p. 14-23"],
     pick("inst", "18"), pick("inst", "19"),
     "## Diagnostic détaillé (instructions d'entretien THF1751)\n\n"
     + pick("tech", "6.1", "6.2", "6.3"), intro=NOTE_KEYS_PFA)
page("depannage/sondes.md", "Sondes de température : tables de résistance",
     "Tables résistance/température des sondes Pt1000 et NTC (chaudière) et des sondes SystaComfort.",
     ["THF1849 p. 35-36", "THF1751 p. 23-24", "THF1777 p. 41"],
     pick("inst", "7.13"),
     "## Sondes du régulateur SystaComfort\n\n" + pick("regul", "12.1", demote=1).split("\n", 1)[1],
     dup("Le manuel d'entretien THF1751 (§ 6.4) reprend les mêmes tables Pt1000/NTC sur une plage plus large :\n\n"
         + "\n".join("    " + l if l else "" for l in pick("tech", "6.4", demote=1).splitlines()[1:]) ))
page("depannage/cablage-pfa.md", "Schémas de câblage PFA II",
     "Schémas de câblage par connecteur de la commande automatique du brûleur PFA II.",
     ["THF1751 p. 25-27"], pick("tech", "7"))

# --- Régulation SystaComfort --------------------------------------------------
NOTE_KEYS_SC = ('!!! note "Notation des touches"\n'
                "    ⊕ / ⊖ (plus / moins), △ / ▽ (haut / bas), ⇩ (double flèche vers le bas : niveau "
                "de menu inférieur / 2e niveau de commande), ⇧ (double flèche vers le haut : niveau "
                "supérieur / affichage par défaut).")
page("regulation/fonctions.md", "Fonctions du régulateur SystaComfort",
     "Modes, programmes horaires, courbe de chauffe, chape, eau chaude, protections, compteurs.",
     ["THF1777 p. 5-11"], pick("regul", "3"))
page("regulation/montage-raccordement.md", "Montage et raccordement électrique du SystaComfort",
     "Montage du régulateur et de la commande, adressage, bornier, sondes, bus, consommateurs, fusible.",
     ["THF1777 p. 11-17"], pick("regul", "4"), pick("regul", "5"))
page("regulation/mise-en-service.md", "Mise en service du SystaComfort",
     "Commande et affichage, contrôle des sondes et bus, réglage des circuits de chauffage, tampon, circulation, tests.",
     ["THF1777 p. 17-31"], pick("regul", "6"), intro=NOTE_KEYS_SC)
page("regulation/fonctionnement-pannes.md", "Fonctionnement, pannes et remplacement (SystaComfort)",
     "Fonctionnement normal, absence, codes de panne du régulateur, entretien, remplacement de pièces.",
     ["THF1777 p. 31-39"], pick("regul", "7", "8", "9", "10"), intro=NOTE_KEYS_SC)
page("regulation/valeurs-defaut.md", "Valeurs par défaut et courbes de chauffe (SystaComfort)",
     "Tableau complet des valeurs par défaut, courbe de chauffe, données techniques du régulateur.",
     ["THF1777 p. 39-41"], pick("regul", "11"), pick("regul", "12", chapters=False))
page("regulation/apercu-commandes.md", "Aperçu des commandes (SystaComfort)",
     "Arborescence complète des menus du SystaComfort (1er et 2e niveau) et procédures de réglage.",
     ["THF1777 p. 42-55"], S["regul"]["13"], intro=NOTE_KEYS_SC)

# --- Référence ---------------------------------------------------------------
page("reference/securite-normes.md", "Sécurité, normes et garantie",
     "Consignes de sécurité, identification de l'appareil, normes et conditions de garantie.",
     ["THF1849 p. 4-6", "THF1777 p. 4"],
     pick("inst", "1", "2", "3", "4"),
     "## Régulateur SystaComfort : sécurité\n\n" + pick("regul", "2.1", "2.2"))
print("ok")
