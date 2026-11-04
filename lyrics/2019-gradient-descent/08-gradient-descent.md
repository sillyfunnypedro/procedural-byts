# Gradient Descent

**Gradient Descent** (2019), track 8

> The title track. The melody walks downhill one step at a time and lands on the lowest note on the album.

## Lyrics

**[Verse 1]**  
I’m standing on a mountain in the dark, and I want the valley floor,  
I can’t see the bottom, but I feel the slope, and that’s what I’m looking for.  
Take a step downhill, then feel the ground again,  
Step by step the error falls, and the model learns, and then…

**[Chorus]**  
Gradient descent! (Step down!)  
Gradient descent! (Lower ground!)  
Measure the loss, find the slope, and take a step the other way,  
Gradient descent, gradient descent, a little better every day!

**[Verse 2]**  
The learning rate’s the step size, and too big you jump right past,  
Too small and you’ll be walking down that mountain till the last.  
Backpropagation sends the error back through every weight,  
Every weight gets nudged a bit, and the model’s doing great!

*[Chorus]*

**[Bridge]**  
Loss! (How wrong?) Gradient! (Which way?)  
Step! (Downhill!) Repeat! (All day!)  
Local minimum! (Stuck in a dip!) Try again! (Another trip!)

**[Lead guitar solo: Qword]**  
*Qword walks the solo down the neck one step at a time, feeling for the lowest note. Once, Qword takes too big a step and overshoots, climbs back, then takes smaller steps until landing on the lowest note on the album.*

**[Final chorus]**  
Gradient descent! (Step down!)  
Gradient descent! (Lower ground!)  
Measure the loss, find the slope, and take a step the other way,  
Gradient descent, gradient descent, a little better every day!

## The lesson

Training a model means minimizing a loss function that measures how wrong it is. Gradient descent works out the gradient, the slope of the loss for every parameter, and takes a small step in the opposite direction, again and again. The learning rate sets the step size: too big and you overshoot, too small and it takes forever. Backpropagation calculates all those gradients efficiently through the layers of a network. Training can settle in a local minimum, though in very large networks that turns out to matter less than people once feared.

## Suno prompt

**Title**

```
Gradient Descent
```

**Style of music**

```
2019 synthwave metal, epic descending synthwave metal anthem, stepping down to a resolution, 120 BPM, lineup: female lead vocalist who also plays bass guitar, lead guitarist playing neon shred solos over synths, synthesizer player on retro analog synthesizers and arpeggios, drummer playing big gated-reverb drums with drum machines and singing male backing vocals, retro-futuristic synth leads, heavy distorted guitars, driving arpeggiated synth bass, cinematic 1980s-inspired production
```

**Exclude styles**

```
autotune, trap beats, country, acoustic, lo-fi, screamed vocals
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, shred lead guitar, retro analog synthesizers, gated-reverb drums and drum machines with male backing vocals]

[Verse 1: female lead vocal]
I’m standing on a mountain in the dark, and I want the valley floor,
I can’t see the bottom, but I feel the slope, and that’s what I’m looking for.
Take a step downhill, then feel the ground again,
Step by step the error falls, and the model learns, and then…

[Chorus: female lead vocal, male backing vocals]
Gradient descent! (Step down!)
Gradient descent! (Lower ground!)
Measure the loss, find the slope, and take a step the other way,
Gradient descent, gradient descent, a little better every day!

[Verse 2: female lead vocal]
The learning rate’s the step size, and too big you jump right past,
Too small and you’ll be walking down that mountain till the last.
Backpropagation sends the error back through every weight,
Every weight gets nudged a bit, and the model’s doing great!

[Chorus: female lead vocal, male backing vocals]
Gradient descent! (Step down!)
Gradient descent! (Lower ground!)
Measure the loss, find the slope, and take a step the other way,
Gradient descent, gradient descent, a little better every day!

[Bridge: female lead vocal, male backing vocals]
Loss! (How wrong?) Gradient! (Which way?)
Step! (Downhill!) Repeat! (All day!)
Local minimum! (Stuck in a dip!) Try again! (Another trip!)

[Lead Guitar Solo: descending melody stepping down note by note, overshooting once, then settling on the lowest note]

[Final Chorus: female lead vocal, male backing vocals]
Gradient descent! (Step down!)
Gradient descent! (Lower ground!)
Measure the loss, find the slope, and take a step the other way,
Gradient descent, gradient descent, a little better every day!

[End]
```
