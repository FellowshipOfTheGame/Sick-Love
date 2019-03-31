# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sofia", color = "#00b3f4", what_color = "#49daff",what_prefix='"', what_suffix='"')

define p = Character("Você", color = "#e0e0e0", what_color = "#ffffff",what_prefix='"', what_suffix='"')

# The game starts here.

label sofiafirstdate:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image bg room = im.Scale("bgroom.png", 1366, 768)
    image sofia standing = im.Scale("sofiaidle.png", 600, 800)

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Bem, já que não trouxe muita coisa comigo pro dormitório, acho que a melhor coisa que posso fazer pra passar o tempo é pegar um bom livro."

    "Será que aqui na biblioteca tem só livros técnicos? Seria bom se desse para pegar alguns livros mais divertidos às vezes..."

    "Olha só, aparentemente tem livros de ficção! Huuum... tem uma seção de terror também..."

    "Caramba, Lovecraft! Eu já vi alguns jogos que fazem referência aos livros dele... E uns memes na internet. Como chamava mesmo aquele monstro?"

    p "Huuum... aquele monstro famoso de Lovecraft..."

    s "Cthulhu?"

    p "Isso! Pera, oi?"

    show sofia standing

    s "*risos* Oi. Desculpa se te assustei."

    p "Não, relaxa. Eu não percebi que estava falando sozinho e assustei."

    # This ends the game.

    return
