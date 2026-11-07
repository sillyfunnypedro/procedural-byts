# Lamport Clock

**Race Condition** (2001), track 9

[▶ Listen on Suno](https://suno.com/song/6a1c1e13-4ed9-471c-bba7-f62c7990a976)

> Every member’s tape machine ran at a slightly different speed. The band stopped trying to agree on the time and agreed on the order instead.

## Lyrics

**[Verse 1]**  
Your clock says five, my clock says ten past,  
Neither one is wrong, but neither one will last.  
There’s no single clock that every machine can see,  
So what came first, the message or the reply from me?

**[Chorus]**  
Lamport clock! (Count the events!)  
Lamport clock! (Make it make sense!)  
If it caused it, it came before, and that’s all we need to know,  
Lamport clock, Lamport clock, and the order’s set to go!

**[Verse 2]**  
Keep a counter, add one each time something happens here,  
Send the counter with the message so the order’s clear.  
When you receive, jump ahead past the number that you got,  
Happened-before is all we have, and happened-before is a lot!

*[Chorus]*

**[Bridge (rapped)]**  
Sent it at three! Got it at four!  
Can’t get a message before it’s sent, and that’s the law!

**[Drum solo: Bytes]**  
*Bytes plays two patterns at slightly different tempos on two halves of the kit, and they drift apart. Every time one sends a cue hit, the other jumps ahead to stay after it. They never agree on the time, only on the order.*

**[Final chorus]**  
Lamport clock! (Count the events!)  
Lamport clock! (Make it make sense!)  
If it caused it, it came before, and that’s all we need to know,  
Lamport clock, Lamport clock, and the order’s set to go!

## The lesson

Machines in a distributed system have no single, perfectly shared clock. Lamport’s logical clocks (1978) order events by cause and effect instead, the “happened-before” relation: each process counts its own events, attaches the count to every message it sends, and when it receives a message jumps its count past the one it got. Anything that could have caused something else always gets a smaller timestamp.

## Suno prompt

**Title**

```
Lamport Clock
```

**Style of music**

```
2001 nu-metal, hypnotic off-kilter groove, ticking samples drifting out of sync, 110 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
Your clock says five, my clock says ten past,
Neither one is wrong, but neither one will last.
There’s no single clock that every machine can see,
So what came first, the message or the reply from me?

[Chorus: female lead vocal, male shouted backing vocals]
Lamport clock! (Count the events!)
Lamport clock! (Make it make sense!)
If it caused it, it came before, and that’s all we need to know,
Lamport clock, Lamport clock, and the order’s set to go!

[Verse 2: female lead vocal]
Keep a counter, add one each time something happens here,
Send the counter with the message so the order’s clear.
When you receive, jump ahead past the number that you got,
Happened-before is all we have, and happened-before is a lot!

[Chorus: female lead vocal, male shouted backing vocals]
Lamport clock! (Count the events!)
Lamport clock! (Make it make sense!)
If it caused it, it came before, and that’s all we need to know,
Lamport clock, Lamport clock, and the order’s set to go!

[Bridge: male rap vocals]
Sent it at three! Got it at four!
Can’t get a message before it’s sent, and that’s the law!

[Drum Solo: two patterns at slightly different tempos, kept in order by cue hits]

[Final Chorus: female lead vocal, male shouted backing vocals]
Lamport clock! (Count the events!)
Lamport clock! (Make it make sense!)
If it caused it, it came before, and that’s all we need to know,
Lamport clock, Lamport clock, and the order’s set to go!

[End]
```
