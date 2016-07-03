class NoteLookup:
  def __init__(self):
    self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

  def note_index(self,note_input):
    counter = 0
    for note in self.notes:
      if note == note_input:
        return counter
      counter += 1
    return -1

    
