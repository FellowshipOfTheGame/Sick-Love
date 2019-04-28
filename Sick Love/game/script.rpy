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

    jump sofiaseconddate

    jump intro

    return




#Pro SSS, só deixei aqui de referência
label screenshotsaturday:
    
    scene bg room
    with Fade(0.7,0.2,0.7)
    
    show sofia standing at noghost
    
    s "Olá, eu sou a Sofia! Uma das personagens do Sick Love!"
    
    scene bg classroom
    
    show sofia evasive at noghost
    
    s "Eu estudo aqui na universidade. Às vezes são tantas obrigações que quase não sobra tempo de fazer o que eu mais gosto..."
    
    scene bg library
    
    show sofia happy at noghost
    
    s "Que é ler! A biblioteca é o meu lugar favorito de toda a universidade! Eu amo todos os livros, mas tenho uma queda por livros de horror."

    s "Espero que você venha jogar Sick Love quando ele ficar pronto. Assim poderemos nos conhecer melhor!"
    
    s "{i}E terei você só pra mim...{/i}"
