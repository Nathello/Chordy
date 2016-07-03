class NoteLookup:
  def __init__(self):
    self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

  def note_index(self,note):
    return self.notes.index(note)

  def note_interval(self, root_note_index, note_to_find):
    self.interval = 0

    self.current_location = root_note_index

    while (self.current_location < len(self.notes)):
      found = self.match(note_to_find)
      if found: return self.interval

    self.current_location = 0

    while (self.current_location < root_note_index):
      found = self.match(note_to_find)
      if found: return self.interval

    return -1

  def match(self, note_to_find):
    current_note = self.notes[self.current_location]
    if note_to_find == current_note:
      return True
    self.interval += 1
    self.current_location += 1
