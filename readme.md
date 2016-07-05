This is a joint project with myself (Chris Dryden) and my wife Valerie Dryden to make a cool little app to help me play guitar. The commits are on Valerie's account because she is mean... but I did it all really... she sucks.

Chordy Algorithm

Take in an array of finger positions on strings.

0 => open
1+ => fret chosen
X => not used

Fretboard reader takes this in and translates it into an array of notes, with any duplicates removed.

["1","X","2","3","4","1"] becomes FEA#D#F

Chord finder takes in this array of notes and changes it into an array starting with the root note, followed by the distance in semitones to the other notes in ascending order.

CEG becomes [1,5,8]

Chord lookup takes this and the root note, converts it to a string key and finds the relevant chord type in it's internal collection.