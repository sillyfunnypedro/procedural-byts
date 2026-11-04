# Race Condition (Nyble First)

**Race Condition** (2001), track 1

> Version one of two. In this version, Nyble’s tape machine started first and the song resolves. The other version is hidden at the end of the album.

## Lyrics

**[Verse 1]**  
Two of us reach for the same thing at the same time,  
I read it, you read it, and we both think it’s fine.  
I write it, you write it, and one of us is lost,  
Whoever gets there last decides, and nobody counts the cost!

**[Chorus]**  
Race condition! (Who got there first?)  
Race condition! (Better or worse?)  
Same code, different timing, a different song each night,  
Race condition, race condition, and nothing comes out right!

**[Verse 2]**  
It works on my machine, it works a thousand times,  
Then once a week it fails and leaves no trace behind.  
It hides when you go looking, it shows up when you’re gone,  
The timing is the bug, and it’s been there all along!

*[Chorus]*

**[Bridge (rapped)]**  
Check, then act! You checked, it changed!  
Read, modify, write, and the value’s rearranged!  
Two threads, one variable, and nobody in charge,  
Make it atomic, or the damage gets large!

**[Turntable solo: Wyrd]**  
*Wyrd plays two copies of the same record on two turntables at once and lets them race. In this version, the left record wins by half a beat, and the song resolves.*

**[Final chorus]**  
Race condition! (Who got there first?)  
Race condition! (Better or worse?)  
Same code, different timing, a different song each night,  
Race condition, race condition, and nothing comes out right!

## The lesson

A race condition happens when a program’s result depends on the timing of things running at the same time. Two threads read the same value, both add one and both write it back, and one update is lost; or a thread checks something and it changes before it acts. Race conditions are intermittent and hard to reproduce: same program, same input, different result. The fix is to make the operation atomic or to synchronize access.

## Suno prompt

**Title**

```
Race Condition (Nyble First)
```

**Style of music**

```
2001 nu-metal, heavy bouncing nu-metal groove, downtuned riff, turntable scratches, 100 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
Two of us reach for the same thing at the same time,
I read it, you read it, and we both think it’s fine.
I write it, you write it, and one of us is lost,
Whoever gets there last decides, and nobody counts the cost!

[Chorus: female lead vocal, male shouted backing vocals]
Race condition! (Who got there first?)
Race condition! (Better or worse?)
Same code, different timing, a different song each night,
Race condition, race condition, and nothing comes out right!

[Verse 2: female lead vocal]
It works on my machine, it works a thousand times,
Then once a week it fails and leaves no trace behind.
It hides when you go looking, it shows up when you’re gone,
The timing is the bug, and it’s been there all along!

[Chorus: female lead vocal, male shouted backing vocals]
Race condition! (Who got there first?)
Race condition! (Better or worse?)
Same code, different timing, a different song each night,
Race condition, race condition, and nothing comes out right!

[Bridge: male rap vocals]
Check, then act! You checked, it changed!
Read, modify, write, and the value’s rearranged!
Two threads, one variable, and nobody in charge,
Make it atomic, or the damage gets large!

[Turntable Solo: two copies of the same record scratched against each other, racing, left one wins]

[Final Chorus: female lead vocal, male shouted backing vocals]
Race condition! (Who got there first?)
Race condition! (Better or worse?)
Same code, different timing, a different song each night,
Race condition, race condition, and nothing comes out right!

[End]
```
