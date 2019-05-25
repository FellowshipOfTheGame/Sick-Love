# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define t = Character("Professor", color = "#36F3AE", what_color = "#2BD798",what_prefix='"', what_suffix='"')
define s = Character("Sofia", color = "#00b3f4", what_color = "#49daff",what_prefix='"', what_suffix='"')
define p = Character("[povname]", color = "#e0e0e0", what_color = "#ffffff", what_prefix='"', what_suffix='"')


# Declare all background images here
image bg room = im.Scale("bgroom.png", 1366, 768)
image bg library = im.Scale("bglibrary.png", 1366, 768)
image bg gym = im.Scale("bggym.png", 1366, 768)
image bg classroom = im.Scale("bgclassroom.png", 1366, 768)
image bg museum = im.Scale("bgmuseum.png", 1366, 768)
image bg arcade = im.Scale("bgarcade.png", 1366, 768)
image bg movies = im.Scale("bgmovies.png", 1366, 768)
image black = "#000"

#Declare all sofia images here
image sofia standing = im.Scale("sofia.png", 1365, 840)
image sofia happy = im.Scale("sofia_sorrindo.png", 1365, 840)
image sofia sad = im.Scale("sofia_triste.png", 1365, 840)
image sofia angry = im.Scale("sofia_braba.png", 1365, 840)
image sofia crying = im.Scale("sofia_chorando.png", 1365, 840)
image sofia evasive = im.Scale("sofia_evasiva.png", 1365, 840)
image sofia upset = im.Scale("sofia_irritada.png", 1365, 840)
image sofia shy = im.Scale("sofia_envergonhada.png", 1365, 840)
image sofia cell = im.Scale("sofiacell.png", 390, 670)

transform noghost:
    xalign 0.5
    yalign -0.9
    
transform arantesnoghost:
    xalign 0.5
    yalign 1.0
    
transform celltransform:
    xalign 0.5
    yalign 0.5

define m = Character("Mariana", color = "#c23ed1", what_color = "#ba38c9",what_prefix='"', what_suffix='"')

define b = Character("Bruno", color = "#db8181", what_color = "#ce7575",what_prefix='"', what_suffix='"')

define d = Character("Diego", color = "#ceb282", what_color = "#bfa57a",what_prefix='"', what_suffix='"')


#Declare all mariana images here
image mariana standing = im.Scale("marianaidle.png", 504, 600)
image mariana evasive = im.Scale("marianaevasive.png", 504, 600)
image mariana sad = im.Scale("marianasad.png", 504, 600)
image mariana excited = im.Scale("marianaexcited.png", 504, 600)
image mariana blushed = im.Scale("marianablushed.png", 504, 600)
image mariana happy = im.Scale("marianahappy.png", 504, 600)
image mariana cell = im.Scale("marianacell.png", 390, 670)

image professor = im.Scale("professor.png", 504, 600)




#Variables of story decision

label checkInterlude(date):  
    if nDatesSofia == 3 or nDatesMariana == 3 or nDatesRafaela == 3:
        jump part2
    else:
        jump expression date
    return

# The game starts here.

label start:

        #Variables need to be initialized here!!!
        $ nDatesSofia = 0
        $ nDatesMariana = 0
        $ nDatesRafaela = 0

        play music "sounds/song1.wav"

        #Só pro SSS
        #jump screenshotsaturday
        python:
            povname = renpy.input("Qual seu nome?")
            povname = povname.strip()

            if not povname:
                povname = "Protagonista-kun"

        call intro

        call checkInterlude("interlude1")
        
        call checkInterlude("interlude2")
             
        call checkInterlude("interlude3")
            
        call checkInterlude("interlude4")
        
        call checkInterlude("interlude5")
        
        call checkInterlude("goodEnding")
        
        return
