# Mutex

**Race Condition** (2001), track 4

> The rap verse was supposed to be Bytes’s alone. Nyble kept stepping on it until they agreed to pass the microphone like a lock.

## Lyrics

**[Verse 1]**  
Only one microphone and four of us to sing,  
Grab it, hold it, sing your part, and then give up the thing.  
That’s a mutex, only one inside the room,  
Everybody else waits outside in the gloom!

**[Chorus]**  
Mutex! (Lock it!)  
Mutex! (Unlock it!)  
One at a time in the critical section, the rest wait in line,  
Mutex, mutex, and the data’s fine!

**[Verse 2]**  
Hold the lock too long and the others sit and stare,  
Lock too little and the race is waiting there.  
Atomic operations, one step that can’t be split,  
Compare and swap in one move, and no one interrupts it!

*[Chorus]*

**[Bridge (rapped)]**  
Acquire! (I’m in!) Release! (You’re next!)  
Forget to release and the whole thing’s wrecked!  
Lock two things in different orders and the deadlock’s back,  
Always lock in the same order and you’re on the right track!

**[Drum breakdown: Bytes]**  
*Bytes plays a breakdown where only one drum is allowed to sound at a time. He passes the beat from snare to kick to tom like a lock, and when he tries to hit two at once, he stops himself.*

**[Final chorus]**  
Mutex! (Lock it!)  
Mutex! (Unlock it!)  
One at a time in the critical section, the rest wait in line,  
Mutex, mutex, and the data’s fine!

## The lesson

A mutex (mutual exclusion lock) lets only one thread at a time into a critical section. Hold locks briefly so the other threads aren’t stuck waiting, always release them, and take multiple locks in the same order everywhere to avoid deadlock. Atomic instructions like compare-and-swap update a value in one indivisible step, and they’re the building block underneath locks.

## Suno prompt

**Title**

```
Mutex
```

**Style of music**

```
2001 nu-metal, crushing staccato nu-metal riff, stop-start, 104 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
Only one microphone and four of us to sing,
Grab it, hold it, sing your part, and then give up the thing.
That’s a mutex, only one inside the room,
Everybody else waits outside in the gloom!

[Chorus: female lead vocal, male shouted backing vocals]
Mutex! (Lock it!)
Mutex! (Unlock it!)
One at a time in the critical section, the rest wait in line,
Mutex, mutex, and the data’s fine!

[Verse 2: female lead vocal]
Hold the lock too long and the others sit and stare,
Lock too little and the race is waiting there.
Atomic operations, one step that can’t be split,
Compare and swap in one move, and no one interrupts it!

[Chorus: female lead vocal, male shouted backing vocals]
Mutex! (Lock it!)
Mutex! (Unlock it!)
One at a time in the critical section, the rest wait in line,
Mutex, mutex, and the data’s fine!

[Bridge: male rap vocals]
Acquire! (I’m in!) Release! (You’re next!)
Forget to release and the whole thing’s wrecked!
Lock two things in different orders and the deadlock’s back,
Always lock in the same order and you’re on the right track!

[Drum Solo: breakdown where only one drum sounds at a time, passed around the kit]

[Final Chorus: female lead vocal, male shouted backing vocals]
Mutex! (Lock it!)
Mutex! (Unlock it!)
One at a time in the critical section, the rest wait in line,
Mutex, mutex, and the data’s fine!

[End]
```
