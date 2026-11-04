# Bresenham

**Rasterize** (2004), track 1

> The first thing Wyrd ever drew on a computer screen, back in 1985, was a single straight line. The album starts there because everything on a screen does.

## Lyrics

**[Verse 1]**  
A screen is just a grid of squares, no curves and no between,  
Draw a line from here to there across the pixel screen.  
Step along the x one square at a time,  
And choose the pixel closest to the line!

**[Chorus]**  
Bresenham! (Step by step!)  
Bresenham! (Error kept!)  
Add the slope to the error, and when it’s more than half you climb,  
Bresenham, Bresenham, integers every time!

**[Verse 2]**  
No floating point, no division, nothing but add and compare,  
Nineteen sixty-two, a plotter pen moving through the air.  
Keep a running error of how far the line has strayed,  
When it tips past the middle, take a step up, and the line is made!

*[Chorus]*

**[Bridge (screamed)]**  
Step x! (Add dy!)  
Too far? (Step y!)  
Subtract dx! (And try again!)  
Pixel by pixel to the end!

**[Lead guitar solo: Qword]**  
*Qword’s first real solo since 1989 climbs the neck like a line on a screen: a few notes across, then one step up, then across again, with the steps spaced exactly to match the slope.*

**[Final chorus]**  
Bresenham! (Step by step!)  
Bresenham! (Error kept!)  
Add the slope to the error, and when it’s more than half you climb,  
Bresenham, Bresenham, integers every time!

## The lesson

A screen is a grid of pixels, so a line has to be approximated by choosing which pixels to light. Bresenham’s line algorithm (1962, written for IBM plotters) steps one pixel at a time along the longer axis and keeps a running integer error. When the error passes the halfway point, it also steps along the shorter axis and subtracts. It uses only integer addition and comparison, with no floating point and no division, which made it fast on early hardware.

## Suno prompt

**Title**

```
Bresenham
```

**Style of music**

```
2004 metalcore, explosive metalcore opener, chugging riff with a staircase-stepping breakdown, 150 BPM, lineup: female lead vocalist singing clean melodic vocals who also plays bass guitar, lead guitarist playing harmonized melodic leads and solos, keyboard player adding atmospheric synths, drummer screaming harsh male backing vocals, palm-muted chugging breakdowns, double-kick drums, clean soaring female choruses against screamed male parts, polished heavy production
```

**Exclude styles**

```
autotune, trap beats, EDM, modern pop, country, acoustic, lo-fi
```

**Lyrics**

```
[Lineup: female clean lead vocals and bass guitar, lead guitar, atmospheric synths, drums with male screamed backing vocals]

[Verse 1: female clean lead vocal]
A screen is just a grid of squares, no curves and no between,
Draw a line from here to there across the pixel screen.
Step along the x one square at a time,
And choose the pixel closest to the line!

[Chorus: female clean lead vocal, male screamed backing vocals]
Bresenham! (Step by step!)
Bresenham! (Error kept!)
Add the slope to the error, and when it’s more than half you climb,
Bresenham, Bresenham, integers every time!

[Verse 2: female clean lead vocal]
No floating point, no division, nothing but add and compare,
Nineteen sixty-two, a plotter pen moving through the air.
Keep a running error of how far the line has strayed,
When it tips past the middle, take a step up, and the line is made!

[Chorus: female clean lead vocal, male screamed backing vocals]
Bresenham! (Step by step!)
Bresenham! (Error kept!)
Add the slope to the error, and when it’s more than half you climb,
Bresenham, Bresenham, integers every time!

[Bridge: male screamed vocals, breakdown]
Step x! (Add dy!)
Too far? (Step y!)
Subtract dx! (And try again!)
Pixel by pixel to the end!

[Lead Guitar Solo: melodic run climbing in a staircase pattern, several notes across, then one step up]

[Final Chorus: female clean lead vocal, male screamed backing vocals]
Bresenham! (Step by step!)
Bresenham! (Error kept!)
Add the slope to the error, and when it’s more than half you climb,
Bresenham, Bresenham, integers every time!

[End]
```
