from chordy import Chordy
import unittest

class TestChordLookup(unittest.TestCase):

  def setUp(self):
    self.chordy = Chordy()

  def test_C_major_chord(self):
    chord = self.chordy.run(["X","3","2","0","1","0"])
    self.assertEquals(chord,"C Major")



  # def test_A_minor_chord(self):
  #   chord = self.chordy.run(["X","0","2","2","1","0"])
  #   self.assertEquals(chord, "A Minor")
    
