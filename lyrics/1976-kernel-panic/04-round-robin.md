# Round Robin

**Kernel Panic** (1976), track 4

> Each member gets exactly four bars of the solo and then gets cut off, ready or not.

## Lyrics

**[Verse 1]**  
Ten programs and a single CPU,  
Who goes first, and how long till you’re through?  
The scheduler picks and the scheduler decides  
Who gets to run and who waits outside!

**[Chorus]**  
Round robin! (Take your turn!)  
Round robin! (Watch the time slice burn!)  
Run a little while, then the back of the line,  
Round and round, everybody gets their time!

**[Verse 2]**  
First come, first served, and the long one blocks the way,  
Shortest job first, but the long ones never play.  
Priority runs the important ones fast,  
But starve the little guys and they’ll never get past!

*[Chorus]*

**[Bridge]**  
Time’s up! (Time’s up!) The timer says so!  
Preempt the process and let the next one go!

**[Trading solo: whole band]**  
*Byt, Nyble and Bytes take turns with exactly four bars each, three times around. When your time slice ends you stop, even mid-phrase, and the next player goes.*

**[Final chorus]**  
Round robin! (Take your turn!)  
Round robin! (Watch the time slice burn!)  
Run a little while, then the back of the line,  
Round and round, everybody gets their time!

## The lesson

The scheduler decides which process gets the CPU. First come, first served is simple, but long jobs block short ones. Shortest job first cuts waiting but can starve long jobs, and priority scheduling can starve low priorities. Round robin gives every process a time slice and uses a timer interrupt to switch to the next.

## Suno prompt

**Title**

```
Round Robin
```

**Style of music**

```
1976 hard rock with an early punk edge, raw fast power trio, fast rotating punk riff, call-and-response between band members, 160 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, loud overdriven lead guitar, driving pick-played bass guitar, pounding live drums, gang vocal shouts, raw live-in-the-room tape production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
Ten programs and a single CPU,
Who goes first, and how long till you’re through?
The scheduler picks and the scheduler decides
Who gets to run and who waits outside!

[Chorus: female lead vocal, male backing vocals]
Round robin! (Take your turn!)
Round robin! (Watch the time slice burn!)
Run a little while, then the back of the line,
Round and round, everybody gets their time!

[Verse 2: female lead vocal]
First come, first served, and the long one blocks the way,
Shortest job first, but the long ones never play.
Priority runs the important ones fast,
But starve the little guys and they’ll never get past!

[Chorus: female lead vocal, male backing vocals]
Round robin! (Take your turn!)
Round robin! (Watch the time slice burn!)
Run a little while, then the back of the line,
Round and round, everybody gets their time!

[Bridge: female lead vocal, male backing shouts]
Time’s up! (Time’s up!) The timer says so!
Preempt the process and let the next one go!

[Instrumental Break: lead guitar, bass guitar and drums trade strict four-bar solos in rotation]

[Final Chorus: female lead vocal, male backing vocals]
Round robin! (Take your turn!)
Round robin! (Watch the time slice burn!)
Run a little while, then the back of the line,
Round and round, everybody gets their time!

[End]
```
