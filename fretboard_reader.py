class FretboardReader:
	def __init__(self):
		self.standard_tuning = ["E","A","D","G","B","E"]
		self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

	def generate_notes(self, fretboard_values):
		#fretboard_values = ["x","3","2","0","1","0"]
		result_array = []
		if len(fretboard_values) < len(self.standard_tuning): 
			return result_array
			#returns empty array if you give a duff input

		for index, fret_number in enumerate(fretboard_values):
			if fret_number.lower() == "x":
				continue
			standard_tuning_note = self.standard_tuning[index]
			note = self.find_note(fret_number, standard_tuning_note)
			#First value to be passed in here is "3"
			result_array.append(note)

		return result_array

	def find_note(self, fretboard_position, open_note):
		fretted_note_index = self.fretted_note_index(fretboard_position, open_note)
		fretted_note = self.notes[fretted_note_index]
		return fretted_note

	def fretted_note_index(self, fretboard_position, open_note):
		fret_number = int(fretboard_position)
		note_index = self.notes.index(open_note)
		fretted_note_index = fret_number + note_index
		valid_fretted_note_index = self.valid_note_index(fretted_note_index)
		return valid_fretted_note_index

	def valid_note_index(self, fretted_note_index):
		number_of_notes = len(self.notes)
		if fretted_note_index < number_of_notes - 1:
			return fretted_note_index

		overflow_times = int(fretted_note_index / number_of_notes)
		multiplier = overflow_times * number_of_notes

		return fretted_note_index - multiplier

	#def remove_duplicate_notes(self, )