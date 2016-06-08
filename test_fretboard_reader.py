from fretboard_reader import FretboardReader

import unittest

class TestFretboardReader(unittest.TestCase):

	def setUp(self):
		self.reader = FretboardReader()

	def test_init(self):
	    self.assertIsNotNone(self.reader)

	def test_standard_tuning(self):
		result = self.reader.standard_tuning
		self.assertEquals(result, ["E","A","D","G","B","E"])

	def test_notes(self):
		result = self.reader.notes
		self.assertEquals(result, ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"])

	def test_generate_notes_with_invalid_note_quantity_returns_empty(self):
		stupid_array = ["x","x","x","x"]
		result = self.reader.generate_notes(stupid_array)
		self.assertEquals(result, [])

	def test_generate_notes_with_x_lower_returns_empty_array(self):
		stupid_array = ["x","x","x","x","x","x"]
		result = self.reader.generate_notes(stupid_array)
		self.assertEquals(result, [])

	def test_generate_notes_with_x_upper_returns_empty_array(self):
		stupid_array = ["X","x","X","x","X","x"]
		result = self.reader.generate_notes(stupid_array)
		self.assertEquals(result, [])

	def test_removes_duplicate_notes(self):
		stupid_array = ["1","X","X","X","X","1"]
		result = self.reader.generate_notes(stupid_array)
		self.assertEquals(result, ["F"])

	def test_fretted_note_index_returns_correct_index__0(self):
		result = self.reader.fretted_note_index("0", "E")
		self.assertEquals(result, 7)

	def test_fretted_note_index_returns_correct_index__2(self):
		result = self.reader.fretted_note_index("2", "E")
		self.assertEquals(result, 9)

	def test_valid_note_index_less_than_max_length_of_notes(self):
		result = self.reader.valid_note_index(2)
		self.assertEquals(result, 2)

	def test_valid_note_index_last_item_plus_1(self):
		result = self.reader.valid_note_index(12)
		self.assertEquals(result,0)

	def test_valid_note_index_last_item_plus_5(self):
		result = self.reader.valid_note_index(16)
		self.assertEquals(result,4)

	def test_valid_note_index_last_item_plus_15(self):
		result = self.reader.valid_note_index(26)
		self.assertEquals(result,2)