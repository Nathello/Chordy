from chord_lookup import ChordLookup
from note_lookup import NoteLookup
from chord_finder import ChordFinder
from fretboard_reader import FretboardReader

class Chordy:
  def __init__(self):
    self.note_lookup = NoteLookup()
    self.reader = FretboardReader(["E","A","D","G","B","E"], self.note_lookup)
    self.chord_finder = ChordFinder(self.note_lookup)
    self.chord_lookup = ChordLookup()

  def run(self, fretboard_config):
    chord_notes = self.reader.generate_notes(fretboard_config)
    root_note_index = self.chord_finder.root_note_index(chord_notes)
    intervals_array = self.chord_finder.note_intervals(chord_notes,root_note_index)
    root_note = self.note_lookup.notes[root_note_index]
    chord = self.chord_lookup.find_chord(intervals_array, root_note)
    return chord