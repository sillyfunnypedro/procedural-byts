# Shared Memory

**Race Condition** (2001), track 3

[▶ Listen on Suno](https://suno.com/song/95e0029e-dbe8-4381-990f-746aa8d3e71f)

> Nyble and Wyrd both recorded into the same bar of tape on this song. Neither knew the other was doing it.

## Lyrics

**[Verse 1]**  
We all live in the same house and we all can read the walls,  
Every thread can see the memory, every thread can make the calls.  
Fast to share, no need to send, just write it and it’s there,  
But when two of us write the same spot, nobody knows who’s where!

**[Chorus]**  
Shared memory! (Everybody sees!)  
Shared memory! (Everybody writes!)  
Easy to share and easy to break in the middle of the night,  
Shared memory, shared memory, and nobody’s right!

**[Verse 2]**  
A thread is a path through the program with its own stack and place,  
But the heap is common ground, a crowded open space.  
Every core has its own cache with a copy of the view,  
And keeping all the copies honest is the hardest thing to do!

*[Chorus]*

**[Bridge (rapped)]**  
Thread one! Thread two! Same address space!  
Cache one! Cache two! Who’s got the latest case?

**[Bass solo: Nyble]**  
*Nyble starts a slap-bass phrase, and halfway through Wyrd’s sampler overwrites the end of it with a different one, because they were both writing to the same bar.*

**[Final chorus]**  
Shared memory! (Everybody sees!)  
Shared memory! (Everybody writes!)  
Easy to share and easy to break in the middle of the night,  
Shared memory, shared memory, and nobody’s right!

## The lesson

Threads in the same process share memory, like the heap and global variables, while each thread has its own stack. Sharing makes communication fast, but writes that aren’t synchronized can collide. Each core also keeps its own cache, and hardware cache coherence keeps those copies consistent; making sure one thread sees another’s writes still needs synchronization.

## Suno prompt

**Title**

```
Shared Memory
```

**Style of music**

```
2001 nu-metal, dark brooding nu-metal, quiet tense verse exploding into the chorus, 92 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
We all live in the same house and we all can read the walls,
Every thread can see the memory, every thread can make the calls.
Fast to share, no need to send, just write it and it’s there,
But when two of us write the same spot, nobody knows who’s where!

[Chorus: female lead vocal, male shouted backing vocals]
Shared memory! (Everybody sees!)
Shared memory! (Everybody writes!)
Easy to share and easy to break in the middle of the night,
Shared memory, shared memory, and nobody’s right!

[Verse 2: female lead vocal]
A thread is a path through the program with its own stack and place,
But the heap is common ground, a crowded open space.
Every core has its own cache with a copy of the view,
And keeping all the copies honest is the hardest thing to do!

[Chorus: female lead vocal, male shouted backing vocals]
Shared memory! (Everybody sees!)
Shared memory! (Everybody writes!)
Easy to share and easy to break in the middle of the night,
Shared memory, shared memory, and nobody’s right!

[Bridge: male rap vocals]
Thread one! Thread two! Same address space!
Cache one! Cache two! Who’s got the latest case?

[Bass Guitar Solo: slap bass phrase overwritten halfway by a sampled phrase]

[Final Chorus: female lead vocal, male shouted backing vocals]
Shared memory! (Everybody sees!)
Shared memory! (Everybody writes!)
Easy to share and easy to break in the middle of the night,
Shared memory, shared memory, and nobody’s right!

[End]
```
