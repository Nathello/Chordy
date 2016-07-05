from chordy import Chordy
import unittest

class TestChordLookup(unittest.TestCase):

  def setUp(self):
    self.chordy = Chordy()

  def test_C_major_chord(self):
    chord = self.chordy.run(["X","3","2","0","1","0"])
    self.assertEquals(chord,"C Major")

  def test_A_minor_chord(self):
    chord = self.chordy.run(["X","0","2","2","1","0"])
    self.assertEquals(chord, "A Minor")

  def test_G_sus4_chord(self):
    chord = self.chordy.run(["3","3","0","0","1","3"])
    self.assertEquals(chord, "G Suspended Fourth")

  def test_naked_dudes(self):
    chord = self.chordy.run(["9","3","0","0","1","3"])
    self.assertEquals(chord, "I wanna see some naked dduuuuuuudes, that's why I built this pooooool")

    
    
