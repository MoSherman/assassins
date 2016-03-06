#THE MAZE OF THE ASSASSINS

from mod_python import apache
import os

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
      <a class="navbar-brand" href="start">The Maze of the Assassins</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="start">Play Again</a></li>
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
                    """ + sphinx() + "</div></div></body></html>"
    
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
                        Your favourite instructor takes pity on your poor start and yells out 'climb or dig you fool!'
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
    return html_head + """
    <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                You choose not to enter the maze.
            </p>
            <p class=text-justify>
                This is a mistake.
            </p>
            <p class=text-justify>
                'You have failed the first test' yells the master assassin.
            </p>
            <p class=text-justify>
                'A man that flies from his fear may find that he has only taken a short cut to meet it.' he finishes in a whisper.
            </p>
            <p class=text-justify>
                The guild is so displeased with your decision that they all attack you at once.
            </p>
            <p class=text-justify>
                It all happened so quickly no one was really sure what got you in the end.
            </p>
            <p class=text-justify>
                There wasn't enough left to figure it out really.
            </p>
            """ + playagain() + "</div></div></body></html>"

def sphinx():
    return """
    <p class=text-justify>
        Before you can even get your bearings you realize you are not alone.
    </p>
    <p class=text-justify>
        Sitting silently before the only exit in front of you is a particularly grumpy looking sphinx.
    </p>
    <p class=text-justify>
        You can not risk running around the sphinx or fighting it as both would mean certain death.
    </p> 
    <p class=text-justify>
        You must answer it's riddle.
    </p> 
    <p class=text-justify>
        The sphinx speaks suddenly in a deep voice but says something rather unexpected.
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
    <FORM value="form" action="sphinx_choice" method="post">
        <P>            
            <input type="text" name="choice">
        </P>
    </FORM> """

def sphinx_choice(req):
    
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
                        The cranky sphinx shuffles into the corner to take a nap and you walk through the door before you.
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
                    <FORM value="form" action="sphinx_choice" method="post">
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
                        <FORM value="form" action="sphinx_try2" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                    </div>
                </div>
                </body>
                </html>
                """ % choice
        
def sphinx_try2(req):
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
                        The cranky sphinx shuffles into the corner to take a nap and you walk through the door before you.
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
                    <FORM value="form" action="sphinx_try2" method="post">
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
                        <FORM value="form" action="sphinx_try3" method="post">
                            <P>            
                                <input type="text" name="choice">
                            </P>
                        </FORM>
                    </div>
                </div>
                </body>
                </html>
                """ % choice
        
def sphinx_try3(req):
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
                        The cranky sphinx shuffles into the corner to take a nap and you walk through the door before you.
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
                    <FORM value="form" action="sphinx_try3" method="post">
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
                        'My patience is gone and your futile attempts have made me hangry!' says the sphinx.
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
                    """ + sphinx() + "</div></div></body></html>"
    
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
                    """ + sphinx() + "</div></div></body></html>"
    
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
    return """
            <p class=text-justify>
                You continue on until you enter another room.
            </p>
            <p class=text-justify>
                Suddenly the door slams shut behind you.
            </p>
            <p class=text-justify>
                There will be no way out of this room by brute force you observe, as the walls, ceiling, and floor are made of troll steel.
            </p>
            <p class=text-justify>
                A table stand in the the room upon which sits three glasses filled with unknown liquids.
            </p>
            <p class=text-justify>
                Apparently two of the glasses contain poison, while a third is a potion which will give you the ability to walk through walls for about 10 seconds.
            </p>
            <p class=text-justify>
                On the wall of the room is written only this: Audaces fortuna iuvat.
            </p>
            <p class=text-justify>
                You must drink either the 'yellow', 'green', or 'blue' liquids. Which will you choose?
            </p>
            <FORM value="form" action="poison_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
            """

def poison_choice(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "yellow" or choice == "green" or choice == "blue":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12"> 
                    <p class=text-justify>
                        You know that fortune favours the bold.
                    </p>
                    <p class=text-justify>
                        So you grab the %r liquid\'s glass and gulp it down.
                    </p>
                    <p class=text-justify>
                        As you run at the wall, you really hope fortune also favours the reckless.
                    </p>
                    """ % choice.strip('choic()\'') + yourself() + "</div></div></body></html>" 
    
    elif choice == "hint":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        On the wall of the room is written only this: Audaces fortuna iuvat.
                    </p>
                    <p class=text-justify>
                        You must drink either the 'yellow', 'green', or 'blue' liquids. Which will you choose?
                    </p>
                    <p class=text-justify>
                        HINT: You only ever lose the games you don\'t play.
                    </p>
                    <p class=text-justify>
                        Taking the leap can be the hardest part, but entering the arena is winning. 
                    </p>
                    <p class=text-justify>
                        Still need some inspiration? Try <u><strong><a href="http://zenpencils.com/comic/142-timothy-ferriss-someday/" target="_blank">this.</a></strong></u>
                    </p>
                    <p class=text-justify>
                        Or another favourite of mine: <u><strong><a href="http://zenpencils.com/comic/theodore-roosevelt-the-man-in-the-arena/" target="_blank">this.</a></strong></u>
                    </p>
                    <FORM value="form" action="poison_choice" method="post">
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
                        You choose not to drink any of the specified coloured liquids.
                    </p>
                    <p class=text-justify>
                        What you did not know was that fortune does not favour the coward, and had you drank from any of the glasses, you could have passed through the wall.
                    </p>
                    <p class=text-justify>
                        Instead you were stuck in the room until your bitter end.
                    </p>
                    """ + death() + "</div></div></body></html>"            
            
def yourself():
     return """
            <p class=text-justify>
                You enter the next room and realize that only one obstacle stands between you and the exit to the maze.
            </p>
            <p class=text-justify>
                At first you believe there to be a mirror in the room, but alas the person before you is very real.
            </p>
            <p class=text-justify>
                Then you remember what makes a true assassin. Knowing that you can be your own worst enemy.
            </p>
            <p class=text-justify>
                You know the doppelganger before you is identical in every way, conjured here by magic from the witches guild.
            </p>
            <p class=text-justify>
                You begin to spar with yourself, but you seem to be evenly matched.
            </p>
            <p class=text-justify>
                How will you get to the exit?
            </p>
            <FORM value="form" action="yourself_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
            """

def yourself_choice(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "kill":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        You know that even the best assassin can be beaten, and magic is no match for determination.
                    </p>
                    <p class=text-justify>
                        You fight valiantly for hours and hours, and eventually the magic animating the doppelganger begins to fade.
                    </p>
                    <p class=text-justify>
                        As the last wisps of smoke from what was once your doppelganger rises out of the maze, you stumble towards the exit.
                    </p>
                    """ + congrats() + "</div></div></body></html>"
    
    elif choice == "run":
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        You could not face yourself.
                    </p>
                    <p class=text-justify>
                        You try to run around the doppelganger but he stabs you in the back like any good assassin would.
                    </p>
                    <p class=text-justify>
                        You failed in your final test: believing in yourself, even against yourself.
                    </p>
                    """ + death() + "</div></div></body></html>"
    
    else:
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        How will you get to the exit?
                    </p>
                    <p class=text-justify>
                        HINT: You can choose to either 'kill' or 'run.'
                    </p>
                    <p class=text-justify>
                        But choose carefully, a mis-step here will certainly end in your death.
                    </p>
                    <p class=text-justify>
                        Still not sure what to do? Try <u><strong><a href="http://zenpencils.com/comic/114-playing-the-game/" target="_blank">this.</a></strong></u>
                    </p>
                    <FORM value="form" action="yourself_choice" method="post">
                        <P>            
                            <input type="text" name="choice">
                        </P>
                    </FORM>
                </div>
           </div>
           </body>
           </html>
           """
    
def lorr1():
    return """
            <p class=text-justify>
                You continue on until the path beyond the door ends.
            </p>
            <p class=text-justify>
                You must go left or right.
            </p>
            <p class=text-justify>
                Which way will you go?
            </p>    
            <FORM value="form" action="lorr1_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
            """

def lorr1_choice(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "left":
         return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        You chose left, lets hope it was a good choice!
                    </p>
                    """ + poison() + "</div></div></body></html>"
    
    elif choice == "right":
        return html_head + """
            <div class="container-fluid bg-3 text-justify"> 
                <div class="col-sm-12">
                    <p class=text-justify>
                        You chose right, lets hope it was a good choice!
                    </p>
                    """ + yourself() + "</div></div></body></html>"
        
    else:
        return html_head + """
    <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                You continue on until the path beyond the door ends.
            </p>
            <p class=text-justify>
                You must go left or right.
            </p>
            <p class=text-justify>
                Which way will you go?
            </p>
            <p class=text-justify>
                You can\'t possibly need a 'hint' here!?! It\'s only 'left' or 'right.'
            </p>
            <FORM value="form" action="lorr1_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
    </div>
</body>
</html>
"""
        

def death():
    return """
            <p class=text-justify>
                You failed to navigate the perils of the maze.
            </p>
            <p class=text-justify>
                But don't feel too bad!
            </p>
            <p class=text-justify>
                At least you were brave enough to try! Maybe in your next life you can come back as a Moon Priest instead!
            </p>
            <p class=text-justify>
                You were never very suited to this whole killing thing, much better to run around naked on the full moon.
            </p>
            <p class=text-justify>
                You probably make less friends that want to kill you that way too!
            </p>
            """ + playagain()

def congrats():
    return """
            <p class=text-justify>
                As you make it past the door you glance back once last time and bow your head.
            </p>
            <p class=text-justify>
                You have proved yourself to be worthy of joining the guild, but you remember all those who tried and failed before you.
            </p>
            <p class=text-justify>
                The life of an assassin is not for everyone, but you have proven yourself beyond doubt.
            </p>
            <p class=text-justify>
                You exit the maze to a round of applause from you instructors.
            </p>
            <p class=text-justify>
                Your favourite instructor yells out only one piece of wisdom, the true lesson of the maze: Non mortem timemus, sed cogitationem mortis.
            </p>
            """ + playagain()

def playagain():
    return """
            <p class=text-justify>
                Would you like to try and navigate the maze again?  (Enter y or n only!)  
            </p>
            <FORM value="form" action="playagain_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
            """

def playagain_choice(req):
    info     = req.form
    choice   = info['choice']
    
    if choice == "y":
        return start()
    
    elif choice == "n":
        return about()
    else:
        return html_head + """
        <div class="container-fluid bg-3 text-justify"> 
        <div class="col-sm-12"> 
            <p class=text-justify>
                Would you like to try and navigate the maze again?  (Enter y or n only!)
            </p>
            <p class=text-justify>
                You can only eneter 'y' for yes or 'n' for no.
            </p>
            <FORM value="form" action="playagain_choice" method="post">
                <P>            
                    <input type="text" name="choice">
                </P>
            </FORM>
        </div>
        </div>
        </body>
        </html>
        """
        
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
                You can only input 'y' or 'n' to proceed. 
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

def about():

    return html_head + """
    <div class="container-fluid bg-3 text-center">    
    <h1><strong>About The Assassains Maze</strong></h1><br>
    <div class="col-sm-2"> 
    </div>
    <div class="col-sm-8"> 
        <p class=text-justify>This simple game is an ongoing attempt to try out my Python skills and show them off. This project uses a Bootstrap template to be accessible to both desktop and mobile users. Future iterations of the project will hopefully include many more rooms, images of the scenes, a 'decision' tracker, and improved aesthetics. The code for this project can be viewed at my <u><strong><a href="https://github.com/MoSherman/assassins.git" target="_blank">GitHub.com assassins repository</a></strong></u>.</p>
        <p class=text-justify>If you would like to play the game in your terminal, please download the <u><strong><a href="https://github.com/MoSherman/assassins/blob/master/assassins.py" target="_blank">assassins.py</a></strong></u> file from my GitHub profile. Save in a directory of your choosing and open a terminal to that directory. Enter the following command: <strong>python assassins.py</strong>, and the game will begin running in your terminal.
    </div>
    <div class="col-sm-2"> 
    </div>
    </div>
    </body>
    </html>
    """

def map():

    return html_head + """
    <div class="container-fluid bg-3 text-center">    
    <h1><strong>Map of The Assassains Maze</strong></h1><br>
    <div class="col-sm-2"> 
    </div>
    <div class="col-sm-8"> 
        <p class=text-justify>The maze is relatively simple for now, but as I learn more skills I hope to expand the maze. If you want to check on any ongoing updates to the maze check my <u><strong><a href="https://github.com/MoSherman/assassins.git" target="_blank">GitHub.com assassins repository</a></strong></u>.</p>
        <p class=text-justify>The map is available on my <u><strong><a href="https://twitter.com/MoriahEVSherman/status/704290248717705217/photo/1" target="_blank">Twitter</a><strong></u>.</p> 
    </div>
    <div class="col-sm-2"> 
    </div>
    </div>
    </body>
    </html>
    """ 


#END
