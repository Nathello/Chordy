class ChordLookup:
  def __init__(self):
    chord_dictionary = {
      "0-4-7":"Major",
      "0-3-7":"Minor",
      "0-4-7-11":"Major Seventh",
      "0-2-7":"Suspended Second",
      "0-5-7":"Suspended Fourth",
      "0-3-7-10":"Minor Seventh"
    }

  def convert_to_key(self, intervals_array):
    return "-".join(str(interval) for interval in intervals_array)
