# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sofia", color = "#00b3f4", what_color = "#49daff")

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
    
    "Falaram que era só atravessar a praça, subir umas escadas, seguir reto e procurar um prédio cheio de janelas à direita, para chegar na biblioteca."
    
    "Huuum... acho que é aquele prédio ali. Uau! Que prédio grande! Deve ser umas 5 vezes maior que a biblioteca da minha escola."
    
    "Caramba, qual o problema do pessoal dessa universidade que não coloca placas com direções e nem com o nome dos prédios em um lugar visível?"
    
    "Quando me falaram que a universidade era um lugar que amadurece as pessoas eu não imaginei que parte do amadurecimento era aprender a adivinhar onde ficam coisas má sinalizadas..."
    
    "É aqui mesmo. Ufa! Beleza, agora é sair procurando o que tem em cada seção."
    
    "Caramba! Quanto livro de cálculo. Deve ter livro aqui de uns 100 anos... Tenho dó de quem tem rinite."
    
    "*suspiro* Pior que o professor já passou lista de exercício. E mal começaram as aulas... Preciso ver depois quais os livros que ele vai usar e reservar aqui."
    
    "Tem uma seção só de publicação científica. Será que alguém pega pra ler algo daqui?"
    
    "Olha só, aparentemente tem livros de ficção! Finalmente encontrei o que eu procurava. Hum..."
    
    "\"Senhor dos Anéis\" eu já tentei ler. Mas aquelas árvores genealógicas infinitas e dezenas de páginas descrevendo toda a família de cada personagem novo me desanimaram."
    
    "Os filmes são mto bons, pelo menos..."
    
    "\"Eu, Robô\" é bem legal. Eu gosto bastante das discussões filosóficas sobre tecnologia do Asimov."
    
    "\"A Torre Negra\"... Nossa, esse é bem legal, apesar de super grande com aqueles 7 volumes um maior que o outro... {i}Pera{/i}, se tem {i}King{/i} aqui eu to na seção de terror, então."
    
    "Nossa, tem terror aqui também, que inusitado. Nada como estudar numa universidade com cursos que estudam literatura."
    
    "Caramba, {i}Lovecraft{/i}! Eu lembro de alguns jogos que fazem referência aos livros dele. Pareciam bem aterrorizantes..."
    
    "... E tinham uns memes na internet sobre aquele monstro dele. Como chamava mesmo aquele monstro?"
    
    p "Huuum... aquele monstro famoso de Lovecraft..."
    
    p "Claudio? Cleber?"
    
    s "*risos* Cthulhu?"

    p "Isso! {i}Pera{/i}, oi?"

    show sofia standing

    s "*risos* Oi. Desculpa se te assustei. É que ouvi você murmurando e respondi por impulso."
    
    p "Não... Relaxa. Eu que não percebi que estava falando sozinho. Foi mal."
    
    p "E obrigado por me ajudar a lembrar. Eu {i}tava{/i} procurando algum livro legal e lembrei que eu já tinha ouvido falar bastante do {i}Lovecraft{/i}, mas não lembrava o nome do monstro."
    
    s "Fica tranquilo. Eu também falo sozinha às vezes. E não é como se você tivesse falado errado o nome dele."
    
    p "Como assim? Não é Cthulu, que nem você falou agora? Como que eu acertei falando Cleber?"
    
    s "É só uma brincadeira. O nome do monstro é impronunciável pelos humanos, então a gente nunca vai acertar o nome dele mesmo. Inclusive tem vários jeitos de falar e escreve o nome \"correto\"."
    
    s "Katulu, Kutulu, Tulu... Então no fim você não tá tão errado assim."
    
    p "Nossa. Você realmente entende do assunto"

    # This ends the game.

    return
