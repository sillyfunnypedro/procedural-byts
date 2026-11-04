# Slow Start

**Packet Storm** (1982), track 10

> The only song where the band deliberately starts quiet. It doesn’t last.

## Lyrics

**[Verse 1]**  
Start with a single packet and see if it gets through,  
Then two, then four, then eight, the window doubles too.  
The road is wide, the road is fast, and no one’s in the way,  
Faster, faster, faster, till the network starts to sway!

**[Chorus]**  
Slow start! (Double it up!)  
Slow start! (Fill the cup!)  
But when a packet’s lost it means the road is jammed,  
Back off, cut it in half, or the whole network’s damned!

**[Verse 2]**  
The receiver has a window that says how much it can take,  
Don’t flood it with more data than its buffers were built to make.  
And the network has its limits, every router has its queue,  
Push too hard and everybody’s slow, including you!

*[Chorus]*

**[Bridge]**  
Flow control! (Don’t drown the one you send to!)  
Congestion control! (Don’t drown the road you’re on too!)

**[Lead guitar solo: Byt]**  
*Byt starts with one note per bar, then two, then four, then eight, until the amp starts to distort. He cuts back to half and climbs again, one note at a time this time, staying just under the edge.*

**[Final chorus]**  
Slow start! (Double it up!)  
Slow start! (Fill the cup!)  
But when a packet’s lost it means the road is jammed,  
Back off, cut it in half, or the whole network’s damned!

## The lesson

Flow control, through the receiver’s window, keeps a sender from overwhelming the receiver. Congestion control keeps senders from overwhelming the network. TCP’s slow start doubles the sending window every round trip; when packets are lost, it cuts the window in half and then grows it slowly again.

## Suno prompt

**Title**

```
Slow Start
```

**Style of music**

```
1982 classic heavy metal, power trio, builds from a slow sparse riff to full speed, then pulls back and climbs again, 132 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, soaring powerful female vocals, sharp harmonized lead guitar, galloping bass guitar, pounding double-kick drums, big reverb production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, lo-fi
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
Start with a single packet and see if it gets through,
Then two, then four, then eight, the window doubles too.
The road is wide, the road is fast, and no one’s in the way,
Faster, faster, faster, till the network starts to sway!

[Chorus: female lead vocal, male backing vocals]
Slow start! (Double it up!)
Slow start! (Fill the cup!)
But when a packet’s lost it means the road is jammed,
Back off, cut it in half, or the whole network’s damned!

[Verse 2: female lead vocal]
The receiver has a window that says how much it can take,
Don’t flood it with more data than its buffers were built to make.
And the network has its limits, every router has its queue,
Push too hard and everybody’s slow, including you!

[Chorus: female lead vocal, male backing vocals]
Slow start! (Double it up!)
Slow start! (Fill the cup!)
But when a packet’s lost it means the road is jammed,
Back off, cut it in half, or the whole network’s damned!

[Bridge: female lead vocal, male backing shouts]
Flow control! (Don’t drown the one you send to!)
Congestion control! (Don’t drown the road you’re on too!)

[Lead Guitar Solo: one note per bar, doubling every bar, then halving and climbing slowly]

[Final Chorus: female lead vocal, male backing vocals]
Slow start! (Double it up!)
Slow start! (Fill the cup!)
But when a packet’s lost it means the road is jammed,
Back off, cut it in half, or the whole network’s damned!

[End]
```
