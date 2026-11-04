# CAP

**Race Condition** (2001), track 12

> The theorem was announced in 2000. The band read about it on the tour bus during the snowstorm and wrote this the same night.

## Lyrics

**[Verse 1]**  
The storm cut the line between the buses and the band,  
Two halves that couldn’t talk, and a choice in each hand.  
Keep on playing and risk that we don’t match,  
Or stop until we’re back and leave the crowd with nothing to catch!

**[Chorus]**  
C! (Everyone agrees!)  
A! (Everyone gets an answer!)  
P! (The network splits!)  
And when it splits you choose: agree, or answer!  
CAP! CAP! You can’t have it all,  
Choose what matters when the partitions fall!

**[Verse 2]**  
A bank will choose consistency, it stops instead of lying,  
A shopping cart picks availability and keeps on trying.  
Partitions will happen, so the real choice is clear,  
Correct or always up, when the other side can’t hear!

*[Chorus]*

**[Bridge (rapped)]**  
Two buses! One city! Two shows, same night!  
Both of them were available, and neither one was right!

**[The partition: full band]**  
*The band splits in half, Nyble and Bytes on one side, Qword and Wyrd on the other, each half unable to hear the other. Both keep playing, and drift apart. When they can hear each other again, they stop, compare, and reconcile into one riff.*

**[Final chorus]**  
C! (Everyone agrees!)  
A! (Everyone gets an answer!)  
P! (The network splits!)  
And when it splits you choose: agree, or answer!  
CAP! CAP! You can’t have it all,  
Choose what matters when the partitions fall!

## The lesson

The CAP theorem (Eric Brewer, 2000, proved in 2002) says a distributed data store can’t guarantee all three of consistency (every node sees the same data), availability (every request gets an answer) and partition tolerance (it keeps working when the network splits). Network splits will happen, so during one, a system has to choose between staying consistent and staying available.

## Suno prompt

**Title**

```
CAP
```

**Style of music**

```
2001 nu-metal, massive closing nu-metal anthem, heavy, three-part chanted chorus, 96 BPM, lineup: female lead vocalist who also plays bass guitar, guitarist on downtuned seven-string guitar, DJ on turntables and samples, drummer who raps and shouts male backing vocals, chunky downtuned riffs, groovy bass, turntable scratches, hip-hop-influenced drum grooves, melodic female vocals with male rapped verses, thick heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM drops, country, acoustic, lo-fi, guitar solo
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, downtuned seven-string guitar, turntables and samples, drums with male rapped backing vocals]

[Verse 1: female lead vocal]
The storm cut the line between the buses and the band,
Two halves that couldn’t talk, and a choice in each hand.
Keep on playing and risk that we don’t match,
Or stop until we’re back and leave the crowd with nothing to catch!

[Chorus: female lead vocal, male shouted backing vocals]
C! (Everyone agrees!)
A! (Everyone gets an answer!)
P! (The network splits!)
And when it splits you choose: agree, or answer!
CAP! CAP! You can’t have it all,
Choose what matters when the partitions fall!

[Verse 2: female lead vocal]
A bank will choose consistency, it stops instead of lying,
A shopping cart picks availability and keeps on trying.
Partitions will happen, so the real choice is clear,
Correct or always up, when the other side can’t hear!

[Chorus: female lead vocal, male shouted backing vocals]
C! (Everyone agrees!)
A! (Everyone gets an answer!)
P! (The network splits!)
And when it splits you choose: agree, or answer!
CAP! CAP! You can’t have it all,
Choose what matters when the partitions fall!

[Bridge: male rap vocals]
Two buses! One city! Two shows, same night!
Both of them were available, and neither one was right!

[Instrumental Break: band splits into two halves playing separately, drifting apart, then rejoins and reconciles]

[Final Chorus: female lead vocal, male shouted backing vocals]
C! (Everyone agrees!)
A! (Everyone gets an answer!)
P! (The network splits!)
And when it splits you choose: agree, or answer!
CAP! CAP! You can’t have it all,
Choose what matters when the partitions fall!

[End]
```
