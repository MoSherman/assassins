#THE MAZE OF THE ASSASSINS

from sys import exit

def enter():
    print "\nCongrats! You passed the first test, had you refused to enter the guild would not have been pleased..."
    print "There is no turning back now as the door shuts behind you."
    print "You see however that there are no doors in the room you are in, just four stone walls. What will you do?\n"
    
    choice = raw_input("> ")
    
    while choice != "climb" or choice != "dig":
    
        if choice == "climb": 
            print "\nYou test the strength of the wall and decide to climb over."
            print "You manage to avoid the poison spikes on top of the wall just barely and land silently on the other side.\n"
            spinhx()
    
        elif choice == "dig":
            print "\nYou remove your foldable spade from your bag and begin to dig under the wall in front of you."
            print "In hour into your digging you start to wonder if you made a bad choice."
            print "This is confirmed a moment later when a hell worm bursts through the wall of you tunnel.\n"
            
            tunnel()
        
        elif choice == "hint":
            print "\nYou can either 'climb' or 'dig.'\n"
            choice = raw_input("> ")
    
        else: 
            print "\nYour favorite instructor takes pity on your poor start and yells out 'climb or dig you fool!'.\n"
            choice = raw_input("> ")

def noenter():
    print "\nYou choose not to enter the maze."
    print "This is a mistake."
    print "'You have failed the first test' yells the master assassin, 'cowards never prosper!'"
    print "The guild is so displeased with you decision that they all attack you at once."
    print "It all happened so quickly no one was really sure what got you in the end."
    print "There wasn't enough left to figure it out really.\n"
    exit(0)

def spinhx():
    print "Before you can even get your bearings you realize you are not alone.\n"
    print "Sitting silently before the only exit in front of you is a particularly grumpy looking spinhx."
    print "You can not risk running around the spinhx or fighting it as both would mean certain death."
    print "You must answer it's riddle."
    print "The spinhx speaks suddenly in a deep voice but says something rather unexpected.\n"
    print "'Look kid I\'m not really in the mood for human today so I\'ll give you an easy one.'\n"
    print "'Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters."
    print "\n'If you don\'t know what that is then you deserve to be eaten!' 'The sphinx yells.'"
    
    
    choice = raw_input("\n> ")
    guesses = 0
    
    while choice != 'wind' or choice != 'hint' and guesses < 2:
            
        if choice == "wind":
            print "\nDespite being not very good with riddles, even you got this one eventually."
            print "The cranky spinhx shuffles into the corner to take a nap and you walk through the door before you.\n"
            lorr1()
    
        elif choice == "hint":
            print "\nThis well known riddle was taken from 'The Hobbit.'\n"
            choice = raw_input("> ")
        
        elif choice != "wind" or choice != "hint":
            print "\n\'Really?\' says the sphinx \%r is you best guess? Do you read!? Try again!\'\n" % choice
            guesses += 1
            choice = raw_input("> ")
        
        else:
            print "\n'My patience is gone and your futile attempts have made me hangry!' says the spinhx."
            print "It grabs you and though you struggle mightily there is no escape!\n"
            death()

def tunnel():
    print "\nThe hell worm is a particularly nasty insect, more dragon cycloptic then worm, it\'s teeth are sharper than diamonds."
    print "Your instructors taught you well however and you know the only two ways to incapacitate a hell worm."
    print "Where must you attack on the hell worm to survive?\n"
    
    choice = raw_input("> ")
    
    while choice != "eye" or choice != "tongue":
    
        if choice == "eye": 
            print "\nYou attack the hell worm's eye with your spade, blinding it."
            print "It's a good thing you paid extra attention in \'Violent Creatures and How to Use Them: 101 \'."
            print "You keep digging until you finally emerge on the other side of the wall.\n"
            spinhx()
    
        elif choice == "tongue":
            print "\nYou stabbed the hell worms tongue."
            print "You nicked yourself in the process however on it\'s diamond teeth."
            print "You better get out of the maze quickly before you bleed to death!\n"
            print "You keep digging and eventually you emerge into the next room.\n"
            spinhx()
            
        elif choice == "hint":
            print "\nYou can either attack the hell worms 'eye' or 'tongue.'\n"
            choice = raw_input("> ")
    
        else: 
            print "\nYou couldn't remember where to attack and the hell worm ate you.\n"
            death()

def poison():
    print "\nYou turn left and continue on until you enter another room."
    print "Suddenly the door slams shut behind you."
    print "There will be no way out of this room by brute force you observe, as the walls, ceiling, and floor are made of troll steel."
    print "A table stand in the the room upon which sits three glasses filled with unknown liquids."
    print "\nApparently two of the glasses contain poison, while a third is a potion which will give you the ability to walk through walls for about 10 seconds."
    print "On the wall of the room is written only this: Audaces fortuna iuvat."
    print "You must drink either the 'yellow', 'green', or 'blue' liquids. Which will you choose?\n"
    
    choice = raw_input("> ")
    
    while choice != "yellow" or choice != "green" or choice != "blue":
    
        if choice == "yellow" or choice == "green" or choice == "blue": 
            print "\nYou know that fortune favours the bold."
            print "So you grab the %r liquid\'s glass and gulp it down." % choice
            print "As you sprint at the wall, you really hope fortune also favours the reckless.\n"
            yourself()
            
        else: 
            print "\nYou choose not to drink any of the specified coloured liquids."
            print "What you did not know was that fortune does not favour the coward, and had you drank from any of the glasses, you could have passed through the wall."
            print "Instead you were stuck in the room until your bitter end.\n"
            death() 
            
            
def yourself():
    print "\nYou enter the next room and realize that only one obstacle stand between you and the exit to the maze."
    print "At first you believe there to be a mirror in the room, but alas the person before you is very real."
    print "Then you remember what makes a true assassin. Knowing that you can be your own worst enemy."
    print "You know the doppelganger before you is identical in every way, conjured here by magic from the witches guild."
    print "You begin to spar with yourself, but you seem to be evenly matched."
    print "How will you get to the exit?\n"
    
    choice = raw_input("> ")
    
    while choice != "kill" or choice != "run":
    
        if choice == "kill": 
            print "\nYou know that even the best assassin can be beaten."
            print "You fight valiantly for hours and hours, and eventually the magic animating the doppelganger begins to fade."
            print "As the last wisps of smoke from what was once your doppelganger rises out of the maze, you stumble towards the exit.\n"
            congrats()
    
        elif choice == "run":
            print "\nYou could not face yourself."
            print "You try to run around the doppelganger but he stabs you in the back like any good assassin would."
            print "You failed in your final test: believing in yourself, even against yourself.\n"
            death()
    
        else: 
            print "\nYou only have two choices: 'kill' the doppelganger or 'run' to the door.\n"
            choice = raw_input("> ")  
        
        
def lorr1():
    print "\nYou continue on until the path ends."
    print "You must go left or right"
    print "Which way will you go?\n"
    choice = raw_input("> ")
    
    while choice != "left" or choice != "right":
    
        if choice == "left":
            poison()
    
        elif choice == "right":
            yourself()
    
        else:
            print "\nYour choices are to go 'left' or 'right'. Seriously how did you even get to this point!?\n"
            choice = raw_input("> ")

def death():
    print "\nYou failed to navigate the perils of the maze."
    print "But don't feel too bad!."
    print "At least you were brave enough to try! Maybe in your next life you can come back as a Moon Priest instead!"
    print "You were never very suited to this whole killing thing, much better to run around naked on the full moon."
    print "You probably make less friends that want to kill you that way too!\n"
    exit(0)

def congrats():
    print "\nAs you make it past the door you glance back once last time and bow your head."
    print "You have proved yourself to be worthy of joining the guild, but you remember all those who tried and failed before you."
    print "The life of an assassin is not for everyone, but you have proven yourself beyond doubt."
    print "You exit the maze to a round of applause from you instructors."
    print "Your favourite instructor yells out only one piece of wisdom, the true lesson of the maze: Non mortem timemus, sed cogitationem mortis.\n"
    exit(0)

def start():
    print "\nYou are an apprentice assassin in the Morning Star Guild."
    print "In order to become a full member of the guild you must survive the maze."
    print "Few who enter leave, but if you keep your wits about you, you might just make it out alive."
    print "Though probably not in one piece."
    print "Don't worry though, all the best assassins have a missing appendage here or there.\n"
    print "Type 'hint' if you are not sure what your options are at any given task.\n"
    
    choice = raw_input("Are you sure you want to go in? (y/n) ")
    
    if choice == "y":
        enter()
    
    elif choice == "n":
        noenter()
    
    else:
        print "You must choose! \(Enter y or n only!\)\n"
        choice = raw_input("Are you sure you want to go in? (y/n) ")
        
start()

#END