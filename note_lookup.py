class NoteLookup:
  def __init__(self):
    self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

  def note_index(self,note):
    return self.notes.index(note)

  def note_interval(self, root_note_index, note_to_find):
    self.interval = 0

    self.current_location = root_note_index

    found = self.match_root_to_end(note_to_find)
    if found: return self.interval

    self.current_location = 0

    found = self.match_start_of_array_to_root(note_to_find, root_note_index)
    if found: return self.interval

    return -1

  def match_root_to_end(self, note_to_find):
    return self.match(note_to_find, len(self.notes))

  def match_start_of_array_to_root(self, note_to_find, previous_start_point):
    return self.match(note_to_find, previous_start_point)

  def match(self, note_to_find, end_point_of_search):
    while (self.current_location < end_point_of_search):
      current_note = self.notes[self.current_location]
      if note_to_find == current_note: return True
      self.interval += 1
      self.current_location += 1
