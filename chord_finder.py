class ChordFinder:
  def __init__(self, note_lookup):
    self.note_lookup = note_lookup

  def find_chord(self, chord_notes):
    #chord_notes = ["C","E","G"]
    #If it's one note then just return the note name
    if len(chord_notes) == 1: return chord_notes[0]

    #find the root note in the notes array and return its index in the list of notes
    root_note_index = root_note_index(chord_notes)
    
    note_intervals = note_intervals(chord_notes, root_note_index)
    

  def root_note_index(self,chord_notes):
    root_note = chord_notes[0]
    return self.note_lookup.note_index(root_note)

  def note_intervals(self,chord_notes, root_note_index):
    #create an empty chord array to hold results with zero as the start point (as this represents the root note)
    chord_array = []
    for note in chord_notes:
      note_interval = self.note_lookup.note_interval(root_note_index, note)
      chord_array.append(note_interval)
    return chord_array


    #for every other note loop and get its index in the notes array
    #subtract the index of the root note from it
    #add result to chord array
    #convert array to string
    #lookup string in premade dictionary