from fretboard_reader import FretboardReader
from note_lookup import NoteLookup

class Main:
  def __init__(self):
    reader = FretboardReader(["E","A","D","G","B","E"], NoteLookup())
    fretboard_input = raw_input("Gimme yo damn fretboard positions biatch: ")

    while fretboard_input != "q":

      array = fretboard_input.split(" ")
      print reader.generate_notes(array)
      fretboard_input = raw_input("Gimme yo damn fretboard positions biatch: ")

    print "see ya later pal"


Main()