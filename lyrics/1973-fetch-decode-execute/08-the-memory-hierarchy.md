# The Memory Hierarchy

**Fetch, Decode, Execute** (1973), track 8

> The longest song on the album. It gets slower every verse, on purpose.

## Lyrics

**[Verse 1]**  
At the top, the registers, fast and very few,  
Then the cache, then the main memory, waiting just for you.  
Down below, the disk drive spins, a giant slow and wide,  
Every step is bigger, but it’s slower down inside.

**[Chorus]**  
Down the memory hierarchy!  
Faster at the top, but smaller, you see!  
Bigger as you go down, but you wait and wait,  
Keep what you need up high, or you’ll be late!

**[Verse 2]**  
Locality, locality, the secret of the speed,  
Use it once, you’ll use it soon, and what’s next door you’ll need.  
Time and space, the cache keeps what you touched before,  
A hit is like the lightning, but a miss goes to the floor!

*[Chorus]*

**[Bridge]**  
Cache hit! (Fast!) Cache miss! (Slow!)  
Walk the array in order and watch the cache glow!

**[Lead guitar solo: Byt]**  
*Byt starts at the very top of the neck, blindingly fast, and works his way down. Every octave lower, the notes get heavier and slower, until the solo ends on one long low note that takes forever to arrive: the disk.*

**[Final chorus]**  
Down the memory hierarchy!  
Faster at the top, but smaller, you see!  
Bigger as you go down, but you wait and wait,  
Keep what you need up high, or you’ll be late!

## The lesson

Memory is a hierarchy: registers, cache, main memory and disk, each level bigger, cheaper and slower than the one above. Caches work because of locality: recently used data tends to be used again (temporal), and nearby data tends to be used soon (spatial). Hits are fast, misses fall through to slower levels, and walking data in order is cache-friendly.

## Suno prompt

**Title**

```
The Memory Hierarchy
```

**Style of music**

```
1973 heavy blues rock, hard rock power trio, epic slow-building, layered riffs that get heavier as the song descends, 84 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, thick overdriven blues guitar, heavy grooving bass guitar, big loose live drums, analog tape warmth
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
At the top, the registers, fast and very few,
Then the cache, then the main memory, waiting just for you.
Down below, the disk drive spins, a giant slow and wide,
Every step is bigger, but it’s slower down inside.

[Chorus: female lead vocal, male backing vocals]
Down the memory hierarchy!
Faster at the top, but smaller, you see!
Bigger as you go down, but you wait and wait,
Keep what you need up high, or you’ll be late!

[Verse 2: female lead vocal]
Locality, locality, the secret of the speed,
Use it once, you’ll use it soon, and what’s next door you’ll need.
Time and space, the cache keeps what you touched before,
A hit is like the lightning, but a miss goes to the floor!

[Chorus: female lead vocal, male backing vocals]
Down the memory hierarchy!
Faster at the top, but smaller, you see!
Bigger as you go down, but you wait and wait,
Keep what you need up high, or you’ll be late!

[Bridge: female lead vocal, male backing shouts]
Cache hit! (Fast!) Cache miss! (Slow!)
Walk the array in order and watch the cache glow!

[Lead Guitar Solo: starts high and fast, descends to slow heavy low notes]

[Final Chorus: female lead vocal, male backing vocals]
Down the memory hierarchy!
Faster at the top, but smaller, you see!
Bigger as you go down, but you wait and wait,
Keep what you need up high, or you’ll be late!

[End]
```
