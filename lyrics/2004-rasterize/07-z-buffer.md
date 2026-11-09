# Z-Buffer

**Rasterize** (2004), track 7

[▶ Listen on Suno](https://suno.com/song/86cfd14e-31d2-442b-93ac-5dd434648ca1)

> In the first render of the music video, Bytes appeared in front of Nyble, through his own drum kit. This song fixed it.

## Lyrics

**[Verse 1]**  
Draw them in any order and the far ones cover the near,  
The drummer’s in front of the singer and the stage is out of here.  
Who should we see? Whoever’s closest to the eye,  
Keep a depth for every pixel, and only nearest ones get by!

**[Chorus]**  
Z-buffer! (Who’s in front?)  
Z-buffer! (Closest wins the hunt!)  
Test the depth of every pixel before you paint it on,  
Z-buffer, z-buffer, and the hidden ones are gone!

**[Verse 2]**  
The painter sorts them back to front and paints the near ones last,  
But overlapping triangles won’t sort, and that idea is past.  
The z-buffer doesn’t care what order they arrive,  
Compare the depth, keep the closest, and the picture comes alive!

*[Chorus]*

**[Bridge (screamed)]**  
Nearer? (Draw it!) Farther? (Drop it!)  
Every pixel! (Test it!) Hidden surface! (Stop it!)

**[Front of the mix: Qword and Nyble]**  
*Qword and Nyble play overlapping parts, and at each moment the engineer lets through only whichever one is closer to the front of the mix. The other part is still there, just hidden behind.*

**[Final chorus]**  
Z-buffer! (Who’s in front?)  
Z-buffer! (Closest wins the hunt!)  
Test the depth of every pixel before you paint it on,  
Z-buffer, z-buffer, and the hidden ones are gone!

## The lesson

When surfaces overlap, only the nearest one should show. The painter’s algorithm sorts surfaces and draws them back to front, but fails when surfaces overlap each other in a cycle. The z-buffer, or depth buffer, stores the depth of the nearest surface drawn so far at every pixel, and a new fragment is drawn only if it’s closer. Triangles can then arrive in any order.

## Suno prompt

**Title**

```
Z-Buffer
```

**Style of music**

```
2004 metalcore, heavy layered metalcore, deep pounding breakdowns, 120 BPM, lineup: female lead vocalist singing clean melodic vocals who also plays bass guitar, lead guitarist playing harmonized melodic leads and solos, keyboard player adding atmospheric synths, drummer screaming harsh male backing vocals, palm-muted chugging breakdowns, double-kick drums, clean soaring female choruses against screamed male parts, polished heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM, modern pop, country, acoustic, lo-fi
```

**Lyrics**

```
[Lineup: female clean lead vocals and bass guitar, lead guitar, atmospheric synths, drums with male screamed backing vocals]

[Verse 1: female clean lead vocal]
Draw them in any order and the far ones cover the near,
The drummer’s in front of the singer and the stage is out of here.
Who should we see? Whoever’s closest to the eye,
Keep a depth for every pixel, and only nearest ones get by!

[Chorus: female clean lead vocal, male screamed backing vocals]
Z-buffer! (Who’s in front?)
Z-buffer! (Closest wins the hunt!)
Test the depth of every pixel before you paint it on,
Z-buffer, z-buffer, and the hidden ones are gone!

[Verse 2: female clean lead vocal]
The painter sorts them back to front and paints the near ones last,
But overlapping triangles won’t sort, and that idea is past.
The z-buffer doesn’t care what order they arrive,
Compare the depth, keep the closest, and the picture comes alive!

[Chorus: female clean lead vocal, male screamed backing vocals]
Z-buffer! (Who’s in front?)
Z-buffer! (Closest wins the hunt!)
Test the depth of every pixel before you paint it on,
Z-buffer, z-buffer, and the hidden ones are gone!

[Bridge: male screamed vocals, breakdown]
Nearer? (Draw it!) Farther? (Drop it!)
Every pixel! (Test it!) Hidden surface! (Stop it!)

[Instrumental Break: guitar and bass overlap, with only the nearer-sounding part heard at each moment]

[Final Chorus: female clean lead vocal, male screamed backing vocals]
Z-buffer! (Who’s in front?)
Z-buffer! (Closest wins the hunt!)
Test the depth of every pixel before you paint it on,
Z-buffer, z-buffer, and the hidden ones are gone!

[End]
```
