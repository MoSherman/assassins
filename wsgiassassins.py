#THE MAZE OF THE ASSASSINS

from mod_python import apache

html_head = """
<html lang="en">
<head>
  <title>ASSASSINS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
      
   
    
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    
    .bg-3 {
      height:100vh;  
      padding-top: 100px;  
      background-color: #000000;
      color: #FFFFFF
      font-size: 20px !important;  
      padding-bottom: 400px;
    }
    
    footer {
      margin-bottom: 0;
      margin-top: 0;  
      background-color: #000000;
      padding: 25px;
      color: #f2f2f2;  
    }
    
    p {
    font-size 18px;
    }
    
    html,body * {
    font-size: 18px;
    color: #FFFFFF
    }
    
    input, textarea {
    background-color : #000000;
    }
      
  </style>
</head>
<body>
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>                        
      </button>
      <a class="navbar-brand" href="wsgiassassins.py/start">The Maze of the Assassins</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="assassin.py">Play Again</a></li>
        <li><a href="map">Map</a></li>
        <li><a href="about">About</a></li>    
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="https://github.com/MoSherman/assassins" target="_blank"> GitHub Repo</a></li>
      </ul>
    </div>
  </div>
</nav>
"""

html_footer = """
        <footer class="container-fluid text-center">
            <p>Copyright &copy; Moriah Sherman 2016</p>
        </footer>
    </body>
</html>
"""

def enter():
    return html_head + """
    <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                Congrats! You passed the first test, had you refused to enter the guild would not have been pleased...
            </p>
            <p class=text-justify>
                There is no turning back now as the door shuts behind you.
            </p>
            <p class=text-justify>
                You see however that there are no doors in the room you are in, just four stone walls. What will you do?
            </p>            
            <FORM value="form" action="enter_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
    </div>
</body>
</html>
"""
def enter_choice(req):
    
    info     = req.form
    choice   = info['choice']
    
    while choice != "climb" or choice != "dig":

        if choice == "climb":
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        You test the strength of the wall and decide to climb over.
                    </p>
                    <p class=text-justify>
                        You manage to avoid the poison spikes on top of the wall just barely and land silently on the other side.
                    </p>
                    """ + spinhx() + "</div></div></body></html>"
    
        elif choice == "dig":
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        You remove your foldable spade from your bag and begin to dig under the wall in front of you
                    </p>
                    <p class=text-justify>
                        An hour into your digging you start to wonder if you made a bad choice.
                    </p>
                    <p class=text-justify>
                        This is confirmed a moment later when a hell worm bursts through the wall of your tunnel.
                    </p>
                    """ + tunnel() + "</div></div></body></html>"
    
        elif choice == "hint":
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        Congrats! You passed the first test, had you refused to enter the guild would not have been pleased...
                    </p>
                    <p class=text-justify>
                        There is no turning back now as the door shuts behind you.
                    </p>
                    <p class=text-justify>
                        You see however that there are no doors in the room you are in, just four stone walls. What will you do?
                    </p> 
                    <p class=text-justify>
                        HINT: The choices here are 'climb' or 'dig.'
                    </p> 
                        <FORM value="form" action="enter_choice" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                </div>
            </div>
            </body>
            </html>
            """
        
        else:
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        Congrats! You passed the first test, had you refused to enter the guild would not have been pleased...
                    </p>
                    <p class=text-justify>
                        There is no turning back now as the door shuts behind you.
                    </p>
                    <p class=text-justify>
                        You see however that there are no doors in the room you are in, just four stone walls. What will you do?
                    </p> 
                    <p class=text-justify>
                        Your favorite instructor takes pity on your poor start and yells out 'climb or dig you fool!'
                    </p> 
                        <FORM value="form" action="enter_choice" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                </div>
            </div>
            </body>
            </html>
            """

def noenter():
    return "\nYou choose not to enter the maze."
    return "This is a mistake."
    return "'You have failed the first test' yells the master assassin, 'cowards never prosper!'"
    return "The guild is so displeased with you decision that they all attack you at once."
    return "It all happened so quickly no one was really sure what got you in the end."
    return "There wasn't enough left to figure it out really.\n"
    playagain()

def spinhx():
    return """
    <p class=text-justify>
        Before you can even get your bearings you realize you are not alone.
    </p>
    <p class=text-justify>
        Sitting silently before the only exit in front of you is a particularly grumpy looking spinhx.
    </p>
    <p class=text-justify>
        You can not risk running around the spinhx or fighting it as both would mean certain death.
    </p> 
    <p class=text-justify>
        You must answer it's riddle.
    </p> 
    <p class=text-justify>
        The spinhx speaks suddenly in a deep voice but says something rather unexpected.
    </p>
    <p class=text-justify>
        'Look kid I'm not really in the mood for human today so I'll give you an easy one.'
    </p>
    <p class=text-justify>
        'Voiceless it cries,
    </p>
    <p class=text-justify>
        Wingless flutters,
    </p>
    <p class=text-justify>
        Toothless bites,
    </p>
    <p class=text-justify>
        Mouthless mutters.
    </p>
    <p class=text-justify>
        What is it?'
    </p>
    <p class=text-justify>
        'If you don't know what that is then you deserve to be eaten!' The sphinx yells.
    </p>
    <FORM value="form" action="spinhx_choice" method="post">
        <P>            
            <input type="text" name="choice">
        </P>
    </FORM> """

def spinhx_choice(req):
    
    info     = req.form
    choice   = info['choice']
            
    if choice == "wind":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        Despite being not very good with riddles, even you got this one eventually.
                    </p>
                    <p class=text-justify>
                        The cranky spinhx shuffles into the corner to take a nap and you walk through the door before you.
                    </p>
                    """ + lorr1() + "</div></div></body></html>"
        
    elif choice == "hint":
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        'Voiceless it cries,
                    </p>
                    <p class=text-justify>
                        Wingless flutters,
                    </p>
                    <p class=text-justify>
                        Toothless bites,
                    </p>
                    <p class=text-justify>
                        Mouthless mutters.
                    </p>
                    <p class=text-justify>
                        What is it?'
                    </p>
                    <p class=text-justify>
                        HINT: This well known riddle was taken from 'The Hobbit.' 
                    </p>
                    <FORM value="form" action="spinhx_choice" method="post">
                        <P>            
                            <input type="text" name="choice">
                        </P>
                    </FORM>
                </div>
            </div>
            </body>
            </html>
            """
        
    elif choice != "wind" or choice != "hint":
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                    <div class="col-sm-12"> 
                        <p class=text-justify>
                            \'Really?\' says the sphinx \'\"%s\" is you best guess? Do you read!? Try again!\'
                        </p>
                        <FORM value="form" action="spinhx_try2" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                    </div>
                </div>
                </body>
                </html>
                """ % choice
        
def spinhx_try2(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "wind":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        Despite being not very good with riddles, even you got this one eventually.
                    </p>
                    <p class=text-justify>
                        The cranky spinhx shuffles into the corner to take a nap and you walk through the door before you.
                    </p>
                    """ + lorr1() + "</div></div></body></html>"
        
    elif choice == "hint":
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        'Voiceless it cries,
                    </p>
                    <p class=text-justify>
                        Wingless flutters,
                    </p>
                    <p class=text-justify>
                        Toothless bites,
                    </p>
                    <p class=text-justify>
                        Mouthless mutters.
                    </p>
                    <p class=text-justify>
                        What is it?'
                    </p>
                    <p class=text-justify>
                        HINT: This well known riddle was taken from 'The Hobbit.' 
                    </p>
                    <FORM value="form" action="spinhx_try2" method="post">
                        <P>            
                            <input type="text" name="choice">
                        </P>
                    </FORM>
                </div>
            </div>
            </body>
            </html>
            """
        
    elif choice != "wind" or choice != "hint":
            return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                    <div class="col-sm-12"> 
                        <p class=text-justify>
                            \'Really?\' says the sphinx \'\"%s\" is you best guess? Do you read!? Last Chance!!\'
                        </p>
                        <FORM value="form" action="spinhx_try3" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                    </div>
                </div>
                </body>
                </html>
                """ % choice
        
def spinhx_try3(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "wind":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        Despite being not very good with riddles, even you got this one eventually.
                    </p>
                    <p class=text-justify>
                        The cranky spinhx shuffles into the corner to take a nap and you walk through the door before you.
                    </p>
                    """ + lorr1() + "</div></div></body></html>"
        
    elif choice == "hint":
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        'Voiceless it cries,
                    </p>
                    <p class=text-justify>
                        Wingless flutters,
                    </p>
                    <p class=text-justify>
                        Toothless bites,
                    </p>
                    <p class=text-justify>
                        Mouthless mutters.
                    </p>
                    <p class=text-justify>
                        What is it?'
                    </p>
                    <p class=text-justify>
                        HINT: This well known riddle was taken from 'The Hobbit.' 
                    </p>
                    <FORM value="form" action="spinhx_try3" method="post">
                        <P>            
                            <input type="text" name="choice">
                        </P>
                    </FORM>
                </div>
            </div>
            </body>
            </html>
            """
        
    elif choice != "wind" or choice != "hint":
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        'My patience is gone and your futile attempts have made me hangry!' says the spinhx.
                    </p>
                    <p class=text-justify>
                        It grabs you and though you struggle mightily there is no escape!
                    </p>
                    """ + death() + "</div></div></body></html>"        

def tunnel():
    
    return """
            <p class=text-justify>
                The hell worm is a particularly nasty insect, more cycloptic dragon then worm, it\'s teeth are sharper than diamonds.
            </p>
            <p class=text-justify>
                Your instructors taught you well however and you know the only two ways to incapacitate a hell worm.
            </p>
            <p class=text-justify>
                Where must you attack on the hell worm to survive?
            </p>            
            <FORM value="form" action="tunnel_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
            """

def tunnel_choice(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "eye":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        You attack the hell worm's eye with your spade, blinding it.
                    </p>
                    <p class=text-justify>
                        It's a good thing you paid extra attention in \'Violent Creatures and How to Use Them: 101 \'.
                    </p>
                    <p class=text-justify>
                        You keep digging until you finally emerge on the other side of the wall.
                    </p>
                    """ + spinhx() + "</div></div></body></html>"
    
    elif choice == "tongue":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        You stabbed the hell worms tongue.
                    </p>
                    <p class=text-justify>
                        You nicked yourself in the process however on it\'s diamond teeth.
                    </p>
                    <p class=text-justify>
                        You better get out of the maze quickly before you bleed to death!
                    </p>
                    <p class=text-justify>
                        You keep digging and eventually you emerge into the next room..
                    </p>
                    """ + spinhx() + "</div></div></body></html>"
    
    elif choice == "hint":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                The hell worm is a particularly nasty insect, more dragon cycloptic then worm, it\'s teeth are sharper than diamonds.
            </p>
            <p class=text-justify>
                Your instructors taught you well however and you know the only two ways to incapacitate a hell worm.
            </p>
            <p class=text-justify>
                Where must you attack on the hell worm to survive?
            </p>
            <p class=text-justify>
                HINT: You can either attack the hell worms 'eye' or 'tongue.'
            </p> 
            <FORM value="form" action="tunnel_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
    </div>
</body>
</html>
"""
    else:
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        You couldn't remember where to attack and the hell worm ate you.
                    </p>
                    <p class=text-justify>
                        Jeez what a nasty way to go!
                    </p>
                    """ + death() + "</div></div></body></html>"
    
    
def poison():
    return "\nYou turn left and continue on until you enter another room."
    return "Suddenly the door slams shut behind you."
    return "There will be no way out of this room by brute force you observe, as the walls, ceiling, and floor are made of troll steel."
    return "A table stand in the the room upon which sits three glasses filled with unknown liquids."
    return "\nApparently two of the glasses contain poison, while a third is a potion which will give you the ability to walk through walls for about 10 seconds."
    return "On the wall of the room is written only this: Audaces fortuna iuvat."
    return "You must drink either the 'yellow', 'green', or 'blue' liquids. Which will you choose?\n"
    
    choice = raw_input("> ")
    
    while choice != "yellow" or choice != "green" or choice != "blue":
    
        if choice == "yellow" or choice == "green" or choice == "blue": 
            return "\nYou know that fortune favours the bold."
            return "So you grab the %r liquid\'s glass and gulp it down." % choice
            return "As you sreturn at the wall, you really hope fortune also favours the reckless.\n"
            yourself()
            
        else: 
            return "\nYou choose not to drink any of the specified coloured liquids."
            return "What you did not know was that fortune does not favour the coward, and had you drank from any of the glasses, you could have passed through the wall."
            return "Instead you were stuck in the room until your bitter end.\n"
            death() 
            
            
def yourself():
    return "\nYou enter the next room and realize that only one obstacle stand between you and the exit to the maze."
    return "At first you believe there to be a mirror in the room, but alas the person before you is very real."
    return "Then you remember what makes a true assassin. Knowing that you can be your own worst enemy."
    return "You know the doppelganger before you is identical in every way, conjured here by magic from the witches guild."
    return "You begin to spar with yourself, but you seem to be evenly matched."
    return "How will you get to the exit?\n"
    
    choice = raw_input("> ")
    
    while choice != "kill" or choice != "run":
    
        if choice == "kill": 
            return "\nYou know that even the best assassin can be beaten."
            return "You fight valiantly for hours and hours, and eventually the magic animating the doppelganger begins to fade."
            return "As the last wisps of smoke from what was once your doppelganger rises out of the maze, you stumble towards the exit.\n"
            congrats()
    
        elif choice == "run":
            return "\nYou could not face yourself."
            return "You try to run around the doppelganger but he stabs you in the back like any good assassin would."
            return "You failed in your final test: believing in yourself, even against yourself.\n"
            death()
    
        else: 
            return "\nYou only have two choices: 'kill' the doppelganger or 'run' to the door.\n"
            choice = raw_input("> ")  
        
        
def lorr1():
    return "\nYou continue on until the path ends."
    return "You must go left or right"
    return "Which way will you go?\n"
    choice = raw_input("> ")
    
    while choice != "left" or choice != "right":
    
        if choice == "left":
            poison()
    
        elif choice == "right":
            yourself()
    
        else:
            return "\nYour choices are to go 'left' or 'right'. Seriously how did you even get to this point!?\n"
            choice = raw_input("> ")

def death():
    return "\nYou failed to navigate the perils of the maze."
    return "But don't feel too bad!."
    return "At least you were brave enough to try! Maybe in your next life you can come back as a Moon Priest instead!"
    return "You were never very suited to this whole killing thing, much better to run around naked on the full moon."
    return "You probably make less friends that want to kill you that way too!\n"
    playagain()

def congrats():
    return "\nAs you make it past the door you glance back once last time and bow your head."
    return "You have proved yourself to be worthy of joining the guild, but you remember all those who tried and failed before you."
    return "The life of an assassin is not for everyone, but you have proven yourself beyond doubt."
    return "You exit the maze to a round of applause from you instructors."
    return "Your favourite instructor yells out only one piece of wisdom, the true lesson of the maze: Non mortem timemus, sed cogitationem mortis.\n"
    playagain()

def playagain():
    return "Would you like to try and navigate the maze again?\n"
    
    choice = raw_input("(y/n) ")
    
    if choice == "y":
        start()
    
    elif choice == "n":
        noenter()
    
    else:
        return "You must choose! \(Enter y or n only!\)\n"
        choice = raw_input("(y/n) ")

    
        
def start():
    return html_head + """
    <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                You are an apprentice assassin in the Morning Star Guild.
            </p>
            <p class=text-justify>
                In order to become a full member of the guild you must survive the maze.
            </p>
            <p class=text-justify>
                Few who enter leave, but if you keep your wits about you, you might just make it out alive.
            </p>
            <p class=text-justify>
                Though probably not in one piece.
            </p>
            <p class=text-justify>
                Don't worry though, all the best assassins have a missing appendage here or there.
            </p>
            <p class=text-justify>
                Type 'hint' if you are not sure what your options are at any given task.
            </p>
            <p class=text-justify>
                Are you sure you want to go in? (y/n)
            </p>
            <FORM value="form" action="start_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
    </div>
</body>
</html>
"""
#<input type=\"text\" color:#FFFFFF value=\">\" style=\"background-color:transparent;border:0px solid white;>

def start_choice(req):
    
    info     = req.form
    choice   = info['choice']

    if choice == "y":
        return enter()
    
    elif choice == "n":
        return noenter()
    
    else:
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
            <div class="col-sm-12"> 
            <p class=text-justify>
                You are an apprentice assassin in the Morning Star Guild.
            </p>
            <p class=text-justify>
                In order to become a full member of the guild you must survive the maze.
            </p>
            <p class=text-justify>
                Few who enter leave, but if you keep your wits about you, you might just make it out alive.
            </p>
            <p class=text-justify>
                Though probably not in one piece.
            </p>
            <p class=text-justify>
                Don't worry though, all the best assassins have a missing appendage here or there.
            </p>
            <p class=text-justify>
                Type 'hint' if you are not sure what your options are at any given task.
            </p>
            <p class=text-justify>
                Are you sure you want to go in? (y/n)
            </p>
            <p class=text-justify>
                You can only input 'y' or 'n' to procede. 
            </p>
            <FORM value="form" action="start_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
    </div>
</body>
</html>
"""


#END
