# Message Passing

**Race Condition** (2001), track 6

> Recorded with Nyble and Bytes in different cities, sending parts back and forth. They had done this before, in 1982.

## Lyrics

**[Verse 1]**  
No shared house this time, we each live on our own,  
Every process has its memory, every process is alone.  
If I want you to know something, I have to send it through,  
A message on the wire from me straight to you!

**[Chorus]**  
Message passing! (Send it!)  
Message passing! (Receive it!)  
Nothing shared and nothing broken, every copy is our own,  
Message passing, message passing, and we’re never alone!

**[Verse 2]**  
Send and receive, the receiver waits until it’s there,  
Copy what you need, and there’s no memory to share.  
It scales across a room of machines, a building or the sea,  
A thousand processes talking, and not a lock to see!

*[Chorus]*

**[Bridge (rapped)]**  
Send! (To you!) Receive! (From me!)  
No locks, no races, just messages, see?

**[Call and answer: Nyble and Bytes]**  
*Nyble sends a phrase on the bass, and Bytes waits until he’s received all of it before sending his reply on the drums. They never play at the same time and never step on each other.*

**[Final chorus]**  
Message passing! (Send it!)  
Message passing! (Receive it!)  
Nothing shared and nothing broken, every copy is our own,  
Message passing, message passing, and we’re never alone!

## The lesson

In message passing, processes don’t share memory at all. They communicate by sending and receiving messages, as in MPI, the standard from 1994. There are no shared-variable races, it scales across many machines, and every bit of communication is explicit, at the cost of copying data and waiting for messages to arrive.

## Suno prompt

**Title**

```
Message Passing
```

**Style of music**

```
2001 nu-metal, driving nu-metal riff with call-and-response between two vocalists, 116 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
No shared house this time, we each live on our own,
Every process has its memory, every process is alone.
If I want you to know something, I have to send it through,
A message on the wire from me straight to you!

[Chorus: female lead vocal, male shouted backing vocals]
Message passing! (Send it!)
Message passing! (Receive it!)
Nothing shared and nothing broken, every copy is our own,
Message passing, message passing, and we’re never alone!

[Verse 2: female lead vocal]
Send and receive, the receiver waits until it’s there,
Copy what you need, and there’s no memory to share.
It scales across a room of machines, a building or the sea,
A thousand processes talking, and not a lock to see!

[Chorus: female lead vocal, male shouted backing vocals]
Message passing! (Send it!)
Message passing! (Receive it!)
Nothing shared and nothing broken, every copy is our own,
Message passing, message passing, and we’re never alone!

[Bridge: male rap vocals]
Send! (To you!) Receive! (From me!)
No locks, no races, just messages, see?

[Instrumental Break: bass guitar and drums exchange phrases, each waiting to receive the whole phrase before replying]

[Final Chorus: female lead vocal, male shouted backing vocals]
Message passing! (Send it!)
Message passing! (Receive it!)
Nothing shared and nothing broken, every copy is our own,
Message passing, message passing, and we’re never alone!

[End]
```
