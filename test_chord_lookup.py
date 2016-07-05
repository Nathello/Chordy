from chord_lookup import ChordLookup

import unittest

class TestChordLookup(unittest.TestCase):

	def setUp(self):
		self.chord_lookup = ChordLookup()

	def test_convert_intervals_to_dictionary_key(self):
		result = self.chord_lookup.convert_to_key([0,4,7])
		self.assertEquals(result,"0-4-7")
