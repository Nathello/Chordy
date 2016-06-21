from chord_finder import ChordFinder
from note_lookup import NoteLookup

import unittest

class TestChordFinder(unittest.TestCase):

	def setUp(self):
		note_lookup = NoteLookup()
		self.chord_finder = ChordFinder(note_lookup)

	def test_init(self):
	  self.assertIsNotNone(self.chord_finder)

	def test_notes(self):
		self.assertEquals(self.chord_finder.notes, ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"])

	def test_one_note_chord(self):
		chord_array = ["C"]
		result = self.chord_finder.find_chord(chord_array)
		self.assertEquals(result, "C")