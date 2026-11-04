# Referential Integrity

**Third Normal Form** (1992), track 4

> The first song where the band’s setlists started pointing at each other instead of copying each other.

## Lyrics

**[Verse 1]**  
My table holds the songs and your table holds the shows,  
Your row says song number seven, and that’s how the linking goes.  
A foreign key points over to a key that’s really there,  
Delete the song it points to and it’s pointing at the air!

**[Chorus]**  
Referential integrity! (Point to something real!)  
Referential integrity! (That’s the deal!)  
No reference to nowhere, no orphans in the night,  
Referential integrity, and the links are right!

**[Verse 2]**  
Try to add a show that plays a song that doesn’t exist,  
The database refuses, it’s a constraint upon the list.  
Delete a song that’s still in use and it will stop you cold,  
Or cascade it all away, if that’s what you were told!

*[Chorus]*

**[Bridge]**  
Orphan row! (No parent!) Dangling! (Nowhere to go!)  
Cascade! (Delete them all!) Restrict! (Tell them no!)

**[Organ solo: Wyrd]**  
*Every organ phrase Wyrd plays answers one that Qword has already played. When Qword stops, Wyrd can’t continue, because there’s nothing left to refer to.*

**[Final chorus]**  
Referential integrity! (Point to something real!)  
Referential integrity! (That’s the deal!)  
No reference to nowhere, no orphans in the night,  
Referential integrity, and the links are right!

## The lesson

A foreign key is a column that refers to the primary key of another table, linking rows together. Referential integrity means every foreign key points to a row that really exists. The database rejects inserts that would break that, and when a referenced row is deleted it can refuse, cascade the delete, or set the reference to NULL.

## Suno prompt

**Title**

```
Referential Integrity
```

**Style of music**

```
1992 grunge and alternative metal, tense grinding riff, building pressure, 112 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, organ player on a distorted Hammond organ, drummer singing male backing vocals, sludgy downtuned guitars, loud-quiet-loud dynamics, gritty raw vocals, heavy drums, raw dry production
```

**Exclude styles**

```
synthesizers, shred guitar, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, distorted Hammond organ, drums with male backing vocals]

[Verse 1: female lead vocal]
My table holds the songs and your table holds the shows,
Your row says song number seven, and that’s how the linking goes.
A foreign key points over to a key that’s really there,
Delete the song it points to and it’s pointing at the air!

[Chorus: female lead vocal, male backing vocals]
Referential integrity! (Point to something real!)
Referential integrity! (That’s the deal!)
No reference to nowhere, no orphans in the night,
Referential integrity, and the links are right!

[Verse 2: female lead vocal]
Try to add a show that plays a song that doesn’t exist,
The database refuses, it’s a constraint upon the list.
Delete a song that’s still in use and it will stop you cold,
Or cascade it all away, if that’s what you were told!

[Chorus: female lead vocal, male backing vocals]
Referential integrity! (Point to something real!)
Referential integrity! (That’s the deal!)
No reference to nowhere, no orphans in the night,
Referential integrity, and the links are right!

[Bridge: female lead vocal, male backing shouts]
Orphan row! (No parent!) Dangling! (Nowhere to go!)
Cascade! (Delete them all!) Restrict! (Tell them no!)

[Organ Solo: every phrase answers a phrase from the guitar, and stops when the guitar stops]

[Final Chorus: female lead vocal, male backing vocals]
Referential integrity! (Point to something real!)
Referential integrity! (That’s the deal!)
No reference to nowhere, no orphans in the night,
Referential integrity, and the links are right!

[End]
```
