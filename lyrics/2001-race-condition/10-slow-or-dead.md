# Slow or Dead

**Race Condition** (2001), track 10

[▶ Listen on Suno](https://suno.com/song/d99f5475-333c-4fe0-bbb1-e6ca43cc4a79)

> In the snowstorm that split the tour, the two buses lost contact for two days. Each assumed the other had crashed. Neither had.

## Lyrics

**[Verse 1]**  
I sent a message hours ago and nothing has come back,  
Did it get lost? Is the server down? Did it fall right off the track?  
Maybe it’s just slow, or maybe it’s already dead,  
From here I cannot tell the difference, and that’s the dread!

**[Chorus]**  
Slow or dead? (I can’t tell!)  
Slow or dead? (Ring the bell!)  
In a distributed system some parts fail and some survive,  
Slow or dead, slow or dead, is anybody alive?

**[Verse 2]**  
One machine fails and the rest of them keep going,  
Partial failure, and the others aren’t knowing.  
Set a timeout, take a guess, and plan for being wrong,  
The network isn’t reliable, it never was, so be strong!

*[Chorus]*

**[Bridge (rapped)]**  
The network isn’t reliable! The latency’s not zero!  
The topology will change, and there’s no single hero!

**[Lead guitar break: Qword]**  
*Qword plays a phrase and waits for the band to answer. Nothing. Four bars. Six. Just as Qword gives up and plays the next part alone, the answer arrives, late, right on top of it.*

**[Final chorus]**  
Slow or dead? (I can’t tell!)  
Slow or dead? (Ring the bell!)  
In a distributed system some parts fail and some survive,  
Slow or dead, slow or dead, is anybody alive?

## The lesson

In a distributed system, parts fail independently: one machine can crash while the rest keep running (partial failure). From the outside, a machine that’s slow looks exactly like one that’s dead, so systems use timeouts and have to cope with guessing wrong. The “fallacies of distributed computing” list the false assumptions that cause trouble, like “the network is reliable” and “latency is zero.”

## Suno prompt

**Title**

```
Slow or Dead
```

**Style of music**

```
2001 nu-metal, tense heavy dirge, long silences, sudden explosions, 84 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
I sent a message hours ago and nothing has come back,
Did it get lost? Is the server down? Did it fall right off the track?
Maybe it’s just slow, or maybe it’s already dead,
From here I cannot tell the difference, and that’s the dread!

[Chorus: female lead vocal, male shouted backing vocals]
Slow or dead? (I can’t tell!)
Slow or dead? (Ring the bell!)
In a distributed system some parts fail and some survive,
Slow or dead, slow or dead, is anybody alive?

[Verse 2: female lead vocal]
One machine fails and the rest of them keep going,
Partial failure, and the others aren’t knowing.
Set a timeout, take a guess, and plan for being wrong,
The network isn’t reliable, it never was, so be strong!

[Chorus: female lead vocal, male shouted backing vocals]
Slow or dead? (I can’t tell!)
Slow or dead? (Ring the bell!)
In a distributed system some parts fail and some survive,
Slow or dead, slow or dead, is anybody alive?

[Bridge: male rap vocals]
The network isn’t reliable! The latency’s not zero!
The topology will change, and there’s no single hero!

[Instrumental Break: guitar phrase, long silence, then a late answer arriving on top of the next phrase]

[Final Chorus: female lead vocal, male shouted backing vocals]
Slow or dead? (I can’t tell!)
Slow or dead? (Ring the bell!)
In a distributed system some parts fail and some survive,
Slow or dead, slow or dead, is anybody alive?

[End]
```
