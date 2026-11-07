# Amdahl

**Race Condition** (2001), track 8

[▶ Listen on Suno](https://suno.com/song/6a5171c9-b9de-479e-8883-0b90bb693049)

> The intro is the same eight bars no matter how many musicians join in. That’s the point.

## Lyrics

**[Verse 1]**  
Ten percent of the program has to run one step at a time,  
Ninety percent can split across the cores, and that part’s fine.  
Add a thousand cores and the ninety disappears,  
But the ten percent is waiting, and it’s still here!

**[Chorus]**  
Amdahl’s law! (The serial part!)  
Amdahl’s law! (Breaks your heart!)  
Ten percent alone means ten times is the best you’ll see,  
Amdahl’s law, Amdahl’s law, and the limit’s plain to see!

**[Verse 2]**  
Speedup is the old time over new time on the clock,  
But the part that won’t divide is the part you can’t unlock.  
So grow the problem bigger, Gustafson came to say,  
More cores for bigger jobs, and the serial part fades away!

*[Chorus]*

**[Bridge (rapped)]**  
Two cores! (Faster!) Eight cores! (Faster!)  
A thousand cores! (Not much faster, master!)

**[The serial part: Wyrd]**  
*Wyrd plays one slow eight-bar phrase that only one instrument can play. Around it, the band speeds up and adds more and more parts, but the song can never finish faster than Wyrd’s eight bars.*

**[Final chorus]**  
Amdahl’s law! (The serial part!)  
Amdahl’s law! (Breaks your heart!)  
Ten percent alone means ten times is the best you’ll see,  
Amdahl’s law, Amdahl’s law, and the limit’s plain to see!

## The lesson

Amdahl’s law: if a fraction of a program has to run one step at a time, that fraction limits the speedup no matter how many processors you add. With 10% serial, the best possible speedup is 10 times. Speedup is old time divided by new time. Gustafson’s law points out that with more processors we usually tackle bigger problems, so the parallel part grows and scaling looks much better.

## Suno prompt

**Title**

```
Amdahl
```

**Style of music**

```
2001 nu-metal, heavy plodding riff with one section that never speeds up, 90 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
Ten percent of the program has to run one step at a time,
Ninety percent can split across the cores, and that part’s fine.
Add a thousand cores and the ninety disappears,
But the ten percent is waiting, and it’s still here!

[Chorus: female lead vocal, male shouted backing vocals]
Amdahl’s law! (The serial part!)
Amdahl’s law! (Breaks your heart!)
Ten percent alone means ten times is the best you’ll see,
Amdahl’s law, Amdahl’s law, and the limit’s plain to see!

[Verse 2: female lead vocal]
Speedup is the old time over new time on the clock,
But the part that won’t divide is the part you can’t unlock.
So grow the problem bigger, Gustafson came to say,
More cores for bigger jobs, and the serial part fades away!

[Chorus: female lead vocal, male shouted backing vocals]
Amdahl’s law! (The serial part!)
Amdahl’s law! (Breaks your heart!)
Ten percent alone means ten times is the best you’ll see,
Amdahl’s law, Amdahl’s law, and the limit’s plain to see!

[Bridge: male rap vocals]
Two cores! (Faster!) Eight cores! (Faster!)
A thousand cores! (Not much faster, master!)

[Instrumental Break: one slow eight-bar phrase that never speeds up while the band accelerates around it]

[Final Chorus: female lead vocal, male shouted backing vocals]
Amdahl’s law! (The serial part!)
Amdahl’s law! (Breaks your heart!)
Ten percent alone means ten times is the best you’ll see,
Amdahl’s law, Amdahl’s law, and the limit’s plain to see!

[End]
```
