from Composer import Composer 
from Musicaly import Musically



def main ():

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




main()