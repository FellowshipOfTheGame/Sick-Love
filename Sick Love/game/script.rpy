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

#Declare all characters images here
image sofia standing = im.Scale("sofia.png", 1365, 840)
image sofia happy = im.Scale("sofia_sorrindo.png", 1365, 840)
image sofia sad = im.Scale("sofia_triste.png", 1365, 840)
image sofia angry = im.Scale("sofia_braba.png", 1365, 840)
image sofia crying = im.Scale("sofia_chorando.png", 1365, 840)
image sofia evasive = im.Scale("sofia_evasiva.png", 1365, 840)
image sofia upset = im.Scale("sofia_irritada.png", 1365, 840)
image sofia shy = im.Scale("sofia_envergonhada.png", 1365, 840)

transform noghost:
    xalign 0.5
    yalign -0.9

define m = Character("Mariana", color = "#c23ed1", what_color = "#ba38c9",what_prefix='"', what_suffix='"')

define b = Character("Bruno", color = "#db8181", what_color = "#ce7575",what_prefix='"', what_suffix='"')

define d = Character("Diego", color = "#ceb282", what_color = "#bfa57a",what_prefix='"', what_suffix='"')

image bg classroom = im.Scale("bgclassroom.png", 1366, 768)
image mariana standing = im.Scale("marianaidle.png", 600, 800)
image mariana evasive = im.Scale("marianaevasive.png", 600, 800)
image mariana sad = im.Scale("marianasad.png", 600, 800)
image mariana excited = im.Scale("marianaexcited.png", 600, 800)


# The game starts here.

label start:

        play music "sounds/song1.wav"

        #Só pro SSS
        #jump screenshotsaturday
        python:
            povname = renpy.input("Qual seu nome?")
            povname = povname.strip()

            if not povname:
                povname = "Protagonista-kun"

        jump intro

        return
