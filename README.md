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

```
player = Musically(chords = 'E-D-C-D-E-E-E-D-D-D-E-G-G-E-D-C-D-E-E-E-E-D-D-E-D-C')
player.createSong('maryhad a little lamb', 1)
```

# How To use Composer

1. You can use Composer as as melody creator where a complete song can be created  automatically.

example 

```
composition1 = Composer()
composition1.create_melody(100)
print(composition1.compose())
```

This will return a composition of 100 notes of random grade, if you wish to obtain only composition with 1 grade, pass the integer 1 as second param

2. Composer also can create individual compositions 

example 

```
    Director = Composer()
    starting = Director.create_individual_melody(5,1) #will return 5 notes of grade 1
    notes1 = Director.create_individual_melody(3,1) #will return 3 notes of grade 1
    notes2 = Director.create_individual_melody(3,3) #will return 3 notes of grade 3
    notes3 = Director.create_individual_melody(5,2) #will return 5 notes of grade 2
    notes4 = Director.create_individual_melody(2,1) #will return 2 notes of grade 1
    FrustaNotata = Director.create_individual_melody(10,3) #will return 10 notes of grade 3

```

# General Example of how to use both classes can be found on main.py

```

    #create notes
    Director = Composer()
    starting = Director.create_individual_melody(5,1)
    notes1 = Director.create_individual_melody(3,1)
    notes2 = Director.create_individual_melody(3,3)
    notes3 = Director.create_individual_melody(5,2)
    notes4 = Director.create_individual_melody(2,1)
    FrustaNotata = Director.create_individual_melody(10,3)
    

    player = Musically(chords = starting, speed = 0)
    player.base_freq = 100
    player.update_last_rate = 1.8

    #introduction
    player.append_rythm_peace(notes2, repeat= 3, speed = 1,  reversed= False)
    player.append_rythm_peace(notes4, repeat= 3, speed = 1,  reversed= False)
    
    # Principal
    player.append_rythm_peace(notes3, repeat= 6, speed = 0.5,  reversed= False)
    player.append_rythm_peace(notes1, repeat= 1, speed = 1)
    player.append_rythm_peace(notes3, repeat= 6, speed = 0.5,  reversed= False)

    ## Resonata-fenale
    player.append_rythm_peace(FrustaNotata, repeat= 1, speed = 1,  reversed= False)

    #play-Song
    player.create_song('mistery', 3)
    player.view()

```


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
