from fretboard_reader import FretboardReader
from chordy import Chordy

class Main:
  def __init__(self):
    chordy = Chordy()
    
    input_message = "Enter fretboard positions (0-6, X): "
    quit_key = "q"
    divider = " "

    fretboard_input = raw_input(input_message)

    while fretboard_input != quit_key:

      array = fretboard_input.split(divider)
      print chordy.run(array)
      fretboard_input = raw_input(input_message)

    print "see ya later pal"


Main()