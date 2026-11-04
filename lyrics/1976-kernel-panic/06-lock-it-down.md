# Lock It Down

**Kernel Panic** (1976), track 6

> The studio had one good microphone. This song is about that microphone.

## Lyrics

**[Verse 1]**  
Two programs reach for the same number at the same time,  
Both of them read it, both add one, and only one makes the line.  
The total should be two, but it’s only one again,  
The critical section needs a guard at the gate, my friend!

**[Chorus]**  
Lock it down! (Only one inside!)  
Lock it down! (The rest wait outside!)  
Grab the lock, do the work, then let it go,  
Mutual exclusion, one at a time, you know!

**[Verse 2]**  
A semaphore counts how many can get through,  
A mutex is a key, and there’s only one for you.  
Forget to unlock and the others wait for good,  
Lock too much and nothing moves the way it should!

*[Chorus]*

**[Bridge]**  
Race condition! (Who got there first?)  
Lock the critical section, or the data’s cursed!

**[Bass solo: Nyble]**  
*Only one instrument may hold the melody at a time. Nyble holds it, hands it to Byt, then takes it back. Once, they both grab it at the same time, and the clash is so ugly they never do it again.*

**[Final chorus]**  
Lock it down! (Only one inside!)  
Lock it down! (The rest wait outside!)  
Grab the lock, do the work, then let it go,  
Mutual exclusion, one at a time, you know!

## The lesson

When processes or threads share data, a race condition can corrupt it: two increments can turn into one. The code that touches shared data is a critical section. A mutex (a lock) lets only one in at a time, and a semaphore counts how many can enter. Always release your locks, and lock only what you need.

## Suno prompt

**Title**

```
Lock It Down
```

**Style of music**

```
1976 hard rock with an early punk edge, raw fast power trio, tense chugging riff, heavy and tight, 118 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, loud overdriven lead guitar, driving pick-played bass guitar, pounding live drums, gang vocal shouts, raw live-in-the-room tape production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
Two programs reach for the same number at the same time,
Both of them read it, both add one, and only one makes the line.
The total should be two, but it’s only one again,
The critical section needs a guard at the gate, my friend!

[Chorus: female lead vocal, male backing vocals]
Lock it down! (Only one inside!)
Lock it down! (The rest wait outside!)
Grab the lock, do the work, then let it go,
Mutual exclusion, one at a time, you know!

[Verse 2: female lead vocal]
A semaphore counts how many can get through,
A mutex is a key, and there’s only one for you.
Forget to unlock and the others wait for good,
Lock too much and nothing moves the way it should!

[Chorus: female lead vocal, male backing vocals]
Lock it down! (Only one inside!)
Lock it down! (The rest wait outside!)
Grab the lock, do the work, then let it go,
Mutual exclusion, one at a time, you know!

[Bridge: female lead vocal, male backing shouts]
Race condition! (Who got there first?)
Lock the critical section, or the data’s cursed!

[Bass Guitar Solo: melody passed back and forth with the lead guitar, never both at once]

[Final Chorus: female lead vocal, male backing vocals]
Lock it down! (Only one inside!)
Lock it down! (The rest wait outside!)
Grab the lock, do the work, then let it go,
Mutual exclusion, one at a time, you know!

[End]
```
