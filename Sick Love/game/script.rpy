# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    define p = Character("[povname]", color = "#e0e0e0", what_color = "#ffffff")
    
    python:
        povname = renpy.input("Qual seu nome?")
        povname = povname.strip()

        if not povname:
             povname = "João José"

    jump sofiafirstdate

    return
