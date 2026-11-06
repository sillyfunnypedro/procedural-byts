#!/usr/bin/env python3
"""Build docs/index.html, the landing page: one table row per album, with
its playlist link (or "Coming soon"), from data/albums/*.json.

Usage: python3 tools/build_landing.py
add_suno_links.py runs this automatically after adding an album.
"""
import glob
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "index.html")
e = html.escape

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Procedural Byts</title>
<meta name="description" content="Procedural Byts: a fictional metal band whose albums cover the computer science curriculum, one decade and one genre at a time. Every album, ready to play.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Metal+Mania&family=Spectral:ital,wght@0,400;0,600;1,400&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#e8e4ea;--ink:#21152a;--muted:#62566c;--accent:#9c2a1e;--accent2:#1f4f9c;--panel:#f6f3f7;--rule:#c8bfce;--onaccent:#fff;color-scheme:light;box-sizing:border-box}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#120b12;--ink:#ece3dc;--muted:#a8999f;--accent:#ee6a4a;--accent2:#7cb6ff;--panel:#1d1320;--rule:#352737;--onaccent:#120b12;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#120b12;--ink:#ece3dc;--muted:#a8999f;--accent:#ee6a4a;--accent2:#7cb6ff;--panel:#1d1320;--rule:#352737;--onaccent:#120b12;color-scheme:dark}
*,*::before,*::after{box-sizing:inherit}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Spectral",Georgia,serif;font-size:1.0625rem;line-height:1.5}
.wrap{max-width:52rem;margin:0 auto;padding:2.5rem 1rem 4rem}
.metal{font-family:"Metal Mania",Impact,fantasy;font-weight:400}
.cond{font-family:"Barlow Condensed","Arial Narrow",sans-serif;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
a{color:var(--accent2)}
h1{font-size:clamp(3rem,14vw,5.2rem);line-height:.95;margin:0;color:var(--accent)}
.sub{margin:.7rem 0 1rem;max-width:38rem}
nav{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;margin:0 0 2rem;font-size:.95rem}
nav a{color:var(--accent);text-decoration:none}
nav a:hover{text-decoration:underline}
table{width:100%;border-collapse:collapse}
thead th{text-align:left;font-size:.85rem;color:var(--muted);padding:.4rem .6rem;border-bottom:2px solid var(--ink)}
tbody td{padding:.7rem .6rem;border-bottom:1px solid var(--rule);vertical-align:middle}
tbody tr:hover{background:var(--panel)}
.yr{font-family:"Barlow Condensed","Arial Narrow",sans-serif;font-weight:700;font-size:1.15rem;color:var(--accent2);width:3.5rem}
.al a{color:var(--ink);font-weight:600;text-decoration-color:var(--rule);text-underline-offset:3px}
.al a:hover{color:var(--accent)}
.al small{display:block;color:var(--muted);font-style:italic;font-size:.88rem}
.cv{color:var(--ink)}
.go{text-align:right;white-space:nowrap}
.play{display:inline-block;font-family:"Barlow Condensed","Arial Narrow",sans-serif;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
 font-size:.95rem;padding:.35rem .8rem;border-radius:4px;background:var(--accent);color:var(--onaccent);text-decoration:none}
.play:hover{filter:brightness(1.12)}
.soon{color:var(--muted);font-style:italic;font-size:.9rem}
.note{color:var(--muted);font-size:.95rem;margin-top:1.6rem}
footer{margin-top:3rem;text-align:center;color:var(--muted);font-style:italic}
a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (max-width:36rem){
 thead{display:none}
 table,tbody,tr,td{display:block}
 tbody tr{display:grid;grid-template-columns:3.2rem 1fr auto;grid-template-areas:"yr al go" "yr cv go";column-gap:.6rem;padding:.75rem 0;border-bottom:1px solid var(--rule)}
 tbody td{padding:0;border:0}
 .yr{grid-area:yr;width:auto}.al{grid-area:al}.cv{grid-area:cv;font-size:.95rem}.go{grid-area:go;align-self:center}
}
</style>
</head>
<body>
<main class="wrap">
<h1 class="metal">Procedural Byts</h1>
<p class="sub">A fictional metal band whose albums cover the computer science curriculum, one decade and one genre at a time. Every song teaches one concept. Pick an album and press play.</p>
<nav class="cond" aria-label="Site"><a href="about.html">The band &amp; full discography</a><a href="making-of.html">The making of</a></nav>

<table>
<thead><tr class="cond"><th>Year</th><th>Album</th><th>What it covers</th><th class="go">Listen</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
<p class="note">Play opens the album on Suno. Click an album name for its lyrics, lessons and liner notes.</p>

<footer><p class="metal" style="font-size:1.5rem;margin:0;font-style:normal">Procedural Byts</p><p>{ready} of {total} albums ready to play.</p></footer>
</main>
</body>
</html>
"""


def row(a):
    genre = re.sub(r"^\d{4}s?\s+", "", a["genre"])
    genre = genre[:1].upper() + genre[1:]
    if a.get("suno_playlist"):
        go = (f'<a class="play" href="{e(a["suno_playlist"])}" target="_blank" rel="noopener" '
              f'aria-label="Play {e(a["title"])} on Suno">▶ Play</a>')
    else:
        go = '<span class="soon">Coming soon</span>'
    return (f'<tr><td class="yr">{a["year"]}</td>'
            f'<td class="al"><a href="albums/{e(a["slug"])}.html">{e(a["title"])}</a><small>{e(genre)}</small></td>'
            f'<td class="cv">{e(a["knowledge_area"])}</td><td class="go">{go}</td></tr>')


def build():
    albums = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(os.path.join(ROOT, "data", "albums", "*.json")))]
    albums.sort(key=lambda a: a["year"])
    page = (PAGE.replace("{rows}", "\n".join(row(a) for a in albums))
                .replace("{ready}", str(sum(1 for a in albums if a.get("suno_playlist"))))
                .replace("{total}", str(len(albums))))
    open(OUT, "w", encoding="utf-8").write(page)
    return OUT


if __name__ == "__main__":
    print("wrote " + os.path.relpath(build(), ROOT))
