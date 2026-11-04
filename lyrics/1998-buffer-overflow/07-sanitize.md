# Sanitize

**Buffer Overflow** (1998), track 7

> A callback to Third Normal Form. The database is fine. The input is the problem.

## Lyrics

**[Verse 1]**  
You typed your name into the box and the box believed you,  
But your name had a quote in it and a command or two.  
The program pasted it straight into a query on the fly,  
And the database obeyed it and it never asked why!

**[Chorus]**  
Sanitize! (Never trust the input!)  
Sanitize! (Check it at the door!)  
Every field and every form and every byte from the outside,  
Sanitize, sanitize, and there’s nowhere for the code to hide!

**[Verse 2]**  
Don’t glue the input into commands like it’s a piece of code,  
Use parameters and keep the data on its own road.  
Validate what you expect, reject what you do not,  
Escape it on the way back out or the page will run their plot!

*[Chorus]*

**[Bridge]**  
Name! (A name!) Number! (A number!)  
Anything else! (Rejected!)

**[Synth solo: Wyrd]**  
*Bytes throws a stream of random noise at Wyrd’s synth. Wyrd passes through only the notes that belong in the key and drops everything else before it can reach the rest of the band.*

**[Final chorus]**  
Sanitize! (Never trust the input!)  
Sanitize! (Check it at the door!)  
Every field and every form and every byte from the outside,  
Sanitize, sanitize, and there’s nowhere for the code to hide!

## The lesson

Never trust input that comes from users or other systems. Injection attacks, like SQL injection, happen when input gets pasted into a command and treated as code. Defend by checking input against what you expect, using parameterized queries that keep data separate from code, and escaping output, for example when putting text on a web page.

## Suno prompt

**Title**

```
Sanitize
```

**Style of music**

```
1998 industrial metal with techno crossover, aggressive chugging riff, sharp stop-start breaks, 140 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, synthesizer player on sequencers and acid synth lines, drummer playing live drums over programmed breakbeats and singing male backing vocals, distorted chugging guitars, squelching acid synths, pounding electronic rhythms, processed aggressive vocals, cold digital production
```

**Exclude styles**

```
autotune, trap beats, modern pop, acoustic, lo-fi, country
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, synthesizers and sequencers, live drums over programmed breakbeats with male backing vocals]

[Verse 1: female lead vocal]
You typed your name into the box and the box believed you,
But your name had a quote in it and a command or two.
The program pasted it straight into a query on the fly,
And the database obeyed it and it never asked why!

[Chorus: female lead vocal, male backing vocals]
Sanitize! (Never trust the input!)
Sanitize! (Check it at the door!)
Every field and every form and every byte from the outside,
Sanitize, sanitize, and there’s nowhere for the code to hide!

[Verse 2: female lead vocal]
Don’t glue the input into commands like it’s a piece of code,
Use parameters and keep the data on its own road.
Validate what you expect, reject what you do not,
Escape it on the way back out or the page will run their plot!

[Chorus: female lead vocal, male backing vocals]
Sanitize! (Never trust the input!)
Sanitize! (Check it at the door!)
Every field and every form and every byte from the outside,
Sanitize, sanitize, and there’s nowhere for the code to hide!

[Bridge: female lead vocal, male backing shouts]
Name! (A name!) Number! (A number!)
Anything else! (Rejected!)

[Synth Solo: synth line filtering stray notes out of an incoming stream of noise]

[Final Chorus: female lead vocal, male backing vocals]
Sanitize! (Never trust the input!)
Sanitize! (Check it at the door!)
Every field and every form and every byte from the outside,
Sanitize, sanitize, and there’s nowhere for the code to hide!

[End]
```
