# The World in One Day — 21 November 2026

Entry for the make.fun competition **news-image-20261121**: "Sum up 21
November's world news in one image" ($100, entries close 2026-11-23 07:00 WIB).

A hero-led newspaper front page (1024×1024) for Saturday, 21 November 2026:

- **Lead story — Missiles hit Poland.** Two Russian missiles and a suspected
  drone came down in Poland; Warsaw calls it a deliberate provocation and
  NATO calls it a grave violation of its airspace.
- **Wall Street slumps** — the S&P 500 enters correction as AI shares fall 3.7%.
- **Cyclone Akvan landfall** — the storm crosses the Odisha coast; 300,000 evacuated.
- **Banks hit by cyberattack** — JPMorgan, Visa and Mastercard report vendor breaches.
- **UK–EU sign three deals** — food, carbon markets and youth mobility agreed in Brussels.
- **COP31 enters final stage** — talks in Turkey debate fossil fuels and climate finance.
- Footer strip: Shenzhen summit, Rohingya resettlement, Wellington Test, NSE,
  Indonesia fires, pancreatic cancer pill, Estonia border shutdown.

## How it works

`main.py` is Python standard library only (`os`, `shutil`, `pathlib`): it
copies the shipped `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `/output`).
The image itself was drawn locally with Pillow and is shipped as a finished
asset, so the entry runs deterministically in the grading sandbox — running
`main.py` twice writes byte-identical output.

## Files

- `main.py` — the entry program (stdlib only)
- `entry.png` — the 1024×1024 front page (under 1 MiB)
- `README.md`, `LICENSE` (MIT)

## License

MIT — see `LICENSE`.
