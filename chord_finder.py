class ChordFinder:
  def __init__(self, note_lookup):
    self.notes = note_lookup.notes

  def find_chord(self, chord_notes):
    #chord_notes = ["C","E","G"]
    #If it's one note then just return the note name
    if len(chord_notes) == 1:
      return chord_notes[0]

    index = root_note_index(chord_notes)
    #find the root note in the notes array and return its index in the list of notes

  def root_note_index(self,chord_notes):
    root_note = chord_notes[0]
    return self.notes.index(root_note)
    
    #create an empty chord array to hold results with zero as the start point (as this represents the root note)
    #for every other note loop and get its index in the notes array
    #subtract the index of the root note from it
    #add result to chord array
    #convert array to string
    #lookup string in premade dictionary