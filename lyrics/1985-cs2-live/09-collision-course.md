# Collision Course

**CS2: Live on the Abstract Data Tour ’85** (1985), track 9

> Inspired by the Hashville hotel, which put Byt and Bytes in the same room. Collision resolved by chaining. Byt slept in the bathtub.

## Lyrics

**[Stage banter]**  
Hashville, Tennessee! True story:  
The hotel put Byt and Bytes in the same room. Hash collision!  
Byt slept in the bathtub. This one’s called Collision Course!

*[The crowd roars]*

**[Verse 1]**  
Give me a key and I’ll hash it into code,  
Mod it by the table size to find the right abode.  
No searching every room, no walking down the hall,  
Straight to the bucket, the fastest of them all!

**[Chorus]**  
Collision course! Two keys, one place!  
Collision course! Fighting for the space!  
Chain them together or probe for the next,  
Constant time on average, that’s what you’d expect!

**[Verse 2]**  
A good hash spreads them evenly across the floor,  
A bad one piles them up behind a single door.  
When the table’s filling up and the load factor’s near,  
Resize and rehash, and the crowd will cheer!

*[Chorus]*

**[Synth solo: Wyrd]**  
*Wyrd’s arpeggio leaps straight to scattered notes instead of climbing a scale, landing on each instantly. Twice it hits the same note as Byt’s guitar, and the two collide and chain into a harmony.*

**[Bridge]**  
Equals and hashCode! (Must agree!)  
Equals and hashCode! (Or you’ll never be free!)  
If two keys are equal, their hashes must match,  
Or the map won’t find you, there’s a bug in the batch!

**[Final chorus]**  
Collision course! Two keys, one place!  
Collision course! Fighting for the space!  
Chain them together or probe for the next,  
Constant time on average, that’s what you’d expect!

## The lesson

A hash table turns a key into a bucket index with a hash function (mod the table size), giving O(1) lookups on average. Collisions are handled by chaining or probing, and the table resizes when the load factor gets high. In Java, equal objects must have equal hashCode() values.

## Suno prompt

**Title**

```
Collision Course (Live)
```

**Style of music**

```
1985 heavy metal, arena metal, live concert recording, fast pounding, laser synth stabs, chaotic energy, 158 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, synthesizer and keytar player, drummer singing male backing vocals, harmonized lead guitar, analog polysynth pads and arpeggios, punchy bass guitar, big gated-reverb drums, gang shouts, roaring audience, live arena sound
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
Hashville, Tennessee! True story:
The hotel put Byt and Bytes in the same room. Hash collision!
Byt slept in the bathtub. This one’s called Collision Course!

[Crowd Cheering]

[Verse 1: female lead vocal]
Give me a key and I’ll hash it into code,
Mod it by the table size to find the right abode.
No searching every room, no walking down the hall,
Straight to the bucket, the fastest of them all!

[Chorus: female lead vocal, male backing vocals, crowd singing along]
Collision course! Two keys, one place!
Collision course! Fighting for the space!
Chain them together or probe for the next,
Constant time on average, that’s what you’d expect!

[Verse 2: female lead vocal]
A good hash spreads them evenly across the floor,
A bad one piles them up behind a single door.
When the table’s filling up and the load factor’s near,
Resize and rehash, and the crowd will cheer!

[Chorus: female lead vocal, male backing vocals, crowd singing along]
Collision course! Two keys, one place!
Collision course! Fighting for the space!
Chain them together or probe for the next,
Constant time on average, that’s what you’d expect!

[Synth Solo: rapid jumping arpeggio, laser stabs]

[Bridge: female lead vocal, male backing shouts]
Equals and hashCode! (Must agree!)
Equals and hashCode! (Or you’ll never be free!)
If two keys are equal, their hashes must match,
Or the map won’t find you, there’s a bug in the batch!

[Final Chorus: female lead vocal, male backing vocals, crowd singing along]
Collision course! Two keys, one place!
Collision course! Fighting for the space!
Chain them together or probe for the next,
Constant time on average, that’s what you’d expect!

[Crowd Cheering]
[End]
```
