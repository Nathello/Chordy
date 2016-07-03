from fretboard_reader import FretboardReader
from note_lookup import NoteLookup

class Main:
  def __init__(self):
    reader = FretboardReader(["E","A","D","G","B","E"], NoteLookup())
    input_message = "Enter fretboard positions (0-6, X): "
    quit_key = "q"
    divider = " "

    fretboard_input = raw_input(input_message)

    while fretboard_input != quit_key:

      array = fretboard_input.split(divider)
      print reader.generate_notes(array)
      fretboard_input = raw_input(input_message)

    print "see ya later pal"


Main()