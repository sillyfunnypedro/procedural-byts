#!/usr/bin/env python3
"""Add Suno listen links for one album, from a public Suno playlist.

Usage:
    python3 tools/add_suno_links.py <album-slug> <suno-playlist-or-album-url> [--dry-run]
    python3 tools/add_suno_links.py cs1 https://suno.com/playlist/5841f41a-...

What it does:
  * fetches the playlist page and reads each song's /song/<id> link and title
  * matches songs to the album's tracks by title (sunoTitle, then title)
  * data/albums/<year>-<slug>.json: adds "suno" to each song and
    "suno_playlist" to the album
  * docs/albums/<slug>.html: adds the same fields to the embedded SONGS data,
    plus (once per page) the CSS and JS that show the Listen links
  * lyrics/<year>-<slug>/NN-*.md: adds a "Listen on Suno" line
  * docs/index.html: rebuilds the landing page (tools/build_landing.py)

It is safe to re-run: links are replaced, the page patch is applied once.
If any track can't be matched, nothing is written. Override a match with
--song N=https://suno.com/song/<id> (repeatable).
"""
import argparse
import glob
import html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
MARK = "/*suno-links*/"

CSS = (MARK + ".album-listen{margin:-.4rem 0 1rem}"
       ".album-listen a,.setlist a.listen{color:var(--accent);font-weight:700;text-decoration:none}"
       ".album-listen a:hover,.setlist a.listen:hover{text-decoration:underline}"
       ".setlist a.listen{font-size:.85rem;margin-left:.35rem;white-space:nowrap}"
       ".listenbtn{display:block;text-align:center;font-size:1.1rem;font-weight:700;padding:.75rem 1rem;"
       "margin:0 0 .8rem;border:2px solid var(--accent);border-radius:4px;color:var(--accent);text-decoration:none}"
       ".listenbtn:hover{background:var(--accent);color:#fff}\n")

SETLIST_JS = ("li.append(a);" + MARK + "if(s.suno){const l=el('a','listen','▶ Listen');l.href=s.suno;"
              "l.target='_blank';l.rel='noopener';l.setAttribute('aria-label','Listen to '+s.title+' on Suno');"
              "li.append(' ',l)}")
PLAYER_JS = (MARK + "if(s.suno){const l=el('a','listenbtn','▶ Listen on Suno');l.href=s.suno;"
             "l.target='_blank';l.rel='noopener';box.append(l)}box.append(all);")
OLD_SELECTOR = "document.querySelectorAll('#setlist a')"
NEW_SELECTOR = "document.querySelectorAll('#setlist a[href^=\"#\"]')"
SETLIST_H2 = '<h2 id="set-h" class="metal">Setlist</h2>'


def norm(t):
    t = html.unescape(t).lower().replace("’", "'")
    return re.sub(r"[^a-z0-9]+", "", t)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (procedural-byts link tool)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def playlist_songs(page):
    """[(title, url)] in order, from a playlist or album page."""
    out, seen = [], set()
    for sid, title in re.findall(r'href="/song/(' + UUID + r')"[^>]*>([^<]+)</a>', page):
        if sid not in seen:
            seen.add(sid)
            out.append((html.unescape(title).strip(), "https://suno.com/song/" + sid))
    if not out:  # album pages carry the songs only in their embedded data
        data = page.replace('\\"', '"')
        for title, sid in re.findall(r'"title":"([^"]*)",[^{}]{0,300}?"id":"(' + UUID + r')","entity_?[tT]ype":"song_schema"', data):
            if sid not in seen:
                seen.add(sid)
                out.append((html.unescape(title).strip(), "https://suno.com/song/" + sid))
    return out


def patch_page(t, album_songs, playlist_url):
    # 1. embedded SONGS data
    i = t.index("const SONGS=") + len("const SONGS=")
    j = t.index("];\n", i) + 1
    emb = json.loads(t[i:j])
    by_n = {s["n"]: s for s in album_songs}
    for s in emb:
        if by_n.get(s["n"], {}).get("suno"):
            s["suno"] = by_n[s["n"]]["suno"]
    t = t[:i] + json.dumps(emb, ensure_ascii=False) + t[j:]

    # 2. one-time render patch
    if MARK not in t:
        for old in ("li.append(a);", "box.append(all);", OLD_SELECTOR, "</style>", SETLIST_H2):
            if t.count(old) < 1:
                sys.exit(f"page is missing expected code: {old!r}")
        t = t.replace("li.append(a);", SETLIST_JS, 1)
        t = t.replace("box.append(all);", PLAYER_JS, 1)
        t = t.replace(OLD_SELECTOR, NEW_SELECTOR, 1)
        t = t.replace("</style>", CSS + "</style>", 1)

    # 3. whole-album playlist link (replaced on re-run)
    t = re.sub(r'\n<p class="album-listen">.*?</p>', "", t)
    link = (f'\n<p class="album-listen"><a href="{html.escape(playlist_url)}" target="_blank" '
            f'rel="noopener">▶ Play the whole album on Suno</a></p>')
    return t.replace(SETLIST_H2, SETLIST_H2 + link, 1)


def patch_lyrics(path, url):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"\n\n\[▶ Listen on Suno\]\([^)]*\)", "", t)
    m = re.search(r"^\*\*.+\*\* \(\d{4}\), track \d+$", t, re.M)
    if not m:
        print(f"  ! no track line in {os.path.relpath(path, ROOT)}, skipped")
        return None
    return t[:m.end()] + f"\n\n[▶ Listen on Suno]({url})" + t[m.end():]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("playlist")
    ap.add_argument("--song", action="append", default=[], metavar="N=URL")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    data_files = glob.glob(os.path.join(ROOT, "data", "albums", f"*-{a.slug}.json"))
    if len(data_files) != 1:
        sys.exit(f"expected one data/albums/*-{a.slug}.json, found {len(data_files)}")
    data_path = data_files[0]
    page_path = os.path.join(ROOT, "docs", "albums", f"{a.slug}.html")
    lyrics_dir = os.path.join(ROOT, "lyrics", os.path.basename(data_path)[:-5])

    m = re.search(r"(playlist|album)/(" + UUID + ")", a.playlist)
    if not m:
        sys.exit("URL should look like https://suno.com/playlist/<id> or https://suno.com/album/<id>")
    playlist_url = f"https://suno.com/{m.group(1)}/{m.group(2)}"

    album = json.load(open(data_path, encoding="utf-8"))
    found = playlist_songs(fetch(playlist_url))
    if not found:
        sys.exit("no songs found on the playlist page (is it public?)")
    by_title = {}
    for title, url in found:
        by_title.setdefault(norm(title), []).append(url)

    overrides = {}
    for o in a.song:
        n, _, url = o.partition("=")
        if not re.search(r"/song/" + UUID, url):
            sys.exit(f"bad --song {o!r}")
        overrides[int(n)] = url

    problems, used = [], set()
    for s in album["songs"]:
        if s["n"] in overrides:
            s["suno"] = overrides[s["n"]]
        else:
            urls = by_title.get(norm(s.get("sunoTitle", s["title"]))) or by_title.get(norm(s["title"])) or []
            if len(urls) != 1:
                problems.append(f"  track {s['n']} {s['title']!r}: "
                                + ("not in playlist" if not urls else f"{len(urls)} matches: {urls}"))
                continue
            s["suno"] = urls[0]
        used.add(s["suno"])
        print(f"  {s['n']:>2}. {s['title']}  ->  {s['suno']}")
    for title, url in found:
        if url not in used:
            print(f"  note: playlist song not used: {title} {url}")
    if problems:
        sys.exit("Could not match every track; nothing written:\n" + "\n".join(problems)
                 + "\nFix the playlist or pass --song N=URL.")

    album["suno_playlist"] = playlist_url
    writes = {data_path: json.dumps(album, indent=2, ensure_ascii=False),
              page_path: patch_page(open(page_path, encoding="utf-8").read(), album["songs"], playlist_url)}
    for s in album["songs"]:
        hits = glob.glob(os.path.join(lyrics_dir, f"{s['n']:02d}-*.md"))
        if len(hits) == 1:
            new = patch_lyrics(hits[0], s["suno"])
            if new is not None:
                writes[hits[0]] = new

    for path, text in writes.items():
        print(("would write " if a.dry_run else "wrote ") + os.path.relpath(path, ROOT))
        if not a.dry_run:
            open(path, "w", encoding="utf-8").write(text)
    if not a.dry_run:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import build_landing
        print("wrote " + os.path.relpath(build_landing.build(), ROOT))


if __name__ == "__main__":
    main()
