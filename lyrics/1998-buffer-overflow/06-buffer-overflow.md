# Buffer Overflow

**Buffer Overflow** (1998), track 6

[▶ Listen on Suno](https://suno.com/song/ae1303c6-ad28-4a32-ab12-784559aab51e)

> The title track. The last chorus is deliberately one line too long.

## Lyrics

**[Verse 1]**  
Sixteen bytes of buffer and you hand me thirty-two,  
I copy every one of them, I never check, it’s true.  
The extra spills past the edge onto the memory next door,  
Overwriting what was there, and it’s not what it was before!

**[Chorus]**  
Buffer overflow! (Too much!)  
Buffer overflow! (Over the edge!)  
Write past the end and you write over the rest,  
Buffer overflow, check the length, it’s the only test!

**[Verse 2]**  
Overwrite the return address and the program jumps away,  
Running someone else’s code, and that’s a very bad day.  
Check the bounds on every copy, never trust the size,  
Use a language that won’t let it happen, and you’ll be wise!

*[Chorus]*

**[Bridge]**  
Bounds check! (Bounds check!) Know where the buffer ends!  
Memory safe! (Memory safe!) The language defends!

**[Lead guitar solo: Qword]**  
*Qword’s solo is given eight bars. Qword plays nine. The ninth bar spills into the start of the next verse and overwrites Nyble’s first line, and the band has to stop and restart.*

**[Final chorus]**  
Buffer overflow! (Too much!)  
Buffer overflow! (Over the edge!)  
Write past the end and you write over the rest,  
Buffer overflow, check the length, it’s the only test!  
Buffer overflow!

## The lesson

A buffer overflow writes more data into a fixed-size buffer than it can hold, overwriting the memory next to it. That can crash the program, or let an attacker take control, for example by overwriting the address a function returns to. Prevent it by checking lengths, using safe library functions, and choosing memory-safe languages that check bounds automatically.

## Suno prompt

**Title**

```
Buffer Overflow
```

**Style of music**

```
1998 industrial metal with techno crossover, frantic overloaded industrial riff that spills over its own edges, 160 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, synthesizer player on sequencers and acid synth lines, drummer playing live drums over programmed breakbeats and singing male backing vocals, distorted chugging guitars, squelching acid synths, pounding electronic rhythms, processed aggressive vocals, cold digital production
```

**Exclude styles**

```
autotune, trap beats, modern pop, acoustic, lo-fi, country
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, synthesizers and sequencers, live drums over programmed breakbeats with male backing vocals]

[Verse 1: female lead vocal]
Sixteen bytes of buffer and you hand me thirty-two,
I copy every one of them, I never check, it’s true.
The extra spills past the edge onto the memory next door,
Overwriting what was there, and it’s not what it was before!

[Chorus: female lead vocal, male backing vocals]
Buffer overflow! (Too much!)
Buffer overflow! (Over the edge!)
Write past the end and you write over the rest,
Buffer overflow, check the length, it’s the only test!

[Verse 2: female lead vocal]
Overwrite the return address and the program jumps away,
Running someone else’s code, and that’s a very bad day.
Check the bounds on every copy, never trust the size,
Use a language that won’t let it happen, and you’ll be wise!

[Chorus: female lead vocal, male backing vocals]
Buffer overflow! (Too much!)
Buffer overflow! (Over the edge!)
Write past the end and you write over the rest,
Buffer overflow, check the length, it’s the only test!

[Bridge: female lead vocal, male backing shouts]
Bounds check! (Bounds check!) Know where the buffer ends!
Memory safe! (Memory safe!) The language defends!

[Lead Guitar Solo: fast phrase that runs one bar past its end and crashes into the next section]

[Final Chorus: female lead vocal, male backing vocals]
Buffer overflow! (Too much!)
Buffer overflow! (Over the edge!)
Write past the end and you write over the rest,
Buffer overflow, check the length, it’s the only test!
Buffer overflow!

[End]
```
