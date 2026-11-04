# Packet Loss

**Packet Storm** (1982), track 8

[▶ Listen on Suno](https://suno.com/song/f75a9560-9ab4-43f9-8bac-db7001eda6a7)

> One of Bytes’s reels never arrived. He waited three weeks, then recorded it again.

## Lyrics

**[Verse 1]**  
I sent it out at midnight and I’m waiting by the line,  
No answer from the other side, no acknowledgment, no sign.  
Maybe it was lost in a storm, maybe dropped along the way,  
The timer’s running down, and I can’t wait another day!

**[Chorus]**  
Packet loss! (Gone!)  
Somewhere in the night!  
Packet loss! (Gone!)  
Send it again and get it right!  
No ACK before the timer ends, then send it once again,  
Packet loss, packet loss, till it reaches you, my friend!

**[Verse 2]**  
The network makes no promises, it does the best it can,  
A full queue drops the extras and a noisy wire will jam.  
The sender keeps a copy till it knows the copy’s home,  
Retransmit what’s missing, and you’re never on your own!

*[Chorus]*

**[Bridge]**  
Timeout! (Timeout!) Send it again!  
Retransmit! (Retransmit!) Until the end!

**[Lead guitar solo: Byt]**  
*Every so often one of Byt’s phrases drops out into silence. He waits for Nyble’s nod that it arrived, and when the nod doesn’t come, he plays the missing phrase again until it does.*

**[Final chorus]**  
Packet loss! (Gone!)  
Somewhere in the night!  
Packet loss! (Gone!)  
Send it again and get it right!  
No ACK before the timer ends, then send it once again,  
Packet loss, packet loss, till it reaches you, my friend!

## The lesson

Networks are best-effort: packets get dropped when router queues fill up, or get corrupted on noisy links. TCP keeps a copy of everything not yet acknowledged and runs a retransmission timer. If no ACK arrives in time, it sends the data again. That retransmission is how TCP stays reliable over an unreliable network.

## Suno prompt

**Title**

```
Packet Loss
```

**Style of music**

```
1982 classic heavy metal, power trio, heavy dramatic riff with sudden dropouts into silence, 108 BPM, lineup: female lead vocalist who also plays bass guitar, lead electric guitarist, drummer singing male backing vocals, soaring powerful female vocals, sharp harmonized lead guitar, galloping bass guitar, pounding double-kick drums, big reverb production
```

**Exclude styles**

```
synths, autotune, EDM, trap beats, modern pop, lo-fi
```

**Lyrics**

```
[Lineup: female lead vocals and bass guitar, lead electric guitar, drums with male backing vocals]

[Verse 1: female lead vocal]
I sent it out at midnight and I’m waiting by the line,
No answer from the other side, no acknowledgment, no sign.
Maybe it was lost in a storm, maybe dropped along the way,
The timer’s running down, and I can’t wait another day!

[Chorus: female lead vocal, male backing vocals]
Packet loss! (Gone!)
Somewhere in the night!
Packet loss! (Gone!)
Send it again and get it right!
No ACK before the timer ends, then send it once again,
Packet loss, packet loss, till it reaches you, my friend!

[Verse 2: female lead vocal]
The network makes no promises, it does the best it can,
A full queue drops the extras and a noisy wire will jam.
The sender keeps a copy till it knows the copy’s home,
Retransmit what’s missing, and you’re never on your own!

[Chorus: female lead vocal, male backing vocals]
Packet loss! (Gone!)
Somewhere in the night!
Packet loss! (Gone!)
Send it again and get it right!
No ACK before the timer ends, then send it once again,
Packet loss, packet loss, till it reaches you, my friend!

[Bridge: female lead vocal, male backing shouts]
Timeout! (Timeout!) Send it again!
Retransmit! (Retransmit!) Until the end!

[Lead Guitar Solo: phrases that suddenly drop into silence and are played again]

[Final Chorus: female lead vocal, male backing vocals]
Packet loss! (Gone!)
Somewhere in the night!
Packet loss! (Gone!)
Send it again and get it right!
No ACK before the timer ends, then send it once again,
Packet loss, packet loss, till it reaches you, my friend!

[End]
```
