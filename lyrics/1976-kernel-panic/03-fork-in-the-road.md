# Fork in the Road

**Kernel Panic** (1976), track 3

[▶ Listen on Suno](https://suno.com/song/d77d54fd-21e7-4d61-8a58-88a37128896d)

> Byt tried to fork himself during the sessions to play two parts at once. The child process hung around the studio for days eating sandwiches until Nyble reaped it.

## Lyrics

**[Verse 1]**  
A program on the disk is just a list of things to do,  
A process is the program running, living, breathing through.  
It’s got its own memory, its own counter and its stack,  
A number for its name, the PID upon its back!

**[Chorus]**  
Fork in the road! (One becomes two!)  
Fork in the road! (The child looks just like you!)  
The parent goes one way, the child goes the other,  
Fork in the road, and they don’t know each other!

**[Verse 2]**  
Fork gives a zero to the child, the parent gets its name,  
Exec wipes the child clean and gives it a brand-new game.  
The parent waits for the child to finish and to die,  
Or the child becomes a zombie, and you’ll never say goodbye!

*[Chorus]*

**[Bridge]**  
Zombie! (Zombie!) Dead but in the table!  
Reap it with a wait, if you’re able!

**[Twin solo: Byt and Nyble]**  
*Byt plays a phrase, and at the fork Nyble’s bass copies it note for note. Then the two lines split and go their own ways, until Byt stops and waits for Nyble to finish before the last chorus.*

**[Final chorus]**  
Fork in the road! (One becomes two!)  
Fork in the road! (The child looks just like you!)  
The parent goes one way, the child goes the other,  
Fork in the road, and they don’t know each other!

## The lesson

A process is a running program with its own memory, registers, stack and process ID. In Unix, fork() copies the process (it returns 0 to the child and the child’s ID to the parent), exec() replaces the child’s program with a new one, and wait() lets the parent collect the child when it finishes. A finished child nobody waits for becomes a zombie.

## Suno prompt

**Title**

```
Fork in the Road
```

**Style of music**

```
1976 hard rock with an early punk edge, raw fast power trio, driving punk-edged riff that splits into two separate lines, 144 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, loud overdriven lead guitar, driving pick-played bass guitar, pounding live drums, gang vocal shouts, raw live-in-the-room tape production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, polished radio production
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
A program on the disk is just a list of things to do,
A process is the program running, living, breathing through.
It’s got its own memory, its own counter and its stack,
A number for its name, the PID upon its back!

[Chorus: female lead vocal, male backing vocals]
Fork in the road! (One becomes two!)
Fork in the road! (The child looks just like you!)
The parent goes one way, the child goes the other,
Fork in the road, and they don’t know each other!

[Verse 2: female lead vocal]
Fork gives a zero to the child, the parent gets its name,
Exec wipes the child clean and gives it a brand-new game.
The parent waits for the child to finish and to die,
Or the child becomes a zombie, and you’ll never say goodbye!

[Chorus: female lead vocal, male backing vocals]
Fork in the road! (One becomes two!)
Fork in the road! (The child looks just like you!)
The parent goes one way, the child goes the other,
Fork in the road, and they don’t know each other!

[Bridge: female lead vocal, male backing shouts]
Zombie! (Zombie!) Dead but in the table!
Reap it with a wait, if you’re able!

[Instrumental Break: lead guitar and bass guitar play in unison, then split into two separate lines]

[Final Chorus: female lead vocal, male backing vocals]
Fork in the road! (One becomes two!)
Fork in the road! (The child looks just like you!)
The parent goes one way, the child goes the other,
Fork in the road, and they don’t know each other!

[End]
```
