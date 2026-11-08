"""Publish agent-friendly files: raw .md next to each page, llms.txt
(index) and llms-full.txt (every page concatenated)."""
import pathlib
import shutil

_pages = []


def on_page_markdown(markdown, page, config, files):
    _pages.append((page.file.src_uri, page.title, page.meta.get("description", ""), markdown))
    return markdown


def on_post_build(config):
    site = pathlib.Path(config["site_dir"])
    base = config.get("site_url") or "/"
    order = {f: i for i, f in enumerate(_nav_order(config["nav"]))}
    pages = sorted(_pages, key=lambda p: order.get(p[0], 999))
    lines = [f"# {config['site_name']}", "", f"> {config['site_description']}", "",
             "Chaque page existe aussi en Markdown brut (même chemin, extension .md).",
             f"Tout le contenu en un seul fichier : {base}llms-full.txt", "", "## Pages", ""]
    full = []
    for src, title, desc, md in pages:
        shutil.copy(pathlib.Path(config["docs_dir"]) / src, site / src)
        lines.append(f"- [{title}]({base}{src}){': ' + desc if desc else ''}")
        full.append(f"<!-- page: {src} -->\n# {title}\n\n{md}\n")
    (site / "llms.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (site / "llms-full.txt").write_text("\n\n".join(full), encoding="utf-8")
    _pages.clear()


def _nav_order(nav):
    for item in nav:
        for v in (item.values() if isinstance(item, dict) else [item]):
            if isinstance(v, list):
                yield from _nav_order(v)
            else:
                yield v
