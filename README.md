# Musically 

### We have created two classes to create our melodies:

- Composer : The principal purpose of this class is the automatic creation of melodies following the rules explained on this paper. 
- Musically: Will be in charge of the creation of the song following an automatic, semi-manual or manual process. This class will create the frequencies that will output the final sound per each note, chord. 


### Chord Rules Creation

We need to identify the grade of the chord before starting to group notes. The Grade of the chords could be defined as the number of notes in the chord. Ie, a chord with 2 notes will be considered a grade 2 chord. 

#### Rules for  grade 1 chord:
- Select any note of the Octave.
#### Rules for grade 2 chord:
- Create a dictionary with the valid relationships per each note
- Select one chord grade 1
- Search on the dictionary the valid relationships for this chord
- Pick any note from the dictionary[ chord grade 1]
#### Rules For grade 3 chord:
- Create a grade 2 chord
- Search on the dictionary the valid relationships per each note on chord 2 grade
- Find the intersection on both set of notes, this intersection will hold the notes that can be combined with both notes, this process will make sure we don't pick a dissonant note 



# How To use Musically

1. You can create an instance of musically an add any melody from the initial octave 
- ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
- the melody must be separate by dashed 
-- Example: 'E-D-C-D-E-E-E-D-D-D-E-G-G-E-D-C-D-E-E-E-E-D-D-E-D-C'

2. you can call the method createsong that will accept a firt string as parameter and a second number the times to loop the melody

This will create a wav file for you

Example:

- player = Musically(chords = 'E-D-C-D-E-E-E-D-D-D-E-G-G-E-D-C-D-E-E-E-E-D-D-E-D-C')
- player.createSong('maryhad a little lamb', 1)




This project was creating following the ideas found on the following paper

# Mathematics-of-Music

Full explaination of the code is at [TowardsDataScience - Medium](https://towardsdatascience.com/mathematics-of-music-in-python-b7d838c84f72)




## Usage
1. Create a virtual environment

`# virtualenv --no-site-packages env`

2. Activate the environment

`# source ./env/bin/activate`

3. Install all the requirements

`# pip install -r requirements.txt`

4. Run the program 

` # python3 main.py`

5. Play the generated wav file

`# aplay twinkle-twinkle.wav`
