"""The World in One Day — 21 November 2026.

make.fun competition news-image-20261121: sum up 21 November 2026's world
news in one image. The image is shipped in this repository as entry.png;
this program copies it to the output directory. Python standard library
only — no third-party imports, because the grading sandbox has nothing
installed.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT_DIR / "entry.png")
