# Chain Reaction

**CS2: Live on the Abstract Data Tour ’85** (1985), track 6

[▶ Listen on Suno](https://suno.com/song/c6605f15-ed57-4eac-b267-898cc0234bf0)

> Written on the tour bus, the Linked List, somewhere between two cities it couldn’t find its way back to.

## Lyrics

**[Stage banter]**  
London! You know how we got here? Our tour bus.  
We call it the Linked List. It only knows where it’s going next.

*[The crowd roars]*

**[Verse 1]**  
Every node holds a value and a link to the next in line,  
A chain of iron rings strung out through space and time.  
Start at the head and follow where it leads,  
Link by link, until null is all it reads!

**[Chorus]**  
Chain reaction! Node to node!  
Follow the pointers down the road!  
Insert at the front in constant time,  
But to find the middle you walk the line!

**[Verse 2]**  
No index here, no jumping to the tenth,  
To find it, you must walk the length.  
Hook the new link first, then unhook the old,  
Or the rest of the chain is lost out in the cold!

*[Chorus]*

**[Bridge]**  
Null pointer! (Null pointer!) You walked off the end!  
Null pointer! (Null pointer!) There’s no next, my friend!  
Doubly linked, a back pointer too,  
Now the chain can walk back home to you!

**[Synth solo: Wyrd]**  
*Wyrd’s sequencer plays one note per node, each note triggering the next. Halfway through, Byt splices a new phrase into the middle of the chain and the arpeggio picks it up without missing a beat.*

**[Final chorus]**  
Chain reaction! Node to node!  
Follow the pointers down the road!  
Insert at the front in constant time,  
But to find the middle you walk the line!

## The lesson

A linked list is a chain of nodes, each holding a value and a reference to the next. Adding at the head is O(1), but reaching position k means walking from the head, O(n). Update links in the right order or you lose the rest of the list. null marks the end; doubly linked lists add a back reference.

## Suno prompt

**Title**

```
Chain Reaction (Live)
```

**Style of music**

```
1985 heavy metal, arena metal, live concert recording, driving relentless riff, sequenced synth bassline, urgent, 144 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, synthesizer and keytar player, drummer singing male backing vocals, harmonized lead guitar, analog polysynth pads and arpeggios, punchy bass guitar, big gated-reverb drums, gang shouts, roaring audience, live arena sound
```

**Exclude styles**

```
autotune, EDM, trap beats, modern pop, lo-fi, dry studio sound
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, synthesizer and keytar, drums with male backing vocals]

[Intro]
[Spoken Word: female voice, live crowd]
London! You know how we got here? Our tour bus.
We call it the Linked List. It only knows where it’s going next.

[Crowd Cheering]

[Verse 1: female lead vocal]
Every node holds a value and a link to the next in line,
A chain of iron rings strung out through space and time.
Start at the head and follow where it leads,
Link by link, until null is all it reads!

[Chorus: female lead vocal, male backing vocals, crowd singing along]
Chain reaction! Node to node!
Follow the pointers down the road!
Insert at the front in constant time,
But to find the middle you walk the line!

[Verse 2: female lead vocal]
No index here, no jumping to the tenth,
To find it, you must walk the length.
Hook the new link first, then unhook the old,
Or the rest of the chain is lost out in the cold!

[Chorus: female lead vocal, male backing vocals, crowd singing along]
Chain reaction! Node to node!
Follow the pointers down the road!
Insert at the front in constant time,
But to find the middle you walk the line!

[Bridge: female lead vocal, male backing shouts]
Null pointer! (Null pointer!) You walked off the end!
Null pointer! (Null pointer!) There’s no next, my friend!
Doubly linked, a back pointer too,
Now the chain can walk back home to you!

[Synth Solo: fast sequenced arpeggio, guitar phrase spliced in]

[Final Chorus: female lead vocal, male backing vocals, crowd singing along]
Chain reaction! Node to node!
Follow the pointers down the road!
Insert at the front in constant time,
But to find the middle you walk the line!

[Crowd Cheering]
[End]
```
