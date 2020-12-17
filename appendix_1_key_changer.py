
# Sommer Implementation


def new_indices(notes, new_key, notes_list, note_difference):
    '''function new indices
    parameters: notes, new key, notes list
    returns list of indices of notes in new melody
    '''
    new_index = []
    for i in range(len(notes)):          
        new_note = (notes_list.index(notes[i]) + note_difference)
        if new_note >= 12:#to account for octave on circle
            new_note = new_note % 12
            new_index.append(new_note)
        else:
            new_index.append(new_note)
    return new_index


def get_new_melody(new_index, notes_list):
    '''function: get new melody
        parameter: list of indices of notes in new melody, notes list
        return: notes of new melody
    '''
    new_melody = []
    for j in new_index:
        new_melody.append(notes_list[j])
    return new_melody

def main():
   #this program assumes that the first note in the melody is the home key
    print("make sure you change the inputs in main-- this program is not interactive while running. Variables to change are 'notes' and 'new_key'")
    notes = ["C", "E", "G"] #Here put the melody who's key you want to change
    new_key = "D"   #Here put the new key in quotation marks

    #this list does not change. helps us find distance between notes
    notes_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    #distance between first note and new key:
    note_difference = (notes_list.index(new_key) - notes_list.index(notes[0]))
   
    new_index = new_indices(notes, new_key, notes_list, note_difference)
    
    print("Your new melody is", get_new_melody(new_index, notes_list))
main()


