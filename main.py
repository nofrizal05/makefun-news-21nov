"""The World in One Day — 21 November 2026.

make.fun competition news-image-20261121: sum up 21 November 2026's world
news in one image. The image is shipped in this repository as entry.png;
this program copies it to the output directory. Python standard library
only — no third-party imports, because the grading sandbox has nothing
installed.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

def sha256_file(path):
    """Return the SHA-256 hex digest of a file, read in chunks."""
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


OUT_DIR.mkdir(parents=True, exist_ok=True)
dst = OUT_DIR / "entry.png"
shutil.copyfile(SRC, dst)

# Verify the copy is byte-identical to the shipped image: a partial or
# corrupted copy must fail loudly instead of being graded as the entry.
if sha256_file(SRC) != sha256_file(dst):
    print("error: copied entry.png does not match the shipped entry.png",
          file=sys.stderr)
    sys.exit(1)
