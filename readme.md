Chordy Algorithm

Take in an array of finger positions on strings.

0 => open
1+ => fret chosen
X => not used

Fretboard reader takes this in and translates it into an array of notes, with any duplicates removed.

["1","X","2","3","4","1"] becomes FEA#D#F


Chord transformer takes in this array of notes and changes it into an array starting with the root note, followed by the distance in semitones to the other notes in ascending order.

CEG becomes [1,5,8]