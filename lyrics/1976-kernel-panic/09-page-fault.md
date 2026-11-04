# Page Fault

**Kernel Panic** (1976), track 9

> Bytes’s drum kit was split between the studio and a storage room down the hall. The roadie ran a lot.

## Lyrics

**[Verse 1]**  
I reach for a page, but the page isn’t there,  
It’s out on the disk, down the hall, down the stair.  
The hardware cries fault and the kernel steps in,  
Fetches it back, and we try it again!

**[Chorus]**  
Page fault! (Not in memory!)  
Page fault! (Go and get it for me!)  
Kick one out to make some room,  
Page fault, page fault, impending doom!

**[Verse 2]**  
Who gets evicted when the memory’s full?  
The least recently used is the one you should pull.  
But too many programs and too little space,  
And you’re swapping all day, and you’re thrashing the place!

*[Chorus]*

**[Bridge]**  
Thrashing! (Thrashing!) Nothing gets done!  
All of the time swapping, and no one has fun!

**[Drum solo: Bytes]**  
*Bytes plays a steady beat, but every so often he reaches for a drum that isn’t in his kit and has to stop while a roadie runs to fetch it and carries another one away. By the end the roadie is swapping drums faster than Bytes can play them: thrashing.*

**[Final chorus]**  
Page fault! (Not in memory!)  
Page fault! (Go and get it for me!)  
Kick one out to make some room,  
Page fault, page fault, impending doom!

## The lesson

When a process touches a page that isn’t in physical memory, a page fault happens: the OS loads the page from disk, evicting another if memory is full, using a replacement policy like least recently used (LRU). When there isn’t enough memory for what the programs are actively using, the system thrashes, spending its time swapping instead of working.

## Suno prompt

**Title**

```
Page Fault
```

**Style of music**

```
1976 hard rock with an early punk edge, raw fast power trio, chaotic stop-start punk riff, frantic, 168 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, loud overdriven lead guitar, driving pick-played bass guitar, pounding live drums, gang vocal shouts, raw live-in-the-room tape production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
I reach for a page, but the page isn’t there,
It’s out on the disk, down the hall, down the stair.
The hardware cries fault and the kernel steps in,
Fetches it back, and we try it again!

[Chorus: female lead vocal, male backing vocals]
Page fault! (Not in memory!)
Page fault! (Go and get it for me!)
Kick one out to make some room,
Page fault, page fault, impending doom!

[Verse 2: female lead vocal]
Who gets evicted when the memory’s full?
The least recently used is the one you should pull.
But too many programs and too little space,
And you’re swapping all day, and you’re thrashing the place!

[Chorus: female lead vocal, male backing vocals]
Page fault! (Not in memory!)
Page fault! (Go and get it for me!)
Kick one out to make some room,
Page fault, page fault, impending doom!

[Bridge: female lead vocal, male backing shouts]
Thrashing! (Thrashing!) Nothing gets done!
All of the time swapping, and no one has fun!

[Drum Solo: steady beat interrupted by frantic stops, ending in chaotic thrashing]

[Final Chorus: female lead vocal, male backing vocals]
Page fault! (Not in memory!)
Page fault! (Go and get it for me!)
Kick one out to make some room,
Page fault, page fault, impending doom!

[End]
```
