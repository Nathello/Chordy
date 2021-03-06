from chord_finder import ChordFinder
from note_lookup import NoteLookup

import unittest

class TestChordFinder(unittest.TestCase):

	def setUp(self):
		self.note_lookup = NoteLookup()
		self.chord_finder = ChordFinder(self.note_lookup)

	def test_init(self):
	  self.assertIsNotNone(self.chord_finder)

	def test_notes(self):
		self.assertEquals(self.chord_finder.note_lookup, self.note_lookup)

	def test_one_note_chord(self):
		chord_array = ["C"]
		result = self.chord_finder.find_chord(chord_array)
		self.assertEquals(result, "C")

	def test_index_of_root_note(self):
		chord_notes = ["C","E","G"]
		result = self.chord_finder.root_note_index(chord_notes)
		self.assertEquals(result, 3)

	def test_note_intervals(self):
		chord_notes = ["C","E","G"]
		root_note_index = 3
		result = self.chord_finder.note_intervals(chord_notes,root_note_index)
		self.assertEquals(result,[0,4,7])

	def test_note_intervals_looping(self):
		chord_notes = ["G","B","D"]
		root_note_index = 10
		result = self.chord_finder.note_intervals(chord_notes,root_note_index)
		self.assertEquals(result,[0,4,7])

	def test_note_intervals_looping_A_minor(self):
		chord_notes = ["A","E","C"]
		root_note_index = 0
		result = self.chord_finder.note_intervals(chord_notes,root_note_index)
		self.assertEquals(result,[0,3,7])

	def test_note_intervals_weird_chord(self):
		chord_notes = ["F#","A","D#"]
		root_note_index = 9
		result = self.chord_finder.note_intervals(chord_notes,root_note_index)
		self.assertEquals(result,[0,3,9]) 