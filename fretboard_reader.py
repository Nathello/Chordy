class FretboardReader:
	def __init__(self):
		self.standard_tuning = ["E","A","D","G","B","E"]
		self.notes = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

	def generate_notes(self, fretboard_values):
		#fretboard_values = ["3","2","0","0","3","3"]
		chord_notes = []
		if len(fretboard_values) < len(self.standard_tuning): 
			return chord_notes
			#returns empty array if you give a duff input

		for index, fret_number in enumerate(fretboard_values):
			if fret_number.lower() == "x":
				continue
			standard_tuning_note = self.standard_tuning[index]
			#loops through and gets the index if each fretted value to then look up the appropriate open note in the standard tuning array
			note = self.find_note(fret_number, standard_tuning_note)
			#some weird crazy wizard magic happens here to get the right note
			chord_notes.append(note)

		return chord_notes

	#finds the appropriate note in the notes array given the index provided by the fretted note
	def find_note(self, fretboard_position, open_note):
		fretted_note_index = self.fretted_note_index(fretboard_position, open_note)
		fretted_note = self.notes[fretted_note_index]
		return fretted_note

	#given fretboard position 3 with open note A returns C
	def fretted_note_index(self, fretboard_position, open_note):
		fret_number = int(fretboard_position)
		#"3" becomes 3
		note_index = self.notes.index(open_note)
		#lookup the index of the open note (A becomes 0)
		fretted_note_index = fret_number + note_index
		#add the fret value to the note index count up the note array - 0+3 = 3
		valid_fretted_note_index = self.valid_note_index(fretted_note_index)
		return valid_fretted_note_index

	#makes sure we don't exceed our array of notes (total of 12) and loops back through the list if required
	def valid_note_index(self, fretted_note_index):
		number_of_notes = len(self.notes)
		#Checking to see if we need to loop back on the array of notes (i.e. if we are counting 4 spaces from G we get B)
		if fretted_note_index < number_of_notes - 1:
			return fretted_note_index
		#Fretted note index for A = 0 but also 12 (as we have 12 notes in our scale)
		overflow_times = int(fretted_note_index / number_of_notes)
		#G as 21 becomes 12/12 = 1, rounded
		multiplier = overflow_times * number_of_notes
		#multiplier returns 1 * 12

		return fretted_note_index - multiplier
		#12 - 12 = 0

	#We have to do this manually because the set() function is stupid and reorders things
	def remove_duplicate_notes(self, chord_notes):
		unique_notes = []
		for note in chord_notes:
			if note not in unique_notes:
				unique_notes.append(note)
		return unique_notes
