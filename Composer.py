import random


#Create a melody from octave series
#@param {array} Octave - notes to be used by default we will use the octave
class Composer ():

    def __init__ (self, octave = []):
        self.base_active = False
        self.composer = []
        self.octave = list(octave) if len(octave) > 0 else ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
        self.process_consonance_groups() ##Create consonance notes groups
        self.separator = "-"

    # Create a dictionary with the consonance notes groups per each element in the octave
    # return none
    # set a dictionary with key the element in the octave and value of the consonance notes per note
    def process_consonance_groups (self) :
        # Create a dictionary with consocance notes: 
        notes_group = {}
        initial_group = self.octave.copy()
        for note in self.octave:
            notes_group[note] =  initial_group[3:-2] 
            initial_group.append(initial_group[0])
            initial_group.pop(0)
        
        self.consonance_notes_dictionary = notes_group


    # Create a base pattern to add the same patter to each additional chord
    # param {array} pattern [notes] notes to add ['a','D','B']
    def add_base_pattern (self, pattern = []):
        self.base_active = True
        self.base = pattern
        self.base_length = len(self.base)
        #CAD -> 3
    

    # Add notes to the starting melody, this can be used to add more 
    # new_notes = [EG, FD, FA]
    # individual {boolean} if True the notes wont be addded to the general melody
    # return if individual this will return a melody to be used outside 
    def add_note_to_composition (self, new_notes = [], individual = False):

        add_key_notes = ''

        if self.base_active:
            if len(new_notes) < self.base_length:
                error = F"Invalid len specified, we need at least {self.base_length} notes to add to the base pattern"
                raise Exception(error)

            for index, item in enumerate(self.base):
                    add_key_notes += item + new_notes[index] + self.separator
            
            add_key_notes = add_key_notes[0:-1]
        else: 
            add_key_notes = self.separator.join(new_notes)

        if individual:  
            return add_key_notes

        self.composer.append(add_key_notes)

    # Create chord with one single note
    def artifial_1_grade_chord (self):
        return random.choice(self.octave)

    # Create chord with 2 notes
    def artifial_2_grade_chord (self):
        
        initial_key = random.choice(self.octave)
        return initial_key + random.choice(self.consonance_notes_dictionary[initial_key])

    # Create chord with three notes
    def artifial_3_grade_chord (self):

        initial_key = random.choice(self.octave)
        second_key = random.choice(self.consonance_notes_dictionary[initial_key])

        first_group = self.consonance_notes_dictionary[initial_key]
        second_group = self.consonance_notes_dictionary[second_key]

        third_key = random.choice(list(set(first_group) & set(second_group)))

        return initial_key + second_key + third_key

    # select a group of grade notes
    # group == 0 will return a random number of notes, among the three artificial groups
    def select_group(self, group = 0):

        chord_option = [self.artifial_1_grade_chord, self.artifial_2_grade_chord, self.artifial_3_grade_chord]

        if group == 1:
            chord_option = [self.artifial_1_grade_chord]
        elif group == 2:
            chord_option = [self.artifial_2_grade_chord]
        elif group == 3:
            chord_option = [self.artifial_3_grade_chord]
        
        return [random.choice(chord_option)()]

    # add notes to the object
    # number of notes {int} number of chords to form,
    # group - grade of notes to include, if 0 will return random grade notes
    # return - none
    def create_melody (self, number_notes = 10, group = 0):
        
        while number_notes > 0:
            self.add_note_to_composition(self.select_group(group))
            number_notes -= 1


    # This will be used as an static function
    # number of notes {int} number of chords to form,
    # group - grade of notes to include, if 0 will return random grade notes
    # return - the individual composition
    def create_individual_melody (self, number_notes = 10, group = 0):
        
        notes = []
        while number_notes > 0:
            notes.append(self.add_note_to_composition(self.select_group(group), individual = True))
            number_notes -= 1
        return self.separator.join(notes)

    #return the composition 
    def compose (self):
        return self.separator.join(self.composer)
    #use the patter to create notes 




#This class will control the composition
composition1 = Composer()
print(composition1.create_individual_melody(100))
# print(composition1.compose())


# composition1.add_base_pattern(['C','A','D'])
# composition1.add_note_to_composition(['EG', 'FD','FA'])
# composition1.add_note_to_composition(['GA', 'GB','a'])
# composition1.add_note_to_composition(['GE', 'Gc','ca'])