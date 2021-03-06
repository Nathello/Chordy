class ChordLookup:
  def __init__(self):
    self.chord_dictionary = {
      "0-4-7":"Major",
      "0-3-7":"Minor",
      "0-4-7-11":"Major Seventh",
      "0-2-7":"Suspended Second",
      "0-5-7":"Suspended Fourth",
      "0-3-7-10":"Minor Seventh",
      "0-4-7-10":"Dominant Seventh"
    }

  def convert_to_key(self, intervals_array):
    return "-".join(str(interval) for interval in intervals_array)

  def find_chord(self, intervals_array, root_note):
    result = root_note + " "
    key = self.convert_to_key(intervals_array)
    chord = self.chord_dictionary.get(key)
    if(chord == None): return "I wanna see some naked dduuuuuuudes, that's why I built this pooooool"
    return result + chord
