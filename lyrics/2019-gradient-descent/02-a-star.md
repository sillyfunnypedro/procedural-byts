# A Star

**Gradient Descent** (2019), track 2

> The 2019 tour bus finally had a navigation system. Bytes named it after the algorithm inside it.

## Lyrics

**[Verse 1]**  
A maze of rooms and roads, and somewhere there’s a goal,  
Search it breadth by breadth, or dive deep into the hole.  
But a heuristic is a hunch of how far there’s left to go,  
And A star adds the cost so far to what it thinks it knows!

**[Chorus]**  
A star! (Cost so far!)  
A star! (Plus the guess!)  
F equals G plus H, and it finds the shortest way,  
A star, A star, the best route home today!

**[Verse 2]**  
If the guess is never longer than the truth, the answer will be best,  
An admissible heuristic, and it beats out all the rest.  
Straight-line distance on a map is never longer than the road,  
So A star finds the shortest path and doesn’t carry extra load!

*[Chorus]*

**[Bridge]**  
Breadth first! (Every way!) Depth first! (Too deep!)  
Greedy! (Too fast!) A star! (Just right, and cheap!)

**[Lead guitar solo: Qword]**  
*Qword tries a few directions on the neck, guessing which is closest to the target note, then commits to the one with the lowest total cost and lands on the target in the fewest moves.*

**[Final chorus]**  
A star! (Cost so far!)  
A star! (Plus the guess!)  
F equals G plus H, and it finds the shortest way,  
A star, A star, the best route home today!

## The lesson

A lot of AI is search: states, actions and a goal. Uninformed searches like breadth-first and depth-first explore blindly. Informed search uses a heuristic, an estimate of how far is left to go. A* expands the option with the lowest f = g + h, the cost so far plus the estimated cost remaining, and as long as the heuristic never overestimates (straight-line distance on a map, for example), it’s guaranteed to find the shortest path.

## Suno prompt

**Title**

```
A Star
```

**Style of music**

```
2019 synthwave metal, driving synthwave metal, a riff that searches and narrows toward a goal, 128 BPM, lineup: female lead vocalist who also plays bass guitar, lead guitarist playing neon shred solos over synths, synthesizer player on retro analog synthesizers and arpeggios, drummer playing big gated-reverb drums with drum machines and singing male backing vocals, retro-futuristic synth leads, heavy distorted guitars, driving arpeggiated synth bass, cinematic 1980s-inspired production
```

**Exclude styles**

```
autotune, trap beats, country, acoustic, lo-fi, screamed vocals
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, shred lead guitar, retro analog synthesizers, gated-reverb drums and drum machines with male backing vocals]

[Verse 1: female lead vocal]
A maze of rooms and roads, and somewhere there’s a goal,
Search it breadth by breadth, or dive deep into the hole.
But a heuristic is a hunch of how far there’s left to go,
And A star adds the cost so far to what it thinks it knows!

[Chorus: female lead vocal, male backing vocals]
A star! (Cost so far!)
A star! (Plus the guess!)
F equals G plus H, and it finds the shortest way,
A star, A star, the best route home today!

[Verse 2: female lead vocal]
If the guess is never longer than the truth, the answer will be best,
An admissible heuristic, and it beats out all the rest.
Straight-line distance on a map is never longer than the road,
So A star finds the shortest path and doesn’t carry extra load!

[Chorus: female lead vocal, male backing vocals]
A star! (Cost so far!)
A star! (Plus the guess!)
F equals G plus H, and it finds the shortest way,
A star, A star, the best route home today!

[Bridge: female lead vocal, male backing vocals]
Breadth first! (Every way!) Depth first! (Too deep!)
Greedy! (Too fast!) A star! (Just right, and cheap!)

[Lead Guitar Solo: searching phrases that try several directions, then lock onto the shortest path to a target note]

[Final Chorus: female lead vocal, male backing vocals]
A star! (Cost so far!)
A star! (Plus the guess!)
F equals G plus H, and it finds the shortest way,
A star, A star, the best route home today!

[End]
```
