# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define t = Character("Professor", color = "#751aff", what_color = "#944dff",what_prefix='"', what_suffix='"')
define s = Character("Sofia", color = "#0083b3", what_color = "#00a8e6",what_prefix='"', what_suffix='"')
define p = Character("[povname]", color = "#e6e6e6", what_color = "#ffffff", what_prefix='"', what_suffix='"')
define m = Character("Mariana", color = "#c23ed1", what_color = "#ba38c9",what_prefix='"', what_suffix='"')
define b = Character("Bruno", color = "#b33232", what_color = "#cd4c4c",what_prefix='"', what_suffix='"')
define d = Character("Diego", color = "#5c4724", what_color = "#816432",what_prefix='"', what_suffix='"')
define r = Character("Rafaela", color = "#b20000", what_color = "#e60000",what_prefix='"', what_suffix='"')
define u = Character("???", what_prefix='"', what_suffix='"')


# Declare all background images here
image bg room = im.Scale("bgroom.png", 1366, 768)
image bg library = im.Scale("bglibrary.png", 1366, 768)
image bg gym = im.Scale("bggym.png", 1366, 768)
image bg classroom = im.Scale("bgclassroom.png", 1366, 768)
image bg museum = im.Scale("bgmuseum.png", 1366, 768)
image bg arcade = im.Scale("bgarcade.png", 1366, 768)
image bg movies = im.Scale("bgmovies.png", 1366, 768)
image bg stadium = im.Scale("bgstadium.png", 1366, 768)
image bg rave = im.Scale("bgrave.png", 1366, 768)
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

#Declare all mariana images here
image mariana standing = im.Scale("marianaidle.png", 504, 600)
image mariana evasive = im.Scale("marianaevasive.png", 504, 600)
image mariana sad = im.Scale("marianasad.png", 504, 600)
image mariana mad = im.Scale("marianamad.png", 504, 600)
image mariana excited = im.Scale("marianaexcited.png", 504, 600)
image mariana blushed = im.Scale("marianablushed.png", 504, 600)
image mariana happy = im.Scale("marianahappy.png", 504, 600)
image mariana cell = im.Scale("marianacell.png", 390, 670)

image professor = im.Scale("professor.png", 504, 600)

#Declare all rafaela images here
image rafaela standing = im.Scale("Rafaela.png", 1365, 840)
image rafaela happy = im.Scale("Rafaela_sorrindo.png", 1365, 840)
image rafaela sad = im.Scale("Rafaela_triste.png", 1365, 840)
image rafaela upset = im.Scale("Rafaela_irritada.png", 1365, 840)
image rafaela evasive = im.Scale("Rafaela_evasiva.png", 1365, 840)
image rafaela shy = im.Scale("Rafaela_envergonhada.png", 1365, 840)
image rafaela cell = im.Scale("rafaelacell.png", 390, 670)



#Variables of story decision

label checkInterlude(date):
    if nDatesSofia == 3 or nDatesMariana == 3 or nDatesRafaela == 3:
        if not ended:
            $ ended = True
            jump part2
        else:
            return
    else:
        jump expression date
    return

# The game starts here.

label start:

        #Variables need to be initialized here!!!
        $ nDatesSofia = 0
        $ nDatesMariana = 0
        $ nDatesRafaela = 0
        $ ended = False

        play music "sounds/song1.wav"

        #Só pro SSS
        #jump screenshotsaturday
        python:
            povname = renpy.input("Qual seu nome?")
            povname = povname.strip()

            if not povname:
                povname = "Protagonista-kun"

        call intro from _call_intro

        call checkInterlude("interlude1") from _call_checkInterlude

        call checkInterlude("interlude2") from _call_checkInterlude_1

        call checkInterlude("interlude3") from _call_checkInterlude_2

        call checkInterlude("interlude4") from _call_checkInterlude_3

        call checkInterlude("interlude5") from _call_checkInterlude_4

        call checkInterlude("goodEnding") from _call_checkInterlude_5

        return
