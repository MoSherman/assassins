#THE MAZE OF THE ASSASSINS

from sys import exit

def enter():
    print "Congrats! You passed the first test, had you refused to enter the guild would not have been pleased..."
    print "There is no turning back now as the door shuts behind you."
    print "You see however that there are no doors in the room your in, just four stone walls. What will you do? /n"
    
    choice = raw_input("> ")
    
    while choice != "climb" or choice != "dig":
    
        if choice == "climb": 
            print "You test the strength of the wall and it's stones and decide to climb over."
            print "You manage to avoid the poison spikes on top of the wall just barely and land silently on the other side."
            spinhx()
    
        elif choice == "dig":
            print "You remove your foldable spade from your bag and begin to dig under the wall in front of you."
            print "In hour into your digging you start to wonder if you made a bad choice."
            print "This is confirmed a moment later when a hell worm bursts through the wall of you tunnel."
            
            tunnel()
    
        else: 
            print "Your favorite instructor takes pity on your poor start and yells out 'climb or dig you fool!'."
            choice = raw_input("> ")

def noenter():
    print "You choose not to enter the maze."
    print "This is a mistake."
    print "'You have failed the first test' yells the master assassain, 'cowards never prosper!'"
    print "The guild is so displeased with you decision that they all attack you at once."
    print "It all happened so quickly no one was really sure what got you in the end."
    print "There wasn't enough left to figure it out really."
    exit(0)

def spinhx():
    print "Before you can even get you bearings you realize you are not alone."
    print "Sitting silently before the only exit in front of you is a perticularly grumpy looking spinhx."
    print "You can not risk running around the spinhx or fighting it as both would mean certain death."
    print "You must answer it's riddle."
    print "The spinhx speaks suddenly in a deep voice but says something rather unexpected."
    print "'Look kid I\'m not really in the mood for human today so I\'ll give you an easy one.'"
    print "'Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters.\nIf you don\'t know what that is then you deserve to be easten probably!'"
    
    
    choice = raw_input("> ")
    guesses = 0
    
    while choice != 'wind' and guesses < 2:
        print "\'Really?\' says the sphinx \'%r is you best guess? Do you read!? Try again!\'" % choice
        choice = raw_input("> ")
    
    if choice == "wind":
        print "Despite being not very good with riddles, even you got this one eventually."
        print "The cranky spinhx shuffles into the corner to take a nap and you walk through the door before you."
        lorr1()
        
    else:
        print "'My patience is gone and your futile attempts have made me hangry!' says the spinhx."
        print "It grabs you and though you struggle mightly there is no escape!"
        death()

def tunnel():
    print "The hell worm is a particularly nasty insect, more dragon cycloptic then worm, it\'s teeth are sharper then diamonds."
    print "Your instructors taught you well however and you know the only two ways to incapacitate a hell worm.
    print "Where must you attack on the hell worm to survive?"
    
    choice = raw_input("> ")
    
    while choice != "eye" or choice != "tongue":
    
        if choice == "eye": 
            print "You attack the hell worm's eye with your spade, blinding it."
            print "It's a good thing you paid extra attention in \'Violent Creatures and How to Use Them: 101 \'."
            print "You keep digging until you finally emerge on the other side of the wall."
            sphinx()
    
        elif choice == "tongue":
            print "You stabbed the hell worms tongue."
            print "You knicked yourself in the process however on it\'s diamond teeth."
            print "You better get out of the maze quickly before you bleed to death!"
            sphinx()
    
        else: 
            print "You couldn't remember where to attack and the hell worm ate you."
            death()

def poison():
    print "The hell worm is a particularly nasty insect, more dragon cycloptic then worm, it\'s teeth are sharper then diamonds."
    print "Your instructors taught you well however and you know the only two ways to incapacitate a hell worm.
    print "Where must you attack on the hell worm to survive?"
    
    choice = raw_input("> ")
    
    while choice != "eye" or choice != "tongue":
    
        if choice == "eye": 
            print "You attack the hell worm's eye with your spade, blinding it."
            print "It's a good thing you paid extra attention in \'Violent Creatures and How to Use Them: 101 \'."
            print "You keep digging until you finally emerge on the other side of the wall."
            sphinx()
    
        elif choice == "tongue":
            print "You stabbed the hell worms tongue."
            print "You knicked yourself in the process however on it\'s diamond teeth."
            print "You better get out of the maze quickly before you bleed to death!"
            sphinx()
    
        else: 
            print "You couldn't remember where to attack and the hell worm ate you."
            death() 
            
            
def yourself():
    print "The hell worm is a particularly nasty insect, more dragon cycloptic then worm, it\'s teeth are sharper then diamonds."
    print "Your instructors taught you well however and you know the only two ways to incapacitate a hell worm.
    print "Where must you attack on the hell worm to survive?"
    
    choice = raw_input("> ")
    
    while choice != "eye" or choice != "tongue":
    
        if choice == "eye": 
            print "You attack the hell worm's eye with your spade, blinding it."
            print "It's a good thing you paid extra attention in \'Violent Creatures and How to Use Them: 101 \'."
            print "You keep digging until you finally emerge on the other side of the wall."
            sphinx()
    
        elif choice == "tongue":
            print "You stabbed the hell worms tongue."
            print "You knicked yourself in the process however on it\'s diamond teeth."
            print "You better get out of the maze quickly before you bleed to death!"
            sphinx()
    
        else: 
            print "You couldn't remember where to attack and the hell worm ate you."
            death()  
        
        
def lorr1():
    print "You continue on until the path ends."
    print "You must go left or right"
    print "Which way will you go?"
    choice = raw_input("> ")
    
    while choice != "left" or choice != "right":
    
        if choice == "left":
            print "Mr. Spock opens the door."
            poison()
    
        elif choice == "right":
            print "Mr. Spock is annoyed by your actions and nerve pinches you."
            yourself()
    
        else:
            print "Your choices are to go 'left' or 'right'. Seriously how did you even get to this point!?"
            choice = raw_input("> ")

def death():
    print "You failed to navigate the perils of the maze."
    print "But don't feel too bad!."
    print "At least you were brave enough to try! Maybe in your next life you can come back as a Moon Priest instead!"
    print "You were never very suited to this whole killing thing, much better to run around naked on the full moon."
    print "You probably make less friends that want to kill you that way too!"
    exit(0)

def congrats():
    print "Congratulations Ensign, you found Mr. Spock!"
    print "Mr. Spock told you the code and now the Enterprise will not explode!"
    print "Good job Ensign!"
    exit(0)

def start():
    print "You are an apprentice assassain in the Morning Star Guild."
    print "In order to become a full memeber of the guild you must survive the maze."
    print "Few who enter leave, but if you keep your wits about you, you might just make it out alive."
    print "Though probably not in one piece."
    print "Don't worry though, all the best assassins have a missing appendage here or there.\n"
    
    choice = raw_input("Are you sure you want to go in? (y/n)")
    
    if choice == "y":
        enter()
    
    elif choice == "n":
        noenter()
    
    else:
        print "You must choose! \(Enter y or n only!\)\n"
        choice = raw_input("Are you sure you want to go in? (y/n)")
        
start()

#END
    
