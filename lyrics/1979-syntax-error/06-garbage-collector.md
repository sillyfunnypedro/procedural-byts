# Garbage Collector

**Syntax Error** (1979), track 6

> Side A. The last song on Side A, and the last guitar Byt plays until the final track.

## Lyrics

**[Verse 1]**  
New object, new object, filling up the heap,  
Every time you make one there’s another one to keep.  
But some of them are orphans and nobody holds their hand,  
No reference points to them, they’re garbage on the land!

**[Chorus]**  
Garbage collector! Coming in the night!  
Garbage collector! Clear the heap tonight!  
Start at the roots and mark what you can reach,  
Sweep away the rest, that’s the sermon that I preach!

**[Verse 2]**  
In C you free it by hand, every byte you take,  
Forget and it’s a leak, free it twice and it’s a break!  
The collector does it for you, but it takes a little time,  
A pause to sweep the heap, a small price for the crime!

*[Chorus]*

**[Bridge]**  
Mark! (Reachable!) Sweep! (Unreachable!)  
Count the references! (Zero and it’s gone!)

**[Lead guitar solo: Byt]**  
*Byt fills the solo with more and more notes until there’s barely room. Then he stops, keeps only the handful still connected to the main melody, and sweeps the rest away into silence.*

**[Final chorus]**  
Garbage collector! Coming in the night!  
Garbage collector! Clear the heap tonight!  
Start at the roots and mark what you can reach,  
Sweep away the rest, that’s the sermon that I preach!

## The lesson

Objects live on the heap. In languages like C, programmers free memory by hand, risking leaks and double frees. A garbage collector frees unreachable objects automatically: mark-and-sweep marks everything reachable from the roots and sweeps away the rest, while reference counting frees an object when nothing refers to it. Collection costs some pause time in exchange for safety.

## Suno prompt

**Title**

```
Garbage Collector
```

**Style of music**

```
1979 new wave of British heavy metal, NWOBHM, power trio, heavy relentless riff, menacing, 138 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, sharp overdriven lead guitar, galloping bass lines, fast hard-hitting drums, raw energetic production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
New object, new object, filling up the heap,
Every time you make one there’s another one to keep.
But some of them are orphans and nobody holds their hand,
No reference points to them, they’re garbage on the land!

[Chorus: female lead vocal, male backing vocals]
Garbage collector! Coming in the night!
Garbage collector! Clear the heap tonight!
Start at the roots and mark what you can reach,
Sweep away the rest, that’s the sermon that I preach!

[Verse 2: female lead vocal]
In C you free it by hand, every byte you take,
Forget and it’s a leak, free it twice and it’s a break!
The collector does it for you, but it takes a little time,
A pause to sweep the heap, a small price for the crime!

[Chorus: female lead vocal, male backing vocals]
Garbage collector! Coming in the night!
Garbage collector! Clear the heap tonight!
Start at the roots and mark what you can reach,
Sweep away the rest, that’s the sermon that I preach!

[Bridge: female lead vocal, male backing shouts]
Mark! (Reachable!) Sweep! (Unreachable!)
Count the references! (Zero and it’s gone!)

[Lead Guitar Solo: dense flurry of notes, then a sudden sweep to silence leaving a few held notes]

[Final Chorus: female lead vocal, male backing vocals]
Garbage collector! Coming in the night!
Garbage collector! Clear the heap tonight!
Start at the roots and mark what you can reach,
Sweep away the rest, that’s the sermon that I preach!

[End]
```
