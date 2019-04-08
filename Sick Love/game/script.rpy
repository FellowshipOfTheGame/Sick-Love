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

#Declare all characters images here
image sofia standing = im.Scale("sofiaidle.png", 975, 900)
image sofia happy = im.Scale("sofiahappy.png", 975, 600)
image sofia sad = im.Scale("sofiasad.png", 975, 600)
image sofia angry = im.Scale("sofiaangry.png", 975, 600)
image sofia crying = im.Scale("sofiacrying.png", 975, 600)
image sofia evasive = im.Scale("sofiaevasive.png", 975, 600)



# The game starts here.

label start:

    play music "sounds/song1.wav"
    
    python:
        povname = renpy.input("Qual seu nome?")
        povname = povname.strip()

        if not povname:
             povname = "Protagonista-kun"

    jump intro

    return
