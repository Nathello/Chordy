from fretboard_reader import FretboardReader

class Main:
  def __init__(self):
    reader = FretboardReader()
    fretboard_input = raw_input("Gimme yo damn fretboard positions biatch: ")

    while fretboard_input != "q":

      array = fretboard_input.split(" ")
      print reader.generate_notes(array)
      fretboard_input = raw_input("Gimme yo damn fretboard positions biatch: ")

    print "see ya later pal"


Main()