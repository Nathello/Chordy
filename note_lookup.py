class NoteLookup:
  def __init__(self):
    self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

  def note_index(self,note):
    return self.notes.index(note)

  def note_interval(self, root_note_index, note_to_find):
    interval = 0
    current_location = root_note_index
    while (current_location < len(self.notes)):
      current_note = self.notes[current_location]
      if note_to_find == current_note:
        return interval
      interval += 1
      current_location += 1
    return interval



