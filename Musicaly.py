from scipy.io.wavfile import write
import numpy as np
from Composer import Composer
import random


class Musically ():

    def __init__ (self, notes ='', chords = '', speed = 0.5):
        self.samplerate = 44100
        self.update_last_rate = 1
        self.base_freq = 261.63 #Frequency of Note C4
        self.amplitude = 4096
        self.__octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
        self.notes = notes
        self.chords = chords
        self.speed = speed
        self.initial_part_song(self.speed)
        
    # This function creates the frequence for each note in our octave
    def get_piano_notes(self):
        ''' Returns a dict object for all the piano note's frequencies '''
        # White keys are in Uppercase and black keys (sharps) are in lowercase
        self.note_freqs = {self.__octave[i]: self.base_freq * pow(2,(i/len(self.__octave))) for i in range(len(self.__octave))}        
        # self.note_freqs[''] = 0.0
        return self.note_freqs
        
        
    def get_wave(self, freq, duration = 0.5 ):
        t = np.linspace(0, duration, int(self.samplerate * duration))
        wave = self.amplitude * np.sin(2 * np.pi * freq * t)
        return wave
         
    def get_chord_data(self, chords, duration = 0.5):
        self.notes += '-' + chords
        chords = chords.split('-')
        
        note_freqs = self.get_piano_notes()
        
        chord_data = []
        for chord in chords:
            data = sum([self.get_wave(note_freqs[note], duration) for note in list(chord)])
            chord_data.append(data)
    
        chord_data = np.concatenate(chord_data, axis=0)    
        return chord_data

    def initial_part_song (self, initial_speed = 0.5):
        self.data = self.get_chord_data(self.chords, initial_speed)
    
    def append_rythm_peace (self, notes, repeat = 2, speed = 0.5, reversed = False):
        
        if reversed : notes = notes[::-1]
        
        while repeat > 0:
            self.data = np.append(self.data, self.get_chord_data(notes, speed))
            repeat -= 1 

    def create_song (self,songname, repeat = 1):

        self.data = np.resize(self.data, (len(self.data)* repeat,))
        write(self.autorized_name(songname), int(self.samplerate * self.update_last_rate) , self.data.astype(np.int16))

    def view (self):
        print('notes:' + self.notes)

    def autorized_name (self, name):
        return "songs/"+ name.replace(" ", "_") +  '.wav'





# player = Musically(chords = 'E-D-C-D-E-E-E-D-D-D-E-G-G-E-D-C-D-E-E-E-E-D-D-E-D-C')
# player.createSong('maryhad a little lamb', 1)

# player2 = Musically(chords = 'C C F F F F F F E F G C C G G G G G G F G A A A B B B B D D B B A A A G F F A A G G G F E E D E F'.replace(' ','-'))
# player2.createSong('If You’re Happy and You Know It', 1)

# player3 = Musically(chords = 'G G G D E E D B B A A G D G G G D E E D B B A A G D D G G G D D G G G G G G G D E E D B B A A G'.replace(' ','-'))
# player3.createSong('Old MacDonald Had a Farm', 5, speed = 0.3)
