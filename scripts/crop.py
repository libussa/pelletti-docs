"""Crop a figure from a PDF page into docs/assets/schemas/<name>.webp.

usage: crop.py <pdf> <page> <x0> <y0> <x1> <y1> <name>
Box coordinates are fractions (0-1) of page width/height.
"""
import subprocess, sys, tempfile, pathlib
from PIL import Image

pdf, page, x0, y0, x1, y1, name = sys.argv[1:8]
page = int(page)
with tempfile.TemporaryDirectory(dir=pathlib.Path.home() / ".cache") as d:
    out = pathlib.Path(d) / "p"
    subprocess.run(["pdftoppm", "-r", "200", "-png", "-f", str(page),
                    "-l", str(page), "-singlefile", pdf, str(out)], check=True)
    im = Image.open(str(out) + ".png").convert("RGB")
    w, h = im.size
    box = tuple(int(float(v) * s) for v, s in
                zip((x0, y0, x1, y1), (w, h, w, h)))
    dest = pathlib.Path(__file__).resolve().parent.parent / "docs/assets/schemas" / f"{name}.webp"
    im.crop(box).save(dest, "WEBP", quality=80)
    print(dest)
